#!/usr/bin/env python3
"""
ブログ記事のアイキャッチ画像をランダム選択するスクリプト。
posts.json を読み込み、使用頻度が低い画像を優先的に返す。
counseling.jpg は使いすぎを防ぐため優先度を下げる。

使い方:
  python3 pick_blog_image.py
"""

import json
import random
from pathlib import Path

# 利用可能な全画像（counseling.jpgは最後尾＝最低優先度）
ALL_IMAGES = [
    "exterior.jpg",
    "room.jpg",
    "interior.jpg",
    "about.jpg",
    "hero.jpg",
    "profile.jpg",
    "counseling.jpg",  # 使いすぎ防止のため最低優先度
]

POSTS_JSON = Path(__file__).parent / "blog" / "posts.json"

def pick_image():
    # posts.json から使用済み画像をカウント
    usage = {img: 0 for img in ALL_IMAGES}
    usage["counseling.jpg"] = 3  # counseling.jpgにペナルティ（最初から3回使用済み扱い）

    if POSTS_JSON.exists():
        posts = json.loads(POSTS_JSON.read_text(encoding="utf-8"))
        for post in posts:
            img = post.get("image", "")
            if img in usage:
                usage[img] += 1

    # 最も使用回数が少ない画像群の中からランダム選択
    min_count = min(usage.values())
    candidates = [img for img, count in usage.items() if count == min_count]
    chosen = random.choice(candidates)

    print(chosen)
    return chosen

if __name__ == "__main__":
    pick_image()
