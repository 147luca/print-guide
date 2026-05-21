#!/bin/bash
# One-command deploy for print-guide.
# Rebuilds the site and force-pushes the built output to the gh-pages branch,
# which GitHub Pages serves live. Use after adding/editing content.
#
#   ./deploy.sh
#
# (CI auto-deploy via .github/workflows/hugo.yml is available too, but needs the
#  gh token to have `workflow` scope: `gh auth refresh -s workflow`, then re-add
#  + push that file. Until then, this script is the deploy path.)
set -e

REPO="/Users/luca/print-guide"
HUGO="/opt/homebrew/bin/hugo"
REMOTE="https://github.com/147luca/print-guide.git"

cd "$REPO"
echo "Building..."
"$HUGO" --gc --minify
touch public/.nojekyll

cd public
[ -d .git ] || git init -q -b gh-pages
git config user.name "Luca"
git config user.email "147luca@users.noreply.github.com"
git add -A
if git commit -q -m "Deploy $(date '+%Y-%m-%d %H:%M')"; then
  git push -f "$REMOTE" gh-pages
  echo "Deployed -> https://147luca.github.io/print-guide/"
else
  echo "No changes to deploy."
fi
