import torch, platform
print(f"""  
PyTorch版本: {torch.__version__}  
Python版本: {platform.python_version()}  
操作系统: {platform.system()} {platform.release()}  
CUDA可用: {torch.cuda.is_available()}  
显卡信息: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}  
""")