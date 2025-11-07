# 维港科技创新小组（VHSTIT）的官方主页

这是一个基于 MkDocs Material 框架构建的现代化技术文档网站。

## 🌟 项目简介

本项目使用 MkDocs Material 框架创建，旨在提供优雅、响应式且功能丰富的技术文档展示平台。Material for MkDocs 是一个基于 Google Material Design 的 MkDocs 主题，为技术文档提供了现代化的外观和优秀的用户体验。

## 🚀 技术栈

### 核心框架
- **MkDocs** - 基于 Python 的静态网站生成器
- **Material for MkDocs** - Material Design 风格的 MkDocs 主题
- **Python 3.8+** - 后端运行环境

### 前端技术
- **Material Design** - Google 的设计语言
- **CSS3** - 样式和动画
- **JavaScript** - 交互功能
- **Markdown** - 文档编写格式

### 特色功能
- ✅ 响应式设计，支持移动端
- ✅ 深色/浅色主题切换
- ✅ 实时搜索功能
- ✅ 代码语法高亮
- ✅ 数学公式支持（LaTeX）
- ✅ 目录导航和面包屑
- ✅ 多语言支持
- ✅ 社交媒体集成

### GitHub Pages
```yaml
# .github/workflows/ci.yml
name: ci
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

## 📈 性能优化

- 静态资源压缩
- 图片懒加载
- CSS/JS 最小化
- CDN 资源加速
- 浏览器缓存优化

---

*最后更新: 2025/11/07*
