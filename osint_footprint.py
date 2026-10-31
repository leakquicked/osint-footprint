import argparse,json,re
from pathlib import Path
RULES=[["email","\\b[\\w.+-]+@[\\w.-]+\\.[A-Z]{2,}\\b","info"],["url","https?://[^\\s<>]+","info"],["handle","(?<!\\w)@[A-Za-z0-9_]{2,32}\\b","info"]]
def analyze_text(text):
    findings=[]
    for rule,pattern,severity in RULES:
        for m in re.finditer(pattern,text,re.I):
            findings.append({"rule":rule,"severity":severity,"line":text.count("\\n",0,m.start())+1,"match":m.group(0)[:120]})
    return findings
def main():
    p=argparse.ArgumentParser(description="Identify manually supplied public-reference strings without scraping")
    p.add_argument("input",type=Path)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    if not a.input.is_file(): p.error("input file not found")
    report={"tool":"osint-footprint","count":0,"findings":analyze_text(a.input.read_text(encoding="utf-8",errors="replace"))}
    report["count"]=len(report["findings"])
    data=json.dumps(report,indent=2,ensure_ascii=False)
    if a.output: a.output.write_text(data+"\\n",encoding="utf-8")
    print(data)
if __name__=="__main__": main()
