/*
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
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
import org.openapitools.client.model.ShareProfileRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProfileApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProfileApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProfileApi(ApiClient apiClient) {
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
     * Build call for v05PatientsProfileSharePost
     * @param authorization Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param shareProfileRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * Invalid Request  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v05PatientsProfileSharePostCall(String authorization, String X_HIP_ID, ShareProfileRequest shareProfileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://your-hrp-server.com" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = shareProfileRequest;

        // create path and map variables
        String localVarPath = "/v0.5/patients/profile/share";

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
    private okhttp3.Call v05PatientsProfileSharePostValidateBeforeCall(String authorization, String X_HIP_ID, ShareProfileRequest shareProfileRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'authorization' is set
        if (authorization == null) {
            throw new ApiException("Missing the required parameter 'authorization' when calling v05PatientsProfileSharePost(Async)");
        }

        // verify the required parameter 'X_HIP_ID' is set
        if (X_HIP_ID == null) {
            throw new ApiException("Missing the required parameter 'X_HIP_ID' when calling v05PatientsProfileSharePost(Async)");
        }

        // verify the required parameter 'shareProfileRequest' is set
        if (shareProfileRequest == null) {
            throw new ApiException("Missing the required parameter 'shareProfileRequest' when calling v05PatientsProfileSharePost(Async)");
        }

        return v05PatientsProfileSharePostCall(authorization, X_HIP_ID, shareProfileRequest, _callback);

    }

    /**
     * Share patient profile details
     * Request for sharing patient&#39;s profile details to HIP 
     * @param authorization Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param shareProfileRequest  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * Invalid Request  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public void v05PatientsProfileSharePost(String authorization, String X_HIP_ID, ShareProfileRequest shareProfileRequest) throws ApiException {
        v05PatientsProfileSharePostWithHttpInfo(authorization, X_HIP_ID, shareProfileRequest);
    }

    /**
     * Share patient profile details
     * Request for sharing patient&#39;s profile details to HIP 
     * @param authorization Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param shareProfileRequest  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * Invalid Request  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> v05PatientsProfileSharePostWithHttpInfo(String authorization, String X_HIP_ID, ShareProfileRequest shareProfileRequest) throws ApiException {
        okhttp3.Call localVarCall = v05PatientsProfileSharePostValidateBeforeCall(authorization, X_HIP_ID, shareProfileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Share patient profile details (asynchronously)
     * Request for sharing patient&#39;s profile details to HIP 
     * @param authorization Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. (required)
     * @param X_HIP_ID Identifier of the health information provider to which the request was intended. (required)
     * @param shareProfileRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Request accepted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Causes:**   * Invalid Request  </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Causes:**   * Unauthorized request  </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v05PatientsProfileSharePostAsync(String authorization, String X_HIP_ID, ShareProfileRequest shareProfileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = v05PatientsProfileSharePostValidateBeforeCall(authorization, X_HIP_ID, shareProfileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
