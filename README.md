# comfyui-primitive-convert

This is custom node includes next primitives nodes:

* **To String** - convert `INT`, `FLOAT`, `BOOLEAN` to `STRING`
* **To Int** - convert `STRING`, `FLOAT`, `BOOLEAN` to `INT`
* **To Float** - convert `STRING`, `INT`, `BOOLEAN` to `FLOAT`

# Installation

Download `comfyui-primitive-convert`, then copy to your `ComfyUI/custom_nodes/` and restart ComfyUI

# Usage

You can use this for input node parameter `filename_prefix` of the Save Image node to name the output generations meaningfully. For example ([Download the workflow](_media/Flux.2_klein.json)):

![](_media/1.png)
![](_media/2.png)

In the output folder you will get file names similar to the following:

![](_media/3.png)
