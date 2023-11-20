"""Demo for using f451 Labs E-Paper Module."""

import time
from f451_epaper.wave_epd27b import EPD27b


# =========================================================
#                    D E M O   A P P
# =========================================================
def main():
    # Initialize device instance which includes all sensors
    # and LED display on Sense HAT
    epd27b = EPD27b({
        "ROTATION": 0,
        "DISPLAY": 0,
        "PROGRESS": 0,
        "SLEEP": 600    
    })

    # Skip display demos if we're using fake HAT
    if not epd27b.is_fake():
        epd27b.display_init()

        # Display text on 8x8 LED
        epd27b.display_message("Hello world!")

        for _ in range(100):
            epd27b.display_sparkle()
            time.sleep(0.2)

        epd27b.display_blank()
        epd27b.display_off()

    else:
        print("\nSkipping LED demo since we don't have a real Sense HAT")

    # Get enviro data, even if it's fake
    tempRaw = round(epd27b.get_temperature(), 1)
    pressRaw = round(epd27b.get_pressure(), 1)
    humidRaw = round(epd27b.get_humidity(), 1)

    print("\n===== [Demo of f451 Labs Enviro+ Module] ======")
    print(f"TEMP:     {tempRaw} C")
    print(f"PRESSURE: {pressRaw} hPa")
    print(f"HUMIDITY: {humidRaw} %")
    # print("Beep boop!")
    print("=============== [End of Demo] =================\n")


if __name__ == "__main__":
    main()