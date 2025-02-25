# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pathlib
import subprocess

from torch.utils import cpp_extension
from pathlib import Path

srcpath = Path(__file__).parent.absolute()

# Setting this param to a list has a problem of generating different
# compilation commands (with diferent order of architectures) and
# leading to recompilation of fused kernels. Set it to empty string
# to avoid recompilation and assign arch flags explicity in
# extra_cuda_cflags below
os.environ["TORCH_CUDA_ARCH_LIST"] = ""


def load_fused_kernels(neox_args):
    try:
        import scaled_upper_triang_masked_softmax_cuda
        import scaled_masked_softmax_cuda
    except (ImportError, ModuleNotFoundError):
        print("\n")
        print("=" * 100)
        print(
            f'ERROR: Please run `python {str(srcpath / "setup.py")} install` to install the fused kernels'
        )
        print("=" * 100)
        exit()
    return
