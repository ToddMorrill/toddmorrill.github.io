# [toddmorrill.github.io](http://toddmorrill.github.io)

#### [Jekyll site setup](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll)
- `brew install ruby`
- `echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc`
- delete `Gemfile.lock` (if on new computer)
- `bundle install`
- may need to run `sudo gem install bundler`
- to serve run `bundle exec jekyll serve --watch --drafts`