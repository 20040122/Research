import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 美观中文字体
plt.rcParams['axes.unicode_minus'] = False

# baseline ratio
baseline_df = pd.DataFrame({
    "benchmark": ["605.mcf_s","641.leela_s","500.perlbench_r","502.gcc_r","508.namd_r","510.parest_r","523.xalancbmk_r","525.x264_r","526.blender_r","538.imagick_r","511.povray_r","519.lbm_r","520.omnetpp_r","531.deepsjeng_r","544.nab_r","557.xz_r"],
    "ratio_before": [3.13,1.48,1.59,2.18,1.55,2.00,1.74,2.16,1.60,2.67,1.58,1.64,1.65,1.64,1.67,1.47]
})

# optimized ratio
optimized_df = pd.DataFrame({
    "benchmark": ["605.mcf_s","641.leela_s","500.perlbench_r","502.gcc_r","508.namd_r","510.parest_r","523.xalancbmk_r","525.x264_r","526.blender_r","538.imagick_r","511.povray_r","519.lbm_r","520.omnetpp_r","531.deepsjeng_r","544.nab_r","557.xz_r"],
    "ratio_after": [3.42,2.00,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
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

ax.bar(x, df["ratio_before"], width=bar_width, label="默认", color="#5B9BD5")
ax.bar([i + bar_width for i in x], df["ratio_after"], width=bar_width, label="优化后", color="#ED7D31")

# 细节
ax.set_xticks([i + bar_width/2 for i in x])
ax.set_xticklabels(df["benchmark"], rotation=45, ha="right")
ax.set_ylabel("Ratio")
ax.set_title("Ratio 对比图")
ax.legend()

# 数值标签
for i, v in enumerate(df["ratio_before"]):
    ax.text(i, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=8)
for i, v in enumerate(df["ratio_after"]):
    ax.text(i + bar_width, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=8)

plt.tight_layout()
plt.show()
