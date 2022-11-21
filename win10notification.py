from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast(
    "แจ้งเตือน",
    "เขียนได้ง่ายนิดเดียว",
    duration = 20,
    threaded = True,
)