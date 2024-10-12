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


import org.openapitools.client.model.AbuseStateSet;
import org.openapitools.client.model.ApiV1AbusesAbuseIdMessagesGet200Response;
import org.openapitools.client.model.ApiV1AbusesAbuseIdMessagesPostRequest;
import org.openapitools.client.model.ApiV1AbusesAbuseIdPutRequest;
import org.openapitools.client.model.ApiV1AbusesPost200Response;
import org.openapitools.client.model.ApiV1AbusesPostRequest;
import org.openapitools.client.model.GetAbuses200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AbusesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AbusesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AbusesApi(ApiClient apiClient) {
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
     * Build call for apiV1AbusesAbuseIdDelete
     * @param abuseId Abuse id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> block not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdDeleteCall(Integer abuseId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/abuses/{abuseId}"
            .replace("{" + "abuseId" + "}", localVarApiClient.escapeString(abuseId.toString()));

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
    private okhttp3.Call apiV1AbusesAbuseIdDeleteValidateBeforeCall(Integer abuseId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'abuseId' is set
        if (abuseId == null) {
            throw new ApiException("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdDelete(Async)");
        }

        return apiV1AbusesAbuseIdDeleteCall(abuseId, _callback);

    }

    /**
     * Delete an abuse
     * 
     * @param abuseId Abuse id (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> block not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1AbusesAbuseIdDelete(Integer abuseId) throws ApiException {
        apiV1AbusesAbuseIdDeleteWithHttpInfo(abuseId);
    }

    /**
     * Delete an abuse
     * 
     * @param abuseId Abuse id (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> block not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1AbusesAbuseIdDeleteWithHttpInfo(Integer abuseId) throws ApiException {
        okhttp3.Call localVarCall = apiV1AbusesAbuseIdDeleteValidateBeforeCall(abuseId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete an abuse (asynchronously)
     * 
     * @param abuseId Abuse id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> block not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdDeleteAsync(Integer abuseId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AbusesAbuseIdDeleteValidateBeforeCall(abuseId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete
     * @param abuseId Abuse id (required)
     * @param abuseMessageId Abuse message id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteCall(Integer abuseId, Integer abuseMessageId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/abuses/{abuseId}/messages/{abuseMessageId}"
            .replace("{" + "abuseId" + "}", localVarApiClient.escapeString(abuseId.toString()))
            .replace("{" + "abuseMessageId" + "}", localVarApiClient.escapeString(abuseMessageId.toString()));

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
    private okhttp3.Call apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteValidateBeforeCall(Integer abuseId, Integer abuseMessageId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'abuseId' is set
        if (abuseId == null) {
            throw new ApiException("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(Async)");
        }

        // verify the required parameter 'abuseMessageId' is set
        if (abuseMessageId == null) {
            throw new ApiException("Missing the required parameter 'abuseMessageId' when calling apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(Async)");
        }

        return apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteCall(abuseId, abuseMessageId, _callback);

    }

    /**
     * Delete an abuse message
     * 
     * @param abuseId Abuse id (required)
     * @param abuseMessageId Abuse message id (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(Integer abuseId, Integer abuseMessageId) throws ApiException {
        apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteWithHttpInfo(abuseId, abuseMessageId);
    }

    /**
     * Delete an abuse message
     * 
     * @param abuseId Abuse id (required)
     * @param abuseMessageId Abuse message id (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteWithHttpInfo(Integer abuseId, Integer abuseMessageId) throws ApiException {
        okhttp3.Call localVarCall = apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteValidateBeforeCall(abuseId, abuseMessageId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete an abuse message (asynchronously)
     * 
     * @param abuseId Abuse id (required)
     * @param abuseMessageId Abuse message id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteAsync(Integer abuseId, Integer abuseMessageId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteValidateBeforeCall(abuseId, abuseMessageId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AbusesAbuseIdMessagesGet
     * @param abuseId Abuse id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdMessagesGetCall(Integer abuseId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/abuses/{abuseId}/messages"
            .replace("{" + "abuseId" + "}", localVarApiClient.escapeString(abuseId.toString()));

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
    private okhttp3.Call apiV1AbusesAbuseIdMessagesGetValidateBeforeCall(Integer abuseId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'abuseId' is set
        if (abuseId == null) {
            throw new ApiException("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdMessagesGet(Async)");
        }

        return apiV1AbusesAbuseIdMessagesGetCall(abuseId, _callback);

    }

    /**
     * List messages of an abuse
     * 
     * @param abuseId Abuse id (required)
     * @return ApiV1AbusesAbuseIdMessagesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiV1AbusesAbuseIdMessagesGet200Response apiV1AbusesAbuseIdMessagesGet(Integer abuseId) throws ApiException {
        ApiResponse<ApiV1AbusesAbuseIdMessagesGet200Response> localVarResp = apiV1AbusesAbuseIdMessagesGetWithHttpInfo(abuseId);
        return localVarResp.getData();
    }

    /**
     * List messages of an abuse
     * 
     * @param abuseId Abuse id (required)
     * @return ApiResponse&lt;ApiV1AbusesAbuseIdMessagesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiV1AbusesAbuseIdMessagesGet200Response> apiV1AbusesAbuseIdMessagesGetWithHttpInfo(Integer abuseId) throws ApiException {
        okhttp3.Call localVarCall = apiV1AbusesAbuseIdMessagesGetValidateBeforeCall(abuseId, null);
        Type localVarReturnType = new TypeToken<ApiV1AbusesAbuseIdMessagesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List messages of an abuse (asynchronously)
     * 
     * @param abuseId Abuse id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdMessagesGetAsync(Integer abuseId, final ApiCallback<ApiV1AbusesAbuseIdMessagesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AbusesAbuseIdMessagesGetValidateBeforeCall(abuseId, _callback);
        Type localVarReturnType = new TypeToken<ApiV1AbusesAbuseIdMessagesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AbusesAbuseIdMessagesPost
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdMessagesPostRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdMessagesPostCall(Integer abuseId, ApiV1AbusesAbuseIdMessagesPostRequest apiV1AbusesAbuseIdMessagesPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1AbusesAbuseIdMessagesPostRequest;

        // create path and map variables
        String localVarPath = "/api/v1/abuses/{abuseId}/messages"
            .replace("{" + "abuseId" + "}", localVarApiClient.escapeString(abuseId.toString()));

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
    private okhttp3.Call apiV1AbusesAbuseIdMessagesPostValidateBeforeCall(Integer abuseId, ApiV1AbusesAbuseIdMessagesPostRequest apiV1AbusesAbuseIdMessagesPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'abuseId' is set
        if (abuseId == null) {
            throw new ApiException("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdMessagesPost(Async)");
        }

        // verify the required parameter 'apiV1AbusesAbuseIdMessagesPostRequest' is set
        if (apiV1AbusesAbuseIdMessagesPostRequest == null) {
            throw new ApiException("Missing the required parameter 'apiV1AbusesAbuseIdMessagesPostRequest' when calling apiV1AbusesAbuseIdMessagesPost(Async)");
        }

        return apiV1AbusesAbuseIdMessagesPostCall(abuseId, apiV1AbusesAbuseIdMessagesPostRequest, _callback);

    }

    /**
     * Add message to an abuse
     * 
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdMessagesPostRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1AbusesAbuseIdMessagesPost(Integer abuseId, ApiV1AbusesAbuseIdMessagesPostRequest apiV1AbusesAbuseIdMessagesPostRequest) throws ApiException {
        apiV1AbusesAbuseIdMessagesPostWithHttpInfo(abuseId, apiV1AbusesAbuseIdMessagesPostRequest);
    }

    /**
     * Add message to an abuse
     * 
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdMessagesPostRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1AbusesAbuseIdMessagesPostWithHttpInfo(Integer abuseId, ApiV1AbusesAbuseIdMessagesPostRequest apiV1AbusesAbuseIdMessagesPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1AbusesAbuseIdMessagesPostValidateBeforeCall(abuseId, apiV1AbusesAbuseIdMessagesPostRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add message to an abuse (asynchronously)
     * 
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdMessagesPostRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdMessagesPostAsync(Integer abuseId, ApiV1AbusesAbuseIdMessagesPostRequest apiV1AbusesAbuseIdMessagesPostRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AbusesAbuseIdMessagesPostValidateBeforeCall(abuseId, apiV1AbusesAbuseIdMessagesPostRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AbusesAbuseIdPut
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> abuse not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdPutCall(Integer abuseId, ApiV1AbusesAbuseIdPutRequest apiV1AbusesAbuseIdPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1AbusesAbuseIdPutRequest;

        // create path and map variables
        String localVarPath = "/api/v1/abuses/{abuseId}"
            .replace("{" + "abuseId" + "}", localVarApiClient.escapeString(abuseId.toString()));

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
    private okhttp3.Call apiV1AbusesAbuseIdPutValidateBeforeCall(Integer abuseId, ApiV1AbusesAbuseIdPutRequest apiV1AbusesAbuseIdPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'abuseId' is set
        if (abuseId == null) {
            throw new ApiException("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdPut(Async)");
        }

        return apiV1AbusesAbuseIdPutCall(abuseId, apiV1AbusesAbuseIdPutRequest, _callback);

    }

    /**
     * Update an abuse
     * 
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdPutRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> abuse not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1AbusesAbuseIdPut(Integer abuseId, ApiV1AbusesAbuseIdPutRequest apiV1AbusesAbuseIdPutRequest) throws ApiException {
        apiV1AbusesAbuseIdPutWithHttpInfo(abuseId, apiV1AbusesAbuseIdPutRequest);
    }

    /**
     * Update an abuse
     * 
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdPutRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> abuse not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1AbusesAbuseIdPutWithHttpInfo(Integer abuseId, ApiV1AbusesAbuseIdPutRequest apiV1AbusesAbuseIdPutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1AbusesAbuseIdPutValidateBeforeCall(abuseId, apiV1AbusesAbuseIdPutRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update an abuse (asynchronously)
     * 
     * @param abuseId Abuse id (required)
     * @param apiV1AbusesAbuseIdPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> abuse not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesAbuseIdPutAsync(Integer abuseId, ApiV1AbusesAbuseIdPutRequest apiV1AbusesAbuseIdPutRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AbusesAbuseIdPutValidateBeforeCall(abuseId, apiV1AbusesAbuseIdPutRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1AbusesPost
     * @param apiV1AbusesPostRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesPostCall(ApiV1AbusesPostRequest apiV1AbusesPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1AbusesPostRequest;

        // create path and map variables
        String localVarPath = "/api/v1/abuses";

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
    private okhttp3.Call apiV1AbusesPostValidateBeforeCall(ApiV1AbusesPostRequest apiV1AbusesPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiV1AbusesPostRequest' is set
        if (apiV1AbusesPostRequest == null) {
            throw new ApiException("Missing the required parameter 'apiV1AbusesPostRequest' when calling apiV1AbusesPost(Async)");
        }

        return apiV1AbusesPostCall(apiV1AbusesPostRequest, _callback);

    }

    /**
     * Report an abuse
     * 
     * @param apiV1AbusesPostRequest  (required)
     * @return ApiV1AbusesPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public ApiV1AbusesPost200Response apiV1AbusesPost(ApiV1AbusesPostRequest apiV1AbusesPostRequest) throws ApiException {
        ApiResponse<ApiV1AbusesPost200Response> localVarResp = apiV1AbusesPostWithHttpInfo(apiV1AbusesPostRequest);
        return localVarResp.getData();
    }

    /**
     * Report an abuse
     * 
     * @param apiV1AbusesPostRequest  (required)
     * @return ApiResponse&lt;ApiV1AbusesPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiV1AbusesPost200Response> apiV1AbusesPostWithHttpInfo(ApiV1AbusesPostRequest apiV1AbusesPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1AbusesPostValidateBeforeCall(apiV1AbusesPostRequest, null);
        Type localVarReturnType = new TypeToken<ApiV1AbusesPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Report an abuse (asynchronously)
     * 
     * @param apiV1AbusesPostRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> incorrect request parameters </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1AbusesPostAsync(ApiV1AbusesPostRequest apiV1AbusesPostRequest, final ApiCallback<ApiV1AbusesPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1AbusesPostValidateBeforeCall(apiV1AbusesPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiV1AbusesPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAbuses
     * @param id only list the report with this id (optional)
     * @param predefinedReason predefined reason the listed reports should contain (optional)
     * @param search plain search that will match with video titles, reporter names and more (optional)
     * @param state  (optional)
     * @param searchReporter only list reports of a specific reporter (optional)
     * @param searchReportee only list reports of a specific reportee (optional)
     * @param searchVideo only list reports of a specific video (optional)
     * @param searchVideoChannel only list reports of a specific video channel (optional)
     * @param videoIs only list deleted or blocklisted videos (optional)
     * @param filter only list account, comment or video reports (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort abuses by criteria (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAbusesCall(Integer id, List<String> predefinedReason, String search, AbuseStateSet state, String searchReporter, String searchReportee, String searchVideo, String searchVideoChannel, String videoIs, String filter, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/abuses";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (id != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("id", id));
        }

        if (predefinedReason != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "predefinedReason", predefinedReason));
        }

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (state != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("state", state));
        }

        if (searchReporter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchReporter", searchReporter));
        }

        if (searchReportee != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchReportee", searchReportee));
        }

        if (searchVideo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchVideo", searchVideo));
        }

        if (searchVideoChannel != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("searchVideoChannel", searchVideoChannel));
        }

        if (videoIs != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("videoIs", videoIs));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAbusesValidateBeforeCall(Integer id, List<String> predefinedReason, String search, AbuseStateSet state, String searchReporter, String searchReportee, String searchVideo, String searchVideoChannel, String videoIs, String filter, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return getAbusesCall(id, predefinedReason, search, state, searchReporter, searchReportee, searchVideo, searchVideoChannel, videoIs, filter, start, count, sort, _callback);

    }

    /**
     * List abuses
     * 
     * @param id only list the report with this id (optional)
     * @param predefinedReason predefined reason the listed reports should contain (optional)
     * @param search plain search that will match with video titles, reporter names and more (optional)
     * @param state  (optional)
     * @param searchReporter only list reports of a specific reporter (optional)
     * @param searchReportee only list reports of a specific reportee (optional)
     * @param searchVideo only list reports of a specific video (optional)
     * @param searchVideoChannel only list reports of a specific video channel (optional)
     * @param videoIs only list deleted or blocklisted videos (optional)
     * @param filter only list account, comment or video reports (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort abuses by criteria (optional)
     * @return GetAbuses200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetAbuses200Response getAbuses(Integer id, List<String> predefinedReason, String search, AbuseStateSet state, String searchReporter, String searchReportee, String searchVideo, String searchVideoChannel, String videoIs, String filter, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<GetAbuses200Response> localVarResp = getAbusesWithHttpInfo(id, predefinedReason, search, state, searchReporter, searchReportee, searchVideo, searchVideoChannel, videoIs, filter, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List abuses
     * 
     * @param id only list the report with this id (optional)
     * @param predefinedReason predefined reason the listed reports should contain (optional)
     * @param search plain search that will match with video titles, reporter names and more (optional)
     * @param state  (optional)
     * @param searchReporter only list reports of a specific reporter (optional)
     * @param searchReportee only list reports of a specific reportee (optional)
     * @param searchVideo only list reports of a specific video (optional)
     * @param searchVideoChannel only list reports of a specific video channel (optional)
     * @param videoIs only list deleted or blocklisted videos (optional)
     * @param filter only list account, comment or video reports (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort abuses by criteria (optional)
     * @return ApiResponse&lt;GetAbuses200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAbuses200Response> getAbusesWithHttpInfo(Integer id, List<String> predefinedReason, String search, AbuseStateSet state, String searchReporter, String searchReportee, String searchVideo, String searchVideoChannel, String videoIs, String filter, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = getAbusesValidateBeforeCall(id, predefinedReason, search, state, searchReporter, searchReportee, searchVideo, searchVideoChannel, videoIs, filter, start, count, sort, null);
        Type localVarReturnType = new TypeToken<GetAbuses200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List abuses (asynchronously)
     * 
     * @param id only list the report with this id (optional)
     * @param predefinedReason predefined reason the listed reports should contain (optional)
     * @param search plain search that will match with video titles, reporter names and more (optional)
     * @param state  (optional)
     * @param searchReporter only list reports of a specific reporter (optional)
     * @param searchReportee only list reports of a specific reportee (optional)
     * @param searchVideo only list reports of a specific video (optional)
     * @param searchVideoChannel only list reports of a specific video channel (optional)
     * @param videoIs only list deleted or blocklisted videos (optional)
     * @param filter only list account, comment or video reports (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort abuses by criteria (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAbusesAsync(Integer id, List<String> predefinedReason, String search, AbuseStateSet state, String searchReporter, String searchReportee, String searchVideo, String searchVideoChannel, String videoIs, String filter, Integer start, Integer count, String sort, final ApiCallback<GetAbuses200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAbusesValidateBeforeCall(id, predefinedReason, search, state, searchReporter, searchReportee, searchVideo, searchVideoChannel, videoIs, filter, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<GetAbuses200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMyAbuses
     * @param id only list the report with this id (optional)
     * @param state  (optional)
     * @param sort Sort abuses by criteria (optional)
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
    public okhttp3.Call getMyAbusesCall(Integer id, AbuseStateSet state, String sort, Integer start, Integer count, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/me/abuses";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (id != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("id", id));
        }

        if (state != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("state", state));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getMyAbusesValidateBeforeCall(Integer id, AbuseStateSet state, String sort, Integer start, Integer count, final ApiCallback _callback) throws ApiException {
        return getMyAbusesCall(id, state, sort, start, count, _callback);

    }

    /**
     * List my abuses
     * 
     * @param id only list the report with this id (optional)
     * @param state  (optional)
     * @param sort Sort abuses by criteria (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @return GetAbuses200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetAbuses200Response getMyAbuses(Integer id, AbuseStateSet state, String sort, Integer start, Integer count) throws ApiException {
        ApiResponse<GetAbuses200Response> localVarResp = getMyAbusesWithHttpInfo(id, state, sort, start, count);
        return localVarResp.getData();
    }

    /**
     * List my abuses
     * 
     * @param id only list the report with this id (optional)
     * @param state  (optional)
     * @param sort Sort abuses by criteria (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @return ApiResponse&lt;GetAbuses200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAbuses200Response> getMyAbusesWithHttpInfo(Integer id, AbuseStateSet state, String sort, Integer start, Integer count) throws ApiException {
        okhttp3.Call localVarCall = getMyAbusesValidateBeforeCall(id, state, sort, start, count, null);
        Type localVarReturnType = new TypeToken<GetAbuses200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List my abuses (asynchronously)
     * 
     * @param id only list the report with this id (optional)
     * @param state  (optional)
     * @param sort Sort abuses by criteria (optional)
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
    public okhttp3.Call getMyAbusesAsync(Integer id, AbuseStateSet state, String sort, Integer start, Integer count, final ApiCallback<GetAbuses200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMyAbusesValidateBeforeCall(id, state, sort, start, count, _callback);
        Type localVarReturnType = new TypeToken<GetAbuses200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
