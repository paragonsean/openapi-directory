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


import org.openapitools.client.model.PostACommentRequest;
import org.openapitools.client.model.PostAReplyForACommentRequest;
import org.openapitools.client.model.UpdateACommentOrReplyRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CommentsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CommentsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CommentsApi(ApiClient apiClient) {
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
     * Build call for deleteACommentOrReply
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteACommentOrReplyCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteACommentOrReplyValidateBeforeCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteACommentOrReply(Async)");
        }

        return deleteACommentOrReplyCall(id, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Delete a comment or reply
     * #### &amp;#128274; OAuth Required  Delete a single comment. The OAuth user must match the author of the comment in order to delete it. If not, a &#x60;401&#x60; HTTP status code is returned. The comment must also be less than 2 weeks old or have 0 replies. If not, a &#x60;409&#x60; HTTP status is returned.
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void deleteACommentOrReply(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        deleteACommentOrReplyWithHttpInfo(id, traktApiVersion, traktApiKey);
    }

    /**
     * Delete a comment or reply
     * #### &amp;#128274; OAuth Required  Delete a single comment. The OAuth user must match the author of the comment in order to delete it. If not, a &#x60;401&#x60; HTTP status code is returned. The comment must also be less than 2 weeks old or have 0 replies. If not, a &#x60;409&#x60; HTTP status is returned.
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteACommentOrReplyWithHttpInfo(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = deleteACommentOrReplyValidateBeforeCall(id, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a comment or reply (asynchronously)
     * #### &amp;#128274; OAuth Required  Delete a single comment. The OAuth user must match the author of the comment in order to delete it. If not, a &#x60;401&#x60; HTTP status code is returned. The comment must also be less than 2 weeks old or have 0 replies. If not, a &#x60;409&#x60; HTTP status is returned.
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteACommentOrReplyAsync(String id, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteACommentOrReplyValidateBeforeCall(id, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getACommentOrReply
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Item-ID -  <br>  * X-Item-Type -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getACommentOrReplyCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
    private okhttp3.Call getACommentOrReplyValidateBeforeCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getACommentOrReply(Async)");
        }

        return getACommentOrReplyCall(id, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get a comment or reply
     * ####  &amp;#128513; Emojis  Returns a single comment and indicates how many replies it has. Use [**_/comments/:id/replies**](/reference/comments/replies/) to get the actual replies.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Item-ID -  <br>  * X-Item-Type -  <br>  </td></tr>
     </table>
     */
    public void getACommentOrReply(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        getACommentOrReplyWithHttpInfo(id, traktApiVersion, traktApiKey);
    }

    /**
     * Get a comment or reply
     * ####  &amp;#128513; Emojis  Returns a single comment and indicates how many replies it has. Use [**_/comments/:id/replies**](/reference/comments/replies/) to get the actual replies.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Item-ID -  <br>  * X-Item-Type -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> getACommentOrReplyWithHttpInfo(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getACommentOrReplyValidateBeforeCall(id, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get a comment or reply (asynchronously)
     * ####  &amp;#128513; Emojis  Returns a single comment and indicates how many replies it has. Use [**_/comments/:id/replies**](/reference/comments/replies/) to get the actual replies.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Item-ID -  <br>  * X-Item-Type -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getACommentOrReplyAsync(String id, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getACommentOrReplyValidateBeforeCall(id, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllUsersWhoLikedAComment
     * @param id A specific comment ID. (required)
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
    public okhttp3.Call getAllUsersWhoLikedACommentCall(Integer id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/{id}/likes"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
    private okhttp3.Call getAllUsersWhoLikedACommentValidateBeforeCall(Integer id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getAllUsersWhoLikedAComment(Async)");
        }

        return getAllUsersWhoLikedACommentCall(id, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get all users who liked a comment
     * #### &amp;#128196; Pagination  Returns all users who liked a comment. If you only need the &#x60;replies&#x60; count, the main &#x60;comment&#x60; object already has that, so no need to use this method.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public void getAllUsersWhoLikedAComment(Integer id, String traktApiVersion, String traktApiKey) throws ApiException {
        getAllUsersWhoLikedACommentWithHttpInfo(id, traktApiVersion, traktApiKey);
    }

    /**
     * Get all users who liked a comment
     * #### &amp;#128196; Pagination  Returns all users who liked a comment. If you only need the &#x60;replies&#x60; count, the main &#x60;comment&#x60; object already has that, so no need to use this method.
     * @param id A specific comment ID. (required)
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
    public ApiResponse<Void> getAllUsersWhoLikedACommentWithHttpInfo(Integer id, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getAllUsersWhoLikedACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get all users who liked a comment (asynchronously)
     * #### &amp;#128196; Pagination  Returns all users who liked a comment. If you only need the &#x60;replies&#x60; count, the main &#x60;comment&#x60; object already has that, so no need to use this method.
     * @param id A specific comment ID. (required)
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
    public okhttp3.Call getAllUsersWhoLikedACommentAsync(Integer id, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllUsersWhoLikedACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRecentlyCreatedComments
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public okhttp3.Call getRecentlyCreatedCommentsCall(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/recent/{comment_type}/{type}"
            .replace("{" + "comment_type" + "}", localVarApiClient.escapeString(commentType.toString()))
            .replace("{" + "type" + "}", localVarApiClient.escapeString(type.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (includeReplies != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("include_replies", includeReplies));
        }

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
    private okhttp3.Call getRecentlyCreatedCommentsValidateBeforeCall(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'commentType' is set
        if (commentType == null) {
            throw new ApiException("Missing the required parameter 'commentType' when calling getRecentlyCreatedComments(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling getRecentlyCreatedComments(Async)");
        }

        return getRecentlyCreatedCommentsCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get recently created comments
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently written comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public void getRecentlyCreatedComments(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey) throws ApiException {
        getRecentlyCreatedCommentsWithHttpInfo(commentType, type, includeReplies, traktApiVersion, traktApiKey);
    }

    /**
     * Get recently created comments
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently written comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public ApiResponse<Void> getRecentlyCreatedCommentsWithHttpInfo(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getRecentlyCreatedCommentsValidateBeforeCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get recently created comments (asynchronously)
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently written comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public okhttp3.Call getRecentlyCreatedCommentsAsync(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRecentlyCreatedCommentsValidateBeforeCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRecentlyUpdatedComments
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public okhttp3.Call getRecentlyUpdatedCommentsCall(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/updates/{comment_type}/{type}"
            .replace("{" + "comment_type" + "}", localVarApiClient.escapeString(commentType.toString()))
            .replace("{" + "type" + "}", localVarApiClient.escapeString(type.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (includeReplies != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("include_replies", includeReplies));
        }

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
    private okhttp3.Call getRecentlyUpdatedCommentsValidateBeforeCall(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'commentType' is set
        if (commentType == null) {
            throw new ApiException("Missing the required parameter 'commentType' when calling getRecentlyUpdatedComments(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling getRecentlyUpdatedComments(Async)");
        }

        return getRecentlyUpdatedCommentsCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get recently updated comments
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently updated comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public void getRecentlyUpdatedComments(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey) throws ApiException {
        getRecentlyUpdatedCommentsWithHttpInfo(commentType, type, includeReplies, traktApiVersion, traktApiKey);
    }

    /**
     * Get recently updated comments
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently updated comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public ApiResponse<Void> getRecentlyUpdatedCommentsWithHttpInfo(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getRecentlyUpdatedCommentsValidateBeforeCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get recently updated comments (asynchronously)
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the most recently updated comments across all of Trakt. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public okhttp3.Call getRecentlyUpdatedCommentsAsync(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRecentlyUpdatedCommentsValidateBeforeCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRepliesForAComment
     * @param id A specific comment ID. (required)
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
    public okhttp3.Call getRepliesForACommentCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/{id}/replies"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
    private okhttp3.Call getRepliesForACommentValidateBeforeCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getRepliesForAComment(Async)");
        }

        return getRepliesForACommentCall(id, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get replies for a comment
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all replies for a comment. It is possible these replies could have replies themselves, so in that case you would just call [**_/comments/:id/replies**](/reference/comments/replies/) again with the new comment &#x60;id&#x60;.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public void getRepliesForAComment(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        getRepliesForACommentWithHttpInfo(id, traktApiVersion, traktApiKey);
    }

    /**
     * Get replies for a comment
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all replies for a comment. It is possible these replies could have replies themselves, so in that case you would just call [**_/comments/:id/replies**](/reference/comments/replies/) again with the new comment &#x60;id&#x60;.
     * @param id A specific comment ID. (required)
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
    public ApiResponse<Void> getRepliesForACommentWithHttpInfo(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getRepliesForACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get replies for a comment (asynchronously)
     * #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all replies for a comment. It is possible these replies could have replies themselves, so in that case you would just call [**_/comments/:id/replies**](/reference/comments/replies/) again with the new comment &#x60;id&#x60;.
     * @param id A specific comment ID. (required)
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
    public okhttp3.Call getRepliesForACommentAsync(String id, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRepliesForACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTheAttachedMediaItem
     * @param id A specific comment ID. (required)
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
    public okhttp3.Call getTheAttachedMediaItemCall(Integer id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/{id}/item"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
    private okhttp3.Call getTheAttachedMediaItemValidateBeforeCall(Integer id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getTheAttachedMediaItem(Async)");
        }

        return getTheAttachedMediaItemCall(id, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get the attached media item
     * #### &amp;#10024; Extended Info  Returns the media item this comment is attached to. The media type can be &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; and it also returns the standard media object for that media type.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void getTheAttachedMediaItem(Integer id, String traktApiVersion, String traktApiKey) throws ApiException {
        getTheAttachedMediaItemWithHttpInfo(id, traktApiVersion, traktApiKey);
    }

    /**
     * Get the attached media item
     * #### &amp;#10024; Extended Info  Returns the media item this comment is attached to. The media type can be &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; and it also returns the standard media object for that media type.
     * @param id A specific comment ID. (required)
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
    public ApiResponse<Void> getTheAttachedMediaItemWithHttpInfo(Integer id, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getTheAttachedMediaItemValidateBeforeCall(id, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get the attached media item (asynchronously)
     * #### &amp;#10024; Extended Info  Returns the media item this comment is attached to. The media type can be &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; and it also returns the standard media object for that media type.
     * @param id A specific comment ID. (required)
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
    public okhttp3.Call getTheAttachedMediaItemAsync(Integer id, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTheAttachedMediaItemValidateBeforeCall(id, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTrendingComments
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public okhttp3.Call getTrendingCommentsCall(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/trending/{comment_type}/{type}"
            .replace("{" + "comment_type" + "}", localVarApiClient.escapeString(commentType.toString()))
            .replace("{" + "type" + "}", localVarApiClient.escapeString(type.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (includeReplies != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("include_replies", includeReplies));
        }

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
    private okhttp3.Call getTrendingCommentsValidateBeforeCall(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'commentType' is set
        if (commentType == null) {
            throw new ApiException("Missing the required parameter 'commentType' when calling getTrendingComments(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling getTrendingComments(Async)");
        }

        return getTrendingCommentsCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Get trending comments
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all comments with the most likes and replies over the last 7 days. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  </td></tr>
     </table>
     */
    public void getTrendingComments(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey) throws ApiException {
        getTrendingCommentsWithHttpInfo(commentType, type, includeReplies, traktApiVersion, traktApiKey);
    }

    /**
     * Get trending comments
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all comments with the most likes and replies over the last 7 days. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public ApiResponse<Void> getTrendingCommentsWithHttpInfo(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = getTrendingCommentsValidateBeforeCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get trending comments (asynchronously)
     * #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all comments with the most likes and replies over the last 7 days. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned. If you want to &#x60;include_replies&#x60; that will return replies in place alongside top level comments.
     * @param commentType  (required)
     * @param type  (required)
     * @param includeReplies include comment replies (optional)
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
    public okhttp3.Call getTrendingCommentsAsync(String commentType, String type, String includeReplies, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTrendingCommentsValidateBeforeCall(commentType, type, includeReplies, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for likeAComment
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call likeACommentCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/{id}/like"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call likeACommentValidateBeforeCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling likeAComment(Async)");
        }

        return likeACommentCall(id, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Like a comment
     * #### &amp;#128274; OAuth Required  Votes help determine popular comments. Only one like is allowed per comment per user.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void likeAComment(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        likeACommentWithHttpInfo(id, traktApiVersion, traktApiKey);
    }

    /**
     * Like a comment
     * #### &amp;#128274; OAuth Required  Votes help determine popular comments. Only one like is allowed per comment per user.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> likeACommentWithHttpInfo(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = likeACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Like a comment (asynchronously)
     * #### &amp;#128274; OAuth Required  Votes help determine popular comments. Only one like is allowed per comment per user.
     * @param id A specific comment ID. (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call likeACommentAsync(String id, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = likeACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for postAComment
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postACommentRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postACommentCall(String traktApiVersion, String traktApiKey, PostACommentRequest postACommentRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postACommentRequest;

        // create path and map variables
        String localVarPath = "/comments";

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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postACommentValidateBeforeCall(String traktApiVersion, String traktApiKey, PostACommentRequest postACommentRequest, final ApiCallback _callback) throws ApiException {
        return postACommentCall(traktApiVersion, traktApiKey, postACommentRequest, _callback);

    }

    /**
     * Post a comment
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new comment to a movie, show, season, episode, or list. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | | &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; object. (see examples &amp;#8594;) | | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? | | &#x60;sharing&#x60;  | object | | Control sharing to any connected social networks. (see below &amp;#8595;) |  #### Sharing  The &#x60;sharing&#x60; object is optional and will apply the user&#39;s settings if not sent. If &#x60;sharing&#x60; is sent, each key will override the user&#39;s setting for that social network. Send &#x60;true&#x60; to post or &#x60;false&#x60; to not post on the indicated social network. You can see which social networks a user has connected with the [**_/users/settings**](/reference/users/settings) method.  | Key | Type | |---|---| | &#x60;twitter&#x60; | boolean | | &#x60;tumblr&#x60; | boolean | | &#x60;medium&#x60; | boolean |
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postACommentRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public void postAComment(String traktApiVersion, String traktApiKey, PostACommentRequest postACommentRequest) throws ApiException {
        postACommentWithHttpInfo(traktApiVersion, traktApiKey, postACommentRequest);
    }

    /**
     * Post a comment
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new comment to a movie, show, season, episode, or list. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | | &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; object. (see examples &amp;#8594;) | | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? | | &#x60;sharing&#x60;  | object | | Control sharing to any connected social networks. (see below &amp;#8595;) |  #### Sharing  The &#x60;sharing&#x60; object is optional and will apply the user&#39;s settings if not sent. If &#x60;sharing&#x60; is sent, each key will override the user&#39;s setting for that social network. Send &#x60;true&#x60; to post or &#x60;false&#x60; to not post on the indicated social network. You can see which social networks a user has connected with the [**_/users/settings**](/reference/users/settings) method.  | Key | Type | |---|---| | &#x60;twitter&#x60; | boolean | | &#x60;tumblr&#x60; | boolean | | &#x60;medium&#x60; | boolean |
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postACommentRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> postACommentWithHttpInfo(String traktApiVersion, String traktApiKey, PostACommentRequest postACommentRequest) throws ApiException {
        okhttp3.Call localVarCall = postACommentValidateBeforeCall(traktApiVersion, traktApiKey, postACommentRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Post a comment (asynchronously)
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new comment to a movie, show, season, episode, or list. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | | &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;list&#x60; object. (see examples &amp;#8594;) | | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? | | &#x60;sharing&#x60;  | object | | Control sharing to any connected social networks. (see below &amp;#8595;) |  #### Sharing  The &#x60;sharing&#x60; object is optional and will apply the user&#39;s settings if not sent. If &#x60;sharing&#x60; is sent, each key will override the user&#39;s setting for that social network. Send &#x60;true&#x60; to post or &#x60;false&#x60; to not post on the indicated social network. You can see which social networks a user has connected with the [**_/users/settings**](/reference/users/settings) method.  | Key | Type | |---|---| | &#x60;twitter&#x60; | boolean | | &#x60;tumblr&#x60; | boolean | | &#x60;medium&#x60; | boolean |
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postACommentRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postACommentAsync(String traktApiVersion, String traktApiKey, PostACommentRequest postACommentRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = postACommentValidateBeforeCall(traktApiVersion, traktApiKey, postACommentRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for postAReplyForAComment
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postAReplyForACommentRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAReplyForACommentCall(String id, String traktApiVersion, String traktApiKey, PostAReplyForACommentRequest postAReplyForACommentRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postAReplyForACommentRequest;

        // create path and map variables
        String localVarPath = "/comments/{id}/replies"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postAReplyForACommentValidateBeforeCall(String id, String traktApiVersion, String traktApiKey, PostAReplyForACommentRequest postAReplyForACommentRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postAReplyForAComment(Async)");
        }

        return postAReplyForACommentCall(id, traktApiVersion, traktApiKey, postAReplyForACommentRequest, _callback);

    }

    /**
     * Post a reply for a comment
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new reply to an existing comment. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the reply. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postAReplyForACommentRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public void postAReplyForAComment(String id, String traktApiVersion, String traktApiKey, PostAReplyForACommentRequest postAReplyForACommentRequest) throws ApiException {
        postAReplyForACommentWithHttpInfo(id, traktApiVersion, traktApiKey, postAReplyForACommentRequest);
    }

    /**
     * Post a reply for a comment
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new reply to an existing comment. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the reply. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postAReplyForACommentRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> postAReplyForACommentWithHttpInfo(String id, String traktApiVersion, String traktApiKey, PostAReplyForACommentRequest postAReplyForACommentRequest) throws ApiException {
        okhttp3.Call localVarCall = postAReplyForACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, postAReplyForACommentRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Post a reply for a comment (asynchronously)
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Add a new reply to an existing comment. Make sure to allow and encourage *spoilers* to be indicated in your app and follow the rules listed above.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Text for the reply. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param postAReplyForACommentRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAReplyForACommentAsync(String id, String traktApiVersion, String traktApiKey, PostAReplyForACommentRequest postAReplyForACommentRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = postAReplyForACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, postAReplyForACommentRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for removeLikeOnAComment
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeLikeOnACommentCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/comments/{id}/like"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call removeLikeOnACommentValidateBeforeCall(String id, String traktApiVersion, String traktApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling removeLikeOnAComment(Async)");
        }

        return removeLikeOnACommentCall(id, traktApiVersion, traktApiKey, _callback);

    }

    /**
     * Remove like on a comment
     * #### &amp;#128274; OAuth Required  Remove a like on a comment.
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void removeLikeOnAComment(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        removeLikeOnACommentWithHttpInfo(id, traktApiVersion, traktApiKey);
    }

    /**
     * Remove like on a comment
     * #### &amp;#128274; OAuth Required  Remove a like on a comment.
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> removeLikeOnACommentWithHttpInfo(String id, String traktApiVersion, String traktApiKey) throws ApiException {
        okhttp3.Call localVarCall = removeLikeOnACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Remove like on a comment (asynchronously)
     * #### &amp;#128274; OAuth Required  Remove a like on a comment.
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeLikeOnACommentAsync(String id, String traktApiVersion, String traktApiKey, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = removeLikeOnACommentValidateBeforeCall(id, traktApiVersion, traktApiKey, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateACommentOrReply
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param updateACommentOrReplyRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateACommentOrReplyCall(String id, String traktApiVersion, String traktApiKey, UpdateACommentOrReplyRequest updateACommentOrReplyRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateACommentOrReplyRequest;

        // create path and map variables
        String localVarPath = "/comments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateACommentOrReplyValidateBeforeCall(String id, String traktApiVersion, String traktApiKey, UpdateACommentOrReplyRequest updateACommentOrReplyRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling updateACommentOrReply(Async)");
        }

        return updateACommentOrReplyCall(id, traktApiVersion, traktApiKey, updateACommentOrReplyRequest, _callback);

    }

    /**
     * Update a comment or reply
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Update a single comment. The OAuth user must match the author of the comment in order to update it. If not, a &#x60;401&#x60; HTTP status is returned.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param updateACommentOrReplyRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void updateACommentOrReply(String id, String traktApiVersion, String traktApiKey, UpdateACommentOrReplyRequest updateACommentOrReplyRequest) throws ApiException {
        updateACommentOrReplyWithHttpInfo(id, traktApiVersion, traktApiKey, updateACommentOrReplyRequest);
    }

    /**
     * Update a comment or reply
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Update a single comment. The OAuth user must match the author of the comment in order to update it. If not, a &#x60;401&#x60; HTTP status is returned.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param updateACommentOrReplyRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updateACommentOrReplyWithHttpInfo(String id, String traktApiVersion, String traktApiKey, UpdateACommentOrReplyRequest updateACommentOrReplyRequest) throws ApiException {
        okhttp3.Call localVarCall = updateACommentOrReplyValidateBeforeCall(id, traktApiVersion, traktApiKey, updateACommentOrReplyRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a comment or reply (asynchronously)
     * #### &amp;#128274; OAuth Required &amp;#128513; Emojis  Update a single comment. The OAuth user must match the author of the comment in order to update it. If not, a &#x60;401&#x60; HTTP status is returned.  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;comment&#x60; | string |  | Text for the comment. | | &#x60;spoiler&#x60; | boolean | &#x60;false&#x60; | Is this a spoiler? |
     * @param id Automatically added (required)
     * @param traktApiVersion e.g. 2 (optional)
     * @param traktApiKey e.g. [client_id] (optional)
     * @param updateACommentOrReplyRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateACommentOrReplyAsync(String id, String traktApiVersion, String traktApiKey, UpdateACommentOrReplyRequest updateACommentOrReplyRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateACommentOrReplyValidateBeforeCall(id, traktApiVersion, traktApiKey, updateACommentOrReplyRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
