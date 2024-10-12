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


import org.openapitools.client.model.ApiV1VideosLiveIdSessionsGet200Response;
import java.io.File;
import org.openapitools.client.model.GetLiveIdIdParameter;
import org.openapitools.client.model.LiveVideoLatencyMode;
import org.openapitools.client.model.LiveVideoReplaySettings;
import org.openapitools.client.model.LiveVideoResponse;
import org.openapitools.client.model.LiveVideoSessionResponse;
import org.openapitools.client.model.LiveVideoUpdate;
import org.openapitools.client.model.VideoPrivacySet;
import org.openapitools.client.model.VideoUploadResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LiveVideosApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LiveVideosApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LiveVideosApi(ApiClient apiClient) {
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
     * Build call for addLive
     * @param channelId Channel id that will contain this live video (required)
     * @param name Live video/replay name (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this live video/replay (optional)
     * @param description Live video/replay description (optional)
     * @param downloadEnabled Enable or disable downloading for the replay of this live video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param latencyMode  (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this live video/replay contains sensitive content (optional)
     * @param permanentLive User can stream multiple times in a permanent live (optional)
     * @param previewfile Live video/replay preview file (optional)
     * @param privacy  (optional)
     * @param replaySettings  (optional)
     * @param saveReplay  (optional)
     * @param support A text tell the audience how to support the creator (optional)
     * @param tags Live video/replay tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Live video/replay thumbnail file (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Disambiguate via &#x60;type&#x60;: - default type for a validation error - &#x60;live_conflicting_permanent_and_save_replay&#x60; for conflicting parameters set  </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;live_not_enabled&#x60; for a disabled live feature - &#x60;live_not_allowing_replay&#x60; for a disabled replay feature - &#x60;max_instance_lives_limit_reached&#x60; for the absolute concurrent live limit - &#x60;max_user_lives_limit_reached&#x60; for the user concurrent live limit  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLiveCall(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/live";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (category != null) {
            localVarFormParams.put("category", category);
        }

        if (channelId != null) {
            localVarFormParams.put("channelId", channelId);
        }

        if (commentsEnabled != null) {
            localVarFormParams.put("commentsEnabled", commentsEnabled);
        }

        if (description != null) {
            localVarFormParams.put("description", description);
        }

        if (downloadEnabled != null) {
            localVarFormParams.put("downloadEnabled", downloadEnabled);
        }

        if (language != null) {
            localVarFormParams.put("language", language);
        }

        if (latencyMode != null) {
            localVarFormParams.put("latencyMode", latencyMode);
        }

        if (licence != null) {
            localVarFormParams.put("licence", licence);
        }

        if (name != null) {
            localVarFormParams.put("name", name);
        }

        if (nsfw != null) {
            localVarFormParams.put("nsfw", nsfw);
        }

        if (permanentLive != null) {
            localVarFormParams.put("permanentLive", permanentLive);
        }

        if (previewfile != null) {
            localVarFormParams.put("previewfile", previewfile);
        }

        if (privacy != null) {
            localVarFormParams.put("privacy", privacy);
        }

        if (replaySettings != null) {
            localVarFormParams.put("replaySettings", replaySettings);
        }

        if (saveReplay != null) {
            localVarFormParams.put("saveReplay", saveReplay);
        }

        if (support != null) {
            localVarFormParams.put("support", support);
        }

        if (tags != null) {
            localVarFormParams.put("tags", tags);
        }

        if (thumbnailfile != null) {
            localVarFormParams.put("thumbnailfile", thumbnailfile);
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
    private okhttp3.Call addLiveValidateBeforeCall(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'channelId' is set
        if (channelId == null) {
            throw new ApiException("Missing the required parameter 'channelId' when calling addLive(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling addLive(Async)");
        }

        return addLiveCall(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile, _callback);

    }

    /**
     * Create a live
     * 
     * @param channelId Channel id that will contain this live video (required)
     * @param name Live video/replay name (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this live video/replay (optional)
     * @param description Live video/replay description (optional)
     * @param downloadEnabled Enable or disable downloading for the replay of this live video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param latencyMode  (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this live video/replay contains sensitive content (optional)
     * @param permanentLive User can stream multiple times in a permanent live (optional)
     * @param previewfile Live video/replay preview file (optional)
     * @param privacy  (optional)
     * @param replaySettings  (optional)
     * @param saveReplay  (optional)
     * @param support A text tell the audience how to support the creator (optional)
     * @param tags Live video/replay tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Live video/replay thumbnail file (optional)
     * @return VideoUploadResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Disambiguate via &#x60;type&#x60;: - default type for a validation error - &#x60;live_conflicting_permanent_and_save_replay&#x60; for conflicting parameters set  </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;live_not_enabled&#x60; for a disabled live feature - &#x60;live_not_allowing_replay&#x60; for a disabled replay feature - &#x60;max_instance_lives_limit_reached&#x60; for the absolute concurrent live limit - &#x60;max_user_lives_limit_reached&#x60; for the user concurrent live limit  </td><td>  -  </td></tr>
     </table>
     */
    public VideoUploadResponse addLive(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile) throws ApiException {
        ApiResponse<VideoUploadResponse> localVarResp = addLiveWithHttpInfo(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile);
        return localVarResp.getData();
    }

    /**
     * Create a live
     * 
     * @param channelId Channel id that will contain this live video (required)
     * @param name Live video/replay name (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this live video/replay (optional)
     * @param description Live video/replay description (optional)
     * @param downloadEnabled Enable or disable downloading for the replay of this live video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param latencyMode  (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this live video/replay contains sensitive content (optional)
     * @param permanentLive User can stream multiple times in a permanent live (optional)
     * @param previewfile Live video/replay preview file (optional)
     * @param privacy  (optional)
     * @param replaySettings  (optional)
     * @param saveReplay  (optional)
     * @param support A text tell the audience how to support the creator (optional)
     * @param tags Live video/replay tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Live video/replay thumbnail file (optional)
     * @return ApiResponse&lt;VideoUploadResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Disambiguate via &#x60;type&#x60;: - default type for a validation error - &#x60;live_conflicting_permanent_and_save_replay&#x60; for conflicting parameters set  </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;live_not_enabled&#x60; for a disabled live feature - &#x60;live_not_allowing_replay&#x60; for a disabled replay feature - &#x60;max_instance_lives_limit_reached&#x60; for the absolute concurrent live limit - &#x60;max_user_lives_limit_reached&#x60; for the user concurrent live limit  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoUploadResponse> addLiveWithHttpInfo(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile) throws ApiException {
        okhttp3.Call localVarCall = addLiveValidateBeforeCall(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile, null);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a live (asynchronously)
     * 
     * @param channelId Channel id that will contain this live video (required)
     * @param name Live video/replay name (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this live video/replay (optional)
     * @param description Live video/replay description (optional)
     * @param downloadEnabled Enable or disable downloading for the replay of this live video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param latencyMode  (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this live video/replay contains sensitive content (optional)
     * @param permanentLive User can stream multiple times in a permanent live (optional)
     * @param previewfile Live video/replay preview file (optional)
     * @param privacy  (optional)
     * @param replaySettings  (optional)
     * @param saveReplay  (optional)
     * @param support A text tell the audience how to support the creator (optional)
     * @param tags Live video/replay tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Live video/replay thumbnail file (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Disambiguate via &#x60;type&#x60;: - default type for a validation error - &#x60;live_conflicting_permanent_and_save_replay&#x60; for conflicting parameters set  </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;live_not_enabled&#x60; for a disabled live feature - &#x60;live_not_allowing_replay&#x60; for a disabled replay feature - &#x60;max_instance_lives_limit_reached&#x60; for the absolute concurrent live limit - &#x60;max_user_lives_limit_reached&#x60; for the user concurrent live limit  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLiveAsync(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile, final ApiCallback<VideoUploadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = addLiveValidateBeforeCall(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile, _callback);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosIdLiveSessionGet
     * @param id The object id, uuid or short uuid (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdLiveSessionGetCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/live-session"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1VideosIdLiveSessionGetValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdLiveSessionGet(Async)");
        }

        return apiV1VideosIdLiveSessionGetCall(id, _callback);

    }

    /**
     * Get live session of a replay
     * If the video is a replay of a live, you can find the associated live session using this endpoint
     * @param id The object id, uuid or short uuid (required)
     * @return LiveVideoSessionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public LiveVideoSessionResponse apiV1VideosIdLiveSessionGet(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<LiveVideoSessionResponse> localVarResp = apiV1VideosIdLiveSessionGetWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get live session of a replay
     * If the video is a replay of a live, you can find the associated live session using this endpoint
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;LiveVideoSessionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LiveVideoSessionResponse> apiV1VideosIdLiveSessionGetWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdLiveSessionGetValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<LiveVideoSessionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get live session of a replay (asynchronously)
     * If the video is a replay of a live, you can find the associated live session using this endpoint
     * @param id The object id, uuid or short uuid (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdLiveSessionGetAsync(GetLiveIdIdParameter id, final ApiCallback<LiveVideoSessionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdLiveSessionGetValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<LiveVideoSessionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosLiveIdSessionsGet
     * @param id The object id, uuid or short uuid (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosLiveIdSessionsGetCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/live/{id}/sessions"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1VideosLiveIdSessionsGetValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosLiveIdSessionsGet(Async)");
        }

        return apiV1VideosLiveIdSessionsGetCall(id, _callback);

    }

    /**
     * List live sessions
     * List all sessions created in a particular live
     * @param id The object id, uuid or short uuid (required)
     * @return ApiV1VideosLiveIdSessionsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiV1VideosLiveIdSessionsGet200Response apiV1VideosLiveIdSessionsGet(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<ApiV1VideosLiveIdSessionsGet200Response> localVarResp = apiV1VideosLiveIdSessionsGetWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * List live sessions
     * List all sessions created in a particular live
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;ApiV1VideosLiveIdSessionsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiV1VideosLiveIdSessionsGet200Response> apiV1VideosLiveIdSessionsGetWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosLiveIdSessionsGetValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<ApiV1VideosLiveIdSessionsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List live sessions (asynchronously)
     * List all sessions created in a particular live
     * @param id The object id, uuid or short uuid (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosLiveIdSessionsGetAsync(GetLiveIdIdParameter id, final ApiCallback<ApiV1VideosLiveIdSessionsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosLiveIdSessionsGetValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<ApiV1VideosLiveIdSessionsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLiveId
     * @param id The object id, uuid or short uuid (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLiveIdCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/live/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLiveIdValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getLiveId(Async)");
        }

        return getLiveIdCall(id, _callback);

    }

    /**
     * Get information about a live
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return LiveVideoResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public LiveVideoResponse getLiveId(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<LiveVideoResponse> localVarResp = getLiveIdWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get information about a live
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;LiveVideoResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LiveVideoResponse> getLiveIdWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = getLiveIdValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<LiveVideoResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get information about a live (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLiveIdAsync(GetLiveIdIdParameter id, final ApiCallback<LiveVideoResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLiveIdValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<LiveVideoResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateLiveId
     * @param id The object id, uuid or short uuid (required)
     * @param liveVideoUpdate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> bad parameters or trying to update a live that has already started </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> trying to save replay of the live but saving replay is not enabled on the instance </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLiveIdCall(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = liveVideoUpdate;

        // create path and map variables
        String localVarPath = "/api/v1/videos/live/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
    private okhttp3.Call updateLiveIdValidateBeforeCall(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling updateLiveId(Async)");
        }

        return updateLiveIdCall(id, liveVideoUpdate, _callback);

    }

    /**
     * Update information about a live
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param liveVideoUpdate  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> bad parameters or trying to update a live that has already started </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> trying to save replay of the live but saving replay is not enabled on the instance </td><td>  -  </td></tr>
     </table>
     */
    public void updateLiveId(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate) throws ApiException {
        updateLiveIdWithHttpInfo(id, liveVideoUpdate);
    }

    /**
     * Update information about a live
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param liveVideoUpdate  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> bad parameters or trying to update a live that has already started </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> trying to save replay of the live but saving replay is not enabled on the instance </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updateLiveIdWithHttpInfo(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate) throws ApiException {
        okhttp3.Call localVarCall = updateLiveIdValidateBeforeCall(id, liveVideoUpdate, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update information about a live (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param liveVideoUpdate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> bad parameters or trying to update a live that has already started </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> trying to save replay of the live but saving replay is not enabled on the instance </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLiveIdAsync(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateLiveIdValidateBeforeCall(id, liveVideoUpdate, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
