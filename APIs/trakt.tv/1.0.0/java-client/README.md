# openapi-java-client

Trakt API
- API version: 1.0.0
  - Build date: 2024-10-12T12:41:35.899060-04:00[America/New_York]
  - Generator version: 7.9.0

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


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AuthenticationDevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    AuthenticationDevicesApi apiInstance = new AuthenticationDevicesApi(defaultClient);
    GenerateNewDeviceCodesRequest generateNewDeviceCodesRequest = new GenerateNewDeviceCodesRequest(); // GenerateNewDeviceCodesRequest | 
    try {
      apiInstance.generateNewDeviceCodes(generateNewDeviceCodesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationDevicesApi#generateNewDeviceCodes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.trakt.tv*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationDevicesApi* | [**generateNewDeviceCodes**](docs/AuthenticationDevicesApi.md#generateNewDeviceCodes) | **POST** /oauth/device/code | Generate new device codes
*AuthenticationDevicesApi* | [**pollForTheAccessToken**](docs/AuthenticationDevicesApi.md#pollForTheAccessToken) | **POST** /oauth/device/token | Poll for the access_token
*AuthenticationOAuthApi* | [**authorizeApplication**](docs/AuthenticationOAuthApi.md#authorizeApplication) | **GET** /oauth/authorize | Authorize Application
*AuthenticationOAuthApi* | [**exchangeRefreshTokenForAccessToken**](docs/AuthenticationOAuthApi.md#exchangeRefreshTokenForAccessToken) | **POST** /oauth/token | Exchange refresh_token for access_token
*AuthenticationOAuthApi* | [**revokeAnAccessToken**](docs/AuthenticationOAuthApi.md#revokeAnAccessToken) | **POST** /oauth/revoke | Revoke an access_token
*CalendarsApi* | [**calendarsAllDvdStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllDvdStartDateDaysGet) | **GET** /calendars/all/dvd/{start_date}/{days} | Get DVD releases
*CalendarsApi* | [**calendarsAllMoviesStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllMoviesStartDateDaysGet) | **GET** /calendars/all/movies/{start_date}/{days} | Get movies
*CalendarsApi* | [**calendarsAllShowsNewStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllShowsNewStartDateDaysGet) | **GET** /calendars/all/shows/new/{start_date}/{days} | Get new shows
*CalendarsApi* | [**calendarsAllShowsPremieresStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllShowsPremieresStartDateDaysGet) | **GET** /calendars/all/shows/premieres/{start_date}/{days} | Get season premieres
*CalendarsApi* | [**calendarsAllShowsStartDateDaysGet**](docs/CalendarsApi.md#calendarsAllShowsStartDateDaysGet) | **GET** /calendars/all/shows/{start_date}/{days} | Get shows
*CalendarsApi* | [**getDVDReleases**](docs/CalendarsApi.md#getDVDReleases) | **GET** /calendars/my/dvd/{start_date}/{days} | Get DVD releases
*CalendarsApi* | [**getMovies**](docs/CalendarsApi.md#getMovies) | **GET** /calendars/my/movies/{start_date}/{days} | Get movies
*CalendarsApi* | [**getNewShows**](docs/CalendarsApi.md#getNewShows) | **GET** /calendars/my/shows/new/{start_date}/{days} | Get new shows
*CalendarsApi* | [**getSeasonPremieres**](docs/CalendarsApi.md#getSeasonPremieres) | **GET** /calendars/my/shows/premieres/{start_date}/{days} | Get season premieres
*CalendarsApi* | [**getShows**](docs/CalendarsApi.md#getShows) | **GET** /calendars/my/shows/{start_date}/{days} | Get shows
*CertificationsApi* | [**getCertifications**](docs/CertificationsApi.md#getCertifications) | **GET** /certifications/{type} | Get certifications
*CheckinApi* | [**checkIntoAnItem**](docs/CheckinApi.md#checkIntoAnItem) | **POST** /checkin | Check into an item
*CheckinApi* | [**deleteAnyActiveCheckins**](docs/CheckinApi.md#deleteAnyActiveCheckins) | **DELETE** /checkin | Delete any active checkins
*CommentsApi* | [**deleteACommentOrReply**](docs/CommentsApi.md#deleteACommentOrReply) | **DELETE** /comments/{id} | Delete a comment or reply
*CommentsApi* | [**getACommentOrReply**](docs/CommentsApi.md#getACommentOrReply) | **GET** /comments/{id} | Get a comment or reply
*CommentsApi* | [**getAllUsersWhoLikedAComment**](docs/CommentsApi.md#getAllUsersWhoLikedAComment) | **GET** /comments/{id}/likes | Get all users who liked a comment
*CommentsApi* | [**getRecentlyCreatedComments**](docs/CommentsApi.md#getRecentlyCreatedComments) | **GET** /comments/recent/{comment_type}/{type} | Get recently created comments
*CommentsApi* | [**getRecentlyUpdatedComments**](docs/CommentsApi.md#getRecentlyUpdatedComments) | **GET** /comments/updates/{comment_type}/{type} | Get recently updated comments
*CommentsApi* | [**getRepliesForAComment**](docs/CommentsApi.md#getRepliesForAComment) | **GET** /comments/{id}/replies | Get replies for a comment
*CommentsApi* | [**getTheAttachedMediaItem**](docs/CommentsApi.md#getTheAttachedMediaItem) | **GET** /comments/{id}/item | Get the attached media item
*CommentsApi* | [**getTrendingComments**](docs/CommentsApi.md#getTrendingComments) | **GET** /comments/trending/{comment_type}/{type} | Get trending comments
*CommentsApi* | [**likeAComment**](docs/CommentsApi.md#likeAComment) | **POST** /comments/{id}/like | Like a comment
*CommentsApi* | [**postAComment**](docs/CommentsApi.md#postAComment) | **POST** /comments | Post a comment
*CommentsApi* | [**postAReplyForAComment**](docs/CommentsApi.md#postAReplyForAComment) | **POST** /comments/{id}/replies | Post a reply for a comment
*CommentsApi* | [**removeLikeOnAComment**](docs/CommentsApi.md#removeLikeOnAComment) | **DELETE** /comments/{id}/like | Remove like on a comment
*CommentsApi* | [**updateACommentOrReply**](docs/CommentsApi.md#updateACommentOrReply) | **PUT** /comments/{id} | Update a comment or reply
*CountriesApi* | [**getCountries**](docs/CountriesApi.md#getCountries) | **GET** /countries/{type} | Get countries
*EpisodesApi* | [**getASingleEpisodeForAShow**](docs/EpisodesApi.md#getASingleEpisodeForAShow) | **GET** /shows/{id}/seasons/{season}/episodes/{episode} | Get a single episode for a show
*EpisodesApi* | [**getAllEpisodeComments**](docs/EpisodesApi.md#getAllEpisodeComments) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort} | Get all episode comments
*EpisodesApi* | [**getAllEpisodeTranslations**](docs/EpisodesApi.md#getAllEpisodeTranslations) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/translations/{language} | Get all episode translations
*EpisodesApi* | [**getAllPeopleForAnEpisode**](docs/EpisodesApi.md#getAllPeopleForAnEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/people | Get all people for an episode
*EpisodesApi* | [**getEpisodeRatings**](docs/EpisodesApi.md#getEpisodeRatings) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/ratings | Get episode ratings
*EpisodesApi* | [**getEpisodeStats**](docs/EpisodesApi.md#getEpisodeStats) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/stats | Get episode stats
*EpisodesApi* | [**getListsContainingThisEpisode**](docs/EpisodesApi.md#getListsContainingThisEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort} | Get lists containing this episode
*EpisodesApi* | [**showsIdSeasonsSeasonEpisodesEpisodeWatchingGet**](docs/EpisodesApi.md#showsIdSeasonsSeasonEpisodesEpisodeWatchingGet) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/watching | Get users watching right now
*GenresApi* | [**getGenres**](docs/GenresApi.md#getGenres) | **GET** /genres/{type} | Get genres
*LanguagesApi* | [**getLanguages**](docs/LanguagesApi.md#getLanguages) | **GET** /languages/{type} | Get languages
*ListsApi* | [**getAllListComments**](docs/ListsApi.md#getAllListComments) | **GET** /lists/{id}/comments/{sort} | Get all list comments
*ListsApi* | [**getAllUsersWhoLikedAList**](docs/ListsApi.md#getAllUsersWhoLikedAList) | **GET** /lists/{id}/likes | Get all users who liked a list
*ListsApi* | [**getItemsOnAList**](docs/ListsApi.md#getItemsOnAList) | **GET** /lists/{id}/items/{type} | Get items on a list
*ListsApi* | [**getList**](docs/ListsApi.md#getList) | **GET** /lists/{id} | Get list
*ListsApi* | [**getPopularLists**](docs/ListsApi.md#getPopularLists) | **GET** /lists/popular | Get popular lists
*ListsApi* | [**getTrendingLists**](docs/ListsApi.md#getTrendingLists) | **GET** /lists/trending | Get trending lists
*MoviesApi* | [**getAMovie**](docs/MoviesApi.md#getAMovie) | **GET** /movies/{id} | Get a movie
*MoviesApi* | [**getAllMovieAliases**](docs/MoviesApi.md#getAllMovieAliases) | **GET** /movies/{id}/aliases | Get all movie aliases
*MoviesApi* | [**getAllMovieComments**](docs/MoviesApi.md#getAllMovieComments) | **GET** /movies/{id}/comments/{sort} | Get all movie comments
*MoviesApi* | [**getAllMovieReleases**](docs/MoviesApi.md#getAllMovieReleases) | **GET** /movies/{id}/releases/{country} | Get all movie releases
*MoviesApi* | [**getAllMovieTranslations**](docs/MoviesApi.md#getAllMovieTranslations) | **GET** /movies/{id}/translations/{language} | Get all movie translations
*MoviesApi* | [**getAllPeopleForAMovie**](docs/MoviesApi.md#getAllPeopleForAMovie) | **GET** /movies/{id}/people | Get all people for a movie
*MoviesApi* | [**getListsContainingThisMovie**](docs/MoviesApi.md#getListsContainingThisMovie) | **GET** /movies/{id}/lists/{type}/{sort} | Get lists containing this movie
*MoviesApi* | [**getMovieRatings**](docs/MoviesApi.md#getMovieRatings) | **GET** /movies/{id}/ratings | Get movie ratings
*MoviesApi* | [**getMovieStats**](docs/MoviesApi.md#getMovieStats) | **GET** /movies/{id}/stats | Get movie stats
*MoviesApi* | [**getMovieStudios**](docs/MoviesApi.md#getMovieStudios) | **GET** /movies/{id}/studios | Get movie studios
*MoviesApi* | [**getPopularMovies**](docs/MoviesApi.md#getPopularMovies) | **GET** /movies/popular | Get popular movies
*MoviesApi* | [**getRecentlyUpdatedMovieTraktIDs**](docs/MoviesApi.md#getRecentlyUpdatedMovieTraktIDs) | **GET** /movies/updates/id/{start_date} | Get recently updated movie Trakt IDs
*MoviesApi* | [**getRecentlyUpdatedMovies**](docs/MoviesApi.md#getRecentlyUpdatedMovies) | **GET** /movies/updates/{start_date} | Get recently updated movies
*MoviesApi* | [**getRelatedMovies**](docs/MoviesApi.md#getRelatedMovies) | **GET** /movies/{id}/related | Get related movies
*MoviesApi* | [**getTheMostAnticipatedMovies**](docs/MoviesApi.md#getTheMostAnticipatedMovies) | **GET** /movies/anticipated | Get the most anticipated movies
*MoviesApi* | [**getTheMostCollectedMovies**](docs/MoviesApi.md#getTheMostCollectedMovies) | **GET** /movies/collected/{period} | Get the most Collected movies
*MoviesApi* | [**getTheMostPlayedMovies**](docs/MoviesApi.md#getTheMostPlayedMovies) | **GET** /movies/played/{period} | Get the most played movies
*MoviesApi* | [**getTheMostRecommendedMovies**](docs/MoviesApi.md#getTheMostRecommendedMovies) | **GET** /movies/recommended/{period} | Get the most recommended movies
*MoviesApi* | [**getTheMostWatchedMovies**](docs/MoviesApi.md#getTheMostWatchedMovies) | **GET** /movies/watched/{period} | Get the most watched movies
*MoviesApi* | [**getTheWeekendBoxOffice**](docs/MoviesApi.md#getTheWeekendBoxOffice) | **GET** /movies/boxoffice | Get the weekend box office
*MoviesApi* | [**getTrendingMovies**](docs/MoviesApi.md#getTrendingMovies) | **GET** /movies/trending | Get trending movies
*MoviesApi* | [**getUsersWatchingRightNow**](docs/MoviesApi.md#getUsersWatchingRightNow) | **GET** /movies/{id}/watching | Get users watching right now
*NetworksApi* | [**getNetworks**](docs/NetworksApi.md#getNetworks) | **GET** /networks | Get networks
*PeopleApi* | [**getASinglePerson**](docs/PeopleApi.md#getASinglePerson) | **GET** /people/{id} | Get a single person
*PeopleApi* | [**getListsContainingThisPerson**](docs/PeopleApi.md#getListsContainingThisPerson) | **GET** /people/{id}/lists/{type}/{sort} | Get lists containing this person
*PeopleApi* | [**getMovieCredits**](docs/PeopleApi.md#getMovieCredits) | **GET** /people/{id}/movies | Get movie credits
*PeopleApi* | [**getRecentlyUpdatedPeople**](docs/PeopleApi.md#getRecentlyUpdatedPeople) | **GET** /people/updates/{start_date} | Get recently updated people
*PeopleApi* | [**getRecentlyUpdatedPeopleTraktIDs**](docs/PeopleApi.md#getRecentlyUpdatedPeopleTraktIDs) | **GET** /people/updates/id/{start_date} | Get recently updated people Trakt IDs
*PeopleApi* | [**getShowCredits**](docs/PeopleApi.md#getShowCredits) | **GET** /people/{id}/shows | Get show credits
*RecommendationsApi* | [**getMovieRecommendations**](docs/RecommendationsApi.md#getMovieRecommendations) | **GET** /recommendations/movies | Get movie recommendations
*RecommendationsApi* | [**getShowRecommendations**](docs/RecommendationsApi.md#getShowRecommendations) | **GET** /recommendations/shows | Get show recommendations
*RecommendationsApi* | [**hideAMovieRecommendation**](docs/RecommendationsApi.md#hideAMovieRecommendation) | **DELETE** /recommendations/movies/{id} | Hide a movie recommendation
*RecommendationsApi* | [**hideAShowRecommendation**](docs/RecommendationsApi.md#hideAShowRecommendation) | **DELETE** /recommendations/shows/{id} | Hide a show recommendation
*ScrobbleApi* | [**pauseWatchingInAMediaCenter**](docs/ScrobbleApi.md#pauseWatchingInAMediaCenter) | **POST** /scrobble/pause | Pause watching in a media center
*ScrobbleApi* | [**startWatchingInAMediaCenter**](docs/ScrobbleApi.md#startWatchingInAMediaCenter) | **POST** /scrobble/start | Start watching in a media center
*ScrobbleApi* | [**stopOrFinishWatchingInAMediaCenter**](docs/ScrobbleApi.md#stopOrFinishWatchingInAMediaCenter) | **POST** /scrobble/stop | Stop or finish watching in a media center
*SearchApi* | [**getIDLookupResults**](docs/SearchApi.md#getIDLookupResults) | **GET** /search/{id_type}/{id} | Get ID lookup results
*SearchApi* | [**getTextQueryResults**](docs/SearchApi.md#getTextQueryResults) | **GET** /search/{type} | Get text query results
*SeasonsApi* | [**getAllPeopleForASeason**](docs/SeasonsApi.md#getAllPeopleForASeason) | **GET** /shows/{id}/seasons/{season}/people | Get all people for a season
*SeasonsApi* | [**getAllSeasonComments**](docs/SeasonsApi.md#getAllSeasonComments) | **GET** /shows/{id}/seasons/{season}/comments/{sort} | Get all season comments
*SeasonsApi* | [**getAllSeasonTranslations**](docs/SeasonsApi.md#getAllSeasonTranslations) | **GET** /shows/{id}/seasons/{season}/translations/{language} | Get all season translations
*SeasonsApi* | [**getAllSeasonsForAShow**](docs/SeasonsApi.md#getAllSeasonsForAShow) | **GET** /shows/{id}/seasons | Get all seasons for a show
*SeasonsApi* | [**getListsContainingThisSeason**](docs/SeasonsApi.md#getListsContainingThisSeason) | **GET** /shows/{id}/seasons/{season}/lists/{type}/{sort} | Get lists containing this season
*SeasonsApi* | [**getSeasonRatings**](docs/SeasonsApi.md#getSeasonRatings) | **GET** /shows/{id}/seasons/{season}/ratings | Get season ratings
*SeasonsApi* | [**getSeasonStats**](docs/SeasonsApi.md#getSeasonStats) | **GET** /shows/{id}/seasons/{season}/stats | Get season stats
*SeasonsApi* | [**getSingleSeasonForAShow**](docs/SeasonsApi.md#getSingleSeasonForAShow) | **GET** /shows/{id}/seasons/{season} | Get single season for a show
*SeasonsApi* | [**showsIdSeasonsSeasonWatchingGet**](docs/SeasonsApi.md#showsIdSeasonsSeasonWatchingGet) | **GET** /shows/{id}/seasons/{season}/watching | Get users watching right now
*ShowsApi* | [**getASingleShow**](docs/ShowsApi.md#getASingleShow) | **GET** /shows/{id} | Get a single show
*ShowsApi* | [**getAllPeopleForAShow**](docs/ShowsApi.md#getAllPeopleForAShow) | **GET** /shows/{id}/people | Get all people for a show
*ShowsApi* | [**getAllShowAliases**](docs/ShowsApi.md#getAllShowAliases) | **GET** /shows/{id}/aliases | Get all show aliases
*ShowsApi* | [**getAllShowCertifications**](docs/ShowsApi.md#getAllShowCertifications) | **GET** /shows/{id}/certifications | Get all show certifications
*ShowsApi* | [**getAllShowComments**](docs/ShowsApi.md#getAllShowComments) | **GET** /shows/{id}/comments/{sort} | Get all show comments
*ShowsApi* | [**getAllShowTranslations**](docs/ShowsApi.md#getAllShowTranslations) | **GET** /shows/{id}/translations/{language} | Get all show translations
*ShowsApi* | [**getLastEpisode**](docs/ShowsApi.md#getLastEpisode) | **GET** /shows/{id}/last_episode | Get last episode
*ShowsApi* | [**getListsContainingThisShow**](docs/ShowsApi.md#getListsContainingThisShow) | **GET** /shows/{id}/lists/{type}/{sort} | Get lists containing this show
*ShowsApi* | [**getNextEpisode**](docs/ShowsApi.md#getNextEpisode) | **GET** /shows/{id}/next_episode | Get next episode
*ShowsApi* | [**getPopularShows**](docs/ShowsApi.md#getPopularShows) | **GET** /shows/popular | Get popular shows
*ShowsApi* | [**getRecentlyUpdatedShowTraktIDs**](docs/ShowsApi.md#getRecentlyUpdatedShowTraktIDs) | **GET** /shows/updates/id/{start_date} | Get recently updated show Trakt IDs
*ShowsApi* | [**getRecentlyUpdatedShows**](docs/ShowsApi.md#getRecentlyUpdatedShows) | **GET** /shows/updates/{start_date} | Get recently updated shows
*ShowsApi* | [**getRelatedShows**](docs/ShowsApi.md#getRelatedShows) | **GET** /shows/{id}/related | Get related shows
*ShowsApi* | [**getShowCollectionProgress**](docs/ShowsApi.md#getShowCollectionProgress) | **GET** /shows/{id}/progress/collection | Get show collection progress
*ShowsApi* | [**getShowRatings**](docs/ShowsApi.md#getShowRatings) | **GET** /shows/{id}/ratings | Get show ratings
*ShowsApi* | [**getShowStats**](docs/ShowsApi.md#getShowStats) | **GET** /shows/{id}/stats | Get show stats
*ShowsApi* | [**getShowStudios**](docs/ShowsApi.md#getShowStudios) | **GET** /shows/{id}/studios | Get show studios
*ShowsApi* | [**getShowWatchedProgress**](docs/ShowsApi.md#getShowWatchedProgress) | **GET** /shows/{id}/progress/watched | Get show watched progress
*ShowsApi* | [**getTheMostAnticipatedShows**](docs/ShowsApi.md#getTheMostAnticipatedShows) | **GET** /shows/anticipated | Get the most anticipated shows
*ShowsApi* | [**getTheMostCollectedShows**](docs/ShowsApi.md#getTheMostCollectedShows) | **GET** /shows/collected/{period} | Get the most collected shows
*ShowsApi* | [**getTheMostPlayedShows**](docs/ShowsApi.md#getTheMostPlayedShows) | **GET** /shows/played/{period} | Get the most played shows
*ShowsApi* | [**getTheMostRecommendedShows**](docs/ShowsApi.md#getTheMostRecommendedShows) | **GET** /shows/recommended/{period} | Get the most recommended shows
*ShowsApi* | [**getTheMostWatchedShows**](docs/ShowsApi.md#getTheMostWatchedShows) | **GET** /shows/watched/{period} | Get the most watched shows
*ShowsApi* | [**getTrendingShows**](docs/ShowsApi.md#getTrendingShows) | **GET** /shows/trending | Get trending shows
*ShowsApi* | [**resetShowProgress**](docs/ShowsApi.md#resetShowProgress) | **POST** /shows/{id}/progress/watched/reset | Reset show progress
*ShowsApi* | [**showsIdWatchingGet**](docs/ShowsApi.md#showsIdWatchingGet) | **GET** /shows/{id}/watching | Get users watching right now
*ShowsApi* | [**undoResetShowProgress**](docs/ShowsApi.md#undoResetShowProgress) | **DELETE** /shows/{id}/progress/watched/reset | Undo reset show progress
*SyncApi* | [**addItemsToCollection**](docs/SyncApi.md#addItemsToCollection) | **POST** /sync/collection | Add items to collection
*SyncApi* | [**addItemsToPersonalRecommendations**](docs/SyncApi.md#addItemsToPersonalRecommendations) | **POST** /sync/recommendations | Add items to personal recommendations
*SyncApi* | [**addItemsToWatchedHistory**](docs/SyncApi.md#addItemsToWatchedHistory) | **POST** /sync/history | Add items to watched history
*SyncApi* | [**addItemsToWatchlist**](docs/SyncApi.md#addItemsToWatchlist) | **POST** /sync/watchlist | Add items to watchlist
*SyncApi* | [**addNewRatings**](docs/SyncApi.md#addNewRatings) | **POST** /sync/ratings | Add new ratings
*SyncApi* | [**getCollection**](docs/SyncApi.md#getCollection) | **GET** /sync/collection/{type} | Get collection
*SyncApi* | [**getLastActivity**](docs/SyncApi.md#getLastActivity) | **GET** /sync/last_activities | Get last activity
*SyncApi* | [**getPersonalRecommendations**](docs/SyncApi.md#getPersonalRecommendations) | **GET** /sync/recommendations/{type}/{sort} | Get personal recommendations
*SyncApi* | [**getPlaybackProgress**](docs/SyncApi.md#getPlaybackProgress) | **GET** /sync/playback/{type} | Get playback progress
*SyncApi* | [**getRatings**](docs/SyncApi.md#getRatings) | **GET** /sync/ratings/{type}/{rating} | Get ratings
*SyncApi* | [**getWatched**](docs/SyncApi.md#getWatched) | **GET** /sync/watched/{type} | Get watched
*SyncApi* | [**getWatchedHistory**](docs/SyncApi.md#getWatchedHistory) | **GET** /sync/history/{type}/{id} | Get watched history
*SyncApi* | [**getWatchlist**](docs/SyncApi.md#getWatchlist) | **GET** /sync/watchlist/{type}/{sort} | Get watchlist
*SyncApi* | [**removeAPlaybackItem**](docs/SyncApi.md#removeAPlaybackItem) | **DELETE** /sync/playback/{id} | Remove a playback item
*SyncApi* | [**removeItemsFromCollection**](docs/SyncApi.md#removeItemsFromCollection) | **POST** /sync/collection/remove | Remove items from collection
*SyncApi* | [**removeItemsFromHistory**](docs/SyncApi.md#removeItemsFromHistory) | **POST** /sync/history/remove | Remove items from history
*SyncApi* | [**removeItemsFromPersonalRecommendations**](docs/SyncApi.md#removeItemsFromPersonalRecommendations) | **POST** /sync/recommendations/remove | Remove items from personal recommendations
*SyncApi* | [**removeItemsFromWatchlist**](docs/SyncApi.md#removeItemsFromWatchlist) | **POST** /sync/watchlist/remove | Remove items from watchlist
*SyncApi* | [**removeRatings**](docs/SyncApi.md#removeRatings) | **POST** /sync/ratings/remove | Remove ratings
*SyncApi* | [**reorderPersonallyRecommendedItems**](docs/SyncApi.md#reorderPersonallyRecommendedItems) | **POST** /sync/recommendations/reorder | Reorder personally recommended items
*SyncApi* | [**reorderWatchlistItems**](docs/SyncApi.md#reorderWatchlistItems) | **POST** /sync/watchlist/reorder | Reorder watchlist items
*UsersApi* | [**addHiddenItems**](docs/UsersApi.md#addHiddenItems) | **POST** /users/hidden/{section} | Add hidden items
*UsersApi* | [**addItemsToPersonalList**](docs/UsersApi.md#addItemsToPersonalList) | **POST** /users/{id}/lists/{list_id}/items | Add items to personal list
*UsersApi* | [**approveFollowRequest**](docs/UsersApi.md#approveFollowRequest) | **POST** /users/requests/{id} | Approve follow request
*UsersApi* | [**createPersonalList**](docs/UsersApi.md#createPersonalList) | **POST** /users/{id}/lists | Create personal list
*UsersApi* | [**deleteAUsersPersonalList**](docs/UsersApi.md#deleteAUsersPersonalList) | **DELETE** /users/{id}/lists/{list_id} | Delete a user&#39;s personal list
*UsersApi* | [**denyFollowRequest**](docs/UsersApi.md#denyFollowRequest) | **DELETE** /users/requests/{id} | Deny follow request
*UsersApi* | [**followThisUser**](docs/UsersApi.md#followThisUser) | **POST** /users/{id}/follow | Follow this user
*UsersApi* | [**getAUsersPersonalLists**](docs/UsersApi.md#getAUsersPersonalLists) | **GET** /users/{id}/lists | Get a user&#39;s personal lists
*UsersApi* | [**getAllListsAUserCanCollaborateOn**](docs/UsersApi.md#getAllListsAUserCanCollaborateOn) | **GET** /users/{id}/lists/collaborations | Get all lists a user can collaborate on
*UsersApi* | [**getComments**](docs/UsersApi.md#getComments) | **GET** /users/{id}/comments/{comment_type}/{type} | Get comments
*UsersApi* | [**getFollowRequests**](docs/UsersApi.md#getFollowRequests) | **GET** /users/requests | Get follow requests
*UsersApi* | [**getFollowers**](docs/UsersApi.md#getFollowers) | **GET** /users/{id}/followers | Get followers
*UsersApi* | [**getFollowing**](docs/UsersApi.md#getFollowing) | **GET** /users/{id}/following | Get following
*UsersApi* | [**getFriends**](docs/UsersApi.md#getFriends) | **GET** /users/{id}/friends | Get friends
*UsersApi* | [**getHiddenItems**](docs/UsersApi.md#getHiddenItems) | **GET** /users/hidden/{section} | Get hidden items
*UsersApi* | [**getItemsOnAPersonalList**](docs/UsersApi.md#getItemsOnAPersonalList) | **GET** /users/{id}/lists/{list_id}/items/{type} | Get items on a personal list
*UsersApi* | [**getLikes**](docs/UsersApi.md#getLikes) | **GET** /users/{id}/likes/{type} | Get likes
*UsersApi* | [**getPendingFollowingRequests**](docs/UsersApi.md#getPendingFollowingRequests) | **GET** /users/requests/following | Get pending following requests
*UsersApi* | [**getPersonalList**](docs/UsersApi.md#getPersonalList) | **GET** /users/{id}/lists/{list_id} | Get personal list
*UsersApi* | [**getSavedFilters**](docs/UsersApi.md#getSavedFilters) | **GET** /users/saved_filters/{section} | Get saved filters
*UsersApi* | [**getStats**](docs/UsersApi.md#getStats) | **GET** /users/{id}/stats | Get stats
*UsersApi* | [**getUserProfile**](docs/UsersApi.md#getUserProfile) | **GET** /users/{id} | Get user profile
*UsersApi* | [**getWatching**](docs/UsersApi.md#getWatching) | **GET** /users/{id}/watching | Get watching
*UsersApi* | [**likeAList**](docs/UsersApi.md#likeAList) | **POST** /users/{id}/lists/{list_id}/like | Like a list
*UsersApi* | [**removeHiddenItems**](docs/UsersApi.md#removeHiddenItems) | **POST** /users/hidden/{section}/remove | Remove hidden items
*UsersApi* | [**removeItemsFromPersonalList**](docs/UsersApi.md#removeItemsFromPersonalList) | **POST** /users/{id}/lists/{list_id}/items/remove | Remove items from personal list
*UsersApi* | [**removeLikeOnAList**](docs/UsersApi.md#removeLikeOnAList) | **DELETE** /users/{id}/lists/{list_id}/like | Remove like on a list
*UsersApi* | [**reorderAUsersLists**](docs/UsersApi.md#reorderAUsersLists) | **POST** /users/{id}/lists/reorder | Reorder a user&#39;s lists
*UsersApi* | [**reorderItemsOnAList**](docs/UsersApi.md#reorderItemsOnAList) | **POST** /users/{id}/lists/{list_id}/items/reorder | Reorder items on a list
*UsersApi* | [**retrieveSettings**](docs/UsersApi.md#retrieveSettings) | **GET** /users/settings | Retrieve settings
*UsersApi* | [**unfollowThisUser**](docs/UsersApi.md#unfollowThisUser) | **DELETE** /users/{id}/follow | Unfollow this user
*UsersApi* | [**updatePersonalList**](docs/UsersApi.md#updatePersonalList) | **PUT** /users/{id}/lists/{list_id} | Update personal list
*UsersApi* | [**usersIdCollectionTypeGet**](docs/UsersApi.md#usersIdCollectionTypeGet) | **GET** /users/{id}/collection/{type} | Get collection
*UsersApi* | [**usersIdHistoryTypeItemIdGet**](docs/UsersApi.md#usersIdHistoryTypeItemIdGet) | **GET** /users/{id}/history/{type}/{item_id} | Get watched history
*UsersApi* | [**usersIdListsListIdCommentsSortGet**](docs/UsersApi.md#usersIdListsListIdCommentsSortGet) | **GET** /users/{id}/lists/{list_id}/comments/{sort} | Get all list comments
*UsersApi* | [**usersIdListsListIdLikesGet**](docs/UsersApi.md#usersIdListsListIdLikesGet) | **GET** /users/{id}/lists/{list_id}/likes | Get all users who liked a list
*UsersApi* | [**usersIdRatingsTypeRatingGet**](docs/UsersApi.md#usersIdRatingsTypeRatingGet) | **GET** /users/{id}/ratings/{type}/{rating} | Get ratings
*UsersApi* | [**usersIdRecommendationsTypeSortGet**](docs/UsersApi.md#usersIdRecommendationsTypeSortGet) | **GET** /users/{id}/recommendations/{type}/{sort} | Get personal recommendations
*UsersApi* | [**usersIdWatchedTypeGet**](docs/UsersApi.md#usersIdWatchedTypeGet) | **GET** /users/{id}/watched/{type} | Get watched
*UsersApi* | [**usersIdWatchlistTypeSortGet**](docs/UsersApi.md#usersIdWatchlistTypeSortGet) | **GET** /users/{id}/watchlist/{type}/{sort} | Get watchlist


## Documentation for Models

 - [AddHiddenItemsRequest](docs/AddHiddenItemsRequest.md)
 - [AddHiddenItemsRequestSeasonsInner](docs/AddHiddenItemsRequestSeasonsInner.md)
 - [AddHiddenItemsRequestSeasonsInnerIds](docs/AddHiddenItemsRequestSeasonsInnerIds.md)
 - [AddHiddenItemsRequestShowsInner](docs/AddHiddenItemsRequestShowsInner.md)
 - [AddHiddenItemsRequestShowsInnerSeasonsInner](docs/AddHiddenItemsRequestShowsInnerSeasonsInner.md)
 - [AddItemsToCollectionRequest](docs/AddItemsToCollectionRequest.md)
 - [AddItemsToCollectionRequestEpisodesInner](docs/AddItemsToCollectionRequestEpisodesInner.md)
 - [AddItemsToCollectionRequestEpisodesInnerIds](docs/AddItemsToCollectionRequestEpisodesInnerIds.md)
 - [AddItemsToCollectionRequestMoviesInner](docs/AddItemsToCollectionRequestMoviesInner.md)
 - [AddItemsToCollectionRequestSeasonsInner](docs/AddItemsToCollectionRequestSeasonsInner.md)
 - [AddItemsToCollectionRequestSeasonsInnerIds](docs/AddItemsToCollectionRequestSeasonsInnerIds.md)
 - [AddItemsToCollectionRequestShowsInner](docs/AddItemsToCollectionRequestShowsInner.md)
 - [AddItemsToCollectionRequestShowsInnerIds](docs/AddItemsToCollectionRequestShowsInnerIds.md)
 - [AddItemsToCollectionRequestShowsInnerSeasonsInner](docs/AddItemsToCollectionRequestShowsInnerSeasonsInner.md)
 - [AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner](docs/AddItemsToCollectionRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [AddItemsToPersonalListRequest](docs/AddItemsToPersonalListRequest.md)
 - [AddItemsToPersonalListRequestMoviesInner](docs/AddItemsToPersonalListRequestMoviesInner.md)
 - [AddItemsToPersonalListRequestMoviesInnerIds](docs/AddItemsToPersonalListRequestMoviesInnerIds.md)
 - [AddItemsToPersonalListRequestPeopleInner](docs/AddItemsToPersonalListRequestPeopleInner.md)
 - [AddItemsToPersonalListRequestShowsInner](docs/AddItemsToPersonalListRequestShowsInner.md)
 - [AddItemsToPersonalRecommendationsRequest](docs/AddItemsToPersonalRecommendationsRequest.md)
 - [AddItemsToPersonalRecommendationsRequestMoviesInner](docs/AddItemsToPersonalRecommendationsRequestMoviesInner.md)
 - [AddItemsToPersonalRecommendationsRequestShowsInner](docs/AddItemsToPersonalRecommendationsRequestShowsInner.md)
 - [AddItemsToWatchedHistoryRequest](docs/AddItemsToWatchedHistoryRequest.md)
 - [AddItemsToWatchedHistoryRequestEpisodesInner](docs/AddItemsToWatchedHistoryRequestEpisodesInner.md)
 - [AddItemsToWatchedHistoryRequestMoviesInner](docs/AddItemsToWatchedHistoryRequestMoviesInner.md)
 - [AddItemsToWatchedHistoryRequestSeasonsInner](docs/AddItemsToWatchedHistoryRequestSeasonsInner.md)
 - [AddItemsToWatchedHistoryRequestShowsInner](docs/AddItemsToWatchedHistoryRequestShowsInner.md)
 - [AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner](docs/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInner.md)
 - [AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner](docs/AddItemsToWatchedHistoryRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [AddItemsToWatchlistRequest](docs/AddItemsToWatchlistRequest.md)
 - [AddItemsToWatchlistRequestShowsInner](docs/AddItemsToWatchlistRequestShowsInner.md)
 - [AddNewRatingsRequest](docs/AddNewRatingsRequest.md)
 - [AddNewRatingsRequestEpisodesInner](docs/AddNewRatingsRequestEpisodesInner.md)
 - [AddNewRatingsRequestMoviesInner](docs/AddNewRatingsRequestMoviesInner.md)
 - [AddNewRatingsRequestSeasonsInner](docs/AddNewRatingsRequestSeasonsInner.md)
 - [AddNewRatingsRequestShowsInner](docs/AddNewRatingsRequestShowsInner.md)
 - [AddNewRatingsRequestShowsInnerSeasonsInner](docs/AddNewRatingsRequestShowsInnerSeasonsInner.md)
 - [AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner](docs/AddNewRatingsRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [CheckIntoAnItemRequest](docs/CheckIntoAnItemRequest.md)
 - [CheckIntoAnItemRequestMovie](docs/CheckIntoAnItemRequestMovie.md)
 - [CheckIntoAnItemRequestMovieIds](docs/CheckIntoAnItemRequestMovieIds.md)
 - [CheckIntoAnItemRequestSharing](docs/CheckIntoAnItemRequestSharing.md)
 - [CreatePersonalListRequest](docs/CreatePersonalListRequest.md)
 - [ExchangeRefreshTokenForAccessTokenRequest](docs/ExchangeRefreshTokenForAccessTokenRequest.md)
 - [GenerateNewDeviceCodesRequest](docs/GenerateNewDeviceCodesRequest.md)
 - [PauseWatchingInAMediaCenterRequest](docs/PauseWatchingInAMediaCenterRequest.md)
 - [PollForTheAccessTokenRequest](docs/PollForTheAccessTokenRequest.md)
 - [PostACommentRequest](docs/PostACommentRequest.md)
 - [PostACommentRequestSharing](docs/PostACommentRequestSharing.md)
 - [PostAReplyForACommentRequest](docs/PostAReplyForACommentRequest.md)
 - [RemoveItemsFromCollectionRequest](docs/RemoveItemsFromCollectionRequest.md)
 - [RemoveItemsFromCollectionRequestMoviesInner](docs/RemoveItemsFromCollectionRequestMoviesInner.md)
 - [RemoveItemsFromCollectionRequestShowsInner](docs/RemoveItemsFromCollectionRequestShowsInner.md)
 - [RemoveItemsFromCollectionRequestShowsInnerSeasonsInner](docs/RemoveItemsFromCollectionRequestShowsInnerSeasonsInner.md)
 - [RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner](docs/RemoveItemsFromCollectionRequestShowsInnerSeasonsInnerEpisodesInner.md)
 - [RemoveItemsFromHistoryRequest](docs/RemoveItemsFromHistoryRequest.md)
 - [RemoveItemsFromPersonalListRequest](docs/RemoveItemsFromPersonalListRequest.md)
 - [RemoveItemsFromPersonalListRequestMoviesInner](docs/RemoveItemsFromPersonalListRequestMoviesInner.md)
 - [RemoveItemsFromPersonalListRequestShowsInner](docs/RemoveItemsFromPersonalListRequestShowsInner.md)
 - [RemoveItemsFromPersonalRecommendationsRequest](docs/RemoveItemsFromPersonalRecommendationsRequest.md)
 - [RemoveItemsFromPersonalRecommendationsRequestShowsInner](docs/RemoveItemsFromPersonalRecommendationsRequestShowsInner.md)
 - [ReorderAUserSListsRequest](docs/ReorderAUserSListsRequest.md)
 - [ReorderPersonallyRecommendedItemsRequest](docs/ReorderPersonallyRecommendedItemsRequest.md)
 - [RevokeAnAccessTokenRequest](docs/RevokeAnAccessTokenRequest.md)
 - [StartWatchingInAMediaCenterRequest](docs/StartWatchingInAMediaCenterRequest.md)
 - [StopOrFinishWatchingInAMediaCenterRequest](docs/StopOrFinishWatchingInAMediaCenterRequest.md)
 - [UpdateACommentOrReplyRequest](docs/UpdateACommentOrReplyRequest.md)
 - [UpdatePersonalListRequest](docs/UpdatePersonalListRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="oauth2"></a>
### oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: /
- **Scopes**: N/A


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



