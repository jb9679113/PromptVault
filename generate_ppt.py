from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

BG_DARK = RGBColor(0x0F, 0x0A, 0x2E)
BG_GRADIENT_MID = RGBColor(0x1A, 0x11, 0x4B)
PURPLE = RGBColor(0x7C, 0x3A, 0xED)
LIGHT_PURPLE = RGBColor(0xA7, 0x8B, 0xFA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xCB, 0xD5, 0xE1)
GREEN = RGBColor(0x10, 0xB9, 0x81)
RED_SOFT = RGBColor(0xF8, 0x71, 0x71)
ORANGE = RGBColor(0xF9, 0x73, 0x16)
BLUE = RGBColor(0x3B, 0x82, 0xF6)
YELLOW = RGBColor(0xFA, 0xCC, 0x15)

def set_slide_bg(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_shape_bg(slide, left, top, width, height, color, alpha=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape

def add_text_box(slide, left, top, width, height, text, font_size=18, color=WHITE, bold=False, alignment=PP_ALIGN.LEFT, font_name='Microsoft YaHei'):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return txBox

def add_bullet_list(slide, left, top, width, height, items, font_size=16, color=WHITE, bullet_color=None, spacing=Pt(8)):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = 'Microsoft YaHei'
        p.space_after = spacing
        p.level = 0
    return txBox

def add_accent_line(slide, left, top, width, color=PURPLE):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Pt(4))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape

# ===================== SLIDE 1: Cover =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_shape_bg(slide, Inches(0), Inches(0), prs.slide_width, prs.slide_height, BG_DARK)
add_text_box(slide, Inches(1), Inches(1.5), Inches(11), Inches(2), 'Day 1', font_size=96, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
add_accent_line(slide, Inches(5), Inches(3.3), Inches(3.333), PURPLE)
add_text_box(slide, Inches(1), Inches(3.6), Inches(11), Inches(1), 'Vibe Coding 启蒙 + 工具准备', font_size=36, color=LIGHT_PURPLE, bold=False, alignment=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(4.8), Inches(11), Inches(0.8), 'Easy-Vibe AI编程 0→1 免费体验营', font_size=22, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(6.2), Inches(11), Inches(0.6), '导师：[你的名字]｜2026年5月', font_size=16, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)

# ===================== SLIDE 2: Welcome =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '欢迎来到 Easy-Vibe 0→1 体验营！', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)
add_text_box(slide, Inches(0.8), Inches(2.2), Inches(6), Inches(0.6), '今日议程', font_size=24, color=LIGHT_PURPLE, bold=True)
add_bullet_list(slide, Inches(1.2), Inches(3.0), Inches(8), Inches(3), [
    '🧠  理解 Vibe Coding 新编程范式',
    '🛠️  手把手安装核心 AI 开发工具 Cursor',
    '🚀  用一句话生成你的第一个 AI 网页',
], font_size=22, color=WHITE, spacing=Pt(16))
add_text_box(slide, Inches(9), Inches(6.2), Inches(3.5), Inches(0.6), '预计时长：40 分钟', font_size=16, color=LIGHT_GRAY, alignment=PP_ALIGN.RIGHT)

# ===================== SLIDE 3: About Instructor =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '我是 [你的名字]', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)
add_bullet_list(slide, Inches(1.2), Inches(2.5), Inches(8), Inches(3), [
    '🎯  专注 AI 原生开发与产品落地',
    '👨‍🏫  已帮助数百名零基础学员做出第一个 AI 产品',
    '🦞  Easy-Vibe 实战导师',
], font_size=22, color=WHITE, spacing=Pt(20))

# ===================== SLIDE 4: Why Learn This =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '为什么你值得花 5 天学习 Vibe Coding？', font_size=36, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(5), PURPLE)

left_box = add_shape_bg(slide, Inches(0.8), Inches(2.2), Inches(5.5), Inches(4.2), RGBColor(0x2D, 0x1B, 0x1B))
add_text_box(slide, Inches(1.2), Inches(2.4), Inches(4.8), Inches(0.6), '❌ 传统编程的痛点', font_size=22, color=RED_SOFT, bold=True)
add_bullet_list(slide, Inches(1.4), Inches(3.2), Inches(4.5), Inches(3), [
    '要背大量语法和框架',
    '环境配置经常卡几个小时',
    '一个简单想法也要写几天代码',
    '调试 Bug 让人崩溃',
], font_size=18, color=RGBColor(0xFB, 0xC0, 0xC0), spacing=Pt(14))

right_box = add_shape_bg(slide, Inches(6.8), Inches(2.2), Inches(5.5), Inches(4.2), RGBColor(0x0D, 0x28, 0x1B))
add_text_box(slide, Inches(7.2), Inches(2.4), Inches(4.8), Inches(0.6), '✅ Vibe Coding 的优势', font_size=22, color=GREEN, bold=True)
add_bullet_list(slide, Inches(7.4), Inches(3.2), Inches(4.5), Inches(3), [
    '用自然语言描述想法',
    'AI 帮你写代码、调试、优化',
    '5 天就能做出完整产品',
    '重点放在产品思维而非语法',
], font_size=18, color=RGBColor(0xA7, 0xF3, 0xD0), spacing=Pt(14))

# ===================== SLIDE 5: Paradigm Shift =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '2026 年的编程范式', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

left_box = add_shape_bg(slide, Inches(0.8), Inches(2.2), Inches(5.2), Inches(2.5), RGBColor(0x1E, 0x15, 0x3A))
add_text_box(slide, Inches(1.2), Inches(2.4), Inches(4.5), Inches(0.6), '传统编程', font_size=22, color=RED_SOFT, bold=True)
add_text_box(slide, Inches(1.2), Inches(3.2), Inches(4.5), Inches(1), '写代码 → 编译 → 调试', font_size=20, color=LIGHT_GRAY)

right_box = add_shape_bg(slide, Inches(7), Inches(2.2), Inches(5.5), Inches(2.5), RGBColor(0x0D, 0x28, 0x1B))
add_text_box(slide, Inches(7.4), Inches(2.4), Inches(4.8), Inches(0.6), 'Vibe Coding（氛围编程）', font_size=22, color=GREEN, bold=True)
add_text_box(slide, Inches(7.4), Inches(3.2), Inches(4.8), Inches(1), '描述想法 → AI 生成 → 对话迭代 → 快速交付', font_size=18, color=RGBColor(0xA7, 0xF3, 0xD0))

add_text_box(slide, Inches(2), Inches(5.2), Inches(9), Inches(1.2), '会说话，就会做应用', font_size=48, color=PURPLE, bold=True, alignment=PP_ALIGN.CENTER)

# ===================== SLIDE 6: Core Philosophy =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(1), Inches(1), Inches(11), Inches(1.5), '会说话，就会做应用', font_size=56, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
add_accent_line(slide, Inches(5), Inches(2.5), Inches(3.333), PURPLE)

items = [
    ('1', '会说话，就会描述产品', PURPLE),
    ('2', '会迭代，就会优化产品', GREEN),
    ('3', '会思考，就会用 AI 完成复杂任务', BLUE),
]
for i, (num, text, color) in enumerate(items):
    y = Inches(3.2) + Inches(i * 1.1)
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(3), y, Inches(0.7), Inches(0.7))
    circle.fill.solid()
    circle.fill.fore_color.rgb = color
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(24)
    tf.paragraphs[0].font.color.rgb = WHITE
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    add_text_box(slide, Inches(4), y + Inches(0.1), Inches(6), Inches(0.6), text, font_size=24, color=WHITE)

add_text_box(slide, Inches(2), Inches(6.3), Inches(9), Inches(0.6), '项目地址：https://datawhalechina.github.io/easy-vibe/zh-cn/', font_size=14, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)

# ===================== SLIDE 7: Day 1 Goals =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), 'Day 1 我们要达成什么？', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

goals = [
    '✅  理解 Vibe Coding 的核心思维',
    '✅  成功安装并配置 Cursor 开发环境',
    '✅  独立生成并美化第一个 "Hello Vibe" 网页',
    '✅  建立"我也能用 AI 做产品"的强烈信心',
]
for i, goal in enumerate(goals):
    y = Inches(2.3) + Inches(i * 1.1)
    box = add_shape_bg(slide, Inches(1.2), y, Inches(10.5), Inches(0.85), RGBColor(0x1A, 0x11, 0x4B))
    add_text_box(slide, Inches(1.6), y + Inches(0.15), Inches(9.5), Inches(0.6), goal, font_size=22, color=WHITE)

# ===================== SLIDE 8: Core Tool =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '今天我们重点掌握的工具', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

cursor_box = add_shape_bg(slide, Inches(2), Inches(2.5), Inches(9), Inches(2.5), RGBColor(0x1A, 0x11, 0x4B))
add_text_box(slide, Inches(2.5), Inches(2.8), Inches(8), Inches(1), 'Cursor', font_size=48, color=PURPLE, bold=True, alignment=PP_ALIGN.CENTER)
add_text_box(slide, Inches(2.5), Inches(3.8), Inches(8), Inches(0.8), 'AI 时代的代码编辑器', font_size=24, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)

add_text_box(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.6), '后续课程还会用到：Claude、Vercel、Supabase、Dify 等', font_size=18, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)

# ===================== SLIDE 9: Why Cursor =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), 'Cursor 到底有多强？', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

features = [
    ('🧠', '深度集成 Claude / GPT-4o / Grok 等顶级模型'),
    ('✏️', 'Composer 模式（多文件智能编辑）'),
    ('💡', '智能自动补全与对话式编程'),
    ('👁️', '支持一键预览网页'),
    ('🆓', '完全免费基础版即可满足日常使用'),
]
for i, (icon, text) in enumerate(features):
    y = Inches(2.2) + Inches(i * 0.95)
    box = add_shape_bg(slide, Inches(1.2), y, Inches(10.5), Inches(0.75), RGBColor(0x1A, 0x11, 0x4B))
    add_text_box(slide, Inches(1.6), y + Inches(0.1), Inches(9.5), Inches(0.6), f'{icon}  {text}', font_size=20, color=WHITE)

# ===================== SLIDE 10: Step 1 =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), 'Step 1  下载并安装 Cursor', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

steps = [
    ('1', '浏览器访问 cursor.com'),
    ('2', '点击 "Download"'),
    ('3', '选择你的操作系统（Mac / Windows / Linux）'),
    ('4', '下载完成后正常安装'),
]
for i, (num, text) in enumerate(steps):
    y = Inches(2.2) + Inches(i * 1.0)
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.5), y, Inches(0.6), Inches(0.6))
    circle.fill.solid()
    circle.fill.fore_color.rgb = PURPLE
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(22)
    tf.paragraphs[0].font.color.rgb = WHITE
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    add_text_box(slide, Inches(2.5), y + Inches(0.1), Inches(8), Inches(0.6), text, font_size=22, color=WHITE)

add_text_box(slide, Inches(1.2), Inches(6.2), Inches(10), Inches(0.6), '⚠️ Windows 用户双击安装，Mac 用户拖入「应用程序」文件夹', font_size=16, color=YELLOW)

# ===================== SLIDE 11: Step 2 =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), 'Step 2  登录并绑定 AI 模型', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

steps = [
    ('1', '用 GitHub 账号登录（推荐）'),
    ('2', '进入 Settings → Models'),
    ('3', '绑定你常用的模型（推荐 Claude 3.5/4 或 GPT-4o）'),
    ('4', '开启 Auto Suggestion（智能提示）'),
]
for i, (num, text) in enumerate(steps):
    y = Inches(2.2) + Inches(i * 1.0)
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.5), y, Inches(0.6), Inches(0.6))
    circle.fill.solid()
    circle.fill.fore_color.rgb = PURPLE
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(22)
    tf.paragraphs[0].font.color.rgb = WHITE
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    add_text_box(slide, Inches(2.5), y + Inches(0.1), Inches(8), Inches(0.6), text, font_size=22, color=WHITE)

# ===================== SLIDE 12: Step 3 =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), 'Step 3  创建你的第一个 Vibe 项目', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

steps = [
    ('1', '在电脑上新建文件夹 → my-first-vibe'),
    ('2', '用 Cursor 打开该文件夹'),
    ('3', '准备完成！🎉'),
]
for i, (num, text) in enumerate(steps):
    y = Inches(2.5) + Inches(i * 1.2)
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.5), y, Inches(0.6), Inches(0.6))
    circle.fill.solid()
    circle.fill.fore_color.rgb = PURPLE
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(22)
    tf.paragraphs[0].font.color.rgb = WHITE
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    add_text_box(slide, Inches(2.5), y + Inches(0.1), Inches(8), Inches(0.6), text, font_size=22, color=WHITE)

# ===================== SLIDE 13: Cursor UI =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), 'Cursor 界面一分钟熟悉', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

areas = [
    ('📁 左侧', '文件浏览器'),
    ('💬 右侧/下方', 'Chat 对话面板'),
    ('⌨️ Cmd/Ctrl + K', '快速询问 AI'),
    ('⌨️ Cmd/Ctrl + L', '进入 Composer 模式'),
    ('🖱️ 右键文件', 'Open in Browser'),
]
for i, (key, desc) in enumerate(areas):
    y = Inches(2.2) + Inches(i * 0.95)
    box = add_shape_bg(slide, Inches(1.2), y, Inches(10.5), Inches(0.75), RGBColor(0x1A, 0x11, 0x4B))
    add_text_box(slide, Inches(1.6), y + Inches(0.1), Inches(3.5), Inches(0.6), key, font_size=20, color=PURPLE, bold=True)
    add_text_box(slide, Inches(5.5), y + Inches(0.1), Inches(5.5), Inches(0.6), desc, font_size=20, color=WHITE)

# ===================== SLIDE 14: First Prompt =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '现在，让我们生成第一个网页！', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

prompt_box = add_shape_bg(slide, Inches(1), Inches(2.2), Inches(11), Inches(4.5), RGBColor(0x1A, 0x11, 0x4B))
add_text_box(slide, Inches(1.4), Inches(2.4), Inches(10), Inches(0.6), 'Prompt 示例：', font_size=20, color=GREEN, bold=True)

prompt_text = (
    '请创建一个现代风格的"Hello Vibe"欢迎页面：\n'
    '- 深蓝到紫色渐变背景\n'
    '- 大标题：会说话，就会做应用\n'
    '- 副标题：我是 [你的名字] 的第一个 AI 作品\n'
    '- 添加一个彩色按钮，点击弹出欢迎消息\n'
    '- 整体科技感强，简洁高级'
)
add_text_box(slide, Inches(1.4), Inches(3.2), Inches(10), Inches(3), prompt_text, font_size=18, color=WHITE)

# ===================== SLIDE 15: Demo =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '🛠️  实操演示：生成你的第一个网页', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

demo_steps = [
    '1. 在 Cursor 中新建 index.html 文件',
    '2. 打开 Composer（Cmd/Ctrl + L）',
    '3. 输入上面的 Prompt',
    '4. 等待 AI 生成代码（约 10-30 秒）',
    '5. 右键文件 → Open in Browser 预览',
    '6. 🎉 恭喜！你刚刚用 AI 做出了第一个网页！',
]
for i, step in enumerate(demo_steps):
    y = Inches(2.2) + Inches(i * 0.8)
    add_text_box(slide, Inches(1.5), y, Inches(10), Inches(0.6), step, font_size=20, color=WHITE)

# ===================== SLIDE 16: Iteration =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '🔄  迭代优化：让网页更完美', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

add_text_box(slide, Inches(1), Inches(2.2), Inches(10), Inches(0.6), 'Vibe Coding 的核心就是持续对话迭代！', font_size=22, color=LIGHT_PURPLE, bold=True)

iter_prompts = [
    '💬 "把按钮改成渐变紫色，更大一点"',
    '💬 "添加一个动态粒子背景效果"',
    '💬 "加一个打字机效果的副标题"',
    '💬 "让页面支持深色/浅色模式切换"',
]
for i, prompt in enumerate(iter_prompts):
    y = Inches(3.2) + Inches(i * 0.9)
    box = add_shape_bg(slide, Inches(1.2), y, Inches(10.5), Inches(0.7), RGBColor(0x1A, 0x11, 0x4B))
    add_text_box(slide, Inches(1.6), y + Inches(0.1), Inches(9.5), Inches(0.5), prompt, font_size=18, color=WHITE)

# ===================== SLIDE 17: Common Issues =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '⚠️  常见问题与解决', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

issues = [
    ('Q: Cursor 下载速度慢？', 'A: 可使用镜像站或 VPN 加速下载'),
    ('Q: AI 生成的代码有 Bug？', 'A: 直接告诉 AI 报错信息，它会自动修复'),
    ('Q: 预览页面空白？', 'A: 检查文件是否保存，尝试刷新浏览器'),
    ('Q: 模型响应慢？', 'A: 可在 Settings 中切换其他模型'),
]
for i, (q, a) in enumerate(issues):
    y = Inches(2.2) + Inches(i * 1.2)
    add_text_box(slide, Inches(1.2), y, Inches(10), Inches(0.5), q, font_size=20, color=YELLOW, bold=True)
    add_text_box(slide, Inches(1.2), y + Inches(0.5), Inches(10), Inches(0.5), a, font_size=18, color=LIGHT_GRAY)

# ===================== SLIDE 18: Key Takeaways =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '📝  Day 1 关键收获', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

takeaways = [
    '🧠  Vibe Coding = 用自然语言描述需求 + AI 生成代码 + 对话迭代',
    '🛠️  Cursor 是目前最强大的 AI 编程工具之一',
    '🚀  你已经能独立用 AI 生成一个网页了！',
    '🔄  持续迭代是 Vibe Coding 的核心方法论',
]
for i, item in enumerate(takeaways):
    y = Inches(2.3) + Inches(i * 1.1)
    box = add_shape_bg(slide, Inches(1.2), y, Inches(10.5), Inches(0.85), RGBColor(0x1A, 0x11, 0x4B))
    add_text_box(slide, Inches(1.6), y + Inches(0.15), Inches(9.5), Inches(0.6), item, font_size=20, color=WHITE)

# ===================== SLIDE 19: Homework =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '🏠  课后作业', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

hw_box = add_shape_bg(slide, Inches(1), Inches(2.2), Inches(11), Inches(4), RGBColor(0x1A, 0x11, 0x4B))
add_text_box(slide, Inches(1.5), Inches(2.5), Inches(10), Inches(0.6), '用 Cursor 生成一个个人介绍网页', font_size=24, color=GREEN, bold=True)
add_bullet_list(slide, Inches(1.5), Inches(3.3), Inches(10), Inches(2.5), [
    '包含你的名字、一句话介绍、兴趣爱好',
    '使用渐变背景 + 至少一个动画效果',
    '添加一个"关于我"按钮，点击展开详情',
    '截图分享到学习群，获得导师反馈！',
], font_size=18, color=WHITE, spacing=Pt(14))

# ===================== SLIDE 20: Preview Day 2 =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '🔮  预告：Day 2 我们将学习', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

preview = [
    '💡  如何找到值得做的好想法',
    '📋  产品需求文档（PRD）的写法',
    '🎨  用 AI 快速构建多页面产品原型',
    '🤖  接入 AI 能力让产品更智能',
]
for i, item in enumerate(preview):
    y = Inches(2.5) + Inches(i * 1.0)
    box = add_shape_bg(slide, Inches(1.2), y, Inches(10.5), Inches(0.75), RGBColor(0x1A, 0x11, 0x4B))
    add_text_box(slide, Inches(1.6), y + Inches(0.1), Inches(9.5), Inches(0.6), item, font_size=22, color=WHITE)

# ===================== SLIDE 21: Resources =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(1), '📚  学习资源', font_size=40, color=WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.5), Inches(4), PURPLE)

resources = [
    ('Easy-Vibe 官方教程', 'https://datawhalechina.github.io/easy-vibe/zh-cn/'),
    ('GitHub 仓库', 'https://github.com/datawhalechina/easy-vibe'),
    ('Cursor 官网', 'https://cursor.com'),
    ('交互式附录', 'https://datawhalechina.github.io/easy-vibe/zh-cn/appendix/'),
]
for i, (name, url) in enumerate(resources):
    y = Inches(2.3) + Inches(i * 1.0)
    box = add_shape_bg(slide, Inches(1.2), y, Inches(10.5), Inches(0.75), RGBColor(0x1A, 0x11, 0x4B))
    add_text_box(slide, Inches(1.6), y + Inches(0.1), Inches(3.5), Inches(0.6), name, font_size=20, color=PURPLE, bold=True)
    add_text_box(slide, Inches(5.5), y + Inches(0.1), Inches(5.5), Inches(0.6), url, font_size=16, color=LIGHT_GRAY)

# ===================== SLIDE 22: Thank You =====================
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, BG_DARK)
add_text_box(slide, Inches(1), Inches(2), Inches(11), Inches(2), '感谢参与 Day 1！', font_size=56, color=WHITE, bold=True, alignment=PP_ALIGN.CENTER)
add_accent_line(slide, Inches(5), Inches(3.8), Inches(3.333), PURPLE)
add_text_box(slide, Inches(1), Inches(4.2), Inches(11), Inches(1), '明天见！Day 2 我们将开始构建真正的产品 🚀', font_size=24, color=LIGHT_PURPLE, alignment=PP_ALIGN.CENTER)
add_text_box(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.6), 'Easy-Vibe AI编程 0→1 免费体验营', font_size=18, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)

output_path = r'd:\校友经济\企业AI学习与服务市场\Vibe coding\Day1_Vibe_Coding.pptx'
prs.save(output_path)
print(f'PPT saved to: {output_path}')
