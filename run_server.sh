#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
gem_home="$project_root/.bundle/gems"
bundle_bin="$gem_home/bin/bundle"

if [[ ! -f "$bundle_bin" ]]; then
  echo "Local Ruby dependencies are missing. Install them before starting the preview." >&2
  exit 1
fi

cd "$project_root"

# The macOS system Ruby reports Apple Silicon as a universal platform, while
# this repository's lockfile records the equivalent arm64 GitHub Pages build.
export GEM_HOME="$gem_home"
export GEM_PATH="$gem_home"
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"

exec /usr/bin/ruby -e '
  require "rubygems"
  class << Gem::Platform
    def local
      Gem::Platform.new("arm64-darwin-22")
    end
  end
  load File.join(ENV.fetch("GEM_HOME"), "bin", "bundle")
' -- _2.2.19_ exec jekyll liveserve "$@"
