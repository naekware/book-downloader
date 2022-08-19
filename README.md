# LibGen Parser

A command line tool to get the direct download links of books from libgen.

## Quick Start

```
naek@naekware:~/Code/book-downloader$ python3 lgparser.py -q "ayn rand"
= == naek libgen parser == = 
====================
Book: Leonard Peikoff /   / djvu / http://library.lol/main/C94F579F87ACC84EAF3D6B349827CCF0
Download: http://62.182.86.140/main/112000/c94f579f87acc84eaf3d6b349827ccf0/%28The%20Ayn%20Rand%20Library%2C%20Volume%206%29%20Leonard%20Peikoff%20-%20Objectivism_%20the%20philosophy%20of%20Ayn%20Rand-Plume%20%281993%29.djvu
====================
Book:  /   / pdf / http://library.lol/main/A2B08C3777782854BC1654F68E3FDED0
Download: http://62.182.86.140/main/272000/a2b08c3777782854bc1654f68e3fded0/Dr.%20Albert%20Ellis%20-%20Are%20Capitalism%2C%20Objectivism%2C%20And%20Libertarianism%20Religions_%20Yes%21_%20Greenspan%20And%20Ayn%20Rand%20Debunked-CreateSpace%20%282007%29.pdf
====================
Book: Jennifer Burns /   / pdf / http://library.lol/main/79FC54DA4CB96AC4D47BC2C533AC4B4C
Download: http://62.182.86.140/main/306000/79fc54da4cb96ac4d47bc2c533ac4b4c/Jennifer%20Burns%20-%20Goddess%20of%20the%20Market_%20Ayn%20Rand%20and%20the%20American%20Right-Oxford%20University%20Press%2C%20USA%20%282009%29.pdf
```

Can also pass a `--num/-n` parameter to change the amount of results you get. Example is `python3 lgparser.py -n 100 -q "ayn rand"`.
