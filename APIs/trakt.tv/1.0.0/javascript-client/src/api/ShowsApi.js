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

/**
* Shows service.
* @module api/ShowsApi
* @version 1.0.0
*/
export default class ShowsApi {

    /**
    * Constructs a new ShowsApi. 
    * @alias module:api/ShowsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getASingleShow operation.
     * @callback module:api/ShowsApi~getASingleShowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a single show
     * #### &#10024; Extended Info  Returns a single shows's details. If you request extended info, the `airs` object is relative to the show's country. You can use the `day`, `time`, and `timezone` to construct your own date then convert it to whatever timezone your user is in.  **Note:** When getting `full` extended info, the `status` field can have a value of `returning series` (airing right now),  `continuing` (airing right now), `in production` (airing soon), `planned` (in development), `upcoming` (in development),  `pilot`, `canceled`, or `ended`.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getASingleShowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getASingleShow(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getASingleShow");
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
        '/shows/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllPeopleForAShow operation.
     * @callback module:api/ShowsApi~getAllPeopleForAShowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all people for a show
     * #### &#10024; Extended Info  Returns all `cast` and `crew` for a show, including the `episode_count` for which they appears. Each `cast` member will have a `characters` array and a standard `person` object.  The `crew` object will be broken up by department into `production`, `art`, `crew`, `costume & make-up`, `directing`, `writing`, `sound`, `camera`, `visual effects`, `lighting`, `editing`, and `created  by` (if there are people for those crew positions). Each of those members will have a `jobs` array and a standard `person` object.  #### Guest Stars  If you add `?extended=guest_stars` to the URL, it will return all guest stars that appeared in at least 1 episode of the show.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getAllPeopleForAShowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllPeopleForAShow(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllPeopleForAShow");
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
        '/shows/{id}/people', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllShowAliases operation.
     * @callback module:api/ShowsApi~getAllShowAliasesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all show aliases
     * Returns all title aliases for a show.  Includes country where name is different.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getAllShowAliasesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllShowAliases(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllShowAliases");
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
        '/shows/{id}/aliases', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllShowCertifications operation.
     * @callback module:api/ShowsApi~getAllShowCertificationsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all show certifications
     * Returns all content certifications for a show, including the country.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getAllShowCertificationsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllShowCertifications(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllShowCertifications");
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
        '/shows/{id}/certifications', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllShowComments operation.
     * @callback module:api/ShowsApi~getAllShowCommentsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all show comments
     * #### &#128196; Pagination &#128513; Emojis  Returns all top level comments for a show. By default, the `newest` comments are returned first. Other sorting options include `oldest`, most `likes`, most `replies`, `highest` rated, `lowest` rated, most `plays`, and highest `watched` percentage.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {module:model/String} sort how to sort
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getAllShowCommentsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllShowComments(id, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllShowComments");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling getAllShowComments");
      }

      let pathParams = {
        'id': id,
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
        '/shows/{id}/comments/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllShowTranslations operation.
     * @callback module:api/ShowsApi~getAllShowTranslationsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all show translations
     * Returns all translations for a show, including language and translated values for title and overview.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {String} language 2 character language code
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getAllShowTranslationsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllShowTranslations(id, language, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllShowTranslations");
      }
      // verify the required parameter 'language' is set
      if (language === undefined || language === null) {
        throw new Error("Missing the required parameter 'language' when calling getAllShowTranslations");
      }

      let pathParams = {
        'id': id,
        'language': language
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
        '/shows/{id}/translations/{language}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLastEpisode operation.
     * @callback module:api/ShowsApi~getLastEpisodeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get last episode
     * #### &#10024; Extended Info  Returns the most recently aired episode. If no episode is found, a `204` HTTP status code will be returned.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getLastEpisodeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getLastEpisode(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getLastEpisode");
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
        '/shows/{id}/last_episode', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getListsContainingThisShow operation.
     * @callback module:api/ShowsApi~getListsContainingThisShowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get lists containing this show
     * #### &#128196; Pagination &#128513; Emojis  Returns all lists that contain this show. By default, `personal` lists are returned sorted by the most `popular`.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {module:model/String} type Filter for a specific list type
     * @param {module:model/String} sort How to sort
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getListsContainingThisShowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getListsContainingThisShow(id, type, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getListsContainingThisShow");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getListsContainingThisShow");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling getListsContainingThisShow");
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
        '/shows/{id}/lists/{type}/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNextEpisode operation.
     * @callback module:api/ShowsApi~getNextEpisodeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get next episode
     * #### &#10024; Extended Info  Returns the next scheduled to air episode. If no episode is found, a `204` HTTP status code will be returned.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getNextEpisodeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getNextEpisode(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getNextEpisode");
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
        '/shows/{id}/next_episode', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPopularShows operation.
     * @callback module:api/ShowsApi~getPopularShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get popular shows
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most popular shows. Popularity is calculated using the rating percentage and the number of ratings.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getPopularShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getPopularShows(opts, callback) {
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/shows/popular', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRecentlyUpdatedShowTraktIDs operation.
     * @callback module:api/ShowsApi~getRecentlyUpdatedShowTraktIDsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get recently updated show Trakt IDs
     * #### &#128196; Pagination  Returns all show Trakt IDs updated since the specified UTC date and time. We recommended storing the `X-Start-Date` header you can be efficient using this method moving forward. By default, `10` results are returned. You can send a `limit` to get up to `100` results per page.  **Important!** The `start_date` is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use `2021-07-17T12:00:00Z` and not `2021-07-17T12:23:34Z`.  **Note:** The `start_date` can only be a maximum of 30 days in the past.
     * @param {String} startDate Updated since this date and time.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getRecentlyUpdatedShowTraktIDsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getRecentlyUpdatedShowTraktIDs(startDate, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'startDate' is set
      if (startDate === undefined || startDate === null) {
        throw new Error("Missing the required parameter 'startDate' when calling getRecentlyUpdatedShowTraktIDs");
      }

      let pathParams = {
        'start_date': startDate
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
        '/shows/updates/id/{start_date}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRecentlyUpdatedShows operation.
     * @callback module:api/ShowsApi~getRecentlyUpdatedShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get recently updated shows
     * #### &#128196; Pagination &#10024; Extended Info  Returns all shows updated since the specified UTC date and time. We recommended storing the `X-Start-Date` header you can be efficient using this method moving forward. By default, `10` results are returned. You can send a `limit` to get up to `100` results per page.  **Important!** The `start_date` is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use `2021-07-17T12:00:00Z` and not `2021-07-17T12:23:34Z`.  **Note:** The `start_date` can only be a maximum of 30 days in the past.
     * @param {String} startDate Updated since this date and time.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getRecentlyUpdatedShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getRecentlyUpdatedShows(startDate, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'startDate' is set
      if (startDate === undefined || startDate === null) {
        throw new Error("Missing the required parameter 'startDate' when calling getRecentlyUpdatedShows");
      }

      let pathParams = {
        'start_date': startDate
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
        '/shows/updates/{start_date}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRelatedShows operation.
     * @callback module:api/ShowsApi~getRelatedShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get related shows
     * #### &#128196; Pagination &#10024; Extended Info  Returns related and similar shows.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getRelatedShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getRelatedShows(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getRelatedShows");
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
        '/shows/{id}/related', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getShowCollectionProgress operation.
     * @callback module:api/ShowsApi~getShowCollectionProgressCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get show collection progress
     * #### &#128274; OAuth Required  Returns collection progress for a show including details on all aired seasons and episodes. The `next_episode` will be the next episode the user should collect, if there are no upcoming episodes it will be set to `null`.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the `hidden` flag to `true`.  By default, specials will be excluded from the response. Set the `specials` flag to `true` to include season 0 and adjust the stats accordingly. If you'd like to include specials, but not adjust the stats, set `count_specials` to `false`.  By default, the `last_episode` and `next_episode` are calculated using the last `aired` episode the user has collected, even if they've collected older episodes more recently. To use their last collected episode for these calculations, set the `last_activity` flag to `collected`.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {String} body 
     * @param {Object} opts Optional parameters
     * @param {String} [hidden] include any hidden seasons
     * @param {String} [specials] include specials as season 0
     * @param {String} [countSpecials] count specials in the overall stats (only applies if specials are included)
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getShowCollectionProgressCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getShowCollectionProgress(id, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getShowCollectionProgress");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling getShowCollectionProgress");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'hidden': opts['hidden'],
        'specials': opts['specials'],
        'count_specials': opts['countSpecials']
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
        '/shows/{id}/progress/collection', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getShowRatings operation.
     * @callback module:api/ShowsApi~getShowRatingsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get show ratings
     * Returns rating (between 0 and 10) and distribution for a show.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getShowRatingsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getShowRatings(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getShowRatings");
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
        '/shows/{id}/ratings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getShowStats operation.
     * @callback module:api/ShowsApi~getShowStatsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get show stats
     * Returns lots of show stats.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getShowStatsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getShowStats(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getShowStats");
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
        '/shows/{id}/stats', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getShowStudios operation.
     * @callback module:api/ShowsApi~getShowStudiosCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get show studios
     * Returns all studios for a show.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getShowStudiosCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getShowStudios(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getShowStudios");
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
        '/shows/{id}/studios', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getShowWatchedProgress operation.
     * @callback module:api/ShowsApi~getShowWatchedProgressCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get show watched progress
     * #### &#128274; OAuth Required  Returns watched progress for a show including details on all aired seasons and episodes. The `next_episode` will be the next episode the user should watch, if there are no upcoming episodes it will be set to `null`. If not `null`, the `reset_at` date is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a `last_watched_at` prior to the `reset_at`.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the `hidden` flag to `true`.  By default, specials will be excluded from the response. Set the `specials` flag to `true` to include season 0 and adjust the stats accordingly. If you'd like to include specials, but not adjust the stats, set `count_specials` to `false`.  By default, the `last_episode` and `next_episode` are calculated using the last `aired` episode the user has watched, even if they've watched older episodes more recently. To use their last watched episode for these calculations, set the `last_activity` flag to `watched`.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {String} body 
     * @param {Object} opts Optional parameters
     * @param {String} [hidden] include any hidden seasons
     * @param {String} [specials] include specials as season 0
     * @param {String} [countSpecials] count specials in the overall stats (only applies if specials are included)
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getShowWatchedProgressCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getShowWatchedProgress(id, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getShowWatchedProgress");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling getShowWatchedProgress");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'hidden': opts['hidden'],
        'specials': opts['specials'],
        'count_specials': opts['countSpecials']
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
        '/shows/{id}/progress/watched', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostAnticipatedShows operation.
     * @callback module:api/ShowsApi~getTheMostAnticipatedShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most anticipated shows
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most anticipated shows based on the number of lists a show appears on.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getTheMostAnticipatedShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostAnticipatedShows(opts, callback) {
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/shows/anticipated', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostCollectedShows operation.
     * @callback module:api/ShowsApi~getTheMostCollectedShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most collected shows
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most collected (unique users) shows in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getTheMostCollectedShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostCollectedShows(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostCollectedShows");
      }

      let pathParams = {
        'period': period
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
        '/shows/collected/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostPlayedShows operation.
     * @callback module:api/ShowsApi~getTheMostPlayedShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most played shows
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most played (a single user can watch multiple episodes multiple times) shows in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getTheMostPlayedShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostPlayedShows(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostPlayedShows");
      }

      let pathParams = {
        'period': period
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
        '/shows/played/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostRecommendedShows operation.
     * @callback module:api/ShowsApi~getTheMostRecommendedShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most recommended shows
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most recommended shows in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getTheMostRecommendedShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostRecommendedShows(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostRecommendedShows");
      }

      let pathParams = {
        'period': period
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
        '/shows/recommended/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostWatchedShows operation.
     * @callback module:api/ShowsApi~getTheMostWatchedShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most watched shows
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most watched (unique users) shows in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getTheMostWatchedShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostWatchedShows(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostWatchedShows");
      }

      let pathParams = {
        'period': period
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
        '/shows/watched/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTrendingShows operation.
     * @callback module:api/ShowsApi~getTrendingShowsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get trending shows
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns all shows being watched right now. Shows with the most users are returned first.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~getTrendingShowsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTrendingShows(opts, callback) {
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/shows/trending', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resetShowProgress operation.
     * @callback module:api/ShowsApi~resetShowProgressCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reset show progress
     * #### &#128274; OAuth Required 🔥 VIP Only  Reset a show's progress when the user started re-watching the show. You can optionally specify the `reset_at` date to have it calculate progress from that specific date onwards.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~resetShowProgressCallback} callback The callback function, accepting three arguments: error, data, response
     */
    resetShowProgress(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling resetShowProgress");
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
        '/shows/{id}/progress/watched/reset', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the showsIdWatchingGet operation.
     * @callback module:api/ShowsApi~showsIdWatchingGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get users watching right now
     * #### &#10024; Extended Info  Returns all users watching this show right now.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~showsIdWatchingGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    showsIdWatchingGet(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling showsIdWatchingGet");
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
        '/shows/{id}/watching', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the undoResetShowProgress operation.
     * @callback module:api/ShowsApi~undoResetShowProgressCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Undo reset show progress
     * #### &#128274; OAuth Required 🔥 VIP Only  Undo the reset and have watched progress use all watched history for the show.
     * @param {String} id Automatically added
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/ShowsApi~undoResetShowProgressCallback} callback The callback function, accepting three arguments: error, data, response
     */
    undoResetShowProgress(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling undoResetShowProgress");
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
        '/shows/{id}/progress/watched/reset', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
