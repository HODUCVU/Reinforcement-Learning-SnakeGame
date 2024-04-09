import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

class Linear_QNet(nn.Module):
	def __init__(self, input_size, hidden_size, output_size):
		super().__init__()
		self.linear1 = nn.Linear(input_size, hidden_size)
		self.linear2 = nn.Linear(hidden_size, output_size)

	def forward(self, x):
		x = F.relu(self.linear1(x))
		x = self.linear2(x)
		return x
	
	def save(self, file_name = 'model.pth'):
		save_folder_path = './save'
		if not os.path.exists(save_folder_path):
			os.makedirs(save_folder_path)

		file_name = os.path.join(save_folder_path, file_name)
		torch.save(self.state_dict(), file_name)

	"""
	To load model existed
	model = YourModel()
	model.load_state_dict(torch.load('rl_model.pth'))
	"""
