# READ ME!

## Here are the HTML and CSS containers, beside some other files. These files are being hosted on the Website.

The Website will contain links to codes on this page. This makes the Website more flexible and easier to maintain. Sudden changes of Rules and such will be simple to achive.
You can find some general information and a guide in here. 
Our Discord server is a good source, if you want to stay up to date. You can find updates related to the game server and the website in there.



# HTML structure guide

## This guide helps contributors editing and creating pages for my website. 

### Headings
Headings are being used to give a description of an article in one or a few words. There are three "real headings": h1, h2, h3. 
The other heading, h4, is not a heading used for this purpose. It's a grey colored paragraph and can be used as a footnote. Quick example: After a video/image
you can give a side note and similar about the media using h4. In this case it should be centered above or below the embedded file.

- h1: The main [title](https://github.com/Goetterescu/Website/blob/main/Codes/Title%20and%20menu.html) of the website
- h2: For titles of the menu and pages
- h3: Title format for articles or important stuff

### Breaks
`<hr>` should be used after every article. Right at the end. It also comes after the first description of a page (below the paragraph which comes after h2).
`<br>` can be used if necessary. It is not being used after titles. After a title comes the paragraph and maybe another title. But no break. 
It can be used to add some distance between a paragraph and an image. But not after a title and a image, or title and a table.

### Traffic violation reports
Please stick to the following structure.
```
<h3 style="text-align:center">Case X</h3>
<table style="width:30%">
<tr style="background-color:gray">
<th>Suspect</th>
<th>Officer</th>
<th>Infractions</th>
<th>Points</th>
</tr><tr>
<td>+++</td>
<td>+++</td>
<td>+++</td>
<td>+++</td>
</tr></table>
<br><h3>Protocol:</h3>
<p>+++
<br><br>- +++ XX/XX/XX</p>
<br><div style="text-align:center"><h4>Proof</h4>
<!-- Please insert your proofs below. Do not change the width! -->
<img width="40%" href="+++">
</div><hr>
```
In this example "+++" are the placeholders for your input and "X" stands for a number. Like the case number or the date of the infraction.

### Event pages
This is a different kind of page. It usually contains a long list of articles and should have an index. This will help visitors navigate through the page.
Here is a quick example on how an event page should be structured. Note: This example is missing a bunch of things, it's supposed to be easy to read and won't function.
It also contains the articles which are necessary for every event.

```
<embedded title and menu>
  <div auftl>
    <h2>Title of the event</h2>
    <p>Description<p>
    maybe some more content. break might be required
    <hr>
    <h3>article 1</h3>
    <p>some info</p>
    <br>
    <img/>
    maybe h4 centered below it
    <hr>
    <h3>rules</h3>
    a list of rules
    <hr>
    <h3>moderators</h3>
    info for mods
    <hr>
    <h3>leaderboard</h3>
    <p>info</p>
    <h3>table</h3>
    <table>
    <p>more info</p>
    <hr>
    <h3>allowed vehicles and objects</h3>
    <list>
    
    Here comes the rest of the page.
 ```
    
### There will be more
I just started creating this guide. Stay tuned for more!



# Here is some stuff that I want to achieve with my Community

### Staff-Event
This is supposed to be done by my Staff. I want them to work on an Event by themselves.
- [ ] Discuss an Event with the Community
- [ ] Plan and script an Event
- [ ] Code the Page
- [ ] Check it using the formation guide on Github
- [ ] Get it checked by the Project Leader

