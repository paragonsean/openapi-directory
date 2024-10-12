/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
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


import org.openapitools.client.model.VideoCommentsForXMLInner;
import org.openapitools.client.model.VideoPrivacySet;
import org.openapitools.client.model.VideosForXMLInner;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VideoFeedsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VideoFeedsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VideoFeedsApi(ApiClient apiClient) {
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
     * Build call for getSyndicatedComments
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param videoId limit listing to a specific video (optional)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 400 </td><td> Arises when:   - videoId filter is mixed with a channel filter  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video, video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSyndicatedCommentsCall(String format, String videoId, String accountId, String accountName, String videoChannelId, String videoChannelName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/feeds/video-comments.{format}"
            .replace("{" + "format" + "}", localVarApiClient.escapeString(format.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (videoId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("videoId", videoId));
        }

        if (accountId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("accountId", accountId));
        }

        if (accountName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("accountName", accountName));
        }

        if (videoChannelId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("videoChannelId", videoChannelId));
        }

        if (videoChannelName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("videoChannelName", videoChannelName));
        }

        final String[] localVarAccepts = {
            "application/atom+xml",
            "application/json",
            "application/rss+xml",
            "application/xml",
            "text/xml"
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
    private okhttp3.Call getSyndicatedCommentsValidateBeforeCall(String format, String videoId, String accountId, String accountName, String videoChannelId, String videoChannelName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling getSyndicatedComments(Async)");
        }

        return getSyndicatedCommentsCall(format, videoId, accountId, accountName, videoChannelId, videoChannelName, _callback);

    }

    /**
     * List comments on videos
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param videoId limit listing to a specific video (optional)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @return List&lt;VideoCommentsForXMLInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 400 </td><td> Arises when:   - videoId filter is mixed with a channel filter  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video, video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public List<VideoCommentsForXMLInner> getSyndicatedComments(String format, String videoId, String accountId, String accountName, String videoChannelId, String videoChannelName) throws ApiException {
        ApiResponse<List<VideoCommentsForXMLInner>> localVarResp = getSyndicatedCommentsWithHttpInfo(format, videoId, accountId, accountName, videoChannelId, videoChannelName);
        return localVarResp.getData();
    }

    /**
     * List comments on videos
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param videoId limit listing to a specific video (optional)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @return ApiResponse&lt;List&lt;VideoCommentsForXMLInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 400 </td><td> Arises when:   - videoId filter is mixed with a channel filter  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video, video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<VideoCommentsForXMLInner>> getSyndicatedCommentsWithHttpInfo(String format, String videoId, String accountId, String accountName, String videoChannelId, String videoChannelName) throws ApiException {
        okhttp3.Call localVarCall = getSyndicatedCommentsValidateBeforeCall(format, videoId, accountId, accountName, videoChannelId, videoChannelName, null);
        Type localVarReturnType = new TypeToken<List<VideoCommentsForXMLInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List comments on videos (asynchronously)
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param videoId limit listing to a specific video (optional)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 400 </td><td> Arises when:   - videoId filter is mixed with a channel filter  </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video, video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSyndicatedCommentsAsync(String format, String videoId, String accountId, String accountName, String videoChannelId, String videoChannelName, final ApiCallback<List<VideoCommentsForXMLInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSyndicatedCommentsValidateBeforeCall(format, videoId, accountId, accountName, videoChannelId, videoChannelName, _callback);
        Type localVarReturnType = new TypeToken<List<VideoCommentsForXMLInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSyndicatedSubscriptionVideos
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (required)
     * @param token private token allowing access (required)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSyndicatedSubscriptionVideosCall(String format, String accountId, String token, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/feeds/subscriptions.{format}"
            .replace("{" + "format" + "}", localVarApiClient.escapeString(format.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accountId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("accountId", accountId));
        }

        if (token != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("token", token));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (nsfw != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nsfw", nsfw));
        }

        if (isLocal != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("isLocal", isLocal));
        }

        if (include != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("include", include));
        }

        if (privacyOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("privacyOneOf", privacyOneOf));
        }

        if (hasHLSFiles != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("hasHLSFiles", hasHLSFiles));
        }

        if (hasWebtorrentFiles != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("hasWebtorrentFiles", hasWebtorrentFiles));
        }

        final String[] localVarAccepts = {
            "application/atom+xml",
            "application/json",
            "application/rss+xml",
            "application/xml",
            "text/xml"
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
    private okhttp3.Call getSyndicatedSubscriptionVideosValidateBeforeCall(String format, String accountId, String token, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling getSyndicatedSubscriptionVideos(Async)");
        }

        // verify the required parameter 'accountId' is set
        if (accountId == null) {
            throw new ApiException("Missing the required parameter 'accountId' when calling getSyndicatedSubscriptionVideos(Async)");
        }

        // verify the required parameter 'token' is set
        if (token == null) {
            throw new ApiException("Missing the required parameter 'token' when calling getSyndicatedSubscriptionVideos(Async)");
        }

        return getSyndicatedSubscriptionVideosCall(format, accountId, token, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, _callback);

    }

    /**
     * List videos of subscriptions tied to a token
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (required)
     * @param token private token allowing access (required)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @return List&lt;VideosForXMLInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public List<VideosForXMLInner> getSyndicatedSubscriptionVideos(String format, String accountId, String token, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles) throws ApiException {
        ApiResponse<List<VideosForXMLInner>> localVarResp = getSyndicatedSubscriptionVideosWithHttpInfo(format, accountId, token, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles);
        return localVarResp.getData();
    }

    /**
     * List videos of subscriptions tied to a token
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (required)
     * @param token private token allowing access (required)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @return ApiResponse&lt;List&lt;VideosForXMLInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<VideosForXMLInner>> getSyndicatedSubscriptionVideosWithHttpInfo(String format, String accountId, String token, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles) throws ApiException {
        okhttp3.Call localVarCall = getSyndicatedSubscriptionVideosValidateBeforeCall(format, accountId, token, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, null);
        Type localVarReturnType = new TypeToken<List<VideosForXMLInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videos of subscriptions tied to a token (asynchronously)
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (required)
     * @param token private token allowing access (required)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSyndicatedSubscriptionVideosAsync(String format, String accountId, String token, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, final ApiCallback<List<VideosForXMLInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSyndicatedSubscriptionVideosValidateBeforeCall(format, accountId, token, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, _callback);
        Type localVarReturnType = new TypeToken<List<VideosForXMLInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSyndicatedVideos
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 404 </td><td> video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSyndicatedVideosCall(String format, String accountId, String accountName, String videoChannelId, String videoChannelName, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/feeds/videos.{format}"
            .replace("{" + "format" + "}", localVarApiClient.escapeString(format.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accountId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("accountId", accountId));
        }

        if (accountName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("accountName", accountName));
        }

        if (videoChannelId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("videoChannelId", videoChannelId));
        }

        if (videoChannelName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("videoChannelName", videoChannelName));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (nsfw != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nsfw", nsfw));
        }

        if (isLocal != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("isLocal", isLocal));
        }

        if (include != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("include", include));
        }

        if (privacyOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("privacyOneOf", privacyOneOf));
        }

        if (hasHLSFiles != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("hasHLSFiles", hasHLSFiles));
        }

        if (hasWebtorrentFiles != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("hasWebtorrentFiles", hasWebtorrentFiles));
        }

        final String[] localVarAccepts = {
            "application/atom+xml",
            "application/json",
            "application/rss+xml",
            "application/xml",
            "text/xml"
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
    private okhttp3.Call getSyndicatedVideosValidateBeforeCall(String format, String accountId, String accountName, String videoChannelId, String videoChannelName, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'format' is set
        if (format == null) {
            throw new ApiException("Missing the required parameter 'format' when calling getSyndicatedVideos(Async)");
        }

        return getSyndicatedVideosCall(format, accountId, accountName, videoChannelId, videoChannelName, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, _callback);

    }

    /**
     * List videos
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @return List&lt;VideosForXMLInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 404 </td><td> video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public List<VideosForXMLInner> getSyndicatedVideos(String format, String accountId, String accountName, String videoChannelId, String videoChannelName, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles) throws ApiException {
        ApiResponse<List<VideosForXMLInner>> localVarResp = getSyndicatedVideosWithHttpInfo(format, accountId, accountName, videoChannelId, videoChannelName, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles);
        return localVarResp.getData();
    }

    /**
     * List videos
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @return ApiResponse&lt;List&lt;VideosForXMLInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 404 </td><td> video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<VideosForXMLInner>> getSyndicatedVideosWithHttpInfo(String format, String accountId, String accountName, String videoChannelId, String videoChannelName, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles) throws ApiException {
        okhttp3.Call localVarCall = getSyndicatedVideosValidateBeforeCall(format, accountId, accountName, videoChannelId, videoChannelName, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, null);
        Type localVarReturnType = new TypeToken<List<VideosForXMLInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videos (asynchronously)
     * 
     * @param format format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) (required)
     * @param accountId limit listing to a specific account (optional)
     * @param accountName limit listing to a specific account (optional)
     * @param videoChannelId limit listing to a specific video channel (optional)
     * @param videoChannelName limit listing to a specific video channel (optional)
     * @param sort Sort column (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  * Cache-Control -  <br>  </td></tr>
        <tr><td> 404 </td><td> video channel or account not found </td><td>  -  </td></tr>
        <tr><td> 406 </td><td> accept header unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSyndicatedVideosAsync(String format, String accountId, String accountName, String videoChannelId, String videoChannelName, String sort, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, final ApiCallback<List<VideosForXMLInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSyndicatedVideosValidateBeforeCall(format, accountId, accountName, videoChannelId, videoChannelName, sort, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, _callback);
        Type localVarReturnType = new TypeToken<List<VideosForXMLInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
