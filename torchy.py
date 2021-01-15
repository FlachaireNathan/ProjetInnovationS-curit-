import analyser

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
from torchvision import transforms, datasets

class Net(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(40, 128)
		self.fc2 = nn.Linear(128, 128)
		self.fc3 = nn.Linear(128, 128)
		self.fc4 = nn.Linear(128, 10)
	
	def forward(self, x):
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = F.relu(self.fc3(x))
		x = self.fc4()
		return F.log_softmax(x, dim=1)

net = Net()
print(net)


dataTrain = analyser.UploadDataBase("corpus/train.txt", ["\n"])
dataTest = analyser.UploadDataBase("corpus/test.txt", ["\n"])

trainset = torch.utils.data.DataLoader(dataTrain, batch_size=64, shuffle=True)
testset = torch.utils.data.DataLoader(dataTest, batch_size=64, shuffle=True)

loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

EPOCHS = 3

for epoch in range(3): # 3 full passes over the data
	for data in trainset:  # `data` is a batch of data
		X = data  # X is the batch of features, y is the batch of targets.
		print(X)
		net.zero_grad()  # sets gradients to 0 before loss calc. You will do this likely every step.
		output = net(X.view(-1,40))  # pass in the reshaped batch (recall they are 28x28 atm)
        #output = net(X.view(-1,784))  # pass in the reshaped batch (recall they are 28x28 atm)
        #loss = F.nll_loss(output, y)  # calc and grab the loss value
        #loss.backward()  # apply this loss backwards thru the network's parameters
        #optimizer.step()  # attempt to optimize weights to account for loss/gradients
    #print(loss)  # print loss. We hope loss (a measure of wrong-ness) declines! 



"""
x = torch.Tensor([5,3])
y = torch.Tensor([2,1])

print(x*y)

#tensor(10., 3.)
"""