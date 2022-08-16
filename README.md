# projcarpvn

## Tham gia vào project

### Cài đặt các công cụ cơ bản
```
git
python
Visual Studio Code và và một số extension trên VS Code (optional theo thứ tự ưu tiên giảm dần) như:
- Python
- Pylance
- HTML Boilderplate
- Auto Rename Tag
- Docker
- Database Client
```

### Clone repo và chạy lại virtual environment
#### Trên Linux/MacOS
Vào thư mục làm việc
```
% cd work/python 
```
Clone code về
```
% git clone https://github.com/tant/projcarpvn.git
Cloning into 'projcarpvn'...
remote: Enumerating objects: 13396, done.
remote: Counting objects: 100% (1620/1620), done.
remote: Compressing objects: 100% (1138/1138), done.
remote: Total 13396 (delta 540), reused 1036 (delta 476), pack-reused 11776
Receiving objects: 100% (13396/13396), 60.69 MiB | 10.12 MiB/s, done.
Resolving deltas: 100% (3498/3498), done.
```
Vào thư mục code
```
% cd projcarpvn 
```
Chạy lệnh tạo virtual environment
```
% python3 -m venv .venv
```

#### Trên Windows 
Hình như chỉ khác dấu nhắc :)

### Chạy VS Code và mở thử mục projcarpvn ra 
Đảm bảo khi mở Terminal/New Terminal phải thấy môi trường ảo được kích hoạt như ví dụ bên dưới
```
source /Users/tantran/work/python/projcarpvn/.venv/bin/activate
tantran@mbam1 projcarpvn % source /Users/tantran/work/python/projcarpvn/.venv/bin/activate
(.venv) tantran@mbam1 projcarpvn % 
```