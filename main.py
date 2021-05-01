import pyautogui, time
# atur lama mulainya sesuai waktu yang dibutuhin untuk pindah ke halaman yang akan
# kalian spam, misal buka line butuh 20 detik ya set dlu jadi 20 biar kalian bisa
# bukan line sebelum botnya ngespam
time.sleep(1)
for i in range(20):
  pyautogui.typewrite("Enter the sentence u want me to spam")
  pyautogui.press("enter")
