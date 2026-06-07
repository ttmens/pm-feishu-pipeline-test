import re

with open('D:/workspace/projects/pm-feishu-pipeline-test/04-mvp/docs/index.html') as f:
    content = f.read()

# Find :root block boundaries
root_start = content.find(':root {')
brace_count = 0
i = root_start
while i < len(content):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            break
    i += 1
root_end = i + 1

rest = content[:root_start] + content[root_end:]
hex_pattern = re.compile(r'#[0-9a-fA-F]{3,8}\b')
hex_in_rest = hex_pattern.findall(rest)

if hex_in_rest:
    print('FAIL: Found hex colors outside :root:', hex_in_rest)
else:
    print('PASS: All hex colors are only in :root block')

# Count tasks coverage
tasks = ['T1.1', 'T1.2', 'T1.3', 'T2.1', 'T2.2', 'T3.1', 'T3.2', 'T3.3', 'T4.1', 'T5.1', 'T6.1', 'T6.2', 'T6.3']
checks = {
    'viewport': 'viewport' in content,
    'css_variables': '--bg' in content and '--accent' in content,
    'status_header': 'feishu-pipeline-test' in content and 'Complete' in content,
    'stage_count': '7 / 7 stages' in content,
    'progress_bar': 'progress-fill' in content and 'progress-bar' in content,
    'stage_cards': 'stage-card' in content and 'stage-list' in content,
    'hover_effect': 'hover' in content and 'box-shadow' in content,
    'touch_target': 'min-height: 44px' in content or '44px' in content,
    'screen_nav': 'showScreen' in content and 'screen-dashboard' in content and 'screen-stage-detail' in content,
    'back_button': 'back-btn' in content,
    'gate_table': 'gate-table' in content and 'detail-gate-body' in content,
    'artifact_links': 'artifact-links' in content and 'target="_blank"' in content,
    'ext_links': 'ttmens.github.io/pm-pipeline-index' in content and 'github.com/ttmens/pm-feishu-pipeline-test' in content,
    'prototype_screen': 'screen-prototype' in content,
    'mobile_responsive': '@media' in content and 'max-width' in content,
}

print('\n=== Task Coverage ===')
for task, passed in checks.items():
    print(f'  {task}: {"PASS" if passed else "FAIL"}')
print(f'\nPassed: {sum(1 for v in checks.values() if v)}/{len(checks)}')
