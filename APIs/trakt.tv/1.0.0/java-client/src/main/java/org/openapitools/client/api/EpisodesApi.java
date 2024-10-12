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

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;



import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EpisodesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public EpisodesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public EpisodesApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for getASingleEpisodeForAShow
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1?extended&#x3D;full &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getASingleEpisodeForAShowCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getASingleEpisodeForAShowValidateBeforeCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getASingleEpisodeForAShow(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling getASingleEpisodeForAShow(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling getASingleEpisodeForAShow(Async)");
        }

        return getASingleEpisodeForAShowCall(id, season, episode, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get a single episode for a show
     * #### &amp;#10024; Extended Info  Returns a single episode&#39;s details. All date and times are in UTC and were calculated using the episode&#39;s &#x60;air_date&#x60; and show&#39;s &#x60;country&#x60; and &#x60;air_time&#x60;.  **Note:** If the &#x60;first_aired&#x60; is unknown, it will be set to &#x60;null&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1?extended&#x3D;full &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public void getASingleEpisodeForAShow(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        getASingleEpisodeForAShowWithHttpInfo(id, season, episode, traktApiVersion, traktApiKey);
    }

    /**
     * Get a single episode for a show
     * #### &amp;#10024; Extended Info  Returns a single episode&#39;s details. All date and times are in UTC and were calculated using the episode&#39;s &#x60;air_date&#x60; and show&#39;s &#x60;country&#x60; and &#x60;air_time&#x60;.  **Note:** If the &#x60;first_aired&#x60; is unknown, it will be set to &#x60;null&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1?extended&#x3D;full &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getASingleEpisodeForAShowWithHttpInfo(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getASingleEpisodeForAShowValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get a single episode for a show (asynchronously)
     * #### &amp;#10024; Extended Info  Returns a single episode&#39;s details. All date and times are in UTC and were calculated using the episode&#39;s &#x60;air_date&#x60; and show&#39;s &#x60;country&#x60; and &#x60;air_time&#x60;.  **Note:** If the &#x60;first_aired&#x60; is unknown, it will be set to &#x60;null&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1?extended&#x3D;full &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getASingleEpisodeForAShowAsync(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getASingleEpisodeForAShowValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllEpisodeComments
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param sort how to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getAllEpisodeCommentsCall(String id, Integer season, Integer episode, String sort, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()))
            .replace("{" + "sort" + "}", localVarApiClient.escapeString(sort.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAllEpisodeCommentsValidateBeforeCall(String id, Integer season, Integer episode, String sort, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getAllEpisodeComments(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling getAllEpisodeComments(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling getAllEpisodeComments(Async)");
        }

        // verify the required parameter 'sort' is set
        if (sort == null) {
            throw new ApiException("Missing the required parameter 'sort' when calling getAllEpisodeComments(Async)");
        }

        return getAllEpisodeCommentsCall(id, season, episode, sort, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get all episode comments
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for an episode. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param sort how to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public void getAllEpisodeComments(String id, Integer season, Integer episode, String sort, String traktApiVersion, String traktApiKey) throws ApiException {
        getAllEpisodeCommentsWithHttpInfo(id, season, episode, sort, traktApiVersion, traktApiKey);
    }

    /**
     * Get all episode comments
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for an episode. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param sort how to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> getAllEpisodeCommentsWithHttpInfo(String id, Integer season, Integer episode, String sort, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getAllEpisodeCommentsValidateBeforeCall(id, season, episode, sort, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get all episode comments (asynchronously)
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for an episode. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param sort how to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getAllEpisodeCommentsAsync(String id, Integer season, Integer episode, String sort, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllEpisodeCommentsValidateBeforeCall(id, season, episode, sort, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllEpisodeTranslations
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param language 2 character language code (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllEpisodeTranslationsCall(String id, Integer season, Integer episode, String language, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}/translations/{language}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()))
            .replace("{" + "language" + "}", localVarApiClient.escapeString(language.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAllEpisodeTranslationsValidateBeforeCall(String id, Integer season, Integer episode, String language, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getAllEpisodeTranslations(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling getAllEpisodeTranslations(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling getAllEpisodeTranslations(Async)");
        }

        // verify the required parameter 'language' is set
        if (language == null) {
            throw new ApiException("Missing the required parameter 'language' when calling getAllEpisodeTranslations(Async)");
        }

        return getAllEpisodeTranslationsCall(id, season, episode, language, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get all episode translations
     * Returns all translations for an episode, including language and translated values for title and overview.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param language 2 character language code (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void getAllEpisodeTranslations(String id, Integer season, Integer episode, String language, String traktApiVersion, String traktApiKey) throws ApiException {
        getAllEpisodeTranslationsWithHttpInfo(id, season, episode, language, traktApiVersion, traktApiKey);
    }

    /**
     * Get all episode translations
     * Returns all translations for an episode, including language and translated values for title and overview.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param language 2 character language code (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getAllEpisodeTranslationsWithHttpInfo(String id, Integer season, Integer episode, String language, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getAllEpisodeTranslationsValidateBeforeCall(id, season, episode, language, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get all episode translations (asynchronously)
     * Returns all translations for an episode, including language and translated values for title and overview.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param language 2 character language code (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllEpisodeTranslationsAsync(String id, Integer season, Integer episode, String language, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllEpisodeTranslationsValidateBeforeCall(id, season, episode, language, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllPeopleForAnEpisode
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1/people?extended&#x3D;guest_stars &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllPeopleForAnEpisodeCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}/people"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAllPeopleForAnEpisodeValidateBeforeCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getAllPeopleForAnEpisode(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling getAllPeopleForAnEpisode(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling getAllPeopleForAnEpisode(Async)");
        }

        return getAllPeopleForAnEpisodeCall(id, season, episode, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get all people for an episode
     * #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for an episode. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in the episode.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1/people?extended&#x3D;guest_stars &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public void getAllPeopleForAnEpisode(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        getAllPeopleForAnEpisodeWithHttpInfo(id, season, episode, traktApiVersion, traktApiKey);
    }

    /**
     * Get all people for an episode
     * #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for an episode. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in the episode.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1/people?extended&#x3D;guest_stars &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getAllPeopleForAnEpisodeWithHttpInfo(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getAllPeopleForAnEpisodeValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get all people for an episode (asynchronously)
     * #### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for an episode. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in the episode.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> &#x60;&#x60;&#x60; /shows/game-of-thrones/seasons/1/episodes/1/people?extended&#x3D;guest_stars &#x60;&#x60;&#x60; </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllPeopleForAnEpisodeAsync(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllPeopleForAnEpisodeValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getEpisodeRatings
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getEpisodeRatingsCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}/ratings"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getEpisodeRatingsValidateBeforeCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getEpisodeRatings(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling getEpisodeRatings(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling getEpisodeRatings(Async)");
        }

        return getEpisodeRatingsCall(id, season, episode, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get episode ratings
     * Returns rating (between 0 and 10) and distribution for an episode.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void getEpisodeRatings(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        getEpisodeRatingsWithHttpInfo(id, season, episode, traktApiVersion, traktApiKey);
    }

    /**
     * Get episode ratings
     * Returns rating (between 0 and 10) and distribution for an episode.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getEpisodeRatingsWithHttpInfo(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getEpisodeRatingsValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get episode ratings (asynchronously)
     * Returns rating (between 0 and 10) and distribution for an episode.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getEpisodeRatingsAsync(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getEpisodeRatingsValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getEpisodeStats
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getEpisodeStatsCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}/stats"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getEpisodeStatsValidateBeforeCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getEpisodeStats(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling getEpisodeStats(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling getEpisodeStats(Async)");
        }

        return getEpisodeStatsCall(id, season, episode, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get episode stats
     * Returns lots of episode stats.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void getEpisodeStats(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        getEpisodeStatsWithHttpInfo(id, season, episode, traktApiVersion, traktApiKey);
    }

    /**
     * Get episode stats
     * Returns lots of episode stats.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getEpisodeStatsWithHttpInfo(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getEpisodeStatsValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get episode stats (asynchronously)
     * Returns lots of episode stats.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getEpisodeStatsAsync(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getEpisodeStatsValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getListsContainingThisEpisode
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param type Filter for a specific list type (required)
     * @param sort How to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getListsContainingThisEpisodeCall(String id, Integer season, Integer episode, String type, String sort, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()))
            .replace("{" + "type" + "}", localVarApiClient.escapeString(type.toString()))
            .replace("{" + "sort" + "}", localVarApiClient.escapeString(sort.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getListsContainingThisEpisodeValidateBeforeCall(String id, Integer season, Integer episode, String type, String sort, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getListsContainingThisEpisode(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling getListsContainingThisEpisode(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling getListsContainingThisEpisode(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling getListsContainingThisEpisode(Async)");
        }

        // verify the required parameter 'sort' is set
        if (sort == null) {
            throw new ApiException("Missing the required parameter 'sort' when calling getListsContainingThisEpisode(Async)");
        }

        return getListsContainingThisEpisodeCall(id, season, episode, type, sort, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get lists containing this episode
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this episode. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param type Filter for a specific list type (required)
     * @param sort How to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public void getListsContainingThisEpisode(String id, Integer season, Integer episode, String type, String sort, String traktApiVersion, String traktApiKey) throws ApiException {
        getListsContainingThisEpisodeWithHttpInfo(id, season, episode, type, sort, traktApiVersion, traktApiKey);
    }

    /**
     * Get lists containing this episode
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this episode. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param type Filter for a specific list type (required)
     * @param sort How to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> getListsContainingThisEpisodeWithHttpInfo(String id, Integer season, Integer episode, String type, String sort, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getListsContainingThisEpisodeValidateBeforeCall(id, season, episode, type, sort, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get lists containing this episode (asynchronously)
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this episode. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param type Filter for a specific list type (required)
     * @param sort How to sort (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getListsContainingThisEpisodeAsync(String id, Integer season, Integer episode, String type, String sort, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getListsContainingThisEpisodeValidateBeforeCall(id, season, episode, type, sort, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for showsIdSeasonsSeasonEpisodesEpisodeWatchingGet
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call showsIdSeasonsSeasonEpisodesEpisodeWatchingGetCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/shows/{id}/seasons/{season}/episodes/{episode}/watching"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "season" + "}", localVarApiClient.escapeString(season.toString()))
            .replace("{" + "episode" + "}", localVarApiClient.escapeString(episode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (traktApiVersion != null) {
            localVarHeaderParams.put("trakt-api-version", localVarApiClient.parameterToString(traktApiVersion));
        }

        if (traktApiKey != null) {
            localVarHeaderParams.put("trakt-api-key", localVarApiClient.parameterToString(traktApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call showsIdSeasonsSeasonEpisodesEpisodeWatchingGetValidateBeforeCall(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(Async)");
        }

        // verify the required parameter 'season' is set
        if (season == null) {
            throw new ApiException("Missing the required parameter 'season' when calling showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(Async)");
        }

        // verify the required parameter 'episode' is set
        if (episode == null) {
            throw new ApiException("Missing the required parameter 'episode' when calling showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(Async)");
        }

        return showsIdSeasonsSeasonEpisodesEpisodeWatchingGetCall(id, season, episode, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get users watching right now
     * #### &amp;#10024; Extended Info  Returns all users watching this episode right now.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        showsIdSeasonsSeasonEpisodesEpisodeWatchingGetWithHttpInfo(id, season, episode, traktApiVersion, traktApiKey);
    }

    /**
     * Get users watching right now
     * #### &amp;#10024; Extended Info  Returns all users watching this episode right now.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> showsIdSeasonsSeasonEpisodesEpisodeWatchingGetWithHttpInfo(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = showsIdSeasonsSeasonEpisodesEpisodeWatchingGetValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get users watching right now (asynchronously)
     * #### &amp;#10024; Extended Info  Returns all users watching this episode right now.
     * @param id Trakt ID, Trakt slug, or IMDB ID (required)
     * @param season season number (required)
     * @param episode episode number (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call showsIdSeasonsSeasonEpisodesEpisodeWatchingGetAsync(String id, Integer season, Integer episode, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = showsIdSeasonsSeasonEpisodesEpisodeWatchingGetValidateBeforeCall(id, season, episode, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
