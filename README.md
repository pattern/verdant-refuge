# Verdant Refuge

This is my personal website (Jeff Pickelman)

## Hyde

It is built using [hyde][hyde] (Version 0.8.5a14), a Python static
website generator inspired by it's Ruby brother [jekyll][jekyll].

[hyde]: https://github.com/hyde/hyde "Hyde static website generator"
[jekyll]: http://jekyllrb.com/ "Jekyll: blog-aware, static site generator in Ruby"

Note that this current version of hyde was the result of a major
refactor/restructuring of the original codebase located here: [old
hyde][hyde-old].  As such, much of the "hyde" documentation available
refers to the previous iteration and isn't particularly helpful in
getting things working perfectly, but is still useful in getting a
handle on what hyde is all about and how it has been used before.

[hyde-old]: https://github.com/lakshmivyas/hyde "Static website generator inspired by Jekyll (Deprecated)"

## Plugins

This section contains a list of the current plugins I am using for this
site, and a description of what they are used for.

-   **MetaPlugin** - This allow metadata to be easily included about
    any files.  All the `meta.yaml` files in the directory tree of a
    given file are evaluated, then the [YAML front matter][yaml] of the
    file is evaluated.  The inheritance allows you to keep [DRY][dry]
    while still being as descriptive as needed.

[yaml]: https://github.com/mojombo/jekyll/wiki/yaml-front-matter "Describes YAML front matter - ignore the Jekyll-specific bits!"
[dry]: http://en.wikipedia.org/wiki/Don't_repeat_yourself "Wikipedia: Don't Repeat Yourself (DRY)"

-   **AutoExtendPlugin** - This plugin wires up the `extends` and
    `default_block` keys in the YAML front matter, allowing for easy
    template inheritance.

-   **UrlCleanerPlugin** - Allows for tighter control of the URLs of
    the site.  You can choose which extensions to hide and whether to
    append a trailing slash, and whether to drop "index.html" from the
    end of urls containing it.

-   **TaggerPlugin** - This wires up the `tags` key in the front
    matter.  It takes a list of tags to be associated with the file.

-   **SorterPlugin** - This allows you to define sorted sets of content
    which obey certain requirements.  The most common example - and the
    only list I have defines thus far - is a listing of blog posts,
    sorted in reverse creation order, omitting all non-listable posts.
    For each sorted set, you have access to
    `walk_resources_sorted_by_[name]`, `prev_by_[name]`, and
    `next_by_[name]`.

-   **TextlinksPlugin** - This simply gives you a more concise way to
    link to both content urls, and media urls.

## Known Bugs

-   **jQuery.timeago** (9/27/2012): The jquery.timeago.js plugin
    doesn't seem to be working correctly on iOS devices - on an iPhone
    it displays "NAN Years Ago" instead of the actual timeago.

