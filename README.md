# Q3 EIA Diesel Outlook

Live chart of weekly U.S. retail diesel prices (EIA actuals) with monthly
STEO forecast overlay, plus a regional PADD breakdown. Part of the Fresh
Freight Q3 2026 Reefer & Perishable Forecast.

**Live URL:** https://[your-username].github.io/q3-eia-diesel-outlook/

## How it works

- `docs/index.html` is the chart. It calls two EIA v2 endpoints from the
  browser (weekly retail diesel + STEO forecast).
- The EIA API key lives in GitHub Secrets as `EIA_API_KEY`. The committed
  HTML has a placeholder string `__EIA_API_KEY__` instead of the real key.
- On every push to main, on a weekly schedule (Wed 18:00 UTC), and on manual
  trigger, the GitHub Action runs `scripts/inject_key.py` to swap the
  placeholder for the real key, then deploys the result to GitHub Pages.

## Local preview

The placeholder version won't load real data. To preview locally, temporarily
edit `docs/index.html` and paste your key in place of `__EIA_API_KEY__`.
**Do not commit that change.** A fallback dataset is built into the HTML so
the chart still renders without an API call.

## Data sources

- EIA weekly retail diesel: `petroleum/pri/gnd` (product EPD2D, process PTE)
- EIA Short-Term Energy Outlook: `steo` (series DSRTUUS)
- Regional breakdown by PADD: NUS, R10, R20, R30, R40, R50, SCA

## Updating the chart

Push changes to `docs/index.html` on main. The Action redeploys automatically.
The weekly cron picks up fresh EIA data without any code change, since the
chart fetches at page load time.
