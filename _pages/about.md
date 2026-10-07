---
layout: academic
permalink: /
title: ""
excerpt: ""
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<header class="profile" id="about-me">
  <div class="profile-heading">
    <h1>Rong-Xi Tan <span lang="zh-Hans">谭荣熙</span></h1>
    <p class="affiliation">PhD Student · Nanjing University</p>
  </div>
  <div class="profile-bio">
    <p>I am a PhD student at the <a href="https://ai.nju.edu.cn">School of Artificial Intelligence</a>,
      <a href="https://www.nju.edu.cn/">Nanjing University</a>, advised by
      <a href="https://www.lamda.nju.edu.cn/qianc/">Prof. Chao Qian</a>. I am a member of the
      <a href="https://www.lamda.nju.edu.cn/">LAMDA Group</a>, led by
      <a href="https://cs.nju.edu.cn/zhouzh/">Prof. Zhi-Hua Zhou</a>, and am fortunate to also work closely with
      <a href="https://yafuly.github.io/yafuly/">Dr. Yafu Li</a>.</p>
    <p>My research focuses on <strong>LLM agents</strong> and <strong>black-box optimization</strong>,
      with applications in AI for Science (geoscience and soil property analysis) and
      electronic design automation.</p>
    <div class="contact">
      <a class="email" href="mailto:tanrx@lamda.nju.edu.cn">tanrx@lamda.nju.edu.cn</a>
      <div class="social-links" aria-label="Other profiles">
        <a href="https://scholar.google.com/citations?user=m82W6XUAAAAJ">Google Scholar</a>
        <span aria-hidden="true">/</span>
        <a href="https://github.com/trxcc">GitHub</a>
        <span aria-hidden="true">/</span>
        <a href="https://twitter.com/rongxitan1">Twitter</a>
      </div>
    </div>
  </div>
  <img class="portrait" src="{{ site.author.avatar | relative_url }}" alt="Rong-Xi Tan at graduation" width="1280" height="1920">
</header>

<section id="news" class="news-section" aria-labelledby="news-heading">
  <span id="-news" class="legacy-anchor" aria-hidden="true"></span>
  <div class="news-label"><h2 id="news-heading">News</h2></div>
  <div class="news-content">
  <ul class="dated-list news-list">
    <li><time datetime="2026-09">Sep 2026</time><span>A co-first-authored paper on AI for Science was accepted by <a href="https://www.nature.com/articles/s43016-026-01419-9">Nature Food</a>.</span></li>
    <li><time datetime="2026-04">Apr 2026</time><span><a href="https://openreview.net/forum?id=ul2qlPcb5Y">GenRe<sup>2</sup></a> was accepted by <strong>ICML 2026</strong>.</span></li>
    <li><time datetime="2025-06">Jun 2025</time><span>Our research results were <a href="https://www.nsfc.gov.cn/p1/3381/2825/83716.html">reported by NSFC</a>.</span></li>
    <li><time datetime="2025-01">Jan 2025</time><span><a href="https://arxiv.org/abs/2410.11502">Offline-RaM</a> was accepted by <strong>ICLR 2025</strong>.</span></li>
  </ul>
  <details class="earlier-news">
    <summary>Earlier news</summary>
    <ul class="dated-list news-list">
      <li><time datetime="2024-12">Dec 2024</time><span>Received the Nanjing University Top-Grade Scholarship.</span></li>
      <li><time datetime="2024-09">Sep 2024</time><span>Received the National Science Foundation for Undergraduates.</span></li>
    </ul>
  </details>
  </div>
</section>

<section id="publications" aria-labelledby="publications-heading">
  <span id="-publications" class="legacy-anchor" aria-hidden="true"></span>
  <div class="section-heading">
    <h2 id="publications-heading">Publications</h2>
    <div class="publication-nav"><span class="contribution-note">* Equal contribution</span><a href="#more-publications">More papers ↓</a></div>
  </div>
  <h3 class="publication-subheading">Selected work</h3>
  {% assign selected_papers = site.data.publications | where: "featured", true %}
  <ol class="publications selected-publications">
    {% for paper in selected_papers %}
      {% include academic-publication.html paper=paper %}
    {% endfor %}
  </ol>

  <div id="more-publications" class="more-publications">
    <h3 class="publication-subheading">More papers</h3>
    {% assign other_papers = site.data.publications | where: "featured", false %}
    {% assign paper_years = other_papers | group_by: "year" | sort: "name" | reverse %}
    {% for year in paper_years %}
    <div class="publication-year">
      <h3 class="year-label">{{ year.name }}</h3>
      <ol class="publications">
        {% for paper in year.items %}
          {% include academic-publication.html paper=paper %}
        {% endfor %}
      </ol>
    </div>
    {% endfor %}
  </div>
</section>

<div class="background-grid">
<section id="education" aria-labelledby="education-heading">
  <span id="-educations" class="legacy-anchor" aria-hidden="true"></span>
  <h2 id="education-heading">Education</h2>
  <ul class="dated-list education-list">
    <li><span class="date">2025.09 – Present</span><span><strong>Nanjing University</strong><br>PhD Student, School of Artificial Intelligence.</span></li>
    <li><span class="date">2021.09 – 2025.06</span><span><strong>Nanjing University</strong><br>Undergraduate, School of Artificial Intelligence.</span></li>
    <li><span class="date">2018.09 – 2021.06</span><span><strong>Xinhui No. 1 Middle School</strong>, Guangdong.</span></li>
  </ul>
</section>

<section id="service" aria-labelledby="service-heading">
  <h2 id="service-heading">Academic Service</h2>
  <div class="service-columns">
    <div>
      <h3>Journal Reviewer</h3>
      <ul class="plain-list">
        <li>Transactions on Machine Learning Research</li>
        <li>IEEE Transactions on Evolutionary Computation</li>
      </ul>
    </div>
    <div>
      <h3>Conference Reviewer</h3>
      <ul class="plain-list">
        <li>ICLR: 2025, 2026, 2027</li>
        <li>NeurIPS: 2025</li>
        <li>ICML: 2026 <span class="reviewer-note">(Gold Reviewer)</span></li>
        <li>AAAI: 2027</li>
      </ul>
    </div>
  </div>
</section>
</div>

<section id="honors" aria-labelledby="honors-heading">
  <span id="-honors-and-awards" class="legacy-anchor" aria-hidden="true"></span>
  <h2 id="honors-heading">Honors &amp; Awards</h2>
  <ul class="dated-list">
    <li><time datetime="2025-06">Jun 2025</time><span>Research results reported by <a href="https://www.nsfc.gov.cn/p1/3381/2825/83716.html">NSFC</a>.</span></li>
    <li><time datetime="2024-12">Dec 2024</time><span>Nanjing University Top-Grade Scholarship — the university’s highest honor.</span></li>
    <li><time datetime="2024-09">Sep 2024</time><span>National Science Foundation for Undergraduates (国家自然科学基金本科生项目).</span></li>
    <li><time datetime="2024-04">Apr 2024</time><span>Merit Student of Jiangsu Province.</span></li>
    <li><time datetime="2023-11">Nov 2023</time><span>Bailu Scholarship, Nanjing University.</span></li>
    <li><time datetime="2023-07">Jul 2023</time><span>Pacemaker to Outstanding Students, Nanjing University.</span></li>
    <li><time datetime="2023-05">May 2023</time><span>One Hundred Outstanding Youths of Qixia District, Communist Youth League of Qixia District.</span></li>
    <li><time datetime="2022-11">Nov 2022</time><span>Second Prize Nationwide in the <a href="http://www.mcm.edu.cn/">National University Mathematical Modeling Competition</a>.</span></li>
  </ul>
</section>

<section id="talks" aria-labelledby="talks-heading">
  <h2 id="talks-heading">Invited Talks</h2>
  <ul class="dated-list">
    <li><time datetime="2025-09">Sep 2025</time><span>Towards Universal Offline Black-Box Optimization via Learning Language Model Embeddings.<br><a href="https://sites.google.com/view/leadworkshop2025">LEAD Workshop by SCUT</a> · Virtual.</span></li>
  </ul>
</section>

<section id="miscellaneous" aria-labelledby="miscellaneous-heading">
  <span id="-Miscellaneous" class="legacy-anchor" aria-hidden="true"></span>
  <h2 id="miscellaneous-heading">Beyond Research</h2>
  <p>My Chinese name is 谭荣熙 (Tan Rongxi), pronounced approximately as /tɑːm wɪŋ ‘heɪ/ in Cantonese.</p>
  <p>I enjoy Cantopop and am a fan of <a href="https://en.wikipedia.org/wiki/Joey_Yung">Joey Yung</a>—especially <a href="https://zh.wikipedia.org/wiki/%E5%BF%83%E4%B9%8B%E7%A7%91%E5%AD%B8">心之科學</a>. I also enjoy going to the gym, jogging, and playing badminton.</p>
</section>

<footer class="site-footer">
  <span>Rong-Xi Tan · Nanjing University</span>
  <a href="#about-me">Back to top ↑</a>
</footer>

<div class="visitor-map">
  <script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=5yfauFD3He7e5eUfjK92_4cq7sJHjoAJIS6eoVMNLWo&amp;cl=ffffff&amp;w=a"></script>
</div>
