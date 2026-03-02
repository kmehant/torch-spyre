import torch

print(
    torch.nn.functional.silu(
        torch.tensor([1, 2, 3], dtype=torch.float16, device="spyre")
    )
)
