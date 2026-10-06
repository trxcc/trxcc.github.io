# Publication maintenance

Verified on 6 October 2026. Homepage entries live in `_data/publications.yml`; both selected and compact entries use `_includes/academic-publication.html`. Each work appears once. The `featured` field controls the selected-work section; `image` independently controls whether an entry has a figure.

## Formatting conventions

- Preserve the official title's capitalization and hyphenation; do not apply CSS title case.
- Use full author names, bold Rong-Xi Tan, and superscript * for equal contribution.
- Use the same order: title; authors; venue, year, volume(issue): pages or article number; resources.
- Use an en dash for page ranges. Article numbers are not page ranges.
- Include PMLR volume and pagination for ICML papers. ICLR does not have a conventional proceedings page range.
- Label links Paper, OpenReview, arXiv, or Code consistently. No separate DOI label; no Nature Food code link.
- Keep journal reviewer names in full, without appended abbreviations.

## Verified records

| Work | Authoritative record | Notes |
| --- | --- | --- |
| Phosphorus use efficiency | [Nature Food](https://www.nature.com/articles/s43016-026-01419-9), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1038/s43016-026-01419-9) | 2026, 7(9): 869–877. Published 1 September 2026. First three authors contribute equally. |
| GenRe² | [PMLR](https://proceedings.mlr.press/v306/chen26ec.html), [author manuscript](https://arxiv.org/abs/2512.06533) | ICML 2026, PMLR 306: 16875–16909. Keep the requested OpenReview and Code links. |
| Universal BBO | [PMLR](https://proceedings.mlr.press/v267/tan25b.html), [author manuscript](https://arxiv.org/abs/2506.07109) | ICML 2025, PMLR 267: 58499–58544. PMLR's landing-page author metadata inverts Sheng Fu; the PDF and author manuscript confirm Sheng Fu, which is retained. |
| Universal BBO — Hot off the Press | [ACM](https://dl.acm.org/doi/10.1145/3795101.3814642), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1145/3795101.3814642) | GECCO 2026 Companion, pp. 85–86. Listed as a note under the original work, not counted twice. |
| Rethinking Learnability | [arXiv](https://arxiv.org/abs/2609.01493) | Retained as a 2026 preprint; no confirmed proceedings information. |
| Learnability: A Ranking Perspective | [arXiv](https://arxiv.org/abs/2603.04000) | Retained as a 2026 preprint; no confirmed proceedings information. |
| BBOPlace-Bench | [IEEE](https://ieeexplore.ieee.org/document/11605958/), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1109/tevc.2026.3712410), [Chao Qian's publication list](https://www.lamda.nju.edu.cn/qianc/) | Added 2026 and the IEEE article link. No final volume/issue; Crossref's 1–1 is a placeholder, not publication pagination. Retain in press. |
| Wetland methane | [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/gcb.70748), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1111/gcb.70748) | Global Change Biology, 2026, 32(2): e70748. |
| Offline-RaM | [OpenReview](https://openreview.net/forum?id=sb1HgVDLjN), [Chao Qian's publication list](https://www.lamda.nju.edu.cn/qianc/) | ICLR 2025. Corrected Learning Representation to Learning Representations. |
| Offline MOO | [PMLR](https://proceedings.mlr.press/v235/xue24b.html) | ICML 2024, PMLR 235: 55595–55624. Normalize Rongxi Tan to the homepage's Rong-Xi Tan. |
| Soil microbial-derived carbon | [PNAS](https://www.pnas.org/doi/10.1073/pnas.2401916121), [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1073/pnas.2401916121) | 2024, 121(35): e2401916121. Corrected title casing and microbial-derived hyphenation. |

The Nature page was readable via an ordinary HTTP fetch even though the search browser's fetch hit a cookie redirect. The OpenReview and ACM landing pages could not be inspected in that fetcher; use PMLR, author manuscripts, advisor records, and publisher-deposited metadata as indicated above.

## Figure provenance

These are figures from the author's papers, not generated artwork. They link back to the original figure or manuscript page.

- `images/publications/phosphorus-efficiency.png`: complete [Figure 1](https://www.nature.com/articles/s43016-026-01419-9/figures/1), downloaded from the publisher's image CDN without alteration.
- `images/publications/genre2.png`: Figure 2 from page 4 of the [author manuscript](https://arxiv.org/pdf/2512.06533), rendered at 220 dpi with only the figure region included.
- `images/publications/universal-bbo.png`: Figure 1 from page 3 of the [author manuscript](https://arxiv.org/pdf/2506.07109), rendered at 220 dpi with only the figure region included.
- `images/publications/bboplace-bench.png`: complete Figure 1 (without its caption) from page 2 of the [author manuscript](https://arxiv.org/pdf/2510.23472), rendered at 144 dpi.
- `images/publications/offline-ram.png`: complete Figure 1 (without its caption) from page 2 of the [author manuscript](https://arxiv.org/pdf/2410.11502), rendered at 216 dpi.
- `images/publications/offline-moo.png`: the Tasks panel of Figure 1 from page 2 of the [author manuscript](https://arxiv.org/pdf/2406.03722), rendered at 216 dpi. Only the six benchmark task families are shown; the Methods and Evaluations panels are omitted.
