



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-e53fc1ddbde2a9e5645df620f65c80ef723c741b33293b6f22a2b7f2c8145fcf.css" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-4664ce357daee067bd8ee8e99e0833d04b115022dbf4ca637241c0f7d1f832b7.css" media="all" rel="stylesheet" />
    
    
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-4b977eeae4ecbfd2f7a7ad7788382645b21e771bbf47835e3793edb12292ff2e.css" media="all" rel="stylesheet" />
    

    <link as="script" href="https://assets-cdn.github.com/assets/frameworks-404cdd1add1f710db016a02e5e31fff8a9089d14ff0c227df862b780886db7d5.js" rel="preload" />
    
    <link as="script" href="https://assets-cdn.github.com/assets/github-bda6c8f3d777243f9192f7725d680673aa13394eaeee5081e53f00e42e950028.js" rel="preload" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    <meta content="origin" name="referrer" />
    
    <title>server.py · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://gist.github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://avatars2.githubusercontent.com/u/14987395?v=3&amp;s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="server.py" name="twitter:title" /><meta content="" name="twitter:description" />
      <meta content="https://avatars2.githubusercontent.com/u/14987395?v=3&amp;s=400" property="og:image" /><meta content="Gist" property="og:site_name" /><meta content="object" property="og:type" /><meta content="server.py" property="og:title" /><meta content="https://gist.github.com/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c" property="og:url" /><meta content="" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="gist_code" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-4">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="gist" name="octolytics-app-id" /><meta content="36ADE2CC:3C6B:982620D:57905DB1" name="octolytics-dimension-request_id" />
<meta content="/&lt;user-name&gt;/&lt;gist-id&gt;" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged Out">


    <meta content="false" name="octolytics-dimension-public" /><meta content="38025701" name="octolytics-dimension-gist_id" /><meta content="377848ecbbf5385e8ebcb8516ea7ac2c" name="octolytics-dimension-gist_name" /><meta content="false" name="octolytics-dimension-anonymous" /><meta content="14987395" name="octolytics-dimension-owner_id" /><meta content="ndarshanrestless" name="octolytics-dimension-owner_login" /><meta content="false" name="octolytics-dimension-forked" />

  <meta class="js-ga-set" name="dimension5" content="secret">
  <meta class="js-ga-set" name="dimension6" content="owned">
  <meta class="js-ga-set" name="dimension7" content="python">



        <meta name="hostname" content="gist.github.com">
    <meta name="user-login" content="">

        <meta name="expected-hostname" content="gist.github.com">
      <meta name="js-proxy-site-detection-payload" content="NTdiNTUyMThkNmMxNmY4MmE3M2ZjYzU4MmE0ZDFhYzEyMzI4YjljZjgxZjc4YmJmY2UxMzNlZGRhMDkyZDVjYnx7InJlbW90ZV9hZGRyZXNzIjoiNTQuMTczLjIyNi4yMDQiLCJyZXF1ZXN0X2lkIjoiMzZBREUyQ0M6M0M2Qjo5ODI2MjBEOjU3OTA1REIxIiwidGltZXN0YW1wIjoxNDY5MDc4OTYxfQ==">


      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta name="html-safe-nonce" content="b7c360067cda254a4ebe30df7a2c07012116951b">
    <meta content="8f20d27857ea8577362ced8443d61cd4f3d24200" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="c85c9b6f8432cc7b07e5ce5161e4d4fc">
    

        <link href="/ndarshanrestless.atom" rel="alternate" title="atom" type="application/atom+xml">
  <meta content="noindex, follow" name="robots" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/gist-8023a6701460564568375656828f60112d6894587d6f9a03b77d18a97f6d8fc6.css" media="all" rel="stylesheet" />


  </head>


  <body class="logged-out   env-production">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



        <div class="header gist-header header-logged-out" role="banner">
  <div class="container clearfix">

    <a href="/" aria-label="Gist Homepage" class="header-logo-wordmark" data-hotkey="g d">
      <svg aria-hidden="true" class="octicon octicon-logo-github" height="28" version="1.1" viewBox="0 0 45 16" width="78"><path d="M18.53 12.03h-.02c.009 0 .015.01.024.011h.006l-.01-.01zm.004.011c-.093.001-.327.05-.574.05-.78 0-1.05-.36-1.05-.83V8.13h1.59c.09 0 .16-.08.16-.19v-1.7c0-.09-.08-.17-.16-.17h-1.59V3.96c0-.08-.05-.13-.14-.13h-2.16c-.09 0-.14.05-.14.13v2.17s-1.09.27-1.16.28c-.08.02-.13.09-.13.17v1.36c0 .11.08.19.17.19h1.11v3.28c0 2.44 1.7 2.69 2.86 2.69.53 0 1.17-.17 1.27-.22.06-.02.09-.09.09-.16v-1.5a.177.177 0 0 0-.146-.18zm23.696-2.2c0-1.81-.73-2.05-1.5-1.97-.6.04-1.08.34-1.08.34v3.52s.49.34 1.22.36c1.03.03 1.36-.34 1.36-2.25zm2.43-.16c0 3.43-1.11 4.41-3.05 4.41-1.64 0-2.52-.83-2.52-.83s-.04.46-.09.52c-.03.06-.08.08-.14.08h-1.48c-.1 0-.19-.08-.19-.17l.02-11.11c0-.09.08-.17.17-.17h2.13c.09 0 .17.08.17.17v3.77s.82-.53 2.02-.53l-.01-.02c1.2 0 2.97.45 2.97 3.88zm-8.72-3.61H33.84c-.11 0-.17.08-.17.19v5.44s-.55.39-1.3.39-.97-.34-.97-1.09V6.25c0-.09-.08-.17-.17-.17h-2.14c-.09 0-.17.08-.17.17v5.11c0 2.2 1.23 2.75 2.92 2.75 1.39 0 2.52-.77 2.52-.77s.05.39.08.45c.02.05.09.09.16.09h1.34c.11 0 .17-.08.17-.17l.02-7.47c0-.09-.08-.17-.19-.17zm-23.7-.01h-2.13c-.09 0-.17.09-.17.2v7.34c0 .2.13.27.3.27h1.92c.2 0 .25-.09.25-.27V6.23c0-.09-.08-.17-.17-.17zm-1.05-3.38c-.77 0-1.38.61-1.38 1.38 0 .77.61 1.38 1.38 1.38.75 0 1.36-.61 1.36-1.38 0-.77-.61-1.38-1.36-1.38zm16.49-.25h-2.11c-.09 0-.17.08-.17.17v4.09h-3.31V2.6c0-.09-.08-.17-.17-.17h-2.13c-.09 0-.17.08-.17.17v11.11c0 .09.09.17.17.17h2.13c.09 0 .17-.08.17-.17V8.96h3.31l-.02 4.75c0 .09.08.17.17.17h2.13c.09 0 .17-.08.17-.17V2.6c0-.09-.08-.17-.17-.17zM8.81 7.35v5.74c0 .04-.01.11-.06.13 0 0-1.25.89-3.31.89-2.49 0-5.44-.78-5.44-5.92S2.58 1.99 5.1 2c2.18 0 3.06.49 3.2.58.04.05.06.09.06.14L7.94 4.5c0 .09-.09.2-.2.17-.36-.11-.9-.33-2.17-.33-1.47 0-3.05.42-3.05 3.73s1.5 3.7 2.58 3.7c.92 0 1.25-.11 1.25-.11v-2.3H4.88c-.11 0-.19-.08-.19-.17V7.35c0-.09.08-.17.19-.17h3.74c.11 0 .19.08.19.17z"></path></svg>
      <svg aria-hidden="true" class="octicon octicon-logo-gist" height="28" version="1.1" viewBox="0 0 25 16" width="40"><path d="M4.7 8.73h2.45v4.02c-.55.27-1.64.34-2.53.34-2.56 0-3.47-2.2-3.47-5.05 0-2.85.91-5.06 3.48-5.06 1.28 0 2.06.23 3.28.73V2.66C7.27 2.33 6.25 2 4.63 2 1.13 2 0 4.69 0 8.03c0 3.34 1.11 6.03 4.63 6.03 1.64 0 2.81-.27 3.59-.64V7.73H4.7v1zm6.39 3.72V6.06h-1.05v6.28c0 1.25.58 1.72 1.72 1.72v-.89c-.48 0-.67-.16-.67-.7v-.02zm.25-8.72c0-.44-.33-.78-.78-.78s-.77.34-.77.78.33.78.77.78.78-.34.78-.78zm4.34 5.69c-1.5-.13-1.78-.48-1.78-1.17 0-.77.33-1.34 1.88-1.34 1.05 0 1.66.16 2.27.36v-.94c-.69-.3-1.52-.39-2.25-.39-2.2 0-2.92 1.2-2.92 2.31 0 1.08.47 1.88 2.73 2.08 1.55.13 1.77.63 1.77 1.34 0 .73-.44 1.42-2.06 1.42-1.11 0-1.86-.19-2.33-.36v.94c.5.2 1.58.39 2.33.39 2.38 0 3.14-1.2 3.14-2.41 0-1.28-.53-2.03-2.75-2.23h-.03zm8.58-2.47v-.86h-2.42v-2.5l-1.08.31v2.11l-1.56.44v.48h1.56v5c0 1.53 1.19 2.13 2.5 2.13.19 0 .52-.02.69-.05v-.89c-.19.03-.41.03-.61.03-.97 0-1.5-.39-1.5-1.34V6.94h2.42v.02-.01z"></path></svg>
</a>
    <div class="site-search js-site-search" role="search">
        <div class="header-search" role="search">

<!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/search" class="position-relative" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="header-search-wrapper form-control js-chromeless-input-container">
    <input type="text"
      class="form-control js-site-search-focus header-search-input"
      data-hotkey="s"
      name="q"
      placeholder="Search…"
      tabindex="1"
      autocorrect="off"
      autocomplete="off"
      autocapitalize="off">
  </label>

</form></div>

    </div>
    <ul class="header-nav left" role="navigation">
      <li class="header-nav-item">
        <a href="/discover" class="header-nav-link" data-ga-click="Header, go to all gists, text:all gists">All gists</a>
      </li>

      <li class="header-nav-item">
        <a href="https://github.com" class="header-nav-link" data-ga-click="Header, go to GitHub, text:GitHub">GitHub</a>
      </li>
    </ul>

      <div class="header-actions" role="navigation">
        <a href="/join?source=header-gist" class="btn btn-primary" data-ga-click="Header, sign up">Sign up for a GitHub account</a>
        <a href="https://gist.github.com/auth/github?return_to=gist" class="btn" data-ga-click="Header, sign in">Sign in</a>
      </div>

  </div>
</div>




    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main">
      
  <div itemscope itemtype="http://schema.org/Code">
    <div id="gist-pjax-container" class="gist-content-wrapper" data-pjax-container>
          <div class="gist-detail-intro gist-banner">
      <div class="container">
        <a href="/" class="btn btn-outline right">Create a gist now</a>
        <p class="lead">
          Instantly share code, notes, and snippets.
        </p>
      </div>
    </div>


  <div class="gisthead pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
    <div class="container">
        

<div class="container repohead-details-container">

  <ul class="pagehead-actions">


    <li>
        <a href="/login?return_to=https%3A%2F%2Fgist.github.com%2Fndarshanrestless%2F377848ecbbf5385e8ebcb8516ea7ac2c" aria-label="You must be signed in to star a gist" class="btn btn-sm btn-with-count tooltipped tooltipped-n" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
    Star
</a>
  <a href="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c/stargazers" class="social-count">
    0
</a>
    </li>

      <li>
          <a href="/login?return_to=https%3A%2F%2Fgist.github.com%2Fndarshanrestless%2F377848ecbbf5385e8ebcb8516ea7ac2c" aria-label="You must be signed in to fork a gist" class="btn btn-sm btn-with-count tooltipped tooltipped-n" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    Fork
</a>
  <a href="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c/forks" class="social-count">
    0
</a>
      </li>

  </ul>

  <h1 class="secret css-truncate">
    <img alt="@ndarshanrestless" class="avatar gist-avatar" height="26" src="https://avatars3.githubusercontent.com/u/14987395?v=3&amp;s=52" width="26" />
    <span class="author"><a href="/ndarshanrestless" class="url fn" rel="author"><span itemprop="author">ndarshanrestless</span></a></span><!--
        --><span class="path-divider">/</span><!--
        --><strong itemprop="name" class="gist-header-title css-truncate-target"><a href="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c">server.py</a></strong>
      <span class="label label-private v-align-middle">Secret</span>

    <div class="gist-timestamp">Created <time-ago datetime="2016-07-21T04:58:26Z">Jul 21, 2016</time-ago></div>
  </h1>
</div>

<div class="container gist-file-navigation">
  <div class="right file-navigation-options" data-multiple>

    <div class="file-navigation-option">
  <input type="hidden" name="protocol_type" value="clone">

  <div class="select-menu js-menu-container js-select-menu">
    <div class="input-group js-select-button js-zeroclipboard-container">
      <div class="input-group-button">
  <button type="button" class="btn btn-sm select-menu-button js-menu-target" data-ga-click="Repository, clone Embed, location:repo overview">
    Embed
  </button>
</div>
<input type="text" class="form-control input-monospace input-sm js-zeroclipboard-target js-url-field" value="&lt;script src=&quot;https://gist.github.com/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c.js&quot;&gt;&lt;/script&gt;" aria-label="Clone this repository at &lt;script src=&quot;https://gist.github.com/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c.js&quot;&gt;&lt;/script&gt;" readonly>
<div class="input-group-button">
  <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><svg aria-hidden="true" class="octicon octicon-clippy" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"></path></svg></button>
</div>

    </div>

    <div class="select-menu-modal-holder">
      <div class="select-menu-modal js-menu-content" aria-hidden="true">
        <div class="select-menu-header">
          <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
          <span class="select-menu-title">What would you like to do?</span>
        </div>

        <div class="select-menu-list js-navigation-container" role="menu">
            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <div class="select-menu-item-text">
                <input type="radio" name="protocol_selector" value="embed" checked>
                <span class="select-menu-item-heading">
                  
                  Embed
                </span>
                  <span class="description">
                    Embed this gist in your website.
                  </span>
                <span class="js-select-button-text hidden-select-button-text">
                  <div class="input-group-button">
  <button type="button" class="btn btn-sm select-menu-button js-menu-target" data-ga-click="Repository, clone Embed, location:repo overview">
    Embed
  </button>
</div>
<input type="text" class="form-control input-monospace input-sm js-zeroclipboard-target js-url-field" value="&lt;script src=&quot;https://gist.github.com/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c.js&quot;&gt;&lt;/script&gt;" aria-label="Clone this repository at &lt;script src=&quot;https://gist.github.com/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c.js&quot;&gt;&lt;/script&gt;" readonly>
<div class="input-group-button">
  <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><svg aria-hidden="true" class="octicon octicon-clippy" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"></path></svg></button>
</div>

                </span>
              </div>
            </div>
            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <div class="select-menu-item-text">
                <input type="radio" name="protocol_selector" value="share" >
                <span class="select-menu-item-heading">
                  
                  Share
                </span>
                  <span class="description">
                    Copy sharable URL for this gist.
                  </span>
                <span class="js-select-button-text hidden-select-button-text">
                  <div class="input-group-button">
  <button type="button" class="btn btn-sm select-menu-button js-menu-target" data-ga-click="Repository, clone Share, location:repo overview">
    Share
  </button>
</div>
<input type="text" class="form-control input-monospace input-sm js-zeroclipboard-target js-url-field" value="https://gist.github.com/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c" aria-label="Clone this repository at https://gist.github.com/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c" readonly>
<div class="input-group-button">
  <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><svg aria-hidden="true" class="octicon octicon-clippy" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"></path></svg></button>
</div>

                </span>
              </div>
            </div>
            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <div class="select-menu-item-text">
                <input type="radio" name="protocol_selector" value="http" >
                <span class="select-menu-item-heading">
                  Clone via
                  HTTPS
                </span>
                  <span class="description">
                    Clone with Git or checkout with SVN using the repository's web address.
                  </span>
                <span class="js-select-button-text hidden-select-button-text">
                  <div class="input-group-button">
  <button type="button" class="btn btn-sm select-menu-button js-menu-target" data-ga-click="Repository, clone HTTPS, location:repo overview">
    HTTPS
  </button>
</div>
<input type="text" class="form-control input-monospace input-sm js-zeroclipboard-target js-url-field" value="https://gist.github.com/377848ecbbf5385e8ebcb8516ea7ac2c.git" aria-label="Clone this repository at https://gist.github.com/377848ecbbf5385e8ebcb8516ea7ac2c.git" readonly>
<div class="input-group-button">
  <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><svg aria-hidden="true" class="octicon octicon-clippy" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M2 13h4v1H2v-1zm5-6H2v1h5V7zm2 3V8l-3 3 3 3v-2h5v-2H9zM4.5 9H2v1h2.5V9zM2 12h2.5v-1H2v1zm9 1h1v2c-.02.28-.11.52-.3.7-.19.18-.42.28-.7.3H1c-.55 0-1-.45-1-1V4c0-.55.45-1 1-1h3c0-1.11.89-2 2-2 1.11 0 2 .89 2 2h3c.55 0 1 .45 1 1v5h-1V6H1v9h10v-2zM2 5h8c0-.55-.45-1-1-1H8c-.55 0-1-.45-1-1s-.45-1-1-1-1 .45-1 1-.45 1-1 1H3c-.55 0-1 .45-1 1z"></path></svg></button>
</div>

                </span>
              </div>
            </div>
        </div>
        <div class="select-menu-list" role="menu">
          <a class="select-menu-item select-menu-action" href="https://help.github.com/articles/which-remote-url-should-i-use" target="_blank">
            <svg aria-hidden="true" class="octicon octicon-question select-menu-item-icon" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M6 10h2v2H6v-2zm4-3.5C10 8.64 8 9 8 9H6c0-.55.45-1 1-1h.5c.28 0 .5-.22.5-.5v-1c0-.28-.22-.5-.5-.5h-1c-.28 0-.5.22-.5.5V7H4c0-1.5 1.5-3 3-3s3 1 3 2.5zM7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7z"></path></svg>
            <div class="select-menu-item-text">
              Learn more about clone URLs
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
</div>


    <div class="file-navigation-option">
</div>


    <div class="file-navigation-option">
      <a href="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c/archive/1549459aab7edcff7b79dbee176f3d47c6b60e75.zip"
          class="btn btn-sm"
          rel="nofollow"
          data-ga-click="Gist, download zip, location:gist overview">
        Download ZIP
      </a>
    </div>
  </div>

  <div class="left">
    <nav class="reponav js-repo-nav js-sidenav-container-pjax"
     role="navigation"
     data-pjax="#gist-pjax-container">

  <a href="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c" aria-label="Code" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-pjax="true" data-selected-links="gist_code /ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c">
    <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
    Code
</a>
    <a href="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c/revisions" aria-label="Revisions" class="js-selected-navigation-item reponav-item" data-hotkey="g r" data-pjax="true" data-selected-links="gist_revisions /ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c/revisions">
      <svg aria-hidden="true" class="octicon octicon-git-commit" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
      Revisions
      <span class="counter">1</span>
</a>

</nav>

  </div>
</div>


    </div><!-- /.container -->
  </div><!-- /.repohead -->

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content gist-content">
    



<div>
  <div class="repository-meta js-details-container">
</div>


      <div class="js-gist-file-update-container js-task-list-container file-box">
  <div id="file-server-py" class="file">
      <div class="file-header">
        <div class="file-actions">

          <a href="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c/raw/1549459aab7edcff7b79dbee176f3d47c6b60e75/server.py" class="btn btn-sm ">Raw</a>
        </div>
        <div class="file-info">
          <span class="icon">
            <svg aria-hidden="true" class="octicon octicon-gist" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.5 5L10 7.5 7.5 10l-.75-.75L8.5 7.5 6.75 5.75 7.5 5zm-3 0L2 7.5 4.5 10l.75-.75L3.5 7.5l1.75-1.75L4.5 5zM0 13V2c0-.55.45-1 1-1h10c.55 0 1 .45 1 1v11c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1zm1 0h10V2H1v11z"></path></svg>
          </span>
          <a class="tooltipped tooltipped-s css-truncate" aria-label="Permalink" href="#file-server-py">
            <strong class="user-select-contain gist-blob-name css-truncate-target">
              server.py
            </strong>
          </a>
        </div>
      </div>
    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="file-server-py-L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="file-server-py-LC1" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="file-server-py-LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> flask <span class="pl-k">import</span> Flask, request, session, g, Response</td>
      </tr>
      <tr>
        <td id="file-server-py-L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="file-server-py-LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> flask.json <span class="pl-k">import</span> jsonify</td>
      </tr>
      <tr>
        <td id="file-server-py-L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="file-server-py-LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="file-server-py-L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="file-server-py-LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> jwt</td>
      </tr>
      <tr>
        <td id="file-server-py-L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="file-server-py-LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> logging</td>
      </tr>
      <tr>
        <td id="file-server-py-L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="file-server-py-LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> logging.handlers</td>
      </tr>
      <tr>
        <td id="file-server-py-L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="file-server-py-LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> functools <span class="pl-k">import</span> wraps</td>
      </tr>
      <tr>
        <td id="file-server-py-L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="file-server-py-LC9" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="file-server-py-LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># from passlib.hash import pbkdf2_sha256</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="file-server-py-LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># import hashlib, uuid</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="file-server-py-LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># from contextlib import closing</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="file-server-py-LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># import sqlite3</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="file-server-py-LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="file-server-py-LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> psycopg2</td>
      </tr>
      <tr>
        <td id="file-server-py-L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="file-server-py-LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> psycopg2.extensions <span class="pl-k">import</span> <span class="pl-c1">ISOLATION_LEVEL_AUTOCOMMIT</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="file-server-py-LC17" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="file-server-py-LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> random</td>
      </tr>
      <tr>
        <td id="file-server-py-L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="file-server-py-LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> ipdb</td>
      </tr>
      <tr>
        <td id="file-server-py-L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="file-server-py-LC20" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="file-server-py-LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> getnearby <span class="pl-k">import</span> db_get_nearby_bars</td>
      </tr>
      <tr>
        <td id="file-server-py-L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="file-server-py-LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> getonebar <span class="pl-k">import</span> db_get_one_bar_information</td>
      </tr>
      <tr>
        <td id="file-server-py-L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="file-server-py-LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> ratebar <span class="pl-k">import</span> insert_rating_into_bar</td>
      </tr>
      <tr>
        <td id="file-server-py-L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="file-server-py-LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> user <span class="pl-k">import</span> insert_user, insert_feedback</td>
      </tr>
      <tr>
        <td id="file-server-py-L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="file-server-py-LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> googlescraper <span class="pl-k">import</span> db_insert_google_bar</td>
      </tr>
      <tr>
        <td id="file-server-py-L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="file-server-py-LC26" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="file-server-py-LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Setup logging for better debugging</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="file-server-py-LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">MAX_LOG_FILE_SIZE</span> <span class="pl-k">=</span> <span class="pl-c1">512</span><span class="pl-k">*</span><span class="pl-c1">1024</span><span class="pl-k">*</span><span class="pl-c1">1024</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="file-server-py-LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">LOG_FILENAME</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/home/admin/work/barlogs/server-<span class="pl-c1">%s</span>.log<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (sys.argv[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="file-server-py-LC30" class="blob-code blob-code-inner js-file-line">log <span class="pl-k">=</span> logging.getLogger(<span class="pl-c1">__name__</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="file-server-py-LC31" class="blob-code blob-code-inner js-file-line">log.setLevel(logging.<span class="pl-c1">DEBUG</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="file-server-py-LC32" class="blob-code blob-code-inner js-file-line">handler <span class="pl-k">=</span> logging.handlers.RotatingFileHandler(</td>
      </tr>
      <tr>
        <td id="file-server-py-L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="file-server-py-LC33" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">LOG_FILENAME</span>, <span class="pl-v">maxBytes</span><span class="pl-k">=</span><span class="pl-c1">MAX_LOG_FILE_SIZE</span>, <span class="pl-v">backupCount</span><span class="pl-k">=</span><span class="pl-c1">5</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="file-server-py-LC34" class="blob-code blob-code-inner js-file-line">log.addHandler(handler)</td>
      </tr>
      <tr>
        <td id="file-server-py-L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="file-server-py-LC35" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="file-server-py-LC36" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="file-server-py-LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># salt = uuid.uuid4().hex</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="file-server-py-LC38" class="blob-code blob-code-inner js-file-line">secret <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>barhopper$$007$$<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="file-server-py-LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="file-server-py-LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># create our little application :)</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="file-server-py-LC41" class="blob-code blob-code-inner js-file-line">app <span class="pl-k">=</span> Flask(<span class="pl-c1">__name__</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="file-server-py-LC42" class="blob-code blob-code-inner js-file-line">app.config.update(<span class="pl-c1">dict</span>(</td>
      </tr>
      <tr>
        <td id="file-server-py-L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="file-server-py-LC43" class="blob-code blob-code-inner js-file-line">    <span class="pl-v">DATABASE</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>postgres<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="file-server-py-L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="file-server-py-LC44" class="blob-code blob-code-inner js-file-line">    <span class="pl-v">HOST</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>localhost<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="file-server-py-L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="file-server-py-LC45" class="blob-code blob-code-inner js-file-line">    <span class="pl-v">DEBUG</span><span class="pl-k">=</span><span class="pl-c1">False</span>,  <span class="pl-c"># True,</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="file-server-py-LC46" class="blob-code blob-code-inner js-file-line">    <span class="pl-v">SECRET_KEY</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>bar007<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="file-server-py-L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="file-server-py-LC47" class="blob-code blob-code-inner js-file-line">    <span class="pl-v">USERNAME</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>postgres<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="file-server-py-L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="file-server-py-LC48" class="blob-code blob-code-inner js-file-line">    <span class="pl-v">PASSWORD</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>bar<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="file-server-py-L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="file-server-py-LC49" class="blob-code blob-code-inner js-file-line">))</td>
      </tr>
      <tr>
        <td id="file-server-py-L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="file-server-py-LC50" class="blob-code blob-code-inner js-file-line">app.config.from_object(<span class="pl-c1">__name__</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="file-server-py-LC51" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="file-server-py-LC52" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="file-server-py-LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">status_400_on_exception</span>(<span class="pl-smi">f</span>):</td>
      </tr>
      <tr>
        <td id="file-server-py-L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="file-server-py-LC54" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Decorator for generating a 400 bad request response.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="file-server-py-LC55" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@wraps</span>(f)</td>
      </tr>
      <tr>
        <td id="file-server-py-L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="file-server-py-LC56" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_f</span>(<span class="pl-k">*</span><span class="pl-smi">args</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="file-server-py-L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="file-server-py-LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="file-server-py-LC58" class="blob-code blob-code-inner js-file-line">            retval <span class="pl-k">=</span> f(<span class="pl-k">*</span>args, <span class="pl-k">**</span>kwargs)</td>
      </tr>
      <tr>
        <td id="file-server-py-L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="file-server-py-LC59" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">Exception</span> <span class="pl-k">as</span> e:</td>
      </tr>
      <tr>
        <td id="file-server-py-L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="file-server-py-LC60" class="blob-code blob-code-inner js-file-line">            log.exception(<span class="pl-s"><span class="pl-pds">&#39;</span>exception in <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(f.<span class="pl-c1">__name__</span>))</td>
      </tr>
      <tr>
        <td id="file-server-py-L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="file-server-py-LC61" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> app.debug:</td>
      </tr>
      <tr>
        <td id="file-server-py-L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="file-server-py-LC62" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">with</span> closing(StringIO()) <span class="pl-k">as</span> s:</td>
      </tr>
      <tr>
        <td id="file-server-py-L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="file-server-py-LC63" class="blob-code blob-code-inner js-file-line">                    traceback.print_exception(<span class="pl-k">*</span>sys.exc_info(), <span class="pl-v">file</span><span class="pl-k">=</span>s)</td>
      </tr>
      <tr>
        <td id="file-server-py-L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="file-server-py-LC64" class="blob-code blob-code-inner js-file-line">                    response <span class="pl-k">=</span> s.getvalue()</td>
      </tr>
      <tr>
        <td id="file-server-py-L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="file-server-py-LC65" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="file-server-py-LC66" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> <span class="pl-c1">repr</span>(e)</td>
      </tr>
      <tr>
        <td id="file-server-py-L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="file-server-py-LC67" class="blob-code blob-code-inner js-file-line">            resp <span class="pl-k">=</span> jsonify(<span class="pl-v">response</span><span class="pl-k">=</span>response, <span class="pl-v">status</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">&#39;</span>success<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">False</span>})</td>
      </tr>
      <tr>
        <td id="file-server-py-L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="file-server-py-LC68" class="blob-code blob-code-inner js-file-line">            resp.status_code <span class="pl-k">=</span> <span class="pl-c1">400</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="file-server-py-LC69" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> resp</td>
      </tr>
      <tr>
        <td id="file-server-py-L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="file-server-py-LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="file-server-py-LC71" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> retval</td>
      </tr>
      <tr>
        <td id="file-server-py-L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="file-server-py-LC72" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> _f</td>
      </tr>
      <tr>
        <td id="file-server-py-L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="file-server-py-LC73" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="file-server-py-LC74" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="file-server-py-LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">connect_db</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="file-server-py-LC76" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="file-server-py-LC77" class="blob-code blob-code-inner js-file-line">        conn <span class="pl-k">=</span> psycopg2.connect(</td>
      </tr>
      <tr>
        <td id="file-server-py-L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="file-server-py-LC78" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>dbname=&#39;postgres&#39; user=&#39;postgres&#39;<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="file-server-py-LC79" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>host=&#39;localhost&#39; password=&#39;bar&#39;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="file-server-py-LC80" class="blob-code blob-code-inner js-file-line">        conn.set_isolation_level(<span class="pl-c1">ISOLATION_LEVEL_AUTOCOMMIT</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="file-server-py-LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="file-server-py-LC82" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Unable to connect to PG database<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="file-server-py-LC83" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> conn</td>
      </tr>
      <tr>
        <td id="file-server-py-L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="file-server-py-LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="file-server-py-LC85" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="file-server-py-LC86" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_db</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="file-server-py-LC87" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="file-server-py-LC88" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Opens a new database connection</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="file-server-py-LC89" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    if there is none yet for the</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="file-server-py-LC90" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    current application context.</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="file-server-py-LC91" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="file-server-py-LC92" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(g, <span class="pl-s"><span class="pl-pds">&#39;</span>postgres_db<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="file-server-py-L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="file-server-py-LC93" class="blob-code blob-code-inner js-file-line">        g.postgres_db <span class="pl-k">=</span> connect_db()</td>
      </tr>
      <tr>
        <td id="file-server-py-L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="file-server-py-LC94" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="file-server-py-LC95" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> g.postgres_db</td>
      </tr>
      <tr>
        <td id="file-server-py-L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="file-server-py-LC96" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="file-server-py-LC97" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="file-server-py-LC98" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.before_request</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="file-server-py-LC99" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">before_request</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="file-server-py-LC100" class="blob-code blob-code-inner js-file-line">    g.postgres_db <span class="pl-k">=</span> connect_db()</td>
      </tr>
      <tr>
        <td id="file-server-py-L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="file-server-py-LC101" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="file-server-py-LC102" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="file-server-py-LC103" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.teardown_request</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="file-server-py-LC104" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">teardown_request</span>(<span class="pl-smi">exception</span>):</td>
      </tr>
      <tr>
        <td id="file-server-py-L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="file-server-py-LC105" class="blob-code blob-code-inner js-file-line">    db <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(g, <span class="pl-s"><span class="pl-pds">&#39;</span>postgres_db<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="file-server-py-LC106" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> db <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="file-server-py-LC107" class="blob-code blob-code-inner js-file-line">        db.close()</td>
      </tr>
      <tr>
        <td id="file-server-py-L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="file-server-py-LC108" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="file-server-py-LC109" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="file-server-py-LC110" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.route</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="file-server-py-LC111" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">index</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="file-server-py-LC112" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> Response(<span class="pl-s"><span class="pl-pds">&quot;</span>What are you looking at?<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">200</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="file-server-py-LC113" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="file-server-py-LC114" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="file-server-py-LC115" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">tokenCreate</span>(<span class="pl-smi">username</span>, <span class="pl-smi">deviceid</span>):</td>
      </tr>
      <tr>
        <td id="file-server-py-L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="file-server-py-LC116" class="blob-code blob-code-inner js-file-line">    token <span class="pl-k">=</span> jwt.encode({<span class="pl-s"><span class="pl-pds">&#39;</span>username<span class="pl-pds">&#39;</span></span>: username, <span class="pl-s"><span class="pl-pds">&#39;</span>deviceid<span class="pl-pds">&#39;</span></span>: deviceid},</td>
      </tr>
      <tr>
        <td id="file-server-py-L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="file-server-py-LC117" class="blob-code blob-code-inner js-file-line">                       secret, <span class="pl-v">algorithm</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>HS256<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="file-server-py-LC118" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> token</td>
      </tr>
      <tr>
        <td id="file-server-py-L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="file-server-py-LC119" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="file-server-py-LC120" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="file-server-py-LC121" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">tokenGetPayload</span>(<span class="pl-smi">token</span>):</td>
      </tr>
      <tr>
        <td id="file-server-py-L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="file-server-py-LC122" class="blob-code blob-code-inner js-file-line">    jret <span class="pl-k">=</span> jwt.decode(token, secret, <span class="pl-v">algorithms</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>HS256<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="file-server-py-LC123" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> jret</td>
      </tr>
      <tr>
        <td id="file-server-py-L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="file-server-py-LC124" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="file-server-py-LC125" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="file-server-py-LC126" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.route</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>/scrape<span class="pl-pds">&#39;</span></span>, <span class="pl-v">methods</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="file-server-py-LC127" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@status_400_on_exception</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="file-server-py-LC128" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">scrape_bar</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="file-server-py-LC129" class="blob-code blob-code-inner js-file-line">    jd <span class="pl-k">=</span> request.get_json()</td>
      </tr>
      <tr>
        <td id="file-server-py-L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="file-server-py-LC130" class="blob-code blob-code-inner js-file-line">    location <span class="pl-k">=</span> jd.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>location<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="file-server-py-LC131" class="blob-code blob-code-inner js-file-line">    radius <span class="pl-k">=</span> <span class="pl-c1">int</span>(jd.get(<span class="pl-s"><span class="pl-pds">&#39;</span>radius<span class="pl-pds">&#39;</span></span>)) <span class="pl-k">*</span> <span class="pl-c1">1610</span>  <span class="pl-c"># to meters</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="file-server-py-LC132" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">type</span> <span class="pl-k">=</span> jd.get(<span class="pl-s"><span class="pl-pds">&#39;</span>type<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>bar<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="file-server-py-LC133" class="blob-code blob-code-inner js-file-line">    totalrows, total_google_requests \</td>
      </tr>
      <tr>
        <td id="file-server-py-L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="file-server-py-LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">=</span> db_insert_google_bar(location, radius, get_db(), <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-c1">type</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="file-server-py-LC135" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> jsonify(<span class="pl-v">result</span><span class="pl-k">=</span>(totalrows, total_google_requests))</td>
      </tr>
      <tr>
        <td id="file-server-py-L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="file-server-py-LC136" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="file-server-py-LC137" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-server-py-L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="file-server-py-LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># eg: POST ratebar?device_id=007&amp;</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="file-server-py-LC139" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># bar_id=554ca521944c028e4da1b7e75623c9acaf9297a1</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="file-server-py-LC140" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.route</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>/ratebar<span class="pl-pds">&#39;</span></span>, <span class="pl-v">methods</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="file-server-py-LC141" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@status_400_on_exception</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="file-server-py-LC142" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">rate_bar</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="file-server-py-LC143" class="blob-code blob-code-inner js-file-line">    jd <span class="pl-k">=</span> request.get_json()</td>
      </tr>
      <tr>
        <td id="file-server-py-L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="file-server-py-LC144" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="file-server-py-LC145" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Assert all the rating fields exsits in request</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="file-server-py-LC146" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> jd <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>body cannot be empty &amp; needs mandatory fields<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="file-server-py-LC147" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>bar_id<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> jd, <span class="pl-s"><span class="pl-pds">&quot;</span>bar_id needs to be provided<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="file-server-py-LC148" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>delta_time<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> jd, <span class="pl-s"><span class="pl-pds">&quot;</span>delta_time mandatory parameter<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="file-server-py-LC149" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="file-server-py-LC150" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># todo: remove the fake random insert when naren start sendig device_id</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="file-server-py-LC151" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># assert &#39;device_id&#39; in jd, &quot;device_id needs to be provided&quot;</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="file-server-py-LC152" class="blob-code blob-code-inner js-file-line">    jd[<span class="pl-s"><span class="pl-pds">&#39;</span>device_id<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> random.randint(<span class="pl-c1">1</span>, <span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="file-server-py-LC153" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="file-server-py-LC154" class="blob-code blob-code-inner js-file-line">    bar_id <span class="pl-k">=</span> jd[<span class="pl-s"><span class="pl-pds">&#39;</span>bar_id<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="file-server-py-L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="file-server-py-LC155" class="blob-code blob-code-inner js-file-line">    jd.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>bar_id<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="file-server-py-LC156" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="file-server-py-LC157" class="blob-code blob-code-inner js-file-line">    delta_time <span class="pl-k">=</span> <span class="pl-c1">int</span>(jd.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>delta_time<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="file-server-py-L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="file-server-py-LC158" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-server-py-L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="file-server-py-LC159" class="blob-code blob-code-inner js-file-line">    rating_fields <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>ambience_rating<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>women_quality_rating<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="file-server-py-L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="file-server-py-LC160" class="blob-code blob-code-inner js-file-line">                     <span class="pl-s"><span class="pl-pds">&#39;</span>men_quality_rating<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>drink_rating<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="file-server-py-L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="file-server-py-LC161" class="blob-code blob-code-inner js-file-line">                     <span class="pl-s"><span class="pl-pds">&#39;</span>hospitality_rating<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>average_age<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="file-server-py-LC162" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-server-py-L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="file-server-py-LC163" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-c1">all</span>(keys <span class="pl-k">in</span> jd <span class="pl-k">for</span> keys <span class="pl-k">in</span> rating_fields),\</td>
      </tr>
      <tr>
        <td id="file-server-py-L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="file-server-py-LC164" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;</span>missing one of field <span class="pl-c1">{}</span><span class="pl-pds">&quot;</span></span>.format(rating_fields)</td>
      </tr>
      <tr>
        <td id="file-server-py-L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="file-server-py-LC165" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="file-server-py-LC166" class="blob-code blob-code-inner js-file-line">    jd <span class="pl-k">=</span> {k: <span class="pl-c1">int</span>(v) <span class="pl-k">for</span> k, v <span class="pl-k">in</span> jd.iteritems()}</td>
      </tr>
      <tr>
        <td id="file-server-py-L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="file-server-py-LC167" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="file-server-py-LC168" class="blob-code blob-code-inner js-file-line">    jd[<span class="pl-s"><span class="pl-pds">&#39;</span>bar_id<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> bar_id</td>
      </tr>
      <tr>
        <td id="file-server-py-L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="file-server-py-LC169" class="blob-code blob-code-inner js-file-line">    device_id <span class="pl-k">=</span> jd[<span class="pl-s"><span class="pl-pds">&#39;</span>device_id<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="file-server-py-L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="file-server-py-LC170" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="file-server-py-LC171" class="blob-code blob-code-inner js-file-line">    db <span class="pl-k">=</span> get_db()</td>
      </tr>
      <tr>
        <td id="file-server-py-L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="file-server-py-LC172" class="blob-code blob-code-inner js-file-line">    insert_user(device_id, db)  <span class="pl-c"># ??? what is this for todo</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="file-server-py-LC173" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># do the real calculation on post and insert into DB</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="file-server-py-LC174" class="blob-code blob-code-inner js-file-line">    inserted_rowid <span class="pl-k">=</span> insert_rating_into_bar(jd, device_id,</td>
      </tr>
      <tr>
        <td id="file-server-py-L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="file-server-py-LC175" class="blob-code blob-code-inner js-file-line">                                                bar_id, delta_time, db)</td>
      </tr>
      <tr>
        <td id="file-server-py-L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="file-server-py-LC176" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> jsonify(<span class="pl-v">result</span><span class="pl-k">=</span>inserted_rowid)</td>
      </tr>
      <tr>
        <td id="file-server-py-L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="file-server-py-LC177" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-server-py-L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="file-server-py-LC178" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.route</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>/feedback<span class="pl-pds">&#39;</span></span>, <span class="pl-v">methods</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="file-server-py-LC179" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@status_400_on_exception</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="file-server-py-LC180" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">feedback</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="file-server-py-LC181" class="blob-code blob-code-inner js-file-line">    jd <span class="pl-k">=</span> request.get_json()</td>
      </tr>
      <tr>
        <td id="file-server-py-L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="file-server-py-LC182" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-server-py-L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="file-server-py-LC183" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Assert all the rating fields exsits in request</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="file-server-py-LC184" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> jd <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>body cannot be empty &amp; needs mandatory fields<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="file-server-py-LC185" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>feedback_text<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> jd,\</td>
      </tr>
      <tr>
        <td id="file-server-py-L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="file-server-py-LC186" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;</span>feedback_text manatatory and cannot be empty<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="file-server-py-LC187" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>device_id<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> jd, <span class="pl-s"><span class="pl-pds">&quot;</span>device_id is mandatory field<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="file-server-py-LC188" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="file-server-py-LC189" class="blob-code blob-code-inner js-file-line">    device_id <span class="pl-k">=</span> jd.get(<span class="pl-s"><span class="pl-pds">&#39;</span>device_id<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="file-server-py-LC190" class="blob-code blob-code-inner js-file-line">    feedback_text <span class="pl-k">=</span> jd.get(<span class="pl-s"><span class="pl-pds">&#39;</span>feedback_text<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="file-server-py-LC191" class="blob-code blob-code-inner js-file-line">    user_name <span class="pl-k">=</span> jd.get(<span class="pl-s"><span class="pl-pds">&#39;</span>user_name<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>anonmyous<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="file-server-py-LC192" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-server-py-L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="file-server-py-LC193" class="blob-code blob-code-inner js-file-line">    insert_feedback(get_db(), device_id,</td>
      </tr>
      <tr>
        <td id="file-server-py-L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="file-server-py-LC194" class="blob-code blob-code-inner js-file-line">                        feedback_text, user_name)</td>
      </tr>
      <tr>
        <td id="file-server-py-L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="file-server-py-LC195" class="blob-code blob-code-inner js-file-line">    resp <span class="pl-k">=</span> jsonify(<span class="pl-c1">dict</span>({<span class="pl-s"><span class="pl-pds">&#39;</span>success<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">True</span>}))</td>
      </tr>
      <tr>
        <td id="file-server-py-L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="file-server-py-LC196" class="blob-code blob-code-inner js-file-line">    resp.status_code <span class="pl-k">=</span> <span class="pl-c1">200</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="file-server-py-LC197" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> resp</td>
      </tr>
      <tr>
        <td id="file-server-py-L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="file-server-py-LC198" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="file-server-py-LC199" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="file-server-py-LC200" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.route</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>/logout<span class="pl-pds">&#39;</span></span>, <span class="pl-v">methods</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>POST<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="file-server-py-LC201" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">logout</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="file-server-py-LC202" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># remove the username from the session if it&#39;s there</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="file-server-py-LC203" class="blob-code blob-code-inner js-file-line">    session_value <span class="pl-k">=</span> session.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>username<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="file-server-py-LC204" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> session_value:</td>
      </tr>
      <tr>
        <td id="file-server-py-L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="file-server-py-LC205" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> Response(<span class="pl-s"><span class="pl-pds">&quot;</span>Successfully logged out user username:<span class="pl-c1">{}</span><span class="pl-pds">&quot;</span></span>.</td>
      </tr>
      <tr>
        <td id="file-server-py-L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="file-server-py-LC206" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">format</span>(session_value), <span class="pl-c1">200</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="file-server-py-LC207" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="file-server-py-LC208" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> Response(<span class="pl-s"><span class="pl-pds">&quot;</span>Hey, you had never logged in actually! :<span class="pl-c1">{}</span><span class="pl-pds">&quot;</span></span>.</td>
      </tr>
      <tr>
        <td id="file-server-py-L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="file-server-py-LC209" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">format</span>(session_value), <span class="pl-c1">200</span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="file-server-py-LC210" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="file-server-py-LC211" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="file-server-py-LC212" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.route</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>/getnearbybars/<span class="pl-pds">&#39;</span></span>, <span class="pl-v">methods</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>GET<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="file-server-py-LC213" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@status_400_on_exception</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="file-server-py-LC214" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_nearby_bars</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="file-server-py-LC215" class="blob-code blob-code-inner js-file-line">    dic <span class="pl-k">=</span> request.args.to_dict()</td>
      </tr>
      <tr>
        <td id="file-server-py-L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="file-server-py-LC216" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="file-server-py-LC217" class="blob-code blob-code-inner js-file-line">    location <span class="pl-k">=</span> dic.get(<span class="pl-s"><span class="pl-pds">&#39;</span>location<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="file-server-py-LC218" class="blob-code blob-code-inner js-file-line">    radius <span class="pl-k">=</span> <span class="pl-c1">int</span>(dic.get(<span class="pl-s"><span class="pl-pds">&#39;</span>radius<span class="pl-pds">&#39;</span></span>)) <span class="pl-k">*</span> <span class="pl-c1">1610</span>  <span class="pl-c"># to meters</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="file-server-py-LC219" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="file-server-py-LC220" class="blob-code blob-code-inner js-file-line">    db <span class="pl-k">=</span> get_db()</td>
      </tr>
      <tr>
        <td id="file-server-py-L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="file-server-py-LC221" class="blob-code blob-code-inner js-file-line">    dic <span class="pl-k">=</span> request.args.to_dict()</td>
      </tr>
      <tr>
        <td id="file-server-py-L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="file-server-py-LC222" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>open_now<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> dic, <span class="pl-s"><span class="pl-pds">&quot;</span>open_now mandatory parameter<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="file-server-py-LC223" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>delta_time<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> dic, <span class="pl-s"><span class="pl-pds">&quot;</span>delta_time mandatory parameter<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="file-server-py-LC224" class="blob-code blob-code-inner js-file-line">    open_now_filter <span class="pl-k">=</span> <span class="pl-c1">bool</span>(<span class="pl-c1">int</span>(dic.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>open_now<span class="pl-pds">&#39;</span></span>)))</td>
      </tr>
      <tr>
        <td id="file-server-py-L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="file-server-py-LC225" class="blob-code blob-code-inner js-file-line">    result <span class="pl-k">=</span> db_get_nearby_bars(location, radius, db, open_now_filter,</td>
      </tr>
      <tr>
        <td id="file-server-py-L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="file-server-py-LC226" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-v">args</span><span class="pl-k">=</span>dic)</td>
      </tr>
      <tr>
        <td id="file-server-py-L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="file-server-py-LC227" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> jsonify(<span class="pl-v">result</span><span class="pl-k">=</span>result)</td>
      </tr>
      <tr>
        <td id="file-server-py-L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="file-server-py-LC228" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="file-server-py-LC229" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="file-server-py-LC230" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@app.route</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>/getonebar/<span class="pl-pds">&#39;</span></span>, <span class="pl-v">methods</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>GET<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="file-server-py-LC231" class="blob-code blob-code-inner js-file-line"><span class="pl-en">@status_400_on_exception</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="file-server-py-LC232" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_one_bar</span>():</td>
      </tr>
      <tr>
        <td id="file-server-py-L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="file-server-py-LC233" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>bar_id<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> request.args, <span class="pl-s"><span class="pl-pds">&#39;</span>bar_id mandatory parameter<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="file-server-py-LC234" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">assert</span> <span class="pl-s"><span class="pl-pds">&#39;</span>delta_time<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> request.args, <span class="pl-s"><span class="pl-pds">&#39;</span>delta_time mandatory parameter<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="file-server-py-L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="file-server-py-LC235" class="blob-code blob-code-inner js-file-line">    bar_id <span class="pl-k">=</span> request.args.get(<span class="pl-s"><span class="pl-pds">&#39;</span>bar_id<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="file-server-py-L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="file-server-py-LC236" class="blob-code blob-code-inner js-file-line">    delta_time <span class="pl-k">=</span> <span class="pl-c1">int</span>(request.args.get(<span class="pl-s"><span class="pl-pds">&#39;</span>delta_time<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="file-server-py-L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="file-server-py-LC237" class="blob-code blob-code-inner js-file-line">    db <span class="pl-k">=</span> get_db()</td>
      </tr>
      <tr>
        <td id="file-server-py-L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="file-server-py-LC238" class="blob-code blob-code-inner js-file-line">    rj <span class="pl-k">=</span> db_get_one_bar_information(bar_id, delta_time, db)</td>
      </tr>
      <tr>
        <td id="file-server-py-L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="file-server-py-LC239" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> jsonify(<span class="pl-v">result</span><span class="pl-k">=</span>rj)</td>
      </tr>
      <tr>
        <td id="file-server-py-L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="file-server-py-LC240" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="file-server-py-L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="file-server-py-LC241" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="file-server-py-L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="file-server-py-LC242" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="file-server-py-LC243" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(sys.argv) <span class="pl-k">&gt;=</span> <span class="pl-c1">2</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="file-server-py-LC244" class="blob-code blob-code-inner js-file-line">        port <span class="pl-k">=</span> <span class="pl-c1">int</span>(sys.argv[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="file-server-py-L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="file-server-py-LC245" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="file-server-py-L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="file-server-py-LC246" class="blob-code blob-code-inner js-file-line">        port <span class="pl-k">=</span> <span class="pl-c1">4000</span></td>
      </tr>
      <tr>
        <td id="file-server-py-L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="file-server-py-LC247" class="blob-code blob-code-inner js-file-line">    app.run(<span class="pl-v">host</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>0.0.0.0<span class="pl-pds">&#39;</span></span>, <span class="pl-v">port</span><span class="pl-k">=</span>port)</td>
      </tr>
      <tr>
        <td id="file-server-py-L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="file-server-py-LC248" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
</table>

  </div>

  </div>
  
</div>


  <a name="comments"></a>
  <div class="discussion-timeline gist-discussion-timeline js-quote-selection-container ">
    <div class="js-discussion js-socket-channel" data-channel="tenant:1:marked-as-read:gist:38025701">
      




<!-- Rendered timeline since 2016-07-20 21:58:26 -->
<div id="partial-timeline-marker"
      class="js-timeline-marker js-updatable-content"
      data-url="/ndarshanrestless/377848ecbbf5385e8ebcb8516ea7ac2c/show_partial?partial=gist%2Ftimeline_marker&amp;since=1469077106"
      data-last-modified="Thu, 21 Jul 2016 04:58:26 GMT"
      >
</div>


      <div class="discussion-timeline-actions">
          <div class="signed-out-comment">
    <a href="/join?source=comment-gist" class="btn btn-primary" rel="nofollow">Sign up for free</a>
    <strong>to join this conversation on GitHub</strong>.
    Already have an account?
    <a href="/login?return_to=https%3A%2F%2Fgist.github.com%2Fndarshanrestless%2F377848ecbbf5385e8ebcb8516ea7ac2c" rel="nofollow">Sign in to comment</a>
</div>

      </div>
    </div>
  </div>
</div>
  </div>

  <div class="modal-backdrop js-touch-events"></div>
</div><!-- /.container -->

    </div><!-- /.gist-pjax-container -->
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.03858s from github-fe153-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-7db58f8b7b91111107fac755dd8b178fe7db0f209ced51fc339c446ad3f8da2b.js"></script>
      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-404cdd1add1f710db016a02e5e31fff8a9089d14ff0c227df862b780886db7d5.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-bda6c8f3d777243f9192f7725d680673aa13394eaeee5081e53f00e42e950028.js"></script>
      
      
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>

