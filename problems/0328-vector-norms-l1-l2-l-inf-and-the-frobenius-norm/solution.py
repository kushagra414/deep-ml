import torch

def compute_norm(arr: torch.Tensor, norm_type: str) -> float:
    """
    Compute the specified norm of the input tensor.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D tensor.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input tensor (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    allowed_norms = ["l1", "l2", "linf", "frobenius"]
    if norm_type not in allowed_norms:
        raise ValueError("Norm type not allowed")
    
    if norm_type == "frobenius" and arr.ndim != 2:
        raise ValueError("Forbenius norm need 2D array")
    ans = 0
    if norm_type == "l1":
        ans = torch.norm(arr, p=1)
    elif norm_type == "l2":
        ans = torch.norm(arr, p=2)
    elif norm_type == "linf":
        ans = torch.linalg.vector_norm(arr, ord=float("inf"))
    else:
        ans = torch.norm(arr,p="fro")
    
    return ans.item()
    
