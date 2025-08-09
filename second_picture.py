import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.DataFrame({
    "benchmark": ["605.mcf_s","641.leela_s","500.perlbench_r","502.gcc_r","508.namd_r","510.parest_r","523.xalancbmk_r","525.x264_r","526.blender_r","538.imagick_r","511.povray_r","519.lbm_r","520.omnetpp_r","531.deepsjeng_r","544.nab_r","557.xz_r"],
    "baseline": [1508,1150,1000,649,613,1310,605,809,954,930,1477,644,795,697,1007,733],
    "optimized": [1382,853,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
})

# ===== (A) 哑铃图 - 纵向 =====
data["saved"] = data["baseline"] - data["optimized"]
data = data.sort_values("saved", ascending=True)
fig, ax = plt.subplots(figsize=(10,6))
ax.vlines(x=data["benchmark"], ymin=data["optimized"], ymax=data["baseline"], color="gray", alpha=0.5)
ax.scatter(data["benchmark"], data["baseline"], color="red", label="默认")
ax.scatter(data["benchmark"], data["optimized"], color="green", label="优化后")

ax.set_ylabel("运行时间 (秒)")
ax.set_title("时间对比 ")
ax.legend()
plt.xticks(rotation=45, ha='right')  # 横轴标签倾斜，防止重叠
plt.tight_layout()
plt.show()

