import torch
state_dict = torch.load("logs\ep079-loss2.896-val_loss3.104.pth")
torch.save(state_dict, "logs\ep079-loss2.896-val_loss3.104.pth", _use_new_zipfile_serialization=False)