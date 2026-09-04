# Dog Breed Classifier

A Python program that uses pretrained CNN models (AlexNet, VGG, and ResNet) to classify images as dogs or not-dogs, and to identify dog breeds. Built as part of the AWS AI & ML Scholarship Program (Udacity Nanodegree).

## Project Overview

This program was built for a "city dog show" scenario: verify that registrants submitting photos for a dog show are actually submitting images of dogs. The core focus is on using Python to work with an already-trained image classifier, not on building the classifier itself.

The program:
1. Extracts the true pet label from each image's filename
2. Runs each image through a pretrained CNN to get a predicted label
3. Compares predicted vs. true labels
4. Determines whether each image is correctly identified as a dog or not-dog (regardless of breed)
5. Calculates accuracy statistics and prints a summary
6. Times the whole process for performance comparison

## Objectives

1. Correctly identify which images are of dogs and which aren't
2. Correctly classify the breed for images that are dogs
3. Determine which CNN architecture (ResNet, AlexNet, or VGG) best achieves objectives 1 and 2
4. Weigh runtime against accuracy — is a faster, slightly-less-accurate model "good enough"?

## How to Run

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

**Arguments:**
- `--dir` — path to the folder of images to classify (default: `pet_images/`)
- `--arch` — CNN architecture to use: `vgg`, `alexnet`, or `resnet` (default: `vgg`)
- `--dogfile` — text file containing valid dog breed names (default: `dognames.txt`)

To run all three architectures and save results:
```bash
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt > vgg_pet-images.txt
```

Or, on Unix-like systems / Git Bash:
```bash
sh run_models_batch.sh
```

## Requirements

- Python 3
- PyTorch
- torchvision

Install dependencies:
```bash
pip install torch torchvision
```

## Project Structure

dog-breed-classifier/
├── check_images.py # Main program
├── get_input_args.py # Parses command-line arguments
├── get_pet_labels.py # Extracts true labels from filenames
├── classify_images.py # Runs classifier, compares labels
├── adjust_results4_isadog.py # Determines dog vs. not-dog
├── calculates_results_stats.py # Computes accuracy statistics
├── print_results.py # Prints summary and misclassifications
├── classifier.py # Provided pretrained classifier function
├── dognames.txt # List of valid dog breed names
├── pet_images/ # Test image dataset
├── resnet_pet-images.txt # Results using ResNet
├── alexnet_pet-images.txt # Results using AlexNet
└── vgg_pet-images.txt # Results using VGG

## Results Summary

All three architectures were tested on a 40-image dataset. Key findings:
- All three correctly distinguished dog images from non-dog images
- VGG generally showed strong breed classification accuracy but had the slowest runtime
- AlexNet was the fastest, offering a solid speed/accuracy trade-off

*(See individual `*_pet-images.txt` files for full per-model statistics.)*

## Author

Kessney Edor — Built as part of the AWS AI & ML Scholars Nanodegree Program (Udacity), 2026