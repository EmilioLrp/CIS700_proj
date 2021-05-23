# CIS 700 Term Project: NTM
This is the repository of the sorce code for CIS 700 Neural Program Learning's semester project. The purpose of this project is to use the architecture of NTM to solve 4 different tasks. Each team member is correpond to one task alone. The task may came from internet and it may varies from its original version. 
This project is modified from the original project at [here](https://github.com/loudinthecloud/pytorch-ntm).

## Instructeor 
* Dr. Garrett Katz(gkatz01@syr.edu)

## Contributors and corresponding tasks
* [Ruipeng LIU](https://github.com/EmilioLrp)(rliu02@syr.edu)
	* [Maximum sub array sum problem](https://leetcode.com/problems/maximum-subarray/)
	* Branch name: rliu02
* Qinwei HUANG (qhuang18@syr.edu)
	* [Merge intervals](https://leetcode.com/problems/merge-intervals/)
	* Branch name: qhuang18
* Chi ZUO (czuo02@syr.edu)
	* [Palindrome numbers](https://leetcode.com/problems/palindrome-number/)
	* Branch name: czuo02
* Yuchao XU (yxu219@syr.edu)
	* Odd and even numbers
	* Branch name: yxu219

## System requirement
In order to run this project, please make sure that the hosting machine having a python3 installed. Being able to build a virtual environment or any other isolated environment is preferred since some of the packages that this project used may not be the most up to date version.

## Dependencies installation
Again it is highly recommended to install an isolated invironment. This instruction assuems the installation happends in virtual environment.

First, activate virtual environment. Then go to the root folder of the project, where the `requirements.txt` is located. Execute the following command:

```
pip install -r requirements.txt
```

There may be issues regarding different package name and versions accross different OS, in that case, please make sure that the following packages are properlly installed:

* attrs==19.1.0
* matplotlib==3.3.4
* numpy==1.19.5
* torch==1.8.1

## Execute instruction
First, select the corresponding branch that aims to solve a particular problem. Pull the branch to the local. Make sure that all the dependencies are installed.

The following command are assume that the virtual environment is activated.

### Data generation
To generate training and testing data, please access file `CIS700_proj/data/generator.py`. Execute the following command:
```
python generator.py
```
If successfully executed, 3 files named `train.txt, test.txt, test_var.txt` corresponding to trainig data, testing data with the same input size with the trainig data and the testing data with different input size with the trainig data should be presented in the same directory.

### Training
To train the model, please make sure that the file `train.txt` exist in directory `CIS700_proj/data/`. Go to the root directory of this project where `train.py` is located, simply execute the following command:
```
python train.py
```

If the program execute correctly, a log at the end states `Done training` should be presented. A file under `CIS700_proj/model/` is presented. And finally a file named `train_loss.txt` is presented in the root directory of the project.

### Testing
To test the model, please make sure that `test.txt, test_var.txt` exist in directory `CIS700_proj/data/` and a model file exist in directory `CIS700_proj/model/`. Go to the root directory where `test.py, test2.py` exist. To run the test with the same input size of the training file, execute: 
```
python test.py
```

To run the test with different input size of the training file, execute:
```
python test2.py
```
If the program execute correctly, a file named `test_loss.txt` (or `test2_loss.txt` for `test2.py`) will be presented in the root folder.

### Plotting
Please make sure that you have a GUI. This instruction may not work for a pure text use interface.
To plot the losses, please make sure that all `train_loss.txt, test_loss.txt, test2_loss.txt` exist in the root directory. Execute command:
```
python learning_curve.py
```
If execute correctly, a graph plotting 3 curves corresponding 3 losses should be presented.

### Configuration
Some configurations can be accessed and modified via `CIS700_proj/data/config.py`. Within this file, it is possible to change the following attributes of the project:
* Upper and lower bound of each element in the training data
* EOS's representation, make sure that this representation cannot be accessed by all possible elements in input and output
* Size of input
* Encoding length of each element both input and output (an unsigned integer's binary representation)
* Threashold for encoding. (Shift the encoding data to non-negateive)
* Training, testing and variate testing data size
* A portion of nerual network configuration

Other configs of the model needs to be accessed within the code.

### Sample model
There is a sample trained model located within the folder `CIS700_proj/model/` that is trained under the current configuration. If you would like to train another model, please make sure that the training data is available and remove the model first. 