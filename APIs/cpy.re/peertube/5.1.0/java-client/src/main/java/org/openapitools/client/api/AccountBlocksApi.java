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


import org.openapitools.client.model.ApiV1ServerBlocklistAccountsPostRequest;
import org.openapitools.client.model.BlockStatus;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AccountBlocksApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AccountBlocksApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AccountBlocksApi(ApiClient apiClient) {
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
     * Build call for apiV1BlocklistStatusGet
     * @param accounts Check if these accounts are blocked (optional)
     * @param hosts Check if these hosts are blocked (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1BlocklistStatusGetCall(List<String> accounts, List<String> hosts, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/blocklist/status";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accounts != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "accounts", accounts));
        }

        if (hosts != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "hosts", hosts));
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
    private okhttp3.Call apiV1BlocklistStatusGetValidateBeforeCall(List<String> accounts, List<String> hosts, final ApiCallback _callback) throws ApiException {
        return apiV1BlocklistStatusGetCall(accounts, hosts, _callback);

    }

    /**
     * Get block status of accounts/hosts
     * 
     * @param accounts Check if these accounts are blocked (optional)
     * @param hosts Check if these hosts are blocked (optional)
     * @return BlockStatus
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public BlockStatus apiV1BlocklistStatusGet(List<String> accounts, List<String> hosts) throws ApiException {
        ApiResponse<BlockStatus> localVarResp = apiV1BlocklistStatusGetWithHttpInfo(accounts, hosts);
        return localVarResp.getData();
    }

    /**
     * Get block status of accounts/hosts
     * 
     * @param accounts Check if these accounts are blocked (optional)
     * @param hosts Check if these hosts are blocked (optional)
     * @return ApiResponse&lt;BlockStatus&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BlockStatus> apiV1BlocklistStatusGetWithHttpInfo(List<String> accounts, List<String> hosts) throws ApiException {
        okhttp3.Call localVarCall = apiV1BlocklistStatusGetValidateBeforeCall(accounts, hosts, null);
        Type localVarReturnType = new TypeToken<BlockStatus>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get block status of accounts/hosts (asynchronously)
     * 
     * @param accounts Check if these accounts are blocked (optional)
     * @param hosts Check if these hosts are blocked (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1BlocklistStatusGetAsync(List<String> accounts, List<String> hosts, final ApiCallback<BlockStatus> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1BlocklistStatusGetValidateBeforeCall(accounts, hosts, _callback);
        Type localVarReturnType = new TypeToken<BlockStatus>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerBlocklistAccountsAccountNameDelete
     * @param accountName account to unblock, in the form &#x60;username@domain&#x60; (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account or account block does not exist </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerBlocklistAccountsAccountNameDeleteCall(String accountName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/blocklist/accounts/{accountName}"
            .replace("{" + "accountName" + "}", localVarApiClient.escapeString(accountName.toString()));

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
    private okhttp3.Call apiV1ServerBlocklistAccountsAccountNameDeleteValidateBeforeCall(String accountName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accountName' is set
        if (accountName == null) {
            throw new ApiException("Missing the required parameter 'accountName' when calling apiV1ServerBlocklistAccountsAccountNameDelete(Async)");
        }

        return apiV1ServerBlocklistAccountsAccountNameDeleteCall(accountName, _callback);

    }

    /**
     * Unblock an account by its handle
     * 
     * @param accountName account to unblock, in the form &#x60;username@domain&#x60; (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account or account block does not exist </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerBlocklistAccountsAccountNameDelete(String accountName) throws ApiException {
        apiV1ServerBlocklistAccountsAccountNameDeleteWithHttpInfo(accountName);
    }

    /**
     * Unblock an account by its handle
     * 
     * @param accountName account to unblock, in the form &#x60;username@domain&#x60; (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account or account block does not exist </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerBlocklistAccountsAccountNameDeleteWithHttpInfo(String accountName) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerBlocklistAccountsAccountNameDeleteValidateBeforeCall(accountName, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Unblock an account by its handle (asynchronously)
     * 
     * @param accountName account to unblock, in the form &#x60;username@domain&#x60; (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> account or account block does not exist </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerBlocklistAccountsAccountNameDeleteAsync(String accountName, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerBlocklistAccountsAccountNameDeleteValidateBeforeCall(accountName, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerBlocklistAccountsGet
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
    public okhttp3.Call apiV1ServerBlocklistAccountsGetCall(Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/server/blocklist/accounts";

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
    private okhttp3.Call apiV1ServerBlocklistAccountsGetValidateBeforeCall(Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return apiV1ServerBlocklistAccountsGetCall(start, count, sort, _callback);

    }

    /**
     * List account blocks
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerBlocklistAccountsGet(Integer start, Integer count, String sort) throws ApiException {
        apiV1ServerBlocklistAccountsGetWithHttpInfo(start, count, sort);
    }

    /**
     * List account blocks
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerBlocklistAccountsGetWithHttpInfo(Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerBlocklistAccountsGetValidateBeforeCall(start, count, sort, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * List account blocks (asynchronously)
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
    public okhttp3.Call apiV1ServerBlocklistAccountsGetAsync(Integer start, Integer count, String sort, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerBlocklistAccountsGetValidateBeforeCall(start, count, sort, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1ServerBlocklistAccountsPost
     * @param apiV1ServerBlocklistAccountsPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> self-blocking forbidden </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerBlocklistAccountsPostCall(ApiV1ServerBlocklistAccountsPostRequest apiV1ServerBlocklistAccountsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1ServerBlocklistAccountsPostRequest;

        // create path and map variables
        String localVarPath = "/api/v1/server/blocklist/accounts";

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
    private okhttp3.Call apiV1ServerBlocklistAccountsPostValidateBeforeCall(ApiV1ServerBlocklistAccountsPostRequest apiV1ServerBlocklistAccountsPostRequest, final ApiCallback _callback) throws ApiException {
        return apiV1ServerBlocklistAccountsPostCall(apiV1ServerBlocklistAccountsPostRequest, _callback);

    }

    /**
     * Block an account
     * 
     * @param apiV1ServerBlocklistAccountsPostRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> self-blocking forbidden </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1ServerBlocklistAccountsPost(ApiV1ServerBlocklistAccountsPostRequest apiV1ServerBlocklistAccountsPostRequest) throws ApiException {
        apiV1ServerBlocklistAccountsPostWithHttpInfo(apiV1ServerBlocklistAccountsPostRequest);
    }

    /**
     * Block an account
     * 
     * @param apiV1ServerBlocklistAccountsPostRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> self-blocking forbidden </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1ServerBlocklistAccountsPostWithHttpInfo(ApiV1ServerBlocklistAccountsPostRequest apiV1ServerBlocklistAccountsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1ServerBlocklistAccountsPostValidateBeforeCall(apiV1ServerBlocklistAccountsPostRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Block an account (asynchronously)
     * 
     * @param apiV1ServerBlocklistAccountsPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> self-blocking forbidden </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1ServerBlocklistAccountsPostAsync(ApiV1ServerBlocklistAccountsPostRequest apiV1ServerBlocklistAccountsPostRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1ServerBlocklistAccountsPostValidateBeforeCall(apiV1ServerBlocklistAccountsPostRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
