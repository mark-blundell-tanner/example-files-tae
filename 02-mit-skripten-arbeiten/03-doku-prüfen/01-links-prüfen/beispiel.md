<!-- Verwenden Sie den Skript check-links.py, um die Links automatisiert zu prüfen -->

# Example Links for Testing

This document contains various links to test the link checker script.

## Working Links

Here are some links that should work correctly:

- [GitHub](https://github.com)
- [Python Official Website](https://www.python.org)
- [Stack Overflow](https://stackoverflow.com)
- [Wikipedia](https://en.wikipedia.org)

## Broken Links (404 Errors)

These links should return 404 errors:

- [Non-existent GitHub Page](https://github.com/this-definitely-does-not-exist-12345)
- [Broken Python Docs Link](https://docs.python.org/nonexistent-page-404)
- [Invalid Wikipedia Article](https://en.wikipedia.org/wiki/This_Article_Does_Not_Exist_404_Test)
- [Non-existent Domain Path](https://www.example.com/path/that/does/not/exist/404)

## Mixed Content

You can also test with mixed content:

- Here's a [valid link to Mozilla](https://www.mozilla.org)
- And here's a [broken link example](https://httpstat.us/404)
- Another [working link to W3C](https://www.w3.org)
- And a [definitely broken link](https://www.github.com/fake-user-12345/fake-repo-67890/fake-file)

## Instructions

To run the link checker:

```bash
python check-links.py
```

The script will check all markdown files in the current directory and report the status of each HTTPS link.
