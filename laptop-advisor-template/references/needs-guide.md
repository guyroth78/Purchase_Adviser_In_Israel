# Needs guide: from a usage profile to a target per criterion

Use this to set each criterion's `need` (the target a model must meet to score 5). Start from the closest profile, then adjust to what the person actually wrote. These are starting points for 2026-era Windows laptops, not rules. When the person's words are more specific, their words win.

The goal is the right-sized laptop: the cheapest machine that meets the need, not the strongest one. Do not raise a target "to be safe". Raise it only when the person asked for headroom (for example "should last 5 years", "I keep laptops a long time") or when the profile clearly needs it.

## Profiles

| Profile | RAM (minimum / target) | CPU | GPU | Storage | Notes |
|---|---|---|---|---|---|
| Office, study, browsing (under ~20 tabs) | 8 / 16GB | Any current U-class (Core 5 / Ultra 5 / Ryzen 5) | Integrated | 256-512GB SSD | Battery and weight usually matter more than speed. |
| Heavy browser and office (many tabs, Teams/Zoom, several apps at once) | 16 / 16GB | U or P class, current gen | Integrated | 512GB | RAM is the usual bottleneck, not the CPU. |
| AI builder / automation (n8n, Claude or ChatGPT apps, Python scripts, cloud services, many tabs) | 16 / 32GB | U, P or H class, current gen; mid-range is enough | Integrated (models run in the cloud) | 512GB-1TB | Target 32GB only if they run several heavy apps at once or Docker; otherwise 16GB meets the need. Python and dev tools: prefer x86 (see risks). |
| Software developer (IDE, Docker/WSL, local databases, VMs) | 16 / 32GB | H or P class | Integrated | 1TB | Docker, WSL and VMs are the RAM drivers. x86 strongly preferred. |
| Local AI models (running LLMs or image models on the laptop) | 32 / 32-64GB | H class | Discrete NVIDIA with 8GB+ VRAM | 1TB+ | Rare; confirm they really run models locally. |
| Photo editing | 16 / 32GB | P or H class | Integrated is fine for most; discrete helps for heavy RAW batches | 1TB | Screen quality (color accuracy, sRGB coverage) matters. |
| Video editing (1080p / 4K) | 32 / 32GB | H class | Discrete (RTX 4050+ class) for 4K | 1TB+ | Plus external storage. |
| Gaming | 16 / 32GB | H class | Discrete, matched to the games (RTX 4060 class for current AAA at 1080p) | 1TB | Heavy and short battery life by nature; say so. |

## Other criteria

- **Portability:** carried every day -> target about 1.4kg or less; carried sometimes -> about 1.8kg; desk only -> weight does not matter (weight 0-1).
- **Battery:** a full day away from a charger -> target a long-battery platform (large battery or an efficient CPU class); mostly plugged in -> low weight.
- **External monitors:** two or more -> Thunderbolt 4 / USB4, or USB-C with DisplayPort plus HDMI; check the maker's spec for how many displays are supported. One monitor through a dock -> USB-C with DisplayPort Alt Mode and Power Delivery.
- **Screen:** 13-14" for carrying daily, 15-16" for a mostly-desk machine. Ask only if the text gives no hint.
- **Upgradability:** matters only if they plan to keep it long or start with less RAM; soldered RAM then fails the need.
- **Service and warranty:** business lines (ThinkPad, Latitude, ExpertBook, EliteBook) usually come with longer or on-site warranty; check per SKU.

## Risks that become default-on hard filters

When a model carries a known risk for a need the person stated, add a hard constraint for it with `on: true`, not only a note. The person can turn it off.

- **ARM (Snapdragon) Windows** vs Python packages with native code, Docker, older dev tools, some VPN clients, drivers for specialized hardware, some games: filter "x86 processor".
- **Soldered RAM** vs "I want to upgrade later" or a minimum the base model does not meet: filter "RAM upgradeable" or a RAM minimum.
- **No OS included** vs a person who will not install Windows themselves: filter "Windows included".
- **One external display only** vs two monitors: filter "supports 2 external displays".

## Scoring against the target

- **5**: meets the target (including any headroom the person asked for).
- **4**: meets it with a small, minor gap.
- **3**: meets the minimum but not the target; a noticeable compromise.
- **2**: below the minimum in a way the person will feel.
- **1**: does not meet the need.
- **Above the target earns nothing extra.** Two models that both meet the target both get 5, and the cheaper one ranks first. Do not reward power the need does not call for.
