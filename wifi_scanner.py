import pywifi
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first wireless interface

    iface.scan()  # Trigger a scan
    time.sleep(2)  # Wait for the scan to complete

    results = iface.scan_results()

    print("Available Wi-Fi networks:")
    for result in results:
        print(f"SSID: {result.ssid}, Signal Strength: {result.signal}")

if __name__ == "__main__":
    scan_wifi()
