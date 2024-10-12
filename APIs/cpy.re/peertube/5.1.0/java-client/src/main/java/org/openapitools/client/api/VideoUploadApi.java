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
import java.time.OffsetDateTime;
import java.net.URI;
import org.openapitools.client.model.VideoPrivacySet;
import org.openapitools.client.model.VideoScheduledUpdate;
import org.openapitools.client.model.VideoUploadRequestResumable;
import org.openapitools.client.model.VideoUploadResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VideoUploadApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VideoUploadApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VideoUploadApi(ApiClient apiClient) {
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
     * Build call for importVideo_0
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param targetUrl remote URL where to find the import&#39;s source video (optional)
     * @param magnetUri magnet URI allowing to resolve the import&#39;s source video (optional)
     * @param torrentfile Torrent file containing only the video file (optional)
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
        <tr><td> 400 </td><td> &#x60;magnetUri&#x60; or &#x60;targetUrl&#x60; or a torrent file missing </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass pre-import filter </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> HTTP or Torrent/magnetURI import not enabled </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call importVideo_0Call(Integer channelId, String name, String targetUrl, URI magnetUri, File torrentfile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/imports";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (targetUrl != null) {
            localVarFormParams.put("targetUrl", targetUrl);
        }

        if (magnetUri != null) {
            localVarFormParams.put("magnetUri", magnetUri);
        }

        if (torrentfile != null) {
            localVarFormParams.put("torrentfile", torrentfile);
        }

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
    private okhttp3.Call importVideo_0ValidateBeforeCall(Integer channelId, String name, String targetUrl, URI magnetUri, File torrentfile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'channelId' is set
        if (channelId == null) {
            throw new ApiException("Missing the required parameter 'channelId' when calling importVideo_0(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling importVideo_0(Async)");
        }

        return importVideo_0Call(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);

    }

    /**
     * Import a video
     * Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param targetUrl remote URL where to find the import&#39;s source video (optional)
     * @param magnetUri magnet URI allowing to resolve the import&#39;s source video (optional)
     * @param torrentfile Torrent file containing only the video file (optional)
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
        <tr><td> 400 </td><td> &#x60;magnetUri&#x60; or &#x60;targetUrl&#x60; or a torrent file missing </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass pre-import filter </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> HTTP or Torrent/magnetURI import not enabled </td><td>  -  </td></tr>
     </table>
     */
    public VideoUploadResponse importVideo_0(Integer channelId, String name, String targetUrl, URI magnetUri, File torrentfile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding) throws ApiException {
        ApiResponse<VideoUploadResponse> localVarResp = importVideo_0WithHttpInfo(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
        return localVarResp.getData();
    }

    /**
     * Import a video
     * Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param targetUrl remote URL where to find the import&#39;s source video (optional)
     * @param magnetUri magnet URI allowing to resolve the import&#39;s source video (optional)
     * @param torrentfile Torrent file containing only the video file (optional)
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
        <tr><td> 400 </td><td> &#x60;magnetUri&#x60; or &#x60;targetUrl&#x60; or a torrent file missing </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass pre-import filter </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> HTTP or Torrent/magnetURI import not enabled </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoUploadResponse> importVideo_0WithHttpInfo(Integer channelId, String name, String targetUrl, URI magnetUri, File torrentfile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding) throws ApiException {
        okhttp3.Call localVarCall = importVideo_0ValidateBeforeCall(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, null);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Import a video (asynchronously)
     * Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)
     * @param channelId Channel id that will contain this video (required)
     * @param name Video name (required)
     * @param targetUrl remote URL where to find the import&#39;s source video (optional)
     * @param magnetUri magnet URI allowing to resolve the import&#39;s source video (optional)
     * @param torrentfile Torrent file containing only the video file (optional)
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
        <tr><td> 400 </td><td> &#x60;magnetUri&#x60; or &#x60;targetUrl&#x60; or a torrent file missing </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> video didn&#39;t pass pre-import filter </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> HTTP or Torrent/magnetURI import not enabled </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call importVideo_0Async(Integer channelId, String name, String targetUrl, URI magnetUri, File torrentfile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback<VideoUploadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = importVideo_0ValidateBeforeCall(channelId, name, targetUrl, magnetUri, torrentfile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadLegacy_0
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
    public okhttp3.Call uploadLegacy_0Call(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call uploadLegacy_0ValidateBeforeCall(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'channelId' is set
        if (channelId == null) {
            throw new ApiException("Missing the required parameter 'channelId' when calling uploadLegacy_0(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling uploadLegacy_0(Async)");
        }

        // verify the required parameter 'videofile' is set
        if (videofile == null) {
            throw new ApiException("Missing the required parameter 'videofile' when calling uploadLegacy_0(Async)");
        }

        return uploadLegacy_0Call(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);

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
    public VideoUploadResponse uploadLegacy_0(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding) throws ApiException {
        ApiResponse<VideoUploadResponse> localVarResp = uploadLegacy_0WithHttpInfo(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding);
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
    public ApiResponse<VideoUploadResponse> uploadLegacy_0WithHttpInfo(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding) throws ApiException {
        okhttp3.Call localVarCall = uploadLegacy_0ValidateBeforeCall(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, null);
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
    public okhttp3.Call uploadLegacy_0Async(Integer channelId, String name, File videofile, Integer category, Boolean commentsEnabled, String description, Boolean downloadEnabled, String language, Integer licence, Boolean nsfw, OffsetDateTime originallyPublishedAt, File previewfile, VideoPrivacySet privacy, VideoScheduledUpdate scheduleUpdate, String support, Set<String> tags, File thumbnailfile, Boolean waitTranscoding, final ApiCallback<VideoUploadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadLegacy_0ValidateBeforeCall(channelId, name, videofile, category, commentsEnabled, description, downloadEnabled, language, licence, nsfw, originallyPublishedAt, previewfile, privacy, scheduleUpdate, support, tags, thumbnailfile, waitTranscoding, _callback);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadResumableCancel_0
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
    public okhttp3.Call uploadResumableCancel_0Call(String uploadId, BigDecimal contentLength, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call uploadResumableCancel_0ValidateBeforeCall(String uploadId, BigDecimal contentLength, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'uploadId' is set
        if (uploadId == null) {
            throw new ApiException("Missing the required parameter 'uploadId' when calling uploadResumableCancel_0(Async)");
        }

        // verify the required parameter 'contentLength' is set
        if (contentLength == null) {
            throw new ApiException("Missing the required parameter 'contentLength' when calling uploadResumableCancel_0(Async)");
        }

        return uploadResumableCancel_0Call(uploadId, contentLength, _callback);

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
    public void uploadResumableCancel_0(String uploadId, BigDecimal contentLength) throws ApiException {
        uploadResumableCancel_0WithHttpInfo(uploadId, contentLength);
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
    public ApiResponse<Void> uploadResumableCancel_0WithHttpInfo(String uploadId, BigDecimal contentLength) throws ApiException {
        okhttp3.Call localVarCall = uploadResumableCancel_0ValidateBeforeCall(uploadId, contentLength, null);
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
    public okhttp3.Call uploadResumableCancel_0Async(String uploadId, BigDecimal contentLength, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadResumableCancel_0ValidateBeforeCall(uploadId, contentLength, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadResumableInit_0
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
    public okhttp3.Call uploadResumableInit_0Call(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call uploadResumableInit_0ValidateBeforeCall(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xUploadContentLength' is set
        if (xUploadContentLength == null) {
            throw new ApiException("Missing the required parameter 'xUploadContentLength' when calling uploadResumableInit_0(Async)");
        }

        // verify the required parameter 'xUploadContentType' is set
        if (xUploadContentType == null) {
            throw new ApiException("Missing the required parameter 'xUploadContentType' when calling uploadResumableInit_0(Async)");
        }

        return uploadResumableInit_0Call(xUploadContentLength, xUploadContentType, videoUploadRequestResumable, _callback);

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
    public void uploadResumableInit_0(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable) throws ApiException {
        uploadResumableInit_0WithHttpInfo(xUploadContentLength, xUploadContentType, videoUploadRequestResumable);
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
    public ApiResponse<Void> uploadResumableInit_0WithHttpInfo(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable) throws ApiException {
        okhttp3.Call localVarCall = uploadResumableInit_0ValidateBeforeCall(xUploadContentLength, xUploadContentType, videoUploadRequestResumable, null);
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
    public okhttp3.Call uploadResumableInit_0Async(BigDecimal xUploadContentLength, String xUploadContentType, VideoUploadRequestResumable videoUploadRequestResumable, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadResumableInit_0ValidateBeforeCall(xUploadContentLength, xUploadContentType, videoUploadRequestResumable, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadResumable_0
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
    public okhttp3.Call uploadResumable_0Call(String uploadId, String contentRange, BigDecimal contentLength, File body, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call uploadResumable_0ValidateBeforeCall(String uploadId, String contentRange, BigDecimal contentLength, File body, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'uploadId' is set
        if (uploadId == null) {
            throw new ApiException("Missing the required parameter 'uploadId' when calling uploadResumable_0(Async)");
        }

        // verify the required parameter 'contentRange' is set
        if (contentRange == null) {
            throw new ApiException("Missing the required parameter 'contentRange' when calling uploadResumable_0(Async)");
        }

        // verify the required parameter 'contentLength' is set
        if (contentLength == null) {
            throw new ApiException("Missing the required parameter 'contentLength' when calling uploadResumable_0(Async)");
        }

        return uploadResumable_0Call(uploadId, contentRange, contentLength, body, _callback);

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
    public VideoUploadResponse uploadResumable_0(String uploadId, String contentRange, BigDecimal contentLength, File body) throws ApiException {
        ApiResponse<VideoUploadResponse> localVarResp = uploadResumable_0WithHttpInfo(uploadId, contentRange, contentLength, body);
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
    public ApiResponse<VideoUploadResponse> uploadResumable_0WithHttpInfo(String uploadId, String contentRange, BigDecimal contentLength, File body) throws ApiException {
        okhttp3.Call localVarCall = uploadResumable_0ValidateBeforeCall(uploadId, contentRange, contentLength, body, null);
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
    public okhttp3.Call uploadResumable_0Async(String uploadId, String contentRange, BigDecimal contentLength, File body, final ApiCallback<VideoUploadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadResumable_0ValidateBeforeCall(uploadId, contentRange, contentLength, body, _callback);
        Type localVarReturnType = new TypeToken<VideoUploadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
