import time, datetime, requests, json, os, re
try:
    import os, sys, time, datetime, random, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from time import sleep
except ImportError:
    os.system('pip2 install requests')
    os.system('pip install requests')
    time.sleep(1)
d = '\x1b[1;91m'
xl = '\x1b[1;92m'
v = '\x1b[1;93m'
xb = '\x1b[1;96m'
t = '\x1b[1;97m'
vio = '\x1b[1;95m'
os.system('clear')
time.sleep(1)
banner="""
\033[1;92m          ████████╗██████╗ ███████╗
\033[1;93m          ╚══██╔══╝██╔══██╗██╔════╝
\033[1;96m             ██║   ██║  ██║███████╗
\033[1;92m             ██║   ██║  ██║╚════██║
\033[1;93m             ██║   ██████╔╝███████║
\033[1;96m             ╚═╝   ╚═════╝ ╚══════╝
\033[1;97m              Tool TDS Python bản free
\033[1;97m               Supporter > Axeyed Kha
"""
f = "-----------------------------------------------------------------"
icon = "\033[1;91m[\033[1;92m•\033[1;91m]"
icon1 = "\033[1;91m[\033[1;92m✓\033[1;91m]"
bang = """
\033[1;97m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃\033[1;93m ➩ Nhập [1] Job like                         \033[1;97m ┃
┃\033[1;93m ➩ Nhập [2] Job Follow(Giới hạn)            \033[1;97m  ┃
┃\033[1;93m ➩ Nhập [3] Job Comment(Giới hạn)            \033[1;97m ┃
┃\033[1;93m ➩ Nhập [4] Job Share(Giới hạn)              \033[1;97m ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
#menu
def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def menu():
  os.system('clear')
  print(xb+"Đang vào tool, chúc ngày mới cày xu tốt")
  time.sleep(3)
  os.system('clear')
  print(banner)
  print("\033[1;92mSupporter:"+"\033[1;97mAxeyed Kha")
  print(f)
  print(icon+vio+"Tool TDS Bản Miễn Phí Thử Nghiệm")
  print(icon+xl+"Bản quyền by Dũng")
  print(icon+v+"Cần thuê tool hay có vấn đề về tool ib zalo: 0936485851")
  print(f)
  print(icon+xb+"Cấp độ: FREE")
  print(icon+xl+"Tên chủ key: UNKNOWN")
  print(f)
  print(xb+"Thông báo: Sắp có tool TDS python bản VIP full nhiệm vụ, key riêng chỉ 10k/tháng ")
  print(f)
  print(icon1+v+"Tool Trao Đổi Sub")
  print(f)
  print(bang)
  print(f)
  ls = input(icon+xl+"Nhập số: ")
  if ls == '01' or ls == '1':
    tool_like_function()
  elif ls == '02' or ls == '2':
    tool_follow_function()
  else:
    print(d+"Ghi sai rồi!!!")
    time.sleep(3)
    os.system('clear')
def tool_like_function():
  os.system('clear')
  print(banner)
  print(f)
  print(v+"Job bạn chọn: Like")
  tokentds = input(icon+xl+"Nhập token TDS: ")
  time.sleep(1)
  log = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
  if 'success'in log:
    user=log['data']['user']
    xu=log['data']['xu']
    print(f) 
    print(xl+"Đăng nhập thành công")
  else:
    print(d+"Nhập sai")
    os.system('clear')
  print(f) 
  write(v+"Tên tài khoản: "+user)
  write(v+"Xu trong tài khoản: "+xu)
  print(f)
  tokenfb = input(icon+xl+"Nhập token facebook: ")
  dl=int(input(xb+"Time Delay >> "))
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
    try:
           getlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+tokentds)
    
           idlike=getlike.json()[0]['id']
           urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
           datalike="access_token="+tokenfb
           like=requests.post(urllike, data=datalike)
           nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+tokentds).text)
           id=idlike[0:15]
           if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m LIKE >\x1b[1;95m {id} >\x1b[1;93m +300 >\x1b[1;97m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Làm job tiếp sau -->   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
           else:
                print(d+'Lỗi '+id,end='\r')
    except:
            for a in range(5, -1, -1):
                print(icon+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
                sleep(1)
menu()
