# src_template
作成中

pycacheを消すとき
```cmd
Get-ChildItem -Directory -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force
```