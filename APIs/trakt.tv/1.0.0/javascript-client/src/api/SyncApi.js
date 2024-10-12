/**
 * Trakt API
 * At Trakt, we collect lots of interesting information about what tv shows and movies everyone is watching. Part of the fun with such data is making it available for anyone to mash up and use on their own site or app. The Trakt API was made just for this purpose. It is very easy to use, you basically call a URL and get some JSON back.  More complex API calls (such as adding a movie or show to your collection) involve sending us data. These are still easy to use, you simply POST some JSON data to a specific URL.  Make sure to check out the [**Required Headers**](#introduction/required-headers) and [**Authentication**](#reference/authentication-oauth) sections for more info on what needs to be sent with each API call. Also check out the [**Terminology**](#introduction/terminology) section insight into the features Trakt supports.  # Create an App  To use the Trakt API, you'll need to [**create a new API app**](https://trakt.tv/oauth/applications/new).  # Stay Connected  API discussion and bugs should be posted in the [**GitHub Developer Forum**](https://github.com/trakt/api-help/issues) and *watch* the repository if you'd like to get notifications. Make sure to follow our [**API Blog**](https://apiblog.trakt.tv) and [**@traktapi on Twitter**](https://twitter.com/traktapi) too.  # API URL  The API should always be accessed over SSL.  ``` https://api.trakt.tv ```  If you would like to use our sandbox environment to not fill production with test data, use this URL over SSL. **Note:** Staging is a completely separate environment, so you'll need to [**create a new API app on staging**](https://staging.trakt.tv/oauth/applications/new).  ``` https://api-staging.trakt.tv ```  # Verbs  The API uses restful verbs.  | Verb | Description | |---|---| | `GET` | Select one or more items. Success returns `200` status code. | | `POST` | Create a new item. Success returns `201` status code. | | `PUT` | Update an item. Success returns `200` status code. | | `DELETE` | Delete an item. Success returns `200` or `204` status code. |  # Status Codes  The API will respond with one of the following HTTP status codes.  | Code | Description | |---|---| | `200` | Success | `201` | Success - *new resource created (POST)* | `204` | Success - *no content to return (DELETE)* | `400` | Bad Request - *request couldn't be parsed* | `401` | Unauthorized - *OAuth must be provided* | `403` | Forbidden - *invalid API key or unapproved app* | `404` | Not Found - *method exists, but no record found* | `405` | Method Not Found - *method doesn't exist* | `409` | Conflict - *resource already created* | `412` | Precondition Failed - *use application/json content type* | `420` | Account Limit Exceeded - *list count, item count, etc* | `422` | Unprocessable Entity - *validation errors* | `423` | Locked User Account - *have the user contact support* | `426` | VIP Only - *user must upgrade to VIP* | `429` | Rate Limit Exceeded | `500` | Server Error - *please open a support ticket* | `502` | Service Unavailable - *server overloaded (try again in 30s)* | `503` | Service Unavailable - *server overloaded (try again in 30s)* | `504` | Service Unavailable - *server overloaded (try again in 30s)* | `520` | Service Unavailable - *Cloudflare error* | `521` | Service Unavailable - *Cloudflare error* | `522` | Service Unavailable - *Cloudflare error*  # Required Headers  You'll need to send some headers when making API calls to identify your application, set the version and set the content type to JSON.  | Header | Value | |---|---| | `Content-type` <span style=\"color:red;\">*</a> | `application/json` | | `trakt-api-key` <span style=\"color:red;\">*</a> | Your `client_id` listed under your Trakt applications. | | `trakt-api-version` <span style=\"color:red;\">*</a> | `2` | API version to use.  All `POST`, `PUT`, and `DELETE` methods require a valid OAuth `access_token`. Some `GET` calls require OAuth and others will return user specific data if OAuth is sent. Methods that &#128274; **require** or have &#128275; **optional** OAuth will be indicated.  Your OAuth library should take care of sending the auth headers for you, but for reference here's how the Bearer token should be sent.  | Header | Value | |---|---| | `Authorization` | `Bearer [access_token]` |  # Rate Limiting  All API methods are rate limited. A `429` HTTP status code is returned when the limit has been exceeded. Check the headers for detailed info, then try your API call in `Retry-After` seconds.  | Header | Value | |---|---| | `X-Ratelimit` | `{\"name\":\"UNAUTHED_API_GET_LIMIT\",\"period\":300,\"limit\":1000,\"remaining\":0,\"until\":\"2020-10-10T00:24:00Z\"}` | | `Retry-After` | `10` |  Here are the current limits. There are separate limits for authed (user level) and unauthed (application level) calls. We'll continue to adjust these limits to optimize API performance for everyone. The goal is to prevent API abuse and poor coding, but allow users to use apps normally.  | Name | Verb | Methods | Limit | |---|---|---|---| | `AUTHED_API_POST_LIMIT` | `POST`, `PUT`, `DELETE` | all | 1 call per second | | `AUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes | | `UNAUTHED_API_GET_LIMIT` | `GET` | all | 1000 calls every 5 minutes |  # Locked User Account  A `423` HTTP status code is returned when the OAuth user has a locked user account. Please instruct the user to [**contact Trakt support**](https://support.trakt.tv) so we can fix their account. API access will be suspended for the user until we fix their account.  # VIP Methods  Some API methods are tagged 🔥 **VIP Only**. A `426` HTTP status code is returned when the user isn't a VIP, indicating they need to sign up for [**Trakt VIP**](https://trakt.tv/vip) in order to use this method. In your app, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` |  Some API methods are tagged 🔥 **VIP Enhanced**. A `420` HTTP status code is returned when the user has exceeded their account limit. Signing up for [**Trakt VIP**](https://trakt.tv/vip) will increase these limits. If the user isn't a VIP, please open a browser to `X-Upgrade-URL` so the user can sign up for Trakt VIP. If they are already VIP and still exceeded the limit, please display a message indicating this.  | Header | Value | |---|---| | `X-Upgrade-URL` | `https://trakt.tv/vip` | | `X-VIP-User` | `true` or `false` | | `X-Account-Limit` | Limit allowed. |  # Pagination  Some methods are paginated. Methods with &#128196; **Pagination** will load 1 page of 10 items by default. Methods with &#128196; **Pagination Optional** will load all items by default. In either case, append a query string like `?page={page}&limit={limit}` to the URL to influence the results.  | Parameter | Type | Default | Value | |---|---|---|---| | `page` | integer | `1` | Number of page of results to be returned. | | `limit` | integer | `10` | Number of results to return per page. |  All paginated methods will return these HTTP headers.  | Header | Value | |---|---| | `X-Pagination-Page` | Current page. | | `X-Pagination-Limit` | Items per page. | | `X-Pagination-Page-Count` | Total number of pages. | | `X-Pagination-Item-Count` | Total number of items. |  # Extended Info  By default, all methods will return minimal info for movies, shows, episodes, people, and users. Minimal info is typically all you need to match locally cached items and includes the `title`, `year`, and `ids`. However, you can request different extended levels of information by adding `?extended={level}` to the URL. Send a comma separated string to get multiple types of extended info.  **Note:** This returns a lot of extra data, so please only use extended parameters if you actually need them!  | Level | Description | |---|---| | `full` | Complete info for an item. | `metadata` | **Collection only.** Additional video and audio info.  # Filters  Some `movies`, `shows`, `calendars`,  and `search` methods support additional filters and will be tagged with &#127898; **Filters**. Applying these filters refines the results and helps your users to more easily discover new items.  Add a query string (i.e. `?years=2016&genres=action`) with any filters you want to use. Some filters allow multiples which can be sent as comma delimited parameters. For example, `?genres=action,adventure` would match the `action` OR `adventure` genre.  **Note:** Make sure to properly URL encode the parameters including spaces and special characters.  #### Common Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `query` | | `batman` | Search titles and descriptions. | | `years` | | `2016` | 4 digit year or range of years. | | `genres` | &#10003; | `action` | [Genre slugs.](#reference/genres) | | `languages` | &#10003; | `en` | [2 character language code.](#reference/languages) | | `countries` | &#10003; | `us` | [2 character country code.](#reference/countries) | | `runtimes` | | `30-90` | Range in minutes. | | `studios` | &#10003; | `marvel-studios` | Studio slugs. |  #### Rating Filters  Trakt, TMDB, and IMDB ratings apply to `movies`, `shows`, and `episodes`. Rotten Tomatoes and Metacritic apply to `movies`.  | Parameter | Multiples | Example | Value | |---|---|---|---| | `ratings` | | `75-100` | Trakt rating range between `0` and `100`. | | `votes` | | `5000-10000` | Trakt vote count between `0` and `100000`. | | `tmdb_ratings` | | `5.5-10.0` | TMDB rating range between `0.0` and `10.0`. | | `tmdb_votes` | | `5000-10000` | TMDB vote count between `0` and `100000`. | | `imdb_ratings` | | `5.5-10.0` | IMDB rating range between `0.0` and `10.0`. | | `imdb_votes` | | `5000-10000` | IMDB vote count between `0` and `3000000`. | | `rt_meters` | | `5.5-10.0` | Rotten Tomatoes meter range between `0` and `100`. | | `metascores` | | `5.5-10.0` | Metacritic score range between `0` and `100`. |  #### Movie Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `pg-13` | US content certification. |  #### Show Filters  | Parameter | Multiples | Example | Value | |---|---|---|---| | `certifications` | &#10003; | `tv-pg` | US content certification. | | `networks` | &#10003; | `HBO` | Network name. | | `status` | &#10003; | `ended` | Set to `returning series`, `continuing`, `in production`, `planned`, `upcoming`,  `pilot`, `canceled`, or `ended`. |  # CORS  When creating your API app, specify the JavaScript (CORS) origins you'll be using. We use these origins to return the headers needed for CORS.  # Dates  All dates will be GMT and returned in the ISO 8601 format like `2014-09-01T09:10:11.000Z`. Adjust accordingly in your app for the user's local timezone.  # Emojis  We use short codes for emojis like `:smiley:` and `:raised_hands:` and render them on the Trakt website using [**JoyPixels**](https://www.joypixels.com/) _(verion 6.6.0)_. Methods that support emojis are tagged with &#128513; **Emojis**. For POST methods, you can send standard unicode emojis and we'll automatically convert them to short codes. For GET methods, we'll return the short codes and it's up to your app to convert them back to unicode emojis.  # Standard Media Objects  All methods will accept or return standard media objects for `movie`, `show`, `season`, `episode`, `person`, and `user` items. Here are examples for all minimal objects.  #### movie  ``` {     \"title\": \"Batman Begins\",     \"year\": 2005,     \"ids\": {         \"trakt\": 1,         \"slug\": \"batman-begins-2005\",         \"imdb\": \"tt0372784\",         \"tmdb\": 272     } } ```  #### show  ``` {     \"title\": \"Breaking Bad\",     \"year\": 2008,     \"ids\": {         \"trakt\": 1,         \"slug\": \"breaking-bad\",         \"tvdb\": 81189,         \"imdb\": \"tt0903747\",         \"tmdb\": 1396     } } ```  #### season  ``` {     \"number\": 0,     \"ids\": {         \"trakt\": 1,         \"tvdb\": 439371,         \"tmdb\": 3577     } } ```  #### episode  ``` {     \"season\": 1,     \"number\": 1,     \"title\": \"Pilot\",     \"ids\": {         \"trakt\": 16,         \"tvdb\": 349232,         \"imdb\": \"tt0959621\",         \"tmdb\": 62085     } } ```  #### person  ``` {     \"name\": \"Bryan Cranston\",     \"ids\": {         \"trakt\": 142,         \"slug\": \"bryan-cranston\",         \"imdb\": \"nm0186505\",         \"tmdb\": 17419     } } ```  #### user  ``` {     \"username\": \"sean\",     \"private\": false,     \"name\": \"Sean Rudford\",     \"vip\": true,     \"vip_ep\": true,     \"ids\": {         \"slug\": \"sean\"     } } ```  # Images  The standard media objects for all `movie`, `show`, `season`, `episode`, and `person` items include an `ids` object. These `ids` map to other services like [TMDB](https://www.themoviedb.org), [TVDB](https://thetvdb.com), [Fanart.tv](https://fanart.tv), [IMDB](https://www.imdb.com), and [OMDB](https://www.omdbapi.com/).  Most of these services have free APIs you can use to grab lots of great looking images. Here’s a chart to help you find the best artwork for your app. [**We also wrote an article to help with this.**](https://apiblog.trakt.tv/how-to-find-the-best-images-516045bcc3b6)  | Media | Type | [TMDB](https://developers.themoviedb.org/3) | [TVDB](https://api.thetvdb.com/swagger) | [Fanart.tv](http://docs.fanarttv.apiary.io) | [OMDB](https://www.omdbapi.com) | |---|---|---|---|---|---| | `shows` | `poster` | &#10003; | &#10003; | &#10003; | &#10003; | |  | `fanart` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `seasons` | `poster` | &#10003; | &#10003; | &#10003; |  | |  | `banner` |  | &#10003; | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `episodes` | `screenshot` | &#10003; | &#10003; |  |  | | `movies` | `poster` | &#10003; |  | &#10003; | &#10003; | |  | `fanart` | &#10003; |  | &#10003; |  | |  | `banner` |  |  | &#10003; |  | |  | `logo` |  |  | &#10003; |  | |  | `clearart` |  |  | &#10003; |  | |  | `thumb` |  |  | &#10003; |  | | `person` | `headshot` | &#10003; |  |  |  | |  | `character` |  | &#10003; |  |  |  # Website Media Links  There are several ways to construct direct links to media on the Trakt website. The website itself uses slugs so the URLs are more readable.  | Type | URL | |---|---| | `movie` | `/movies/:slug` | | `show` | `/shows/:slug` | | `season` | `/shows/:slug/seasons/:num` | | `episode` | `/shows/:slug/seasons/:num/episodes/:num` | | `person` | `/people/:slug` | | `comment` | `/comments/:id` | | `list` | `/lists/:id` |  You can also create links using the Trakt, IMDB, TMDB, or TVDB IDs. We recommend using the Trakt ID if possible since that will always have full coverage. If you use the search url without an `id_type` it will return search results if multiple items are found.  | Type | URL | |---|---| | `trakt` | `/search/trakt/:id` | |  | `/search/trakt/:id?id_type=movie` | |  | `/search/trakt/:id?id_type=show` | |  | `/search/trakt/:id?id_type=season` | |  | `/search/trakt/:id?id_type=episode` | |  | `/search/trakt/:id?id_type=person` | | `imdb` | `/search/imdb/:id` | | `tmdb` | `/search/tmdb/:id` | |  | `/search/tmdb/:id?id_type=movie` | |  | `/search/tmdb/:id?id_type=show` | |  | `/search/tmdb/:id?id_type=episode` | |  | `/search/tmdb/:id?id_type=person` | | `tvdb` | `/search/tvdb/:id` | |  | `/search/tvdb/:id?id_type=show` | |  | `/search/tvdb/:id?id_type=episode` |  # Third Party Libraries  All of the libraries listed below are user contributed. If you find a bug or missing feature, please contact the developer directly. These might help give your project a head start, but we can't provide direct support for any of these libraries. Please help us keep this list up to date.  | Language | Name | Repository | |---|---|---| | `C#` | `Trakt.NET` | https://github.com/henrikfroehling/Trakt.NET | |  | `TraktSharp` | https://github.com/wwarby/TraktSharp | | `C++` | `libtraqt` | https://github.com/RobertMe/libtraqt | | `Clojure` | `clj-trakt` | https://github.com/niamu/clj-trakt | | `Java` | `trakt-java` | https://github.com/UweTrottmann/trakt-java | | `Kotlin` | `trakt-api` | https://github.com/MoviebaseApp/trakt-api | | `Node.js` | `Trakt.tv` | https://github.com/vankasteelj/trakt.tv | |  | `TraktApi2` | https://github.com/PatrickE94/traktapi2 | | `Python` | `trakt.py` | https://github.com/fuzeman/trakt.py | |  | `pyTrakt` | https://github.com/moogar0880/PyTrakt | | `R` | `tRakt` | https://github.com/jemus42/tRakt | | `React Native` | `nodeless-trakt` | https://github.com/kdemoya/nodeless-trakt | | `Ruby` | `omniauth-trakt` | https://github.com/wafcio/omniauth-trakt | |  | `omniauth-trakt` | https://github.com/alextakitani/omniauth-trakt | | `Swift` | `TraktKit` | https://github.com/MaxHasADHD/TraktKit | |  | `AKTrakt` | https://github.com/arsonik/AKTrakt |  # Terminology  Trakt has a lot of features and here's a chart to help explain the differences between some of them.  | Term | Description | |---|---| | `scrobble` | Automatic way to track what a user is watching in a media center. | | `checkin` | Manual action used by mobile apps allowing the user to indicate what they are watching right now. | | `history` | All watched items (scrobbles, checkins, watched) for a user. | | `collection` | Items a user has available to watch including Blu-Rays, DVDs, and digital downloads. | | `watchlist` | Items a user wants to watch in the future. Once watched, they are auto removed from this list. | | `list` | Personal list for any purpose. Items are not auto removed from any personal lists. | | `recommendations` | Movies and TV shows a user personally recommends to others. |
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AddItemsToCollectionRequest from '../model/AddItemsToCollectionRequest';
import AddItemsToPersonalRecommendationsRequest from '../model/AddItemsToPersonalRecommendationsRequest';
import AddItemsToWatchedHistoryRequest from '../model/AddItemsToWatchedHistoryRequest';
import AddItemsToWatchlistRequest from '../model/AddItemsToWatchlistRequest';
import AddNewRatingsRequest from '../model/AddNewRatingsRequest';
import RemoveItemsFromCollectionRequest from '../model/RemoveItemsFromCollectionRequest';
import RemoveItemsFromHistoryRequest from '../model/RemoveItemsFromHistoryRequest';
import RemoveItemsFromPersonalRecommendationsRequest from '../model/RemoveItemsFromPersonalRecommendationsRequest';
import ReorderPersonallyRecommendedItemsRequest from '../model/ReorderPersonallyRecommendedItemsRequest';

/**
* Sync service.
* @module api/SyncApi
* @version 1.0.0
*/
export default class SyncApi {

    /**
    * Constructs a new SyncApi. 
    * @alias module:api/SyncApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addItemsToCollection operation.
     * @callback module:api/SyncApi~addItemsToCollectionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add items to collection
     * #### &#128274; OAuth Required  Add items to a user's collection. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be collected. If seasons are specified, all episodes in those seasons will be collected.  Send a `collected_at` UTC datetime to mark items as collected in the past. You can also send additional metadata about the media itself to have a very accurate collection. Showcase what is available to watch from your epic HD DVD collection down to your downloaded iTunes movies.  **Note:** You can resend items already in your collection and they will be updated with any new values. This includes the `collected_at` and any other metadata.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item <span style=\"color:red;\">*</a> | object | `movie`, `show`, or `episode` object. | | `collected_at` | datetime | UTC datetime when the item was collected. Set to `released` to automatically use the inital release date + runtime *(episodes only)*). | | `media_type` | string | Set to `digital`, `bluray`, `hddvd`, `dvd`, `vcd`, `vhs`, `betamax`, or `laserdisc`. | | `resolution` | string | Set to `uhd_4k`, `hd_1080p`, `hd_1080i`, `hd_720p`, `sd_480p`, `sd_480i`, `sd_576p`, or `sd_576i`. | | `hdr` | string | Set to `dolby_vision`, `hdr10`, `hdr10_plus`, or `hlg`. | | `audio` | string | Set to `dolby_digital`, `dolby_digital_plus`, `dolby_digital_plus_atmos`, `dolby_truehd`, `dolby_atmos` *(Dolby TrueHD Atmos)*, `dolby_prologic`, `dts`, `dts_ma`, `dts_hr`, `dts_x`, `auro_3d`, `mp3`, `mp2`, `aac`, `lpcm`, `ogg` *(Ogg Vorbis)*, `ogg_opus`, `wma`, or `flac`. | | `audio_channels` | string | Set to `1.0`, `2.0`, `2.1`, `3.0`, `3.1`, `4.0`, `4.1`, `5.0`, `5.1`, `5.1.2`, `5.1.4`, `6.1`, `7.1`, `7.1.2`, `7.1.4`, `9.1`, or `10.1` | | `3d` | boolean | Set `true` if in 3D. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddItemsToCollectionRequest} [addItemsToCollectionRequest] 
     * @param {module:api/SyncApi~addItemsToCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addItemsToCollection(opts, callback) {
      opts = opts || {};
      let postBody = opts['addItemsToCollectionRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/collection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addItemsToPersonalRecommendations operation.
     * @callback module:api/SyncApi~addItemsToPersonalRecommendationsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add items to personal recommendations
     * #### &#128274; OAuth Required &#128513; Emojis  If the user only had 50 movies and TV shows to bring with them on a desert island, what would they be? These recommendations are used to enchance Trakt's social recommendation algorithm. Apps should encourage user's to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation can optionally accept a `notes` *(255 maximum characters)* field explaining why the user recommended the item.  #### Limits  If the user has recommended 50 items already, a `420` HTTP error code is returned. This limit applies to all users.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddItemsToPersonalRecommendationsRequest} [addItemsToPersonalRecommendationsRequest] 
     * @param {module:api/SyncApi~addItemsToPersonalRecommendationsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addItemsToPersonalRecommendations(opts, callback) {
      opts = opts || {};
      let postBody = opts['addItemsToPersonalRecommendationsRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/recommendations', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addItemsToWatchedHistory operation.
     * @callback module:api/SyncApi~addItemsToWatchedHistoryCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add items to watched history
     * #### &#128274; OAuth Required  Add items to a user's watch history. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be added. If seasons are specified, only episodes in those seasons will be added.  Send a `watched_at` UTC datetime to mark items as watched in the past. This is useful for syncing past watches from a media center.  **Note:** Please be careful with sending duplicate data. We don't verify the `item` + `watched_at` to ensure it's unique, it is up to your app to veify this and not send duplicate plays.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item <span style=\"color:red;\">*</a> | object | `movie`, `show`, or `episode` object. | | `watched_at` | datetime | UTC datetime when the item was watched. Set to `released` to automatically use the initial release date + runtime *(episodes only)*. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddItemsToWatchedHistoryRequest} [addItemsToWatchedHistoryRequest] 
     * @param {module:api/SyncApi~addItemsToWatchedHistoryCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addItemsToWatchedHistory(opts, callback) {
      opts = opts || {};
      let postBody = opts['addItemsToWatchedHistoryRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/history', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addItemsToWatchlist operation.
     * @callback module:api/SyncApi~addItemsToWatchlistCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add items to watchlist
     * #### &#128274; OAuth Required &#128513; Emojis 🔥 VIP Enhanced  Add one of more items to a user's watchlist. Accepts shows, seasons, episodes and movies. If only a show is passed, only the show itself will be added. If seasons are specified, all of those seasons will be added.  #### Notes  Each watchlist item can optionally accept a `notes` *(255 maximum characters)* field with custom text. The user must be a [**Trakt VIP**](https://trakt.tv/vip) to send `notes`.  #### Limits  If the user's watchlist limit is exceeded, a `420` HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddItemsToWatchlistRequest} [addItemsToWatchlistRequest] 
     * @param {module:api/SyncApi~addItemsToWatchlistCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addItemsToWatchlist(opts, callback) {
      opts = opts || {};
      let postBody = opts['addItemsToWatchlistRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/watchlist', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addNewRatings operation.
     * @callback module:api/SyncApi~addNewRatingsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add new ratings
     * #### &#128274; OAuth Required  Rate one or more items. Accepts shows, seasons, episodes and movies. If only a show is passed, only the show itself will be rated. If seasons are specified, all of those seasons will be rated.  Send a `rated_at` UTC datetime to mark items as rated in the past. This is useful for syncing ratings from a media center.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. |  #### Media Object POST Data  | Key | Type | Value | |---|---|---| | item <span style=\"color:red;\">*</a> | object | `movie`, `show`, `season`, or `episode` object. | | `rating` <span style=\"color:red;\">*</a> | integer | Between 1 and 10. | | `rated_at` | datetime | UTC datetime when the item was rated. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddNewRatingsRequest} [addNewRatingsRequest] 
     * @param {module:api/SyncApi~addNewRatingsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addNewRatings(opts, callback) {
      opts = opts || {};
      let postBody = opts['addNewRatingsRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/ratings', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCollection operation.
     * @callback module:api/SyncApi~getCollectionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get collection
     * #### &#128274; OAuth Required &#10024; Extended Info  Get all collected items in a user's collection. A collected item indicates availability to watch digitally or on physical media.  Each `movie` object contains `collected_at` and `updated_at` timestamps. Since users can set custom dates when they collected movies, it is possible for `collected_at` to be in the past. We also include `updated_at` to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movie if you see a newer timestamp.  Each `show` object contains `last_collected_at` and `last_updated_at` timestamps. Since users can set custom dates when they collected episodes, it is possible for `last_collected_at` to be in the past. We also include `last_updated_at` to help sync Trakt data with your app. Cache this timestamp locally and only re-process the show if you see a newer timestamp.  If you add `?extended=metadata` to the URL, it will return the additional `media_type`, `resolution`, `hdr`, `audio`, `audio_channels` and '3d' metadata. It will use `null` if the metadata isn't set for an item.
     * @param {module:model/String} type 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getCollection(type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getCollection");
      }

      let pathParams = {
        'type': type
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/collection/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLastActivity operation.
     * @callback module:api/SyncApi~getLastActivityCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get last activity
     * #### &#128274; OAuth Required  This method is a useful first step in the syncing process. We recommended caching these dates locally, then you can compare to know exactly what data has changed recently. This can greatly optimize your syncs so you don't pull down a ton of data only to see nothing has actually changed.  #### Account  `settings_at` is set when the OAuth user updates any of their Trakt settings on the website. `followed_at` is set when another Trakt user follows or unfollows the OAuth user. `following_at` is set when the OAuth user follows or unfollows another Trakt user. `pending_at` is set when the OAuth user follows a private account, which requires their approval. `requested_at` is set when the OAuth user has a private account and someone requests to follow them.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getLastActivityCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getLastActivity(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/last_activities', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPersonalRecommendations operation.
     * @callback module:api/SyncApi~getPersonalRecommendationsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get personal recommendations
     * #### &#128274; OAuth Required &#128196; Pagination Optional &#10024; Extended Info &#128513; Emojis  If the user only had 50 movies and TV shows to bring with them on a desert island, what would they be? These recommendations are used to enchance Trakt's social recommendation algorithm. Apps should encourage user's to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation contains a `notes` field explaining why the user recommended the item.
     * @param {module:model/String} type Filter for a specific item type
     * @param {module:model/String} sort How to sort (only if type is also sent)
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getPersonalRecommendationsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getPersonalRecommendations(type, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getPersonalRecommendations");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling getPersonalRecommendations");
      }

      let pathParams = {
        'type': type,
        'sort': sort
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/recommendations/{type}/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPlaybackProgress operation.
     * @callback module:api/SyncApi~getPlaybackProgressCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get playback progress
     * #### &#128274; OAuth Required &#128196; Pagination Optional  Whenever a scrobble is paused, the playback progress is saved. Use this progress to sync up playback across different media centers or apps. For example, you can start watching a movie in a media center, stop it, then resume on your tablet from the same spot. Each item will have the `progress` percentage between 0 and 100.  You can optionally specify a `type` to only get `movies` or `episodes`.  By default, all results will be returned. Pagination is optional and can be used for something like an \"on deck\" feature, or if you only need a limited data set.  **Note:** We only save playback progress for the last 6 months.
     * @param {module:model/String} type 
     * @param {Object} opts Optional parameters
     * @param {String} [startAt] Starting date.
     * @param {String} [endAt] Ending date.
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getPlaybackProgressCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getPlaybackProgress(type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getPlaybackProgress");
      }

      let pathParams = {
        'type': type
      };
      let queryParams = {
        'start_at': opts['startAt'],
        'end_at': opts['endAt']
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/playback/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRatings operation.
     * @callback module:api/SyncApi~getRatingsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get ratings
     * #### &#128274; OAuth Required &#128196; Pagination Optional &#10024; Extended Info  Get a user's ratings filtered by `type`. You can optionally filter for a specific `rating` between 1 and 10. Send a comma separated string for `rating` if you need multiple ratings.
     * @param {module:model/String} type 
     * @param {module:model/Number} rating Filter for a specific rating.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getRatingsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getRatings(type, rating, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getRatings");
      }
      // verify the required parameter 'rating' is set
      if (rating === undefined || rating === null) {
        throw new Error("Missing the required parameter 'rating' when calling getRatings");
      }

      let pathParams = {
        'type': type,
        'rating': rating
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/ratings/{type}/{rating}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWatched operation.
     * @callback module:api/SyncApi~getWatchedCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get watched
     * #### &#128274; OAuth Required &#10024; Extended Info  Returns all movies or shows a user has watched sorted by most plays.  If `type` is set to _shows_ and you add `?extended=noseasons` to the URL, it won't return season or episode info.  Each `movie` and `show` object contains `last_watched_at` and `last_updated_at` timestamps. Since users can set custom dates when they watched movies and episodes, it is possible for `last_watched_at` to be in the past. We also include `last_updated_at` to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movies and shows if you see a newer timestamp.  Each `show` object contains a `reset_at` timestamp. If not `null`, this is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a `last_watched_at` prior to the `reset_at`.
     * @param {module:model/String} type 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getWatchedCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getWatched(type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getWatched");
      }

      let pathParams = {
        'type': type
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/watched/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWatchedHistory operation.
     * @callback module:api/SyncApi~getWatchedHistoryCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get watched history
     * #### &#128274; OAuth Required &#128196; Pagination &#10024; Extended Info  Returns movies and episodes that a user has watched, sorted by most recent. You can optionally limit the `type` to `movies` or `episodes`. The `id` _(64-bit integer)_ in each history item uniquely identifies the event and can be used to remove individual events by using the [**_/sync/history/remove**](#reference/sync/remove-from-history/get-watched-history) method. The `action` will be set to `scrobble`, `checkin`, or `watch`.  Specify a `type` and trakt `id` to limit the history for just that item. If the `id` is valid, but there is no history, an empty array will be returned.  | Example URL | Returns watches for... | |---|---| | `/history/movies/12601` | TRON: Legacy | | `/history/shows/1388` | All episodes of Breaking Bad | | `/history/seasons/3950` | All episodes of Breaking Bad: Season 1 | | `/history/episodes/73482` | Only episode 1 for Breaking Bad: Season 1 |
     * @param {module:model/String} type 
     * @param {Number} id Trakt ID for a specific item.
     * @param {Object} opts Optional parameters
     * @param {String} [startAt] Starting date.
     * @param {String} [endAt] Ending date.
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getWatchedHistoryCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getWatchedHistory(type, id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getWatchedHistory");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getWatchedHistory");
      }

      let pathParams = {
        'type': type,
        'id': id
      };
      let queryParams = {
        'start_at': opts['startAt'],
        'end_at': opts['endAt']
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/history/{type}/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWatchlist operation.
     * @callback module:api/SyncApi~getWatchlistCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get watchlist
     * #### &#128274; OAuth Required &#128196; Pagination Optional &#10024; Extended Info &#128513; Emojis  Returns all items in a user's watchlist filtered by type.  #### Notes  Each watchlist item contains a `notes` field with text entered by the user.  #### Sorting Headers  By default, all list items are sorted by `rank` `asc`. We send `X-Applied-Sort-By` and `X-Applied-Sort-How` headers to indicate how the results are actually being sorted.  We also send `X-Sort-By` and `X-Sort-How` headers which indicate the user's sort preference. Use these to to custom sort the watchlist _**in your app**_ for more advanced sort abilities we can't do in the API. Values for `X-Sort-By` include `rank`, `added`, `title`, `released`, `runtime`, `popularity`, `percentage`, and `votes`. Values for `X-Sort-How` include `asc` and `desc`.  #### Auto Removal  When an item is watched, it will be automatically removed from the watchlist. For shows and seasons, watching 1 episode will remove the entire show or season.  _**The watchlist should not be used as a list of what the user is actively watching.**_  Use a combination of the [**_/sync/watched**](/reference/sync/get-watched) and [**_/shows/:id/progress**](/reference/shows/watched-progress) methods to get what the user is actively watching.
     * @param {module:model/String} type Filter for a specific item type
     * @param {module:model/String} sort How to sort (only if type is also sent)
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~getWatchlistCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getWatchlist(type, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getWatchlist");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling getWatchlist");
      }

      let pathParams = {
        'type': type,
        'sort': sort
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/watchlist/{type}/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeAPlaybackItem operation.
     * @callback module:api/SyncApi~removeAPlaybackItemCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove a playback item
     * #### &#128274; OAuth Required  Remove a playback item from a user's playback progress list. A `404` will be returned if the `id` is invalid.
     * @param {Number} id playback ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/SyncApi~removeAPlaybackItemCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeAPlaybackItem(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling removeAPlaybackItem");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/playback/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeItemsFromCollection operation.
     * @callback module:api/SyncApi~removeItemsFromCollectionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove items from collection
     * #### &#128274; OAuth Required  Remove one or more items from a user's collection.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/RemoveItemsFromCollectionRequest} [removeItemsFromCollectionRequest] 
     * @param {module:api/SyncApi~removeItemsFromCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeItemsFromCollection(opts, callback) {
      opts = opts || {};
      let postBody = opts['removeItemsFromCollectionRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/collection/remove', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeItemsFromHistory operation.
     * @callback module:api/SyncApi~removeItemsFromHistoryCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove items from history
     * #### &#128274; OAuth Required  Remove items from a user's watch history including all watches, scrobbles, and checkins. Accepts shows, seasons, episodes and movies. If only a show is passed, all episodes for the show will be removed. If seasons are specified, only episodes in those seasons will be removed.  You can also send a list of raw history `ids` _(64-bit integers)_ to delete single plays from the watched history. The [**_/sync/history**](#reference/sync/get-history) method will return an individual `id` _(64-bit integer)_ for each history item.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. | | `ids` | array | Array of history ids. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/RemoveItemsFromHistoryRequest} [removeItemsFromHistoryRequest] 
     * @param {module:api/SyncApi~removeItemsFromHistoryCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeItemsFromHistory(opts, callback) {
      opts = opts || {};
      let postBody = opts['removeItemsFromHistoryRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/history/remove', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeItemsFromPersonalRecommendations operation.
     * @callback module:api/SyncApi~removeItemsFromPersonalRecommendationsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove items from personal recommendations
     * #### &#128274; OAuth Required  Remove items from a user's personal recommendations. These recommendations are used to enchance Trakt's social recommendation algorithm. Apps should encourage user's to build their personal recommendations so the algorithm keeps getting better.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/RemoveItemsFromPersonalRecommendationsRequest} [removeItemsFromPersonalRecommendationsRequest] 
     * @param {module:api/SyncApi~removeItemsFromPersonalRecommendationsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeItemsFromPersonalRecommendations(opts, callback) {
      opts = opts || {};
      let postBody = opts['removeItemsFromPersonalRecommendationsRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/recommendations/remove', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeItemsFromWatchlist operation.
     * @callback module:api/SyncApi~removeItemsFromWatchlistCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove items from watchlist
     * #### &#128274; OAuth Required  Remove one or more items from a user's watchlist.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/RemoveItemsFromCollectionRequest} [removeItemsFromCollectionRequest] 
     * @param {module:api/SyncApi~removeItemsFromWatchlistCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeItemsFromWatchlist(opts, callback) {
      opts = opts || {};
      let postBody = opts['removeItemsFromCollectionRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/watchlist/remove', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeRatings operation.
     * @callback module:api/SyncApi~removeRatingsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove ratings
     * #### &#128274; OAuth Required  Remove ratings for one or more items.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. |
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/RemoveItemsFromCollectionRequest} [removeItemsFromCollectionRequest] 
     * @param {module:api/SyncApi~removeRatingsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeRatings(opts, callback) {
      opts = opts || {};
      let postBody = opts['removeItemsFromCollectionRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/ratings/remove', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reorderPersonallyRecommendedItems operation.
     * @callback module:api/SyncApi~reorderPersonallyRecommendedItemsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reorder personally recommended items
     * #### &#128274; OAuth Required  Reorder all items on a user's personal recommendations by sending the updated `rank` of list item ids. Use the [**_/sync/recommendations**](#reference/sync/get-personal-recommendations) method to get all list item ids.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/ReorderPersonallyRecommendedItemsRequest} [reorderPersonallyRecommendedItemsRequest] 
     * @param {module:api/SyncApi~reorderPersonallyRecommendedItemsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reorderPersonallyRecommendedItems(opts, callback) {
      opts = opts || {};
      let postBody = opts['reorderPersonallyRecommendedItemsRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/recommendations/reorder', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reorderWatchlistItems operation.
     * @callback module:api/SyncApi~reorderWatchlistItemsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reorder watchlist items
     * #### &#128274; OAuth Required  Reorder all items on a user's watchlist by sending the updated `rank` of list item ids. Use the [**_/sync/watchlist**](#reference/sync/get-watchlist) method to get all list item ids.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/ReorderPersonallyRecommendedItemsRequest} [reorderPersonallyRecommendedItemsRequest] 
     * @param {module:api/SyncApi~reorderWatchlistItemsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reorderWatchlistItems(opts, callback) {
      opts = opts || {};
      let postBody = opts['reorderPersonallyRecommendedItemsRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/sync/watchlist/reorder', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
