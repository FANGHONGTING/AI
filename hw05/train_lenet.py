"""
LeNet-5 训练与评估入口脚本
用法：python train_lenet.py
"""

import torch
import torch.nn as nn
import torch.optim as optim
from lenet5 import LeNet5, load_data, test


def train(model, train_loader, criterion, optimizer, device, epochs=5):
    """训练模型并打印每个epoch的结果"""
    model.train()
    print("\n开始训练 LeNet-5...")
    print("-" * 50)

    for epoch in range(epochs):
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total
        print(f'Epoch {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.2f}%')

    print("-" * 50)
    print("训练完成！\n")
    return model


def main():
    # 设置随机种子
    torch.manual_seed(42)

    # 选择设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'使用设备: {device}')

    # 加载数据
    train_loader, test_loader = load_data(batch_size=64)

    # 创建模型
    model = LeNet5().to(device)
    print(model)

    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # 训练模型
    train(model, train_loader, criterion, optimizer, device, epochs=5)

    # 测试模型
    test_loss, test_accuracy = test(model, test_loader, criterion, device)

    # 保存模型
    torch.save(model.state_dict(), 'lenet5_mnist.pth')
    print('模型已保存为 lenet5_mnist.pth')


if __name__ == '__main__':
    main()
