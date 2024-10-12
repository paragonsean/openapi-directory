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
import AddHiddenItemsRequest from '../model/AddHiddenItemsRequest';
import AddItemsToPersonalListRequest from '../model/AddItemsToPersonalListRequest';
import CreatePersonalListRequest from '../model/CreatePersonalListRequest';
import RemoveItemsFromPersonalListRequest from '../model/RemoveItemsFromPersonalListRequest';
import ReorderAUserSListsRequest from '../model/ReorderAUserSListsRequest';
import ReorderPersonallyRecommendedItemsRequest from '../model/ReorderPersonallyRecommendedItemsRequest';
import UpdatePersonalListRequest from '../model/UpdatePersonalListRequest';

/**
* Users service.
* @module api/UsersApi
* @version 1.0.0
*/
export default class UsersApi {

    /**
    * Constructs a new UsersApi. 
    * @alias module:api/UsersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addHiddenItems operation.
     * @callback module:api/UsersApi~addHiddenItemsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add hidden items
     * #### &#128274; OAuth Required  Hide items for a specific section. Here's what type of items can hidden for each section.  #### Hideable Media Objects  | Section | Objects | |---|---|---| | `calendar` | `movie`, `show` | | `progress_watched` | `show`, `season` | | `progress_collected` | `show`, `season` | | `recommendations` | `movie`, `show` | | `comments` | `user` |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `users` | array | Array of `user` objects. |
     * @param {module:model/String} section 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddHiddenItemsRequest} [addHiddenItemsRequest] 
     * @param {module:api/UsersApi~addHiddenItemsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addHiddenItems(section, opts, callback) {
      opts = opts || {};
      let postBody = opts['addHiddenItemsRequest'];
      // verify the required parameter 'section' is set
      if (section === undefined || section === null) {
        throw new Error("Missing the required parameter 'section' when calling addHiddenItems");
      }

      let pathParams = {
        'section': section
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
        '/users/hidden/{section}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addItemsToPersonalList operation.
     * @callback module:api/UsersApi~addItemsToPersonalListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add items to personal list
     * #### &#128274; OAuth Required &#128513; Emojis 🔥 VIP Enhanced  Add one or more items to a personal list. Items can be movies, shows, seasons, episodes, or people.  #### Notes  Each list item can optionally accept a `notes` *(255 maximum characters)* field with custom text. The user must be a [**Trakt VIP**](https://trakt.tv/vip) to send `notes`.  #### Limits  If the user's list item limit is exceeded, a `420` HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. | | `people` | array | Array of `person` objects. |
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddItemsToPersonalListRequest} [addItemsToPersonalListRequest] 
     * @param {module:api/UsersApi~addItemsToPersonalListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addItemsToPersonalList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = opts['addItemsToPersonalListRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling addItemsToPersonalList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling addItemsToPersonalList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
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
        '/users/{id}/lists/{list_id}/items', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the approveFollowRequest operation.
     * @callback module:api/UsersApi~approveFollowRequestCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Approve follow request
     * #### &#128274; OAuth Required  Approve a follower using the `id` of the request. If the `id` is not found, was already approved, or was already denied, a `404` error will be returned.
     * @param {String} id ID of the follower request.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~approveFollowRequestCallback} callback The callback function, accepting three arguments: error, data, response
     */
    approveFollowRequest(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling approveFollowRequest");
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
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/requests/{id}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPersonalList operation.
     * @callback module:api/UsersApi~createPersonalListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create personal list
     * #### &#128274; OAuth Required 🔥 VIP Enhanced  Create a new personal list. The `name` is the only required field, but the other info is recommended to ask for.  #### Limits  If the user's list limit is exceeded, a `420` HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### Privacy  Lists will be `private` by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | `private` | Only you can see the list. | | `link` | Anyone with the `share_link` can see the list. | | `friends` | Only your friends can see the list. | | `public` | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | `name` <span style=\"color:red;\">*</a> | string |  | Name of the list. | | `description` | string |  | Description for this list. | | `privacy` | string | `private` | `private`, `link`, `friends`, `public` | | `display_numbers` | boolean | `false` | Should each item be numbered? | | `allow_comments` | boolean | `true` | Are comments allowed? | | `sort_by` | string | `rank` | `rank`, `added`, `title`, `released`, `runtime`, `popularity`, `percentage`, `votes`, `my_rating`, `random`, `watched`, `collected` | | `sort_how` | string | `asc` | `asc`, `desc` |
     * @param {String} id Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/CreatePersonalListRequest} [createPersonalListRequest] 
     * @param {module:api/UsersApi~createPersonalListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    createPersonalList(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['createPersonalListRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling createPersonalList");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteAUsersPersonalList operation.
     * @callback module:api/UsersApi~deleteAUsersPersonalListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a user's personal list
     * #### &#128274; OAuth Required  Remove a personal list and all items it contains.
     * @param {String} id Automatically added
     * @param {String} listId Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~deleteAUsersPersonalListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteAUsersPersonalList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteAUsersPersonalList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling deleteAUsersPersonalList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
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
        '/users/{id}/lists/{list_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the denyFollowRequest operation.
     * @callback module:api/UsersApi~denyFollowRequestCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deny follow request
     * #### &#128274; OAuth Required  Deny a follower using the `id` of the request. If the `id` is not found, was already approved, or was already denied, a `404` error will be returned.
     * @param {String} id Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~denyFollowRequestCallback} callback The callback function, accepting three arguments: error, data, response
     */
    denyFollowRequest(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling denyFollowRequest");
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
        '/users/requests/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the followThisUser operation.
     * @callback module:api/UsersApi~followThisUserCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Follow this user
     * #### &#128274; OAuth Required  If the user has a private profile, the follow request will require approval (`approved_at` will be null). If a user is public, they will be followed immediately (`approved_at` will have a date).  **Note:** If this user is already being followed, a `409` HTTP status code will returned.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~followThisUserCallback} callback The callback function, accepting three arguments: error, data, response
     */
    followThisUser(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling followThisUser");
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
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/follow', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAUsersPersonalLists operation.
     * @callback module:api/UsersApi~getAUsersPersonalListsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a user's personal lists
     * #### &#128275; OAuth Optional &#128513; Emojis  Returns all personal lists for a user. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items a specific list contains.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getAUsersPersonalListsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAUsersPersonalLists(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAUsersPersonalLists");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllListsAUserCanCollaborateOn operation.
     * @callback module:api/UsersApi~getAllListsAUserCanCollaborateOnCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all lists a user can collaborate on
     * #### &#128275; OAuth Optional  Returns all lists a user can collaborate on. This gives full access to add, remove, and re-order list items. It essentially works just like a list owned by the user, just make sure to use the correct list owner `user` when building the API URLs.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getAllListsAUserCanCollaborateOnCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllListsAUserCanCollaborateOn(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllListsAUserCanCollaborateOn");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists/collaborations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getComments operation.
     * @callback module:api/UsersApi~getCommentsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get comments
     * #### &#128275; OAuth Optional &#128196; Pagination &#10024; Extended Info  Returns the most recently written comments for the user. You can optionally filter by the `comment_type` and media `type` to limit what gets returned.  By default, only top level comments are returned. Set `?include_replies=true` to return replies in addition to top level comments. Set `?include_replies=only` to return only replies and no top level comments.
     * @param {String} id User slug
     * @param {module:model/String} commentType 
     * @param {module:model/String} type 
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [includeReplies] include comment replies
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getCommentsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getComments(id, commentType, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getComments");
      }
      // verify the required parameter 'commentType' is set
      if (commentType === undefined || commentType === null) {
        throw new Error("Missing the required parameter 'commentType' when calling getComments");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getComments");
      }

      let pathParams = {
        'id': id,
        'comment_type': commentType,
        'type': type
      };
      let queryParams = {
        'include_replies': opts['includeReplies']
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/comments/{comment_type}/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFollowRequests operation.
     * @callback module:api/UsersApi~getFollowRequestsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get follow requests
     * #### &#128274; OAuth Required &#10024; Extended Info  List a user's pending follow requests so they can either approve or deny them.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getFollowRequestsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getFollowRequests(opts, callback) {
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
        '/users/requests', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFollowers operation.
     * @callback module:api/UsersApi~getFollowersCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get followers
     * #### &#128275; OAuth Optional &#10024; Extended Info  Returns all followers including when the relationship began.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getFollowersCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getFollowers(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getFollowers");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/followers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFollowing operation.
     * @callback module:api/UsersApi~getFollowingCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get following
     * #### &#128275; OAuth Optional &#10024; Extended Info  Returns all user's they follow including when the relationship began.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getFollowingCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getFollowing(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getFollowing");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/following', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFriends operation.
     * @callback module:api/UsersApi~getFriendsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get friends
     * #### &#128275; OAuth Optional &#10024; Extended Info  Returns all friends for a user including when the relationship began. Friendship is a 2 way relationship where each user follows the other.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getFriendsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getFriends(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getFriends");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/friends', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getHiddenItems operation.
     * @callback module:api/UsersApi~getHiddenItemsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get hidden items
     * #### &#128274; OAuth Required &#128196; Pagination &#10024; Extended Info  Get hidden items for a section. This will return an array of standard media objects. You can optionally limit the `type` of results to return.
     * @param {module:model/String} section 
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [type] Narrow down by element type.
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getHiddenItemsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getHiddenItems(section, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'section' is set
      if (section === undefined || section === null) {
        throw new Error("Missing the required parameter 'section' when calling getHiddenItems");
      }

      let pathParams = {
        'section': section
      };
      let queryParams = {
        'type': opts['type']
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
        '/users/hidden/{section}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getItemsOnAPersonalList operation.
     * @callback module:api/UsersApi~getItemsOnAPersonalListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get items on a personal list
     * #### &#128275; OAuth Optional &#128196; Pagination Optional &#10024; Extended Info &#128513; Emojis  Get all items on a personal list. Items can be a `movie`, `show`, `season`, `episode`, or `person`. You can optionally specify the `type` parameter with a single value or comma delimited string for multiple item types.  #### Notes  Each list item contains a `notes` field with text entered by the user.  #### Sorting Headers  All list items are sorted by ascending `rank`. We also send `X-Sort-By` and `X-Sort-How` headers which can be used to custom sort the list _**in your app**_ based on the user's preference. Values for `X-Sort-By` include `rank`, `added`, `title`, `released`, `runtime`, `popularity`, `percentage`, `votes`, `my_rating`, `random`, `watched`, and `collected`. Values for `X-Sort-How` include `asc` and `desc`.
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {module:model/String} type Filter for a specific item type
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getItemsOnAPersonalListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getItemsOnAPersonalList(id, listId, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getItemsOnAPersonalList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling getItemsOnAPersonalList");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getItemsOnAPersonalList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId,
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists/{list_id}/items/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLikes operation.
     * @callback module:api/UsersApi~getLikesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get likes
     * #### &#128274; OAuth Optional &#128196; Pagination  Get items a user likes. This will return an array of standard media objects. You can optionally limit the `type` of results to return.  #### Comment Media Objects  If you add `?extended=comments` to the URL, it will return media objects for each comment like.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!
     * @param {String} id User slug
     * @param {module:model/String} type 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getLikesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getLikes(id, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getLikes");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getLikes");
      }

      let pathParams = {
        'id': id,
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
        '/users/{id}/likes/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPendingFollowingRequests operation.
     * @callback module:api/UsersApi~getPendingFollowingRequestsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get pending following requests
     * #### &#128274; OAuth Required &#10024; Extended Info  List a user's pending following requests that they're waiting for the other user's to approve.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getPendingFollowingRequestsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getPendingFollowingRequests(opts, callback) {
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
        '/users/requests/following', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPersonalList operation.
     * @callback module:api/UsersApi~getPersonalListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get personal list
     * #### &#128275; OAuth Optional &#128513; Emojis  Returns a single personal list. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items this list contains.
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getPersonalListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getPersonalList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getPersonalList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling getPersonalList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists/{list_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSavedFilters operation.
     * @callback module:api/UsersApi~getSavedFiltersCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get saved filters
     * #### &#128274; OAuth Required &#128196; Pagination 🔥 VIP Only  Get all saved filters a user has created. The `path` and `query` can be used to construct an API path to retrieve the saved data. Think of this like a dynamically updated list.
     * @param {module:model/String} section 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getSavedFiltersCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getSavedFilters(section, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'section' is set
      if (section === undefined || section === null) {
        throw new Error("Missing the required parameter 'section' when calling getSavedFilters");
      }

      let pathParams = {
        'section': section
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
        '/users/saved_filters/{section}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getStats operation.
     * @callback module:api/UsersApi~getStatsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get stats
     * #### &#128275; OAuth Optional  Returns stats about the movies, shows, and episodes a user has watched, collected, and rated.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getStatsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getStats(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getStats");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/stats', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUserProfile operation.
     * @callback module:api/UsersApi~getUserProfileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get user profile
     * #### &#128275; OAuth Optional &#10024; Extended Info  Get a user's profile information. If the user is private, info will only be returned if you send OAuth and are either that user or an approved follower. Adding `?extended=vip` will return some additional VIP related fields so you can display the user's Trakt VIP status and year count.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getUserProfileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getUserProfile(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getUserProfile");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWatching operation.
     * @callback module:api/UsersApi~getWatchingCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get watching
     * #### &#128275; OAuth Optional &#10024; Extended Info  Returns a movie or episode if the user is currently watching something.  If they are not, it returns no data and a `204` HTTP status code.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~getWatchingCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getWatching(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getWatching");
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/watching', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the likeAList operation.
     * @callback module:api/UsersApi~likeAListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Like a list
     * #### &#128274; OAuth Required  Votes help determine popular lists. Only one like is allowed per list per user.
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~likeAListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    likeAList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling likeAList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling likeAList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
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
        '/users/{id}/lists/{list_id}/like', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeHiddenItems operation.
     * @callback module:api/UsersApi~removeHiddenItemsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove hidden items
     * #### &#128274; OAuth Required  Unhide items for a specific section. Here's what type of items can unhidden for each section.  #### Unhideable Media Objects  | Section | Objects | |---|---|---| | `calendar` | `movie`, `show` | | `progress_watched` | `show`, `season` | | `progress_collected` | `show`, `season` | | `recommendations` | `movie`, `show` | | `comments` | `user` |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `users` | array | Array of `user` objects. |
     * @param {module:model/String} section 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/AddHiddenItemsRequest} [addHiddenItemsRequest] 
     * @param {module:api/UsersApi~removeHiddenItemsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeHiddenItems(section, opts, callback) {
      opts = opts || {};
      let postBody = opts['addHiddenItemsRequest'];
      // verify the required parameter 'section' is set
      if (section === undefined || section === null) {
        throw new Error("Missing the required parameter 'section' when calling removeHiddenItems");
      }

      let pathParams = {
        'section': section
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
        '/users/hidden/{section}/remove', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeItemsFromPersonalList operation.
     * @callback module:api/UsersApi~removeItemsFromPersonalListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove items from personal list
     * #### &#128274; OAuth Required  Remove one or more items from a personal list.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | `movies` | array | Array of `movie` objects. (see examples &#8594;) | | `shows` | array | Array of `show` objects. | | `seasons` | array | Array of `season` objects. | | `episodes` | array | Array of `episode` objects. | | `people` | array | Array of `person` objects. |
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/RemoveItemsFromPersonalListRequest} [removeItemsFromPersonalListRequest] 
     * @param {module:api/UsersApi~removeItemsFromPersonalListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeItemsFromPersonalList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = opts['removeItemsFromPersonalListRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling removeItemsFromPersonalList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling removeItemsFromPersonalList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
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
        '/users/{id}/lists/{list_id}/items/remove', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeLikeOnAList operation.
     * @callback module:api/UsersApi~removeLikeOnAListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove like on a list
     * #### &#128274; OAuth Required  Remove a like on a list.
     * @param {String} id Automatically added
     * @param {String} listId Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~removeLikeOnAListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    removeLikeOnAList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling removeLikeOnAList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling removeLikeOnAList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
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
        '/users/{id}/lists/{list_id}/like', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reorderAUsersLists operation.
     * @callback module:api/UsersApi~reorderAUsersListsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reorder a user's lists
     * #### &#128274; OAuth Required  Reorder all lists by sending the updated `rank` of list ids. Use the [**_/users/:id/lists**](#reference/users/lists) method to get all list ids.
     * @param {String} id User slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/ReorderAUserSListsRequest} [reorderAUserSListsRequest] 
     * @param {module:api/UsersApi~reorderAUsersListsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reorderAUsersLists(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['reorderAUserSListsRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling reorderAUsersLists");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists/reorder', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reorderItemsOnAList operation.
     * @callback module:api/UsersApi~reorderItemsOnAListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reorder items on a list
     * #### &#128274; OAuth Required  Reorder all items on a list by sending the updated `rank` of list item ids. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get all list item ids.
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/ReorderPersonallyRecommendedItemsRequest} [reorderPersonallyRecommendedItemsRequest] 
     * @param {module:api/UsersApi~reorderItemsOnAListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reorderItemsOnAList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = opts['reorderPersonallyRecommendedItemsRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling reorderItemsOnAList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling reorderItemsOnAList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
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
        '/users/{id}/lists/{list_id}/items/reorder', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the retrieveSettings operation.
     * @callback module:api/UsersApi~retrieveSettingsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve settings
     * #### &#128274; OAuth Required  Get the user's settings so you can align your app's experience with what they're used to on the trakt website. A globally unique `uuid` is also returned, which can be used to identify the user locally in your app if needed. However, the `uuid` can't be used to retrieve data from the Trakt API.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~retrieveSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    retrieveSettings(opts, callback) {
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
        '/users/settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the unfollowThisUser operation.
     * @callback module:api/UsersApi~unfollowThisUserCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Unfollow this user
     * #### &#128274; OAuth Required  Unfollow someone you already follow.
     * @param {String} id Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~unfollowThisUserCallback} callback The callback function, accepting three arguments: error, data, response
     */
    unfollowThisUser(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling unfollowThisUser");
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
        '/users/{id}/follow', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePersonalList operation.
     * @callback module:api/UsersApi~updatePersonalListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update personal list
     * #### &#128274; OAuth Required  Update a personal list by sending 1 or more parameters. If you update the list name, the original slug will still be retained so existing references to this list won't break.  #### Privacy  Lists will be `private` by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | `private` | Only you can see the list. | | `link` | Anyone with the `share_link` can see the list. | | `friends` | Only your friends can see the list. | | `public` | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Value | |---|---|---|---| | `name` | string | Name of the list. | | `description` | string | Description for this list. | | `privacy` | string | `private`, `link`, `friends`, `public` | | `display_numbers` | boolean | Should each item be numbered? | | `allow_comments` | boolean | Are comments allowed? | | `sort_by` | string | `rank`, `added`, `title`, `released`, `runtime`, `popularity`, `percentage`, `votes`, `my_rating`, `random`, `watched`, `collected` | | `sort_how` | string | `asc`, `desc` |
     * @param {String} id Automatically added
     * @param {String} listId Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:model/UpdatePersonalListRequest} [updatePersonalListRequest] 
     * @param {module:api/UsersApi~updatePersonalListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updatePersonalList(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updatePersonalListRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updatePersonalList");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling updatePersonalList");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
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
        '/users/{id}/lists/{list_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdCollectionTypeGet operation.
     * @callback module:api/UsersApi~usersIdCollectionTypeGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get collection
     * #### &#128275; OAuth Optional &#10024; Extended Info  Get all collected items in a user's collection. A collected item indicates availability to watch digitally or on physical media.  Each `movie` object contains `collected_at` and `updated_at` timestamps. Since users can set custom dates when they collected movies, it is possible for `collected_at` to be in the past. We also include `updated_at` to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movie if you see a newer timestamp.  Each `show` object contains `last_collected_at` and `last_updated_at` timestamps. Since users can set custom dates when they collected episodes, it is possible for `last_collected_at` to be in the past. We also include `last_updated_at` to help sync Trakt data with your app. Cache this timestamp locally and only re-process the show if you see a newer timestamp.  If you add `?extended=metadata` to the URL, it will return the additional `media_type`, `resolution`, `hdr`, `audio`, `audio_channels` and '3d' metadata. It will use `null` if the metadata isn't set for an item.
     * @param {String} id User slug
     * @param {module:model/String} type 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdCollectionTypeGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdCollectionTypeGet(id, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdCollectionTypeGet");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling usersIdCollectionTypeGet");
      }

      let pathParams = {
        'id': id,
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/collection/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdHistoryTypeItemIdGet operation.
     * @callback module:api/UsersApi~usersIdHistoryTypeItemIdGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get watched history
     * #### &#128275; OAuth Optional &#128196; Pagination &#10024; Extended Info  Returns movies and episodes that a user has watched, sorted by most recent. You can optionally limit the `type` to `movies` or `episodes`. The `id` _(64-bit integer)_ in each history item uniquely identifies the event and can be used to remove individual events by using the [**_/sync/history/remove**](#reference/sync/remove-from-history/get-watched-history) method. The `action` will be set to `scrobble`, `checkin`, or `watch`.  Specify a `type` and trakt `item_id` to limit the history for just that item. If the `item_id` is valid, but there is no history, an empty array will be returned.  | Example URL | Returns watches for... | |---|---| | `/history/movies/12601` | TRON: Legacy | | `/history/shows/1388` | All episodes of Breaking Bad | | `/history/seasons/3950` | All episodes of Breaking Bad: Season 1 | | `/history/episodes/73482` | Only episode 1 for Breaking Bad: Season 1 |
     * @param {String} id User slug
     * @param {module:model/String} type 
     * @param {Number} itemId Trakt ID for a specific item.
     * @param {Object} opts Optional parameters
     * @param {String} [startAt] Starting date.
     * @param {String} [endAt] Ending date.
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdHistoryTypeItemIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdHistoryTypeItemIdGet(id, type, itemId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdHistoryTypeItemIdGet");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling usersIdHistoryTypeItemIdGet");
      }
      // verify the required parameter 'itemId' is set
      if (itemId === undefined || itemId === null) {
        throw new Error("Missing the required parameter 'itemId' when calling usersIdHistoryTypeItemIdGet");
      }

      let pathParams = {
        'id': id,
        'type': type,
        'item_id': itemId
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/history/{type}/{item_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdListsListIdCommentsSortGet operation.
     * @callback module:api/UsersApi~usersIdListsListIdCommentsSortGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all list comments
     * #### &#128275; OAuth Optional &#128196; Pagination &#128513; Emojis  Returns all top level comments for a list. By default, the `newest` comments are returned first. Other sorting options include `oldest`, most `likes`, and most `replies`.
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {module:model/String} sort how to sort
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdListsListIdCommentsSortGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdListsListIdCommentsSortGet(id, listId, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdListsListIdCommentsSortGet");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling usersIdListsListIdCommentsSortGet");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling usersIdListsListIdCommentsSortGet");
      }

      let pathParams = {
        'id': id,
        'list_id': listId,
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists/{list_id}/comments/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdListsListIdLikesGet operation.
     * @callback module:api/UsersApi~usersIdListsListIdLikesGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all users who liked a list
     * #### &#128275; OAuth Optional &#128196; Pagination  Returns all users who liked a list.
     * @param {String} id User slug
     * @param {String} listId Trakt ID or Trakt slug
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdListsListIdLikesGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdListsListIdLikesGet(id, listId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdListsListIdLikesGet");
      }
      // verify the required parameter 'listId' is set
      if (listId === undefined || listId === null) {
        throw new Error("Missing the required parameter 'listId' when calling usersIdListsListIdLikesGet");
      }

      let pathParams = {
        'id': id,
        'list_id': listId
      };
      let queryParams = {
      };
      let headerParams = {
        'trakt-api-version': opts['traktApiVersion'],
        'trakt-api-key': opts['traktApiKey']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/lists/{list_id}/likes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdRatingsTypeRatingGet operation.
     * @callback module:api/UsersApi~usersIdRatingsTypeRatingGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get ratings
     * #### &#128275; OAuth Optional &#128196; Pagination Optional &#10024; Extended Info  Get a user's ratings filtered by `type`. You can optionally filter for a specific `rating` between 1 and 10. Send a comma separated string for `rating` if you need multiple ratings.
     * @param {String} id User slug
     * @param {module:model/String} type 
     * @param {module:model/Number} rating Filter for a specific rating.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdRatingsTypeRatingGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdRatingsTypeRatingGet(id, type, rating, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdRatingsTypeRatingGet");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling usersIdRatingsTypeRatingGet");
      }
      // verify the required parameter 'rating' is set
      if (rating === undefined || rating === null) {
        throw new Error("Missing the required parameter 'rating' when calling usersIdRatingsTypeRatingGet");
      }

      let pathParams = {
        'id': id,
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/ratings/{type}/{rating}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdRecommendationsTypeSortGet operation.
     * @callback module:api/UsersApi~usersIdRecommendationsTypeSortGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get personal recommendations
     * #### &#128274; OAuth Required &#128196; Pagination Optional &#10024; Extended Info &#128513; Emojis  Returns the top 50 items a user personally recommendeds to others. These recommendations are used to enchance Trakt's social recommendation algorithm. Apps should encourage user's to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation contains a `notes` field explaining why the user recommended the item.
     * @param {String} id User slug
     * @param {module:model/String} type Filter for a specific item type
     * @param {module:model/String} sort How to sort (only if type is also sent)
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdRecommendationsTypeSortGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdRecommendationsTypeSortGet(id, type, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdRecommendationsTypeSortGet");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling usersIdRecommendationsTypeSortGet");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling usersIdRecommendationsTypeSortGet");
      }

      let pathParams = {
        'id': id,
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
        '/users/{id}/recommendations/{type}/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdWatchedTypeGet operation.
     * @callback module:api/UsersApi~usersIdWatchedTypeGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get watched
     * #### &#128275; OAuth Optional &#10024; Extended Info  Returns all movies or shows a user has watched sorted by most plays.  If `type` is set to _shows_ and you add `?extended=noseasons` to the URL, it won't return season or episode info.  Each `movie` and `show` object contains `last_watched_at` and `last_updated_at` timestamps. Since users can set custom dates when they watched movies and episodes, it is possible for `last_watched_at` to be in the past. We also include `last_updated_at` to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movies and shows if you see a newer timestamp.  Each `show` object contains a `reset_at` timestamp. If not `null`, this is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a `last_watched_at` prior to the `reset_at`.
     * @param {String} id User slug
     * @param {module:model/String} type 
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdWatchedTypeGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdWatchedTypeGet(id, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdWatchedTypeGet");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling usersIdWatchedTypeGet");
      }

      let pathParams = {
        'id': id,
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/watched/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdWatchlistTypeSortGet operation.
     * @callback module:api/UsersApi~usersIdWatchlistTypeSortGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get watchlist
     * #### &#128275; OAuth Optional &#128196; Pagination Optional &#10024; Extended Info &#128513; Emojis  Returns all items in a user's watchlist filtered by type.  #### Notes  Each watchlist item contains a `notes` field with text entered by the user.  #### Sorting Headers  By default, all list items are sorted by `rank` `asc`. We send `X-Applied-Sort-By` and `X-Applied-Sort-How` headers to indicate how the results are actually being sorted.  We also send `X-Sort-By` and `X-Sort-How` headers which indicate the user's sort preference. Use these to to custom sort the watchlist _**in your app**_ for more advanced sort abilities we can't do in the API. Values for `X-Sort-By` include `rank`, `added`, `title`, `released`, `runtime`, `popularity`, `percentage`, and `votes`. Values for `X-Sort-How` include `asc` and `desc`.  #### Auto Removal  When an item is watched, it will be automatically removed from the watchlist. For shows and seasons, watching 1 episode will remove the entire show or season.  _**The watchlist should not be used as a list of what the user is actively watching.**_  Use a combination of the [**_/sync/watched**](/reference/sync/get-watched) and [**_/shows/:id/progress**](/reference/shows/watched-progress) methods to get what the user is actively watching.
     * @param {String} id User slug
     * @param {module:model/String} type Filter for a specific item type
     * @param {module:model/String} sort How to sort (only if type is also sent)
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/UsersApi~usersIdWatchlistTypeSortGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdWatchlistTypeSortGet(id, type, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdWatchlistTypeSortGet");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling usersIdWatchlistTypeSortGet");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling usersIdWatchlistTypeSortGet");
      }

      let pathParams = {
        'id': id,
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/{id}/watchlist/{type}/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
