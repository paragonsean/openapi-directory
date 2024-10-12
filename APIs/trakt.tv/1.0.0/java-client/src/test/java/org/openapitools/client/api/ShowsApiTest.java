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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ShowsApi
 */
@Disabled
public class ShowsApiTest {

    private final ShowsApi api = new ShowsApi();

    /**
     * Get a single show
     *
     * #### &amp;#10024; Extended Info  Returns a single shows&#39;s details. If you request extended info, the &#x60;airs&#x60; object is relative to the show&#39;s country. You can use the &#x60;day&#x60;, &#x60;time&#x60;, and &#x60;timezone&#x60; to construct your own date then convert it to whatever timezone your user is in.  **Note:** When getting &#x60;full&#x60; extended info, the &#x60;status&#x60; field can have a value of &#x60;returning series&#x60; (airing right now),  &#x60;continuing&#x60; (airing right now), &#x60;in production&#x60; (airing soon), &#x60;planned&#x60; (in development), &#x60;upcoming&#x60; (in development),  &#x60;pilot&#x60;, &#x60;canceled&#x60;, or &#x60;ended&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getASingleShowTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getASingleShow(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get all people for a show
     *
     * #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a show, including the &#x60;episode_count&#x60; for which they appears. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, &#x60;editing&#x60;, and &#x60;created  by&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in at least 1 episode of the show.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAllPeopleForAShowTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getAllPeopleForAShow(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get all show aliases
     *
     * Returns all title aliases for a show.  Includes country where name is different.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAllShowAliasesTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getAllShowAliases(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get all show certifications
     *
     * Returns all content certifications for a show, including the country.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAllShowCertificationsTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getAllShowCertifications(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get all show comments
     *
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a show. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, most &#x60;plays&#x60;, and highest &#x60;watched&#x60; percentage.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAllShowCommentsTest() throws ApiException {
        String id = null;
        String sort = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getAllShowComments(id, sort, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get all show translations
     *
     * Returns all translations for a show, including language and translated values for title and overview.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAllShowTranslationsTest() throws ApiException {
        String id = null;
        String language = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getAllShowTranslations(id, language, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get last episode
     *
     * #### &amp;#10024; Extended Info  Returns the most recently aired episode. If no episode is found, a &#x60;204&#x60; HTTP status code will be returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLastEpisodeTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getLastEpisode(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get lists containing this show
     *
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this show. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getListsContainingThisShowTest() throws ApiException {
        String id = null;
        String type = null;
        String sort = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getListsContainingThisShow(id, type, sort, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get next episode
     *
     * #### &amp;#10024; Extended Info  Returns the next scheduled to air episode. If no episode is found, a &#x60;204&#x60; HTTP status code will be returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNextEpisodeTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getNextEpisode(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get popular shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most popular shows. Popularity is calculated using the rating percentage and the number of ratings.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPopularShowsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getPopularShows(traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get recently updated show Trakt IDs
     *
     * #### &amp;#128196; Pagination  Returns all show Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRecentlyUpdatedShowTraktIDsTest() throws ApiException {
        String startDate = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getRecentlyUpdatedShowTraktIDs(startDate, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get recently updated shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all shows updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRecentlyUpdatedShowsTest() throws ApiException {
        String startDate = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getRecentlyUpdatedShows(startDate, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get related shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns related and similar shows.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRelatedShowsTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getRelatedShows(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get show collection progress
     *
     * #### &amp;#128274; OAuth Required  Returns collection progress for a show including details on all aired seasons and episodes. The &#x60;next_episode&#x60; will be the next episode the user should collect, if there are no upcoming episodes it will be set to &#x60;null&#x60;.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the &#x60;hidden&#x60; flag to &#x60;true&#x60;.  By default, specials will be excluded from the response. Set the &#x60;specials&#x60; flag to &#x60;true&#x60; to include season 0 and adjust the stats accordingly. If you&#39;d like to include specials, but not adjust the stats, set &#x60;count_specials&#x60; to &#x60;false&#x60;.  By default, the &#x60;last_episode&#x60; and &#x60;next_episode&#x60; are calculated using the last &#x60;aired&#x60; episode the user has collected, even if they&#39;ve collected older episodes more recently. To use their last collected episode for these calculations, set the &#x60;last_activity&#x60; flag to &#x60;collected&#x60;.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getShowCollectionProgressTest() throws ApiException {
        String id = null;
        String body = null;
        String hidden = null;
        String specials = null;
        String countSpecials = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getShowCollectionProgress(id, body, hidden, specials, countSpecials, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get show ratings
     *
     * Returns rating (between 0 and 10) and distribution for a show.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getShowRatingsTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getShowRatings(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get show stats
     *
     * Returns lots of show stats.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getShowStatsTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getShowStats(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get show studios
     *
     * Returns all studios for a show.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getShowStudiosTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getShowStudios(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get show watched progress
     *
     * #### &amp;#128274; OAuth Required  Returns watched progress for a show including details on all aired seasons and episodes. The &#x60;next_episode&#x60; will be the next episode the user should watch, if there are no upcoming episodes it will be set to &#x60;null&#x60;. If not &#x60;null&#x60;, the &#x60;reset_at&#x60; date is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the &#x60;hidden&#x60; flag to &#x60;true&#x60;.  By default, specials will be excluded from the response. Set the &#x60;specials&#x60; flag to &#x60;true&#x60; to include season 0 and adjust the stats accordingly. If you&#39;d like to include specials, but not adjust the stats, set &#x60;count_specials&#x60; to &#x60;false&#x60;.  By default, the &#x60;last_episode&#x60; and &#x60;next_episode&#x60; are calculated using the last &#x60;aired&#x60; episode the user has watched, even if they&#39;ve watched older episodes more recently. To use their last watched episode for these calculations, set the &#x60;last_activity&#x60; flag to &#x60;watched&#x60;.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getShowWatchedProgressTest() throws ApiException {
        String id = null;
        String body = null;
        String hidden = null;
        String specials = null;
        String countSpecials = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getShowWatchedProgress(id, body, hidden, specials, countSpecials, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get the most anticipated shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most anticipated shows based on the number of lists a show appears on.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTheMostAnticipatedShowsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getTheMostAnticipatedShows(traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get the most collected shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most collected (unique users) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTheMostCollectedShowsTest() throws ApiException {
        String period = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getTheMostCollectedShows(period, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get the most played shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most played (a single user can watch multiple episodes multiple times) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTheMostPlayedShowsTest() throws ApiException {
        String period = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getTheMostPlayedShows(period, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get the most recommended shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most recommended shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTheMostRecommendedShowsTest() throws ApiException {
        String period = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getTheMostRecommendedShows(period, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get the most watched shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most watched (unique users) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTheMostWatchedShowsTest() throws ApiException {
        String period = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getTheMostWatchedShows(period, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get trending shows
     *
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows being watched right now. Shows with the most users are returned first.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTrendingShowsTest() throws ApiException {
        String traktApiVersion = null;
        String traktApiKey = null;
        api.getTrendingShows(traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Reset show progress
     *
     * #### &amp;#128274; OAuth Required 🔥 VIP Only  Reset a show&#39;s progress when the user started re-watching the show. You can optionally specify the &#x60;reset_at&#x60; date to have it calculate progress from that specific date onwards.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resetShowProgressTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.resetShowProgress(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Get users watching right now
     *
     * #### &amp;#10024; Extended Info  Returns all users watching this show right now.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void showsIdWatchingGetTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.showsIdWatchingGet(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

    /**
     * Undo reset show progress
     *
     * #### &amp;#128274; OAuth Required 🔥 VIP Only  Undo the reset and have watched progress use all watched history for the show.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void undoResetShowProgressTest() throws ApiException {
        String id = null;
        String traktApiVersion = null;
        String traktApiKey = null;
        api.undoResetShowProgress(id, traktApiVersion, traktApiKey);
        // TODO: test validations
    }

}
