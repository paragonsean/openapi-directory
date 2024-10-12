/*
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
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
import org.openapitools.client.model.PatientSMSNotifcationRequest;
import org.openapitools.client.model.PatientSMSNotifcationResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PatientNotificationApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PatientNotificationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PatientNotificationApi(ApiClient apiClient) {
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
     * Build call for v05PatientsSmsNotifyPost_0
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_CM_ID Suffix of the consent manager to which the request was intended. (required)
     * @param patientSMSNotifcationRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * required information not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v05PatientsSmsNotifyPost_0Call(String authorization, String X_CM_ID, PatientSMSNotifcationRequest patientSMSNotifcationRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = patientSMSNotifcationRequest;

        // create path and map variables
        String localVarPath = "/v0.5/patients/sms/notify";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (authorization != null) {
            localVarHeaderParams.put("Authorization", localVarApiClient.parameterToString(authorization));
        }

        if (X_CM_ID != null) {
            localVarHeaderParams.put("X-CM-ID", localVarApiClient.parameterToString(X_CM_ID));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v05PatientsSmsNotifyPost_0ValidateBeforeCall(String authorization, String X_CM_ID, PatientSMSNotifcationRequest patientSMSNotifcationRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'authorization' is set
        if (authorization == null) {
            throw new ApiException("Missing the required parameter 'authorization' when calling v05PatientsSmsNotifyPost_0(Async)");
        }

        // verify the required parameter 'X_CM_ID' is set
        if (X_CM_ID == null) {
            throw new ApiException("Missing the required parameter 'X_CM_ID' when calling v05PatientsSmsNotifyPost_0(Async)");
        }

        // verify the required parameter 'patientSMSNotifcationRequest' is set
        if (patientSMSNotifcationRequest == null) {
            throw new ApiException("Missing the required parameter 'patientSMSNotifcationRequest' when calling v05PatientsSmsNotifyPost_0(Async)");
        }

        return v05PatientsSmsNotifyPost_0Call(authorization, X_CM_ID, patientSMSNotifcationRequest, _callback);

    }

    /**
     * API for HIP to send SMS notifications to patients
     * API to send SMS notifications to patient with custom deeplink. 
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_CM_ID Suffix of the consent manager to which the request was intended. (required)
     * @param patientSMSNotifcationRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * required information not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public void v05PatientsSmsNotifyPost_0(String authorization, String X_CM_ID, PatientSMSNotifcationRequest patientSMSNotifcationRequest) throws ApiException {
        v05PatientsSmsNotifyPost_0WithHttpInfo(authorization, X_CM_ID, patientSMSNotifcationRequest);
    }

    /**
     * API for HIP to send SMS notifications to patients
     * API to send SMS notifications to patient with custom deeplink. 
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_CM_ID Suffix of the consent manager to which the request was intended. (required)
     * @param patientSMSNotifcationRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * required information not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> v05PatientsSmsNotifyPost_0WithHttpInfo(String authorization, String X_CM_ID, PatientSMSNotifcationRequest patientSMSNotifcationRequest) throws ApiException {
        okhttp3.Call localVarCall = v05PatientsSmsNotifyPost_0ValidateBeforeCall(authorization, X_CM_ID, patientSMSNotifcationRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * API for HIP to send SMS notifications to patients (asynchronously)
     * API to send SMS notifications to patient with custom deeplink. 
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_CM_ID Suffix of the consent manager to which the request was intended. (required)
     * @param patientSMSNotifcationRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * required information not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v05PatientsSmsNotifyPost_0Async(String authorization, String X_CM_ID, PatientSMSNotifcationRequest patientSMSNotifcationRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = v05PatientsSmsNotifyPost_0ValidateBeforeCall(authorization, X_CM_ID, patientSMSNotifcationRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for v05PatientsSmsOnNotifyPost_0
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param patientSMSNotifcationResponse  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request Accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request, required attributes not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v05PatientsSmsOnNotifyPost_0Call(String authorization, String X_HIP_ID, PatientSMSNotifcationResponse patientSMSNotifcationResponse, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = patientSMSNotifcationResponse;

        // create path and map variables
        String localVarPath = "/v0.5/patients/sms/on-notify";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (authorization != null) {
            localVarHeaderParams.put("Authorization", localVarApiClient.parameterToString(authorization));
        }

        if (X_HIP_ID != null) {
            localVarHeaderParams.put("X-HIP-ID", localVarApiClient.parameterToString(X_HIP_ID));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v05PatientsSmsOnNotifyPost_0ValidateBeforeCall(String authorization, String X_HIP_ID, PatientSMSNotifcationResponse patientSMSNotifcationResponse, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'authorization' is set
        if (authorization == null) {
            throw new ApiException("Missing the required parameter 'authorization' when calling v05PatientsSmsOnNotifyPost_0(Async)");
        }

        // verify the required parameter 'X_HIP_ID' is set
        if (X_HIP_ID == null) {
            throw new ApiException("Missing the required parameter 'X_HIP_ID' when calling v05PatientsSmsOnNotifyPost_0(Async)");
        }

        // verify the required parameter 'patientSMSNotifcationResponse' is set
        if (patientSMSNotifcationResponse == null) {
            throw new ApiException("Missing the required parameter 'patientSMSNotifcationResponse' when calling v05PatientsSmsOnNotifyPost_0(Async)");
        }

        return v05PatientsSmsOnNotifyPost_0Call(authorization, X_HIP_ID, patientSMSNotifcationResponse, _callback);

    }

    /**
     * Acknowledgment response for SMS notification sent to patient by HIP
     * If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param patientSMSNotifcationResponse  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request Accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request, required attributes not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public void v05PatientsSmsOnNotifyPost_0(String authorization, String X_HIP_ID, PatientSMSNotifcationResponse patientSMSNotifcationResponse) throws ApiException {
        v05PatientsSmsOnNotifyPost_0WithHttpInfo(authorization, X_HIP_ID, patientSMSNotifcationResponse);
    }

    /**
     * Acknowledgment response for SMS notification sent to patient by HIP
     * If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param patientSMSNotifcationResponse  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request Accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request, required attributes not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> v05PatientsSmsOnNotifyPost_0WithHttpInfo(String authorization, String X_HIP_ID, PatientSMSNotifcationResponse patientSMSNotifcationResponse) throws ApiException {
        okhttp3.Call localVarCall = v05PatientsSmsOnNotifyPost_0ValidateBeforeCall(authorization, X_HIP_ID, patientSMSNotifcationResponse, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Acknowledgment response for SMS notification sent to patient by HIP (asynchronously)
     * If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 
     * @param authorization Access token which was issued after successful login with gateway auth server. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param patientSMSNotifcationResponse  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request Accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Invalid request, required attributes not provided  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v05PatientsSmsOnNotifyPost_0Async(String authorization, String X_HIP_ID, PatientSMSNotifcationResponse patientSMSNotifcationResponse, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = v05PatientsSmsOnNotifyPost_0ValidateBeforeCall(authorization, X_HIP_ID, patientSMSNotifcationResponse, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
