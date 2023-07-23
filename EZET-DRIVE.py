K=None
J=open
I=Exception
D=True
B=print
import os as A,time,importlib as O
P=['requests','tqdm']
def Q(packages):
	C=[]
	for D in packages:
		try:O.import_module(D)
		except ImportError:C.append(D)
	if C:B('Required packages not found. Installing...');A.system(f"pip install {' '.join(C)}");B('Packages installed successfully.')
Q(P)
import requests as L
from urllib.parse import urlparse,parse_qs,unquote as R
from tqdm import tqdm
def S(url):
	D='id=';C='file/d/';A=url
	if'drive.google.com'not in A:return
	B=K
	if C in A:B=A.split(C)[-1].split('/')[0]
	elif D in A:B=A.split(D)[-1].split('&')[0]
	if B:return f"https://drive.google.com/uc?id={B}"
	else:return
def T(url):
	B='Content-Disposition';A=L.head(url,allow_redirects=D)
	if B in A.headers:C=A.headers[B];E=C.split(';')[1].split('filename=')[1].strip('\'"');return R(E)
	else:return
def U(filename,output_dir):
	D=output_dir;C=filename;B=A.path.join(D,C);F,G=A.path.splitext(C);E=1
	while A.path.exists(B):B=A.path.join(D,f"{F}_{E}{G}");E+=1
	return B
def V(url,output_dir='.'):
	try:
		C=S(url)
		if C is K:raise I('Failed to convert URL to direct download link.')
		F=T(C)
		if F is K:raise I('Failed to retrieve the filename from the URL.')
		G=U(F,output_dir);E=L.get(C,stream=D);E.raise_for_status();M=int(E.headers.get('content-length',0))
		with J(G,'wb')as N,tqdm(total=M,unit='B',unit_scale=D,unit_divisor=1024)as O:
			for H in E.iter_content(chunk_size=8192):N.write(H);O.update(len(H))
		B(f"Downloaded: {A.path.basename(G)}");return D
	except I as P:B(f"Error downloading {url}: {P}");return False
def W():A="\n             _          _     _                     \n  ___ ______| |_ ___ __| |_ _(_)_ _____   _ __ _  _ \n / -_)_ / -_)  _|___/ _` | '_| \\ V / -_)_| '_ \\ || |\n \\___/__\\___|\\__|   \\__,_|_| |_|\\_/\\___(_) .__/\\_, |\n                                         |_|   |__/ \n\n\n    ";A+='\nWelcome to EZET-DRIVE.py';A+='\nSupport me by following @fidho_redana on insta!\n';B(A)
if __name__=='__main__':
	W();X='url.txt';E='Downloads';Y='failed_url.txt';M=3
	if not A.path.exists(E):A.makedirs(E)
	with J(X,'r')as F:Z=F.readlines()
	G=[]
	for C in Z:
		C=C.strip()
		if not C:continue
		H=0
		while H<M:
			N=V(C,E)
			if N:break
			H+=1;B(f"Retrying ({H}/{M})...");time.sleep(1)
		if not N:G.append(C)
	if len(G)==0:B("The downloaded files are stored in the 'Downloads' folder.")
	else:
		B('Failed download URLs are listed in failed_url.txt')
		with J(Y,'w')as F:
			for C in G:F.write(C+'\n')
