# 04 - 强化学习（D093–D104）

**主课**：[蘑菇书 EasyRL 配套视频](https://www.bilibili.com/video/BV1HZ4y1v7eX)（理论）+ [作者手把手实现算法](https://www.bilibili.com/video/BV1Pd4y1u77J)（代码）
**辅课**：[上交大张伟楠 动手学强化学习](https://www.bilibili.com/video/BV186T7zeEzv)
**开源书**：https://hrl.boyuai.com ｜ https://github.com/datawhalechina/easy-rl
**参考实现（禁止直接抄，只在卡住时看）**：https://github.com/vwxyzjn/cleanrl

## D093 先装环境

```bash
conda activate rl
pip install "gymnasium[box2d]" torch matplotlib
# 装不上 box2d 就先 pip install swig 再重试

# 验证
python -c "import gymnasium as gym; e = gym.make('CartPole-v1'); print(e.reset())"
```

## 三个子文件夹

| 文件夹 | 内容 | 对应天数 |
|---|---|---|
| `01-DQN/` | DQN 原理、经验回放缓冲区、训练脚本 | D096–D098 |
| `02-策略梯度/` | REINFORCE、Actor-Critic、A2C、GAE | D099–D101 |
| `03-PPO/` | PPO 的 clip 目标、训练与调参 | D102–D104 |

## 建议的实现顺序（别跳）

```
表格版 Q-learning 解 FrozenLake        ← D096，先建立直觉
      ↓
DQN 解 CartPole（跑到 475+ 分）        ← D098
      ↓
REINFORCE 解 CartPole                  ← D099
      ↓
A2C 解 CartPole                        ← D100
      ↓
GAE → PPO 解 LunarLander               ← D102–D104  ★ 最终交付物
```

## 核心概念自检清单

- [ ] 能默写贝尔曼方程 V(s) 和 Q(s,a)
- [ ] 能说清 **on-policy 和 off-policy** 的区别（举 DQN 和 PPO 为例）
- [ ] 能解释为什么要**经验回放**、为什么要**目标网络**
- [ ] 能说清 **Actor 和 Critic 各在干什么**
- [ ] 能解释**优势函数** A(s,a) 比原始回报好在哪里
- [ ] 能手推 **PPO 的 clip 目标函数**，并说明它为什么能防止更新过大
- [ ] 知道 **GAE 的 λ** 控制什么
- [ ] 能看训练曲线诊断问题（不收敛时依次怀疑：学习率 → 奖励尺度 → 探索不足 → 优势估计）

## 🔴 最终交付物（D104）

**自己写的 PPO（不是调库、不是抄的）在 LunarLander 上跑出稳定上升的平均回报曲线。**

连同 `dqn.py` / `reinforce.py` / `a2c.py` / `ppo.py` 四个文件都要有 README 说明怎么跑。

> ⚠️ **PPO 一次调不出来是正常的**，这是 RL 界的经典难题。卡住了先降到 CartPole，把 LunarLander 放到 2 月。
> 记住：**曲线是结果，理解才是目的。** 曲线没出来但每一步都能解释清楚，也不算失败。

## 训练日志规范（重要）

每个实验单独建文件夹，把超参数和结果存下来：

```
03-PPO/
├── ppo.py
├── config.yaml            ← 超参数（lr / clip / epochs / batch / gamma / lam）
├── README.md              ← 怎么跑 + 最终得分
└── runs/2027-01-13_2003/  ← 曲线上图 + 训练日志
```

> 不记录超参数的实验等于没做。三天后你不可能记得当时 lr 设的是 3e-4 还是 1e-3。
