from pathlib import Path
root = Path(__file__).resolve().parent.parent
dist = root / 'dist'
html = (dist / 'index.html').read_text()
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>' + (dist / 'style.css').read_text() + '</style>')
for name in ['app.js']:
    source = (dist / name).read_text().replace('</script', '<\\/script')
    html = html.replace('<script src="' + name + '"></script>', '<script>' + source + '</script>')
(root / '习惯手记.html').write_text(html)
