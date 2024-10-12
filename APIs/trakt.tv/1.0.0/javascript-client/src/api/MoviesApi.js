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
* Movies service.
* @module api/MoviesApi
* @version 1.0.0
*/
export default class MoviesApi {

    /**
    * Constructs a new MoviesApi. 
    * @alias module:api/MoviesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getAMovie operation.
     * @callback module:api/MoviesApi~getAMovieCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a movie
     * #### &#10024; Extended Info  Returns a single movie's details.  **Note:** When getting `full` extended info, the `status` field can have a value of `released`, `in production`, `post production`, `planned`, `rumored`, or `canceled`.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getAMovieCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAMovie(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAMovie");
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
        '/movies/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllMovieAliases operation.
     * @callback module:api/MoviesApi~getAllMovieAliasesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all movie aliases
     * Returns all title aliases for a movie.  Includes country where name is different.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getAllMovieAliasesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllMovieAliases(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllMovieAliases");
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
        '/movies/{id}/aliases', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllMovieComments operation.
     * @callback module:api/MoviesApi~getAllMovieCommentsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all movie comments
     * #### &#128196; Pagination &#128513; Emojis  Returns all top level comments for a movie. By default, the `newest` comments are returned first. Other sorting options include `oldest`, most `likes`, most `replies`, `highest` rated, `lowest` rated, and most `plays`.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {module:model/String} sort how to sort
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getAllMovieCommentsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllMovieComments(id, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllMovieComments");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling getAllMovieComments");
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
        '/movies/{id}/comments/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllMovieReleases operation.
     * @callback module:api/MoviesApi~getAllMovieReleasesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all movie releases
     * Returns all releases for a movie including country, certification, release date, release type, and note. The release type can be set to `unknown`, `premiere`, `limited`, `theatrical`, `digital`, `physical`, or `tv`. The `note` might have optional info such as the film festival name for a `premiere` release or Blu-ray specs for a `physical` release. We pull this info from [TMDB](https://developers.themoviedb.org/3/movies/get-movie-release-dates).
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {String} country 2 character country code
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getAllMovieReleasesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllMovieReleases(id, country, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllMovieReleases");
      }
      // verify the required parameter 'country' is set
      if (country === undefined || country === null) {
        throw new Error("Missing the required parameter 'country' when calling getAllMovieReleases");
      }

      let pathParams = {
        'id': id,
        'country': country
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
        '/movies/{id}/releases/{country}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllMovieTranslations operation.
     * @callback module:api/MoviesApi~getAllMovieTranslationsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all movie translations
     * Returns all translations for a movie, including language and translated values for title, tagline and overview.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {String} language 2 character language code
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getAllMovieTranslationsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllMovieTranslations(id, language, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllMovieTranslations");
      }
      // verify the required parameter 'language' is set
      if (language === undefined || language === null) {
        throw new Error("Missing the required parameter 'language' when calling getAllMovieTranslations");
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
        '/movies/{id}/translations/{language}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllPeopleForAMovie operation.
     * @callback module:api/MoviesApi~getAllPeopleForAMovieCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all people for a movie
     * #### &#10024; Extended Info  Returns all `cast` and `crew` for a movie. Each `cast` member will have a `characters` array and a standard `person` object.  The `crew` object will be broken up by department into `production`, `art`, `crew`, `costume & make-up`, `directing`, `writing`, `sound`, `camera`, `visual effects`, `lighting`, and `editing` (if there are people for those crew positions). Each of those members will have a `jobs` array and a standard `person` object.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getAllPeopleForAMovieCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getAllPeopleForAMovie(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getAllPeopleForAMovie");
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
        '/movies/{id}/people', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getListsContainingThisMovie operation.
     * @callback module:api/MoviesApi~getListsContainingThisMovieCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get lists containing this movie
     * #### &#128196; Pagination &#128513; Emojis  Returns all lists that contain this movie. By default, `personal` lists are returned sorted by the most `popular`.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {module:model/String} type Filter for a specific list type
     * @param {module:model/String} sort How to sort
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getListsContainingThisMovieCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getListsContainingThisMovie(id, type, sort, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getListsContainingThisMovie");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getListsContainingThisMovie");
      }
      // verify the required parameter 'sort' is set
      if (sort === undefined || sort === null) {
        throw new Error("Missing the required parameter 'sort' when calling getListsContainingThisMovie");
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
        '/movies/{id}/lists/{type}/{sort}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMovieRatings operation.
     * @callback module:api/MoviesApi~getMovieRatingsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get movie ratings
     * Returns rating (between 0 and 10) and distribution for a movie.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getMovieRatingsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getMovieRatings(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getMovieRatings");
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
        '/movies/{id}/ratings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMovieStats operation.
     * @callback module:api/MoviesApi~getMovieStatsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get movie stats
     * Returns lots of movie stats.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getMovieStatsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getMovieStats(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getMovieStats");
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
        '/movies/{id}/stats', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMovieStudios operation.
     * @callback module:api/MoviesApi~getMovieStudiosCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get movie studios
     * Returns all studios for a movie.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getMovieStudiosCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getMovieStudios(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getMovieStudios");
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
        '/movies/{id}/studios', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPopularMovies operation.
     * @callback module:api/MoviesApi~getPopularMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get popular movies
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most popular movies. Popularity is calculated using the rating percentage and the number of ratings.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getPopularMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getPopularMovies(opts, callback) {
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
        '/movies/popular', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRecentlyUpdatedMovieTraktIDs operation.
     * @callback module:api/MoviesApi~getRecentlyUpdatedMovieTraktIDsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get recently updated movie Trakt IDs
     * #### &#128196; Pagination  Returns all movie Trakt IDs updated since the specified UTC date and time. We recommended storing the `X-Start-Date` header you can be efficient using this method moving forward. By default, `10` results are returned. You can send a `limit` to get up to `100` results per page.  **Important!** The `start_date` is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use `2021-07-17T12:00:00Z` and not `2021-07-17T12:23:34Z`.  **Note:** The `start_date` can only be a maximum of 30 days in the past.
     * @param {String} startDate Updated since this date and time.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getRecentlyUpdatedMovieTraktIDsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getRecentlyUpdatedMovieTraktIDs(startDate, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'startDate' is set
      if (startDate === undefined || startDate === null) {
        throw new Error("Missing the required parameter 'startDate' when calling getRecentlyUpdatedMovieTraktIDs");
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
        '/movies/updates/id/{start_date}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRecentlyUpdatedMovies operation.
     * @callback module:api/MoviesApi~getRecentlyUpdatedMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get recently updated movies
     * #### &#128196; Pagination &#10024; Extended Info  Returns all movies updated since the specified UTC date and time. We recommended storing the `X-Start-Date` header you can be efficient using this method moving forward. By default, `10` results are returned. You can send a `limit` to get up to `100` results per page.  **Important!** The `start_date` is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use `2021-07-17T12:00:00Z` and not `2021-07-17T12:23:34Z`.  **Note:** The `start_date` can only be a maximum of 30 days in the past.
     * @param {String} startDate Updated since this date and time.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getRecentlyUpdatedMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getRecentlyUpdatedMovies(startDate, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'startDate' is set
      if (startDate === undefined || startDate === null) {
        throw new Error("Missing the required parameter 'startDate' when calling getRecentlyUpdatedMovies");
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
        '/movies/updates/{start_date}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRelatedMovies operation.
     * @callback module:api/MoviesApi~getRelatedMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get related movies
     * #### &#128196; Pagination &#10024; Extended Info  Returns related and similar movies.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getRelatedMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getRelatedMovies(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getRelatedMovies");
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
        '/movies/{id}/related', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostAnticipatedMovies operation.
     * @callback module:api/MoviesApi~getTheMostAnticipatedMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most anticipated movies
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most anticipated movies based on the number of lists a movie appears on.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getTheMostAnticipatedMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostAnticipatedMovies(opts, callback) {
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
        '/movies/anticipated', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostCollectedMovies operation.
     * @callback module:api/MoviesApi~getTheMostCollectedMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most Collected movies
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most collected (unique users) movies in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getTheMostCollectedMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostCollectedMovies(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostCollectedMovies");
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
        '/movies/collected/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostPlayedMovies operation.
     * @callback module:api/MoviesApi~getTheMostPlayedMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most played movies
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most played (a single user can watch multiple times) movies in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getTheMostPlayedMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostPlayedMovies(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostPlayedMovies");
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
        '/movies/played/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostRecommendedMovies operation.
     * @callback module:api/MoviesApi~getTheMostRecommendedMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most recommended movies
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most recommended movies in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getTheMostRecommendedMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostRecommendedMovies(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostRecommendedMovies");
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
        '/movies/recommended/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheMostWatchedMovies operation.
     * @callback module:api/MoviesApi~getTheMostWatchedMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the most watched movies
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns the most watched (unique users) movies in the specified time `period`, defaulting to `weekly`. All stats are relative to the specific time `period`.
     * @param {module:model/String} period Time period.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getTheMostWatchedMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheMostWatchedMovies(period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getTheMostWatchedMovies");
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
        '/movies/watched/{period}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTheWeekendBoxOffice operation.
     * @callback module:api/MoviesApi~getTheWeekendBoxOfficeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the weekend box office
     * #### &#10024; Extended Info  Returns the top 10 grossing movies in the U.S. box office last weekend. Updated every Monday morning.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getTheWeekendBoxOfficeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTheWeekendBoxOffice(opts, callback) {
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
        '/movies/boxoffice', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTrendingMovies operation.
     * @callback module:api/MoviesApi~getTrendingMoviesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get trending movies
     * #### &#128196; Pagination &#10024; Extended Info &#127898; Filters  Returns all movies being watched right now. Movies with the most users are returned first.
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getTrendingMoviesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getTrendingMovies(opts, callback) {
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
        '/movies/trending', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUsersWatchingRightNow operation.
     * @callback module:api/MoviesApi~getUsersWatchingRightNowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get users watching right now
     * #### &#10024; Extended Info  Returns all users watching this movie right now.
     * @param {String} id Trakt ID, Trakt slug, or IMDB ID
     * @param {Object} opts Optional parameters
     * @param {String} [traktApiVersion] e.g. 2
     * @param {String} [traktApiKey] e.g. [client_id]
     * @param {module:api/MoviesApi~getUsersWatchingRightNowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    getUsersWatchingRightNow(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getUsersWatchingRightNow");
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
        '/movies/{id}/watching', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
