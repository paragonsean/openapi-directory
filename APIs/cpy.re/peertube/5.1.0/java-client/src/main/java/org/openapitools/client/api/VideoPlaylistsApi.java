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


import org.openapitools.client.model.AddPlaylist200Response;
import org.openapitools.client.model.AddVideoPlaylistVideo200Response;
import org.openapitools.client.model.AddVideoPlaylistVideoRequest;
import org.openapitools.client.model.ApiV1AccountsNameVideoPlaylistsGet200Response;
import org.openapitools.client.model.ApiV1UsersMeVideoPlaylistsVideosExistGet200Response;
import java.io.File;
import org.openapitools.client.model.PutVideoPlaylistVideoRequest;
import org.openapitools.client.model.ReorderVideoPlaylistRequest;
import org.openapitools.client.model.VideoListResponse;
import org.openapitools.client.model.VideoPlaylist;
import org.openapitools.client.model.VideoPlaylistPrivacySet;
import org.openapitools.client.model.VideoPlaylistTypeSet;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VideoPlaylistsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VideoPlaylistsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VideoPlaylistsApi(ApiClient apiClient) {
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
     * Build call for addPlaylist
     * @param displayName Video playlist display name (required)
     * @param description Video playlist description (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addPlaylistCall(String displayName, String description, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (description != null) {
            localVarFormParams.put("description", description);
        }

        if (displayName != null) {
            localVarFormParams.put("displayName", displayName);
        }

        if (privacy != null) {
            localVarFormParams.put("privacy", privacy);
        }

        if (thumbnailfile != null) {
            localVarFormParams.put("thumbnailfile", thumbnailfile);
        }

        if (videoChannelId != null) {
            localVarFormParams.put("videoChannelId", videoChannelId);
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addPlaylistValidateBeforeCall(String displayName, String description, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'displayName' is set
        if (displayName == null) {
            throw new ApiException("Missing the required parameter 'displayName' when calling addPlaylist(Async)");
        }

        return addPlaylistCall(displayName, description, privacy, thumbnailfile, videoChannelId, _callback);

    }

    /**
     * Create a video playlist
     * If the video playlist is set as public, &#x60;videoChannelId&#x60; is mandatory.
     * @param displayName Video playlist display name (required)
     * @param description Video playlist description (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @return AddPlaylist200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public AddPlaylist200Response addPlaylist(String displayName, String description, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId) throws ApiException {
        ApiResponse<AddPlaylist200Response> localVarResp = addPlaylistWithHttpInfo(displayName, description, privacy, thumbnailfile, videoChannelId);
        return localVarResp.getData();
    }

    /**
     * Create a video playlist
     * If the video playlist is set as public, &#x60;videoChannelId&#x60; is mandatory.
     * @param displayName Video playlist display name (required)
     * @param description Video playlist description (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @return ApiResponse&lt;AddPlaylist200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AddPlaylist200Response> addPlaylistWithHttpInfo(String displayName, String description, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId) throws ApiException {
        okhttp3.Call localVarCall = addPlaylistValidateBeforeCall(displayName, description, privacy, thumbnailfile, videoChannelId, null);
        Type localVarReturnType = new TypeToken<AddPlaylist200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a video playlist (asynchronously)
     * If the video playlist is set as public, &#x60;videoChannelId&#x60; is mandatory.
     * @param displayName Video playlist display name (required)
     * @param description Video playlist description (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addPlaylistAsync(String displayName, String description, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId, final ApiCallback<AddPlaylist200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = addPlaylistValidateBeforeCall(displayName, description, privacy, thumbnailfile, videoChannelId, _callback);
        Type localVarReturnType = new TypeToken<AddPlaylist200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for addVideoPlaylistVideo_0
     * @param playlistId Playlist id (required)
     * @param addVideoPlaylistVideoRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addVideoPlaylistVideo_0Call(Integer playlistId, AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addVideoPlaylistVideoRequest;

        // create path and map variables
        String localVarPath = "/api/v1/video-playlists/{playlistId}/videos"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addVideoPlaylistVideo_0ValidateBeforeCall(Integer playlistId, AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling addVideoPlaylistVideo_0(Async)");
        }

        return addVideoPlaylistVideo_0Call(playlistId, addVideoPlaylistVideoRequest, _callback);

    }

    /**
     * Add a video in a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param addVideoPlaylistVideoRequest  (optional)
     * @return AddVideoPlaylistVideo200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public AddVideoPlaylistVideo200Response addVideoPlaylistVideo_0(Integer playlistId, AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest) throws ApiException {
        ApiResponse<AddVideoPlaylistVideo200Response> localVarResp = addVideoPlaylistVideo_0WithHttpInfo(playlistId, addVideoPlaylistVideoRequest);
        return localVarResp.getData();
    }

    /**
     * Add a video in a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param addVideoPlaylistVideoRequest  (optional)
     * @return ApiResponse&lt;AddVideoPlaylistVideo200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AddVideoPlaylistVideo200Response> addVideoPlaylistVideo_0WithHttpInfo(Integer playlistId, AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest) throws ApiException {
        okhttp3.Call localVarCall = addVideoPlaylistVideo_0ValidateBeforeCall(playlistId, addVideoPlaylistVideoRequest, null);
        Type localVarReturnType = new TypeToken<AddVideoPlaylistVideo200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a video in a playlist (asynchronously)
     * 
     * @param playlistId Playlist id (required)
     * @param addVideoPlaylistVideoRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addVideoPlaylistVideo_0Async(Integer playlistId, AddVideoPlaylistVideoRequest addVideoPlaylistVideoRequest, final ApiCallback<AddVideoPlaylistVideo200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = addVideoPlaylistVideo_0ValidateBeforeCall(playlistId, addVideoPlaylistVideoRequest, _callback);
        Type localVarReturnType = new TypeToken<AddVideoPlaylistVideo200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AccountsNameVideoPlaylistsGet
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @param playlistType  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AccountsNameVideoPlaylistsGetCall(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts/{name}/video-playlists"
            .replace("{" + "name" + "}", localVarApiClient.escapeString(name.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (playlistType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("playlistType", playlistType));
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
    private okhttp3.Call apiV1AccountsNameVideoPlaylistsGetValidateBeforeCall(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling apiV1AccountsNameVideoPlaylistsGet(Async)");
        }

        return apiV1AccountsNameVideoPlaylistsGetCall(name, start, count, sort, search, playlistType, _callback);

    }

    /**
     * List playlists of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @param playlistType  (optional)
     * @return ApiV1AccountsNameVideoPlaylistsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiV1AccountsNameVideoPlaylistsGet200Response apiV1AccountsNameVideoPlaylistsGet(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType) throws ApiException {
        ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> localVarResp = apiV1AccountsNameVideoPlaylistsGetWithHttpInfo(name, start, count, sort, search, playlistType);
        return localVarResp.getData();
    }

    /**
     * List playlists of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @param playlistType  (optional)
     * @return ApiResponse&lt;ApiV1AccountsNameVideoPlaylistsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> apiV1AccountsNameVideoPlaylistsGetWithHttpInfo(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType) throws ApiException {
        okhttp3.Call localVarCall = apiV1AccountsNameVideoPlaylistsGetValidateBeforeCall(name, start, count, sort, search, playlistType, null);
        Type localVarReturnType = new TypeToken<ApiV1AccountsNameVideoPlaylistsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List playlists of an account (asynchronously)
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @param playlistType  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AccountsNameVideoPlaylistsGetAsync(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType, final ApiCallback<ApiV1AccountsNameVideoPlaylistsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AccountsNameVideoPlaylistsGetValidateBeforeCall(name, start, count, sort, search, playlistType, _callback);
        Type localVarReturnType = new TypeToken<ApiV1AccountsNameVideoPlaylistsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1UsersMeVideoPlaylistsVideosExistGet
     * @param videoIds The video ids to check (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeVideoPlaylistsVideosExistGetCall(List<Integer> videoIds, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/me/video-playlists/videos-exist";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (videoIds != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "videoIds", videoIds));
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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1UsersMeVideoPlaylistsVideosExistGetValidateBeforeCall(List<Integer> videoIds, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'videoIds' is set
        if (videoIds == null) {
            throw new ApiException("Missing the required parameter 'videoIds' when calling apiV1UsersMeVideoPlaylistsVideosExistGet(Async)");
        }

        return apiV1UsersMeVideoPlaylistsVideosExistGetCall(videoIds, _callback);

    }

    /**
     * Check video exists in my playlists
     * 
     * @param videoIds The video ids to check (required)
     * @return ApiV1UsersMeVideoPlaylistsVideosExistGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiV1UsersMeVideoPlaylistsVideosExistGet200Response apiV1UsersMeVideoPlaylistsVideosExistGet(List<Integer> videoIds) throws ApiException {
        ApiResponse<ApiV1UsersMeVideoPlaylistsVideosExistGet200Response> localVarResp = apiV1UsersMeVideoPlaylistsVideosExistGetWithHttpInfo(videoIds);
        return localVarResp.getData();
    }

    /**
     * Check video exists in my playlists
     * 
     * @param videoIds The video ids to check (required)
     * @return ApiResponse&lt;ApiV1UsersMeVideoPlaylistsVideosExistGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiV1UsersMeVideoPlaylistsVideosExistGet200Response> apiV1UsersMeVideoPlaylistsVideosExistGetWithHttpInfo(List<Integer> videoIds) throws ApiException {
        okhttp3.Call localVarCall = apiV1UsersMeVideoPlaylistsVideosExistGetValidateBeforeCall(videoIds, null);
        Type localVarReturnType = new TypeToken<ApiV1UsersMeVideoPlaylistsVideosExistGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Check video exists in my playlists (asynchronously)
     * 
     * @param videoIds The video ids to check (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeVideoPlaylistsVideosExistGetAsync(List<Integer> videoIds, final ApiCallback<ApiV1UsersMeVideoPlaylistsVideosExistGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1UsersMeVideoPlaylistsVideosExistGetValidateBeforeCall(videoIds, _callback);
        Type localVarReturnType = new TypeToken<ApiV1UsersMeVideoPlaylistsVideosExistGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideoChannelsChannelHandleVideoPlaylistsGet
     * @param channelHandle The video channel handle (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoChannelsChannelHandleVideoPlaylistsGetCall(String channelHandle, Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-channels/{channelHandle}/video-playlists"
            .replace("{" + "channelHandle" + "}", localVarApiClient.escapeString(channelHandle.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (playlistType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("playlistType", playlistType));
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
    private okhttp3.Call apiV1VideoChannelsChannelHandleVideoPlaylistsGetValidateBeforeCall(String channelHandle, Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'channelHandle' is set
        if (channelHandle == null) {
            throw new ApiException("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleVideoPlaylistsGet(Async)");
        }

        return apiV1VideoChannelsChannelHandleVideoPlaylistsGetCall(channelHandle, start, count, sort, playlistType, _callback);

    }

    /**
     * List playlists of a channel
     * 
     * @param channelHandle The video channel handle (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @return ApiV1AccountsNameVideoPlaylistsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiV1AccountsNameVideoPlaylistsGet200Response apiV1VideoChannelsChannelHandleVideoPlaylistsGet(String channelHandle, Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType) throws ApiException {
        ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> localVarResp = apiV1VideoChannelsChannelHandleVideoPlaylistsGetWithHttpInfo(channelHandle, start, count, sort, playlistType);
        return localVarResp.getData();
    }

    /**
     * List playlists of a channel
     * 
     * @param channelHandle The video channel handle (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @return ApiResponse&lt;ApiV1AccountsNameVideoPlaylistsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> apiV1VideoChannelsChannelHandleVideoPlaylistsGetWithHttpInfo(String channelHandle, Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideoChannelsChannelHandleVideoPlaylistsGetValidateBeforeCall(channelHandle, start, count, sort, playlistType, null);
        Type localVarReturnType = new TypeToken<ApiV1AccountsNameVideoPlaylistsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List playlists of a channel (asynchronously)
     * 
     * @param channelHandle The video channel handle (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoChannelsChannelHandleVideoPlaylistsGetAsync(String channelHandle, Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType, final ApiCallback<ApiV1AccountsNameVideoPlaylistsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideoChannelsChannelHandleVideoPlaylistsGetValidateBeforeCall(channelHandle, start, count, sort, playlistType, _callback);
        Type localVarReturnType = new TypeToken<ApiV1AccountsNameVideoPlaylistsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideoPlaylistsPlaylistIdDelete
     * @param playlistId Playlist id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoPlaylistsPlaylistIdDeleteCall(Integer playlistId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists/{playlistId}"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1VideoPlaylistsPlaylistIdDeleteValidateBeforeCall(Integer playlistId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling apiV1VideoPlaylistsPlaylistIdDelete(Async)");
        }

        return apiV1VideoPlaylistsPlaylistIdDeleteCall(playlistId, _callback);

    }

    /**
     * Delete a video playlist
     * 
     * @param playlistId Playlist id (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1VideoPlaylistsPlaylistIdDelete(Integer playlistId) throws ApiException {
        apiV1VideoPlaylistsPlaylistIdDeleteWithHttpInfo(playlistId);
    }

    /**
     * Delete a video playlist
     * 
     * @param playlistId Playlist id (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1VideoPlaylistsPlaylistIdDeleteWithHttpInfo(Integer playlistId) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideoPlaylistsPlaylistIdDeleteValidateBeforeCall(playlistId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a video playlist (asynchronously)
     * 
     * @param playlistId Playlist id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoPlaylistsPlaylistIdDeleteAsync(Integer playlistId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideoPlaylistsPlaylistIdDeleteValidateBeforeCall(playlistId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideoPlaylistsPlaylistIdGet
     * @param playlistId Playlist id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoPlaylistsPlaylistIdGetCall(Integer playlistId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists/{playlistId}"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call apiV1VideoPlaylistsPlaylistIdGetValidateBeforeCall(Integer playlistId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling apiV1VideoPlaylistsPlaylistIdGet(Async)");
        }

        return apiV1VideoPlaylistsPlaylistIdGetCall(playlistId, _callback);

    }

    /**
     * Get a video playlist
     * 
     * @param playlistId Playlist id (required)
     * @return VideoPlaylist
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoPlaylist apiV1VideoPlaylistsPlaylistIdGet(Integer playlistId) throws ApiException {
        ApiResponse<VideoPlaylist> localVarResp = apiV1VideoPlaylistsPlaylistIdGetWithHttpInfo(playlistId);
        return localVarResp.getData();
    }

    /**
     * Get a video playlist
     * 
     * @param playlistId Playlist id (required)
     * @return ApiResponse&lt;VideoPlaylist&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoPlaylist> apiV1VideoPlaylistsPlaylistIdGetWithHttpInfo(Integer playlistId) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideoPlaylistsPlaylistIdGetValidateBeforeCall(playlistId, null);
        Type localVarReturnType = new TypeToken<VideoPlaylist>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a video playlist (asynchronously)
     * 
     * @param playlistId Playlist id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoPlaylistsPlaylistIdGetAsync(Integer playlistId, final ApiCallback<VideoPlaylist> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideoPlaylistsPlaylistIdGetValidateBeforeCall(playlistId, _callback);
        Type localVarReturnType = new TypeToken<VideoPlaylist>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideoPlaylistsPlaylistIdPut
     * @param playlistId Playlist id (required)
     * @param description Video playlist description (optional)
     * @param displayName Video playlist display name (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoPlaylistsPlaylistIdPutCall(Integer playlistId, String description, String displayName, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists/{playlistId}"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (description != null) {
            localVarFormParams.put("description", description);
        }

        if (displayName != null) {
            localVarFormParams.put("displayName", displayName);
        }

        if (privacy != null) {
            localVarFormParams.put("privacy", privacy);
        }

        if (thumbnailfile != null) {
            localVarFormParams.put("thumbnailfile", thumbnailfile);
        }

        if (videoChannelId != null) {
            localVarFormParams.put("videoChannelId", videoChannelId);
        }

        final String[] localVarAccepts = {
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1VideoPlaylistsPlaylistIdPutValidateBeforeCall(Integer playlistId, String description, String displayName, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling apiV1VideoPlaylistsPlaylistIdPut(Async)");
        }

        return apiV1VideoPlaylistsPlaylistIdPutCall(playlistId, description, displayName, privacy, thumbnailfile, videoChannelId, _callback);

    }

    /**
     * Update a video playlist
     * If the video playlist is set as public, the playlist must have a assigned channel.
     * @param playlistId Playlist id (required)
     * @param description Video playlist description (optional)
     * @param displayName Video playlist display name (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1VideoPlaylistsPlaylistIdPut(Integer playlistId, String description, String displayName, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId) throws ApiException {
        apiV1VideoPlaylistsPlaylistIdPutWithHttpInfo(playlistId, description, displayName, privacy, thumbnailfile, videoChannelId);
    }

    /**
     * Update a video playlist
     * If the video playlist is set as public, the playlist must have a assigned channel.
     * @param playlistId Playlist id (required)
     * @param description Video playlist description (optional)
     * @param displayName Video playlist display name (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1VideoPlaylistsPlaylistIdPutWithHttpInfo(Integer playlistId, String description, String displayName, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideoPlaylistsPlaylistIdPutValidateBeforeCall(playlistId, description, displayName, privacy, thumbnailfile, videoChannelId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a video playlist (asynchronously)
     * If the video playlist is set as public, the playlist must have a assigned channel.
     * @param playlistId Playlist id (required)
     * @param description Video playlist description (optional)
     * @param displayName Video playlist display name (optional)
     * @param privacy  (optional)
     * @param thumbnailfile Video playlist thumbnail file (optional)
     * @param videoChannelId Video channel in which the playlist will be published (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideoPlaylistsPlaylistIdPutAsync(Integer playlistId, String description, String displayName, VideoPlaylistPrivacySet privacy, File thumbnailfile, Integer videoChannelId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideoPlaylistsPlaylistIdPutValidateBeforeCall(playlistId, description, displayName, privacy, thumbnailfile, videoChannelId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for delVideoPlaylistVideo
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delVideoPlaylistVideoCall(Integer playlistId, Integer playlistElementId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists/{playlistId}/videos/{playlistElementId}"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()))
            .replace("{" + "playlistElementId" + "}", localVarApiClient.escapeString(playlistElementId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call delVideoPlaylistVideoValidateBeforeCall(Integer playlistId, Integer playlistElementId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling delVideoPlaylistVideo(Async)");
        }

        // verify the required parameter 'playlistElementId' is set
        if (playlistElementId == null) {
            throw new ApiException("Missing the required parameter 'playlistElementId' when calling delVideoPlaylistVideo(Async)");
        }

        return delVideoPlaylistVideoCall(playlistId, playlistElementId, _callback);

    }

    /**
     * Delete an element from a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void delVideoPlaylistVideo(Integer playlistId, Integer playlistElementId) throws ApiException {
        delVideoPlaylistVideoWithHttpInfo(playlistId, playlistElementId);
    }

    /**
     * Delete an element from a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> delVideoPlaylistVideoWithHttpInfo(Integer playlistId, Integer playlistElementId) throws ApiException {
        okhttp3.Call localVarCall = delVideoPlaylistVideoValidateBeforeCall(playlistId, playlistElementId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete an element from a playlist (asynchronously)
     * 
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delVideoPlaylistVideoAsync(Integer playlistId, Integer playlistElementId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = delVideoPlaylistVideoValidateBeforeCall(playlistId, playlistElementId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPlaylistPrivacyPolicies
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPlaylistPrivacyPoliciesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists/privacies";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call getPlaylistPrivacyPoliciesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getPlaylistPrivacyPoliciesCall(_callback);

    }

    /**
     * List available playlist privacy policies
     * 
     * @return List&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<String> getPlaylistPrivacyPolicies() throws ApiException {
        ApiResponse<List<String>> localVarResp = getPlaylistPrivacyPoliciesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List available playlist privacy policies
     * 
     * @return ApiResponse&lt;List&lt;String&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<String>> getPlaylistPrivacyPoliciesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getPlaylistPrivacyPoliciesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List available playlist privacy policies (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPlaylistPrivacyPoliciesAsync(final ApiCallback<List<String>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPlaylistPrivacyPoliciesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPlaylists
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPlaylistsCall(Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (playlistType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("playlistType", playlistType));
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
    private okhttp3.Call getPlaylistsValidateBeforeCall(Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
        return getPlaylistsCall(start, count, sort, playlistType, _callback);

    }

    /**
     * List video playlists
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @return ApiV1AccountsNameVideoPlaylistsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiV1AccountsNameVideoPlaylistsGet200Response getPlaylists(Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType) throws ApiException {
        ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> localVarResp = getPlaylistsWithHttpInfo(start, count, sort, playlistType);
        return localVarResp.getData();
    }

    /**
     * List video playlists
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @return ApiResponse&lt;ApiV1AccountsNameVideoPlaylistsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> getPlaylistsWithHttpInfo(Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType) throws ApiException {
        okhttp3.Call localVarCall = getPlaylistsValidateBeforeCall(start, count, sort, playlistType, null);
        Type localVarReturnType = new TypeToken<ApiV1AccountsNameVideoPlaylistsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List video playlists (asynchronously)
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param playlistType  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPlaylistsAsync(Integer start, Integer count, String sort, VideoPlaylistTypeSet playlistType, final ApiCallback<ApiV1AccountsNameVideoPlaylistsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPlaylistsValidateBeforeCall(start, count, sort, playlistType, _callback);
        Type localVarReturnType = new TypeToken<ApiV1AccountsNameVideoPlaylistsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideoPlaylistVideos_0
     * @param playlistId Playlist id (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideoPlaylistVideos_0Call(Integer playlistId, Integer start, Integer count, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-playlists/{playlistId}/videos"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
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
    private okhttp3.Call getVideoPlaylistVideos_0ValidateBeforeCall(Integer playlistId, Integer start, Integer count, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling getVideoPlaylistVideos_0(Async)");
        }

        return getVideoPlaylistVideos_0Call(playlistId, start, count, _callback);

    }

    /**
     * List videos of a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @return VideoListResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoListResponse getVideoPlaylistVideos_0(Integer playlistId, Integer start, Integer count) throws ApiException {
        ApiResponse<VideoListResponse> localVarResp = getVideoPlaylistVideos_0WithHttpInfo(playlistId, start, count);
        return localVarResp.getData();
    }

    /**
     * List videos of a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @return ApiResponse&lt;VideoListResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoListResponse> getVideoPlaylistVideos_0WithHttpInfo(Integer playlistId, Integer start, Integer count) throws ApiException {
        okhttp3.Call localVarCall = getVideoPlaylistVideos_0ValidateBeforeCall(playlistId, start, count, null);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videos of a playlist (asynchronously)
     * 
     * @param playlistId Playlist id (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideoPlaylistVideos_0Async(Integer playlistId, Integer start, Integer count, final ApiCallback<VideoListResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideoPlaylistVideos_0ValidateBeforeCall(playlistId, start, count, _callback);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putVideoPlaylistVideo
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @param putVideoPlaylistVideoRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putVideoPlaylistVideoCall(Integer playlistId, Integer playlistElementId, PutVideoPlaylistVideoRequest putVideoPlaylistVideoRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = putVideoPlaylistVideoRequest;

        // create path and map variables
        String localVarPath = "/api/v1/video-playlists/{playlistId}/videos/{playlistElementId}"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()))
            .replace("{" + "playlistElementId" + "}", localVarApiClient.escapeString(playlistElementId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putVideoPlaylistVideoValidateBeforeCall(Integer playlistId, Integer playlistElementId, PutVideoPlaylistVideoRequest putVideoPlaylistVideoRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling putVideoPlaylistVideo(Async)");
        }

        // verify the required parameter 'playlistElementId' is set
        if (playlistElementId == null) {
            throw new ApiException("Missing the required parameter 'playlistElementId' when calling putVideoPlaylistVideo(Async)");
        }

        return putVideoPlaylistVideoCall(playlistId, playlistElementId, putVideoPlaylistVideoRequest, _callback);

    }

    /**
     * Update a playlist element
     * 
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @param putVideoPlaylistVideoRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void putVideoPlaylistVideo(Integer playlistId, Integer playlistElementId, PutVideoPlaylistVideoRequest putVideoPlaylistVideoRequest) throws ApiException {
        putVideoPlaylistVideoWithHttpInfo(playlistId, playlistElementId, putVideoPlaylistVideoRequest);
    }

    /**
     * Update a playlist element
     * 
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @param putVideoPlaylistVideoRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putVideoPlaylistVideoWithHttpInfo(Integer playlistId, Integer playlistElementId, PutVideoPlaylistVideoRequest putVideoPlaylistVideoRequest) throws ApiException {
        okhttp3.Call localVarCall = putVideoPlaylistVideoValidateBeforeCall(playlistId, playlistElementId, putVideoPlaylistVideoRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a playlist element (asynchronously)
     * 
     * @param playlistId Playlist id (required)
     * @param playlistElementId Playlist element id (required)
     * @param putVideoPlaylistVideoRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putVideoPlaylistVideoAsync(Integer playlistId, Integer playlistElementId, PutVideoPlaylistVideoRequest putVideoPlaylistVideoRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putVideoPlaylistVideoValidateBeforeCall(playlistId, playlistElementId, putVideoPlaylistVideoRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for reorderVideoPlaylist
     * @param playlistId Playlist id (required)
     * @param reorderVideoPlaylistRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reorderVideoPlaylistCall(Integer playlistId, ReorderVideoPlaylistRequest reorderVideoPlaylistRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = reorderVideoPlaylistRequest;

        // create path and map variables
        String localVarPath = "/api/v1/video-playlists/{playlistId}/videos/reorder"
            .replace("{" + "playlistId" + "}", localVarApiClient.escapeString(playlistId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call reorderVideoPlaylistValidateBeforeCall(Integer playlistId, ReorderVideoPlaylistRequest reorderVideoPlaylistRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'playlistId' is set
        if (playlistId == null) {
            throw new ApiException("Missing the required parameter 'playlistId' when calling reorderVideoPlaylist(Async)");
        }

        return reorderVideoPlaylistCall(playlistId, reorderVideoPlaylistRequest, _callback);

    }

    /**
     * Reorder a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param reorderVideoPlaylistRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void reorderVideoPlaylist(Integer playlistId, ReorderVideoPlaylistRequest reorderVideoPlaylistRequest) throws ApiException {
        reorderVideoPlaylistWithHttpInfo(playlistId, reorderVideoPlaylistRequest);
    }

    /**
     * Reorder a playlist
     * 
     * @param playlistId Playlist id (required)
     * @param reorderVideoPlaylistRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> reorderVideoPlaylistWithHttpInfo(Integer playlistId, ReorderVideoPlaylistRequest reorderVideoPlaylistRequest) throws ApiException {
        okhttp3.Call localVarCall = reorderVideoPlaylistValidateBeforeCall(playlistId, reorderVideoPlaylistRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Reorder a playlist (asynchronously)
     * 
     * @param playlistId Playlist id (required)
     * @param reorderVideoPlaylistRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reorderVideoPlaylistAsync(Integer playlistId, ReorderVideoPlaylistRequest reorderVideoPlaylistRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = reorderVideoPlaylistValidateBeforeCall(playlistId, reorderVideoPlaylistRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
