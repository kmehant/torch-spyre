import torch

d = torch.empty(3, device="spyre", dtype=torch.float16)
print(torch.nn.functional.silu(d))