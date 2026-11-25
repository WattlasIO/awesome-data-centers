# Awesome Data Centers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![CI](https://github.com/WattlasIO/awesome-data-centers/actions/workflows/ci.yml/badge.svg)](https://github.com/WattlasIO/awesome-data-centers/actions/workflows/ci.yml)

> A curated directory of data center infrastructure standards, grid and interconnection portals, open-source DCIM tools, energy and water research, public trackers, and field guides.

Maintained by **[Wattlas](https://wattlas.io)** (`WattlasIO`). Contributions via pull request are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

- [Standards, Reliability & Engineering](#standards-reliability--engineering)
- [Grid, Power & Interconnection](#grid-power--interconnection)
- [Open-Source DCIM, Infrastructure & Telemetry](#open-source-dcim-infrastructure--telemetry)
- [Public Permitting & Regulatory References](#public-permitting--regulatory-references)
- [Maps, Directories & Pipeline Trackers](#maps-directories--pipeline-trackers)
- [Water, Cooling & Sustainability Research](#water-cooling--sustainability-research)
- [Calculators & Open Specifications](#calculators--open-specifications)
- [News, Analysis & Research](#news-analysis--research)
- [Field Guides & Record Reading](#field-guides--record-reading)
- [Jobs & Industry Communities](#jobs--industry-communities)
- [FAQ](#faq)

---

## Standards, Reliability & Engineering

- [ASHRAE TC 9.9](https://tc0909.ashraetcs.org/) - Thermal guidelines, environmental envelopes, and liquid-cooling standards for mission-critical data processing environments.
- [BICSI](https://www.bicsi.org/) - Cabling, telecommunications, and data center design standards including ANSI/BICSI 002.
- [NFPA 75 & 76](https://www.nfpa.org/) - Fire protection standards for information technology equipment and telecommunications facilities (plus NFPA 855 for stationary energy storage).
- [Open Compute Project (OCP)](https://www.opencompute.org/) - Open hardware designs for racks, power shelves, liquid cooling manifolds, and hyperscale facility engineering.
- [The Green Grid](https://www.thegreengrid.org/) - Industry consortium behind PUE (Power Usage Effectiveness), WUE (Water Usage Effectiveness), and CUE metrics.
- [TIA-942](https://www.tiaonline.org/) - Telecommunications infrastructure standard covering data center topology, redundancy, and facility ratings.
- [Uptime Institute Tier Standards](https://uptimeinstitute.com/tiers) - Widely used Tier I–IV topology and operational sustainability classifications for data center availability.

## Grid, Power & Interconnection

### Federal & Continental Authorities
- [FERC (Federal Energy Regulatory Commission)](https://www.ferc.gov/) - US interstate transmission regulation, interconnection rulemaking (Order 2023), and large-load co-location proceedings.
- [NERC (North American Electric Reliability Corporation)](https://www.nerc.com/) - Long-Term Reliability Assessments (LTRA), bulk power system standards, and large-load demand growth studies.
- [US Department of Energy (DOE)](https://www.energy.gov/) - Federal grid modernization, power demand research, and AI data center energy policy publications.
- [US Energy Information Administration (EIA)](https://www.eia.gov/electricity/) - Official US electricity generation, capacity (EIA-860 / 860M), utility territory (EIA-861), and hourly grid monitor (EIA-930) datasets.

### US Regional Transmission Organizations (RTOs / ISOs)
- [CAISO](https://www.caiso.com/) - California Independent System Operator interconnection queues, transmission plans, and load forecasts.
- [ERCOT](https://www.ercot.com/) - Electric Reliability Council of Texas large flexible load studies, GIS interconnection reports, and grid conditions.
- [ISO New England](https://www.iso-ne.com/) - New England interconnection queue, CELT load forecasts, and regional system planning.
- [MISO](https://www.misoenergy.org/) - Midcontinent Independent System Operator generator interconnection queue, MTEP transmission planning, and resource adequacy.
- [NYISO](https://www.nyiso.com/) - New York Independent System Operator Gold Book load forecasts and interconnection queue.
- [PJM Interconnection](https://www.pjm.com/) - Mid-Atlantic and Midwest RTO serving Northern Virginia, Ohio, and Illinois; publishes annual Load Forecast reports and transmission plans.
- [SPP (Southwest Power Pool)](https://www.spp.org/) - Great Plains and South-Central US transmission planning, generation interconnection, and large-load integration studies.

### Power & Grid Research Institutes
- [EPRI (Electric Power Research Institute)](https://www.epri.com/) - Power delivery, DCFlex grid-flexibility initiative, and data center load impact engineering research.
- [Lawrence Berkeley National Laboratory — Energy Technologies Area](https://eta.lbl.gov/) - Authors of the US Data Center Energy Usage Report and the Queued Up interconnection queue dataset.
- [RMI (Rocky Mountain Institute)](https://rmi.org/) - Grid-enhancing technologies, large-load tariff design, and clean-power procurement research.

## Open-Source DCIM, Infrastructure & Telemetry

- [Grafana](https://grafana.com/oss/grafana/) - Open-source dashboards for facility power metering, PUE tracking, and environmental telemetry.
- [LibreNMS](https://www.librenms.org/) - Auto-discovering SNMP network and PDU/UPS monitoring system.
- [Nautobot](https://github.com/nautobot/nautobot) - Network source of truth and automation platform forked from NetBox with extensible data models.
- [NetBox](https://github.com/netbox-community/netbox) - De facto open-source DCIM and IPAM platform for modeling sites, racks, power feeds, circuits, and cables.
- [openDCIM](https://github.com/samilliken/openDCIM) - Web-based open-source data center infrastructure management tool focused on physical rack, power, and cooling tracking.
- [PeeringDB](https://www.peeringdb.com/) - Community-maintained global database of colocation facilities, internet exchange points (IXPs), and carrier networks, with a public REST API.
- [Prometheus](https://prometheus.io/) - Open-source time-series monitoring engine widely used for telemetry across server halls and electrical infrastructure.
- [RackTables](https://github.com/RackTables/racktables) - Lightweight open-source datacenter asset, rackspace, and IP address manager.
- [Ralph](https://github.com/allegro/ralph) - Open-source asset management and DCIM system built for hardware lifecycle tracking.

## Public Permitting & Regulatory References

Checking whether an announced data center campus is actually advancing requires looking at primary government records rather than press releases alone:

- [US Data Center Permit & Filing Sources (`datacenter-permit-sources`)](https://github.com/WattlasIO/datacenter-permit-sources) - Machine-readable JSON directory and zero-dependency Python CLI of official US federal, RTO, and state filing portals (EIA-860M, EIA-861, PJM Load Forecast, GLEIF LEI, US Census Places, TX TDLR TABS, MD MDE, OK DEQ, MN PUC), documenting what each record proves and what it does not prove.
- [US Census Gazetteer & Place Files](https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html) - Official US county and incorporated place FIPS codes and coordinates for normalizing site locations.
- [GLEIF Legal Entity Identifier (LEI) API](https://www.gleif.org/en/lei-data/gleif-api/) - Public lookup for legal entities and parent-subsidiary corporate structures behind project LLCs.
- [US EPA Envirofacts](https://enviro.epa.gov/) - Public federal environmental facility and air/water permitting lookup across US jurisdictions.

## Maps, Directories & Pipeline Trackers

- [Baxtel](https://baxtel.com/) - Commercial colocation, cloud region, and global data center facility directory.
- [Cloudscene](https://cloudscene.com/) - Directory of colocation data centers, cloud on-ramps, and network fabric providers.
- [Data Center Map](https://www.datacentermap.com/) - Global directory of colocation facilities, internet exchanges, and cloud regions.
- [Epoch AI — Frontier Data Centers Hub](https://epoch.ai/data/data-centers) - Public research dataset tracking major frontier AI training clusters and estimated compute/power scale.
- [LBNL Queued Up](https://emp.lbl.gov/queues) - Annual empirical dataset of US transmission interconnection queues compiled by Lawrence Berkeley National Laboratory.
- [PeeringDB Facilities](https://www.peeringdb.com/advanced_search) - Carrier-neutral facility directory focused on interconnection and peering density.
- [Wattlas](https://wattlas.io) *(maintained by this organization)* - US-only tracker of planned and under-construction data center projects tied to official public filings, with free public directories for [projects](https://wattlas.io/projects), [34 US markets](https://wattlas.io/metros), and [local moratoria & opposition](https://wattlas.io/opposition).

## Water, Cooling & Sustainability Research

- [Climate Neutral Data Centre Pact](https://www.climateneutraldatacentre.net/) - European operator self-regulatory initiative on energy efficiency, clean power, water conservation, and circular economy targets.
- [IEA — Data Centres and Data Transmission Networks](https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks) - International Energy Agency global electricity demand analysis and forecasts for data centers and AI workloads.
- [LBNL US Data Center Energy Usage Report](https://eta.lbl.gov/publications/2024-united-states-data-center-energy) - Benchmark federal study of historical and projected US data center electricity consumption.
- [WRI Aqueduct Water Risk Atlas](https://www.wri.org/aqueduct) - Open global mapping of baseline water stress, drought risk, and seasonal variability used in site selection.

## Calculators & Open Specifications

- [`WattlasIO/datacenter-mw-calculator`](https://github.com/WattlasIO/datacenter-mw-calculator) - Zero-dependency Python CLI and library converting IT load (MW), utility load via PUE, annual GWh, water consumption via WUE, substation MVA, and N+1 / 2N backup generator counts.
- [`WattlasIO/datacenter-stage-spec`](https://github.com/WattlasIO/datacenter-stage-spec) - Open JSON Schema (`project-record.schema.json`), stage taxonomy, and validation rules for tracking pre-operational data center projects from announcement to energization.
- [The Green Grid PUE & WUE Whitepapers](https://www.thegreengrid.org/en/resources/library-and-tools) - Reference methodology for calculating Power Usage Effectiveness and Water Usage Effectiveness across facilities.

## News, Analysis & Research

- [Capacity Media](https://www.capacitymedia.com/) - Subsea cable, carrier, and wholesale data center infrastructure news.
- [Data Center Dynamics (DCD)](https://www.datacenterdynamics.com/) - Global trade publication covering hyperscale builds, power constraints, cooling, and market developments.
- [Data Center Frontier](https://www.datacenterfrontier.com/) - Coverage of US data center construction, edge computing, and power infrastructure.
- [Data Center Knowledge](https://www.datacenterknowledge.com/) - Industry reporting on colocation, cloud infrastructure, sustainability, and facility operations.
- [Interconnection.fyi](https://www.interconnection.fyi/) - Public analytics and search across US utility interconnection queues.
- [SemiAnalysis](https://www.semianalysis.com/) - Deep technical research on AI clusters, silicon supply chains, and gigawatt-scale campus power architecture.
- [Uptime Institute Intelligence](https://uptimeinstitute.com/uptime-intelligence) - Research reports on outage causes, staffing, PUE trends, and AI power density.
- [Utility Dive](https://www.utilitydive.com/) - US electric utility, regulatory docket, transmission, and large-load tariff reporting.

## Field Guides & Record Reading

Practical guides on interpreting capacity figures, permits, timelines, and project ownership from public records:

- [Announced isn't built: reading a datacenter's stage from the record](https://wattlas.io/articles/announced-isnt-built)
- [Data center megawatts: IT load vs utility load](https://wattlas.io/articles/data-center-megawatts-explained)
- [How long it takes to build a data center, by stage](https://wattlas.io/articles/how-long-to-build-a-data-center)
- [Phantom data centers: the record test](https://wattlas.io/articles/phantom-data-centers-record-test)
- [Large load interconnection: definitions and the six steps](https://wattlas.io/articles/what-is-a-large-load-interconnection)
- [Data center site permit vs building permit: the differences](https://wattlas.io/articles/data-center-site-permit-vs-building-permit)
- [Find the developer or owner behind a data center project](https://wattlas.io/articles/find-the-developer-or-owner-behind-a-data-center-project)

## Jobs & Industry Communities

- [AFCOM](https://www.afcom.com/) - Association for data center management and operations professionals; host of Data Center World.
- [Infrastructure Masons (iMasons)](https://imasons.org/) - Global professional community of digital infrastructure builders and executives.
- [NANOG](https://www.nanog.org/) - North American Network Operators' Group covering peering, routing, and interconnection engineering.
- [r/datacenter](https://www.reddit.com/r/datacenter/) - Practitioner forum for data center technicians, critical facilities engineers, and builders.
- [Wattlas US Data Center Jobs](https://wattlas.io/jobs) - Weekly refreshed index of open US data center roles across engineering, construction, and operations.

---

## FAQ

### What is the difference between IT load and utility load in a data center?
IT load is the electrical power delivered directly to servers, storage, and networking equipment. Utility (or facility) load equals IT load multiplied by Power Usage Effectiveness (PUE) — covering cooling, UPS losses, and lighting — and is typically 15% to 40% higher than IT load. See [Data center megawatts: IT load vs utility load](https://wattlas.io/articles/data-center-megawatts-explained) or calculate conversions with [`datacenter-mw-calculator`](https://github.com/WattlasIO/datacenter-mw-calculator).

### How can you tell whether an announced data center project is actually being built?
Track primary milestones in order: land acquisition or zoning filing, zoning approval, site or environmental permits (air/water/stormwater), utility large-load service agreements, and vertical building permits. A press release or queue request alone does not confirm construction. See [`datacenter-stage-spec`](https://github.com/WattlasIO/datacenter-stage-spec) and [Phantom data centers: the record test](https://wattlas.io/articles/phantom-data-centers-record-test).

### Where can I browse US data center projects, markets, and local moratoria?
Public directories for US planned and operating campuses, 34 regional power markets, and city/county data center moratoria are available free on [wattlas.io/projects](https://wattlas.io/projects), [wattlas.io/metros](https://wattlas.io/metros), and [wattlas.io/opposition](https://wattlas.io/opposition).

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, Wattlas has waived all copyright and related or neighboring rights to this curated list.
