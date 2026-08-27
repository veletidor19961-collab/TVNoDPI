from pathlib import Path
import re
import sys

root = Path(sys.argv[1])

# Rename app in all localized strings.xml files.
for p in root.rglob('strings.xml'):
    try:
        s = p.read_text(encoding='utf-8')
    except Exception:
        continue
    if 'name="app_name"' in s:
        s = re.sub(
            r'<string name="app_name">.*?</string>',
            '<string name="app_name">TVNoDPI</string>',
            s,
            count=1,
        )
        p.write_text(s, encoding='utf-8')

main = root / 'app/src/main/java/io/github/romanvht/byedpi/activities/MainActivity.kt'
s = main.read_text(encoding='utf-8')

# Put initial D-pad focus on the main power button.
focus_needle = '        ShortcutUtils.update(this)\n'
if focus_needle in s and 'binding.statusButtonCard.requestFocus()' not in s:
    s = s.replace(
        focus_needle,
        focus_needle + '        binding.statusButtonCard.requestFocus()\n',
        1,
    )

# Add top-bar Settings action handler.
if 'R.id.action_settings -> {' not in s:
    diagnostics_case = '            R.id.action_diagnostics -> {\n'
    settings_case = (
        '            R.id.action_settings -> {\n'
        '                val settingsIntent = Intent(this, SettingsActivity::class.java)\n'
        '                startActivity(settingsIntent)\n'
        '                true\n'
        '            }\n\n'
    )
    if diagnostics_case not in s:
        raise RuntimeError('Could not locate diagnostics menu handler in MainActivity.kt')
    s = s.replace(diagnostics_case, settings_case + diagnostics_case, 1)

main.write_text(s, encoding='utf-8')
print('TVNoDPI patch applied successfully')
