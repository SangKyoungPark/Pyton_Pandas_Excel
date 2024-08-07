가상환경 : 필요한 lib 가 설치된 방

가상환경 list 보기
```
conda env list
```
가상환경 접속
```
conda activate py2exe
```
가상환경 생성
```
conda create -n py3exe python=3.7
```
가상환경 로그아웃
```
conda deactivate
```

```
python to exe : 가상환경 접속 -> py 경로 접속 -> pyinstaller ~~~.py
```
---

[Pyinstaller Option]
```
pyinstaller ~~~~~.py -F -w
```
1) -F 가 1개의 파일로 묶는거고,
2) -w 는 콘솔을 없게 파일을 배포
