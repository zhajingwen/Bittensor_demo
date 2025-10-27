import bittensor as bt

# 创建子网连接
subtensor = bt.subtensor(network='finney')  # 主网

# 查询 Subnet 55 信息
metagraph = subtensor.metagraph(netuid=55)

print(f"Subnet 55 有 {len(metagraph.neurons)} 个神经元")
