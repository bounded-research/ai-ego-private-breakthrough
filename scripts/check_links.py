from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,re,json
r=Path(__file__).resolve().parents[1]
urls=set(re.findall(r'https://[^\s)<>]+',(r/'ARTICLE.md').read_text()))
def check(u):
 try:
  x=requests.get(u,timeout=30,headers={'User-Agent':'Mozilla/5.0 (publication source link check)'},stream=True)
  out={'url':u,'status':x.status_code,'final_url':x.url,'content_type':x.headers.get('content-type','')};x.close();return out
 except requests.RequestException as e:return {'url':u,'status':None,'error':type(e).__name__}
results=list(ThreadPoolExecutor(6).map(check,sorted(urls)))
(r/'checks/LINK-CHECKS.json').write_text(json.dumps(results,indent=2)+'\n')
for row in results:print(row['status'],row['url'])
