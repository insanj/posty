# posty

[![Build Status](https://travis-ci.com/insanj/posty.svg?token=esypzNUpVoxWgx65pRhC&branch=master)](https://travis-ci.com/insanj/posty)
[![](https://img.shields.io/badge/language-python3.5-4dbdd1.svg)](https://github.com/insanj/posty/search?l=python)
![](https://img.shields.io/badge/package--manager-conda-edcb47.svg)
[![](https://img.shields.io/aur/license/yaourt.svg?style=popout)](LICENSE)

🍴 A fun tool to scrape and sort [Postmates](https://postmates.com)

## Usage

`make run`

Posty will launch a bot-controlled Chrome instance and scrape various Postmates pages using the config provided by the Python class [PostyUser](https://github.com/insanj/posty/blob/master/src/posty.py#L17). The following attributes are customizable:

- Address
- Feed (Home page, Category page, etc)

Using these fields, ideally Posty can:

- Sort restaurants (price, distance, name)
- Scrape various feeds and/or addresses and aggregate content
- Easily display rich data and deeplink into restaurant sites

## Installation

Posty uses [Conda](https://conda.io/) to manage the Python environment. Use the provided [Makefile](src/Makefile) to automatically configure the setup for production. Examples of setting up a Linux workspace from scratch are also in the Make recipes.

To manually setup dependencies, install Python 3+ and use Pip to ensure Selenium is installed ([Linux & Windows webdrivers included](https://github.com/insanj/posty/tree/master/src/drivers)).

## Examples

```
Running Posty v1!! Here are all the restaurants I found nearby...

- Chipotle Mexican Grill $3.99 Delivery · 30-45 min 69 added to favorites
- 7-Eleven $3.99 Delivery · 30-45 min
- Thang Long Pho $3.99 Delivery · 30-45 min
- The Igloo Frankford $3.99 Delivery · 25-40 min
- Snap Kitchen $3.99 Delivery · 30-45 min
- Campus Pizza $3.99 Delivery · 30-45 min
- Pancho's Cafe $3.99 Delivery · 40-55 min
- Mood Indian Restaurant $4.99 Delivery · 30-45 min
- Kostas $3.99 Delivery · 30-45 min
- Alamodak Restaurant $3.99 Delivery · 35-50 min
- Pita Chip $4.99 Delivery · 25-40 min
- Tiffin Indian Cuisine $3.99 Delivery · 40-55 min
- Lee's Hoagies $4.99 Delivery · 30-45 min
- Del Rossi's Cheesesteak Co $3.99 Delivery · 45-60 min
- Golden Cuisine $4.99 Delivery · 30-45 min
- City Gourmet Market &amp; Deli $3.99 Delivery · 35-50 min
- Apricot Stone $3.99 Delivery · 30-45 min
- Love Park Pizza and Chicken $4.99 Delivery · 30-45 min
- Pho Don $3.99 Delivery · 30-45 min
- Pho 20 $4.99 Delivery · 30-45 min 57 added to favorites
- Kopi Latte $3.99 Delivery · 35-50 min
- Sang Kee Peking Duck House $3.99 Delivery · 45-60 min
- Saffron $3.99 Delivery · 40-55 min
- Brandywine Tratoria &amp; Pizza $3.99 Delivery · 45-60 min
- Torch - Wood Cafe $4.99 Delivery · 40-55 min
- Philly Poke $3.99 Delivery · 25-40 min
- Angry Deekin Ribs $3.99 Delivery · 35-50 min
- Temple Town Pizza $3.99 Delivery · 40-55 min
- Vietnam Palace $4.99 Delivery · 30-45 min
- East Coast Wings + Grill $3.99 Delivery · 45-60 min
- Indian Restaurant 722 $3.99 Delivery · 35-50 min
- John's Place $3.99 Delivery · 35-50 min
- Kurry Korner $3.99 Delivery · 30-45 min
- Miu Cha $3.99 Delivery · 40-55 min
- Khmer Grill $3.99 Delivery · 40-55 min
- Inspired Brews $3.99 Delivery · 40-55 min
- I CE NY $3.99 Delivery · 40-55 min
- Available LaterLil Lina's Slices &amp; ScoopsOffline
- Available LaterEatalia BYOBOffline
- Available LaterQuick StopOffline
- Available LaterTK Homestyle CookingOffline
- Available LaterHeffeOffline
- Available LaterSoul D'lysh Offline
- Available LaterEl Guaco LocoOffline
- Available LaterOhh Lala SaladOffline
- Available LaterWedge + FigOffline
See ya next time!
```

## License

insanj/posty is licensed under the GNU General Public License v3.0

[See LICENSE](LICENSE).


## Author

[Julian @insanj Weiss](https://github.com/insanj), 2018
