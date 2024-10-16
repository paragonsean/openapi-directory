/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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



import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AttackDetectionApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AttackDetectionApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AttackDetectionApi(ApiClient apiClient) {
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
     * Build call for realmAttackDetectionBruteForceUsersDelete
     * @param realm realm name (not id!) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmAttackDetectionBruteForceUsersDeleteCall(String realm, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{realm}/attack-detection/brute-force/users"
            .replace("{" + "realm" + "}", localVarApiClient.escapeString(realm.toString()));

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

        String[] localVarAuthNames = new String[] { "access_token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call realmAttackDetectionBruteForceUsersDeleteValidateBeforeCall(String realm, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmAttackDetectionBruteForceUsersDelete(Async)");
        }

        return realmAttackDetectionBruteForceUsersDeleteCall(realm, _callback);

    }

    /**
     * Clear any user login failures for all users   This can release temporary disabled users
     * 
     * @param realm realm name (not id!) (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public void realmAttackDetectionBruteForceUsersDelete(String realm) throws ApiException {
        realmAttackDetectionBruteForceUsersDeleteWithHttpInfo(realm);
    }

    /**
     * Clear any user login failures for all users   This can release temporary disabled users
     * 
     * @param realm realm name (not id!) (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> realmAttackDetectionBruteForceUsersDeleteWithHttpInfo(String realm) throws ApiException {
        okhttp3.Call localVarCall = realmAttackDetectionBruteForceUsersDeleteValidateBeforeCall(realm, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Clear any user login failures for all users   This can release temporary disabled users (asynchronously)
     * 
     * @param realm realm name (not id!) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmAttackDetectionBruteForceUsersDeleteAsync(String realm, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmAttackDetectionBruteForceUsersDeleteValidateBeforeCall(realm, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for realmAttackDetectionBruteForceUsersUserIdDelete
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmAttackDetectionBruteForceUsersUserIdDeleteCall(String realm, String userId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{realm}/attack-detection/brute-force/users/{userId}"
            .replace("{" + "realm" + "}", localVarApiClient.escapeString(realm.toString()))
            .replace("{" + "userId" + "}", localVarApiClient.escapeString(userId.toString()));

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

        String[] localVarAuthNames = new String[] { "access_token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call realmAttackDetectionBruteForceUsersUserIdDeleteValidateBeforeCall(String realm, String userId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmAttackDetectionBruteForceUsersUserIdDelete(Async)");
        }

        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling realmAttackDetectionBruteForceUsersUserIdDelete(Async)");
        }

        return realmAttackDetectionBruteForceUsersUserIdDeleteCall(realm, userId, _callback);

    }

    /**
     * Clear any user login failures for the user   This can release temporary disabled user
     * 
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public void realmAttackDetectionBruteForceUsersUserIdDelete(String realm, String userId) throws ApiException {
        realmAttackDetectionBruteForceUsersUserIdDeleteWithHttpInfo(realm, userId);
    }

    /**
     * Clear any user login failures for the user   This can release temporary disabled user
     * 
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> realmAttackDetectionBruteForceUsersUserIdDeleteWithHttpInfo(String realm, String userId) throws ApiException {
        okhttp3.Call localVarCall = realmAttackDetectionBruteForceUsersUserIdDeleteValidateBeforeCall(realm, userId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Clear any user login failures for the user   This can release temporary disabled user (asynchronously)
     * 
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmAttackDetectionBruteForceUsersUserIdDeleteAsync(String realm, String userId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmAttackDetectionBruteForceUsersUserIdDeleteValidateBeforeCall(realm, userId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for realmAttackDetectionBruteForceUsersUserIdGet
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmAttackDetectionBruteForceUsersUserIdGetCall(String realm, String userId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{realm}/attack-detection/brute-force/users/{userId}"
            .replace("{" + "realm" + "}", localVarApiClient.escapeString(realm.toString()))
            .replace("{" + "userId" + "}", localVarApiClient.escapeString(userId.toString()));

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

        String[] localVarAuthNames = new String[] { "access_token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call realmAttackDetectionBruteForceUsersUserIdGetValidateBeforeCall(String realm, String userId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmAttackDetectionBruteForceUsersUserIdGet(Async)");
        }

        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling realmAttackDetectionBruteForceUsersUserIdGet(Async)");
        }

        return realmAttackDetectionBruteForceUsersUserIdGetCall(realm, userId, _callback);

    }

    /**
     * Get status of a username in brute force detection
     * 
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @return Map&lt;String, Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public Map<String, Object> realmAttackDetectionBruteForceUsersUserIdGet(String realm, String userId) throws ApiException {
        ApiResponse<Map<String, Object>> localVarResp = realmAttackDetectionBruteForceUsersUserIdGetWithHttpInfo(realm, userId);
        return localVarResp.getData();
    }

    /**
     * Get status of a username in brute force detection
     * 
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @return ApiResponse&lt;Map&lt;String, Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Map<String, Object>> realmAttackDetectionBruteForceUsersUserIdGetWithHttpInfo(String realm, String userId) throws ApiException {
        okhttp3.Call localVarCall = realmAttackDetectionBruteForceUsersUserIdGetValidateBeforeCall(realm, userId, null);
        Type localVarReturnType = new TypeToken<Map<String, Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get status of a username in brute force detection (asynchronously)
     * 
     * @param realm realm name (not id!) (required)
     * @param userId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmAttackDetectionBruteForceUsersUserIdGetAsync(String realm, String userId, final ApiCallback<Map<String, Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmAttackDetectionBruteForceUsersUserIdGetValidateBeforeCall(realm, userId, _callback);
        Type localVarReturnType = new TypeToken<Map<String, Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
