# python-learning

104 天：从 0 基础到能手写 PPO。

**起点**：2026-10-03 ｜ **目标**：2027-01-14 跑通自己写的 PPO（LunarLander）
**主计划**：[`00-计划/104天作战计划-每日打卡表.md`](00-计划/104天作战计划-每日打卡表.md)

---

## 这个仓库是什么

一个本科生的 Python → PyTorch → 强化学习 学习仓库，每天一个 commit。
计划文档、每日代码、学习笔记、踩坑记录全在这里，**只有一个入口**。

## 目录结构

| 目录 | 放什么 | 对应天数 |
|---|---|---|
| `00-计划/` | 学习路线 + 104 天作战计划（每天在这里打勾） | — |
| `01-Python基础/` | Python 语法练习，按周分文件夹 | D001–D030 |
| `01-Python基础/项目-学生成绩管理/` | 第一阶段综合项目 | D028–D30 |
| `02-NumPy与数据分析/` | NumPy / pandas / Matplotlib 练习 | D030–D043 |
| `03-PyTorch与深度学习/` | 张量、autograd、MNIST、CIFAR-10、手写反向传播 | D044–D064 |
| `04-强化学习/` | DQN / 策略梯度 / PPO | D093–D104 |
| `notes/` | `learning-log.ipynb` 每日笔记 | 全程 |
| `参考/` | 论文、别人代码的阅读笔记 | 全程 |

## 每天怎么用这个仓库（5 步）

```bash
# 0. 进环境、进目录
conda activate rl
cd /d D:\code\python-learning

# 1. 看一眼今天的任务
#    打开 00-计划/104天作战计划-每日打卡表.md，找到今天的 Day

# 2. 写代码（放在对应的周文件夹里，文件名带 Day 编号）
#    例：01-Python基础/week1/D003_成绩等级.py

# 3. 写笔记（打开 notes/learning-log.ipynb，追加今天的记录）

# 4. 打勾（在打卡表里把 [ ] 改成 [x]）

# 5. 提交
git add .
git commit -m "D003: if 判断 + 成绩等级判定"
```

## 必须记住的 5 条命令

| 命令 | 作用 |
|---|---|
| `git status` | 看现在有哪些改动（最常用，不确定就敲它） |
| `git add .` | 把当前所有改动加入本次提交 |
| `git commit -m "说明"` | 提交，说明写清是哪个 Day、做了什么 |
| `git log --oneline` | 看历史提交（能看到自己的打卡记录） |
| `git diff` | 看具体改了哪几行 |

## commit message 格式

```
D012: 函数进阶-闭包与装饰器
D029: 完成学生成绩管理系统 v1.0
D098: DQN 解 CartPole 收敛到 492 分
```

**每天一个 commit。** 断更了不要伪造记录，空着就行——`git log` 里的日期是给你自己看的诚实记录。

## 环境

```bash
conda create -n rl python=3.10 -y
conda activate rl
```

| 阶段 | 需要装的东西 |
|---|---|
| 阶段 1 | 无需额外安装（Python 自带够用） |
| 阶段 2 | `pip install jupyter numpy pandas matplotlib` |
| 阶段 3 | PyTorch（见 D044），`pip install torch torchvision` |
| 阶段 4 | `pip install gymnasium[box2d] torch matplotlib` |

> 硬件：RTX 4070 Laptop (8GB) + Python 3.10。CUDA 可用，MuJoCo 级别的训练没问题。

---

## 进度

- [ ] 第一阶段 Python 核心语法（D001–D030）
- [ ] 第二阶段 NumPy / pandas / Matplotlib（D030–D043）
- [ ] 第三阶段 PyTorch + 深度学习（D044–D064）
- [ ] 复习周 + 考试周（D065–D092）
- [ ] 第四阶段 强化学习冲刺（D093–D104）
- [ ] 🎯 **自己写的 PPO 在 LunarLander 上跑出上升曲线**

**最后更新**：2026-10-03
