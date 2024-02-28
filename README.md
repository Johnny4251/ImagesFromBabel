# ImagesFromBabel

## Overview
ImagesFromBabel explores a simple yet profound conjecture through seeded image generation. By generating random binary images from integer seeds, this project proves the mathematical inevitability that, given infinite inputs (seeds), some must inevitably produce identical outputs (images).

## Background Information

### The Pigeonhole Principle

#### Inputs
In an environment with infinite computing capabilities (akin to a Turing Machine), an infinite number of seeds can be generated.

#### Outputs
Conversely, the set of possible outputs (images) is finite. The total number of unique images that can be generated is defined by (|PIXELVALUES|)^(HEIGHT x WIDTH), assuming an image with finite dimensions and number of values per pixel.

#### Result
The cardinality (or size) of the set of inputs (seeds) vastly exceeds the cardinality of the set of outputs (images). This discrepancy guarantees that multiple distinct seeds must produce identical images.

### Simplified Explanation

In essence, within the bounds of theoretical, unlimited computing power, there must exist at least one seed that generates the same image as another, entirely different seed. This concept challenges our understanding of randomness and determinism in computational processes.

### Mindblowing Concept

Imagine the possibility of replicating a specific image, such as a portrait of oneself, purely through this process. Mathematically, there exists an infinite set of seeds capable of generating any given image. While practically implausible due to the immense scale of computation required, this notion suggests that, in an infinitely expanding universe, there might exist a precise seed that can recreate any desired image. 

# Code
## Information
The python code provided uses opencv and seed generation produce a binary image. Explore custom seeds and see if you can find one that replicates something cool!
