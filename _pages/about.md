---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi, this is Rong-Xi Tan. Currently I am a first-year PhD student of [School of Artificial Intelligence](https://ai.nju.edu.cn) in [Nanjing University](https://www.nju.edu.cn/) advised by [Prof. Chao Qian](https://www.lamda.nju.edu.cn/qianc/) and a member of [LAMDA Group](https://www.lamda.nju.edu.cn/), led by [Prof. Zhi-Hua Zhou](https://cs.nju.edu.cn/zhouzh/).

My research interest lies in **black-box optimization (BBO) algorithms**, and their applications in AI4Science (e.g., geoscience and soil property analysis) and industrial scenarios (e.g., electronic design automation). 

<!--
I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).
-->

# 🔥 News
- *2025.06*: &nbsp;🎉🎉 Research results reported by NSFC [[Link](https://www.nsfc.gov.cn/p1/3381/2825/83716.html)].
- *2025.01*: &nbsp;🎉🎉 Offline-RaM is accepted by ICLR'25.
- *2024.12*: &nbsp;🎉🎉 I got Top-Grade Scholarship of Nanjing University.
- *2024.09*: &nbsp;🎉🎉 I got National Science Foundation for Undergraduates.

# 📝 Publications 

## 📤 Preprint
1. Shen-Huan Lyu, **Rong-Xi Tan**, Ke Xue, Yi-Xiao He, Yu Huang, Qingfu Zhang, Chao Qian. On the Learnability of Offline Model-Based Optimization: A Ranking Perspective. arXiv:2603.04000. [[Paper](https://arxiv.org/abs/2603.04000)]
1. Ming Chen\*, Sheng Tang\*, **Rong-Xi Tan\***, Ziniu Li, Jiacheng Chen, Ke Xue, Chao Qian. Beyond Token-level Supervision: Unlocking the Potential of Decoding-based Regression via Reinforcement Learning. arXiv:2512.06533. [[Paper](https://arxiv.org/abs/2512.06533)]
1. Ke Xue\*, Ruo-Tong Chen\*, **Rong-Xi Tan\***, Xi Lin, Yunqi Shi, Siyuan Xu, Mingxuan Yuan, Chao Qian. BBOPlace-Bench: Benchmarking Black-Box Optimization for Chip Placement. arXiv:2510.23472. [[Paper](https://arxiv.org/abs/2510.23472)] [[Code](https://github.com/lamda-bbo/BBOPlace-Bench)]

## 📈 Conference

1. **Rong-Xi Tan\***, Ming Chen\*, Ke Xue, Yao Wang, Yaoyuan Wang, Sheng Fu, Chao Qian. Towards Universal Offline Black-Box Optimization via Learning Language Model Embeddings. In: **Proceedings of the 42nd International Conference on Machine Learning (ICML'25)**, Vancouver, Canada, 2025, to appear. [[Paper](https://openreview.net/forum?id=NOV32X1Rq3)] [[Code](https://github.com/trxcc/universal-offline-bbo)]  
  Also in: [**2nd Workshop on Foundation Models in the Wild**](https://fm-wild-community.github.io/) **at ICLR'25**, Singapore, 2025. **(Oral presentation)** 
1. **Rong-Xi Tan**, Ke Xue, Shen-Huan Lyu, Haopu Shang, Yao Wang, Yaoyuan Wang, Sheng Fu, Chao Qian. Offline Model-Based Optimization by Learning to Rank. In: **Proceedings of the 13th International Conference on Learning Representation (ICLR'25)**, Singapore, 2025. [[Paper](http://arxiv.org/abs/2410.11502)] [[Code](https://github.com/trxcc/Offline-RaM)]
1. Ke Xue\*, **Rong-Xi Tan\***, Xiaobin Huang, Chao Qian. Offline Multi-Objective Optimization. In: **Proceedings of the 41st International Conference on Machine Learning (ICML'24)**, Vienna, Austria, 2024, pp. 55595-55624. [[Paper](https://arxiv.org/abs/2406.03722)] [[Code](https://github.com/lamda-bbo/offline-moo)]

## 📚 Journal

1. Han Hu, Ke Xue, Yishen Sun, Qing Zhu, Hans K. Carlson, Ruiwen Hu, **Rong-Xi Tan**, Chao Qian, Weigen Huang, Jizhong Zhou, Jingdong Mao, Thomas W. Crowther, Zhi-Hua Zhou, Jiabao Zhang, and Yuting Liang. Reducing the Discrepancy in Quantifying the Temperature Dependence of Global Wetland Methane Emission. **Global Change Biology**, 2026, 32(2): e70748. [[Paper](https://onlinelibrary.wiley.com/doi/10.1111/gcb.70748)]
1. Han Hu\*, Chao Qian\*, Ke Xue\*, Rainer Georg Jörgensen, Marco Keiluweit, Chao Liang, Xuefeng Zhu, Ji Chen, Yishen Sun, Haowei Ni, Jixian Ding, Weigen Huang, Jingdong Mao, **Rong-Xi Tan**, Jizhong Zhou, Thomas W. Crowther, Zhi-Hua Zhou, Jiabao Zhang, and Yuting Liang. Reducing the Uncertainty in Estimating Soil Microbial Derived Carbon Storage. **Proceedings of the National Academy of Sciences (PNAS)**, 2024, 121(35): e2401916121. [[Paper](https://www.pnas.org/doi/10.1073/pnas.2401916121)]



<!--
[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div>

- [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020**
-->

# 🎖 Honors and Awards
- *2025.06*: Research results reported by NSFC [[Link](https://www.nsfc.gov.cn/p1/3381/2825/83716.html)].
- *2024.12*: Nanjing University Top-Grade Scholarship (the highest honor at Nanjing University).
- *2024.09*: National Science Foundation for Undergraduates (国家自然科学基金本科生项目).
- *2024.04*: Merit Student of Jiangsu Province.
- *2023.11*: Bailu Scholarship, Nanjing University. 
- *2023.07*: Pacemaker to Outstanding students, Nanjing University. 
- *2023.05*: One Hundred Outstanding Youths of Qixia District, Communist Youth League of Qixia District. 
- *2022.11*: Second Prize Nationwide in [National University Mathematical Modeling Competition (MCM)](http://www.mcm.edu.cn/).

# 📪 Services
**Conference Reviewer**:
- ICLR: 2025, 2026
- NeurIPS: 2025
- ICML: 2026

# 📖 Educations
- *2025.09 - Present*, PhD student in [the School of Artificial Intelligence](https://ai.nju.edu.cn), [Nanjing University](https://www.nju.edu.cn/).
- *2021.09 - 2025.06*, Undergradute in [the School of Artificial Intelligence](https://ai.nju.edu.cn), [Nanjing University](https://www.nju.edu.cn/).
- *2018.09 - 2021.06*, Xinhui No.1 Middle School, Guangdong. 


# 💬 Invited Talks
- *2025.09*, Towards Universal Offline Black-Box Optimization via Learning Language Model Embeddings. @ [LEAD Workshop by SCUT](https://sites.google.com/view/leadworkshop2025), Virtual.

<!--

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
-->

# 🥳 Miscellaneous
- My Chinese name is 谭荣熙 (Tan Rongxi), which can be pronounced as /tɑːm wɪŋ 'heɪ/ in Cantonese.
- I sincerely enjoy in Cantopop, and I am a fan of [Joey](https://en.wikipedia.org/wiki/Joey_Yung). It would be absolutely cool if you are also interested in [心之科學](https://zh.wikipedia.org/wiki/%E5%BF%83%E4%B9%8B%E7%A7%91%E5%AD%B8).
- I also enjoy working out, like going to the gym💪, jogging🏃, and playing badminton🏸 (though I could not play it for a long time due to injury😭).

<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=5yfauFD3He7e5eUfjK92_4cq7sJHjoAJIS6eoVMNLWo&cl=ffffff&w=a" width="80%"></script>