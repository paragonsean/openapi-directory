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


import org.openapitools.client.model.EndpointDeleteWebhooksID;
import org.openapitools.client.model.EndpointGetWebhooks;
import org.openapitools.client.model.EndpointPostWebhooks;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class WebhooksApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public WebhooksApi() {
        this(Configuration.getDefaultApiClient());
    }

    public WebhooksApi(ApiClient apiClient) {
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
     * Build call for webhooksGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/webhooks";

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
    private okhttp3.Call webhooksGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return webhooksGetCall(_callback);

    }

    /**
     * 
     * Fetch a listing of all webhooks owned by the current user/bubble combination.
     * @return EndpointGetWebhooks
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointGetWebhooks webhooksGet() throws ApiException {
        ApiResponse<EndpointGetWebhooks> localVarResp = webhooksGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * 
     * Fetch a listing of all webhooks owned by the current user/bubble combination.
     * @return ApiResponse&lt;EndpointGetWebhooks&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointGetWebhooks> webhooksGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = webhooksGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<EndpointGetWebhooks>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Fetch a listing of all webhooks owned by the current user/bubble combination.
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksGetAsync(final ApiCallback<EndpointGetWebhooks> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<EndpointGetWebhooks>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for webhooksIDDelete
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
    public okhttp3.Call webhooksIDDeleteCall(Integer ID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/webhooks/{ID}"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call webhooksIDDeleteValidateBeforeCall(Integer ID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling webhooksIDDelete(Async)");
        }

        return webhooksIDDeleteCall(ID, _callback);

    }

    /**
     * 
     * Delete a webhook that was previously registered by the current user/bubble combination.
     * @param ID  (required)
     * @return EndpointDeleteWebhooksID
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointDeleteWebhooksID webhooksIDDelete(Integer ID) throws ApiException {
        ApiResponse<EndpointDeleteWebhooksID> localVarResp = webhooksIDDeleteWithHttpInfo(ID);
        return localVarResp.getData();
    }

    /**
     * 
     * Delete a webhook that was previously registered by the current user/bubble combination.
     * @param ID  (required)
     * @return ApiResponse&lt;EndpointDeleteWebhooksID&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointDeleteWebhooksID> webhooksIDDeleteWithHttpInfo(Integer ID) throws ApiException {
        okhttp3.Call localVarCall = webhooksIDDeleteValidateBeforeCall(ID, null);
        Type localVarReturnType = new TypeToken<EndpointDeleteWebhooksID>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Delete a webhook that was previously registered by the current user/bubble combination.
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
    public okhttp3.Call webhooksIDDeleteAsync(Integer ID, final ApiCallback<EndpointDeleteWebhooksID> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksIDDeleteValidateBeforeCall(ID, _callback);
        Type localVarReturnType = new TypeToken<EndpointDeleteWebhooksID>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for webhooksPost
     * @param event  (required)
     * @param name  (required)
     * @param uri  (required)
     * @param bubbled  (optional, default to false)
     * @param objectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksPostCall(String event, String name, String uri, Boolean bubbled, Integer objectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/webhooks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (bubbled != null) {
            localVarFormParams.put("bubbled", bubbled);
        }

        if (event != null) {
            localVarFormParams.put("event", event);
        }

        if (name != null) {
            localVarFormParams.put("name", name);
        }

        if (objectId != null) {
            localVarFormParams.put("object_id", objectId);
        }

        if (uri != null) {
            localVarFormParams.put("uri", uri);
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "implicit_flow", "explicit_flow" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call webhooksPostValidateBeforeCall(String event, String name, String uri, Boolean bubbled, Integer objectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'event' is set
        if (event == null) {
            throw new ApiException("Missing the required parameter 'event' when calling webhooksPost(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling webhooksPost(Async)");
        }

        // verify the required parameter 'uri' is set
        if (uri == null) {
            throw new ApiException("Missing the required parameter 'uri' when calling webhooksPost(Async)");
        }

        return webhooksPostCall(event, name, uri, bubbled, objectId, _callback);

    }

    /**
     * 
     * Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you&#39;re in, groups you&#39;re a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.
     * @param event  (required)
     * @param name  (required)
     * @param uri  (required)
     * @param bubbled  (optional, default to false)
     * @param objectId  (optional)
     * @return EndpointPostWebhooks
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointPostWebhooks webhooksPost(String event, String name, String uri, Boolean bubbled, Integer objectId) throws ApiException {
        ApiResponse<EndpointPostWebhooks> localVarResp = webhooksPostWithHttpInfo(event, name, uri, bubbled, objectId);
        return localVarResp.getData();
    }

    /**
     * 
     * Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you&#39;re in, groups you&#39;re a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.
     * @param event  (required)
     * @param name  (required)
     * @param uri  (required)
     * @param bubbled  (optional, default to false)
     * @param objectId  (optional)
     * @return ApiResponse&lt;EndpointPostWebhooks&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointPostWebhooks> webhooksPostWithHttpInfo(String event, String name, String uri, Boolean bubbled, Integer objectId) throws ApiException {
        okhttp3.Call localVarCall = webhooksPostValidateBeforeCall(event, name, uri, bubbled, objectId, null);
        Type localVarReturnType = new TypeToken<EndpointPostWebhooks>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you&#39;re in, groups you&#39;re a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.
     * @param event  (required)
     * @param name  (required)
     * @param uri  (required)
     * @param bubbled  (optional, default to false)
     * @param objectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksPostAsync(String event, String name, String uri, Boolean bubbled, Integer objectId, final ApiCallback<EndpointPostWebhooks> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksPostValidateBeforeCall(event, name, uri, bubbled, objectId, _callback);
        Type localVarReturnType = new TypeToken<EndpointPostWebhooks>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
