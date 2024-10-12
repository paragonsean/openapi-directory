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
import org.openapitools.client.model.NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NegotiableQuoteSubmitToCustomerApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public NegotiableQuoteSubmitToCustomerApi() {
        this(Configuration.getDefaultApiClient());
    }

    public NegotiableQuoteSubmitToCustomerApi(ApiClient apiClient) {
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
     * Build call for negotiableQuoteNegotiableQuoteManagementV1AdminSendPost
     * @param negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest  (optional)
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
    public okhttp3.Call negotiableQuoteNegotiableQuoteManagementV1AdminSendPostCall(NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest;

        // create path and map variables
        String localVarPath = "/V1/negotiableQuote/submitToCustomer";

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
    private okhttp3.Call negotiableQuoteNegotiableQuoteManagementV1AdminSendPostValidateBeforeCall(NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest, final ApiCallback _callback) throws ApiException {
        return negotiableQuoteNegotiableQuoteManagementV1AdminSendPostCall(negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest, _callback);

    }

    /**
     * negotiableQuote/submitToCustomer
     * Submit the B2B quote to the customer. The quote status for the customer will be changed to &#39;Updated&#39;, and the customer can work with the quote.
     * @param negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest  (optional)
     * @return Boolean
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public Boolean negotiableQuoteNegotiableQuoteManagementV1AdminSendPost(NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest) throws ApiException {
        ApiResponse<Boolean> localVarResp = negotiableQuoteNegotiableQuoteManagementV1AdminSendPostWithHttpInfo(negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest);
        return localVarResp.getData();
    }

    /**
     * negotiableQuote/submitToCustomer
     * Submit the B2B quote to the customer. The quote status for the customer will be changed to &#39;Updated&#39;, and the customer can work with the quote.
     * @param negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest  (optional)
     * @return ApiResponse&lt;Boolean&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Boolean> negotiableQuoteNegotiableQuoteManagementV1AdminSendPostWithHttpInfo(NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest) throws ApiException {
        okhttp3.Call localVarCall = negotiableQuoteNegotiableQuoteManagementV1AdminSendPostValidateBeforeCall(negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest, null);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * negotiableQuote/submitToCustomer (asynchronously)
     * Submit the B2B quote to the customer. The quote status for the customer will be changed to &#39;Updated&#39;, and the customer can work with the quote.
     * @param negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest  (optional)
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
    public okhttp3.Call negotiableQuoteNegotiableQuoteManagementV1AdminSendPostAsync(NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest, final ApiCallback<Boolean> _callback) throws ApiException {

        okhttp3.Call localVarCall = negotiableQuoteNegotiableQuoteManagementV1AdminSendPostValidateBeforeCall(negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest, _callback);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
