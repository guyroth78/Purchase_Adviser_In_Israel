# מפרט לפטופ בקטלוג (טיוטה 3)

ארבעה קבצי נתונים: `laptops.json` (רשומות הלפטופים), `brands.json`, `cpus.json` ו-`gpus.json` (טבלאות סטטיות שהלפטופים מפנים אליהן). בשלב 2 יתווסף קובץ הצעות (`offers`): חנות, `laptop_id`, מחיר, `url`.

## עקרונות

1. **עובדות בלבד.** אין בקטלוג ציוני התאמה. ה-Skill גוזר אותם מהמפרט.
2. **שדה חסר ≠ ערך שלילי.** אם לא ידוע, השדה מושמט (או `null`). לעולם לא מנחשים.
3. **שדות חובה = מה שנחוץ כדי לסנן ולהשוות.**
4. **יחידות קבועות בשם השדה** (`_gb`, `_in`, `_kg`, `_wh`, `_nits`, `_hz`).
5. **ערכים מוגדרים (enum)** איפה שאפשר.
6. **הפניות במקום טקסט חופשי:** מותג, CPU ו-GPU מפנים לטבלאות לפי מזהה.
7. **הקטלוג הוא עדיפות ראשונה, לא גבול.** ה-Skill מחפש קודם בקטלוג. מה שחסר שם (דגם, שדה או מעבד), הוא משלים בחיפוש ברשת. כל ערך שהגיע מהרשת מסומן כך בהערות הדף, עם תאריך. הקטלוג לא מחליף את המחקר, אלא חוסך אותו כשהנתון כבר קיים.

## רמה 1: חובה (בלפטופ)

| שדה | סוג | הערה |
|---|---|---|
| `id` | string | מזהה ייחודי, באנגלית, ללא רווחים |
| `brand_id` | string | הפניה ל-`brands.json` |
| `name` | string | שם הדגם כפי שמופיע ביצרן |
| `price` | number | מחיר ברירת מחדל לדגם, במטבע הקובץ. בשלב 2 `offers` יכולות לעקוף אותו |
| `price_checked` | date `YYYY-MM-DD` | מתי נבדק `price` |
| `cpu_id` | string | הפניה ל-`cpus.json` |
| `ram_gb` | number | |
| `storage_gb` | number | קיבולת כוללת |
| `screen_in` | number | אלכסון באינץ' |
| `os_included` | boolean | האם מערכת הפעלה כלולה במחיר |
| `warranty_years` | number | |

## רמה 2: מומלץ (בלפטופ)

| קבוצה | שדה | סוג / ערכים |
|---|---|---|
| זיהוי | `sub_brand_id` | הפניה לתת-מותג בתוך המותג (למשל ThinkPad תחת Lenovo) |
| | `sku` | מק"ט יצרן מדויק |
| | `spec_url` | דף המפרט הרשמי |
| | `year` | שנת השקה |
| מערכת | `os` | `windows11` / `windows11pro` / `none` / `linux` / `chromeos` / `macos` |
| זיכרון | `ram_max_gb` | number |
| | `ram_type` | `DDR4` / `DDR5` / `LPDDR5` / `LPDDR5X` |
| | `ram_upgradable` | `soldered` / `slot` / `partial` |
| אחסון | `storage_type` | `NVMe` / `SATA_SSD` / `HDD` / `eMMC` |
| | `storage_slots_free` | number |
| מסך | `resolution` | `"1920x1200"` |
| | `panel` | `IPS` / `OLED` / `TN` / `VA` |
| | `brightness_nits` | number |
| | `refresh_hz` | number |
| | `touch`, `matte` | boolean |
| גרפיקה | `gpu_id` | הפניה ל-`gpus.json` |
| סוללה ומשקל | `battery_wh`, `weight_kg` | number |
| **רשת** | `network` | אובייקט, ראו למטה |
| **פורטים** | `ports` | אובייקט, ראו למטה |
| קלט | `keyboard_backlit`, `keyboard_numpad`, `keyboard_hebrew` | boolean |
| אחריות | `warranty_type` | `onsite` / `carry-in` / `pickup` |
| | `warranty_provider` | `maker` / `importer` / `store` |

### פורטים מול ממשק רשת

הם לא אותו דבר, אז הפרדתי:
- **`ports`** = מחברים פיזיים שמחברים אליהם כבלים או התקנים: USB-C, USB-A, HDMI, שקע אוזניות, קורא כרטיסים.
- **`network`** = דרכי התחברות לרשת: Wi-Fi, Bluetooth, כרטיס רשת קווי (שקע RJ45 שייך לכאן), סלולר.

```json
"ports": {
  "usb_c": [
    { "speed_gbps": 10, "power_delivery": true, "displayport": true, "thunderbolt": null }
  ],
  "usb_a": 2,
  "hdmi": "2.1",
  "sdcard": false,
  "headphone_jack": true
},
"network": {
  "wifi": "Wi-Fi 6E",
  "bluetooth": "5.3",
  "ethernet_mbps": 1000,
  "cellular": "none"
}
```

ערכים: `thunderbolt` = `null` / `3` / `4` / `5`; `wifi` = `Wi-Fi 5` / `6` / `6E` / `7`; `ethernet_mbps` = `null` אם אין שקע; `cellular` = `none` / `4G` / `5G`.

**גודל מסך:** `screen_in` נשאר ברמה 1 (חובה), כי דרישת "מסך 14 אינץ'" נפוצה. פרטי המסך האחרים (רזולוציה, פאנל, בהירות, רענון) נמצאים ברמה 2.

## טבלת מותגים: `brands.json`

```json
{
  "version": 1,
  "brands": [
    {
      "id": "lenovo",
      "name": "Lenovo",
      "country": "CN",
      "sub_brands": [
        { "id": "thinkpad", "name": "ThinkPad", "segment": "business" },
        { "id": "ideapad", "name": "IdeaPad", "segment": "consumer" }
      ]
    }
  ]
}
```

| שדה | חובה | הערה |
|---|---|---|
| `id` | כן | |
| `name` | כן | |
| `country` | לא | מדינת המטה |
| `sub_brands[].id`, `.name` | כן | |
| `sub_brands[].segment` | לא | `business` / `consumer` / `gaming` / `premium` / `workstation` / `education` |
| `reputation` | לא | משפט על המותג כולו |
| `service_il`, `warranty_il` | לא | אובייקט: `summary` (משפט), `length_years`, `service_type` (`onsite` / `pickup` / `lab` / `null`), `provider`, `sources` (רשימה של `url`, `says`, `kind`: `maker` / `store` / `press` / `forum`, `checked`), `notes`. `null` אם לא נמצא |
| `sub_brands[].profile.tagline` | לא | משפט אחד: מה הסדרה הזאת |
| `.profile.strengths`, `.weaknesses` | לא | רשימות קצרות, להסבר למשתמש |
| `.profile.best_for`, `.avoid_if` | לא | למי מתאים ולמי לא |
| `.profile.scores` | לא | `durability`, `build`, `keyboard`, `service`: 1 עד 5, טיפוסי לסדרה ולא לכל דגם. `null` אם לא ידוע |
| `.profile.notes` | לא | הערה חשובה, למשל זיכרון מולחם |
| `.profile.service_il`, `.warranty_il` | לא | כמו ברמת המותג, כשהסדרה שונה ממנו |

## טבלת מעבדים: `cpus.json`

```json
{
  "version": 1,
  "cpus": [
    {
      "id": "intel-core-ultra-5-125u",
      "vendor": "Intel",
      "family": "Core Ultra 5",
      "name": "Intel Core Ultra 5 125U",
      "cores": 12,
      "threads": 14,
      "base_tdp_w": 15,
      "release_year": 2024,
      "class": "U",
      "npu_tops": null,
      "benchmark": { "passmark": null, "source": null, "date": null }
    }
  ]
}
```

| שדה | חובה | הערה |
|---|---|---|
| `id` | כן | |
| `vendor` | כן | `Intel` / `AMD` / `Apple` / `Qualcomm` |
| `name` | כן | שם מלא |
| `family` | לא | למשל "Core Ultra 5", "Ryzen 7" |
| `cores`, `threads` | לא | |
| `base_tdp_w` | לא | |
| `class` | לא | `U` / `P` / `H` / `HX` / `other`; מרמז על צריכה וביצועים |
| `release_year` | לא | |
| `npu_tops` | לא | |
| `benchmark.passmark` | לא | הבסיס האובייקטיבי לציון "ביצועים". חובה לציין `source` ו-`date` כשהוא מלא |

## טבלת כרטיסי מסך: `gpus.json`

```json
{
  "version": 1,
  "gpus": [
    {
      "id": "intel-arc-graphics-125u",
      "vendor": "Intel",
      "name": "Intel Graphics (Core Ultra 5 125U)",
      "type": "integrated",
      "vram_gb": null,
      "release_year": 2024,
      "benchmark": { "passmark": null, "source": null, "date": null }
    }
  ]
}
```

| שדה | חובה | הערה |
|---|---|---|
| `id` | כן | |
| `vendor` | כן | `Intel` / `AMD` / `NVIDIA` / `Apple` / `Qualcomm` |
| `name` | כן | |
| `type` | כן | `integrated` / `discrete` |
| `vram_gb` | לא | `null` בגרפיקה משולבת (זיכרון משותף) |
| `tgp_w` | לא | הספק כרטיס נפרד, מושפע מדגם הלפטופ |
| `release_year` | לא | |
| `benchmark.passmark` | לא | חובה לציין `source` ו-`date` כשמלא |

## איך השדות מזינים את התבנית

| קריטריון קשיח אפשרי | שדה |
|---|---|
| לפחות X GB RAM | `ram_gb` |
| Windows כלול | `os_included` / `os` |
| אחריות X שנים | `warranty_years` |
| גודל מסך | `screen_in` |
| USB-C עם תמונה וטעינה | `ports.usb_c[].displayport`, `power_delivery` |
| Thunderbolt | `ports.usb_c[].thunderbolt` |
| Wi-Fi 6E ומעלה, שקע רשת | `network.wifi`, `network.ethernet_mbps` |
| מחיר מקסימלי | `price` (או הצעה זולה ביותר, בשלב 2) |

| קריטריון רך | שדות שהציון נגזר מהם |
|---|---|
| ביצועים | `cpu_id` -> `cpus.json` (`benchmark`, `class`), `gpu_id` -> `gpus.json`, `ram_gb`, `storage_type` |
| נוחות ועמידות | `keyboard_*`, `matte`, `panel` |
| יוקרה ומראה | `brand_id`, `sub_brand_id` (segment), `panel`, `weight_kg` |
| אפשרות שדרוג | `ram_upgradable`, `ram_max_gb`, `storage_slots_free` |
| חיבוריות | `ports`, `network` |
| ניידות | `weight_kg`, `battery_wh`, `screen_in` |
| שירות ואחריות | `warranty_years`, `warranty_type`, `warranty_provider` |
| אחסון | `storage_gb`, `storage_type` |

## החלטות (אושרו)

1. `ports` הוא אובייקט מובנה.
2. `segment` של תת-מותג מספיק לקריטריונים "עמידות" ו"יוקרה".
3. GPU בטבלה נפרדת (`gpus.json`).
4. הטבלאות ימולאו על ידי סקריפט. עדיין לא נכתב. נדרש להחליט על מקורות (ראו למטה).
5. נתון חסר (למשל benchmark) לא נשאר ריק: ה-Skill מחפש אותו ברשת, ואם אינו נמצא מסמן "חסר" ולא מנחש.

## שאלות פתוחות

1. מקורות לסקריפט המילוי: דפי יצרן (PSREF של Lenovo, Intel ARK, AMD specs), PassMark למדדי ביצועים, או אחר?
2. האם הסקריפט ירוץ ידנית כשאתה מוסיף דגם (נותן שם/מק"ט ומקבל רשומה מלאה), או כעדכון מרוכז של כל הקטלוג?
