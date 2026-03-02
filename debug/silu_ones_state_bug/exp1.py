import torch

d = torch.tensor([1, 2, 3], dtype=torch.float16, device="spyre")
print(torch.nn.functional.silu(d))
