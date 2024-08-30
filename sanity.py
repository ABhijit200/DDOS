from monkeyrun import run
import time

# Connect to the device
device = monkeyrun.waitForConnection()

# Function to simulate a phone call
def simulate_call():
    device.startActivity(component="com.android.dialer/com.android.dialer.DialtactsActivity")
    monkeyrun.sleep(2)
    device.touch(100, 1000, 'DOWN_AND_UP')  # Adjust coordinates as needed for the dial pad
    device.touch(100, 1000, 'DOWN_AND_UP')
    device.touch(100, 1000, 'DOWN_AND_UP')
    device.press('KEYCODE_CALL', 'DOWN_AND_UP')
    monkeyrun.sleep(10)
    device.press('KEYCODE_ENDCALL', 'DOWN_AND_UP')

# Function to simulate sending a message
def simulate_message():
    device.startActivity(component="com.android.mms/com.android.mms.ui.ConversationList")
    monkeyrun.sleep(2)
    device.touch(500, 1800, 'DOWN_AND_UP')  # Adjust coordinates as needed for "New Message" button
    device.type("Test message")
    device.press('KEYCODE_BACK', 'DOWN_AND_UP')

# Function to simulate internet surfing
def simulate_internet_surfing():
    device.startActivity(component="com.android.chrome/com.google.android.apps.chrome.Main")
    monkeyrun.sleep(5)
    device.type("https://www.example.com")
    device.press('KEYCODE_ENTER', 'DOWN_AND_UP')
    monkeyrun.sleep(10)
    device.drag((300, 1000), (300, 200), 0.5, 10)  # Scroll down
    monkeyrun.sleep(2)

# Main test sequence
print("Starting device sanity test...")

print("Testing phone call...")
simulate_call()

print("Testing messaging...")
simulate_message()

print("Testing internet surfing...")
simulate_internet_surfing()

print("Device sanity test completed.")