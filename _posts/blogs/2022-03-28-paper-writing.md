---
layout: article
title: 会议短论文写作经验
mathjax: true
aside:
  toc: true
date: 2022-03-27 11:23:14 +0800
category: [Blog]
---

写第一篇论文时肯定没有人来手把手指导怎么写论文，自己主要从知乎和学校的`学术论文写作`英语课上去找论文写作的感觉。对于我这种很久没有经历过英文写作训练的学生来说，写论文的捷径就是模仿，套模板。把和自己工作最相关的论文拿来反复读反复研究，从句子到段落上都进行模仿。段落与段落之间也进行模仿，逻辑第一，循循善诱，有理有据。

<!--more-->

# **一 Abstraction 摘要**
                                                                                                                                        
摘要里面大概要写出下列3点内容
- 介绍问题背景，你研究工作所属的领域，处理这个问题的目的目标。
- 介绍你研究工作的内容，用了什么方法。
- 得到什么结果，有什么发现。

摘要是整篇论文的简短总结，里面写的内容会和正文里的产生重复，所以摘要里面的内容都尽量以最精简的句子来写出上面的3点内容，并且摘要只是一个全篇的总结，不需要在摘要中写出细节。

### （一）问题背景，解决这个问题的意义

1. What problem are you trying to solve?
你处理的问题是什么，如果解决的问题大多数人没有接触过，在第一句简单介绍这个Topic，可以由大家都比较熟悉的研究点引申出来。拿这篇关于`开放集领域自适应`的摘要开头部分做例子：

>Existing domain adaptation methods generally assume different domains have the identical label space, which is quite restrict for real world applications. In this paper, we focus on a more realistic and challenging case of open set domain adaptation.

2. Why did you undertake the study.
为什么做这个课题，就是阐述这篇工作的意义。比如上一个摘要的例子中`We focus on a more realistic and challenging case of open set domain adaptation`就说明`开放集领域自适应`更加符合现实情况的需要，体现了这个研究点的意义。

还有一些说明文章主题的常用句型可以写进论文摘要当中，当然从最相关的论文中模仿句型是最好的。

>1）The papers examines …… and considers …… | 本文研究了……并考虑了……。
2）The authous consider two specific subjects which …… | 作者考虑了两个……的专题。
3）This articles discusses the reasons for …… and offers an insight into …… | 本文研讨了……的原因并阐明了对……的观点。
4）The influence of …… on …… is investigated. | 研讨了……对……的影响。
5）This paper analyzes some important characteristics of …… | 本文分析了……的一些重要特征。

说明研究目的的句型
>1）领域自适应论文中的例子This work is driven by the question whether or not it is beneficial to operate the source images to another image domain as close to the target as possible.
2）One of the purposes of this study is to ...本研究的一个目的是：
3）This paper seeks to justify …… in terms of …… 本文目标是从……角度来论证……
4）The aim of this study is to carry out analysis for …… 本项研究的目的是对……进行分析
5）The primary objective of the study was to determine 本项研究的主要目标是确定……

### （二）介绍研究工作，用了什么方法

用最简短的语句简短阐述提出方法的大概思路。模型结构如果分成多个部分，每个部分用一句话说就差不多。开头写“本文提出用……方法解决……问题，我们的方法由几个部分组成，第一个部分用来……，第二个部分用来……”。

> 1）We propose to address the …… by doing sth. ……. Our approach, called "XXX", consists of two components.
> 2）To tackle this challenge/To achieve this goal, we propose a new approach called "XXX".
> 3）The method is based on …… 
> 4）Two basic technologies are used to lay down …… 
> 5）The experiments on … have been carried out using/with …
> 6）Different from the softmax cross-entropy loss, our proposal is established on the assumption that the …… 

### （三）得到什么结果，有什么发现

摘要最后的一部分，一般是“我们提出的方法取得好的效果”，“我们方法SOTA”，“在多个数据集上的实验证明了我们方法的有效性”，“我们方法在代表性数据集上比SOTA方法好”,"实验描述了提出方法是怎么作用的，然后通过什么展示了方法的有效性。"

>1）The results found that ……
2）A theoretical model has been developed to predict ……
3）The paper concludes that ……
4）Extensive experiments on multiple benchmark datasets demonstrate the effectiveness of our approach.
5）Our experiment also demonstrates that an image-to-image translation component can further improve the decision boundaries for ……

**摘要一般放在整篇论文写作工作的最后，当然也可以先写一个摘要给自己的论文和实验部分定一个框架，完成论文的剩余部分后肯定还会对摘要的内容进行修改或补充的。**

我在写摘要的时候也是参考了很多相关论文的摘要结构（论文每个部分都模仿了其他论文的写作结构）。阅读其他论文的摘要，在其他摘要上找到上述3个部分。


![](https://s1.ax1x.com/2020/05/14/YBLMNT.png)


# **二 Introduction 引言**

写introduction的时候主要参考了知乎上的这一篇[怎样写好英文论文的Introduction部分](https://www.zhihu.com/question/49355121/answer/322451208)。Introduction和Abstract好像很像，比Abstract更详细一点。好像又和后面Related部分有一定内容重叠。

### **引言讲述论文方法的动机`motivation`**

一篇论文的目标是“inform”而不是“impress”，论文必须要是高度可读可懂的。论文需要说服读者，通过呈现课题折射的研究理论来说服目标读者。说服读者什么，说服读者可以让他们知道我们的研究工作很重要。想要让读者觉得我们的工作重要且有意义，就需要写出论文提出方法的`motivation`，给出论文提出方法得到的结果`outcome`，并且给出足够的证据证明结果的正确性。而Introduction部分就负责阐述研究工作的动机`motivation`。可以在引言的最后给读者罗列整篇论文的结构。

### **为什么需要一个引言`Introduction`**

>从文章结构看，Introduction用来提出你的研究问题，这个问题的答案在文章之后的Discussion或者Conclusion部分呈现给读者，在文章的首尾形成前后呼应。

引言内容需要能够回答两个核心问题：
    1. 研究的空白是什么，为什么需要填补这个空白？
    你要说服读者这个研究空白很重要，值得我们费时费力去探究。
    
    2. 你研究的是什么，为什么你的研究可以填补这个空白。
    你要说服读者相信你的研究的确填补了这个领域的空白。

所以整个引言的逻辑就是：

$$ \textbf{定位}\text{研究空白}-->\textbf{解释}\text{为什么要填补这个空白}-->\textbf{总结}\text{你是怎么填补这个空白}$$

因此引言要呈现的思路就是：
$$ \textbf{研究空白是这个}-->\textbf{研究空白很重要}-->\textbf{你看我的研究就是可以填补这个空白}$$


### **引言的4个部分**

网上有很多资料，把引言用不同的方法分解成几个部分，不同的方法都有自己的道理，我这里按照`英语学术写作`的方法将**引言的写作内容**分成4个部分。

1）**Context** 背景和重要性

介绍一些研究领域的大背景，勾勒该领域研究成果的一个走向和趋势。能够引导不熟悉你这个研究领域的读者，让读者知道你研究工作的重要性。这部分内容一定要引用一些前人的文献工作，体现你对该学科的总体把握是全面客观的。如何从大背景引入到论文课题呢？就是把`关联该论文课题的相关信息`拿出来说。比如：从"计算机视觉、深度学习"的大背景引入到“领域自适应”这个论文课题，相关信息就是“深度学习需要大量带标签的数据，为每个场景收集标签是一个很费力的工作，迁移学习的领域自适应方法提供了一个很有吸引力的解决思路”。

2）**Need** 该领域还需要做什么，科研空白是什么

写出现在的科研领域进展是什么样的，已经有了什么，但是还差什么。给出“这个研究领域的目标”和“现在有的研究成果”之间的矛盾和差距。                    

在引言中，**Context**和**Need**一起组成一个漏斗状的结构，从一个很广范围的研究背景开始，逐步缩小到论文解决处理的这个问题点上去。


![](https://s1.ax1x.com/2020/05/15/Ysf6jP.jpg)


3）**Task** 你做了什么

为了处理上面说的`Need`，说明一下你做了什么样的工作。简洁地对自己的研究工作做出概述，写**主要**的研究手段和研究发现，不要过分展开细节。

    we applied xxx to ...
    We computed the ... of ... to
    We evaluate the efficacy of ...
    ......

1) **Object** 

1⃣（可选） 根据论文后面的内容在这里给读者一个论文内容结构，比如“论文第2部分详细介绍了方法的细节，第3部分展示了……数据集上的实验结果”。

2⃣ 直接罗列论文的贡献和成果，可以写：提出了一个新的思路处理这个问题、构造了新的数据集、大量的实验证结果显示出论文方法有效，超过SOTA。

![](https://s1.ax1x.com/2020/05/15/YsyRJ0.png)

# **三 Conclution 结论**

最后的结论中直接写你工作中最重要的结果，和`Introduction`首尾呼应，引言中提到的问题，你解决到哪个程度了。
> Interpret your findings at a higher level of abstraction. 
 
不用重复说明自己做了什么，只给读者展示对他最有意义的东西，目的是让`Conclusion`的内容令读者感到有趣和印象深刻。
结尾可以来个展望，比如 “后续工作是什么”，“还有什么不足”。
    
    In the coming months, we will ……

如果自己不想再沿着这个方向继续科研下去，可以向读者发出对这项研究工作的邀请，写“希望我们的工作可以启发其他研究人员，从我们这个思路处理这个问题”、“这个研究方向很有继续探索的潜力”

    Our remaining question is ……

    And it is promising to make more exploration in this direction in the future

摘要`Abstraction`和引言`Introduction`里面已经说清楚的东西就不需要在`Conclusion`里面重复说了，结论部分主要关注你发现了什么，你的发现有什么意义。不要害怕写一个很短的`Conclusion`。

# **实验**

刚入门科研做对比实验的时候一般不用自己复现一遍别人的论文方法计算结果，而是直接从别人论文里取实验结果。

    For a fair comparision, the results of other approaches are taken from their original papers.

# **补充**
可以按照下面的写作顺序来写
$\textbf{Method} -> \textbf{Exmeriment/Result} -> \textbf{(Discussion)} -> \textbf{Introduction} -> \textbf{Conclusion} -> \textbf{Abstract}$

$\textbf{Related Work}$可以单独写，也可以融入到`Introduction`里面去。

![](https://s1.ax1x.com/2020/05/15/YsRhqS.png)


第一次写论文没经验的话，可以辛苦一点边写自己的论文，边看很多与自己论文工作最相关的其他论文。正在写自己论文的情况下，更容易发现其他论文里哪些句子自己是可以运用的，发现可以模仿的句子后，马上把句子的模板句型摘抄下来做记录，等在自己论文中也使用了这个句子后，就在旁边打一个勾，尽量在写论文的时候不落下任何应该表达出来的语句。

![](https://s1.ax1x.com/2020/05/15/YshYCj.png)


# 参考资料
[知乎--怎样写好英文论文的 Introduction 部分？](https://www.zhihu.com/question/49355121/answer/322451208)