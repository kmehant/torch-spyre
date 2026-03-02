import torch

print(torch.nn.functional.silu(torch.empty(3, device="spyre", dtype=torch.float16)))