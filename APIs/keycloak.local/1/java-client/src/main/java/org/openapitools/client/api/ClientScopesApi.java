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


import org.openapitools.client.model.ClientScopeRepresentation;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ClientScopesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ClientScopesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ClientScopesApi(ApiClient apiClient) {
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
     * Build call for realmClientScopesGet
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
    public okhttp3.Call realmClientScopesGetCall(String realm, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{realm}/client-scopes"
            .replace("{" + "realm" + "}", localVarApiClient.escapeString(realm.toString()));

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
    private okhttp3.Call realmClientScopesGetValidateBeforeCall(String realm, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmClientScopesGet(Async)");
        }

        return realmClientScopesGetCall(realm, _callback);

    }

    /**
     * Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm
     * 
     * @param realm realm name (not id!) (required)
     * @return List&lt;ClientScopeRepresentation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public List<ClientScopeRepresentation> realmClientScopesGet(String realm) throws ApiException {
        ApiResponse<List<ClientScopeRepresentation>> localVarResp = realmClientScopesGetWithHttpInfo(realm);
        return localVarResp.getData();
    }

    /**
     * Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm
     * 
     * @param realm realm name (not id!) (required)
     * @return ApiResponse&lt;List&lt;ClientScopeRepresentation&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ClientScopeRepresentation>> realmClientScopesGetWithHttpInfo(String realm) throws ApiException {
        okhttp3.Call localVarCall = realmClientScopesGetValidateBeforeCall(realm, null);
        Type localVarReturnType = new TypeToken<List<ClientScopeRepresentation>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm (asynchronously)
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
    public okhttp3.Call realmClientScopesGetAsync(String realm, final ApiCallback<List<ClientScopeRepresentation>> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmClientScopesGetValidateBeforeCall(realm, _callback);
        Type localVarReturnType = new TypeToken<List<ClientScopeRepresentation>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for realmClientScopesIdDelete
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesIdDeleteCall(String realm, String id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{realm}/client-scopes/{id}"
            .replace("{" + "realm" + "}", localVarApiClient.escapeString(realm.toString()))
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

        String[] localVarAuthNames = new String[] { "access_token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call realmClientScopesIdDeleteValidateBeforeCall(String realm, String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmClientScopesIdDelete(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling realmClientScopesIdDelete(Async)");
        }

        return realmClientScopesIdDeleteCall(realm, id, _callback);

    }

    /**
     * Delete the client scope
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public void realmClientScopesIdDelete(String realm, String id) throws ApiException {
        realmClientScopesIdDeleteWithHttpInfo(realm, id);
    }

    /**
     * Delete the client scope
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> realmClientScopesIdDeleteWithHttpInfo(String realm, String id) throws ApiException {
        okhttp3.Call localVarCall = realmClientScopesIdDeleteValidateBeforeCall(realm, id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete the client scope (asynchronously)
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesIdDeleteAsync(String realm, String id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmClientScopesIdDeleteValidateBeforeCall(realm, id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for realmClientScopesIdGet
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesIdGetCall(String realm, String id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{realm}/client-scopes/{id}"
            .replace("{" + "realm" + "}", localVarApiClient.escapeString(realm.toString()))
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

        String[] localVarAuthNames = new String[] { "access_token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call realmClientScopesIdGetValidateBeforeCall(String realm, String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmClientScopesIdGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling realmClientScopesIdGet(Async)");
        }

        return realmClientScopesIdGetCall(realm, id, _callback);

    }

    /**
     * Get representation of the client scope
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @return ClientScopeRepresentation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ClientScopeRepresentation realmClientScopesIdGet(String realm, String id) throws ApiException {
        ApiResponse<ClientScopeRepresentation> localVarResp = realmClientScopesIdGetWithHttpInfo(realm, id);
        return localVarResp.getData();
    }

    /**
     * Get representation of the client scope
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @return ApiResponse&lt;ClientScopeRepresentation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClientScopeRepresentation> realmClientScopesIdGetWithHttpInfo(String realm, String id) throws ApiException {
        okhttp3.Call localVarCall = realmClientScopesIdGetValidateBeforeCall(realm, id, null);
        Type localVarReturnType = new TypeToken<ClientScopeRepresentation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get representation of the client scope (asynchronously)
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesIdGetAsync(String realm, String id, final ApiCallback<ClientScopeRepresentation> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmClientScopesIdGetValidateBeforeCall(realm, id, _callback);
        Type localVarReturnType = new TypeToken<ClientScopeRepresentation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for realmClientScopesIdPut
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param clientScopeRepresentation  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesIdPutCall(String realm, String id, ClientScopeRepresentation clientScopeRepresentation, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = clientScopeRepresentation;

        // create path and map variables
        String localVarPath = "/{realm}/client-scopes/{id}"
            .replace("{" + "realm" + "}", localVarApiClient.escapeString(realm.toString()))
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

        String[] localVarAuthNames = new String[] { "access_token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call realmClientScopesIdPutValidateBeforeCall(String realm, String id, ClientScopeRepresentation clientScopeRepresentation, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmClientScopesIdPut(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling realmClientScopesIdPut(Async)");
        }

        // verify the required parameter 'clientScopeRepresentation' is set
        if (clientScopeRepresentation == null) {
            throw new ApiException("Missing the required parameter 'clientScopeRepresentation' when calling realmClientScopesIdPut(Async)");
        }

        return realmClientScopesIdPutCall(realm, id, clientScopeRepresentation, _callback);

    }

    /**
     * Update the client scope
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param clientScopeRepresentation  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public void realmClientScopesIdPut(String realm, String id, ClientScopeRepresentation clientScopeRepresentation) throws ApiException {
        realmClientScopesIdPutWithHttpInfo(realm, id, clientScopeRepresentation);
    }

    /**
     * Update the client scope
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param clientScopeRepresentation  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> realmClientScopesIdPutWithHttpInfo(String realm, String id, ClientScopeRepresentation clientScopeRepresentation) throws ApiException {
        okhttp3.Call localVarCall = realmClientScopesIdPutValidateBeforeCall(realm, id, clientScopeRepresentation, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update the client scope (asynchronously)
     * 
     * @param realm realm name (not id!) (required)
     * @param id id of client scope (not name) (required)
     * @param clientScopeRepresentation  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesIdPutAsync(String realm, String id, ClientScopeRepresentation clientScopeRepresentation, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmClientScopesIdPutValidateBeforeCall(realm, id, clientScopeRepresentation, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for realmClientScopesPost
     * @param realm realm name (not id!) (required)
     * @param clientScopeRepresentation  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesPostCall(String realm, ClientScopeRepresentation clientScopeRepresentation, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = clientScopeRepresentation;

        // create path and map variables
        String localVarPath = "/{realm}/client-scopes"
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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "access_token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call realmClientScopesPostValidateBeforeCall(String realm, ClientScopeRepresentation clientScopeRepresentation, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'realm' is set
        if (realm == null) {
            throw new ApiException("Missing the required parameter 'realm' when calling realmClientScopesPost(Async)");
        }

        // verify the required parameter 'clientScopeRepresentation' is set
        if (clientScopeRepresentation == null) {
            throw new ApiException("Missing the required parameter 'clientScopeRepresentation' when calling realmClientScopesPost(Async)");
        }

        return realmClientScopesPostCall(realm, clientScopeRepresentation, _callback);

    }

    /**
     * Create a new client scope   Client Scope’s name must be unique!
     * 
     * @param realm realm name (not id!) (required)
     * @param clientScopeRepresentation  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public void realmClientScopesPost(String realm, ClientScopeRepresentation clientScopeRepresentation) throws ApiException {
        realmClientScopesPostWithHttpInfo(realm, clientScopeRepresentation);
    }

    /**
     * Create a new client scope   Client Scope’s name must be unique!
     * 
     * @param realm realm name (not id!) (required)
     * @param clientScopeRepresentation  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> realmClientScopesPostWithHttpInfo(String realm, ClientScopeRepresentation clientScopeRepresentation) throws ApiException {
        okhttp3.Call localVarCall = realmClientScopesPostValidateBeforeCall(realm, clientScopeRepresentation, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a new client scope   Client Scope’s name must be unique! (asynchronously)
     * 
     * @param realm realm name (not id!) (required)
     * @param clientScopeRepresentation  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 2XX </td><td> success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call realmClientScopesPostAsync(String realm, ClientScopeRepresentation clientScopeRepresentation, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = realmClientScopesPostValidateBeforeCall(realm, clientScopeRepresentation, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
