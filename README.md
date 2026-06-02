# PVTA: Pipelined Micro-architecture for VTA

Artifacts for the paper *"Pipelined Micro-architecture for VTA with Circuit and
Instruction Co-optimization."* This repository reproduces the end-to-end
inference time of ResNet-50 and YOLOv3 on a Xilinx ZCU104 board, as reported in
Section V-C / Table IV of the paper.

## Contents

| Path | Description |
|------|-------------|
| `vta_200_300_fuse.bit` | FPGA bitstream (200 MHz compute core, 300 MHz AXI bus, with the fused-instruction PVTA configuration) |
| `down_bit.py` | Script to program the bitstream onto the ZCU104 PL |
| `resnet/` | Compiled C++ test program (`resnet_test`) + precompiled instruction stream for ResNet-50 |
| `v3/`     | Compiled C++ test program (`v3_test`) + precompiled instruction stream for YOLOv3 |


> **Note on instructions vs. TVM.** The instruction streams are pre-generated
> with the TVM v0.7 compiler and committed directly to this repository, so TVM
> is not required to run the tests. Only the VTA runtime libraries and the
> compiled C++ test programs are needed for on-board execution. The C++ test
> programs implement the ARM-side runtime described in Section V-A of the paper.

## Requirements

- Xilinx ZCU104 (Zynq UltraScale+), running ___ (e.g. PYNQ v___ / PetaLinux ___)
- Vivado 2020.1 (used to generate the bitstream; not needed just to run)
- Python 3 on the board (for `down_bit.py`)

## How to run

1. Program the FPGA with the PVTA bitstream:
```bash
   python down_bit.py vta_200_300_fuse.bit
```
2. Run the per-network test program (prints end-to-end inference time):
```bash
   # ResNet-50
   cd resnet
   sudo LD_LIBRARY_PATH=. ./resnet_test

   # YOLOv3
   cd v3
   sudo LD_LIBRARY_PATH=. ./v3_test
```

## Mapping to the paper

- `vta_200_300_fuse.bit` corresponds to the **PVTA** configuration in Table III
  (200 MHz core, 300 MHz AXI, instruction optimization enabled).
- The measured inference times correspond to the PVTA column of **Table IV**
  (ResNet-50 and YOLOv3).
