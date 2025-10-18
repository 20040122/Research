import torch

if torch.cuda.is_available():
    print("CUDA 可用")
    device = torch.device("cuda")
    a = torch.tensor([1.0, 2.0], device=device)
    b = torch.tensor([3.0, 4.0], device=device)
    c = a + b
    print("a + b =", c)
else:
    print("CUDA 不可用")