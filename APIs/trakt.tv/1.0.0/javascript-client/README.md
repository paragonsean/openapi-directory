# trakt_api

TraktApi - JavaScript client for trakt_api
At Trakt, we collect lots of interesting information about what tv shows and movies everyone is watching. Part of the fun with such data is making it available for anyone to mash up and use on their own site or app. The Trakt API was made just for this purpose. It is very easy to use, you basically call a URL and get some JSON back.

More complex API calls (such as adding a movie or show to your collection) involve sending us data. These are still easy to use, you simply POST some JSON data to a specific URL.

Make sure to check out the [**Required Headers**](#introduction/required-headers) and [**Authentication**](#reference/authentication-oauth) sections for more info on what needs to be sent with each API call. Also check out the [**Terminology**](#introduction/terminology) section insight into the features Trakt supports.

# Create an App

To use the Trakt API, you'll need to [**create a new API app**](https://trakt.tv/oauth/applications/new).

# Stay Connected

API discussion and bugs should be posted in the [**GitHub Developer Forum**](https://github.com/trakt/api-help/issues) and *watch* the repository if you'd like to get notifications. Make sure to follow our [**API Blog**](https://apiblog.trakt.tv) and [**@traktapi on Twitter**](https://twitter.com/traktapi) too.

# API URL

The API should always be accessed over SSL.

```
https://api.trakt.tv
```

If you would like to use our sandbox environment to not fill production with test data, use this URL over SSL. **Note:** Staging is a completely separate environment, so you'll need to [**create a new API app on staging**](https://staging.trakt.tv/oauth/applications/new).

```
https://api-staging.trakt.tv
```

# Verbs

The API uses restful verbs.

| Verb | Description |
|---|---|
| `GET` | Select one or more items. Success returns `200` status code. |
| `POST` | Create a new item. Success returns `201` status code. |
| `PUT` | Update an item. Success returns `200` status code. |
| `DELETE` | Delete an item. Success returns `200` or `204` status code. |

# Status Codes

The API will respond with one of the following HTTP status codes.

| Code | Description |
|---|---|
| `200` | Success
| `201` | Success - *new resource created (POST)*
| `204` | Success - *no content to return (DELETE)*
| `400` | Bad Request - *request couldn't be parsed*
| `401` | Unauthorized - *OAuth must be provided*
| `403` | Forbidden - *invalid API key or unapproved app*
| `404` | Not Found - *method exists, but no record found*
| `405` | Method Not Found - *method doesn't exist*
| `409` | Conflict - *resource already created*
| `412` | Precondition Failed - *use application/json content type*
| `420` | Account Limit Exceeded - *list count, item count, etc*
| `422` | Unprocessable Entity - *validation errors*
| `423` | Locked User Account - *have the user contact support*
| `426` | VIP Only - *user must upgrade to VIP*
| `429` | Rate Limit Exceeded
| `500` | Server Error - *please open a support ticket*
| `502` | Service Unavailable - *server overloaded (try again in 30s)*
| `503` | Service Unavailable - *server overloaded (try again in 30s)*
| `504` | Service Unavailable - *server overloaded (try again in 30s)*
| `520` | Service Unavailable - *Cloudflare error*
| `521` | Service Unavailable - *Cloudflare error*
| `522` | Service Unavailable - *Cloudflare error*

# Required Headers

You'll need to send some headers when making API calls to identify your application, set the version and set the content type to JSON.

| Header | Value |
|---|---|
| `Content-type` <span style=\"color:red;\">*</a> | `application/json` |
| `trakt-api-key` <span style=\"color:red;\">*</a> | Your `client_id` listed under your Trakt applications. |
| `trakt-api-version` <span style=\"color:red;\">*</a> | `2` | API version to use.

All `POST`, `PUT`, and `DELETE` methods require a valid OAuth `access_token`. Some `GET` calls require OAuth and others will return user specific data if OAuth is sent. Methods that &#128274; **require** or have &#128275; **optional** OAuth will be indicated.

Your OAuth library should take care of sending the auth headers for you, but for reference here's how the Bearer token should be sent.

| Header | Value |
|---|---|
| `Authorization` | `Bearer [access_token]` |

# Rate Limiting

All API methods are rate limited. A `429` HTTP status code is returned when the limit has been exceeded. Check the headers for detailed info, then try your API call in `Retry-After` seconds.

| Header | Value |
|---|---|
| `X-Ratelimit` | `{\"name\":\"UNAUTHED_API_GET_LIMIT\",\"period\":300,\"limit\":1000,\"remaining\":0,\"until\":\"2020-10-10T00:24:00Z\"}` |
| `Retry-After` | `10` |

Here are the current limits. There are separate limits for authed (user level) and unauthed (application level) calls. We'll continue to adjust these limits to optimize API performance for everyone. The goal is to prevent API abuse and poor coding, but allow users to use apps normally.

| Name | Verb | Methods | Limit |
|---|---|---|---|
| `AUTHED_API_POST_LIMIT` | `POST`, `PUT`, `DELETE` | all | 1 call per second |
| `AUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes |
| `UNAUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes |

# Locked User Account

A `423` HTTP status code is returned when the OAuth user has a locked user account. Please instruct the user to [**contact Trakt support**](https://support.trakt.tv) so we can fix their account. API access will be suspended for the user until we fix their account.

# VIP Methods

Some API methods are tagged 🔥 **VIP Only**. A `426` HTTP status code is returned when the user isn't a VIP, indicating they need to sign up for [**Trakt VIP**](https://trakt.tv/vip) in order to use this method. In your app, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP.

| Header | Value |
|---|---|
| `X-Upgrade-URL` | `https://trakt.tv/vip` |

Some API methods are tagged 🔥 **VIP Enhanced**. A `420` HTTP status code is returned when the user has exceeded their account limit. Signing up for [**Trakt VIP**](https://trakt.tv/vip) will increase these limits. If the user isn't a VIP, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP. If they are already VIP and still exceeded the limit, please display a message indicating this.

| Header | Value |
|---|---|
| `X-Upgrade-URL` | `https://trakt.tv/vip` |
| `X-VIP-User` | `true` or `false` |
| `X-Account-Limit` | Limit allowed. |

# Pagination

Some methods are paginated. Methods with &#128196; **Pagination** will load 1 page of 10 items by default. Methods with &#128196; **Pagination Optional** will load all items by default. In either case, append a query string like `?page={page}&limit={limit}` to the URL to influence the results.

| Parameter | Type | Default | Value |
|---|---|---|---|
| `page` | integer | `1` | Number of page of results to be returned. |
| `limit` | integer | `10` | Number of results to return per page. |

All paginated methods will return these HTTP headers.

| Header | Value |
|---|---|
| `X-Pagination-Page` | Current page. |
| `X-Pagination-Limit` | Items per page. |
| `X-Pagination-Page-Count` | Total number of pages. |
| `X-Pagination-Item-Count` | Total number of items. |

# Extended Info

By default, all methods will return minimal info for movies, shows, episodes, people, and users. Minimal info is typically all you need to match locally cached items and includes the `title`, `year`, and `ids`. However, you can request different extended levels of information by adding `?extended={level}` to the URL. Send a comma separated string to get multiple types of extended info.

**Note:** This returns a lot of extra data, so please only use extended parameters if you actually need them!

| Level | Description |
|---|---|
| `full` | Complete info for an item.
| `metadata` | **Collection only.** Additional video and audio info.

# Filters

Some `movies`, `shows`, `calendars`,  and `search` methods support additional filters and will be tagged with &#127898; **Filters**. Applying these filters refines the results and helps your users to more easily discover new items.

Add a query string (i.e. `?years=2016&genres=action`) with any filters you want to use. Some filters allow multiples which can be sent as comma delimited parameters. For example, `?genres=action,adventure` would match the `action` OR `adventure` genre.

**Note:** Make sure to properly URL encode the parameters including spaces and special characters.

#### Common Filters

| Parameter | Multiples | Example | Value |
|---|---|---|---|
| `query` | | `batman` | Search titles and descriptions. |
| `years` | | `2016` | 4 digit year or range of years. |
| `genres` | &#10003; | `action` | [Genre slugs.](#reference/genres) |
| `languages` | &#10003; | `en` | [2 character language code.](#reference/languages) |
| `countries` | &#10003; | `us` | [2 character country code.](#reference/countries) |
| `runtimes` | | `30-90` | Range in minutes. |
| `studios` | &#10003; | `marvel-studios` | Studio slugs. |

#### Rating Filters

Trakt, TMDB, and IMDB ratings apply to `movies`, `shows`, and `episodes`. Rotten Tomatoes and Metacritic apply to `movies`.

| Parameter | Multiples | Example | Value |
|---|---|---|---|
| `ratings` | | `75-100` | Trakt rating range between `0` and `100`. |
| `votes` | | `5000-10000` | Trakt vote count between `0` and `100000`. |
| `tmdb_ratings` | | `5.5-10.0` | TMDB rating range between `0.0` and `10.0`. |
| `tmdb_votes` | | `5000-10000` | TMDB vote count between `0` and `100000`. |
| `imdb_ratings` | | `5.5-10.0` | IMDB rating range between `0.0` and `10.0`. |
| `imdb_votes` | | `5000-10000` | IMDB vote count between `0` and `3000000`. |
| `rt_meters` | | `5.5-10.0` | Rotten Tomatoes meter range between `0` and `100`. |
| `metascores` | | `5.5-10.0` | Metacritic score range between `0` and `100`. |

#### Movie Filters

| Parameter | Multiples | Example | Value |
|---|---|---|---|
| `certifications` | &#10003; | `pg-13` | US content certification. |

#### Show Filters

| Parameter | Multiples | Example | Value |
|---|---|---|---|
| `certifications` | &#10003; | `tv-pg` | US content certification. |
| `networks` | &#10003; | `HBO` | Network name. |
| `status` | &#10003; | `ended` | Set to `returning series`, `continuing`, `in production`, `planned`, `upcoming`,  `pilot`, `canceled`, or `ended`. |

# CORS

When creating your API app, specify the JavaScript (CORS) origins you'll be using. We use these origins to return the headers needed for CORS.

# Dates

All dates will be GMT and returned in the ISO 8601 format like `2014-09-01T09:10:11.000Z`. Adjust accordingly in your app for the user's local timezone.

# Emojis

We use short codes for emojis like `:smiley:` and `:raised_hands:` and render them on the Trakt website using [**JoyPixels**](https://www.joypixels.com/) _(verion 6.6.0)_. Methods that support emojis are tagged with &#128513; **Emojis**. For POST methods, you can send standard unicode emojis and we'll automatically convert them to short codes. For GET methods, we'll return the short codes and it's up to your app to convert them back to unicode emojis.

# Standard Media Objects

All methods will accept or return standard media objects for `movie`, `show`, `season`, `episode`, `person`, and `user` items. Here are examples for all minimal objects.

#### movie

```
{
    \"title\": \"Batman Begins\",
    \"year\": 2005,
    \"ids\": {
        \"trakt\": 1,
        \"slug\": \"batman-begins-2005\",
        \"imdb\": \"tt0372784\",
        \"tmdb\": 272
    }
}
```

#### show

```
{
    \"title\": \"Breaking Bad\",
    \"year\": 2008,
    \"ids\": {
        \"trakt\": 1,
        \"slug\": \"breaking-bad\",
        \"tvdb\": 81189,
        \"imdb\": \"tt0903747\",
        \"tmdb\": 1396
    }
}
```

#### season

```
{
    \"number\": 0,
    \"ids\": {
        \"trakt\": 1,
        \"tvdb\": 439371,
        \"tmdb\": 3577
    }
}
```

#### episode

```
{
    \"season\": 1,
    \"number\": 1,
    \"title\": \"Pilot\",
    \"ids\": {
        \"trakt\": 16,
        \"tvdb\": 349232,
        \"imdb\": \"tt0959621\",
        \"tmdb\": 62085
    }
}
```

#### person

```
{
    \"name\": \"Bryan Cranston\",
    \"ids\": {
        \"trakt\": 142,
        \"slug\": \"bryan-cranston\",
        \"imdb\": \"nm0186505\",
        \"tmdb\": 17419
    }
}
```

#### user

```
{
    \"username\": \"sean\",
    \"private\": false,
    \"name\": \"Sean Rudford\",
    \"vip\": true,
    \"vip_ep\": true,
    \"ids\": {
        \"slug\": \"sean\"
    }
}
```

# Images

The standard media objects for all `movie`, `show`, `season`, `episode`, and `person` items include an `ids` object. These `ids` map to other services like [TMDB](https://www.themoviedb.org), [TVDB](https://thetvdb.com), [Fanart.tv](https://fanart.tv), [IMDB](https://www.imdb.com), and [OMDB](https://www.omdbapi.com/).

Most of these services have free APIs you can use to grab lots of great looking images. Here’s a chart to help you find the best artwork for your app. [**We also wrote an article to help with this.**](https://apiblog.trakt.tv/how-to-find-the-best-images-516045bcc3b6)

| Media | Type | [TMDB](https://developers.themoviedb.org/3) | [TVDB](https://api.thetvdb.com/swagger) | [Fanart.tv](http://docs.fanarttv.apiary.io) | [OMDB](https://www.omdbapi.com) |
|---|---|---|---|---|---|
| `shows` | `poster` | &#10003; | &#10003; | &#10003; | &#10003; |
|  | `fanart` | &#10003; | &#10003; | &#10003; |  |
|  | `banner` |  | &#10003; | &#10003; |  |
|  | `logo` |  |  | &#10003; |  |
|  | `clearart` |  |  | &#10003; |  |
|  | `thumb` |  |  | &#10003; |  |
| `seasons` | `poster` | &#10003; | &#10003; | &#10003; |  |
|  | `banner` |  | &#10003; | &#10003; |  |
|  | `thumb` |  |  | &#10003; |  |
| `episodes` | `screenshot` | &#10003; | &#10003; |  |  |
| `movies` | `poster` | &#10003; |  | &#10003; | &#10003; |
|  | `fanart` | &#10003; |  | &#10003; |  |
|  | `banner` |  |  | &#10003; |  |
|  | `logo` |  |  | &#10003; |  |
|  | `clearart` |  |  | &#10003; |  |
|  | `thumb` |  |  | &#10003; |  |
| `person` | `headshot` | &#10003; |  |  |  |
|  | `character` |  | &#10003; |  |  |

# Website Media Links

There are several ways to construct direct links to media on the Trakt website. The website itself uses slugs so the URLs are more readable.

| Type | URL |
|---|---|
| `movie` | `/movies/:slug` |
| `show` | `/shows/:slug` |
| `season` | `/shows/:slug/seasons/:num` |
| `episode` | `/shows/:slug/seasons/:num/episodes/:num` |
| `person` | `/people/:slug` |
| `comment` | `/comments/:id` |
| `list` | `/lists/:id` |

You can also create links using the Trakt, IMDB, TMDB, or TVDB IDs. We recommend using the Trakt ID if possible since that will always have full coverage. If you use the search url without an `id_type` it will return search results if multiple items are found.

| Type | URL |
|---|---|
| `trakt` | `/search/trakt/:id` |
|  | `/search/trakt/:id?id_type=movie` |
|  | `/search/trakt/:id?id_type=show` |
|  | `/search/trakt/:id?id_type=season` |
|  | `/search/trakt/:id?id_type=episode` |
|  | `/search/trakt/:id?id_type=person` |
| `imdb` | `/search/imdb/:id` |
| `tmdb` | `/search/tmdb/:id` |
|  | `/search/tmdb/:id?id_type=movie` |
|  | `/search/tmdb/:id?id_type=show` |
|  | `/search/tmdb/:id?id_type=episode` |
|  | `/search/tmdb/:id?id_type=person` |
| `tvdb` | `/search/tvdb/:id` |
|  | `/search/tvdb/:id?id_type=show` |
|  | `/search/tvdb/:id?id_type=episode` |

# Third Party Libraries

All of the libraries listed below are user contributed. If you find a bug or missing feature, please contact the developer directly. These might help give your project a head start, but we can't provide direct support for any of these libraries. Please help us keep this list up to date.

| Language | Name | Repository |
|---|---|---|
| `C#` | `Trakt.NET` | https://github.com/henrikfroehling/Trakt.NET |
|  | `TraktSharp` | https://github.com/wwarby/TraktSharp |
| `C++` | `libtraqt` | https://github.com/RobertMe/libtraqt |
| `Clojure` | `clj-trakt` | https://github.com/niamu/clj-trakt |
| `Java` | `trakt-java` | https://github.com/UweTrottmann/trakt-java |
| `Kotlin` | `trakt-api` | https://github.com/MoviebaseApp/trakt-api |
| `Node.js` | `Trakt.tv` | https://github.com/vankasteelj/trakt.tv |
|  | `TraktApi2` | https://github.com/PatrickE94/traktapi2 |
| `Python` | `trakt.py` | https://github.com/fuzeman/trakt.py |
|  | `pyTrakt` | https://github.com/moogar0880/PyTrakt |
| `R` | `tRakt` | https://github.com/jemus42/tRakt |
| `React Native` | `nodeless-trakt` | https://github.com/kdemoya/nodeless-trakt |
| `Ruby` | `omniauth-trakt` | https://github.com/wafcio/omniauth-trakt |
|  | `omniauth-trakt` | https://github.com/alextakitani/omniauth-trakt |
| `Swift` | `TraktKit` | https://github.com/MaxHasADHD/TraktKit |
|  | `AKTrakt` | https://github.com/arsonik/AKTrakt |

# Terminology

Trakt has a lot of features and here's a chart to help explain the differences between some of them.

| Term | Description |
|---|---|
| `scrobble` | Automatic way to track what a user is watching in a media center. |
| `checkin` | Manual action used by mobile apps allowing the user to indicate what they are watching right now. |
| `history` | All watched items (scrobbles, checkins, watched) for a user. |
| `collection` | Items a user has available to watch including Blu-Rays, DVDs, and digital downloads. |
| `watchlist` | Items a user wants to watch in the future. Once watched, they are auto removed from this list. |
| `list` | Personal list for any purpose. Items are not auto removed from any personal lists. |
| `recommendations` | Movies and TV shows a user personally recommends to others. |
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install trakt_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your trakt_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var TraktApi = require('trakt_api');


var api = new TraktApi.AuthenticationDevicesApi()
var opts = {
  'generateNewDeviceCodesRequest': new TraktApi.GenerateNewDeviceCodesRequest() // {GenerateNewDeviceCodesRequest} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.generateNewDeviceCodes(opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.trakt.tv*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TraktApi.AuthenticationDevicesApi* | [**generateNewDeviceCodes**](docs/AuthenticationDevicesApi.md#generateNewDeviceCodes) | **POST** /oauth/device/code | Generate new device codes
*TraktApi.AuthenticationDevicesApi* | [**pollForTheAccessToken**](docs/AuthenticationDevicesApi.md#pollForTheAccessToken) | **POST** /oauth/device/token | Poll for the access_token
*TraktApi.AuthenticationOAuthApi* | [**authorizeApplication**](docs/AuthenticationOAuthApi.md#authorizeApplication) | **GET** /oauth/authorize | Authorize Application
*TraktApi.AuthenticationOAuthApi* | [**exchangeRefreshTokenForAccessToken**](docs/AuthenticationOAuthApi.md#exchangeRefreshTokenForAccessToken) | **POST** /oauth/token | Exchange refresh_token for access_token
*TraktApi.AuthenticationOAuthApi* | [**revokeAnAccessToken**](docs/AuthenticationOAuthApi.md#revokeAnAccessToken) | **POST** /oauth/revoke | Revoke an access_token
*TraktApi.CalendarsApi* | [**calendarsAllDvdStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllDvdStartDateDaysGet) | **GET** /calendars/all/dvd/{start_date}/{days} | Get DVD releases
*TraktApi.CalendarsApi* | [**calendarsAllMoviesStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllMoviesStartDateDaysGet) | **GET** /calendars/all/movies/{start_date}/{days} | Get movies
*TraktApi.CalendarsApi* | [**calendarsAllShowsNewStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllShowsNewStartDateDaysGet) | **GET** /calendars/all/shows/new/{start_date}/{days} | Get new shows
*TraktApi.CalendarsApi* | [**calendarsAllShowsPremieresStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllShowsPremieresStartDateDaysGet) | **GET** /calendars/all/shows/premieres/{start_date}/{days} | Get season premieres
*TraktApi.CalendarsApi* | [**calendarsAllShowsStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllShowsStartDateDaysGet) | **GET** /calendars/all/shows/{start_date}/{days} | Get shows
*TraktApi.CalendarsApi* | [**getDVDReleases**](docs/CalendarsApi.md#getDVDReleases) | **GET** /calendars/my/dvd/{start_date}/{days} | Get DVD releases
*TraktApi.CalendarsApi* | [**getMovies**](docs/CalendarsApi.md#getMovies) | **GET** /calendars/my/movies/{start_date}/{days} | Get movies
*TraktApi.CalendarsApi* | [**getNewShows**](docs/CalendarsApi.md#getNewShows) | **GET** /calendars/my/shows/new/{start_date}/{days} | Get new shows
*TraktApi.CalendarsApi* | [**getSeasonPremieres**](docs/CalendarsApi.md#getSeasonPremieres) | **GET** /calendars/my/shows/premieres/{start_date}/{days} | Get season premieres
*TraktApi.CalendarsApi* | [**getShows**](docs/CalendarsApi.md#getShows) | **GET** /calendars/my/shows/{start_date}/{days} | Get shows
*TraktApi.CertificationsApi* | [**getCertifications**](docs/CertificationsApi.md#getCertifications) | **GET** /certifications/{type} | Get certifications
*TraktApi.CheckinApi* | [**checkIntoAnItem**](docs/CheckinApi.md#checkIntoAnItem) | **POST** /checkin | Check into an item
*TraktApi.CheckinApi* | [**deleteAnyActiveCheckins**](docs/CheckinApi.md#deleteAnyActiveCheckins) | **DELETE** /checkin | Delete any active checkins
*TraktApi.CommentsApi* | [**deleteACommentOrReply**](docs/CommentsApi.md#deleteACommentOrReply) | **DELETE** /comments/{id} | Delete a comment or reply
*TraktApi.CommentsApi* | [**getACommentOrReply**](docs/CommentsApi.md#getACommentOrReply) | **GET** /comments/{id} | Get a comment or reply
*TraktApi.CommentsApi* | [**getAllUsersWhoLikedAComment**](docs/CommentsApi.md#getAllUsersWhoLikedAComment) | **GET** /comments/{id}/likes | Get all users who liked a comment
*TraktApi.CommentsApi* | [**getRecentlyCreatedComments**](docs/CommentsApi.md#getRecentlyCreatedComments) | **GET** /comments/recent/{comment_type}/{type} | Get recently created comments
*TraktApi.CommentsApi* | [**getRecentlyUpdatedComments**](docs/CommentsApi.md#getRecentlyUpdatedComments) | **GET** /comments/updates/{comment_type}/{type} | Get recently updated comments
*TraktApi.CommentsApi* | [**getRepliesForAComment**](docs/CommentsApi.md#getRepliesForAComment) | **GET** /comments/{id}/replies | Get replies for a comment
*TraktApi.CommentsApi* | [**getTheAttachedMediaItem**](docs/CommentsApi.md#getTheAttachedMediaItem) | **GET** /comments/{id}/item | Get the attached media item
*TraktApi.CommentsApi* | [**getTrendingComments**](docs/CommentsApi.md#getTrendingComments) | **GET** /comments/trending/{comment_type}/{type} | Get trending comments
*TraktApi.CommentsApi* | [**likeAComment**](docs/CommentsApi.md#likeAComment) | **POST** /comments/{id}/like | Like a comment
*TraktApi.CommentsApi* | [**postAComment**](docs/CommentsApi.md#postAComment) | **POST** /comments | Post a comment
*TraktApi.CommentsApi* | [**postAReplyForAComment**](docs/CommentsApi.md#postAReplyForAComment) | **POST** /comments/{id}/replies | Post a reply for a comment
*TraktApi.CommentsApi* | [**removeLikeOnAComment**](docs/CommentsApi.md#removeLikeOnAComment) | **DELETE** /comments/{id}/like | Remove like on a comment
*TraktApi.CommentsApi* | [**updateACommentOrReply**](docs/CommentsApi.md#updateACommentOrReply) | **PUT** /comments/{id} | Update a comment or reply
*TraktApi.CountriesApi* | [**getCountries**](docs/CountriesApi.md#getCountries) | **GET** /countries/{type} | Get countries
*TraktApi.EpisodesApi* | [**getASingleEpisodeForAShow**](docs/EpisodesApi.md#getASingleEpisodeForAShow) | **GET** /shows/{id}/seasons/{season}/episodes/{episode} | Get a single episode for a show
*TraktApi.EpisodesApi* | [**getAllEpisodeComments**](docs/EpisodesApi.md#getAllEpisodeComments) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort} | Get all episode comments
*TraktApi.EpisodesApi* | [**getAllEpisodeTranslations**](docs/EpisodesApi.md#getAllEpisodeTranslations) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/translations/{language} | Get all episode translations
*TraktApi.EpisodesApi* | [**getAllPeopleForAnEpisode**](docs/EpisodesApi.md#getAllPeopleForAnEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/people | Get all people for an episode
*TraktApi.EpisodesApi* | [**getEpisodeRatings**](docs/EpisodesApi.md#getEpisodeRatings) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/ratings | Get episode ratings
*TraktApi.EpisodesApi* | [**getEpisodeStats**](docs/EpisodesApi.md#getEpisodeStats) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/stats | Get episode stats
*TraktApi.EpisodesApi* | [**getListsContainingThisEpisode**](docs/EpisodesApi.md#getListsContainingThisEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort} | Get lists containing this episode
*TraktApi.EpisodesApi* | [**showsIdSeasonsSeasonEpisodesEpisodeWatchingGet**](docs/EpisodesApi.md#showsIdSeasonsSeasonEpisodesEpisodeWatchingGet) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/watching | Get users watching right now
*TraktApi.GenresApi* | [**getGenres**](docs/GenresApi.md#getGenres) | **GET** /genres/{type} | Get genres
*TraktApi.LanguagesApi* | [**getLanguages**](docs/LanguagesApi.md#getLanguages) | **GET** /languages/{type} | Get languages
*TraktApi.ListsApi* | [**getAllListComments**](docs/ListsApi.md#getAllListComments) | **GET** /lists/{id}/comments/{sort} | Get all list comments
*TraktApi.ListsApi* | [**getAllUsersWhoLikedAList**](docs/ListsApi.md#getAllUsersWhoLikedAList) | **GET** /lists/{id}/likes | Get all users who liked a list
*TraktApi.ListsApi* | [**getItemsOnAList**](docs/ListsApi.md#getItemsOnAList) | **GET** /lists/{id}/items/{type} | Get items on a list
*TraktApi.ListsApi* | [**getList**](docs/ListsApi.md#getList) | **GET** /lists/{id} | Get list
*TraktApi.ListsApi* | [**getPopularLists**](docs/ListsApi.md#getPopularLists) | **GET** /lists/popular | Get popular lists
*TraktApi.ListsApi* | [**getTrendingLists**](docs/ListsApi.md#getTrendingLists) | **GET** /lists/trending | Get trending lists
*TraktApi.MoviesApi* | [**getAMovie**](docs/MoviesApi.md#getAMovie) | **GET** /movies/{id} | Get a movie
*TraktApi.MoviesApi* | [**getAllMovieAliases**](docs/MoviesApi.md#getAllMovieAliases) | **GET** /movies/{id}/aliases | Get all movie aliases
*TraktApi.MoviesApi* | [**getAllMovieComments**](docs/MoviesApi.md#getAllMovieComments) | **GET** /movies/{id}/comments/{sort} | Get all movie comments
*TraktApi.MoviesApi* | [**getAllMovieReleases**](docs/MoviesApi.md#getAllMovieReleases) | **GET** /movies/{id}/releases/{country} | Get all movie releases
*TraktApi.MoviesApi* | [**getAllMovieTranslations**](docs/MoviesApi.md#getAllMovieTranslations) | **GET** /movies/{id}/translations/{language} | Get all movie translations
*TraktApi.MoviesApi* | [**getAllPeopleForAMovie**](docs/MoviesApi.md#getAllPeopleForAMovie) | **GET** /movies/{id}/people | Get all people for a movie
*TraktApi.MoviesApi* | [**getListsContainingThisMovie**](docs/MoviesApi.md#getListsContainingThisMovie) | **GET** /movies/{id}/lists/{type}/{sort} | Get lists containing this movie
*TraktApi.MoviesApi* | [**getMovieRatings**](docs/MoviesApi.md#getMovieRatings) | **GET** /movies/{id}/ratings | Get movie ratings
*TraktApi.MoviesApi* | [**getMovieStats**](docs/MoviesApi.md#getMovieStats) | **GET** /movies/{id}/stats | Get movie stats
*TraktApi.MoviesApi* | [**getMovieStudios**](docs/MoviesApi.md#getMovieStudios) | **GET** /movies/{id}/studios | Get movie studios
*TraktApi.MoviesApi* | [**getPopularMovies**](docs/MoviesApi.md#getPopularMovies) | **GET** /movies/popular | Get popular movies
*TraktApi.MoviesApi* | [**getRecentlyUpdatedMovieTraktIDs**](docs/MoviesApi.md#getRecentlyUpdatedMovieTraktIDs) | **GET** /movies/updates/id/{start_date} | Get recently updated movie Trakt IDs
*TraktApi.MoviesApi* | [**getRecentlyUpdatedMovies**](docs/MoviesApi.md#getRecentlyUpdatedMovies) | **GET** /movies/updates/{start_date} | Get recently updated movies
*TraktApi.MoviesApi* | [**getRelatedMovies**](docs/MoviesApi.md#getRelatedMovies) | **GET** /movies/{id}/related | Get related movies
*TraktApi.MoviesApi* | [**getTheMostAnticipatedMovies**](docs/MoviesApi.md#getTheMostAnticipatedMovies) | **GET** /movies/anticipated | Get the most anticipated movies
*TraktApi.MoviesApi* | [**getTheMostCollectedMovies**](docs/MoviesApi.md#getTheMostCollectedMovies) | **GET** /movies/collected/{period} | Get the most Collected movies
*TraktApi.MoviesApi* | [**getTheMostPlayedMovies**](docs/MoviesApi.md#getTheMostPlayedMovies) | **GET** /movies/played/{period} | Get the most played movies
*TraktApi.MoviesApi* | [**getTheMostRecommendedMovies**](docs/MoviesApi.md#getTheMostRecommendedMovies) | **GET** /movies/recommended/{period} | Get the most recommended movies
*TraktApi.MoviesApi* | [**getTheMostWatchedMovies**](docs/MoviesApi.md#getTheMostWatchedMovies) | **GET** /movies/watched/{period} | Get the most watched movies
*TraktApi.MoviesApi* | [**getTheWeekendBoxOffice**](docs/MoviesApi.md#getTheWeekendBoxOffice) | **GET** /movies/boxoffice | Get the weekend box office
*TraktApi.MoviesApi* | [**getTrendingMovies**](docs/MoviesApi.md#getTrendingMovies) | **GET** /movies/trending | Get trending movies
*TraktApi.MoviesApi* | [**getUsersWatchingRightNow**](docs/MoviesApi.md#getUsersWatchingRightNow) | **GET** /movies/{id}/watching | Get users watching right now
*TraktApi.NetworksApi* | [**getNetworks**](docs/NetworksApi.md#getNetworks) | **GET** /networks | Get networks
*TraktApi.PeopleApi* | [**getASinglePerson**](docs/PeopleApi.md#getASinglePerson) | **GET** /people/{id} | Get a single person
*TraktApi.PeopleApi* | [**getListsContainingThisPerson**](docs/PeopleApi.md#getListsContainingThisPerson) | **GET** /people/{id}/lists/{type}/{sort} | Get lists containing this person
*TraktApi.PeopleApi* | [**getMovieCredits**](docs/PeopleApi.md#getMovieCredits) | **GET** /people/{id}/movies | Get movie credits
*TraktApi.PeopleApi* | [**getRecentlyUpdatedPeople**](docs/PeopleApi.md#getRecentlyUpdatedPeople) | **GET** /people/updates/{start_date} | Get recently updated people
*TraktApi.PeopleApi* | [**getRecentlyUpdatedPeopleTraktIDs**](docs/PeopleApi.md#getRecentlyUpdatedPeopleTraktIDs) | **GET** /people/updates/id/{start_date} | Get recently updated people Trakt IDs
*TraktApi.PeopleApi* | [**getShowCredits**](docs/PeopleApi.md#getShowCredits) | **GET** /people/{id}/shows | Get show credits
*TraktApi.RecommendationsApi* | [**getMovieRecommendations**](docs/RecommendationsApi.md#getMovieRecommendations) | **GET** /recommendations/movies | Get movie recommendations
*TraktApi.RecommendationsApi* | [**getShowRecommendations**](docs/RecommendationsApi.md#getShowRecommendations) | **GET** /recommendations/shows | Get show recommendations
*TraktApi.RecommendationsApi* | [**hideAMovieRecommendation**](docs/RecommendationsApi.md#hideAMovieRecommendation) | **DELETE** /recommendations/movies/{id} | Hide a movie recommendation
*TraktApi.RecommendationsApi* | [**hideAShowRecommendation**](docs/RecommendationsApi.md#hideAShowRecommendation) | **DELETE** /recommendations/shows/{id} | Hide a show recommendation
*TraktApi.ScrobbleApi* | [**pauseWatchingInAMediaCenter**](docs/ScrobbleApi.md#pauseWatchingInAMediaCenter) | **POST** /scrobble/pause | Pause watching in a media center
*TraktApi.ScrobbleApi* | [**startWatchingInAMediaCenter**](docs/ScrobbleApi.md#startWatchingInAMediaCenter) | **POST** /scrobble/start | Start watching in a media center
*TraktApi.ScrobbleApi* | [**stopOrFinishWatchingInAMediaCenter**](docs/ScrobbleApi.md#stopOrFinishWatchingInAMediaCenter) | **POST** /scrobble/stop | Stop or finish watching in a media center
*TraktApi.SearchApi* | [**getIDLookupResults**](docs/SearchApi.md#getIDLookupResults) | **GET** /search/{id_type}/{id} | Get ID lookup results
*TraktApi.SearchApi* | [**getTextQueryResults**](docs/SearchApi.md#getTextQueryResults) | **GET** /search/{type} | Get text query results
*TraktApi.SeasonsApi* | [**getAllPeopleForASeason**](docs/SeasonsApi.md#getAllPeopleForASeason) | **GET** /shows/{id}/seasons/{season}/people | Get all people for a season
*TraktApi.SeasonsApi* | [**getAllSeasonComments**](docs/SeasonsApi.md#getAllSeasonComments) | **GET** /shows/{id}/seasons/{season}/comments/{sort} | Get all season comments
*TraktApi.SeasonsApi* | [**getAllSeasonTranslations**](docs/SeasonsApi.md#getAllSeasonTranslations) | **GET** /shows/{id}/seasons/{season}/translations/{language} | Get all season translations
*TraktApi.SeasonsApi* | [**getAllSeasonsForAShow**](docs/SeasonsApi.md#getAllSeasonsForAShow) | **GET** /shows/{id}/seasons | Get all seasons for a show
*TraktApi.SeasonsApi* | [**getListsContainingThisSeason**](docs/SeasonsApi.md#getListsContainingThisSeason) | **GET** /shows/{id}/seasons/{season}/lists/{type}/{sort} | Get lists containing this season
*TraktApi.SeasonsApi* | [**getSeasonRatings**](docs/SeasonsApi.md#getSeasonRatings) | **GET** /shows/{id}/seasons/{season}/ratings | Get season ratings
*TraktApi.SeasonsApi* | [**getSeasonStats**](docs/SeasonsApi.md#getSeasonStats) | **GET** /shows/{id}/seasons/{season}/stats | Get season stats
*TraktApi.SeasonsApi* | [**getSingleSeasonForAShow**](docs/SeasonsApi.md#getSingleSeasonForAShow) | **GET** /shows/{id}/seasons/{season} | Get single season for a show
*TraktApi.SeasonsApi* | [**showsIdSeasonsSeasonWatchingGet**](docs/SeasonsApi.md#showsIdSeasonsSeasonWatchingGet) | **GET** /shows/{id}/seasons/{season}/watching | Get users watching right now
*TraktApi.ShowsApi* | [**getASingleShow**](docs/ShowsApi.md#getASingleShow) | **GET** /shows/{id} | Get a single show
*TraktApi.ShowsApi* | [**getAllPeopleForAShow**](docs/ShowsApi.md#getAllPeopleForAShow) | **GET** /shows/{id}/people | Get all people for a show
*TraktApi.ShowsApi* | [**getAllShowAliases**](docs/ShowsApi.md#getAllShowAliases) | **GET** /shows/{id}/aliases | Get all show aliases
*TraktApi.ShowsApi* | [**getAllShowCertifications**](docs/ShowsApi.md#getAllShowCertifications) | **GET** /shows/{id}/certifications | Get all show certifications
*TraktApi.ShowsApi* | [**getAllShowComments**](docs/ShowsApi.md#getAllShowComments) | **GET** /shows/{id}/comments/{sort} | Get all show comments
*TraktApi.ShowsApi* | [**getAllShowTranslations**](docs/ShowsApi.md#getAllShowTranslations) | **GET** /shows/{id}/translations/{language} | Get all show translations
*TraktApi.ShowsApi* | [**getLastEpisode**](docs/ShowsApi.md#getLastEpisode) | **GET** /shows/{id}/last_episode | Get last episode
*TraktApi.ShowsApi* | [**getListsContainingThisShow**](docs/ShowsApi.md#getListsContainingThisShow) | **GET** /shows/{id}/lists/{type}/{sort} | Get lists containing this show
*TraktApi.ShowsApi* | [**getNextEpisode**](docs/ShowsApi.md#getNextEpisode) | **GET** /shows/{id}/next_episode | Get next episode
*TraktApi.ShowsApi* | [**getPopularShows**](docs/ShowsApi.md#getPopularShows) | **GET** /shows/popular | Get popular shows
*TraktApi.ShowsApi* | [**getRecentlyUpdatedShowTraktIDs**](docs/ShowsApi.md#getRecentlyUpdatedShowTraktIDs) | **GET** /shows/updates/id/{start_date} | Get recently updated show Trakt IDs
*TraktApi.ShowsApi* | [**getRecentlyUpdatedShows**](docs/ShowsApi.md#getRecentlyUpdatedShows) | **GET** /shows/updates/{start_date} | Get recently updated shows
*TraktApi.ShowsApi* | [**getRelatedShows**](docs/ShowsApi.md#getRelatedShows) | **GET** /shows/{id}/related | Get related shows
*TraktApi.ShowsApi* | [**getShowCollectionProgress**](docs/ShowsApi.md#getShowCollectionProgress) | **GET** /shows/{id}/progress/collection | Get show collection progress
*TraktApi.ShowsApi* | [**getShowRatings**](docs/ShowsApi.md#getShowRatings) | **GET** /shows/{id}/ratings | Get show ratings
*TraktApi.ShowsApi* | [**getShowStats**](docs/ShowsApi.md#getShowStats) | **GET** /shows/{id}/stats | Get show stats
*TraktApi.ShowsApi* | [**getShowStudios**](docs/ShowsApi.md#getShowStudios) | **GET** /shows/{id}/studios | Get show studios
*TraktApi.ShowsApi* | [**getShowWatchedProgress**](docs/ShowsApi.md#getShowWatchedProgress) | **GET** /shows/{id}/progress/watched | Get show watched progress
*TraktApi.ShowsApi* | [**getTheMostAnticipatedShows**](docs/ShowsApi.md#getTheMostAnticipatedShows) | **GET** /shows/anticipated | Get the most anticipated shows
*TraktApi.ShowsApi* | [**getTheMostCollectedShows**](docs/ShowsApi.md#getTheMostCollectedShows) | **GET** /shows/collected/{period} | Get the most collected shows
*TraktApi.ShowsApi* | [**getTheMostPlayedShows**](docs/ShowsApi.md#getTheMostPlayedShows) | **GET** /shows/played/{period} | Get the most played shows
*TraktApi.ShowsApi* | [**getTheMostRecommendedShows**](docs/ShowsApi.md#getTheMostRecommendedShows) | **GET** /shows/recommended/{period} | Get the most recommended shows
*TraktApi.ShowsApi* | [**getTheMostWatchedShows**](docs/ShowsApi.md#getTheMostWatchedShows) | **GET** /shows/watched/{period} | Get the most watched shows
*TraktApi.ShowsApi* | [**getTrendingShows**](docs/ShowsApi.md#getTrendingShows) | **GET** /shows/trending | Get trending shows
*TraktApi.ShowsApi* | [**resetShowProgress**](docs/ShowsApi.md#resetShowProgress) | **POST** /shows/{id}/progress/watched/reset | Reset show progress
*TraktApi.ShowsApi* | [**showsIdWatchingGet**](docs/ShowsApi.md#showsIdWatchingGet) | **GET** /shows/{id}/watching | Get users watching right now
*TraktApi.ShowsApi* | [**undoResetShowProgress**](docs/ShowsApi.md#undoResetShowProgress) | **DELETE** /shows/{id}/progress/watched/reset | Undo reset show progress
*TraktApi.SyncApi* | [**addItemsToCollection**](docs/SyncApi.md#addItemsToCollection) | **POST** /sync/collection | Add items to collection
*TraktApi.SyncApi* | [**addItemsToPersonalRecommendations**](docs/SyncApi.md#addItemsToPersonalRecommendations) | **POST** /sync/recommendations | Add items to personal recommendations
*TraktApi.SyncApi* | [**addItemsToWatchedHistory**](docs/SyncApi.md#addItemsToWatchedHistory) | **POST** /sync/history | Add items to watched history
*TraktApi.SyncApi* | [**addItemsToWatchlist**](docs/SyncApi.md#addItemsToWatchlist) | **POST** /sync/watchlist | Add items to watchlist
*TraktApi.SyncApi* | [**addNewRatings**](docs/SyncApi.md#addNewRatings) | **POST** /sync/ratings | Add new ratings
*TraktApi.SyncApi* | [**getCollection**](docs/SyncApi.md#getCollection) | **GET** /sync/collection/{type} | Get collection
*TraktApi.SyncApi* | [**getLastActivity**](docs/SyncApi.md#getLastActivity) | **GET** /sync/last_activities | Get last activity
*TraktApi.SyncApi* | [**getPersonalRecommendations**](docs/SyncApi.md#getPersonalRecommendations) | **GET** /sync/recommendations/{type}/{sort} | Get personal recommendations
*TraktApi.SyncApi* | [**getPlaybackProgress**](docs/SyncApi.md#getPlaybackProgress) | **GET** /sync/playback/{type} | Get playback progress
*TraktApi.SyncApi* | [**getRatings**](docs/SyncApi.md#getRatings) | **GET** /sync/ratings/{type}/{rating} | Get ratings
*TraktApi.SyncApi* | [**getWatched**](docs/SyncApi.md#getWatched) | **GET** /sync/watched/{type} | Get watched
*TraktApi.SyncApi* | [**getWatchedHistory**](docs/SyncApi.md#getWatchedHistory) | **GET** /sync/history/{type}/{id} | Get watched history
*TraktApi.SyncApi* | [**getWatchlist**](docs/SyncApi.md#getWatchlist) | **GET** /sync/watchlist/{type}/{sort} | Get watchlist
*TraktApi.SyncApi* | [**removeAPlaybackItem**](docs/SyncApi.md#removeAPlaybackItem) | **DELETE** /sync/playback/{id} | Remove a playback item
*TraktApi.SyncApi* | [**removeItemsFromCollection**](docs/SyncApi.md#removeItemsFromCollection) | **POST** /sync/collection/remove | Remove items from collection
*TraktApi.SyncApi* | [**removeItemsFromHistory**](docs/SyncApi.md#removeItemsFromHistory) | **POST** /sync/history/remove | Remove items from history
*TraktApi.SyncApi* | [**removeItemsFromPersonalRecommendations**](docs/SyncApi.md#removeItemsFromPersonalRecommendations) | **POST** /sync/recommendations/remove | Remove items from personal recommendations
*TraktApi.SyncApi* | [**removeItemsFromWatchlist**](docs/SyncApi.md#removeItemsFromWatchlist) | **POST** /sync/watchlist/remove | Remove items from watchlist
*TraktApi.SyncApi* | [**removeRatings**](docs/SyncApi.md#removeRatings) | **POST** /sync/ratings/remove | Remove ratings
*TraktApi.SyncApi* | [**reorderPersonallyRecommendedItems**](docs/SyncApi.md#reorderPersonallyRecommendedItems) | **POST** /sync/recommendations/reorder | Reorder personally recommended items
*TraktApi.SyncApi* | [**reorderWatchlistItems**](docs/SyncApi.md#reorderWatchlistItems) | **POST** /sync/watchlist/reorder | Reorder watchlist items
*TraktApi.UsersApi* | [**addHiddenItems**](docs/UsersApi.md#addHiddenItems) | **POST** /users/hidden/{section} | Add hidden items
*TraktApi.UsersApi* | [**addItemsToPersonalList**](docs/UsersApi.md#addItemsToPersonalList) | **POST** /users/{id}/lists/{list_id}/items | Add items to personal list
*TraktApi.UsersApi* | [**approveFollowRequest**](docs/UsersApi.md#approveFollowRequest) | **POST** /users/requests/{id} | Approve follow request
*TraktApi.UsersApi* | [**createPersonalList**](docs/UsersApi.md#createPersonalList) | **POST** /users/{id}/lists | Create personal list
*TraktApi.UsersApi* | [**deleteAUsersPersonalList**](docs/UsersApi.md#deleteAUsersPersonalList) | **DELETE** /users/{id}/lists/{list_id} | Delete a user&#39;s personal list
*TraktApi.UsersApi* | [**denyFollowRequest**](docs/UsersApi.md#denyFollowRequest) | **DELETE** /users/requests/{id} | Deny follow request
*TraktApi.UsersApi* | [**followThisUser**](docs/UsersApi.md#followThisUser) | **POST** /users/{id}/follow | Follow this user
*TraktApi.UsersApi* | [**getAUsersPersonalLists**](docs/UsersApi.md#getAUsersPersonalLists) | **GET** /users/{id}/lists | Get a user&#39;s personal lists
*TraktApi.UsersApi* | [**getAllListsAUserCanCollaborateOn**](docs/UsersApi.md#getAllListsAUserCanCollaborateOn) | **GET** /users/{id}/lists/collaborations | Get all lists a user can collaborate on
*TraktApi.UsersApi* | [**getComments**](docs/UsersApi.md#getComments) | **GET** /users/{id}/comments/{comment_type}/{type} | Get comments
*TraktApi.UsersApi* | [**getFollowRequests**](docs/UsersApi.md#getFollowRequests) | **GET** /users/requests | Get follow requests
*TraktApi.UsersApi* | [**getFollowers**](docs/UsersApi.md#getFollowers) | **GET** /users/{id}/followers | Get followers
*TraktApi.UsersApi* | [**getFollowing**](docs/UsersApi.md#getFollowing) | **GET** /users/{id}/following | Get following
*TraktApi.UsersApi* | [**getFriends**](docs/UsersApi.md#getFriends) | **GET** /users/{id}/friends | Get friends
*TraktApi.UsersApi* | [**getHiddenItems**](docs/UsersApi.md#getHiddenItems) | **GET** /users/hidden/{section} | Get hidden items
*TraktApi.UsersApi* | [**getItemsOnAPersonalList**](docs/UsersApi.md#getItemsOnAPersonalList) | **GET** /users/{id}/lists/{list_id}/items/{type} | Get items on a personal list
*TraktApi.UsersApi* | [**getLikes**](docs/UsersApi.md#getLikes) | **GET** /users/{id}/likes/{type} | Get likes
*TraktApi.UsersApi* | [**getPendingFollowingRequests**](docs/UsersApi.md#getPendingFollowingRequests) | **GET** /users/requests/following | Get pending following requests
*TraktApi.UsersApi* | [**getPersonalList**](docs/UsersApi.md#getPersonalList) | **GET** /users/{id}/lists/{list_id} | Get personal list
*TraktApi.UsersApi* | [**getSavedFilters**](docs/UsersApi.md#getSavedFilters) | **GET** /users/saved_filters/{section} | Get saved filters
*TraktApi.UsersApi* | [**getStats**](docs/UsersApi.md#getStats) | **GET** /users/{id}/stats | Get stats
*TraktApi.UsersApi* | [**getUserProfile**](docs/UsersApi.md#getUserProfile) | **GET** /users/{id} | Get user profile
*TraktApi.UsersApi* | [**getWatching**](docs/UsersApi.md#getWatching) | **GET** /users/{id}/watching | Get watching
*TraktApi.UsersApi* | [**likeAList**](docs/UsersApi.md#likeAList) | **POST** /users/{id}/lists/{list_id}/like | Like a list
*TraktApi.UsersApi* | [**removeHiddenItems**](docs/UsersApi.md#removeHiddenItems) | **POST** /users/hidden/{section}/remove | Remove hidden items
*TraktApi.UsersApi* | [**removeItemsFromPersonalList**](docs/UsersApi.md#removeItemsFromPersonalList) | **POST** /users/{id}/lists/{list_id}/items/remove | Remove items from personal list
*TraktApi.UsersApi* | [**removeLikeOnAList**](docs/UsersApi.md#removeLikeOnAList) | **DELETE** /users/{id}/lists/{list_id}/like | Remove like on a list
*TraktApi.UsersApi* | [**reorderAUsersLists**](docs/UsersApi.md#reorderAUsersLists) | **POST** /users/{id}/lists/reorder | Reorder a user&#39;s lists
*TraktApi.UsersApi* | [**reorderItemsOnAList**](docs/UsersApi.md#reorderItemsOnAList) | **POST** /users/{id}/lists/{list_id}/items/reorder | Reorder items on a list
*TraktApi.UsersApi* | [**retrieveSettings**](docs/UsersApi.md#retrieveSettings) | **GET** /users/settings | Retrieve settings
*TraktApi.UsersApi* | [**unfollowThisUser**](docs/UsersApi.md#unfollowThisUser) | **DELETE** /users/{id}/follow | Unfollow this user
*TraktApi.UsersApi* | [**updatePersonalList**](docs/UsersApi.md#updatePersonalList) | **PUT** /users/{id}/lists/{list_id} | Update personal list
*TraktApi.UsersApi* | [**usersIdCollectionTypeGet**](docs/UsersApi.md#usersIdCollectionTypeGet) | **GET** /users/{id}/collection/{type} | Get collection
*TraktApi.UsersApi* | [**usersIdHistoryTypeItemIdGet**](docs/UsersApi.md#usersIdHistoryTypeItemIdGet) | **GET** /users/{id}/history/{type}/{item_id} | Get watched history
*TraktApi.UsersApi* | [**usersIdListsListIdCommentsSortGet**](docs/UsersApi.md#usersIdListsListIdCommentsSortGet) | **GET** /users/{id}/lists/{list_id}/comments/{sort} | Get all list comments
*TraktApi.UsersApi* | [**usersIdListsListIdLikesGet**](docs/UsersApi.md#usersIdListsListIdLikesGet) | **GET** /users/{id}/lists/{list_id}/likes | Get all users who liked a list
*TraktApi.UsersApi* | [**usersIdRatingsTypeRatingGet**](docs/UsersApi.md#usersIdRatingsTypeRatingGet) | **GET** /users/{id}/ratings/{type}/{rating} | Get ratings
*TraktApi.UsersApi* | [**usersIdRecommendationsTypeSortGet**](docs/UsersApi.md#usersIdRecommendationsTypeSortGet) | **GET** /users/{id}/recommendations/{type}/{sort} | Get personal recommendations
*TraktApi.UsersApi* | [**usersIdWatchedTypeGet**](docs/UsersApi.md#usersIdWatchedTypeGet) | **GET** /users/{id}/watched/{type} | Get watched
*TraktApi.UsersApi* | [**usersIdWatchlistTypeSortGet**](docs/UsersApi.md#usersIdWatchlistTypeSortGet) | **GET** /users/{id}/watchlist/{type}/{sort} | Get watchlist


## Documentation for Models

 - [TraktApi.AddHiddenItemsRequest](docs/AddHiddenItemsRequest.md)
 - [TraktApi.AddHiddenItemsRequestSeasonsInner](docs/AddHiddenItemsRequestSeasonsInner.md)
 - [TraktApi.AddHiddenItemsRequestSeasonsInnerIds](docs/AddHiddenItemsRequestSeasonsInnerIds.md)
 - [TraktApi.AddHiddenItemsRequestShowsInner](docs/AddHiddenItemsRequestShowsInner.md)
 - [TraktApi.AddHiddenItemsRequestShowsInnerSeasonsInner](docs/AddHiddenItemsRequestShowsInnerSeasonsInner.md)
 - [TraktApi.AddItemsToCollectionRequest](docs/AddItemsToCollectionRequest.md)
 - [TraktApi.AddItemsToCollectionRequestEpisodesInner](docs/AddItemsToCollectionRequestEpisodesInner.md)
 - [TraktApi.AddItemsToCollectionRequestEpisodesInnerIds](docs/AddItemsToCollectionRequestEpisodesInnerIds.md)
 - [TraktApi.AddItemsToCollectionRequestMoviesInner](docs/AddItemsToCollectionRequestMoviesInner.md)
 - [TraktApi.AddItemsToCollectionRequestSeasonsInner](docs/AddItemsToCollectionRequestSeasonsInner.md)
 - [TraktApi.AddItemsToCollectionRequestSeasonsInnerIds](docs/AddItemsToCollectionRequestSeasonsInnerIds.md)
 - [TraktApi.AddItemsToCollectionRequestShowsInner](docs/AddItemsToCollectionRequestShowsInner.md)
 - [TraktApi.AddItemsToCollectionRequestShowsInnerIds](docs/AddItemsToCollectionRequestShowsInnerIds.md)
 - [TraktApi.AddItemsToCollectionRequestShowsInnerSeasonsInner](docs/AddItemsToCollectionRequestShowsInnerSeasonsInner.md)
 - [TraktApi.AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner](docs/AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [TraktApi.AddItemsToPersonalListRequest](docs/AddItemsToPersonalListRequest.md)
 - [TraktApi.AddItemsToPersonalListRequestMoviesInner](docs/AddItemsToPersonalListRequestMoviesInner.md)
 - [TraktApi.AddItemsToPersonalListRequestMoviesInnerIds](docs/AddItemsToPersonalListRequestMoviesInnerIds.md)
 - [TraktApi.AddItemsToPersonalListRequestPeopleInner](docs/AddItemsToPersonalListRequestPeopleInner.md)
 - [TraktApi.AddItemsToPersonalListRequestShowsInner](docs/AddItemsToPersonalListRequestShowsInner.md)
 - [TraktApi.AddItemsToPersonalRecommendationsRequest](docs/AddItemsToPersonalRecommendationsRequest.md)
 - [TraktApi.AddItemsToPersonalRecommendationsRequestMoviesInner](docs/AddItemsToPersonalRecommendationsRequestMoviesInner.md)
 - [TraktApi.AddItemsToPersonalRecommendationsRequestShowsInner](docs/AddItemsToPersonalRecommendationsRequestShowsInner.md)
 - [TraktApi.AddItemsToWatchedHistoryRequest](docs/AddItemsToWatchedHistoryRequest.md)
 - [TraktApi.AddItemsToWatchedHistoryRequestEpisodesInner](docs/AddItemsToWatchedHistoryRequestEpisodesInner.md)
 - [TraktApi.AddItemsToWatchedHistoryRequestMoviesInner](docs/AddItemsToWatchedHistoryRequestMoviesInner.md)
 - [TraktApi.AddItemsToWatchedHistoryRequestSeasonsInner](docs/AddItemsToWatchedHistoryRequestSeasonsInner.md)
 - [TraktApi.AddItemsToWatchedHistoryRequestShowsInner](docs/AddItemsToWatchedHistoryRequestShowsInner.md)
 - [TraktApi.AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner](docs/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner.md)
 - [TraktApi.AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner](docs/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [TraktApi.AddItemsToWatchlistRequest](docs/AddItemsToWatchlistRequest.md)
 - [TraktApi.AddItemsToWatchlistRequestShowsInner](docs/AddItemsToWatchlistRequestShowsInner.md)
 - [TraktApi.AddNewRatingsRequest](docs/AddNewRatingsRequest.md)
 - [TraktApi.AddNewRatingsRequestEpisodesInner](docs/AddNewRatingsRequestEpisodesInner.md)
 - [TraktApi.AddNewRatingsRequestMoviesInner](docs/AddNewRatingsRequestMoviesInner.md)
 - [TraktApi.AddNewRatingsRequestSeasonsInner](docs/AddNewRatingsRequestSeasonsInner.md)
 - [TraktApi.AddNewRatingsRequestShowsInner](docs/AddNewRatingsRequestShowsInner.md)
 - [TraktApi.AddNewRatingsRequestShowsInnerSeasonsInner](docs/AddNewRatingsRequestShowsInnerSeasonsInner.md)
 - [TraktApi.AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner](docs/AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [TraktApi.CheckIntoAnItemRequest](docs/CheckIntoAnItemRequest.md)
 - [TraktApi.CheckIntoAnItemRequestMovie](docs/CheckIntoAnItemRequestMovie.md)
 - [TraktApi.CheckIntoAnItemRequestMovieIds](docs/CheckIntoAnItemRequestMovieIds.md)
 - [TraktApi.CheckIntoAnItemRequestSharing](docs/CheckIntoAnItemRequestSharing.md)
 - [TraktApi.CreatePersonalListRequest](docs/CreatePersonalListRequest.md)
 - [TraktApi.ExchangeRefreshTokenForAccessTokenRequest](docs/ExchangeRefreshTokenForAccessTokenRequest.md)
 - [TraktApi.GenerateNewDeviceCodesRequest](docs/GenerateNewDeviceCodesRequest.md)
 - [TraktApi.PauseWatchingInAMediaCenterRequest](docs/PauseWatchingInAMediaCenterRequest.md)
 - [TraktApi.PollForTheAccessTokenRequest](docs/PollForTheAccessTokenRequest.md)
 - [TraktApi.PostACommentRequest](docs/PostACommentRequest.md)
 - [TraktApi.PostACommentRequestSharing](docs/PostACommentRequestSharing.md)
 - [TraktApi.PostAReplyForACommentRequest](docs/PostAReplyForACommentRequest.md)
 - [TraktApi.RemoveItemsFromCollectionRequest](docs/RemoveItemsFromCollectionRequest.md)
 - [TraktApi.RemoveItemsFromCollectionRequestMoviesInner](docs/RemoveItemsFromCollectionRequestMoviesInner.md)
 - [TraktApi.RemoveItemsFromCollectionRequestShowsInner](docs/RemoveItemsFromCollectionRequestShowsInner.md)
 - [TraktApi.RemoveItemsFromCollectionRequestShowsInnerSeasonsInner](docs/RemoveItemsFromCollectionRequestShowsInnerSeasonsInner.md)
 - [TraktApi.RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner](docs/RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [TraktApi.RemoveItemsFromHistoryRequest](docs/RemoveItemsFromHistoryRequest.md)
 - [TraktApi.RemoveItemsFromPersonalListRequest](docs/RemoveItemsFromPersonalListRequest.md)
 - [TraktApi.RemoveItemsFromPersonalListRequestMoviesInner](docs/RemoveItemsFromPersonalListRequestMoviesInner.md)
 - [TraktApi.RemoveItemsFromPersonalListRequestShowsInner](docs/RemoveItemsFromPersonalListRequestShowsInner.md)
 - [TraktApi.RemoveItemsFromPersonalRecommendationsRequest](docs/RemoveItemsFromPersonalRecommendationsRequest.md)
 - [TraktApi.RemoveItemsFromPersonalRecommendationsRequestShowsInner](docs/RemoveItemsFromPersonalRecommendationsRequestShowsInner.md)
 - [TraktApi.ReorderAUserSListsRequest](docs/ReorderAUserSListsRequest.md)
 - [TraktApi.ReorderPersonallyRecommendedItemsRequest](docs/ReorderPersonallyRecommendedItemsRequest.md)
 - [TraktApi.RevokeAnAccessTokenRequest](docs/RevokeAnAccessTokenRequest.md)
 - [TraktApi.StartWatchingInAMediaCenterRequest](docs/StartWatchingInAMediaCenterRequest.md)
 - [TraktApi.StopOrFinishWatchingInAMediaCenterRequest](docs/StopOrFinishWatchingInAMediaCenterRequest.md)
 - [TraktApi.UpdateACommentOrReplyRequest](docs/UpdateACommentOrReplyRequest.md)
 - [TraktApi.UpdatePersonalListRequest](docs/UpdatePersonalListRequest.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### oauth2


- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: /
- **Scopes**: N/A

