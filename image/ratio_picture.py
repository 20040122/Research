import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 美观中文字体
plt.rcParams['axes.unicode_minus'] = False

# baseline ratio
baseline_df = pd.DataFrame({
    "benchmark": ["605.mcf_s","641.leela_s","500.perlbench_r","508.namd_r","510.parest_r","523.xalancbmk_r","525.x264_r","538.imagick_r","511.povray_r","519.lbm_r","520.omnetpp_r","531.deepsjeng_r","544.nab_r","557.xz_r","600.perlbench_s","620.omnetpp_s","623.xalancbmk_s","625.x264_s","631.deepsjeng_s"],
    "ratio_before": [3.13,1.48,1.59,1.55,2.00,1.74,2.16,2.67,1.58,1.64,1.65,1.64,1.67,1.47,1.76,2.05,2.04,2.18,1.80]
})

# optimized ratio
optimized_df = pd.DataFrame({
    "benchmark": ["605.mcf_s","641.leela_s","500.perlbench_r","508.namd_r","510.parest_r","523.xalancbmk_r","525.x264_r","538.imagick_r","511.povray_r","519.lbm_r","520.omnetpp_r","531.deepsjeng_r","544.nab_r","557.xz_r","600.perlbench_s","620.omnetpp_s","623.xalancbmk_s","625.x264_s","631.deepsjeng_s"],
    "ratio_after": [3.46,2.00,1.87,1.58,2.04,1.69,2.17,3.16,1.83,1.66,2.19,2.08,1.73,1.41,2.09,2.74,2.30,2.19,2.31]
})

# 合并
df = pd.merge(baseline_df, optimized_df, on="benchmark")

# 去掉 NaN
df = df.dropna(subset=["ratio_before", "ratio_after"])

# 按优化前 ratio 排序
df = df.sort_values("ratio_before", ascending=True)

# 绘图
fig, ax = plt.subplots(figsize=(10,6))
bar_width = 0.35
x = range(len(df))

ax.bar(x, df["ratio_before"], width=bar_width, label="Baseline", color="#5B9BD5")
ax.bar([i + bar_width for i in x], df["ratio_after"], width=bar_width, label="Optimized", color="#ED7D31")

# 细节
ax.set_xticks([i + bar_width/2 for i in x])
ax.set_xticklabels(df["benchmark"], rotation=45, ha="right")
ax.set_ylabel("Ratio")
ax.set_title("SPEC 2017 Benchmark Performance Comparison (Baseline vs Optimized)")
ax.legend()

# 数值标签
for i, v in enumerate(df["ratio_before"]):
    ax.text(i, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=8)
for i, v in enumerate(df["ratio_after"]):
    ax.text(i + bar_width, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=8)

plt.tight_layout()
plt.show()
