# Transform
transform = transforms.Compose([
    transforms.Resize((300, 300)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.475, 0.453, 0.406],
                         std=[0.228, 0.224, 0.225])
])

# Feature extractor
def extract_features(img_path):
    img = Image.open(img_path).convert("RGB")
    img = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        feat = model(img)
    return feat.squeeze().cpu().numpy()