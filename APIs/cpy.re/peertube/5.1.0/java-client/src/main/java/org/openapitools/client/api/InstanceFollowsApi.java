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


import org.openapitools.client.model.ApiV1ServerFollowingPostRequest;
import org.openapitools.client.model.GetAccountFollowers200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InstanceFollowsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public InstanceFollowsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public InstanceFollowsApi(ApiClient apiClient) {
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
     * Build call for apiV1ServerFollowersGet
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersGetCall(String state, String actorType, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/followers";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (state != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("state", state));
        }

        if (actorType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("actorType", actorType));
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
    private okhttp3.Call apiV1ServerFollowersGetValidateBeforeCall(String state, String actorType, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return apiV1ServerFollowersGetCall(state, actorType, start, count, sort, _callback);

    }

    /**
     * List instances following the server
     * 
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return GetAccountFollowers200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetAccountFollowers200Response apiV1ServerFollowersGet(String state, String actorType, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<GetAccountFollowers200Response> localVarResp = apiV1ServerFollowersGetWithHttpInfo(state, actorType, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List instances following the server
     * 
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;GetAccountFollowers200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAccountFollowers200Response> apiV1ServerFollowersGetWithHttpInfo(String state, String actorType, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerFollowersGetValidateBeforeCall(state, actorType, start, count, sort, null);
        Type localVarReturnType = new TypeToken<GetAccountFollowers200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List instances following the server (asynchronously)
     * 
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersGetAsync(String state, String actorType, Integer start, Integer count, String sort, final ApiCallback<GetAccountFollowers200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerFollowersGetValidateBeforeCall(state, actorType, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<GetAccountFollowers200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerFollowersNameWithHostAcceptPost
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersNameWithHostAcceptPostCall(String nameWithHost, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/followers/{nameWithHost}/accept"
            .replace("{" + "nameWithHost" + "}", localVarApiClient.escapeString(nameWithHost.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1ServerFollowersNameWithHostAcceptPostValidateBeforeCall(String nameWithHost, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nameWithHost' is set
        if (nameWithHost == null) {
            throw new ApiException("Missing the required parameter 'nameWithHost' when calling apiV1ServerFollowersNameWithHostAcceptPost(Async)");
        }

        return apiV1ServerFollowersNameWithHostAcceptPostCall(nameWithHost, _callback);

    }

    /**
     * Accept a pending follower to your server
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerFollowersNameWithHostAcceptPost(String nameWithHost) throws ApiException {
        apiV1ServerFollowersNameWithHostAcceptPostWithHttpInfo(nameWithHost);
    }

    /**
     * Accept a pending follower to your server
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerFollowersNameWithHostAcceptPostWithHttpInfo(String nameWithHost) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerFollowersNameWithHostAcceptPostValidateBeforeCall(nameWithHost, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Accept a pending follower to your server (asynchronously)
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersNameWithHostAcceptPostAsync(String nameWithHost, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerFollowersNameWithHostAcceptPostValidateBeforeCall(nameWithHost, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerFollowersNameWithHostDelete
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersNameWithHostDeleteCall(String nameWithHost, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/followers/{nameWithHost}"
            .replace("{" + "nameWithHost" + "}", localVarApiClient.escapeString(nameWithHost.toString()));

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
    private okhttp3.Call apiV1ServerFollowersNameWithHostDeleteValidateBeforeCall(String nameWithHost, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nameWithHost' is set
        if (nameWithHost == null) {
            throw new ApiException("Missing the required parameter 'nameWithHost' when calling apiV1ServerFollowersNameWithHostDelete(Async)");
        }

        return apiV1ServerFollowersNameWithHostDeleteCall(nameWithHost, _callback);

    }

    /**
     * Remove or reject a follower to your server
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerFollowersNameWithHostDelete(String nameWithHost) throws ApiException {
        apiV1ServerFollowersNameWithHostDeleteWithHttpInfo(nameWithHost);
    }

    /**
     * Remove or reject a follower to your server
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerFollowersNameWithHostDeleteWithHttpInfo(String nameWithHost) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerFollowersNameWithHostDeleteValidateBeforeCall(nameWithHost, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Remove or reject a follower to your server (asynchronously)
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersNameWithHostDeleteAsync(String nameWithHost, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerFollowersNameWithHostDeleteValidateBeforeCall(nameWithHost, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerFollowersNameWithHostRejectPost
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersNameWithHostRejectPostCall(String nameWithHost, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/followers/{nameWithHost}/reject"
            .replace("{" + "nameWithHost" + "}", localVarApiClient.escapeString(nameWithHost.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1ServerFollowersNameWithHostRejectPostValidateBeforeCall(String nameWithHost, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nameWithHost' is set
        if (nameWithHost == null) {
            throw new ApiException("Missing the required parameter 'nameWithHost' when calling apiV1ServerFollowersNameWithHostRejectPost(Async)");
        }

        return apiV1ServerFollowersNameWithHostRejectPostCall(nameWithHost, _callback);

    }

    /**
     * Reject a pending follower to your server
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerFollowersNameWithHostRejectPost(String nameWithHost) throws ApiException {
        apiV1ServerFollowersNameWithHostRejectPostWithHttpInfo(nameWithHost);
    }

    /**
     * Reject a pending follower to your server
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerFollowersNameWithHostRejectPostWithHttpInfo(String nameWithHost) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerFollowersNameWithHostRejectPostValidateBeforeCall(nameWithHost, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Reject a pending follower to your server (asynchronously)
     * 
     * @param nameWithHost The remote actor handle to remove from your followers (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> follower not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowersNameWithHostRejectPostAsync(String nameWithHost, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerFollowersNameWithHostRejectPostValidateBeforeCall(nameWithHost, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerFollowingGet
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowingGetCall(String state, String actorType, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/following";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (state != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("state", state));
        }

        if (actorType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("actorType", actorType));
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
    private okhttp3.Call apiV1ServerFollowingGetValidateBeforeCall(String state, String actorType, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return apiV1ServerFollowingGetCall(state, actorType, start, count, sort, _callback);

    }

    /**
     * List instances followed by the server
     * 
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return GetAccountFollowers200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetAccountFollowers200Response apiV1ServerFollowingGet(String state, String actorType, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<GetAccountFollowers200Response> localVarResp = apiV1ServerFollowingGetWithHttpInfo(state, actorType, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List instances followed by the server
     * 
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;GetAccountFollowers200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAccountFollowers200Response> apiV1ServerFollowingGetWithHttpInfo(String state, String actorType, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerFollowingGetValidateBeforeCall(state, actorType, start, count, sort, null);
        Type localVarReturnType = new TypeToken<GetAccountFollowers200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List instances followed by the server (asynchronously)
     * 
     * @param state  (optional)
     * @param actorType  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowingGetAsync(String state, String actorType, Integer start, Integer count, String sort, final ApiCallback<GetAccountFollowers200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerFollowingGetValidateBeforeCall(state, actorType, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<GetAccountFollowers200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerFollowingHostOrHandleDelete
     * @param hostOrHandle The hostOrHandle to unfollow (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> host or handle not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowingHostOrHandleDeleteCall(String hostOrHandle, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/following/{hostOrHandle}"
            .replace("{" + "hostOrHandle" + "}", localVarApiClient.escapeString(hostOrHandle.toString()));

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
    private okhttp3.Call apiV1ServerFollowingHostOrHandleDeleteValidateBeforeCall(String hostOrHandle, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'hostOrHandle' is set
        if (hostOrHandle == null) {
            throw new ApiException("Missing the required parameter 'hostOrHandle' when calling apiV1ServerFollowingHostOrHandleDelete(Async)");
        }

        return apiV1ServerFollowingHostOrHandleDeleteCall(hostOrHandle, _callback);

    }

    /**
     * Unfollow an actor (PeerTube instance, channel or account)
     * 
     * @param hostOrHandle The hostOrHandle to unfollow (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> host or handle not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerFollowingHostOrHandleDelete(String hostOrHandle) throws ApiException {
        apiV1ServerFollowingHostOrHandleDeleteWithHttpInfo(hostOrHandle);
    }

    /**
     * Unfollow an actor (PeerTube instance, channel or account)
     * 
     * @param hostOrHandle The hostOrHandle to unfollow (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> host or handle not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerFollowingHostOrHandleDeleteWithHttpInfo(String hostOrHandle) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerFollowingHostOrHandleDeleteValidateBeforeCall(hostOrHandle, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Unfollow an actor (PeerTube instance, channel or account) (asynchronously)
     * 
     * @param hostOrHandle The hostOrHandle to unfollow (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> host or handle not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowingHostOrHandleDeleteAsync(String hostOrHandle, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerFollowingHostOrHandleDeleteValidateBeforeCall(hostOrHandle, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerFollowingPost
     * @param apiV1ServerFollowingPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> cannot follow a non-HTTPS server </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowingPostCall(ApiV1ServerFollowingPostRequest apiV1ServerFollowingPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1ServerFollowingPostRequest;

        // create path and map variables
        String localVarPath = "/api/v1/server/following";

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
    private okhttp3.Call apiV1ServerFollowingPostValidateBeforeCall(ApiV1ServerFollowingPostRequest apiV1ServerFollowingPostRequest, final ApiCallback _callback) throws ApiException {
        return apiV1ServerFollowingPostCall(apiV1ServerFollowingPostRequest, _callback);

    }

    /**
     * Follow a list of actors (PeerTube instance, channel or account)
     * 
     * @param apiV1ServerFollowingPostRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> cannot follow a non-HTTPS server </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerFollowingPost(ApiV1ServerFollowingPostRequest apiV1ServerFollowingPostRequest) throws ApiException {
        apiV1ServerFollowingPostWithHttpInfo(apiV1ServerFollowingPostRequest);
    }

    /**
     * Follow a list of actors (PeerTube instance, channel or account)
     * 
     * @param apiV1ServerFollowingPostRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> cannot follow a non-HTTPS server </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerFollowingPostWithHttpInfo(ApiV1ServerFollowingPostRequest apiV1ServerFollowingPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerFollowingPostValidateBeforeCall(apiV1ServerFollowingPostRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Follow a list of actors (PeerTube instance, channel or account) (asynchronously)
     * 
     * @param apiV1ServerFollowingPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> cannot follow a non-HTTPS server </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerFollowingPostAsync(ApiV1ServerFollowingPostRequest apiV1ServerFollowingPostRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerFollowingPostValidateBeforeCall(apiV1ServerFollowingPostRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
