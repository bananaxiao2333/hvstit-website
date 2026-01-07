# KS IA - 维科火箭模型项目燃料改良方案

## 项目概述

```mermaid
graph LR
    A[KNSB燃料改良项目] --> B[氧化剂改良]
    A --> C[燃料改良]
    A --> D[添加剂与工艺]

    B --> B1[粒度控制 A1]
    B --> B2[氧化剂掺杂 A2]

    C --> C1[混合替换 B1]
    C --> C2[金属添加 B2]

    D --> D1[增塑剂 C1]
    D --> D2[固化剂 C2]
    D --> D3[工艺改进 C3]
```

## 成分定义

| 符号  | 成分     | 说明             |
| ----- | -------- | ---------------- |
| K     | 硝酸钾   | 主要氧化剂       |
| N/S/B | 山梨糖醇 | 主要燃料和粘结剂 |

!!! note "配方说明"
    经典 KNSB 配方为 65%硝酸钾 + 35%山梨糖醇，是一种安全稳定的糖基推进剂。

## 改良方案详解

### 氧化剂改良路径

```mermaid
flowchart TD
    Start[氧化剂改良] --> Method1
    Start --> Method2

    subgraph Method1 [A1 粒度控制]
        A1_1[使用更细硝酸钾粉末] --> A1_2[325目以上粉末]
        A1_1 --> A1_3[球磨机加工]
    end

    subgraph Method2 [A2 氧化剂掺杂]
        A2_1[添加金属氧化物] --> A2_2[氧化铁催化剂]
        A2_2 --> A2_3[稳定燃烧]
        A2_2 --> A2_4[提高燃速]
    end
```

### 燃料改良方案比较

```mermaid
graph LR
    A[燃料改良] --> B[成本优化]
    A --> C[性能提升]

    B --> B1[蔗糖/葡萄糖替换]
    B1 --> B1_1[优点: 降低成本]
    B1 --> B1_2[缺点: 可能降低燃速]

    C --> C1[赤藓糖醇替换]
    C1 --> C1_1[优点: 更高比冲]
    C1 --> C1_2[缺点: 价格高昂]

    C --> C2[添加铝粉]
    C2 --> C2_1[优点: 显著提高性能]
    C2 --> C2_2[挑战: 工艺复杂]
```

## 方案 A 具体配方

### 成分配比

```mermaid
pie title
    "硝酸钾" : 65
    "山梨糖醇" : 30
    "铝粉" : 2
    "氧化铁" : 1
    "硬脂酸" : 0.5
```

### 反应过程分析

```mermaid
sequenceDiagram
    participant KNO3 as 硝酸钾
    participant Fe2O3 as 氧化铁催化剂
    participant Al as 铝粉
    participant Sorbitol as 山梨糖醇

    Fe2O3->>KNO3: 催化分解
    KNO3->>KNO3: 释放O₂ + N₂
    KNO3->>Al: 优先供氧
    Al->>Al: 氧化为Al₂O₃
    KNO3->>Sorbitol: 剩余氧气
    Sorbitol->>Sorbitol: 不完全氧化
```

## 化学反应计算

### 摩尔数分析

```mermaid
graph TB
    Base[100克药柱基准] --> Comp1
    Base --> Comp2
    Base --> Comp3
    Base --> Comp4

    Comp1[硝酸钾 65g] --> Calc1[0.643 mol]
    Comp2[山梨糖醇 30g] --> Calc2[0.165 mol]
    Comp3[铝粉 2g] --> Calc3[0.074 mol]
    Comp4[硬脂酸 0.5g] --> Calc4[0.00176 mol]
```

### 氧平衡分析

```mermaid
graph LR
    O2_Need[总需氧量] --> Need_Calc[1.458 mol O₂]
    O2_Supply[总供氧量] --> Supply_Calc[0.804 mol O₂]

    Need_Calc --> Compare{比较}
    Supply_Calc --> Compare

    Compare --> Result[负氧平衡配方]
```

!!! warning "重要提示"
    这是一个负氧平衡配方，依赖不完全燃烧产物获得更高比冲，但需要精确控制工艺条件。

## 工艺流程图

```mermaid
flowchart TD
    Start[开始制备] --> Step1
    Step1[干燥成分混合] --> Step2
    Step2[加热熔化山梨糖醇] --> Step3
    Step3[加入混合粉末] --> Step4
    Step4[搅拌均匀] --> Step5
    Step5[精确控温固化] --> End[成品]

    Note1[注意防焦化] -.-> Step5
```

## 总结

```mermaid
mindmap
  root((KNSB改良方案))
    性能提升
      更高比冲
      更快燃速
      更好稳定性
    工艺优化
      加工更容易
      质量控制更精确
      安全性更高
    应用效果
      吸引优质成员
      提升小组形象
      促进科研推广
```

!!! success "项目成果"
    该改良方案有效提升了推进剂性能，为科研小组的对外推广和人才吸纳提供了有力技术支持。
