#!/bin/bash
# sawzan-site: git push の前に、必ず利用者の確認を求める(公開は、ユーザーが「公開して」と言うまで行わない。CLAUDE.md)。
input=$(cat)
command=$(echo "$input" | python3 -c "import json,sys; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null)
if echo "$command" | grep -qE "git[[:space:]]+(-C[[:space:]]+[^[:space:]]+[[:space:]]+)?push" && ! echo "$command" | grep -q -- "--dry-run"; then
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"sawzan-siteのpushは公開です。ユーザーが「公開して」と言ったときだけ進めます。"}}'
fi
exit 0
