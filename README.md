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

-   [AutoExtendPlugin][1] - This plugin wires up the `extends` and
    `default_block` keys in the YAML front matter, allowing for easy
    template inheritance.

-   [UrlCleanerPlugin][2] - Allows for tighter control of the URLs of
    the site.  You can choose which extensions to hide and whether to
    append a trailing slash, and whether to drop "index.html" from the
    end of urls containing it.

-   [TaggerPlugin][3] - This wires up the `tags` key in the front
    matter.  It takes a list of tags to be associated with the file.

-   [SorterPlugin][4] - This allows you to define sorted sets of content
    which obey certain requirements.  The most common example - and the
    only list I have defines thus far - is a listing of blog posts,
    sorted in reverse creation order, omitting all non-listable posts.
    For each sorted set, you have access to
    `walk_resources_sorted_by_[name]`, `prev_by_[name]`, and
    `next_by_[name]`.

-   [TextlinksPlugin][5] - This simply gives you a more concise way to
    link to both content urls, and media urls.

-   [ImageSizerPlugin][6] - This adds the _height_ and _width_
    attributes to `<img>`s which don't already have them. This is good
    practice for page rendering reasons. Also could come in handy if I
    ever decide to implement delayed-loading of images (so the
    placeholders would have correct dimensions).

[1]: https://github.com/hyde/hyde/blob/master/hyde/ext/plugins/auto_extend.py
[2]: https://github.com/hyde/hyde/blob/master/hyde/ext/plugins/urls.py
[3]: https://github.com/hyde/hyde/blob/master/hyde/ext/plugins/tagger.py
[4]: https://github.com/hyde/hyde/blob/master/hyde/ext/plugins/sorter.py
[5]: https://github.com/hyde/hyde/blob/master/hyde/ext/plugins/textlinks.py
[6]: https://github.com/hyde/hyde/blob/master/hyde/ext/plugins/images.py

## Typical Development Usage

Have two terminal windows open. In the first, `cd` to project directory and `workon vr`. In the second, do the same, and then `compass watch`. Whenever the site needs to be rebuilt and tested locally, run `fab serve`, which will host the site at `http://loalhost:8080/`.

## Publishing to Amazon S3

In the Verdant Refuge virtualenv folder, I appended the following to the `bin/activate` script which is run whenever the environment is activated:

    :::bash
    AWS_ACCESS_KEY_ID=<<REDACTED>>
    export AWS_ACCESS_KEY_ID

    AWS_SECRET_ACCESS_KEY=<<REDACTED>>
    export AWS_SECRET_ACCESS_KEY

This exports the necessary bash environment variables so that the [boto][boto] library can authenticate with S3. This is detailed on the linked boto Github project page.

[boto]: https://github.com/boto/boto "Github: boto project home"


## Todo

-   Need a `apple-touch-icon.png` in the base directory.

-   Make sure overflow scroller looks good and functions in code
    blocks ([antiscroll](https://github.com/LearnBoost/antiscroll/blob/master/index.html)).

-   Create a Fabric function for creating new posts.

-   Consider changing the deployment process to deploy the HEAD as
    opposed to the current local filesystem.

## Known Bugs

-   **jQuery.timeago** (9/27/2012): The jquery.timeago.js plugin
    doesn't seem to be working correctly on iOS devices - on an iPhone
    it displays "NAN Years Ago" instead of the actual timeago.

