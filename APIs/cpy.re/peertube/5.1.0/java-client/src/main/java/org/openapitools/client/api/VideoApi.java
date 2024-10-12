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


import java.math.BigDecimal;
import java.io.File;
import org.openapitools.client.model.GetAccountVideosCategoryOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLanguageOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLicenceOneOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsAllOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsOneOfParameter;
import org.openapitools.client.model.GetLiveIdIdParameter;
import org.openapitools.client.model.LiveVideoLatencyMode;
import org.openapitools.client.model.LiveVideoReplaySettings;
import org.openapitools.client.model.LiveVideoResponse;
import org.openapitools.client.model.LiveVideoUpdate;
import java.time.OffsetDateTime;
import org.openapitools.client.model.UserViewingVideo;
import org.openapitools.client.model.VideoDetails;
import org.openapitools.client.model.VideoListResponse;
import org.openapitools.client.model.VideoPrivacySet;
import org.openapitools.client.model.VideoScheduledUpdate;
import org.openapitools.client.model.VideoSource;
import org.openapitools.client.model.VideoTokenResponse;
import org.openapitools.client.model.VideoUploadRequestResumable;
import org.openapitools.client.model.VideoUploadResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VideoApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VideoApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VideoApi(ApiClient apiClient) {
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
     * Build call for addLive_0
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
    public okhttp3.Call addLive_0Call(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call addLive_0ValidateBeforeCall(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'channelId' is set
        if (channelId == null) {
            throw new ApiException("Missing the required parameter 'channelId' when calling addLive_0(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling addLive_0(Async)");
        }

        return addLive_0Call(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile, _callback);

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
    public VideoUploadResponse addLive_0(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile) throws ApiException {
        ApiResponse<VideoUploadResponse> localVarResp = addLive_0WithHttpInfo(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile);
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
    public ApiResponse<VideoUploadResponse> addLive_0WithHttpInfo(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile) throws ApiException {
        okhttp3.Call localVarCall = addLive_0ValidateBeforeCall(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile, null);
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
    public okhttp3.Call addLive_0Async(Integer channelId, String name, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, LiveVideoLatencyMode latencyMode, Integer licence, Boolean nsfw, Boolean permanentLive, File previewfile, VideoPrivacySet privacy, LiveVideoReplaySettings replaySettings, Boolean saveReplay, String support, List<String> tags, File thumbnailfile, final ApiCallback<VideoUploadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = addLive_0ValidateBeforeCall(channelId, name, category, commentsEnabled, description, downloadEnabled, language, latencyMode, licence, nsfw, permanentLive, previewfile, privacy, replaySettings, saveReplay, support, tags, thumbnailfile, _callback);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for addView
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addViewCall(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = userViewingVideo;

        // create path and map variables
        String localVarPath = "/api/v1/videos/{id}/views"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addViewValidateBeforeCall(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling addView(Async)");
        }

        // verify the required parameter 'userViewingVideo' is set
        if (userViewingVideo == null) {
            throw new ApiException("Missing the required parameter 'userViewingVideo' when calling addView(Async)");
        }

        return addViewCall(id, userViewingVideo, _callback);

    }

    /**
     * Notify user is watching a video
     * Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video&#39;s viewers counter. If the user is authenticated, PeerTube will also store the current player time.
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void addView(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo) throws ApiException {
        addViewWithHttpInfo(id, userViewingVideo);
    }

    /**
     * Notify user is watching a video
     * Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video&#39;s viewers counter. If the user is authenticated, PeerTube will also store the current player time.
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> addViewWithHttpInfo(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo) throws ApiException {
        okhttp3.Call localVarCall = addViewValidateBeforeCall(id, userViewingVideo, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Notify user is watching a video (asynchronously)
     * Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video&#39;s viewers counter. If the user is authenticated, PeerTube will also store the current player time.
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addViewAsync(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addViewValidateBeforeCall(id, userViewingVideo, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosIdStudioEditPost_0
     * @param id The object id, uuid or short uuid (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdStudioEditPost_0Call(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/studio/edit"
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
            "application/x-www-form-urlencoded"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1VideosIdStudioEditPost_0ValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdStudioEditPost_0(Async)");
        }

        return apiV1VideosIdStudioEditPost_0Call(id, _callback);

    }

    /**
     * Create a studio task
     * Create a task to edit a video  (cut, add intro/outro etc)
     * @param id The object id, uuid or short uuid (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1VideosIdStudioEditPost_0(GetLiveIdIdParameter id) throws ApiException {
        apiV1VideosIdStudioEditPost_0WithHttpInfo(id);
    }

    /**
     * Create a studio task
     * Create a task to edit a video  (cut, add intro/outro etc)
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1VideosIdStudioEditPost_0WithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdStudioEditPost_0ValidateBeforeCall(id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a studio task (asynchronously)
     * Create a task to edit a video  (cut, add intro/outro etc)
     * @param id The object id, uuid or short uuid (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdStudioEditPost_0Async(GetLiveIdIdParameter id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdStudioEditPost_0ValidateBeforeCall(id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosIdWatchingPut
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     * @deprecated
     */
    @Deprecated
    public okhttp3.Call apiV1VideosIdWatchingPutCall(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = userViewingVideo;

        // create path and map variables
        String localVarPath = "/api/v1/videos/{id}/watching"
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

    @Deprecated
    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1VideosIdWatchingPutValidateBeforeCall(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdWatchingPut(Async)");
        }

        // verify the required parameter 'userViewingVideo' is set
        if (userViewingVideo == null) {
            throw new ApiException("Missing the required parameter 'userViewingVideo' when calling apiV1VideosIdWatchingPut(Async)");
        }

        return apiV1VideosIdWatchingPutCall(id, userViewingVideo, _callback);

    }

    /**
     * Set watching progress of a video
     * This endpoint has been deprecated. Use &#x60;/videos/{id}/views&#x60; instead
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     * @deprecated
     */
    @Deprecated
    public void apiV1VideosIdWatchingPut(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo) throws ApiException {
        apiV1VideosIdWatchingPutWithHttpInfo(id, userViewingVideo);
    }

    /**
     * Set watching progress of a video
     * This endpoint has been deprecated. Use &#x60;/videos/{id}/views&#x60; instead
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     * @deprecated
     */
    @Deprecated
    public ApiResponse<Void> apiV1VideosIdWatchingPutWithHttpInfo(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdWatchingPutValidateBeforeCall(id, userViewingVideo, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Set watching progress of a video (asynchronously)
     * This endpoint has been deprecated. Use &#x60;/videos/{id}/views&#x60; instead
     * @param id The object id, uuid or short uuid (required)
     * @param userViewingVideo  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     * @deprecated
     */
    @Deprecated
    public okhttp3.Call apiV1VideosIdWatchingPutAsync(GetLiveIdIdParameter id, UserViewingVideo userViewingVideo, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdWatchingPutValidateBeforeCall(id, userViewingVideo, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for delVideo
     * @param id The object id, uuid or short uuid (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delVideoCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}"
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call delVideoValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling delVideo(Async)");
        }

        return delVideoCall(id, _callback);

    }

    /**
     * Delete a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void delVideo(GetLiveIdIdParameter id) throws ApiException {
        delVideoWithHttpInfo(id);
    }

    /**
     * Delete a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> delVideoWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = delVideoValidateBeforeCall(id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a video (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delVideoAsync(GetLiveIdIdParameter id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = delVideoValidateBeforeCall(id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAccountVideos_0
     * @param name The username or handle of the account (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAccountVideos_0Call(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts/{name}/videos"
            .replace("{" + "name" + "}", localVarApiClient.escapeString(name.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (categoryOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("categoryOneOf", categoryOneOf));
        }

        if (isLive != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("isLive", isLive));
        }

        if (tagsOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("tagsOneOf", tagsOneOf));
        }

        if (tagsAllOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("tagsAllOf", tagsAllOf));
        }

        if (licenceOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("licenceOneOf", licenceOneOf));
        }

        if (languageOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("languageOneOf", languageOneOf));
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

        if (skipCount != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("skipCount", skipCount));
        }

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (excludeAlreadyWatched != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("excludeAlreadyWatched", excludeAlreadyWatched));
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
    private okhttp3.Call getAccountVideos_0ValidateBeforeCall(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling getAccountVideos_0(Async)");
        }

        return getAccountVideos_0Call(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);

    }

    /**
     * List videos of an account
     * 
     * @param name The username or handle of the account (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @return VideoListResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoListResponse getAccountVideos_0(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        ApiResponse<VideoListResponse> localVarResp = getAccountVideos_0WithHttpInfo(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        return localVarResp.getData();
    }

    /**
     * List videos of an account
     * 
     * @param name The username or handle of the account (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @return ApiResponse&lt;VideoListResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoListResponse> getAccountVideos_0WithHttpInfo(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        okhttp3.Call localVarCall = getAccountVideos_0ValidateBeforeCall(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, null);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videos of an account (asynchronously)
     * 
     * @param name The username or handle of the account (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAccountVideos_0Async(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback<VideoListResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAccountVideos_0ValidateBeforeCall(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCategories
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCategoriesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/categories";

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
    private okhttp3.Call getCategoriesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getCategoriesCall(_callback);

    }

    /**
     * List available video categories
     * 
     * @return List&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<String> getCategories() throws ApiException {
        ApiResponse<List<String>> localVarResp = getCategoriesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List available video categories
     * 
     * @return ApiResponse&lt;List&lt;String&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<String>> getCategoriesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getCategoriesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List available video categories (asynchronously)
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
    public okhttp3.Call getCategoriesAsync(final ApiCallback<List<String>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCategoriesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLanguages
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLanguagesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/languages";

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
    private okhttp3.Call getLanguagesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getLanguagesCall(_callback);

    }

    /**
     * List available video languages
     * 
     * @return List&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<String> getLanguages() throws ApiException {
        ApiResponse<List<String>> localVarResp = getLanguagesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List available video languages
     * 
     * @return ApiResponse&lt;List&lt;String&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<String>> getLanguagesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getLanguagesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List available video languages (asynchronously)
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
    public okhttp3.Call getLanguagesAsync(final ApiCallback<List<String>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLanguagesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLicences
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLicencesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/licences";

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
    private okhttp3.Call getLicencesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getLicencesCall(_callback);

    }

    /**
     * List available video licences
     * 
     * @return List&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<String> getLicences() throws ApiException {
        ApiResponse<List<String>> localVarResp = getLicencesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List available video licences
     * 
     * @return ApiResponse&lt;List&lt;String&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<String>> getLicencesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getLicencesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List available video licences (asynchronously)
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
    public okhttp3.Call getLicencesAsync(final ApiCallback<List<String>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLicencesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLiveId_0
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
    public okhttp3.Call getLiveId_0Call(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call getLiveId_0ValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getLiveId_0(Async)");
        }

        return getLiveId_0Call(id, _callback);

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
    public LiveVideoResponse getLiveId_0(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<LiveVideoResponse> localVarResp = getLiveId_0WithHttpInfo(id);
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
    public ApiResponse<LiveVideoResponse> getLiveId_0WithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = getLiveId_0ValidateBeforeCall(id, null);
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
    public okhttp3.Call getLiveId_0Async(GetLiveIdIdParameter id, final ApiCallback<LiveVideoResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLiveId_0ValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<LiveVideoResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideo
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
    public okhttp3.Call getVideoCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideoValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getVideo(Async)");
        }

        return getVideoCall(id, _callback);

    }

    /**
     * Get a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return VideoDetails
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoDetails getVideo(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<VideoDetails> localVarResp = getVideoWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;VideoDetails&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoDetails> getVideoWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = getVideoValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<VideoDetails>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a video (asynchronously)
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
    public okhttp3.Call getVideoAsync(GetLiveIdIdParameter id, final ApiCallback<VideoDetails> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideoValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<VideoDetails>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideoChannelVideos
     * @param channelHandle The video channel handle (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideoChannelVideosCall(String channelHandle, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/video-channels/{channelHandle}/videos"
            .replace("{" + "channelHandle" + "}", localVarApiClient.escapeString(channelHandle.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (categoryOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("categoryOneOf", categoryOneOf));
        }

        if (isLive != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("isLive", isLive));
        }

        if (tagsOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("tagsOneOf", tagsOneOf));
        }

        if (tagsAllOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("tagsAllOf", tagsAllOf));
        }

        if (licenceOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("licenceOneOf", licenceOneOf));
        }

        if (languageOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("languageOneOf", languageOneOf));
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

        if (skipCount != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("skipCount", skipCount));
        }

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (excludeAlreadyWatched != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("excludeAlreadyWatched", excludeAlreadyWatched));
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
    private okhttp3.Call getVideoChannelVideosValidateBeforeCall(String channelHandle, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'channelHandle' is set
        if (channelHandle == null) {
            throw new ApiException("Missing the required parameter 'channelHandle' when calling getVideoChannelVideos(Async)");
        }

        return getVideoChannelVideosCall(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);

    }

    /**
     * List videos of a video channel
     * 
     * @param channelHandle The video channel handle (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @return VideoListResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoListResponse getVideoChannelVideos(String channelHandle, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        ApiResponse<VideoListResponse> localVarResp = getVideoChannelVideosWithHttpInfo(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        return localVarResp.getData();
    }

    /**
     * List videos of a video channel
     * 
     * @param channelHandle The video channel handle (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @return ApiResponse&lt;VideoListResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoListResponse> getVideoChannelVideosWithHttpInfo(String channelHandle, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        okhttp3.Call localVarCall = getVideoChannelVideosValidateBeforeCall(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, null);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videos of a video channel (asynchronously)
     * 
     * @param channelHandle The video channel handle (required)
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideoChannelVideosAsync(String channelHandle, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback<VideoListResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideoChannelVideosValidateBeforeCall(channelHandle, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideoDesc
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
    public okhttp3.Call getVideoDescCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/description"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideoDescValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getVideoDesc(Async)");
        }

        return getVideoDescCall(id, _callback);

    }

    /**
     * Get complete video description
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public String getVideoDesc(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<String> localVarResp = getVideoDescWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get complete video description
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> getVideoDescWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = getVideoDescValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get complete video description (asynchronously)
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
    public okhttp3.Call getVideoDescAsync(GetLiveIdIdParameter id, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideoDescValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideoPrivacyPolicies
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideoPrivacyPoliciesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/privacies";

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
    private okhttp3.Call getVideoPrivacyPoliciesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getVideoPrivacyPoliciesCall(_callback);

    }

    /**
     * List available video privacy policies
     * 
     * @return List&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<String> getVideoPrivacyPolicies() throws ApiException {
        ApiResponse<List<String>> localVarResp = getVideoPrivacyPoliciesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List available video privacy policies
     * 
     * @return ApiResponse&lt;List&lt;String&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<String>> getVideoPrivacyPoliciesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVideoPrivacyPoliciesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List available video privacy policies (asynchronously)
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
    public okhttp3.Call getVideoPrivacyPoliciesAsync(final ApiCallback<List<String>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideoPrivacyPoliciesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideoSource
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
    public okhttp3.Call getVideoSourceCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/source"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVideoSourceValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getVideoSource(Async)");
        }

        return getVideoSourceCall(id, _callback);

    }

    /**
     * Get video source file metadata
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return VideoSource
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoSource getVideoSource(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<VideoSource> localVarResp = getVideoSourceWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get video source file metadata
     * 
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;VideoSource&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoSource> getVideoSourceWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = getVideoSourceValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<VideoSource>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get video source file metadata (asynchronously)
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
    public okhttp3.Call getVideoSourceAsync(GetLiveIdIdParameter id, final ApiCallback<VideoSource> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideoSourceValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<VideoSource>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVideos
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideosCall(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (categoryOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("categoryOneOf", categoryOneOf));
        }

        if (isLive != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("isLive", isLive));
        }

        if (tagsOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("tagsOneOf", tagsOneOf));
        }

        if (tagsAllOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("tagsAllOf", tagsAllOf));
        }

        if (licenceOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("licenceOneOf", licenceOneOf));
        }

        if (languageOneOf != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("languageOneOf", languageOneOf));
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

        if (skipCount != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("skipCount", skipCount));
        }

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (excludeAlreadyWatched != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("excludeAlreadyWatched", excludeAlreadyWatched));
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
    private okhttp3.Call getVideosValidateBeforeCall(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
        return getVideosCall(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);

    }

    /**
     * List videos
     * 
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @return VideoListResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoListResponse getVideos(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        ApiResponse<VideoListResponse> localVarResp = getVideosWithHttpInfo(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        return localVarResp.getData();
    }

    /**
     * List videos
     * 
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @return ApiResponse&lt;VideoListResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoListResponse> getVideosWithHttpInfo(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        okhttp3.Call localVarCall = getVideosValidateBeforeCall(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, null);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videos (asynchronously)
     * 
     * @param categoryOneOf category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param isLive whether or not the video is a live (optional)
     * @param tagsOneOf tag(s) of the video (optional)
     * @param tagsAllOf tag(s) of the video, where all should be present in the video (optional)
     * @param licenceOneOf licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param languageOneOf language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language (optional)
     * @param nsfw whether to include nsfw videos, if any (optional)
     * @param isLocal **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos (optional)
     * @param include **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  (optional)
     * @param privacyOneOf **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies (optional)
     * @param hasHLSFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files (optional)
     * @param hasWebtorrentFiles **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files (optional)
     * @param skipCount if you don&#39;t need the &#x60;total&#x60; in the response (optional, default to false)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort  (optional)
     * @param excludeAlreadyWatched Whether or not to exclude videos that are in the user&#39;s video history (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVideosAsync(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback<VideoListResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVideosValidateBeforeCall(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putVideo
     * @param id The object id, uuid or short uuid (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param name Video name (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putVideoCall(GetLiveIdIdParameter id, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, String name, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, List<String> tags, File thumbnailfile, String waitTranscoding, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (category != null) {
            localVarFormParams.put("category", category);
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

        if (licence != null) {
            localVarFormParams.put("licence", licence);
        }

        if (name != null) {
            localVarFormParams.put("name", name);
        }

        if (nsfw != null) {
            localVarFormParams.put("nsfw", nsfw);
        }

        if (originallyPublishedAt != null) {
            localVarFormParams.put("originallyPublishedAt", originallyPublishedAt);
        }

        if (previewfile != null) {
            localVarFormParams.put("previewfile", previewfile);
        }

        if (privacy != null) {
            localVarFormParams.put("privacy", privacy);
        }

        if (scheduleUpdate != null) {
            localVarFormParams.put("scheduleUpdate", scheduleUpdate);
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

        if (waitTranscoding != null) {
            localVarFormParams.put("waitTranscoding", waitTranscoding);
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
    private okhttp3.Call putVideoValidateBeforeCall(GetLiveIdIdParameter id, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, String name, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, List<String> tags, File thumbnailfile, String waitTranscoding, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putVideo(Async)");
        }

        return putVideoCall(id, category, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);

    }

    /**
     * Update a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param name Video name (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void putVideo(GetLiveIdIdParameter id, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, String name, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, List<String> tags, File thumbnailfile, String waitTranscoding) throws ApiException {
        putVideoWithHttpInfo(id, category, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
    }

    /**
     * Update a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param name Video name (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putVideoWithHttpInfo(GetLiveIdIdParameter id, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, String name, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, List<String> tags, File thumbnailfile, String waitTranscoding) throws ApiException {
        okhttp3.Call localVarCall = putVideoValidateBeforeCall(id, category, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a video (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param name Video name (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putVideoAsync(GetLiveIdIdParameter id, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, String name, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, List<String> tags, File thumbnailfile, String waitTranscoding, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putVideoValidateBeforeCall(id, category, commentsEnabled, description, downloadEnabled, language, licence, name, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for requestVideoToken
     * @param id The object id, uuid or short uuid (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call requestVideoTokenCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/token"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call requestVideoTokenValidateBeforeCall(GetLiveIdIdParameter id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling requestVideoToken(Async)");
        }

        return requestVideoTokenCall(id, _callback);

    }

    /**
     * Request video token
     * Request special tokens that expire quickly to use them in some context (like accessing private static files)
     * @param id The object id, uuid or short uuid (required)
     * @return VideoTokenResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public VideoTokenResponse requestVideoToken(GetLiveIdIdParameter id) throws ApiException {
        ApiResponse<VideoTokenResponse> localVarResp = requestVideoTokenWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Request video token
     * Request special tokens that expire quickly to use them in some context (like accessing private static files)
     * @param id The object id, uuid or short uuid (required)
     * @return ApiResponse&lt;VideoTokenResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoTokenResponse> requestVideoTokenWithHttpInfo(GetLiveIdIdParameter id) throws ApiException {
        okhttp3.Call localVarCall = requestVideoTokenValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<VideoTokenResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Request video token (asynchronously)
     * Request special tokens that expire quickly to use them in some context (like accessing private static files)
     * @param id The object id, uuid or short uuid (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect parameters </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call requestVideoTokenAsync(GetLiveIdIdParameter id, final ApiCallback<VideoTokenResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = requestVideoTokenValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<VideoTokenResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateLiveId_0
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
    public okhttp3.Call updateLiveId_0Call(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call updateLiveId_0ValidateBeforeCall(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling updateLiveId_0(Async)");
        }

        return updateLiveId_0Call(id, liveVideoUpdate, _callback);

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
    public void updateLiveId_0(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate) throws ApiException {
        updateLiveId_0WithHttpInfo(id, liveVideoUpdate);
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
    public ApiResponse<Void> updateLiveId_0WithHttpInfo(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate) throws ApiException {
        okhttp3.Call localVarCall = updateLiveId_0ValidateBeforeCall(id, liveVideoUpdate, null);
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
    public okhttp3.Call updateLiveId_0Async(GetLiveIdIdParameter id, LiveVideoUpdate liveVideoUpdate, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateLiveId_0ValidateBeforeCall(id, liveVideoUpdate, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadLegacy
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param videofile Video file (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 408 </td><td> upload has timed out </td><td>  -  </td></tr>
        <tr><td> 413 </td><td> If the response has no body, it means the reverse-proxy didn&#39;t let it through. Otherwise disambiguate via &#x60;type&#x60;: - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  * X-File-Maximum-Size - Maximum file size for the video <br>  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uploadLegacyCall(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/upload";

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

        if (licence != null) {
            localVarFormParams.put("licence", licence);
        }

        if (name != null) {
            localVarFormParams.put("name", name);
        }

        if (nsfw != null) {
            localVarFormParams.put("nsfw", nsfw);
        }

        if (originallyPublishedAt != null) {
            localVarFormParams.put("originallyPublishedAt", originallyPublishedAt);
        }

        if (previewfile != null) {
            localVarFormParams.put("previewfile", previewfile);
        }

        if (privacy != null) {
            localVarFormParams.put("privacy", privacy);
        }

        if (scheduleUpdate != null) {
            localVarFormParams.put("scheduleUpdate", scheduleUpdate);
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

        if (waitTranscoding != null) {
            localVarFormParams.put("waitTranscoding", waitTranscoding);
        }

        if (videofile != null) {
            localVarFormParams.put("videofile", videofile);
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
    private okhttp3.Call uploadLegacyValidateBeforeCall(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'channelId' is set
        if (channelId == null) {
            throw new ApiException("Missing the required parameter 'channelId' when calling uploadLegacy(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling uploadLegacy(Async)");
        }

        // verify the required parameter 'videofile' is set
        if (videofile == null) {
            throw new ApiException("Missing the required parameter 'videofile' when calling uploadLegacy(Async)");
        }

        return uploadLegacyCall(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);

    }

    /**
     * Upload a video
     * Uses a single request to upload a video.
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param videofile Video file (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @return VideoUploadResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 408 </td><td> upload has timed out </td><td>  -  </td></tr>
        <tr><td> 413 </td><td> If the response has no body, it means the reverse-proxy didn&#39;t let it through. Otherwise disambiguate via &#x60;type&#x60;: - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  * X-File-Maximum-Size - Maximum file size for the video <br>  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
     </table>
     */
    public VideoUploadResponse uploadLegacy(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding) throws ApiException {
        ApiResponse<VideoUploadResponse> localVarResp = uploadLegacyWithHttpInfo(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
        return localVarResp.getData();
    }

    /**
     * Upload a video
     * Uses a single request to upload a video.
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param videofile Video file (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @return ApiResponse&lt;VideoUploadResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 408 </td><td> upload has timed out </td><td>  -  </td></tr>
        <tr><td> 413 </td><td> If the response has no body, it means the reverse-proxy didn&#39;t let it through. Otherwise disambiguate via &#x60;type&#x60;: - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  * X-File-Maximum-Size - Maximum file size for the video <br>  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoUploadResponse> uploadLegacyWithHttpInfo(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding) throws ApiException {
        okhttp3.Call localVarCall = uploadLegacyValidateBeforeCall(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, null);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Upload a video (asynchronously)
     * Uses a single request to upload a video.
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param videofile Video file (required)
     * @param category category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
     * @param commentsEnabled Enable or disable comments for this video (optional)
     * @param description Video description (optional)
     * @param downloadEnabled Enable or disable downloading for this video (optional)
     * @param language language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
     * @param licence licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
     * @param nsfw Whether or not this video contains sensitive content (optional)
     * @param originallyPublishedAt Date when the content was originally published (optional)
     * @param previewfile Video preview file (optional)
     * @param privacy  (optional)
     * @param scheduleUpdate  (optional)
     * @param support A text tell the audience how to support the video creator (optional)
     * @param tags Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
     * @param thumbnailfile Video thumbnail file (optional)
     * @param waitTranscoding Whether or not we wait transcoding before publish the video (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 408 </td><td> upload has timed out </td><td>  -  </td></tr>
        <tr><td> 413 </td><td> If the response has no body, it means the reverse-proxy didn&#39;t let it through. Otherwise disambiguate via &#x60;type&#x60;: - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  * X-File-Maximum-Size - Maximum file size for the video <br>  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uploadLegacyAsync(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback<VideoUploadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadLegacyValidateBeforeCall(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadResumable
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  (required)
     * @param contentRange Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  (required)
     * @param contentLength Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  (required)
     * @param body  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> last chunk received </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 308 </td><td> resume incomplete </td><td>  * Content-Length -  <br>  * Range -  <br>  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> chunk doesn&#39;t match range </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many concurrent requests </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> upload is already being processed </td><td>  * Retry-After -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call uploadResumableCall(String uploadId, String contentRange, BigDecimal contentLength, File body, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/api/v1/videos/upload-resumable";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (uploadId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("upload_id", uploadId));
        }

        if (contentRange != null) {
            localVarHeaderParams.put("Content-Range", localVarApiClient.parameterToString(contentRange));
        }

        if (contentLength != null) {
            localVarHeaderParams.put("Content-Length", localVarApiClient.parameterToString(contentLength));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/octet-stream"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call uploadResumableValidateBeforeCall(String uploadId, String contentRange, BigDecimal contentLength, File body, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'uploadId' is set
        if (uploadId == null) {
            throw new ApiException("Missing the required parameter 'uploadId' when calling uploadResumable(Async)");
        }

        // verify the required parameter 'contentRange' is set
        if (contentRange == null) {
            throw new ApiException("Missing the required parameter 'contentRange' when calling uploadResumable(Async)");
        }

        // verify the required parameter 'contentLength' is set
        if (contentLength == null) {
            throw new ApiException("Missing the required parameter 'contentLength' when calling uploadResumable(Async)");
        }

        return uploadResumableCall(uploadId, contentRange, contentLength, body, _callback);

    }

    /**
     * Send chunk for the resumable upload of a video
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  (required)
     * @param contentRange Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  (required)
     * @param contentLength Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  (required)
     * @param body  (optional)
     * @return VideoUploadResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> last chunk received </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 308 </td><td> resume incomplete </td><td>  * Content-Length -  <br>  * Range -  <br>  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> chunk doesn&#39;t match range </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many concurrent requests </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> upload is already being processed </td><td>  * Retry-After -  <br>  </td></tr>
     </table>
     */
    public VideoUploadResponse uploadResumable(String uploadId, String contentRange, BigDecimal contentLength, File body) throws ApiException {
        ApiResponse<VideoUploadResponse> localVarResp = uploadResumableWithHttpInfo(uploadId, contentRange, contentLength, body);
        return localVarResp.getData();
    }

    /**
     * Send chunk for the resumable upload of a video
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  (required)
     * @param contentRange Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  (required)
     * @param contentLength Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  (required)
     * @param body  (optional)
     * @return ApiResponse&lt;VideoUploadResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> last chunk received </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 308 </td><td> resume incomplete </td><td>  * Content-Length -  <br>  * Range -  <br>  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> chunk doesn&#39;t match range </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many concurrent requests </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> upload is already being processed </td><td>  * Retry-After -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<VideoUploadResponse> uploadResumableWithHttpInfo(String uploadId, String contentRange, BigDecimal contentLength, File body) throws ApiException {
        okhttp3.Call localVarCall = uploadResumableValidateBeforeCall(uploadId, contentRange, contentLength, body, null);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Send chunk for the resumable upload of a video (asynchronously)
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  (required)
     * @param contentRange Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  (required)
     * @param contentLength Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  (required)
     * @param body  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> last chunk received </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 308 </td><td> resume incomplete </td><td>  * Content-Length -  <br>  * Range -  <br>  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass upload filter </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> chunk doesn&#39;t match range </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> video unreadable </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> too many concurrent requests </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> upload is already being processed </td><td>  * Retry-After -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call uploadResumableAsync(String uploadId, String contentRange, BigDecimal contentLength, File body, final ApiCallback<VideoUploadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadResumableValidateBeforeCall(uploadId, contentRange, contentLength, body, _callback);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadResumableCancel
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  (required)
     * @param contentLength  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> upload cancelled </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uploadResumableCancelCall(String uploadId, BigDecimal contentLength, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/upload-resumable";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (uploadId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("upload_id", uploadId));
        }

        if (contentLength != null) {
            localVarHeaderParams.put("Content-Length", localVarApiClient.parameterToString(contentLength));
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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call uploadResumableCancelValidateBeforeCall(String uploadId, BigDecimal contentLength, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'uploadId' is set
        if (uploadId == null) {
            throw new ApiException("Missing the required parameter 'uploadId' when calling uploadResumableCancel(Async)");
        }

        // verify the required parameter 'contentLength' is set
        if (contentLength == null) {
            throw new ApiException("Missing the required parameter 'contentLength' when calling uploadResumableCancel(Async)");
        }

        return uploadResumableCancelCall(uploadId, contentLength, _callback);

    }

    /**
     * Cancel the resumable upload of a video, deleting any data uploaded so far
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  (required)
     * @param contentLength  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> upload cancelled </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
     </table>
     */
    public void uploadResumableCancel(String uploadId, BigDecimal contentLength) throws ApiException {
        uploadResumableCancelWithHttpInfo(uploadId, contentLength);
    }

    /**
     * Cancel the resumable upload of a video, deleting any data uploaded so far
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  (required)
     * @param contentLength  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> upload cancelled </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> uploadResumableCancelWithHttpInfo(String uploadId, BigDecimal contentLength) throws ApiException {
        okhttp3.Call localVarCall = uploadResumableCancelValidateBeforeCall(uploadId, contentLength, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Cancel the resumable upload of a video, deleting any data uploaded so far (asynchronously)
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video
     * @param uploadId Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  (required)
     * @param contentLength  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> upload cancelled </td><td>  * Content-Length -  <br>  </td></tr>
        <tr><td> 404 </td><td> upload not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uploadResumableCancelAsync(String uploadId, BigDecimal contentLength, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadResumableCancelValidateBeforeCall(uploadId, contentLength, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadResumableInit
     * @param xUploadContentLength Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. (required)
     * @param xUploadContentType MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. (required)
     * @param videoUploadRequestResumable  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> file already exists, send a [&#x60;resume&#x60;](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) request instead </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> created </td><td>  * Content-Length -  <br>  * Location -  <br>  </td></tr>
        <tr><td> 413 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;max_file_size_reached&#x60; for the absolute file size limit - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  -  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uploadResumableInitCall(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = videoUploadRequestResumable;

        // create path and map variables
        String localVarPath = "/api/v1/videos/upload-resumable";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xUploadContentLength != null) {
            localVarHeaderParams.put("X-Upload-Content-Length", localVarApiClient.parameterToString(xUploadContentLength));
        }

        if (xUploadContentType != null) {
            localVarHeaderParams.put("X-Upload-Content-Type", localVarApiClient.parameterToString(xUploadContentType));
        }

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
    private okhttp3.Call uploadResumableInitValidateBeforeCall(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xUploadContentLength' is set
        if (xUploadContentLength == null) {
            throw new ApiException("Missing the required parameter 'xUploadContentLength' when calling uploadResumableInit(Async)");
        }

        // verify the required parameter 'xUploadContentType' is set
        if (xUploadContentType == null) {
            throw new ApiException("Missing the required parameter 'xUploadContentType' when calling uploadResumableInit(Async)");
        }

        return uploadResumableInitCall(xUploadContentLength, xUploadContentType, videoUploadRequestResumable, _callback);

    }

    /**
     * Initialize the resumable upload of a video
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video
     * @param xUploadContentLength Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. (required)
     * @param xUploadContentType MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. (required)
     * @param videoUploadRequestResumable  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> file already exists, send a [&#x60;resume&#x60;](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) request instead </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> created </td><td>  * Content-Length -  <br>  * Location -  <br>  </td></tr>
        <tr><td> 413 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;max_file_size_reached&#x60; for the absolute file size limit - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  -  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
     </table>
     */
    public void uploadResumableInit(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable) throws ApiException {
        uploadResumableInitWithHttpInfo(xUploadContentLength, xUploadContentType, videoUploadRequestResumable);
    }

    /**
     * Initialize the resumable upload of a video
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video
     * @param xUploadContentLength Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. (required)
     * @param xUploadContentType MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. (required)
     * @param videoUploadRequestResumable  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> file already exists, send a [&#x60;resume&#x60;](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) request instead </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> created </td><td>  * Content-Length -  <br>  * Location -  <br>  </td></tr>
        <tr><td> 413 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;max_file_size_reached&#x60; for the absolute file size limit - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  -  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> uploadResumableInitWithHttpInfo(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable) throws ApiException {
        okhttp3.Call localVarCall = uploadResumableInitValidateBeforeCall(xUploadContentLength, xUploadContentType, videoUploadRequestResumable, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Initialize the resumable upload of a video (asynchronously)
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video
     * @param xUploadContentLength Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. (required)
     * @param xUploadContentType MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. (required)
     * @param videoUploadRequestResumable  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> file already exists, send a [&#x60;resume&#x60;](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) request instead </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> created </td><td>  * Content-Length -  <br>  * Location -  <br>  </td></tr>
        <tr><td> 413 </td><td> Disambiguate via &#x60;type&#x60;: - &#x60;max_file_size_reached&#x60; for the absolute file size limit - &#x60;quota_reached&#x60; for quota limits whether daily or global  </td><td>  -  </td></tr>
        <tr><td> 415 </td><td> video type unsupported </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uploadResumableInitAsync(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadResumableInitValidateBeforeCall(xUploadContentLength, xUploadContentType, videoUploadRequestResumable, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
