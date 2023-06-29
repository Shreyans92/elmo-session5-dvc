import torch
import torch.nn as nn
import timm

class TIMMModel(nn.Module):
    def __init__(self, model, input_ch=3, num_cls=10):
        super(TIMMModel, self).__init__()
        self.timm_model = timm.models.create_model(
            model, pretrained=True, in_chans=input_ch, num_classes=num_cls
        )
    
    def forward(self, x):
        return self.timm_model(x)
if __name__ == "__main__":
    _ = TIMMModel()