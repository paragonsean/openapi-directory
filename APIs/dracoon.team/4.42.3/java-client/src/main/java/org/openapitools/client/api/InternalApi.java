/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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


import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.SubscriptionPlanRequest;
import org.openapitools.client.model.SubscriptionPlanResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InternalApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public InternalApi() {
        this(Configuration.getDefaultApiClient());
    }

    public InternalApi(ApiClient apiClient) {
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
     * Build call for internalRequestSubscriptionPlan
     * @param xSdsServiceToken Service Authentication token (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call internalRequestSubscriptionPlanCall(String xSdsServiceToken, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/internal/tenant/subscription_plan";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xSdsServiceToken != null) {
            localVarHeaderParams.put("X-Sds-Service-Token", localVarApiClient.parameterToString(xSdsServiceToken));
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
    private okhttp3.Call internalRequestSubscriptionPlanValidateBeforeCall(String xSdsServiceToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xSdsServiceToken' is set
        if (xSdsServiceToken == null) {
            throw new ApiException("Missing the required parameter 'xSdsServiceToken' when calling internalRequestSubscriptionPlan(Async)");
        }

        return internalRequestSubscriptionPlanCall(xSdsServiceToken, _callback);

    }

    /**
     * Request subscription plan
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Get the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param xSdsServiceToken Service Authentication token (required)
     * @return SubscriptionPlanResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionPlanResponse internalRequestSubscriptionPlan(String xSdsServiceToken) throws ApiException {
        ApiResponse<SubscriptionPlanResponse> localVarResp = internalRequestSubscriptionPlanWithHttpInfo(xSdsServiceToken);
        return localVarResp.getData();
    }

    /**
     * Request subscription plan
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Get the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param xSdsServiceToken Service Authentication token (required)
     * @return ApiResponse&lt;SubscriptionPlanResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionPlanResponse> internalRequestSubscriptionPlanWithHttpInfo(String xSdsServiceToken) throws ApiException {
        okhttp3.Call localVarCall = internalRequestSubscriptionPlanValidateBeforeCall(xSdsServiceToken, null);
        Type localVarReturnType = new TypeToken<SubscriptionPlanResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Request subscription plan (asynchronously)
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Get the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param xSdsServiceToken Service Authentication token (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call internalRequestSubscriptionPlanAsync(String xSdsServiceToken, final ApiCallback<SubscriptionPlanResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = internalRequestSubscriptionPlanValidateBeforeCall(xSdsServiceToken, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionPlanResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for internalSetSubscriptionPlan
     * @param xSdsServiceToken Service Authentication token (required)
     * @param subscriptionPlanRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call internalSetSubscriptionPlanCall(String xSdsServiceToken, SubscriptionPlanRequest subscriptionPlanRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscriptionPlanRequest;

        // create path and map variables
        String localVarPath = "/v4/internal/tenant/subscription_plan";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xSdsServiceToken != null) {
            localVarHeaderParams.put("X-Sds-Service-Token", localVarApiClient.parameterToString(xSdsServiceToken));
        }

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call internalSetSubscriptionPlanValidateBeforeCall(String xSdsServiceToken, SubscriptionPlanRequest subscriptionPlanRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xSdsServiceToken' is set
        if (xSdsServiceToken == null) {
            throw new ApiException("Missing the required parameter 'xSdsServiceToken' when calling internalSetSubscriptionPlan(Async)");
        }

        // verify the required parameter 'subscriptionPlanRequest' is set
        if (subscriptionPlanRequest == null) {
            throw new ApiException("Missing the required parameter 'subscriptionPlanRequest' when calling internalSetSubscriptionPlan(Async)");
        }

        return internalSetSubscriptionPlanCall(xSdsServiceToken, subscriptionPlanRequest, _callback);

    }

    /**
     * Set subscription plan
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description:  Change the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: The subscription plan of the current tenant is set to the given value.   Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param xSdsServiceToken Service Authentication token (required)
     * @param subscriptionPlanRequest  (required)
     * @return SubscriptionPlanResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionPlanResponse internalSetSubscriptionPlan(String xSdsServiceToken, SubscriptionPlanRequest subscriptionPlanRequest) throws ApiException {
        ApiResponse<SubscriptionPlanResponse> localVarResp = internalSetSubscriptionPlanWithHttpInfo(xSdsServiceToken, subscriptionPlanRequest);
        return localVarResp.getData();
    }

    /**
     * Set subscription plan
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description:  Change the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: The subscription plan of the current tenant is set to the given value.   Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param xSdsServiceToken Service Authentication token (required)
     * @param subscriptionPlanRequest  (required)
     * @return ApiResponse&lt;SubscriptionPlanResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionPlanResponse> internalSetSubscriptionPlanWithHttpInfo(String xSdsServiceToken, SubscriptionPlanRequest subscriptionPlanRequest) throws ApiException {
        okhttp3.Call localVarCall = internalSetSubscriptionPlanValidateBeforeCall(xSdsServiceToken, subscriptionPlanRequest, null);
        Type localVarReturnType = new TypeToken<SubscriptionPlanResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Set subscription plan (asynchronously)
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description:  Change the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: The subscription plan of the current tenant is set to the given value.   Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 
     * @param xSdsServiceToken Service Authentication token (required)
     * @param subscriptionPlanRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call internalSetSubscriptionPlanAsync(String xSdsServiceToken, SubscriptionPlanRequest subscriptionPlanRequest, final ApiCallback<SubscriptionPlanResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = internalSetSubscriptionPlanValidateBeforeCall(xSdsServiceToken, subscriptionPlanRequest, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionPlanResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
