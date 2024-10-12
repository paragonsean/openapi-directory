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


import org.openapitools.client.model.ApiV1VideosIdCommentThreadsPostRequest;
import org.openapitools.client.model.CommentThreadPostResponse;
import org.openapitools.client.model.CommentThreadResponse;
import org.openapitools.client.model.GetLiveIdIdParameter;
import org.openapitools.client.model.VideoCommentThreadTree;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VideoCommentsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VideoCommentsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VideoCommentsApi(ApiClient apiClient) {
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
     * Build call for apiV1VideosIdCommentThreadsGet
     * @param id The object id, uuid or short uuid (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort comments by criteria (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentThreadsGetCall(GetLiveIdIdParameter id, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/comment-threads"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
    private okhttp3.Call apiV1VideosIdCommentThreadsGetValidateBeforeCall(GetLiveIdIdParameter id, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdCommentThreadsGet(Async)");
        }

        return apiV1VideosIdCommentThreadsGetCall(id, start, count, sort, _callback);

    }

    /**
     * List threads of a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort comments by criteria (optional)
     * @return CommentThreadResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public CommentThreadResponse apiV1VideosIdCommentThreadsGet(GetLiveIdIdParameter id, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<CommentThreadResponse> localVarResp = apiV1VideosIdCommentThreadsGetWithHttpInfo(id, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List threads of a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort comments by criteria (optional)
     * @return ApiResponse&lt;CommentThreadResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CommentThreadResponse> apiV1VideosIdCommentThreadsGetWithHttpInfo(GetLiveIdIdParameter id, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdCommentThreadsGetValidateBeforeCall(id, start, count, sort, null);
        Type localVarReturnType = new TypeToken<CommentThreadResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List threads of a video (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort comments by criteria (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentThreadsGetAsync(GetLiveIdIdParameter id, Integer start, Integer count, String sort, final ApiCallback<CommentThreadResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdCommentThreadsGetValidateBeforeCall(id, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<CommentThreadResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosIdCommentThreadsPost
     * @param id The object id, uuid or short uuid (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentThreadsPostCall(GetLiveIdIdParameter id, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1VideosIdCommentThreadsPostRequest;

        // create path and map variables
        String localVarPath = "/api/v1/videos/{id}/comment-threads"
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
    private okhttp3.Call apiV1VideosIdCommentThreadsPostValidateBeforeCall(GetLiveIdIdParameter id, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdCommentThreadsPost(Async)");
        }

        return apiV1VideosIdCommentThreadsPostCall(id, apiV1VideosIdCommentThreadsPostRequest, _callback);

    }

    /**
     * Create a thread
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @return CommentThreadPostResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public CommentThreadPostResponse apiV1VideosIdCommentThreadsPost(GetLiveIdIdParameter id, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest) throws ApiException {
        ApiResponse<CommentThreadPostResponse> localVarResp = apiV1VideosIdCommentThreadsPostWithHttpInfo(id, apiV1VideosIdCommentThreadsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Create a thread
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @return ApiResponse&lt;CommentThreadPostResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CommentThreadPostResponse> apiV1VideosIdCommentThreadsPostWithHttpInfo(GetLiveIdIdParameter id, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdCommentThreadsPostValidateBeforeCall(id, apiV1VideosIdCommentThreadsPostRequest, null);
        Type localVarReturnType = new TypeToken<CommentThreadPostResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a thread (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentThreadsPostAsync(GetLiveIdIdParameter id, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest, final ApiCallback<CommentThreadPostResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdCommentThreadsPostValidateBeforeCall(id, apiV1VideosIdCommentThreadsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<CommentThreadPostResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosIdCommentThreadsThreadIdGet
     * @param id The object id, uuid or short uuid (required)
     * @param threadId The thread id (root comment id) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentThreadsThreadIdGetCall(GetLiveIdIdParameter id, Integer threadId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/comment-threads/{threadId}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "threadId" + "}", localVarApiClient.escapeString(threadId.toString()));

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
    private okhttp3.Call apiV1VideosIdCommentThreadsThreadIdGetValidateBeforeCall(GetLiveIdIdParameter id, Integer threadId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdCommentThreadsThreadIdGet(Async)");
        }

        // verify the required parameter 'threadId' is set
        if (threadId == null) {
            throw new ApiException("Missing the required parameter 'threadId' when calling apiV1VideosIdCommentThreadsThreadIdGet(Async)");
        }

        return apiV1VideosIdCommentThreadsThreadIdGetCall(id, threadId, _callback);

    }

    /**
     * Get a thread
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param threadId The thread id (root comment id) (required)
     * @return VideoCommentThreadTree
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoCommentThreadTree apiV1VideosIdCommentThreadsThreadIdGet(GetLiveIdIdParameter id, Integer threadId) throws ApiException {
        ApiResponse<VideoCommentThreadTree> localVarResp = apiV1VideosIdCommentThreadsThreadIdGetWithHttpInfo(id, threadId);
        return localVarResp.getData();
    }

    /**
     * Get a thread
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param threadId The thread id (root comment id) (required)
     * @return ApiResponse&lt;VideoCommentThreadTree&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoCommentThreadTree> apiV1VideosIdCommentThreadsThreadIdGetWithHttpInfo(GetLiveIdIdParameter id, Integer threadId) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdCommentThreadsThreadIdGetValidateBeforeCall(id, threadId, null);
        Type localVarReturnType = new TypeToken<VideoCommentThreadTree>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a thread (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param threadId The thread id (root comment id) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentThreadsThreadIdGetAsync(GetLiveIdIdParameter id, Integer threadId, final ApiCallback<VideoCommentThreadTree> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdCommentThreadsThreadIdGetValidateBeforeCall(id, threadId, _callback);
        Type localVarReturnType = new TypeToken<VideoCommentThreadTree>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosIdCommentsCommentIdDelete
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> cannot remove comment of another user </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> comment or video does not exist </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> comment is already deleted </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentsCommentIdDeleteCall(GetLiveIdIdParameter id, Integer commentId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/videos/{id}/comments/{commentId}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "commentId" + "}", localVarApiClient.escapeString(commentId.toString()));

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
    private okhttp3.Call apiV1VideosIdCommentsCommentIdDeleteValidateBeforeCall(GetLiveIdIdParameter id, Integer commentId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdCommentsCommentIdDelete(Async)");
        }

        // verify the required parameter 'commentId' is set
        if (commentId == null) {
            throw new ApiException("Missing the required parameter 'commentId' when calling apiV1VideosIdCommentsCommentIdDelete(Async)");
        }

        return apiV1VideosIdCommentsCommentIdDeleteCall(id, commentId, _callback);

    }

    /**
     * Delete a comment or a reply
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> cannot remove comment of another user </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> comment or video does not exist </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> comment is already deleted </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1VideosIdCommentsCommentIdDelete(GetLiveIdIdParameter id, Integer commentId) throws ApiException {
        apiV1VideosIdCommentsCommentIdDeleteWithHttpInfo(id, commentId);
    }

    /**
     * Delete a comment or a reply
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> cannot remove comment of another user </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> comment or video does not exist </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> comment is already deleted </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1VideosIdCommentsCommentIdDeleteWithHttpInfo(GetLiveIdIdParameter id, Integer commentId) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdCommentsCommentIdDeleteValidateBeforeCall(id, commentId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a comment or a reply (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> cannot remove comment of another user </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> comment or video does not exist </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> comment is already deleted </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentsCommentIdDeleteAsync(GetLiveIdIdParameter id, Integer commentId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdCommentsCommentIdDeleteValidateBeforeCall(id, commentId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1VideosIdCommentsCommentIdPost
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> thread or video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentsCommentIdPostCall(GetLiveIdIdParameter id, Integer commentId, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1VideosIdCommentThreadsPostRequest;

        // create path and map variables
        String localVarPath = "/api/v1/videos/{id}/comments/{commentId}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "commentId" + "}", localVarApiClient.escapeString(commentId.toString()));

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
    private okhttp3.Call apiV1VideosIdCommentsCommentIdPostValidateBeforeCall(GetLiveIdIdParameter id, Integer commentId, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling apiV1VideosIdCommentsCommentIdPost(Async)");
        }

        // verify the required parameter 'commentId' is set
        if (commentId == null) {
            throw new ApiException("Missing the required parameter 'commentId' when calling apiV1VideosIdCommentsCommentIdPost(Async)");
        }

        return apiV1VideosIdCommentsCommentIdPostCall(id, commentId, apiV1VideosIdCommentThreadsPostRequest, _callback);

    }

    /**
     * Reply to a thread of a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @return CommentThreadPostResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> thread or video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public CommentThreadPostResponse apiV1VideosIdCommentsCommentIdPost(GetLiveIdIdParameter id, Integer commentId, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest) throws ApiException {
        ApiResponse<CommentThreadPostResponse> localVarResp = apiV1VideosIdCommentsCommentIdPostWithHttpInfo(id, commentId, apiV1VideosIdCommentThreadsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Reply to a thread of a video
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @return ApiResponse&lt;CommentThreadPostResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> thread or video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CommentThreadPostResponse> apiV1VideosIdCommentsCommentIdPostWithHttpInfo(GetLiveIdIdParameter id, Integer commentId, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1VideosIdCommentsCommentIdPostValidateBeforeCall(id, commentId, apiV1VideosIdCommentThreadsPostRequest, null);
        Type localVarReturnType = new TypeToken<CommentThreadPostResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reply to a thread of a video (asynchronously)
     * 
     * @param id The object id, uuid or short uuid (required)
     * @param commentId The comment id (required)
     * @param apiV1VideosIdCommentThreadsPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> thread or video does not exist </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1VideosIdCommentsCommentIdPostAsync(GetLiveIdIdParameter id, Integer commentId, ApiV1VideosIdCommentThreadsPostRequest apiV1VideosIdCommentThreadsPostRequest, final ApiCallback<CommentThreadPostResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1VideosIdCommentsCommentIdPostValidateBeforeCall(id, commentId, apiV1VideosIdCommentThreadsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<CommentThreadPostResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
