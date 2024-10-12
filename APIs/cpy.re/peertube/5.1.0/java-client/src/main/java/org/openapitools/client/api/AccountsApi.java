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


import org.openapitools.client.model.Account;
import org.openapitools.client.model.ApiV1AccountsNameVideoPlaylistsGet200Response;
import org.openapitools.client.model.GetAccountFollowers200Response;
import org.openapitools.client.model.GetAccountVideosCategoryOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLanguageOneOfParameter;
import org.openapitools.client.model.GetAccountVideosLicenceOneOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsAllOfParameter;
import org.openapitools.client.model.GetAccountVideosTagsOneOfParameter;
import org.openapitools.client.model.VideoChannelList;
import org.openapitools.client.model.VideoChannelSyncList;
import org.openapitools.client.model.VideoListResponse;
import org.openapitools.client.model.VideoPlaylistTypeSet;
import org.openapitools.client.model.VideoPrivacySet;
import org.openapitools.client.model.VideoRating;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AccountsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AccountsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AccountsApi(ApiClient apiClient) {
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
     * Build call for apiV1AccountsNameRatingsGet
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param rating Optionally filter which ratings to retrieve (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AccountsNameRatingsGetCall(String name, Integer start, Integer count, String sort, String rating, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts/{name}/ratings"
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

        if (rating != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("rating", rating));
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
    private okhttp3.Call apiV1AccountsNameRatingsGetValidateBeforeCall(String name, Integer start, Integer count, String sort, String rating, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling apiV1AccountsNameRatingsGet(Async)");
        }

        return apiV1AccountsNameRatingsGetCall(name, start, count, sort, rating, _callback);

    }

    /**
     * List ratings of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param rating Optionally filter which ratings to retrieve (optional)
     * @return List&lt;VideoRating&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<VideoRating> apiV1AccountsNameRatingsGet(String name, Integer start, Integer count, String sort, String rating) throws ApiException {
        ApiResponse<List<VideoRating>> localVarResp = apiV1AccountsNameRatingsGetWithHttpInfo(name, start, count, sort, rating);
        return localVarResp.getData();
    }

    /**
     * List ratings of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param rating Optionally filter which ratings to retrieve (optional)
     * @return ApiResponse&lt;List&lt;VideoRating&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<VideoRating>> apiV1AccountsNameRatingsGetWithHttpInfo(String name, Integer start, Integer count, String sort, String rating) throws ApiException {
        okhttp3.Call localVarCall = apiV1AccountsNameRatingsGetValidateBeforeCall(name, start, count, sort, rating, null);
        Type localVarReturnType = new TypeToken<List<VideoRating>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List ratings of an account (asynchronously)
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param rating Optionally filter which ratings to retrieve (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AccountsNameRatingsGetAsync(String name, Integer start, Integer count, String sort, String rating, final ApiCallback<List<VideoRating>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AccountsNameRatingsGetValidateBeforeCall(name, start, count, sort, rating, _callback);
        Type localVarReturnType = new TypeToken<List<VideoRating>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AccountsNameVideoChannelSyncsGet_1
     * @param name The username or handle of the account (required)
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
    public okhttp3.Call apiV1AccountsNameVideoChannelSyncsGet_1Call(String name, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts/{name}/video-channel-syncs"
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
    private okhttp3.Call apiV1AccountsNameVideoChannelSyncsGet_1ValidateBeforeCall(String name, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling apiV1AccountsNameVideoChannelSyncsGet_1(Async)");
        }

        return apiV1AccountsNameVideoChannelSyncsGet_1Call(name, start, count, sort, _callback);

    }

    /**
     * List the synchronizations of video channels of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return VideoChannelSyncList
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public VideoChannelSyncList apiV1AccountsNameVideoChannelSyncsGet_1(String name, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<VideoChannelSyncList> localVarResp = apiV1AccountsNameVideoChannelSyncsGet_1WithHttpInfo(name, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List the synchronizations of video channels of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;VideoChannelSyncList&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<VideoChannelSyncList> apiV1AccountsNameVideoChannelSyncsGet_1WithHttpInfo(String name, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = apiV1AccountsNameVideoChannelSyncsGet_1ValidateBeforeCall(name, start, count, sort, null);
        Type localVarReturnType = new TypeToken<VideoChannelSyncList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List the synchronizations of video channels of an account (asynchronously)
     * 
     * @param name The username or handle of the account (required)
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
    public okhttp3.Call apiV1AccountsNameVideoChannelSyncsGet_1Async(String name, Integer start, Integer count, String sort, final ApiCallback<VideoChannelSyncList> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AccountsNameVideoChannelSyncsGet_1ValidateBeforeCall(name, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<VideoChannelSyncList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AccountsNameVideoChannelsGet_0
     * @param name The username or handle of the account (required)
     * @param withStats include daily view statistics for the last 30 days and total views (only if authentified as the account user) (optional)
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
    public okhttp3.Call apiV1AccountsNameVideoChannelsGet_0Call(String name, Boolean withStats, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts/{name}/video-channels"
            .replace("{" + "name" + "}", localVarApiClient.escapeString(name.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (withStats != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("withStats", withStats));
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
    private okhttp3.Call apiV1AccountsNameVideoChannelsGet_0ValidateBeforeCall(String name, Boolean withStats, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling apiV1AccountsNameVideoChannelsGet_0(Async)");
        }

        return apiV1AccountsNameVideoChannelsGet_0Call(name, withStats, start, count, sort, _callback);

    }

    /**
     * List video channels of an account
     * 
     * @param name The username or handle of the account (required)
     * @param withStats include daily view statistics for the last 30 days and total views (only if authentified as the account user) (optional)
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
    public VideoChannelList apiV1AccountsNameVideoChannelsGet_0(String name, Boolean withStats, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<VideoChannelList> localVarResp = apiV1AccountsNameVideoChannelsGet_0WithHttpInfo(name, withStats, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List video channels of an account
     * 
     * @param name The username or handle of the account (required)
     * @param withStats include daily view statistics for the last 30 days and total views (only if authentified as the account user) (optional)
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
    public ApiResponse<VideoChannelList> apiV1AccountsNameVideoChannelsGet_0WithHttpInfo(String name, Boolean withStats, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = apiV1AccountsNameVideoChannelsGet_0ValidateBeforeCall(name, withStats, start, count, sort, null);
        Type localVarReturnType = new TypeToken<VideoChannelList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List video channels of an account (asynchronously)
     * 
     * @param name The username or handle of the account (required)
     * @param withStats include daily view statistics for the last 30 days and total views (only if authentified as the account user) (optional)
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
    public okhttp3.Call apiV1AccountsNameVideoChannelsGet_0Async(String name, Boolean withStats, Integer start, Integer count, String sort, final ApiCallback<VideoChannelList> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AccountsNameVideoChannelsGet_0ValidateBeforeCall(name, withStats, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<VideoChannelList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AccountsNameVideoPlaylistsGet_0
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
    public okhttp3.Call apiV1AccountsNameVideoPlaylistsGet_0Call(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call apiV1AccountsNameVideoPlaylistsGet_0ValidateBeforeCall(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling apiV1AccountsNameVideoPlaylistsGet_0(Async)");
        }

        return apiV1AccountsNameVideoPlaylistsGet_0Call(name, start, count, sort, search, playlistType, _callback);

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
    public ApiV1AccountsNameVideoPlaylistsGet200Response apiV1AccountsNameVideoPlaylistsGet_0(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType) throws ApiException {
        ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> localVarResp = apiV1AccountsNameVideoPlaylistsGet_0WithHttpInfo(name, start, count, sort, search, playlistType);
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
    public ApiResponse<ApiV1AccountsNameVideoPlaylistsGet200Response> apiV1AccountsNameVideoPlaylistsGet_0WithHttpInfo(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType) throws ApiException {
        okhttp3.Call localVarCall = apiV1AccountsNameVideoPlaylistsGet_0ValidateBeforeCall(name, start, count, sort, search, playlistType, null);
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
    public okhttp3.Call apiV1AccountsNameVideoPlaylistsGet_0Async(String name, Integer start, Integer count, String sort, String search, VideoPlaylistTypeSet playlistType, final ApiCallback<ApiV1AccountsNameVideoPlaylistsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AccountsNameVideoPlaylistsGet_0ValidateBeforeCall(name, start, count, sort, search, playlistType, _callback);
        Type localVarReturnType = new TypeToken<ApiV1AccountsNameVideoPlaylistsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAccount
     * @param name The username or handle of the account (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAccountCall(String name, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts/{name}"
            .replace("{" + "name" + "}", localVarApiClient.escapeString(name.toString()));

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
    private okhttp3.Call getAccountValidateBeforeCall(String name, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling getAccount(Async)");
        }

        return getAccountCall(name, _callback);

    }

    /**
     * Get an account
     * 
     * @param name The username or handle of the account (required)
     * @return Account
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account not found </td><td>  -  </td></tr>
     </table>
     */
    public Account getAccount(String name) throws ApiException {
        ApiResponse<Account> localVarResp = getAccountWithHttpInfo(name);
        return localVarResp.getData();
    }

    /**
     * Get an account
     * 
     * @param name The username or handle of the account (required)
     * @return ApiResponse&lt;Account&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Account> getAccountWithHttpInfo(String name) throws ApiException {
        okhttp3.Call localVarCall = getAccountValidateBeforeCall(name, null);
        Type localVarReturnType = new TypeToken<Account>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get an account (asynchronously)
     * 
     * @param name The username or handle of the account (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAccountAsync(String name, final ApiCallback<Account> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAccountValidateBeforeCall(name, _callback);
        Type localVarReturnType = new TypeToken<Account>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAccountFollowers
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort followers by criteria (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAccountFollowersCall(String name, Integer start, Integer count, String sort, String search, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts/{name}/followers"
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
    private okhttp3.Call getAccountFollowersValidateBeforeCall(String name, Integer start, Integer count, String sort, String search, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling getAccountFollowers(Async)");
        }

        return getAccountFollowersCall(name, start, count, sort, search, _callback);

    }

    /**
     * List followers of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort followers by criteria (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @return GetAccountFollowers200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetAccountFollowers200Response getAccountFollowers(String name, Integer start, Integer count, String sort, String search) throws ApiException {
        ApiResponse<GetAccountFollowers200Response> localVarResp = getAccountFollowersWithHttpInfo(name, start, count, sort, search);
        return localVarResp.getData();
    }

    /**
     * List followers of an account
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort followers by criteria (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @return ApiResponse&lt;GetAccountFollowers200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAccountFollowers200Response> getAccountFollowersWithHttpInfo(String name, Integer start, Integer count, String sort, String search) throws ApiException {
        okhttp3.Call localVarCall = getAccountFollowersValidateBeforeCall(name, start, count, sort, search, null);
        Type localVarReturnType = new TypeToken<GetAccountFollowers200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List followers of an account (asynchronously)
     * 
     * @param name The username or handle of the account (required)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort followers by criteria (optional)
     * @param search Plain text search, applied to various parts of the model depending on endpoint (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAccountFollowersAsync(String name, Integer start, Integer count, String sort, String search, final ApiCallback<GetAccountFollowers200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAccountFollowersValidateBeforeCall(name, start, count, sort, search, _callback);
        Type localVarReturnType = new TypeToken<GetAccountFollowers200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAccountVideos
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
    public okhttp3.Call getAccountVideosCall(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call getAccountVideosValidateBeforeCall(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling getAccountVideos(Async)");
        }

        return getAccountVideosCall(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);

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
    public VideoListResponse getAccountVideos(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        ApiResponse<VideoListResponse> localVarResp = getAccountVideosWithHttpInfo(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
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
    public ApiResponse<VideoListResponse> getAccountVideosWithHttpInfo(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched) throws ApiException {
        okhttp3.Call localVarCall = getAccountVideosValidateBeforeCall(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, null);
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
    public okhttp3.Call getAccountVideosAsync(String name, GetAccountVideosCategoryOneOfParameter categoryOneOf, Boolean isLive, GetAccountVideosTagsOneOfParameter tagsOneOf, GetAccountVideosTagsAllOfParameter tagsAllOf, GetAccountVideosLicenceOneOfParameter licenceOneOf, GetAccountVideosLanguageOneOfParameter languageOneOf, String nsfw, Boolean isLocal, Integer include, VideoPrivacySet privacyOneOf, Boolean hasHLSFiles, Boolean hasWebtorrentFiles, String skipCount, Integer start, Integer count, String sort, Boolean excludeAlreadyWatched, final ApiCallback<VideoListResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAccountVideosValidateBeforeCall(name, categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched, _callback);
        Type localVarReturnType = new TypeToken<VideoListResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAccounts
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
    public okhttp3.Call getAccountsCall(Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/accounts";

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
    private okhttp3.Call getAccountsValidateBeforeCall(Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return getAccountsCall(start, count, sort, _callback);

    }

    /**
     * List accounts
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return List&lt;Account&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<Account> getAccounts(Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<List<Account>> localVarResp = getAccountsWithHttpInfo(start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List accounts
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;List&lt;Account&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Account>> getAccountsWithHttpInfo(Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = getAccountsValidateBeforeCall(start, count, sort, null);
        Type localVarReturnType = new TypeToken<List<Account>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List accounts (asynchronously)
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
    public okhttp3.Call getAccountsAsync(Integer start, Integer count, String sort, final ApiCallback<List<Account>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAccountsValidateBeforeCall(start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<List<Account>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
