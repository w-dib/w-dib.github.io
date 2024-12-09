# frozen_string_literal: true

source "https://rubygems.org"

# Specify the required Ruby version
ruby "~> 3.1"

# Chirpy theme gem
gem "jekyll-theme-chirpy", "~> 7.2", ">= 7.2.2"

# Add jekyll-compose under the :jekyll_plugins group
group :jekyll_plugins do
  gem "jekyll-compose"
end

# Add testing tools
gem "html-proofer", "~> 5.0", group: :test

# Platform-specific gems
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Watchdog gem for Windows
gem "wdm", "~> 0.2.0", :platforms => [:mingw, :x64_mingw, :mswin]
