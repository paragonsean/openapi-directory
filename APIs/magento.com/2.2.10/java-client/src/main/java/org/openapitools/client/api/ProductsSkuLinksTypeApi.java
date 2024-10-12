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


import org.openapitools.client.model.CatalogDataProductLinkInterface;
import org.openapitools.client.model.ErrorResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductsSkuLinksTypeApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductsSkuLinksTypeApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductsSkuLinksTypeApi(ApiClient apiClient) {
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
     * Build call for catalogProductLinkManagementV1GetLinkedItemsByTypeGet
     * @param sku  (required)
     * @param type  (required)
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
    public okhttp3.Call catalogProductLinkManagementV1GetLinkedItemsByTypeGetCall(String sku, String type, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/V1/products/{sku}/links/{type}"
            .replace("{" + "sku" + "}", localVarApiClient.escapeString(sku.toString()))
            .replace("{" + "type" + "}", localVarApiClient.escapeString(type.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call catalogProductLinkManagementV1GetLinkedItemsByTypeGetValidateBeforeCall(String sku, String type, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'sku' is set
        if (sku == null) {
            throw new ApiException("Missing the required parameter 'sku' when calling catalogProductLinkManagementV1GetLinkedItemsByTypeGet(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling catalogProductLinkManagementV1GetLinkedItemsByTypeGet(Async)");
        }

        return catalogProductLinkManagementV1GetLinkedItemsByTypeGetCall(sku, type, _callback);

    }

    /**
     * products/{sku}/links/{type}
     * Provide the list of links for a specific product
     * @param sku  (required)
     * @param type  (required)
     * @return List&lt;CatalogDataProductLinkInterface&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public List<CatalogDataProductLinkInterface> catalogProductLinkManagementV1GetLinkedItemsByTypeGet(String sku, String type) throws ApiException {
        ApiResponse<List<CatalogDataProductLinkInterface>> localVarResp = catalogProductLinkManagementV1GetLinkedItemsByTypeGetWithHttpInfo(sku, type);
        return localVarResp.getData();
    }

    /**
     * products/{sku}/links/{type}
     * Provide the list of links for a specific product
     * @param sku  (required)
     * @param type  (required)
     * @return ApiResponse&lt;List&lt;CatalogDataProductLinkInterface&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<CatalogDataProductLinkInterface>> catalogProductLinkManagementV1GetLinkedItemsByTypeGetWithHttpInfo(String sku, String type) throws ApiException {
        okhttp3.Call localVarCall = catalogProductLinkManagementV1GetLinkedItemsByTypeGetValidateBeforeCall(sku, type, null);
        Type localVarReturnType = new TypeToken<List<CatalogDataProductLinkInterface>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * products/{sku}/links/{type} (asynchronously)
     * Provide the list of links for a specific product
     * @param sku  (required)
     * @param type  (required)
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
    public okhttp3.Call catalogProductLinkManagementV1GetLinkedItemsByTypeGetAsync(String sku, String type, final ApiCallback<List<CatalogDataProductLinkInterface>> _callback) throws ApiException {

        okhttp3.Call localVarCall = catalogProductLinkManagementV1GetLinkedItemsByTypeGetValidateBeforeCall(sku, type, _callback);
        Type localVarReturnType = new TypeToken<List<CatalogDataProductLinkInterface>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
