# Publication maintenance

Verified on 7 October 2026. Homepage entries live in `_data/publications.yml`; both selected and compact entries use `_includes/academic-publication.html`. Each work appears once. The `featured` field controls the selected-work section; `image` independently controls whether an entry has a figure.

## Formatting conventions

- Preserve the official title and hyphenation in `title`. A separate `display_title` provides the requested title-case homepage heading for Nature Food; never apply CSS title case globally.
- Use full author names and bold Rong-Xi Tan. Display co-first-author asterisks only on papers where Rong-Xi Tan is one of the equal contributors. Keep factual contribution metadata even when its markers are hidden.
- Use the same order: title; authors; venue, volume(issue): pages or article number, year; resources. Omit fields that do not apply. Put in-press status after the year.
- Use an en dash for page ranges. Article numbers are not page ranges.
- Include PMLR volume and pagination for ICML papers. ICLR does not have a conventional proceedings page range.
- Label resources consistently as [paper], [openreview], [arxiv], [code], and [bib]. Preprints link directly to their arXiv abstract page. No separate DOI label; no Nature Food code link.
- Keep journal reviewer names in full, without appended abbreviations.
- Omit per-paper topic/method subheadings; the title and figure identify each selected work.

## Verified records

| Work | Authoritative record | Notes |
| --- | --- | --- |
| Phosphorus use efficiency | [Nature Food](https://www.nature.com/articles/s43016-026-01419-9), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1038/s43016-026-01419-9) | 2026, 7(9): 869–877. Published 1 September 2026. First three authors contribute equally. |
| GenRe² | [PMLR](https://proceedings.mlr.press/v306/chen26ec.html), [author manuscript](https://arxiv.org/abs/2512.06533) | ICML 2026, PMLR 306: 16875–16909. Keep the requested OpenReview and Code links. |
| Universal BBO | [PMLR](https://proceedings.mlr.press/v267/tan25b.html), [author manuscript](https://arxiv.org/abs/2506.07109) | ICML 2025, PMLR 267: 58499–58544. PMLR's landing-page author metadata inverts Sheng Fu; the PDF and author manuscript confirm Sheng Fu, which is retained. |
| Universal BBO — Hot off the Press | [ACM](https://dl.acm.org/doi/10.1145/3795101.3814642), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1145/3795101.3814642) | GECCO 2026 Companion, pp. 85–86. Listed as a note under the original work, not counted twice. |
| Agentic HDBO (HERA) | [arXiv](https://arxiv.org/abs/2609.34281), [author manuscript](https://arxiv.org/html/2609.34281v1) | New preprint, 28 September 2026. Five authors; normalize Rongxi Tan to Rong-Xi Tan. No equal-contribution statement or official code link found in the manuscript. |
| Rethinking Critic Learning (SP³O) | [arXiv](https://arxiv.org/abs/2609.18708), [author manuscript](https://arxiv.org/html/2609.18708v1) | New preprint, 16 September 2026. Twelve authors; first two contribute equally. The manuscript links to [SP3O code](https://github.com/Dodojordi/SP3O). |
| Rethinking Learnability | [arXiv](https://arxiv.org/abs/2609.01493) | Retained as a 2026 preprint; no confirmed proceedings information. |
| Learnability: A Ranking Perspective | [arXiv](https://arxiv.org/abs/2603.04000) | Retained as a 2026 preprint; no confirmed proceedings information. |
| BBOPlace-Bench | [IEEE](https://ieeexplore.ieee.org/document/11605958/), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1109/tevc.2026.3712410), [Chao Qian's publication list](https://www.lamda.nju.edu.cn/qianc/) | Added 2026 and the IEEE article link. No final volume/issue; Crossref's 1–1 is a placeholder, not publication pagination. Retain in press. |
| Wetland methane | [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/gcb.70748), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1111/gcb.70748) | Global Change Biology, 2026, 32(2): e70748. |
| Offline-RaM | [OpenReview](https://openreview.net/forum?id=sb1HgVDLjN), [Chao Qian's publication list](https://www.lamda.nju.edu.cn/qianc/) | ICLR 2025. Corrected Learning Representation to Learning Representations. |
| Offline MOO | [PMLR](https://proceedings.mlr.press/v235/xue24b.html) | ICML 2024, PMLR 235: 55595–55624. Normalize Rongxi Tan to the homepage's Rong-Xi Tan. |
| Soil microbial-derived carbon | [PNAS](https://www.pnas.org/doi/10.1073/pnas.2401916121), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1073/pnas.2401916121) | 2024, 121(35): e2401916121. Corrected title casing and microbial-derived hyphenation. |

The Nature page was readable via an ordinary HTTP fetch even though the search browser's fetch hit a cookie redirect. The OpenReview and ACM landing pages could not be inspected in that fetcher; use PMLR, author manuscripts, advisor records, and publisher-deposited metadata as indicated above.

The Google Scholar profile (`m82W6XUAAAAJ`) timed out during the 7 October check. As a fallback, checked arXiv's full author searches for both [Rong-Xi Tan](https://arxiv.org/search/?query=Tan%2C+Rong-Xi&searchtype=author&abstracts=hide&order=-announced_date_first&size=50) (eight results) and [Rongxi Tan](https://arxiv.org/search/?query=Tan%2C+Rongxi&searchtype=author&abstracts=hide&order=-announced_date_first&size=50) (one result). Those nine distinct arXiv works are represented in the homepage, with published works cited using the publisher record rather than counted again as preprints. This is not a claim that the entire Scholar profile was read.

## BibTeX maintenance

- Every entry has a unique `citekey`. `_includes/academic-bibtex.bib` generates both the inline [bib] panel and the corresponding `files/bibtex/<id>.bib` download from the same YAML record.
- Follow the user-supplied [reference-writing guide](https://xuek-nju.notion.site/2a6ca732f30041be8eaa4e85301d3d58): journal `@article` fields are title, author, journal, volume, number, pages, year; conference `@inproceedings` fields are title, author, booktitle, pages, address, year. Omit unavailable fields. arXiv-only papers use `@article` with `journal={arXiv:<id>}`.
- Export sentence-case titles without a whole-title protection group. Use `bib_protected_terms` for proper names/acronyms (BBOPlace-Bench, Bayesian, PPO); also protect the initial after a colon, as the guide requests. Use full author names joined by `and`, `--` for page ranges, and a TeX accent for Jörgensen. Never include co-first markers in BibTeX.
- Spell out booktitles and include the conference acronym consistently. Conference locations were checked against the official [ICML 2026 call](https://icml.cc/Conferences/2026/CallForPapers), [ICML 2025 fact sheet (also records Vienna 2024)](https://media.icml.cc/Conferences/ICML2025/ICML2025_Fact_Sheet.pdf), and [ICLR 2025 venue](https://iclr.cc/Conferences/2025/VisaTravel).
- No URL, DOI, publisher, series, eprint, archivePrefix, primaryClass, or status-note fields in the compact BibTeX. Journal article identifiers use `pages`; PMLR volume and in-press status remain on the webpage, but are omitted from BibTeX to match the guide. Never invent missing pagination.
- Native HTML details and downloads work without JavaScript. The small `academic-bibtex.js` enhancement adds clipboard copying when supported and reports a manual-copy/download fallback if access fails.
- When adding a paper, add its YAML record and a thin `.bib` wrapper containing its `paper_id`; no duplicated citation metadata is needed.

## Figure provenance

These are figures from the author's papers, not generated artwork. They link back to the original figure or manuscript page.

- `images/publications/phosphorus-efficiency.png`: complete [Figure 1](https://www.nature.com/articles/s43016-026-01419-9/figures/1), downloaded from the publisher's image CDN without alteration.
- `images/publications/genre2.png`: Figure 2 from page 4 of the [author manuscript](https://arxiv.org/pdf/2512.06533), rendered at 220 dpi with only the figure region included.
- `images/publications/universal-bbo.png`: Figure 1 from page 3 of the [author manuscript](https://arxiv.org/pdf/2506.07109), rendered at 220 dpi with only the figure region included.
- `images/publications/bboplace-bench.png`: complete Figure 1 (without its caption) from page 2 of the [author manuscript](https://arxiv.org/pdf/2510.23472), rendered at 144 dpi.
- `images/publications/offline-ram.png`: complete Figure 1 (without its caption) from page 2 of the [author manuscript](https://arxiv.org/pdf/2410.11502), rendered at 216 dpi.
- `images/publications/offline-moo.png`: the Tasks panel of Figure 1 from page 2 of the [author manuscript](https://arxiv.org/pdf/2406.03722), rendered at 216 dpi. Only the six benchmark task families are shown; the Methods and Evaluations panels are omitted.
