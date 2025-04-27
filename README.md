# Assignment 2

## 任务总结

### Prompt Engineering

#### 设计一个Prompt

设计一个prompt，满足测试两个 LLM，要求一个LLM可以生成正确的答案，但是另一个LLM不能生成正确的答案。

LLM 从下面的几个中选择：

- Deepseek V3 (with deep thinking)
- GPT-4o,o1 or o3
- Gemini 2.5 Pro Experimental 03-25
- Claude 3.7 sonnet

要求：

1. 问题有一个单独且容易验证的答案
2. 问题重复3次，检查一致性
3. prompt和答案都是英文的

#### In-Context Learning

要求：

1. 在 [GSM-8K](https://huggingface.co/datasets/openai/gsm8k) 上随机选择三个推理问题
2. 设计一个prompt，要求解决这三个问题（只设计一个prompt）
3. 确保输出是structured format，包含：

    - 问题 ID
    - 推理过程
    - 答案
    - 难度分级

4. 最终提供两版的prompt，一个是few-shot的，一个是zero-shot的。

### NLP architecture Analysis

除了 GPT 结构外，还有一些其他的结构：

- GQA (Grouped Query Attention)
- Mamba-1 and Mamba-2
- GLA (Gated Linear Attention)

这个任务需要计算：

- Model size
- the KV cache size
- the FLOPs in a forward pass

使用的模型是标准的 GPT-2 结构。

至少要实现 GQA，剩余两个可以不实现。

### Model Implementation

只完成下面两个任务的一个。

#### Modifying Qwen2.5

主要修改的内容为：

1. Learned Positional Embedding： 改为可以修改的位置编码
2. 修改 RMSNorm 为 DyT
3. ReLU-Attention
4. Layer-Dependent Attention Mask

#### Mannual Forward of ReGLA

要求：

1. 阅读 GLA 和 ReGLA 的论文，写出二者前向的表达式
2. 使用 `Numpy` 实现 ReGLA 的前向计算

