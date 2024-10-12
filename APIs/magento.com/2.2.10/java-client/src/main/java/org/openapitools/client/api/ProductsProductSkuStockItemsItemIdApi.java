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


import org.openapitools.client.model.CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest;
import org.openapitools.client.model.ErrorResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductsProductSkuStockItemsItemIdApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductsProductSkuStockItemsItemIdApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductsProductSkuStockItemsItemIdApi(ApiClient apiClient) {
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
     * Build call for catalogInventoryStockRegistryV1UpdateStockItemBySkuPut
     * @param productSku  (required)
     * @param itemId  (required)
     * @param catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> 400 Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call catalogInventoryStockRegistryV1UpdateStockItemBySkuPutCall(String productSku, String itemId, CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest;

        // create path and map variables
        String localVarPath = "/V1/products/{productSku}/stockItems/{itemId}"
            .replace("{" + "productSku" + "}", localVarApiClient.escapeString(productSku.toString()))
            .replace("{" + "itemId" + "}", localVarApiClient.escapeString(itemId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call catalogInventoryStockRegistryV1UpdateStockItemBySkuPutValidateBeforeCall(String productSku, String itemId, CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productSku' is set
        if (productSku == null) {
            throw new ApiException("Missing the required parameter 'productSku' when calling catalogInventoryStockRegistryV1UpdateStockItemBySkuPut(Async)");
        }

        // verify the required parameter 'itemId' is set
        if (itemId == null) {
            throw new ApiException("Missing the required parameter 'itemId' when calling catalogInventoryStockRegistryV1UpdateStockItemBySkuPut(Async)");
        }

        return catalogInventoryStockRegistryV1UpdateStockItemBySkuPutCall(productSku, itemId, catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest, _callback);

    }

    /**
     * products/{productSku}/stockItems/{itemId}
     * 
     * @param productSku  (required)
     * @param itemId  (required)
     * @param catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest  (optional)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> 400 Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public Integer catalogInventoryStockRegistryV1UpdateStockItemBySkuPut(String productSku, String itemId, CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest) throws ApiException {
        ApiResponse<Integer> localVarResp = catalogInventoryStockRegistryV1UpdateStockItemBySkuPutWithHttpInfo(productSku, itemId, catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest);
        return localVarResp.getData();
    }

    /**
     * products/{productSku}/stockItems/{itemId}
     * 
     * @param productSku  (required)
     * @param itemId  (required)
     * @param catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest  (optional)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> 400 Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> catalogInventoryStockRegistryV1UpdateStockItemBySkuPutWithHttpInfo(String productSku, String itemId, CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest) throws ApiException {
        okhttp3.Call localVarCall = catalogInventoryStockRegistryV1UpdateStockItemBySkuPutValidateBeforeCall(productSku, itemId, catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * products/{productSku}/stockItems/{itemId} (asynchronously)
     * 
     * @param productSku  (required)
     * @param itemId  (required)
     * @param catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> 400 Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call catalogInventoryStockRegistryV1UpdateStockItemBySkuPutAsync(String productSku, String itemId, CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = catalogInventoryStockRegistryV1UpdateStockItemBySkuPutValidateBeforeCall(productSku, itemId, catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
