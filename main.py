# inget di import dulu
import pyautogui, time, emoji, pyperclip

# atur lama mulainya sesuai waktu yang dibutuhin untuk pindah ke halaman yang akan
# kalian spam, misal buka line butuh 20 detik ya set dlu jadi 20 biar kalian bisa
# bukan line sebelum botnya ngespam
time.sleep(1)

text = "Testing emoji: " + emoji.emojize(":red_heart:")
pyperclip.copy(text)

for i in range(5):
  # emoji harus di paste dari clipboard
  pyautogui.hotkey("ctrl", "v")
  pyautogui.press("enter")

  # text biasa bisa di typewrite kek gini
  pyautogui.typewrite("Spam")
  pyautogui.press("enter")
