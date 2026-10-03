# 零基础 → Python → 强化学习/VLA 学习路线

> 面向：大一学过 C 语言（基本忘光）、想走 VLA+RL 方向的纯零基础。
> 目标：不绕路。Python 只学到「够用」，尽快进入真正的目标领域。
> 建议投入：每天 1.5–2 小时。下面的「周」都按这个强度算。

---

## 0. 先看结论：到底要花多久

| 阶段 | 内容 | 时长 | 能不能跳过 |
|---|---|---|---|
| 阶段 0 | 环境 + 工具（conda / VS Code / Jupyter / git） | 2–3 天 | 不能 |
| 阶段 1 | Python 核心语法 | 3 周 | 不能（但有 C 底子可提速） |
| 阶段 2 | 科学计算三件套 NumPy / pandas / Matplotlib | 2 周 | 不能 |
| 阶段 3 | PyTorch + 深度学习基础 | 4 周 | 不能 |
| 阶段 4 | 强化学习（对应你那张图的第 1 部分） | 8–10 周 | 这是终点之一 |
| 阶段 5 | 生成模型（扩散 / Flow Matching / DiT）+ VLA 架构 | 8–12 周 | 图里的第 2、3 部分 |

**大约 6 个月**可以走到「能复现 PPO、能读懂一篇 VLA 论文并跑通它的仓库」。
图里那三步是 12–18 个月量级的东西，不用急，前 5 个月的重心只有一个：**把 Python 和 PyTorch 变成肌肉记忆。**

---

## 1. 心态：有 C 基础，你是加速而不是从零

好消息：你懂变量、循环、函数、数组、指针、编译这些概念，**编程思维的坑你已经踩过一遍了**。Python 对你是「换一门语法 + 换一套工具链」。

坏消息：C 的习惯会拖你后腿，这几条要主动改：

| C 的习惯 | Python 的现实 | 怎么改 |
|---|---|---|
| 声明类型 `int a = 0;` | 不需要，变量是「贴标签」不是「盒子」 | 先接受，等以后用 type hints 补回来 |
| `for (int i=0; i<n; i++)` | `for x in list:` / `for i in range(n):` | 优先遍历元素，少用下标 |
| 手动管理内存、`malloc/free` | 有垃圾回收 | 但要小心**可变对象共享引用**（见下条） |
| 数组是连续内存 | `list` 是对象指针数组，慢 | 数值计算一律用 **NumPy 数组**，不要用 list 硬算 |
| 大括号 `{}` 定块 | 缩进定块 | 装好编辑器，统一 4 空格，别混 Tab |
| 编译报错才运行 | 解释执行，错在运行期才炸 | 养成随时运行、随时 print 的习惯 |

**最容易踩的 3 个 Python 特有的坑**（记下来，能省你两天）：

```python
# 坑 1：可变默认参数（C 里没有这个概念）
def f(x, acc=[]):      # 错！acc 会在多次调用间累积
    acc.append(x)
    return acc

def f(x, acc=None):    # 对
    if acc is None:
        acc = []
    acc.append(x)
    return acc

# 坑 2：浅拷贝 —— b 和 a 指向同一个列表
a = [1, 2, 3]
b = a                  # 不是复制！
b.append(4)            # a 也变成 [1,2,3,4]
b = a.copy()           # 这样才是复制

# 坑 3：整数除法和循环变量的作用域
print(7 / 2)           # 3.5，不是 3
print(7 // 2)          # 3，整除要用 //
for i in range(3):
    pass
print(i)               # 2，for 变量出了循环还在（C 里也是，但 Python 里更容易忘）
```

---

## 2. 阶段 0：环境（2–3 天，一次搞定，别在这耗太久）

### 你电脑的现状（已检查）
- ✅ Python **3.10** 已装在 `C:\Users\lenovo\AppData\Local\Programs\Python\Python310`
- ✅ 已有 numpy / pandas / matplotlib / openpyxl —— 阶段 2 的工具现成的
- ✅ 已有 git（`C:\Program Files\Git`）和 VS Code（`D:\Microsoft VS Code`）
- ❌ **没有 conda** —— 建议装一个，后面 PyTorch / gymnasium / mujoco 的版本冲突靠它救命
- ❌ **没有 PyTorch / gymnasium / stable-baselines3** —— 阶段 3 再装

### 要做的事
1. **装 Miniconda**（不是 Anaconda，Anaconda 太臃肿）：搜 `Miniconda Windows 安装`，勾选 "Add to PATH"。
2. **建一个专用环境**（别用 base 乱装）：
   ```bash
   conda create -n rl python=3.10 -y
   conda activate rl
   ```
   > 强化学习生态对 3.10 最友好，gymnasium / mujoco 都稳。不要追最新版 Python。
3. **VS Code 装 3 个扩展**：Python、Pylance、Jupyter。
4. **配 Jupyter**：`pip install jupyter`，以后学习笔记全部用 `.ipynb` 写，边讲边跑。
5. **过一遍命令行最小集**：`cd / ls / mkdir / cp / rm`、`pip install`、`python xxx.py`。Windows 上用 PowerShell 就行，别去折腾 WSL。

> ⚠️ 一个真实提醒：训练强化学习**很吃显卡**。先确认你的机器是 N 卡还是 A 卡——N 卡才能用 CUDA 加速 PyTorch。（阶段 1、2 完全不需要显卡，先学起来，到阶段 3 再确认。）

---

## 3. 阶段 1：Python 核心语法（约 30 天）

### 主课：尚硅谷《Python 核心全解》（新版）
- 官网（附源码/课件/笔记，**免费下载**）：https://www.atguigu.com/video/351/
- B 站搜 `尚硅谷 Python 核心全解`，认准官方账号

**为什么不用 2017 年的黑马 600 集**：那套课缺 f-string、列表推导式、装饰器、类型注解、生成器、虚拟环境。
尚硅谷这套是新版，**这些全都有**，而且只有 172 节（黑马是 536 个分 P，还含 100 集用不上的 Linux 命令）。

**取舍：看到第 142 节就停。**

| 节号 | 内容 | 你的处理 |
|---|---|---|
| 01–43 | 变量、数据类型、运算符、流程控制（if / while / for） | **精看** |
| 44–88 | 函数全套、列表、元组、集合、字典、数据容器通用操作 | **精看，这是地基** |
| 89–135 | 面向对象、lambda、**列表推导式**、**深浅拷贝**、闭包、**装饰器**、类型注解、异常、模块、**生成器** | **精看，含金量最高** |
| 136–141 | 文件与目录操作 | **精看** |
| 142–172 | 进程 / 线程 / GIL / 协程 / 异步 | **跳过**（和 RL 无关，以后要用再回来） |

**进度安排**：每天 10–15 节（每节 10 分钟左右，1.25–1.5 倍速）+ 当天敲一遍代码。约 30 天完成。

### 必须练出来的 10 件事（这是阶段 1 的真正验收标准）

1. `list` / `dict` / `set` / `tuple` 的增删改查和**推导式**
   ```python
   squares = [x**2 for x in range(10) if x % 2 == 0]      # 列表推导式
   d = {k: v for k, v in zip(keys, values)}               # 字典推导式
   ```
2. 切片和负索引：`a[1:5]`、`a[::-1]`（反转）、`a[-1]`（最后一个）
3. 函数进阶：`*args` / `**kwargs`、默认参数、`lambda`、返回多值
4. **类与继承**：会写 `class Env: def step(self, action): ...` 这种程度就够了
5. 异常处理：`try / except / finally`
6. 文件与路径：`open()`、`with` 语句、`pathlib.Path`（比 `os.path` 好用）
7. **标准库四件套**：`random`（RL 里天天用）、`math`、`collections`（`deque` 做经验回放）、`argparse`（跑实验传参数）
8. 虚拟环境 + `pip install / freeze`：知道为什么要用环境
9. **读文档的能力**：遇到不会的函数，第一反应是查 [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/index.html)，而不是搜「XX 怎么用」
10. 调试：会用 `print` 排查，也会在 VS Code 里打断点单步

### 补充资源（选一门当第二视角，别全看）
- [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/index.html) —— 最权威，语法查漏补缺用
- 小甲鱼《零基础入门学习Python》—— 讲课幽默、零基础友好，B 站搜 `小甲鱼 零基础入门学习Python`
- 廖雪峰 Python 教程 —— 文字版，适合当参考书
- 练习平台：[LeetCode 简单题](https://leetcode.cn/problemset/) 或 洛谷入门题，**每天 1 题**练手感（有 C 基础，你会觉得很轻松）

### ✅ 阶段 1 验收：能独立写出这两个东西
- 一个「学生成绩管理」小程序：字典存数据、函数分模块、能存读 JSON 文件、有异常处理
- 一个命令行小游戏（猜数字 / 21 点）：用类组织代码，用 `random`，用 `argparse` 接收参数

写不出来就说明前面的课白看了，回去补。

---

## 4. 阶段 2：科学计算三件套（2 周）

**为什么必须学**：强化学习的代码 90% 是「矩阵乘 + 随机采样 + 画曲线」。不会 NumPy，你连 PPO 的 loss 都算不出来。

### 课程
- [【2026最新版】Numpy+Pandas+Matplotlib——Python数据分析，数据可视化教程](https://www.bilibili.com/video/BV12Hac6fETB)（B站）
- [同系列另一版本](https://www.bilibili.com/video/BV1cDgE67Ej2)（标题就是「零基础入门到精通」，内容大同小异，挑一个看得顺眼的）
- 搜索关键词：`numpy pandas matplotlib 教程`

### 只学这些（别学成数据分析师）
**NumPy（重点，占 60% 时间）**
- 创建数组、`dtype`、`shape`、`reshape`
- 索引 / 切片 / 布尔索引：`a[a > 0]`
- **广播机制（broadcasting）** —— 最重要的一个概念，务必吃透
- 矩阵运算：`@`、`np.dot`、`np.linalg.inv`、`np.linalg.norm`
- 随机数：`np.random.randn`、`np.random.choice`（RL 里的动作采样全靠它）
- `np.sum(a, axis=0)` 里的 `axis` 到底是什么意思 —— 想清楚再往下走

**pandas（20%）**：`DataFrame` 读写 csv、筛选、`groupby`、画统计图就够了
**Matplotlib（20%）**：`plot`、`scatter`、`hist`、`xlabel/ylabel/legend/title`、`subplots`
> 强化学习里你 80% 的时间在画「reward 随 episode 的变化曲线」，这技能是刚需。

### ✅ 阶段 2 验收
- 用 NumPy **不用任何循环**（纯向量化）实现线性回归的批量梯度下降，并画出 loss 下降曲线
- 写一个 10000 步的一维随机游走模拟，画直方图看分布
- 把一份 csv 读进 pandas，做个 groupby 统计并画图

---

## 5. 阶段 3：PyTorch + 深度学习（4 周）

**这一步没有任何捷径。** 强化学习 = 深度学习 + 决策，网络都不会搭，后面全是玄学。

### 课程（两门配合看）
1. [刘二大人《PyTorch 深度学习实践》](https://www.bilibili.com/video/BV1Y7411d7Ys) —— B 站经典，极简、代码驱动、中文，适合第一遍。
   （若链接失效，B 站搜 `刘二大人 PyTorch深度学习实践`）
2. [李沐《动手学深度学习》(d2l)](https://courses.d2l.ai/zh-v2/) —— 配套 B 站官方视频，理论 + 代码最扎实的一门，**国内做 AI 的几乎人手一份**。B 站搜 `跟李沐学AI`。
   - 先看**前言 + 线性神经网络 + 多层感知机 + 深度学习计算**这几章
   - 卷积网络 / 注意力机制 先了解概念，阶段 5 再回头精读

### 要掌握的知识点
- **张量 tensor**：创建、`shape`、`device`（cpu/cuda）、和 numpy 互转
- **自动求导 autograd**：`requires_grad`、`backward()`、`.grad`、`zero_grad()`
- **`nn.Module`**：`__init__` 定义层、`forward` 定义计算流程
- **训练五步循环**（背下来）：
  ```python
  for epoch in range(n):
      y_pred = model(x)            # 1 前向
      loss = criterion(y_pred, y)  # 2 算损失
      optimizer.zero_grad()        # 3 梯度清零（忘了这步必错）
      loss.backward()              # 4 反向传播
      optimizer.step()             # 5 更新参数
  ```
- `Dataset` / `DataLoader`、`train()` / `eval()` / `torch.no_grad()`
- 保存加载模型、`.to(device)`、查看显存

### ✅ 阶段 3 验收
- **不用 PyTorch 的 autograd**，只用 numpy 手写一个两层 MLP 的反向传播（做完这个，你就真的懂神经网络了）
- 用 PyTorch 在 MNIST 或 CIFAR-10 上训练到 >95% / >70% 准确率
- 能解释清楚：为什么需要激活函数？`zero_grad()` 不写会怎样？`eval()` 有什么用？

---

## 6. 阶段 4：强化学习（8–10 周）—— 对应你图中第 1 部分

你那张图里推荐的资料是准确的，按这个顺序走：

### 主线课程
1. [《动手学强化学习》(张伟楠等) 配套视频](https://www.bilibili.com/video/BV186T7zeEzv) —— 上图作者推荐的第一顺位，B 站搜 `动手学强化学习`
   - [2025版 上交大张伟楠 动手学强化学习系列课程](https://www.bilibili.com/video/BV1Z6o9YeECB)（内容更全：含模仿学习、多智能体、AI Agent）
   - 官方在线阅读：`https://hrl.boyuai.com/`
2. [《EasyRL：强化学习教程》(蘑菇书) 配套视频](https://www.bilibili.com/video/BV1HZ4y1v7eX)｜[作者手把手实现算法](https://www.bilibili.com/video/BV1Pd4y1u77J)
   - 开源书：[datawhalechina/easy-rl](https://github.com/datawhalechina/easy-rl)
3. 李宏毅《深度强化学习》—— 理论最清晰，B 站搜 `李宏毅 强化学习`；配套笔记 [leedeeprl-notes](https://github.com/yxjun1984/leedeeprl-notes)
4. David Silver《Reinforcement Learning》公开课 —— 图里提到的深度补充，英文，等前三个看完再上

### 学习顺序（严格按这个来，别跳）
| 顺序 | 内容 | 关键概念 | 代码产出 |
|---|---|---|---|
| 1 | gymnasium 环境 + MDP | 状态/动作/奖励/折扣因子、`reset()`/`step()` | 跑通 CartPole 随机策略 |
| 2 | 动态规划 | 贝尔曼方程、策略迭代、价值迭代 | 手写价值迭代解 FrozenLake |
| 3 | 无模型预测 | MC、TD、Q-learning、Sarsa、on/off-policy 区别 | 表格版 Q-learning 解 FrozenLake |
| 4 | 函数逼近 → **DQN** | 经验回放、目标网络、ε-greedy | DQN 解 CartPole（能稳定收敛） |
| 5 | **策略梯度** | 策略梯度定理、REINFORCE、基线、优势函数 | REINFORCE 解 CartPole |
| 6 | **Actor-Critic** | A2C、GAE、优势函数到底在干嘛 | A2C 解 LunarLander |
| 7 | **PPO**（最重要） | clip 目标、重要性采样、TRPO 的关系 | PPO 解 LunarLander/MuJoCo |
| 8 | **SAC**（连续控制） | 最大熵 RL、双 Q、重参数化 | SAC 解 Pendulum / HalfCheetah |
| 9 | 模仿学习 | 行为克隆、DAgger | 从专家轨迹学 CartPole |

> 图里说的「**吃透 Actor-Critic 框架的运行机制**」是重点中的重点。PPO、SAC、A3C 全是它的变体，这一个吃透，后面全是换皮。

### 必做的项目实操（图里 B 条）
- 目标：**复现 PPO / SAC 的训练曲线**，不是「能跑」，是「能解释每一步超参数为什么这么设」
- 参考实现：[CleanRL](https://github.com/vwxyzjn/cleanrl)（单文件实现，最适合逐行读）、[Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3)（工程规范）
- 图里提到的 **RLinf** 开源框架，等你能手写 PPO 之后再去上手，否则只会变成「调参侠」
- 环境从 `CartPole → LunarLander → MuJoCo(HalfCheetah)` 逐步升级

### 数学补充（穿插着补，不用先学完）
- 线性代数：矩阵乘法、特征值、范数
- 概率论：期望、方差、条件期望（贝尔曼方程的核心）、重要性采样
- 微积分：链式法则、梯度、雅可比（策略梯度推导要用）
- 推荐：《强化学习的数学原理》(赵世钰) + 配套 B 站视频，搜 `赵世钰 强化学习的数学原理`。讲贝尔曼最优公式讲得最清楚的一门。

### ⚠️ 关于这张图的诚实提醒
这张《VLA+RL 入门指南》看起来是 AI 生成的「技能清单」类内容（排版和话术特征很明显），上面那行「**（招人需求很大）**」更像是引流话术，不要当成某家公司的招聘要求。里面推荐的书和课是靠谱的，但**别被它吓到**：它描述的是 12–18 个月、甚至研究生阶段的目标。你的任务只有一件——把 Python 和 PyTorch 学扎实。

---

## 7. 阶段 5：生成模型 + VLA（8–12 周，图中的第 2、3 部分）

这部分**不要现在开始**，写在这是让你知道路还有多远、中途不慌。

### 生成模型基础（第 2 部分）
| 主题 | 图里的链路 | 学习资源建议 |
|---|---|---|
| 扩散模型 | DDPM → DDIM → Classifier-Free Guidance → DiT | 李宏毅扩散模型系列；B 站搜 `扩散模型 DDPM 从零实现`、`李宏毅 扩散模型`；《扩散模型：原理与实践》 |
| 流匹配 | Flow Matching，ODE 概率路径 | B 站搜 `Flow Matching 流匹配 教程`；斯坦福 CS236 |
| 为什么当动作头 | 多模态动作分布、比直接坐标回归稳 | 读 π0、OpenVLA 论文的动作头部分 |

> 图里说 Flow Matching「推理阶段一般需要 10 步左右」，这是 VLA 里的常见配置（如 π0 用 10 步）。等你到这一步再抠这些细节。

### VLA 架构（第 3 部分）
- 三段式：**视觉编码器 → 预训练语言模型 → 动作输出头**（可选扩散 / 流匹配 / 离散 token）
- 训练链路：基座预训练 → 监督微调 SFT → 后训练强化学习（RLHF / 偏好对齐）
- 图里提到的「分布外泛化弱、开环误差累积、视觉层面虚假关联」是当前真实的研究难点，也是 RL 的用武之地
- 动手起点：跑通 [OpenVLA](https://github.com/openvla/openvla) 或 π0 的推理 demo，再看 [Dawn-1/2](https://github.com/RealVLA/Dawn-1)（多模态 VLA 基座模型）

---

## 8. 每周节奏模板（照抄就行）

| 时间 | 做什么 |
|---|---|
| 周一–周五 每天 1.5–2h | 40 分钟看视频课 → 60 分钟**自己敲代码**（关掉视频凭记忆写）→ 20 分钟记笔记（写成 `.ipynb`，带代码和图） |
| 周六 2–3h | 做本周阶段项目 / 补没懂的坑 |
| 周日 1h | 复习 + 把代码推到 GitHub + 写本周总结 |

**GitHub 从第 1 周就开始用。** 你现在 `git` 已经装好了。每个阶段的代码、笔记、踩坑记录都提交上去——半年后这就是你最好的简历。

---

## 9. 十条避坑建议（血泪浓缩）

1. **只看不写 = 没学。** 视频看完必须关掉自己重敲一遍，报错了再回头看。
2. **不要追求「学完 Python 再学别的」。** Python 是交通工具，不是目的地。够用就上车。
3. **不要一开始就用 Stable-Baselines3 跑 PPO 然后觉得自己会 RL 了。** 手写一遍 DQN，胜过跑十遍别人的 PPO。
4. **不要收集课程。** 收藏夹里躺 20 门课的人，通常一门都没看完。每个阶段选 1 门主课 + 1 门备选，看完再换。
5. **环境隔离是保命的。** 一个项目一个 conda 环境，出问题直接删了重建，比修环境快 10 倍。
6. **报错先读报错信息。** Python 的 traceback 会告诉你具体哪一行、什么类型错误，90% 的问题看最后一行就能解决。
7. **不要碰**：爬虫、Web 开发、Django、MySQL、数据分析师技能树。它们跟你的目标无关，是最大的时间黑洞。
8. **卡住超过 1 小时就问。** 问 AI、问群、问搜索引擎都行。一个人闷头卡三天是新手最大的浪费。
9. **数学和代码同步推进。** 把数学全学完再学 RL 是伪命题——你会忘，而且没有应用场景记不住。
10. **接受「看不懂」是常态。** 第一遍看 PPO 论文看不懂是正常的。先看代码跑通，再回头读理论，效果翻倍。

---

## 10. 资源速查表

### B 站（按学习顺序）
| 阶段 | 课程 | 链接 |
|---|---|---|
| 1 | **尚硅谷《Python 核心全解》**（新版，含 f-string/推导式/装饰器/生成器） | https://www.atguigu.com/video/351/ |
| 1 | 黑马 600 集（2017，仅作对照参考，分P目录在 参考/） | https://www.bilibili.com/video/BV1ex411x7Em |
| 1 | 小甲鱼 零基础入门学习Python | B站搜「小甲鱼 零基础入门学习Python」 |
| 2 | Numpy+Pandas+Matplotlib | https://www.bilibili.com/video/BV12Hac6fETB |
| 3 | 刘二大人 PyTorch 深度学习实践 | https://www.bilibili.com/video/BV1Y7411d7Ys |
| 3 | 跟李沐学AI《动手学深度学习》 | B站搜「跟李沐学AI」 |
| 4 | 上交大 动手学强化学习（张伟楠） | https://www.bilibili.com/video/BV186T7zeEzv ｜ https://www.bilibili.com/video/BV1Z6o9YeECB |
| 4 | 蘑菇书 EasyRL | https://www.bilibili.com/video/BV1HZ4y1v7eX ｜ https://www.bilibili.com/video/BV1Pd4y1u77J |
| 4 | 李宏毅 深度强化学习 | B站搜「李宏毅 强化学习」 |
| 4 | 赵世钰 强化学习的数学原理 | B站搜「赵世钰 强化学习的数学原理」 |
| 5 | 扩散模型 / Flow Matching | B站搜「扩散模型 DDPM 从零实现」「Flow Matching 流匹配」 |

> B 站课程会下架、会换 UP 主重传，**链接失效就用标题 + 关键词在 B 站搜**，同名课程一般都有。

### 书
- 《Python编程：从入门到实践》—— 阶段 1 纸质书首选
- 《动手学深度学习》(李沐) —— 在线免费：https://zh.d2l.ai
- 《动手学强化学习》(张伟楠) —— 在线免费：https://hrl.boyuai.com
- 《EasyRL 强化学习教程》(蘑菇书) —— 开源：https://github.com/datawhalechina/easy-rl
- 《强化学习的数学原理》(赵世钰)
- Sutton & Barto《Reinforcement Learning: An Introduction》—— 理论圣经，第二版免费 PDF，等你 RL 入门后再啃

### 代码仓库
- https://github.com/vwxyzjn/cleanrl —— 单文件 RL 算法实现，最适合逐行精读
- https://github.com/DLR-RM/stable-baselines3 —— 工程级 RL 库
- https://github.com/datawhalechina/easy-rl —— 蘑菇书配套代码
- https://github.com/openvla/openvla ｜ https://github.com/RealVLA/Dawn-1 —— VLA 方向

---

## 11. 你现在的第一步（今天就做）

1. 装 Miniconda，建 `rl` 环境（30 分钟）
2. 打开 **尚硅谷《Python 核心全解》**（https://www.atguigu.com/video/351/ 或 B 站搜同名），从第 01 节开始看
3. 新建 `learning-log.ipynb`，把今天学的代码敲一遍
4. 在桌面建个 `python-learning` 文件夹，`git init`，今天就把第一份笔记提交上去

**别做计划了，打开视频开始看吧。**
