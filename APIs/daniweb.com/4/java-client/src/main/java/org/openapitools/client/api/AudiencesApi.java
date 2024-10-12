/*
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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


import org.openapitools.client.model.EndpointGetAudiences;
import org.openapitools.client.model.EndpointGetAudiencesID;
import org.openapitools.client.model.EndpointPostAudiencesIDMemberships;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AudiencesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AudiencesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AudiencesApi(ApiClient apiClient) {
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
     * Build call for audiencesGet
     * @param offset  (optional, default to 0)
     * @param limit  (optional, default to 50)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call audiencesGetCall(Integer offset, Integer limit, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/audiences";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
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

        String[] localVarAuthNames = new String[] { "implicit_flow", "explicit_flow" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call audiencesGetValidateBeforeCall(Integer offset, Integer limit, final ApiCallback _callback) throws ApiException {
        return audiencesGetCall(offset, limit, _callback);

    }

    /**
     * 
     * Fetch all Daniapp audience segments that comprise the current access token&#39;s bubble.
     * @param offset  (optional, default to 0)
     * @param limit  (optional, default to 50)
     * @return EndpointGetAudiences
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointGetAudiences audiencesGet(Integer offset, Integer limit) throws ApiException {
        ApiResponse<EndpointGetAudiences> localVarResp = audiencesGetWithHttpInfo(offset, limit);
        return localVarResp.getData();
    }

    /**
     * 
     * Fetch all Daniapp audience segments that comprise the current access token&#39;s bubble.
     * @param offset  (optional, default to 0)
     * @param limit  (optional, default to 50)
     * @return ApiResponse&lt;EndpointGetAudiences&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointGetAudiences> audiencesGetWithHttpInfo(Integer offset, Integer limit) throws ApiException {
        okhttp3.Call localVarCall = audiencesGetValidateBeforeCall(offset, limit, null);
        Type localVarReturnType = new TypeToken<EndpointGetAudiences>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Fetch all Daniapp audience segments that comprise the current access token&#39;s bubble.
     * @param offset  (optional, default to 0)
     * @param limit  (optional, default to 50)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call audiencesGetAsync(Integer offset, Integer limit, final ApiCallback<EndpointGetAudiences> _callback) throws ApiException {

        okhttp3.Call localVarCall = audiencesGetValidateBeforeCall(offset, limit, _callback);
        Type localVarReturnType = new TypeToken<EndpointGetAudiences>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for audiencesIDGet
     * @param ID  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call audiencesIDGetCall(List<Integer> ID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/audiences/{ID}"
            .replace("{" + "ID" + "}", localVarApiClient.escapeString(localVarApiClient.collectionPathParameterToString("csv", ID)));

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

        String[] localVarAuthNames = new String[] { "implicit_flow", "explicit_flow" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call audiencesIDGetValidateBeforeCall(List<Integer> ID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling audiencesIDGet(Async)");
        }

        return audiencesIDGetCall(ID, _callback);

    }

    /**
     * 
     * Fetch an array of Daniapp audience segments that comprise the current access token&#39;s bubble.
     * @param ID  (required)
     * @return EndpointGetAudiencesID
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointGetAudiencesID audiencesIDGet(List<Integer> ID) throws ApiException {
        ApiResponse<EndpointGetAudiencesID> localVarResp = audiencesIDGetWithHttpInfo(ID);
        return localVarResp.getData();
    }

    /**
     * 
     * Fetch an array of Daniapp audience segments that comprise the current access token&#39;s bubble.
     * @param ID  (required)
     * @return ApiResponse&lt;EndpointGetAudiencesID&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointGetAudiencesID> audiencesIDGetWithHttpInfo(List<Integer> ID) throws ApiException {
        okhttp3.Call localVarCall = audiencesIDGetValidateBeforeCall(ID, null);
        Type localVarReturnType = new TypeToken<EndpointGetAudiencesID>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Fetch an array of Daniapp audience segments that comprise the current access token&#39;s bubble.
     * @param ID  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call audiencesIDGetAsync(List<Integer> ID, final ApiCallback<EndpointGetAudiencesID> _callback) throws ApiException {

        okhttp3.Call localVarCall = audiencesIDGetValidateBeforeCall(ID, _callback);
        Type localVarReturnType = new TypeToken<EndpointGetAudiencesID>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for audiencesIDMembershipsPost
     * @param ID  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call audiencesIDMembershipsPostCall(Integer ID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/audiences/{ID}/memberships"
            .replace("{" + "ID" + "}", localVarApiClient.escapeString(ID.toString()));

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

        String[] localVarAuthNames = new String[] { "implicit_flow", "explicit_flow" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call audiencesIDMembershipsPostValidateBeforeCall(Integer ID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling audiencesIDMembershipsPost(Async)");
        }

        return audiencesIDMembershipsPostCall(ID, _callback);

    }

    /**
     * 
     * Create a membership record for the OAuth&#39;ed end-user based on the current audience segment/bubble combination.
     * @param ID  (required)
     * @return EndpointPostAudiencesIDMemberships
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointPostAudiencesIDMemberships audiencesIDMembershipsPost(Integer ID) throws ApiException {
        ApiResponse<EndpointPostAudiencesIDMemberships> localVarResp = audiencesIDMembershipsPostWithHttpInfo(ID);
        return localVarResp.getData();
    }

    /**
     * 
     * Create a membership record for the OAuth&#39;ed end-user based on the current audience segment/bubble combination.
     * @param ID  (required)
     * @return ApiResponse&lt;EndpointPostAudiencesIDMemberships&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointPostAudiencesIDMemberships> audiencesIDMembershipsPostWithHttpInfo(Integer ID) throws ApiException {
        okhttp3.Call localVarCall = audiencesIDMembershipsPostValidateBeforeCall(ID, null);
        Type localVarReturnType = new TypeToken<EndpointPostAudiencesIDMemberships>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Create a membership record for the OAuth&#39;ed end-user based on the current audience segment/bubble combination.
     * @param ID  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call audiencesIDMembershipsPostAsync(Integer ID, final ApiCallback<EndpointPostAudiencesIDMemberships> _callback) throws ApiException {

        okhttp3.Call localVarCall = audiencesIDMembershipsPostValidateBeforeCall(ID, _callback);
        Type localVarReturnType = new TypeToken<EndpointPostAudiencesIDMemberships>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
