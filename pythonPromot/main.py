import requests
from pathlib import Path
# 图片的URL
file_url = 'https://www.brantect.com/uapi/files/operation'

# 定义保存的文件名

headers_raw = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie':'_ga=GA1.2.29204228.1713929507; _gid=GA1.2.1213211104.1713929507; visitor_id959492=228098271; visitor_id959492-hash=fd34074ed63a277f8709539f6f4578d3237b6412b891ac9fc4bf13de3e7d7707d3b6a2b774eae4f10ac23fca15bfac0a2ffd6f73; SCROLL_TOP_TAGNO_1=82; brantect_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQxMTYzNTIsImlhdCI6MTcxNDAyOTk1MiwibG9nX29uX25tIjoiIiwibmJmIjoxNzE0MDI5OTUyLCJzZXNzaW9uX2lkIjoiOTY0ZTU0YzAtNDdmZC00OWIxLThhMTQtZDM0MGZjMzM5NWY3In0.bEHe580cNSLGFArvvsU0OLoIXJex_UIqSJ3SeVJ-8AABZv05-MJ-JWn3RrYBZstlIq-v3r8-7lzwDgDxqqwysOeVyDx7v3hbg7heo1RvQceWjyNxPmvvpBdt2ruzMPomPDvO0WxprPcv5fjHDcTtaBdoXGcyMBRewVlYtUjNtUA32WidS4RlwvsAEUSuVuIfmhIUG90fw1B-PO7b4mpvvp1QL9UbrZbgJlZRTJY4Jn3h1ydb90Y3is44lVzGGrMeWCY499OYR5g0dN7CXVV51DG7BvF2Gj3naz-iBUNWFHRZOmNisxVeEjAaSlnbJCUPGontWnZfU9XsW7Vb2Mys9A; PHPSESSID=d536dddd9edddf87aea48fef29782aa1; _gat=1; _ga_V5DD0RPQDB=GS1.2.1714029211.9.1.1714029968.60.0.0',
        'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQxMTYzNTIsImlhdCI6MTcxNDAyOTk1MiwibG9nX29uX25tIjoiIiwibmJmIjoxNzE0MDI5OTUyLCJzZXNzaW9uX2lkIjoiOTY0ZTU0YzAtNDdmZC00OWIxLThhMTQtZDM0MGZjMzM5NWY3In0.bEHe580cNSLGFArvvsU0OLoIXJex_UIqSJ3SeVJ-8AABZv05-MJ-JWn3RrYBZstlIq-v3r8-7lzwDgDxqqwysOeVyDx7v3hbg7heo1RvQceWjyNxPmvvpBdt2ruzMPomPDvO0WxprPcv5fjHDcTtaBdoXGcyMBRewVlYtUjNtUA32WidS4RlwvsAEUSuVuIfmhIUG90fw1B-PO7b4mpvvp1QL9UbrZbgJlZRTJY4Jn3h1ydb90Y3is44lVzGGrMeWCY499OYR5g0dN7CXVV51DG7BvF2Gj3naz-iBUNWFHRZOmNisxVeEjAaSlnbJCUPGontWnZfU9XsW7Vb2Mys9A'
}

path = '/00000011980/tm/task_at/4744.pdf'

req_data = {
            "method":"GET",
            "server":"db10",
            "path": "/00000011980/tm/task_at/3328.pdf"
        }

filename = path.rsplit('/', 1)[-1]

# 发送GET请求获取图片内容
response = requests.get(file_url, stream=True, headers = headers_raw, params=req_data)
print(response.status_code)
open(f'.\imgs\{filename}','wb').write(response.content)