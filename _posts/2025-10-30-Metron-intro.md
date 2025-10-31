---
layout: post
title: "Hello World"
date: 2025-10-30
categories: [gamedev]
tags: []
---
This is a test of a Jekyll-powered blog hosted on GitHub pages and mapped to a subdomain of my main website.
I'm implementing the bare minimum of CSS styles required to allow me to post very occasional game dev and game audio-related blog posts which might by necessity feature embedded videos, syntax-highlighted code snippets and the occasional table...but not much more.

Test this new paragraph.

**Some bold text**, and *some italics*.

All I need to do to update this blog is to write a new markdown file and commit it to the github repository, whereupon a server-side Jekyll script will turn it into static HTML and hook up all the correct links. The only thing that's a pain in the arse is setting up an easy means of adding images to posts. Obviously I can just link directly to an image file in the repo, but I'm lazy and it'd be nice to have some drag-and-drop flow.

```
Code? Is this code?
Oh, it's literally just indenting 4 spaces or 1 tab?
tab
```

And here's an embedded YouTube video - literally just a paste of the Share->Embed code. It looks fine, which saves me having to wrap it and override styles.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dhieS6isR1k?si=OKyypJU3iRSIXvka" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<small>And because I can mix and match HTML and markdown, here I'm using the `<small>` tag to sort of caption the video. </small>

Language-specific syntax highlighting seems to work, if I specify the language; I've added some basic styles, but they really are *very* basic.

```c++
void ReturnValue(const int inVal)
{
    return inVal;
}
```

|This is |a Table|
|-------|-----------|
|Header | Title     |
|Content| Value     |


What about inline code? `What if this were inline code?` But not this?
And then if there were lots of text constituting the remainder of a paragraph that was relatively substantial, covering a whole range of diverse and interesting topics.