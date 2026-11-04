# Pixl Cafe

A retro console-based ordering system for the Pixl Cafe featuring ASCII art, dynamic split-screen dashboard, real-time order tracking, and an interactive ordering chat.

## Features

- **ASCII Art Menu & Dashboard**: Left side displays the drinks and food menu alongside ASCII artwork; the right side shows an active orders table.
- **Auto-Refreshing Screen**: When idle, the console clears and refreshes every few seconds to update order countdowns.
- **Non-Blocking Wait**: Uses keyboard detection to allow real-time background updates without locking up the terminal.
- **Ordering Chat**: Stays at the bottom. When you press Enter, auto-refresh pauses so you can place orders without the screen clearing mid-sentence.
- **Sand Grains Currency**: Calculates the total price in Sand Grains.
- **Order Tracking**: Assigns order numbers and counts down preparation time until ready.

## Requirements

- Python 3.8+
- Windows OS (uses the built-in `msvcrt` module for non-blocking key detection)

## How to Run

```bash
python order.py
```

## How to Use

1. Run the script to see the cafe menu and active orders board.
2. Press **Enter** to open ordering mode.
3. Type the item numbers separated by spaces (e.g. `1 10 13`).
4. Choose whether to add more items or complete your order.
5. Watch your order appear on the live order board with its preparation countdown!

