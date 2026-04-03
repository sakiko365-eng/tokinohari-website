#!/usr/bin/env python3
"""
ブログ記事のアイキャッチ画像をランダム選択するスクリプト。
posts.json を読み込み、使用頻度が低い画像を優先的に返す。
counseling.jpg / profile.jpg は使いすぎを防ぐため除外。

使い方:
  python3 pick_blog_image.py
"""

import json
import random
from pathlib import Path

# 利用可能な画像（テーマ別に分類）
ALL_IMAGES = [
    # 雰囲気・院内
    "tokinohari-atmosphere-calm.jpg",
    "tokinohari-atmosphere-relax.jpg",
    "tokinohari-atmosphere-season.jpg",
    "tokinohari-kojinshitsu-bed.jpg",
    "tokinohari-kojinshitsu-light.jpg",
    "tokinohari-naikan-room01.jpg",
    "tokinohari-naikan-room03.jpg",
    "tokinohari-naikan-detail01.jpg",
    "tokinohari-detail-pillow.jpg",
    "tokinohari-detail-towel.jpg",
    # 施術
    "tokinohari-harikyu-shoulder.jpg",
    "tokinohari-harikyu-whole-body.jpg",
    "tokinohari-harikyu-tools.jpg",
    "tokinohari-ninkatsu-harikyu.jpg",
    "tokinohari-biyoshin-face.jpg",
    # 旧画像（サブ候補）
    "exterior.jpg",
    "hero.jpg",
    "interior.jpg",
    "about.jpg",
    "room.jpg",
    # 除外（カウンセリング写真）
    # "counseling.jpg"  ← 使用禁止
    # "profile.jpg"     ← 使用禁止
    # "tokinohari-counseling-room.jpg" ← カウンセリング写真のため除外
]

POSTS_JSON = Path(__file__).parent / "blog" / "posts.json"

def pick_image():
    # posts.json から使用済み画像をカウント
    usage = {img: 0 for img in ALL_IMAGES}

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
