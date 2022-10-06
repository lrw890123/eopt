## 目标函数 ##

$$
\max \sum_{s \in S}C_s(Time-(\sum_{i \in N_s}\tau_i+\sum_{i\in N_s}\sum_{j \in N_s}s_{ij}z_{ij}))o_s
$$



## 约束 ##

1. 被修复的装备必须分配一个维修队伍：

$$
\sum_{p \in P}y_{ip}=x_i,\quad \forall i \in N
$$

2. 选择某个装备作为维修人员出发后的第一站：

$$
y_{ip}^{,} \le y_{ip}, \quad \forall i \in N, p \in P \\
\sum_{i \in N}y_{ip}^{,}=1,\quad \forall p \in P
$$

3.  选择某个装备作为维修人员出发后的最后一站：

$$
y_{ip}^{,,} \le y_{ip}, \quad \forall i \in N, p \in P\\
\sum_{i \in N}y_{ip}^{,,}=1,\quad \forall p \in P
$$

4. 建立维修人员的维修路径：
   $$
   \sum_{p \in P}y_{ip}^{,}+\sum_{j \in N, j \neq i}z_{ji} = x_i, \quad \forall i \in N\\
   y_{ip}-y_{jp} \ge z_{ij}-1, \quad \forall i,j \in N;p \in P:i \neq j\\
   \sum_{p \in P}y_{ip}^{,,}+\sum_{j \in N, j \neq i}z_{ij} = x_i, \quad \forall i \in N\\
   $$
   
5. 系统恢复约束：
   $$
   o_s \le x_i, \quad \forall s \in S, i \in N_s
   $$
   
6. 定义变量的值域：
   $$
   y_{ip},y_{ip}^,,y_{ip}^{,,},z_{ij},x_i,o_s \in \{0,1\}, \quad \forall i,j \in N; s \in S; p \in P
   $$

