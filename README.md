# Echolevel.co.uk static site for GitHub Pages

## Install

Requirements:
* Ruby (recommended: Ruby+Devkit for Windows)
* Bundler (Ruby gem)
* Jekyll will be installed via Bundler from the Gemfile
* Git

Make sure Ruby is in the PATH:
```
ruby -v
gem -v
```

Clone the repo
```
git clone <REPO_URL>
cd echolevel.github.io
```

Install gems from the Gemfile
```
gem install bundler
bundle install
```

## Run local environment

Run local dev server with LiveReload
.\run.ps1

What it does:
* runs ``bundle exec jekyll serve --livereload --force_polling``
* opens the site at ``http://127.0.0.1:4000/``

## VSCode 

Add this shortcut to user keybindings.json:

```
{
    "key": "ctrl+alt+n",
    "command": "workbench.action.tasks.runTask",
    "args": { "task": "New Jekyll post (Python)" },
    "when": "resourcePath =~ /echolevel\\.github\\.io/"
}
```


Use ``ctrl+alt+n`` to prompt for a title and create a new markdown file for a blogpost with the current timestamp and all the front matter (post metadata) set up correctly.

Install the Paste Image extension by mushan, then use ``ctrl+alt+v`` to store whatever image is in the clipboard to /assets/img/ and generate image markdown in the current file.