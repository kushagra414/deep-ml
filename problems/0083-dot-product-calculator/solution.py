import torch

def calculate_dot_product(vec1: torch.Tensor, vec2: torch.Tensor) -> torch.Tensor:
    return vec1 @ vec2.T