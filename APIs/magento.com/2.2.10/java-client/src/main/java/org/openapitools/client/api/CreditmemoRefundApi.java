/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
import org.openapitools.client.model.SalesCreditmemoManagementV1RefundPostRequest;
import org.openapitools.client.model.SalesDataCreditmemoInterface;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CreditmemoRefundApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CreditmemoRefundApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CreditmemoRefundApi(ApiClient apiClient) {
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
     * Build call for salesCreditmemoManagementV1RefundPost
     * @param salesCreditmemoManagementV1RefundPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditmemoManagementV1RefundPostCall(SalesCreditmemoManagementV1RefundPostRequest salesCreditmemoManagementV1RefundPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = salesCreditmemoManagementV1RefundPostRequest;

        // create path and map variables
        String localVarPath = "/V1/creditmemo/refund";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call salesCreditmemoManagementV1RefundPostValidateBeforeCall(SalesCreditmemoManagementV1RefundPostRequest salesCreditmemoManagementV1RefundPostRequest, final ApiCallback _callback) throws ApiException {
        return salesCreditmemoManagementV1RefundPostCall(salesCreditmemoManagementV1RefundPostRequest, _callback);

    }

    /**
     * creditmemo/refund
     * Prepare creditmemo to refund and save it.
     * @param salesCreditmemoManagementV1RefundPostRequest  (optional)
     * @return SalesDataCreditmemoInterface
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public SalesDataCreditmemoInterface salesCreditmemoManagementV1RefundPost(SalesCreditmemoManagementV1RefundPostRequest salesCreditmemoManagementV1RefundPostRequest) throws ApiException {
        ApiResponse<SalesDataCreditmemoInterface> localVarResp = salesCreditmemoManagementV1RefundPostWithHttpInfo(salesCreditmemoManagementV1RefundPostRequest);
        return localVarResp.getData();
    }

    /**
     * creditmemo/refund
     * Prepare creditmemo to refund and save it.
     * @param salesCreditmemoManagementV1RefundPostRequest  (optional)
     * @return ApiResponse&lt;SalesDataCreditmemoInterface&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SalesDataCreditmemoInterface> salesCreditmemoManagementV1RefundPostWithHttpInfo(SalesCreditmemoManagementV1RefundPostRequest salesCreditmemoManagementV1RefundPostRequest) throws ApiException {
        okhttp3.Call localVarCall = salesCreditmemoManagementV1RefundPostValidateBeforeCall(salesCreditmemoManagementV1RefundPostRequest, null);
        Type localVarReturnType = new TypeToken<SalesDataCreditmemoInterface>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * creditmemo/refund (asynchronously)
     * Prepare creditmemo to refund and save it.
     * @param salesCreditmemoManagementV1RefundPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditmemoManagementV1RefundPostAsync(SalesCreditmemoManagementV1RefundPostRequest salesCreditmemoManagementV1RefundPostRequest, final ApiCallback<SalesDataCreditmemoInterface> _callback) throws ApiException {

        okhttp3.Call localVarCall = salesCreditmemoManagementV1RefundPostValidateBeforeCall(salesCreditmemoManagementV1RefundPostRequest, _callback);
        Type localVarReturnType = new TypeToken<SalesDataCreditmemoInterface>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
