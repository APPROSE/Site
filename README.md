# Archive Site

画像アーカイブサイト

## GitHub Pagesでのホスティング手順

1. このリポジトリをGitHubにプッシュ
2. リポジトリの Settings > Pages に移動
3. Source で「Deploy from a branch」を選択
4. Branch で「main」（または「master」）を選択し、`/ (root)` を選択
5. Save をクリック
6. 数分後に `https://[ユーザー名].github.io/[リポジトリ名]/` でアクセス可能になります

## QRコードの生成

QRコードを生成するには、以下の手順を実行してください：

### 1. 仮想環境のセットアップ（初回のみ）

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. QRコードの生成

```bash
source venv/bin/activate  # 仮想環境を有効化（毎回）
python3 generate_qr.py
```

GitHub PagesのURLを入力すると、QRコード画像（`qrcode.png`）が生成されます。

### 例

```
URL: https://username.github.io/repository-name/
```

生成されたQRコードは `qrcode.png` として保存されます。

