---
permalink: /
title: "Zhangyao Song"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

# About Me
I am currently a Ph.D. student at the [School of Cyber Science and Engineering, Southeast University](https://www.seu.edu.cn/), Nanjing, China. I received the M.S. degree in cybersecurity from Southeast University in 2026, and the B.S. degree in computer science from Zhengzhou University, Zhengzhou, China, in 2023.

My research interests include channel prediction and data mining, with a focus on:

- **Time Series Forecasting**: long-term forecasting, frequency-domain modeling, and representation learning.
- **Wireless Channel Prediction**: diffusion models and spatio-temporal modeling for 6G communications.
- **Audio Security**: audio deepfake detection and audio watermarking.
- **Information Theory**: rate-distortion theory for task-oriented compression.

# News ❗
<!-- TODO: keep the 3-5 most recent items; older news can be removed -->
- \[2026.09.06\] One paper accepted by **Knowledge-Based Systems (KBS)**.
- \[2026.09\] One paper accepted by **ICONIP 2026** (Springer CCIS).
- \[2026.05\] One paper accepted by **IEEE ICASSP 2026**.
- \[2025.10\] One paper accepted by **IEEE WCSP 2025**.

# Selected Publications
<!-- TODO: optional "Selected" subset; full list lives on the Publications page -->
- **Zhangyao Song**, et al. "TempoPINN: Physics-Informed Learning for Weather Forecasting." *ICONIP 2026*, Springer CCIS (to appear).
- **Zhangyao Song**, Xiang Zhang, Li Zhuang, et al. "Diffusion-Based Spatio-Temporal Channel Prediction via Non-Stationarity Decoupling." *IEEE Transactions on Cognitive Communications and Networking (TCCN)*, 2026. [[paper]](https://doi.org/10.1109/TCCN.2026.3685404)
- **Zhangyao Song**, Nanqing Jiang, Miaohong He, Xiaoyu Zhao, Tao Guo. "Channel, Trend and Periodic-Wise Representation Learning for Multivariate Long-Term Time Series Forecasting." *IEEE ICASSP*, 2026. [[paper]](https://doi.org/10.1109/ICASSP55912.2026.11464481)
- **Zhangyao Song**, Nanqing Jiang, Ziqiong Li, et al. "Frequency Interpolation with Period-aware Regularization for Robust Long-term Time Series Forecasting." *Knowledge-Based Systems (KBS)*, 2026 (accepted).
- **Zhangyao Song**, Xiang Zhang, Li Zhuang, et al. "Channel Prediction Based on Spatially Dependent Diffusion Models." *IEEE WCSP*, 2025. [[paper]](https://doi.org/10.1109/WCSP68525.2025.1010203)
- **Zhangyao Song**, Chaofeng Qu, Chao Zha, et al. "Adaptive Oscillatory-State Alignment for Time Series Forecasting." *arXiv preprint* 2026. [[paper]](https://arxiv.org/abs/2606.06010)

📄 A full list of my publications is available on the [Publications]({{ "/publications/" | relative_url }}) page and my [Google Scholar profile](https://scholar.google.com.hk/citations?user=KnRThI0AAAAJ).

# Projects
{% for post in site.portfolio reversed %}

<div class="project-row" style="display:flex; gap:2.2em; align-items:flex-start; margin:1.8em 0; flex-wrap:wrap;">
  <div style="flex:0 0 340px; max-width:100%; position:relative;">
    {% if post.venue %}<span style="position:absolute; top:-0.55em; left:0; z-index:2; background:#2f4b7c; color:#fff; padding:3px 12px; font-size:0.95em; font-weight:bold;">{{ post.venue }}</span>{% endif %}
    <img src="{{ '/images/' | append: post.header.teaser }}" alt="{{ post.title }}" style="width:100%; display:block; margin-top:0.9em; border:1px solid #e5e7eb; box-shadow:0 2px 8px rgba(0,0,0,0.12);">
  </div>
  <div style="flex:1; min-width:280px;">
    <h3 style="margin-top:0;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p style="margin:0.4em 0;">{{ post.authors }}</p>
    <p style="margin:0.4em 0;"><a href="{{ post.projecturl }}"><strong>Project</strong></a></p>
    <ul>
      <li><strong>Abstract:</strong> {{ post.abstract }}</li>
      <li><strong>Core Idea:</strong> {{ post.coreidea }}</li>
      <li><strong>Domain:</strong> {{ post.domain }}</li>
    </ul>
  </div>
</div>

{% endfor %}

# Education
- 2026.09 – present: **Ph.D. student**, School of Cyber Science and Engineering, Southeast University, Nanjing, China.
- 2023.09 – 2026.06: **M.S. in Cybersecurity**, School of Cyber Science and Engineering, Southeast University, Nanjing, China.
- 2019.09 – 2023.06: **B.S. in Computer Science**, Zhengzhou University, Zhengzhou, China.

# Honors and Awards
- Graduate Scholarship, Southeast University (2024, 2025, 2026).

# Academic Service
Reviewer for conferences and journals, including:

- **IEEE ICASSP** (IEEE International Conference on Acoustics, Speech and Signal Processing)
- **IEEE Transactions on Communications (TCOM)**
- **AAAI Conference on Artificial Intelligence**
- **International Conference on Neural Information Processing (ICONIP)**

# Internships
- 2025.04 – 2025.09: AI Algorithm Engineering Intern, Shenzhen Huasi Technology Co., Ltd., Shenzhen, China. Built LLM workflow prototypes for environmental monitoring and decision support on Dify; designed prediction models for CO2, SO2 and PM2.5.
