/*
 * Enterobase-API
 *  API for EnteroBase (https://enterobase.warwick.ac.uk)   EnteroBase is a user-friendly online resource, where users can upload their  own sequencing data for de novo assembly by a stream-lined pipeline. The assemblies  are used for calling MLST and wgMLST patterns, allowing users to compare their strains  to publically available genotyping data from other EnteroBase users, GenBank and classical MLST databases.  Click here to find how to get and use an API token: http://bit.ly/1TKlaOU 
 *
 * The version of the OpenAPI document: v2.0
 * Contact: enterobase@warwick.ac.uk
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

public class LoginApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LoginApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LoginApi(ApiClient apiClient) {
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
     * Build call for apiV20LoginGet
     * @param password EnteroBase Password (optional)
     * @param username EnteroBase username (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A login object </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource or data </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV20LoginGetCall(String password, String username, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2.0/login";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (password != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("password", password));
        }

        if (username != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("username", username));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV20LoginGetValidateBeforeCall(String password, String username, final ApiCallback _callback) throws ApiException {
        return apiV20LoginGetCall(password, username, _callback);

    }

    /**
     * 
     * Login endpoint, refresh your API token
     * @param password EnteroBase Password (optional)
     * @param username EnteroBase username (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A login object </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource or data </td><td>  -  </td></tr>
     </table>
     */
    public void apiV20LoginGet(String password, String username) throws ApiException {
        apiV20LoginGetWithHttpInfo(password, username);
    }

    /**
     * 
     * Login endpoint, refresh your API token
     * @param password EnteroBase Password (optional)
     * @param username EnteroBase username (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A login object </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource or data </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV20LoginGetWithHttpInfo(String password, String username) throws ApiException {
        okhttp3.Call localVarCall = apiV20LoginGetValidateBeforeCall(password, username, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Login endpoint, refresh your API token
     * @param password EnteroBase Password (optional)
     * @param username EnteroBase username (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A login object </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Unauthorised access for this specific resource or data </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV20LoginGetAsync(String password, String username, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV20LoginGetValidateBeforeCall(password, username, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
