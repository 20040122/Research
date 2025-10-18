from pykeen.pipeline import pipeline

result = pipeline(
    model='TransE',
    dataset='nations',
)
# 打印评估结果
print(result.metric_results.to_df())

# 或者查看更详细的模型表现
print(result.get_metric('mean_rank'))
print(result.get_metric('hits_at_10'))

# 如果想看模型、数据、训练参数等信息
print(result)