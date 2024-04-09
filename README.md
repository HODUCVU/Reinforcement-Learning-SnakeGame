# Train an AI to play snake game by using Reinforcement Learning
## Introduction
* Using Deep Q Learning to implement reinforcement learning.
* Framework: PyTorch, Pygame
	![](/images/framework.png)
* Use Bellman Equation to update Q value (Quality of action in reinforcement learning)
	![](/images/bellman-equation.png)
* Steps
	![](/images/steps.png)
## Install tools
* init virtual environment
	* install virtual env
	```
	> sudo apt install python3-virtualenv
	> virtualenv venv 
	```
	* install virtual env in python3.7
	```
	> sudo add-apt-repository ppa:deadsnakes/ppa
	> sudo apt update
	> sudo apt install python3.7-venv
	> python3.7 -m venv venv
	```
	* Activate venv
	```
	bash
	> source venv/bin/activate
	fish
	> source venv/bin/activate.fish
	```
	* Deactivate venv
	```
	> deactivate
	```
* install tools
```
> pip install -r setup.txt
```
## Run Game
```
> cd /game
> python3 game.py
```
## Train
```
> python3 train/agent.py
```
* if you don't train with model existed from /save/model.pth, then add comment in /train/agent.py like below:
```
### Load existed model
# self.model.load_state_dict(torch.load('./save/model.pth'))
###
```
## Result train
![](/images/result.png)
# Resource
* Full tutorial: [freeCodeCamp.org](https://www.youtube.com/watch?v=L8ypSXwyBds&list=LL&index=1&t=287s)
* My tutorials:
	* Code game: [Snake game with Python | Pygame](https://www.youtube.com/watch?v=EZ6uXPTmxKo)
	<!-- * Train model: -->
