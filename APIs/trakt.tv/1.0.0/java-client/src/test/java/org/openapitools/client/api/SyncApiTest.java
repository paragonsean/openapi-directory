/*
 * Trakt API
 * At Trakt, we collect lots of interesting information about what tv shows and movies everyone is watching. Part of the fun with such data is making it available for anyone to mash up and use on their own site or app. The Trakt API was made just for this purpose. It is very easy to use, you basically call a URL and get some JSON back.  More complex API calls (such as adding a movie or show to your collection) involve sending us data. These are still easy to use, you simply POST some JSON data to a specific URL.  Make sure to check out the [**Required Headers**](#introduction/required-headers) and [**Authentication**](#reference/authentication-oauth) sections for more info on what needs to be sent with each API call. Also check out the [**Terminology**](#introduction/terminology) section insight into the features Trakt supports.  # Create an App  To use the Trakt API, you'll need to [**create a new API app**](https://trakt.tv/oauth/applications/new).  # Stay Connected  API discussion and bugs should be posted in the [**GitHub Developer Forum**](https://github.com/trakt/api-help/issues) and *watch* the repository if you'd like to get notifications. Make sure to follow our [**API Blog**](https://apiblog.trakt.tv) and [**@traktapi on Twitter**](https://twitter.com/traktapi) too.  # API URL  The API should always be accessed over SSL.  ``` https://api.trakt.tv ```  If you would like to use our sandbox environment to not fill production with test data, use this URL over SSL. **Note:** Staging is a completely separate environment, so you'll need to [**create a new API app on staging**](https://staging.trakt.tv/oauth/applications/new).  ``` https://api-staging.trakt.tv ```  # Verbs  The API uses restful verbs.  | Verb | Description | |---|---| | `GET` | Select one or more items. Success returns `200` status code. | | `POST` | Create a new item. Success returns `201` status code. | | `PUT` | Update an item. Success returns `200` status code. | | `DELETE` | Delete an item. Success returns `200` or `204` status code. |  # Status Codes  The API will respond with one of the following HTTP status codes.  | Code | Description | |---|---| | `200` | Success | `201` | Success - *new resource created (POST)* | `204` | Success - *no content to return (DELETE)* | `400` | Bad Request - *request couldn't be parsed* | `401` | Unauthorized - *OAuth must be provided* | `403` | Forbidden - *invalid API key or unapproved app* | `404` | Not Found - *method exists, but no record found* | `405` | Method Not Found - *method doesn't exist* | `409` | Conflict - *resource already created* | `412` | Precondition Failed - *use application/json content type* | `420` | Account Limit Exceeded - *list count, item count, etc* | `422` | Unprocessable Entity - *validation errors* | `423` | Locked User Account - *have the user contact support* | `426` | VIP Only - *user must upgrade to VIP* | `429` | Rate Limit Exceeded | `500` | Server Error - *please open a support ticket* | `502` | Service Unavailable - *server overloaded (try again in 30s)* | `503` | Service Unavailable - *server overloaded (try again in 30s)* | `504` | Service Unavailable - *server overloaded (try again in 30s)* | `520` | Service Unavailable - *Cloudflare error* | `521` | Service Unavailable - *Cloudflare error* | `522` | Service Unavailable - *Cloudflare error*  # Required Headers  You'll need to send some headers when making API calls to identify your application, set the version and set the content type to JSON.  | Header | Value | |---|---| | `Content-type` <span style=\"color:red;\">*</a> | `application/json` | | `trakt-api-key` <span style=\"color:red;\">*</a> | Your `client_id` listed under your Trakt applications. | | `trakt-api-version` <span style=\"color:red;\">*</a> | `2` | API version to use.  All `POST`, `PUT`, and `DELETE` methods require a valid OAuth `access_token`. Some `GET` calls require OAuth and others will return user specific data if OAuth is sent. Methods that &#128274; **require** or have &#128275; **optional** OAuth will be indicated.  Your OAuth library should take care of sending the auth headers for you, but for reference here's how the Bearer token should be sent.  | Header | Value | |---|---| | `Authorization` | `Bearer [access_token]` |  # Rate Limiting  All API methods are rate limited. A `429` HTTP status code is returned when the limit has been exceeded. Check the headers for detailed info, then try your API call in `Retry-After` seconds.  | Header | Value | |---|---| | `X-Ratelimit` | `{\"name\":\"UNAUTHED_API_GET_LIMIT\",\"period\":300,\"limit\":1000,\"remaining\":0,\"until\":\"2020-10-10T00:24:00Z\"}` | | `Retry-After` | `10` |  Here are the current limits. There are separate limits for authed (user level) and unauthed (application level) calls. We'll continue to adjust these limits to optimize API performance for everyone. The goal is to prevent API abuse and poor coding, but allow users to use apps normally.  | Name | Verb | Methods | Limit | |---|---|---|---| | `AUTHED_API_POST_LIMIT` | `POST`, `PUT`, `DELETE` | all | 1 call per second | | `AUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes | | `UNAUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes |  # Locked User Account  A `423` HTTP status code is returned when the OAuth user has a locked user account. Please instruct the user to [**contact Trakt support**](https://support.trakt.tv) so we can fix their account. API access will be suspended for the user until we fix their account.  # VIP Methods  Some API methods are tagged 🔥 **VIP Only**. A `426` HTTP status code is returned when the user isn't a VIP, indicating they need to sign up for [**Trakt VIP**](https://trakt.tv/vip) in order to use this method. In your app, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` |  Some API methods are tagged 🔥 **VIP Enhanced**. A `420` HTTP status code is returned when the user has exceeded their account limit. Signing up for [**Trakt VIP**](https://trakt.tv/vip) will increase these limits. If the user isn't a VIP, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP. If they are already VIP and still exceeded the limit, please display a message indicating this.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` | | `X-VIP-User` | `true` or `false` | | `X-Account-Limit` | Limit allowed. |  # Pagination  Some methods are paginated. Methods with &#128196; **Pagination** will load 1 page of 10 items by default. Methods with &#128196; **Pagination Optional** will load all items by default. In either case, append a query string like `?page={page}&limit={limit}` to the URL to influence the results.  | Parameter | Type | Default | Value | |---|---|---|---| | `page` | integer | `1` | Number of page of results to be returned. | | `limit` | integer | `10` | Number of results to return per page. |  All paginated methods will return these HTTP headers.  | Header | Value | |---|---| | `X-Pagination-Page` | Current page. | | `X-Pagination-Limit` | Items per page. | | `X-Pagination-Page-Count` | Total number of pages. | | `X-Pagination-Item-Count` | Total number of items. |  # Extended Info  By default, all methods will return minimal info for movies, shows, episodes, people, and users. Minimal info is typically all you need to match locally cached items and includes the `title`, `year`, and `ids`. However, you can request different extended levels of information by adding `?extended={level}` to the URL. Send a comma separated string to get multiple types of extended info.  **Note:** This returns a lot of extra data, so please only use extended parameters if you actually need them!  | Level | Description | |---|---| | `full` | Complete info for an item. | `metadata` | **Collection only.** Additional video and audio info.  # Filters  Some `movies`, `shows`, `calendars`,  and `search` methods support additional filters and will be tagged with &#127898; **Filters**. Applying these filters refines the results and helps your users to more easily discover new items.  Add a query string (i.e. `?years=2016&genres=action`) with any filters you want to use. Some filters allow multiples which can be sent as comma delimited parameters. For example, `?genres=action,adventure` would match the `action` OR `adventure` genre.  **Note:** Make sure to properly URL encode the parameters including spaces and special characters.  #### Common Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `query` | | `batman` | Search titles and descriptions. | | `years` | | `2016` | 4 digit year or range of years. | | `genres` | &#10003; | `action` | [Genre slugs.](#reference/genres) | | `languages` | &#10003; | `en` | [2 character language code.](#reference/languages) | | `countries` | &#10003; | `us` | [2 character country code.](#reference/countries) | | `runtimes` | | `30-90` | Range in minutes. | | `studios` | &#10003; | `marvel-studios` | Studio slugs. |  #### Rating Filters  Trakt, TMDB, and IMDB ratings apply to `movies`, `shows`, and `episodes`. Rotten Tomatoes and Metacritic apply to `movies`.  | Parameter | Multiples | Example | Value | |---|---|---|---| | `ratings` | | `75-100` | Trakt rating range between `0` and `100`. | | `votes` | | `5000-10000` | Trakt vote count between `0` and `100000`. | | `tmdb_ratings` | | `5.5-10.0` | TMDB rating range between `0.0` and `10.0`. | | `tmdb_votes` | | `5000-10000` | TMDB vote count between `0` and `100000`. | | `imdb_ratings` | | `5.5-10.0` | IMDB rating range between `0.0` and `10.0`. | | `imdb_votes` | | `5000-10000` | IMDB vote count between `0` and `3000000`. | | `rt_meters` | | `5.5-10.0` | Rotten Tomatoes meter range between `0` and `100`. | | `metascores` | | `5.5-10.0` | Metacritic score range between `0` and `100`. |  #### Movie Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `pg-13` | US content certification. |  #### Show Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `tv-pg` | US content certification. | | `networks` | &#10003; | `HBO` | Network name. | | `status` | &#10003; | `ended` | Set to `returning series`, `continuing`, `in production`, `planned`, `upcoming`,  `pilot`, `canceled`, or `ended`. |  # CORS  When creating your API app, specify the JavaScript (CORS) origins you'll be using. We use these origins to return the headers needed for CORS.  # Dates  All dates will be GMT and returned in the ISO 8601 format like `2014-09-01T09:10:11.000Z`. Adjust accordingly in your app for the user's local timezone.  # Emojis  We use short codes for emojis like `:smiley:` and `:raised_hands:` and render them on the Trakt website using [**JoyPixels**](https://www.joypixels.com/) _(verion 6.6.0)_. Methods that support emojis are tagged with &#128513; **Emojis**. For POST methods, you can send standard unicode emojis and we'll automatically convert them to short codes. For GET methods, we'll return the short codes and it's up to your app to convert them back to unicode emojis.  # Standard Media Objects  All methods will accept or return standard media objects for `movie`, `show`, `season`, `episode`, `person`, and `user` items. Here are examples for all minimal objects.  #### movie  ``` {     \"title\": \"Batman Begins\",     \"year\": 2005,     \"ids\": {         \"trakt\": 1,         \"slug\": \"batman-begins-2005\",         \"imdb\": \"tt0372784\",         \"tmdb\": 272     } } ```  #### show  ``` {     \"title\": \"Breaking Bad\",     \"year\": 2008,     \"ids\": {         \"trakt\": 1,         \"slug\": \"breaking-bad\",         \"tvdb\": 81189,         \"imdb\": \"tt0903747\",         \"tmdb\": 1396     } } ```  #### season  ``` {     \"number\": 0,     \"ids\": {         \"trakt\": 1,         \"tvdb\": 439371,         \"tmdb\": 3577     } } ```  #### episode  ``` {     \"season\": 1,     \"number\": 1,     \"title\": \"Pilot\",     \"ids\": {         \"trakt\": 16,         \"tvdb\": 349232,         \"imdb\": \"tt0959621\",         \"tmdb\": 62085     } } ```  #### person  ``` {     \"name\": \"Bryan Cranston\",     \"ids\": {         \"trakt\": 142,         \"slug\": \"bryan-cranston\",         \"imdb\": \"nm0186505\",         \"tmdb\": 17419     } } ```  #### user  ``` {     \"username\": \"sean\",     \"private\": false,     \"name\": \"Sean Rudford\",     \"vip\": true,     \"vip_ep\": true,     \"ids\": {         \"slug\": \"sean\"     } } ```  # Images  The standard media objects for all `movie`, `show`, `season`, `episode`, and `person` items include an `ids` object. These `ids` map to other services like [TMDB](https://www.themoviedb.org), [TVDB](https://thetvdb.com), [Fanart.tv](https://fanart.tv), [IMDB](https://www.imdb.com), and [OMDB](https://www.omdbapi.com/).  Most of these services have free APIs you can use to grab lots of great looking images. Here’s a chart to help you find the best artwork for your app. [**We also wrote an article to help with this.**](https://apiblog.trakt.tv/how-to-find-the-best-images-516045bcc3b6)  | Media | Type | [TMDB](https://developers.themoviedb.org/3) | [TVDB](https://api.thetvdb.com/swagger) | [Fanart.tv](http://docs.fanarttv.apiary.io) | [OMDB](https://www.omdbapi.com) | |---|---|---|---|---|---| | `shows` | `poster` | &#10003; | &#10003; | &#10003; | &#10003; | |  | `fanart` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `seasons` | `poster` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `episodes` | `screenshot` | &#10003; | &#10003; |  |  | | `movies` | `poster` | &#10003; |  | &#10003; | &#10003; | |  | `fanart` | &#10003; |  | &#10003; |  | |  | `banner` |  |  | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `person` | `headshot` | &#10003; |  |  |  | |  | `character` |  | &#10003; |  |  |  # Website Media Links  There are several ways to construct direct links to media on the Trakt website. The website itself uses slugs so the URLs are more readable.  | Type | URL | |---|---| | `movie` | `/movies/:slug` | | `show` | `/shows/:slug` | | `season` | `/shows/:slug/seasons/:num` | | `episode` | `/shows/:slug/seasons/:num/episodes/:num` | | `person` | `/people/:slug` | | `comment` | `/comments/:id` | | `list` | `/lists/:id` |  You can also create links using the Trakt, IMDB, TMDB, or TVDB IDs. We recommend using the Trakt ID if possible since that will always have full coverage. If you use the search url without an `id_type` it will return search results if multiple items are found.  | Type | URL | |---|---| | `trakt` | `/search/trakt/:id` | |  | `/search/trakt/:id?id_type=movie` | |  | `/search/trakt/:id?id_type=show` | |  | `/search/trakt/:id?id_type=season` | |  | `/search/trakt/:id?id_type=episode` | |  | `/search/trakt/:id?id_type=person` | | `imdb` | `/search/imdb/:id` | | `tmdb` | `/search/tmdb/:id` | |  | `/search/tmdb/:id?id_type=movie` | |  | `/search/tmdb/:id?id_type=show` | |  | `/search/tmdb/:id?id_type=episode` | |  | `/search/tmdb/:id?id_type=person` | | `tvdb` | `/search/tvdb/:id` | |  | `/search/tvdb/:id?id_type=show` | |  | `/search/tvdb/:id?id_type=episode` |  # Third Party Libraries  All of the libraries listed below are user contributed. If you find a bug or missing feature, please contact the developer directly. These might help give your project a head start, but we can't provide direct support for any of these libraries. Please help us keep this list up to date.  | Language | Name | Repository | |---|---|---| | `C#` | `Trakt.NET` | https://github.com/henrikfroehling/Trakt.NET | |  | `TraktSharp` | https://github.com/wwarby/TraktSharp | | `C++` | `libtraqt` | https://github.com/RobertMe/libtraqt | | `Clojure` | `clj-trakt` | https://github.com/niamu/clj-trakt | | `Java` | `trakt-java` | https://github.com/UweTrottmann/trakt-java | | `Kotlin` | `trakt-api` | https://github.com/MoviebaseApp/trakt-api | | `Node.js` | `Trakt.tv` | https://github.com/vankasteelj/trakt.tv | |  | `TraktApi2` | https://github.com/PatrickE94/traktapi2 | | `Python` | `trakt.py` | https://github.com/fuzeman/trakt.py | |  | `pyTrakt` | https://github.com/moogar0880/PyTrakt | | `R` | `tRakt` | https://github.com/jemus42/tRakt | | `React Native` | `nodeless-trakt` | https://github.com/kdemoya/nodeless-trakt | | `Ruby` | `omniauth-trakt` | https://github.com/wafcio/omniauth-trakt | |  | `omniauth-trakt` | https://github.com/alextakitani/omniauth-trakt | | `Swift` | `TraktKit` | https://github.com/MaxHasADHD/TraktKit | |  | `AKTrakt` | https://github.com/arsonik/AKTrakt |  # Terminology  Trakt has a lot of features and here's a chart to help explain the differences between some of them.  | Term | Description | |---|---| | `scrobble` | Automatic way to track what a user is watching in a media center. | | `checkin` | Manual action used by mobile apps allowing the user to indicate what they are watching right now. | | `history` | All watched items (scrobbles, checkins, watched) for a user. | | `collection` | Items a user has available to watch including Blu-Rays, DVDs, and digital downloads. | | `watchlist` | Items a user wants to watch in the future. Once watched, they are auto removed from this list. | | `list` | Personal list for any purpose. Items are not auto removed from any personal lists. | | `recommendations` | Movies and TV shows a user personally recommends to others. |
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AddItemsToCollectionRequest;
import org.openapitools.client.model.AddItemsToPersonalRecommendationsRequest;
import org.openapitools.client.model.AddItemsToWatchedHistoryRequest;
import org.openapitools.client.model.AddItemsToWatchlistRequest;
import org.openapitools.client.model.AddNewRatingsRequest;
import org.openapitools.client.model.RemoveItemsFromCollectionRequest;
import org.openapitools.client.model.RemoveItemsFromHistoryRequest;
import org.openapitools.client.model.RemoveItemsFromPersonalRecommendationsRequest;
import org.openapitools.client.model.ReorderPersonallyRecommendedItemsRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SyncApi
 */
@Disabled
public class SyncApiTest {

    private final SyncApi api = new SyncApi();

    /**
     * Add items to collection
     *
     * #### &amp;#128274; OAuth Required  Add items to a user&#39;s collection. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be collected. If seasons are specified, all episodes in those seasons will be collected.  Send a &#x60;collected_at&#x60; UTC datetime to mark items as collected in the past. You can also send additional metadata about the media itself to have a very accurate collection. Showcase what is available to watch from your epic HD DVD collection down to your downloaded iTunes movies.  **Note:** You can resend items already in your collection and they will be updated with any new values. This includes the &#x60;collected_at&#x60; and any other metadata.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60;, &#x60;show&#x60;, or &#x60;episode&#x60; object. | | &#x60;collected_at&#x60; | datetime | UTC datetime when the item was collected. Set to &#x60;released&#x60; to automatically use the inital release date + runtime *(episodes only)*). | | &#x60;media_type&#x60; | string | Set to &#x60;digital&#x60;, &#x60;bluray&#x60;, &#x60;hddvd&#x60;, &#x60;dvd&#x60;, &#x60;vcd&#x60;, &#x60;vhs&#x60;, &#x60;betamax&#x60;, or &#x60;laserdisc&#x60;. | | &#x60;resolution&#x60; | string | Set to &#x60;uhd_4k&#x60;, &#x60;hd_1080p&#x60;, &#x60;hd_1080i&#x60;, &#x60;hd_720p&#x60;, &#x60;sd_480p&#x60;, &#x60;sd_480i&#x60;, &#x60;sd_576p&#x60;, or &#x60;sd_576i&#x60;. | | &#x60;hdr&#x60; | string | Set to &#x60;dolby_vision&#x60;, &#x60;hdr10&#x60;, &#x60;hdr10_plus&#x60;, or &#x60;hlg&#x60;. | | &#x60;audio&#x60; | string | Set to &#x60;dolby_digital&#x60;, &#x60;dolby_digital_plus&#x60;, &#x60;dolby_digital_plus_atmos&#x60;, &#x60;dolby_truehd&#x60;, &#x60;dolby_atmos&#x60; *(Dolby TrueHD Atmos)*, &#x60;dolby_prologic&#x60;, &#x60;dts&#x60;, &#x60;dts_ma&#x60;, &#x60;dts_hr&#x60;, &#x60;dts_x&#x60;, &#x60;auro_3d&#x60;, &#x60;mp3&#x60;, &#x60;mp2&#x60;, &#x60;aac&#x60;, &#x60;lpcm&#x60;, &#x60;ogg&#x60; *(Ogg Vorbis)*, &#x60;ogg_opus&#x60;, &#x60;wma&#x60;, or &#x60;flac&#x60;. | | &#x60;audio_channels&#x60; | string | Set to &#x60;1.0&#x60;, &#x60;2.0&#x60;, &#x60;2.1&#x60;, &#x60;3.0&#x60;, &#x60;3.1&#x60;, &#x60;4.0&#x60;, &#x60;4.1&#x60;, &#x60;5.0&#x60;, &#x60;5.1&#x60;, &#x60;5.1.2&#x60;, &#x60;5.1.4&#x60;, &#x60;6.1&#x60;, &#x60;7.1&#x60;, &#x60;7.1.2&#x60;, &#x60;7.1.4&#x60;, &#x60;9.1&#x60;, or &#x60;10.1&#x60; | | &#x60;3d&#x60; | boolean | Set &#x60;true&#x60; if in 3D. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addItemsToCollectionTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        AddItemsToCollectionRequest addItemsToCollectionRequest = null;
        api.addItemsToCollection(traktApiVersion, traktApiKey, addItemsToCollectionRequest);
        // TODO: test validations
    }

    /**
     * Add items to personal recommendations
     *
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  If the user only had 50 movies and TV shows to bring with them on a desert island, what would they be? These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation can optionally accept a &#x60;notes&#x60; *(255 maximum characters)* field explaining why the user recommended the item.  #### Limits  If the user has recommended 50 items already, a &#x60;420&#x60; HTTP error code is returned. This limit applies to all users.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addItemsToPersonalRecommendationsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        AddItemsToPersonalRecommendationsRequest addItemsToPersonalRecommendationsRequest = null;
        api.addItemsToPersonalRecommendations(traktApiVersion, traktApiKey, addItemsToPersonalRecommendationsRequest);
        // TODO: test validations
    }

    /**
     * Add items to watched history
     *
     * #### &amp;#128274; OAuth Required  Add items to a user&#39;s watch history. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be added. If seasons are specified, only episodes in those seasons will be added.  Send a &#x60;watched_at&#x60; UTC datetime to mark items as watched in the past. This is useful for syncing past watches from a media center.  **Note:** Please be careful with sending duplicate data. We don&#39;t verify the &#x60;item&#x60; + &#x60;watched_at&#x60; to ensure it&#39;s unique, it is up to your app to veify this and not send duplicate plays.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60;, &#x60;show&#x60;, or &#x60;episode&#x60; object. | | &#x60;watched_at&#x60; | datetime | UTC datetime when the item was watched. Set to &#x60;released&#x60; to automatically use the initial release date + runtime *(episodes only)*. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addItemsToWatchedHistoryTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        AddItemsToWatchedHistoryRequest addItemsToWatchedHistoryRequest = null;
        api.addItemsToWatchedHistory(traktApiVersion, traktApiKey, addItemsToWatchedHistoryRequest);
        // TODO: test validations
    }

    /**
     * Add items to watchlist
     *
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis 🔥 VIP Enhanced  Add one of more items to a user&#39;s watchlist. Accepts shows, seasons, episodes and movies. If only a show is passed, only the show itself will be added. If seasons are specified, all of those seasons will be added.  #### Notes  Each watchlist item can optionally accept a &#x60;notes&#x60; *(255 maximum characters)* field with custom text. The user must be a [**Trakt VIP**](https://trakt.tv/vip) to send &#x60;notes&#x60;.  #### Limits  If the user&#39;s watchlist limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addItemsToWatchlistTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        AddItemsToWatchlistRequest addItemsToWatchlistRequest = null;
        api.addItemsToWatchlist(traktApiVersion, traktApiKey, addItemsToWatchlistRequest);
        // TODO: test validations
    }

    /**
     * Add new ratings
     *
     * #### &amp;#128274; OAuth Required  Rate one or more items. Accepts shows, seasons, episodes and movies. If only a show is passed, only the show itself will be rated. If seasons are specified, all of those seasons will be rated.  Send a &#x60;rated_at&#x60; UTC datetime to mark items as rated in the past. This is useful for syncing ratings from a media center.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, or &#x60;episode&#x60; object. | | &#x60;rating&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | integer | Between 1 and 10. | | &#x60;rated_at&#x60; | datetime | UTC datetime when the item was rated. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addNewRatingsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        AddNewRatingsRequest addNewRatingsRequest = null;
        api.addNewRatings(traktApiVersion, traktApiKey, addNewRatingsRequest);
        // TODO: test validations
    }

    /**
     * Get collection
     *
     * #### &amp;#128274; OAuth Required &amp;#10024; Extended Info  Get all collected items in a user&#39;s collection. A collected item indicates availability to watch digitally or on physical media.  Each &#x60;movie&#x60; object contains &#x60;collected_at&#x60; and &#x60;updated_at&#x60; timestamps. Since users can set custom dates when they collected movies, it is possible for &#x60;collected_at&#x60; to be in the past. We also include &#x60;updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movie if you see a newer timestamp.  Each &#x60;show&#x60; object contains &#x60;last_collected_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they collected episodes, it is possible for &#x60;last_collected_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the show if you see a newer timestamp.  If you add &#x60;?extended&#x3D;metadata&#x60; to the URL, it will return the additional &#x60;media_type&#x60;, &#x60;resolution&#x60;, &#x60;hdr&#x60;, &#x60;audio&#x60;, &#x60;audio_channels&#x60; and &#39;3d&#39; metadata. It will use &#x60;null&#x60; if the metadata isn&#39;t set for an item.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCollectionTest() throws ApiException {
        String type = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getCollection(type, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get last activity
     *
     * #### &amp;#128274; OAuth Required  This method is a useful first step in the syncing process. We recommended caching these dates locally, then you can compare to know exactly what data has changed recently. This can greatly optimize your syncs so you don&#39;t pull down a ton of data only to see nothing has actually changed.  #### Account  &#x60;settings_at&#x60; is set when the OAuth user updates any of their Trakt settings on the website. &#x60;followed_at&#x60; is set when another Trakt user follows or unfollows the OAuth user. &#x60;following_at&#x60; is set when the OAuth user follows or unfollows another Trakt user. &#x60;pending_at&#x60; is set when the OAuth user follows a private account, which requires their approval. &#x60;requested_at&#x60; is set when the OAuth user has a private account and someone requests to follow them.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLastActivityTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getLastActivity(traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get personal recommendations
     *
     * #### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  If the user only had 50 movies and TV shows to bring with them on a desert island, what would they be? These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation contains a &#x60;notes&#x60; field explaining why the user recommended the item.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPersonalRecommendationsTest() throws ApiException {
        String type = null;
        String sort = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getPersonalRecommendations(type, sort, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get playback progress
     *
     * #### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional  Whenever a scrobble is paused, the playback progress is saved. Use this progress to sync up playback across different media centers or apps. For example, you can start watching a movie in a media center, stop it, then resume on your tablet from the same spot. Each item will have the &#x60;progress&#x60; percentage between 0 and 100.  You can optionally specify a &#x60;type&#x60; to only get &#x60;movies&#x60; or &#x60;episodes&#x60;.  By default, all results will be returned. Pagination is optional and can be used for something like an \&quot;on deck\&quot; feature, or if you only need a limited data set.  **Note:** We only save playback progress for the last 6 months.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPlaybackProgressTest() throws ApiException {
        String type = null;
        String startAt = null;
        String endAt = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getPlaybackProgress(type, startAt, endAt, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get ratings
     *
     * #### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info  Get a user&#39;s ratings filtered by &#x60;type&#x60;. You can optionally filter for a specific &#x60;rating&#x60; between 1 and 10. Send a comma separated string for &#x60;rating&#x60; if you need multiple ratings.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRatingsTest() throws ApiException {
        String type = null;
        Integer rating = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getRatings(type, rating, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get watched
     *
     * #### &amp;#128274; OAuth Required &amp;#10024; Extended Info  Returns all movies or shows a user has watched sorted by most plays.  If &#x60;type&#x60; is set to _shows_ and you add &#x60;?extended&#x3D;noseasons&#x60; to the URL, it won&#39;t return season or episode info.  Each &#x60;movie&#x60; and &#x60;show&#x60; object contains &#x60;last_watched_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they watched movies and episodes, it is possible for &#x60;last_watched_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movies and shows if you see a newer timestamp.  Each &#x60;show&#x60; object contains a &#x60;reset_at&#x60; timestamp. If not &#x60;null&#x60;, this is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getWatchedTest() throws ApiException {
        String type = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getWatched(type, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get watched history
     *
     * #### &amp;#128274; OAuth Required &amp;#128196; Pagination &amp;#10024; Extended Info  Returns movies and episodes that a user has watched, sorted by most recent. You can optionally limit the &#x60;type&#x60; to &#x60;movies&#x60; or &#x60;episodes&#x60;. The &#x60;id&#x60; _(64-bit integer)_ in each history item uniquely identifies the event and can be used to remove individual events by using the [**_/sync/history/remove**](#reference/sync/remove-from-history/get-watched-history) method. The &#x60;action&#x60; will be set to &#x60;scrobble&#x60;, &#x60;checkin&#x60;, or &#x60;watch&#x60;.  Specify a &#x60;type&#x60; and trakt &#x60;id&#x60; to limit the history for just that item. If the &#x60;id&#x60; is valid, but there is no history, an empty array will be returned.  | Example URL | Returns watches for... | |---|---| | &#x60;/history/movies/12601&#x60; | TRON: Legacy | | &#x60;/history/shows/1388&#x60; | All episodes of Breaking Bad | | &#x60;/history/seasons/3950&#x60; | All episodes of Breaking Bad: Season 1 | | &#x60;/history/episodes/73482&#x60; | Only episode 1 for Breaking Bad: Season 1 |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getWatchedHistoryTest() throws ApiException {
        String type = null;
        Integer id = null;
        String startAt = null;
        String endAt = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getWatchedHistory(type, id, startAt, endAt, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get watchlist
     *
     * #### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all items in a user&#39;s watchlist filtered by type.  #### Notes  Each watchlist item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  By default, all list items are sorted by &#x60;rank&#x60; &#x60;asc&#x60;. We send &#x60;X-Applied-Sort-By&#x60; and &#x60;X-Applied-Sort-How&#x60; headers to indicate how the results are actually being sorted.  We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which indicate the user&#39;s sort preference. Use these to to custom sort the watchlist _**in your app**_ for more advanced sort abilities we can&#39;t do in the API. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, and &#x60;votes&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.  #### Auto Removal  When an item is watched, it will be automatically removed from the watchlist. For shows and seasons, watching 1 episode will remove the entire show or season.  _**The watchlist should not be used as a list of what the user is actively watching.**_  Use a combination of the [**_/sync/watched**](/reference/sync/get-watched) and [**_/shows/:id/progress**](/reference/shows/watched-progress) methods to get what the user is actively watching.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getWatchlistTest() throws ApiException {
        String type = null;
        String sort = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getWatchlist(type, sort, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Remove a playback item
     *
     * #### &amp;#128274; OAuth Required  Remove a playback item from a user&#39;s playback progress list. A &#x60;404&#x60; will be returned if the &#x60;id&#x60; is invalid.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeAPlaybackItemTest() throws ApiException {
        Integer id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.removeAPlaybackItem(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Remove items from collection
     *
     * #### &amp;#128274; OAuth Required  Remove one or more items from a user&#39;s collection.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeItemsFromCollectionTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        RemoveItemsFromCollectionRequest removeItemsFromCollectionRequest = null;
        api.removeItemsFromCollection(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest);
        // TODO: test validations
    }

    /**
     * Remove items from history
     *
     * #### &amp;#128274; OAuth Required  Remove items from a user&#39;s watch history including all watches, scrobbles, and checkins. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be removed. If seasons are specified, only episodes in those seasons will be removed.  You can also send a list of raw history &#x60;ids&#x60; _(64-bit integers)_ to delete single plays from the watched history. The [**_/sync/history**](#reference/sync/get-history) method will return an individual &#x60;id&#x60; _(64-bit integer)_ for each history item.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;ids&#x60; | array | Array of history ids. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeItemsFromHistoryTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        RemoveItemsFromHistoryRequest removeItemsFromHistoryRequest = null;
        api.removeItemsFromHistory(traktApiVersion, traktApiKey, removeItemsFromHistoryRequest);
        // TODO: test validations
    }

    /**
     * Remove items from personal recommendations
     *
     * #### &amp;#128274; OAuth Required  Remove items from a user&#39;s personal recommendations. These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeItemsFromPersonalRecommendationsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        RemoveItemsFromPersonalRecommendationsRequest removeItemsFromPersonalRecommendationsRequest = null;
        api.removeItemsFromPersonalRecommendations(traktApiVersion, traktApiKey, removeItemsFromPersonalRecommendationsRequest);
        // TODO: test validations
    }

    /**
     * Remove items from watchlist
     *
     * #### &amp;#128274; OAuth Required  Remove one or more items from a user&#39;s watchlist.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeItemsFromWatchlistTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        RemoveItemsFromCollectionRequest removeItemsFromCollectionRequest = null;
        api.removeItemsFromWatchlist(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest);
        // TODO: test validations
    }

    /**
     * Remove ratings
     *
     * #### &amp;#128274; OAuth Required  Remove ratings for one or more items.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. |
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeRatingsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        RemoveItemsFromCollectionRequest removeItemsFromCollectionRequest = null;
        api.removeRatings(traktApiVersion, traktApiKey, removeItemsFromCollectionRequest);
        // TODO: test validations
    }

    /**
     * Reorder personally recommended items
     *
     * #### &amp;#128274; OAuth Required  Reorder all items on a user&#39;s personal recommendations by sending the updated &#x60;rank&#x60; of list item ids. Use the [**_/sync/recommendations**](#reference/sync/get-personal-recommendations) method to get all list item ids.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reorderPersonallyRecommendedItemsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        ReorderPersonallyRecommendedItemsRequest reorderPersonallyRecommendedItemsRequest = null;
        api.reorderPersonallyRecommendedItems(traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest);
        // TODO: test validations
    }

    /**
     * Reorder watchlist items
     *
     * #### &amp;#128274; OAuth Required  Reorder all items on a user&#39;s watchlist by sending the updated &#x60;rank&#x60; of list item ids. Use the [**_/sync/watchlist**](#reference/sync/get-watchlist) method to get all list item ids.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reorderWatchlistItemsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        ReorderPersonallyRecommendedItemsRequest reorderPersonallyRecommendedItemsRequest = null;
        api.reorderWatchlistItems(traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest);
        // TODO: test validations
    }

}
