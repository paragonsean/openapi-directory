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


import org.openapitools.client.model.ApiV1UsersMeSubscriptionsPostRequest;
import org.openapitools.client.model.GetAccountVideosCategoryOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLanguageOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLicenceOneOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsAllOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsOneOfParameter;
import java.net.URI;
import org.openapitools.client.model.VideoChannel;
import org.openapitools.client.model.VideoChannelList;
import org.openapitools.client.model.VideoListResponse;
import org.openapitools.client.model.VideoPrivacySet;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MySubscriptionsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MySubscriptionsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MySubscriptionsApi(ApiClient apiClient) {
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
     * Build call for apiV1UsersMeSubscriptionsExistGet
     * @param uris list of uris to check if each is part of the user subscriptions (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsExistGetCall(List<URI> uris, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/me/subscriptions/exist";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (uris != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "uris", uris));
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
    private okhttp3.Call apiV1UsersMeSubscriptionsExistGetValidateBeforeCall(List<URI> uris, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'uris' is set
        if (uris == null) {
            throw new ApiException("Missing the required parameter 'uris' when calling apiV1UsersMeSubscriptionsExistGet(Async)");
        }

        return apiV1UsersMeSubscriptionsExistGetCall(uris, _callback);

    }

    /**
     * Get if subscriptions exist for my user
     * 
     * @param uris list of uris to check if each is part of the user subscriptions (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object apiV1UsersMeSubscriptionsExistGet(List<URI> uris) throws ApiException {
        ApiResponse<Object> localVarResp = apiV1UsersMeSubscriptionsExistGetWithHttpInfo(uris);
        return localVarResp.getData();
    }

    /**
     * Get if subscriptions exist for my user
     * 
     * @param uris list of uris to check if each is part of the user subscriptions (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> apiV1UsersMeSubscriptionsExistGetWithHttpInfo(List<URI> uris) throws ApiException {
        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsExistGetValidateBeforeCall(uris, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get if subscriptions exist for my user (asynchronously)
     * 
     * @param uris list of uris to check if each is part of the user subscriptions (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsExistGetAsync(List<URI> uris, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsExistGetValidateBeforeCall(uris, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1UsersMeSubscriptionsGet
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
    public okhttp3.Call apiV1UsersMeSubscriptionsGetCall(Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/me/subscriptions";

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1UsersMeSubscriptionsGetValidateBeforeCall(Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return apiV1UsersMeSubscriptionsGetCall(start, count, sort, _callback);

    }

    /**
     * Get my user subscriptions
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return VideoChannelList
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoChannelList apiV1UsersMeSubscriptionsGet(Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<VideoChannelList> localVarResp = apiV1UsersMeSubscriptionsGetWithHttpInfo(start, count, sort);
        return localVarResp.getData();
    }

    /**
     * Get my user subscriptions
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;VideoChannelList&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoChannelList> apiV1UsersMeSubscriptionsGetWithHttpInfo(Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsGetValidateBeforeCall(start, count, sort, null);
        Type localVarReturnType = new TypeToken<VideoChannelList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get my user subscriptions (asynchronously)
     * 
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
    public okhttp3.Call apiV1UsersMeSubscriptionsGetAsync(Integer start, Integer count, String sort, final ApiCallback<VideoChannelList> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsGetValidateBeforeCall(start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<VideoChannelList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1UsersMeSubscriptionsPost
     * @param apiV1UsersMeSubscriptionsPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsPostCall(ApiV1UsersMeSubscriptionsPostRequest apiV1UsersMeSubscriptionsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1UsersMeSubscriptionsPostRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/me/subscriptions";

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
    private okhttp3.Call apiV1UsersMeSubscriptionsPostValidateBeforeCall(ApiV1UsersMeSubscriptionsPostRequest apiV1UsersMeSubscriptionsPostRequest, final ApiCallback _callback) throws ApiException {
        return apiV1UsersMeSubscriptionsPostCall(apiV1UsersMeSubscriptionsPostRequest, _callback);

    }

    /**
     * Add subscription to my user
     * 
     * @param apiV1UsersMeSubscriptionsPostRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1UsersMeSubscriptionsPost(ApiV1UsersMeSubscriptionsPostRequest apiV1UsersMeSubscriptionsPostRequest) throws ApiException {
        apiV1UsersMeSubscriptionsPostWithHttpInfo(apiV1UsersMeSubscriptionsPostRequest);
    }

    /**
     * Add subscription to my user
     * 
     * @param apiV1UsersMeSubscriptionsPostRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1UsersMeSubscriptionsPostWithHttpInfo(ApiV1UsersMeSubscriptionsPostRequest apiV1UsersMeSubscriptionsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsPostValidateBeforeCall(apiV1UsersMeSubscriptionsPostRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add subscription to my user (asynchronously)
     * 
     * @param apiV1UsersMeSubscriptionsPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsPostAsync(ApiV1UsersMeSubscriptionsPostRequest apiV1UsersMeSubscriptionsPostRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsPostValidateBeforeCall(apiV1UsersMeSubscriptionsPostRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1UsersMeSubscriptionsSubscriptionHandleDelete
     * @param subscriptionHandle The subscription handle (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsSubscriptionHandleDeleteCall(String subscriptionHandle, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/me/subscriptions/{subscriptionHandle}"
            .replace("{" + "subscriptionHandle" + "}", localVarApiClient.escapeString(subscriptionHandle.toString()));

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
    private okhttp3.Call apiV1UsersMeSubscriptionsSubscriptionHandleDeleteValidateBeforeCall(String subscriptionHandle, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionHandle' is set
        if (subscriptionHandle == null) {
            throw new ApiException("Missing the required parameter 'subscriptionHandle' when calling apiV1UsersMeSubscriptionsSubscriptionHandleDelete(Async)");
        }

        return apiV1UsersMeSubscriptionsSubscriptionHandleDeleteCall(subscriptionHandle, _callback);

    }

    /**
     * Delete subscription of my user
     * 
     * @param subscriptionHandle The subscription handle (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1UsersMeSubscriptionsSubscriptionHandleDelete(String subscriptionHandle) throws ApiException {
        apiV1UsersMeSubscriptionsSubscriptionHandleDeleteWithHttpInfo(subscriptionHandle);
    }

    /**
     * Delete subscription of my user
     * 
     * @param subscriptionHandle The subscription handle (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1UsersMeSubscriptionsSubscriptionHandleDeleteWithHttpInfo(String subscriptionHandle) throws ApiException {
        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsSubscriptionHandleDeleteValidateBeforeCall(subscriptionHandle, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete subscription of my user (asynchronously)
     * 
     * @param subscriptionHandle The subscription handle (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsSubscriptionHandleDeleteAsync(String subscriptionHandle, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsSubscriptionHandleDeleteValidateBeforeCall(subscriptionHandle, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1UsersMeSubscriptionsSubscriptionHandleGet
     * @param subscriptionHandle The subscription handle (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsSubscriptionHandleGetCall(String subscriptionHandle, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/me/subscriptions/{subscriptionHandle}"
            .replace("{" + "subscriptionHandle" + "}", localVarApiClient.escapeString(subscriptionHandle.toString()));

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
    private okhttp3.Call apiV1UsersMeSubscriptionsSubscriptionHandleGetValidateBeforeCall(String subscriptionHandle, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionHandle' is set
        if (subscriptionHandle == null) {
            throw new ApiException("Missing the required parameter 'subscriptionHandle' when calling apiV1UsersMeSubscriptionsSubscriptionHandleGet(Async)");
        }

        return apiV1UsersMeSubscriptionsSubscriptionHandleGetCall(subscriptionHandle, _callback);

    }

    /**
     * Get subscription of my user
     * 
     * @param subscriptionHandle The subscription handle (required)
     * @return VideoChannel
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoChannel apiV1UsersMeSubscriptionsSubscriptionHandleGet(String subscriptionHandle) throws ApiException {
        ApiResponse<VideoChannel> localVarResp = apiV1UsersMeSubscriptionsSubscriptionHandleGetWithHttpInfo(subscriptionHandle);
        return localVarResp.getData();
    }

    /**
     * Get subscription of my user
     * 
     * @param subscriptionHandle The subscription handle (required)
     * @return ApiResponse&lt;VideoChannel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoChannel> apiV1UsersMeSubscriptionsSubscriptionHandleGetWithHttpInfo(String subscriptionHandle) throws ApiException {
        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsSubscriptionHandleGetValidateBeforeCall(subscriptionHandle, null);
        Type localVarReturnType = new TypeToken<VideoChannel>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get subscription of my user (asynchronously)
     * 
     * @param subscriptionHandle The subscription handle (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1UsersMeSubscriptionsSubscriptionHandleGetAsync(String subscriptionHandle, final ApiCallback<VideoChannel> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsSubscriptionHandleGetValidateBeforeCall(subscriptionHandle, _callback);
        Type localVarReturnType = new TypeToken<VideoChannel>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1UsersMeSubscriptionsVideosGet
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
    public okhttp3.Call apiV1UsersMeSubscriptionsVideosGetCall(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/me/subscriptions/videos";

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1UsersMeSubscriptionsVideosGetValidateBeforeCall(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
        return apiV1UsersMeSubscriptionsVideosGetCall(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);

    }

    /**
     * List videos of subscriptions of my user
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
    public VideoListResponse apiV1UsersMeSubscriptionsVideosGet(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        ApiResponse<VideoListResponse> localVarResp = apiV1UsersMeSubscriptionsVideosGetWithHttpInfo(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
        return localVarResp.getData();
    }

    /**
     * List videos of subscriptions of my user
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
    public ApiResponse<VideoListResponse> apiV1UsersMeSubscriptionsVideosGetWithHttpInfo(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsVideosGetValidateBeforeCall(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, null);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List videos of subscriptions of my user (asynchronously)
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
    public okhttp3.Call apiV1UsersMeSubscriptionsVideosGetAsync(GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback<VideoListResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1UsersMeSubscriptionsVideosGetValidateBeforeCall(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
