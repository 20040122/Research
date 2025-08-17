import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.DataFrame({
    "benchmark": ["605.mcf_s","641.leela_s","500.perlbench_r","508.namd_r","510.parest_r","523.xalancbmk_r","525.x264_r","538.imagick_r","511.povray_r","519.lbm_r","520.omnetpp_r","531.deepsjeng_r","544.nab_r","557.xz_r","600.perlbench_s","620.omnetpp_s","623.xalancbmk_s","625.x264_s","631.deepsjeng_s"],
    "baseline": [1508,1150,1000,613,1310,605,809,930,1477,644,795,697,1007,733,1011,797,696,808,797],
    "optimized": [1366,854,849,603,1283,625,806,786,1278,633,599,551,970,765,851,594,617,805,620]
})

# 去掉 None 的行
data = data.dropna(subset=["optimized"])

# 计算节省时间
data["saved"] = data["optimized"] - data["baseline"]

# 按 saved 排序（从节省少到多）
data = data.sort_values("saved", ascending=True)

# ===== 水平哑铃图 =====
fig, ax = plt.subplots(figsize=(8,10))

# 绘制水平线
ax.hlines(y=data["benchmark"], xmin=data["optimized"], xmax=data["baseline"], color="gray", alpha=0.5)

# 两端的点
ax.scatter(data["baseline"], data["benchmark"], color="red", label="Baseline")
ax.scatter(data["optimized"], data["benchmark"], color="green", label="Optimized")

# 在中间标注节省时间
for i, (b, o, s) in enumerate(zip(data["baseline"], data["optimized"], data["saved"])):
    mid = (b + o) / 2
    ax.text(mid, data["benchmark"].iloc[i], f"{s:.0f}s",
            ha='center', va='center', fontsize=8, color="blue")

ax.set_xlabel("Runtime")
ax.set_title("SPEC 2017 Benchmark Performance Comparison (Baseline vs Optimized)")
ax.legend()
plt.tight_layout()
plt.show()
