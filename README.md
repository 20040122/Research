远程有readme的main分支，默认本地为最新
```
git init
git branch -m master main
git remote add origin https://github.com/你的用户名/Research.git
git fetch origin
git reset --hard origin/main

git add .
git commit -m "更新"
git push -u origin main --force
```
