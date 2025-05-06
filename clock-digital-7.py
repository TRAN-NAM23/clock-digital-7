
#các bạn lưu ý cài lệnh pip install ntplib đồng bộ với internet

from tkinter import *
from tkinter import font
from time import strftime
import time
import os

root = Tk()
root.title("Digital Clock Pro")
root.configure(background='black')

# Tạo font Digital-7 (nếu có) hoặc dùng font dự phòng
try:
    # Kiểm tra xem font đã được cài đặt hệ thống chưa
    if "Digital-7" in font.families():
        digital_font = font.Font(family="Digital-7", size=80)
    else:
        # Thử tải từ file nếu có trong thư mục fonts
        font_path = os.path.join("fonts", "digital-7.ttf")
        digital_font = font.Font(family="Digital-7", size=80, file=font_path)
except:
    # Font dự phòng nếu không tìm thấy Digital-7
    digital_font = font.Font(family="Courier New", size=80)

# Tạo label hiển thị đồng hồ
label = Label(root,
              font=digital_font,
              background='black',
              foreground='#00FF00')  # Màu xanh lá điện tử
label.pack(anchor='center', expand=True)


def clock():
    # Hiệu ứng nhấp nháy dấu hai chấm
    if int(time.strftime('%S')) % 2 == 0:
        time_format = '%H:%M:%S'
    else:
        time_format = '%H %M %S'

    # Lấy giờ hệ thống chính xác
    current_time = strftime(time_format + ' %p')

    # Cập nhật giao diện
    label.config(text=current_time)

    # Kiểm tra đồng bộ thời gian mỗi phút
    if int(time.strftime('%S')) == 0:
        label.config(foreground='yellow')  # Đổi màu khi đồng bộ
    else:
        label.config(foreground='#00FF00')

    # Tiếp tục cập nhật
    label.after(1000, clock)


# Bắt đầu chạy đồng hồ
clock()

# Hiển thị ngày tháng
date_label = Label(root,
                   font=('Arial', 20),
                   background='black',
                   foreground='white')
date_label.pack(side='bottom')


def update_date():
    date_str = strftime('%A, %d %B %Y')
    date_label.config(text=date_str)
    root.after(60000, update_date)  # Cập nhật mỗi phút


update_date()

# Tùy chỉnh kích thước cửa sổ
root.geometry("800x400")
root.resizable(True, True)

root.mainloop()