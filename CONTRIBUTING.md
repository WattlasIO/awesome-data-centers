# Contributing to Awesome Data Centers

Pull requests that add genuinely useful, publicly verifiable data center resources are welcome.

## Inclusion criteria

- **Publicly accessible URL:** Must use `https://` and resolve cleanly without a paywall wall just to see what the tool/standard is.
- **Concrete utility:** Standards bodies, official grid/regulatory agencies, open-source infrastructure tools, peer-reviewed or empirical energy/water studies, or established industry publications.
- **No spam or SEO filler:** Keep descriptions to one plain, factual sentence (`- [Name](https://...) - Concise description.`). Avoid marketing adjectives.
- **Disclose affiliation:** If you submit a tool or tracker you maintain, mention it briefly in your PR description.

## Validation

Run the local structure and link-hygiene check before opening a PR:

```bash
python3 scripts/validate_readme.py
```
