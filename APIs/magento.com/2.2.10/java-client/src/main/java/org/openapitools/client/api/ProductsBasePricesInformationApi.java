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


import org.openapitools.client.model.CatalogBasePriceStorageV1GetPostRequest;
import org.openapitools.client.model.CatalogDataBasePriceInterface;
import org.openapitools.client.model.ErrorResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductsBasePricesInformationApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductsBasePricesInformationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductsBasePricesInformationApi(ApiClient apiClient) {
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
     * Build call for catalogBasePriceStorageV1GetPost
     * @param catalogBasePriceStorageV1GetPostRequest  (optional)
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
    public okhttp3.Call catalogBasePriceStorageV1GetPostCall(CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = catalogBasePriceStorageV1GetPostRequest;

        // create path and map variables
        String localVarPath = "/V1/products/base-prices-information";

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
    private okhttp3.Call catalogBasePriceStorageV1GetPostValidateBeforeCall(CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest, final ApiCallback _callback) throws ApiException {
        return catalogBasePriceStorageV1GetPostCall(catalogBasePriceStorageV1GetPostRequest, _callback);

    }

    /**
     * products/base-prices-information
     * Return product prices. In case of at least one of skus is not found exception will be thrown.
     * @param catalogBasePriceStorageV1GetPostRequest  (optional)
     * @return List&lt;CatalogDataBasePriceInterface&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public List<CatalogDataBasePriceInterface> catalogBasePriceStorageV1GetPost(CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest) throws ApiException {
        ApiResponse<List<CatalogDataBasePriceInterface>> localVarResp = catalogBasePriceStorageV1GetPostWithHttpInfo(catalogBasePriceStorageV1GetPostRequest);
        return localVarResp.getData();
    }

    /**
     * products/base-prices-information
     * Return product prices. In case of at least one of skus is not found exception will be thrown.
     * @param catalogBasePriceStorageV1GetPostRequest  (optional)
     * @return ApiResponse&lt;List&lt;CatalogDataBasePriceInterface&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 Success. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> 401 Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<CatalogDataBasePriceInterface>> catalogBasePriceStorageV1GetPostWithHttpInfo(CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest) throws ApiException {
        okhttp3.Call localVarCall = catalogBasePriceStorageV1GetPostValidateBeforeCall(catalogBasePriceStorageV1GetPostRequest, null);
        Type localVarReturnType = new TypeToken<List<CatalogDataBasePriceInterface>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * products/base-prices-information (asynchronously)
     * Return product prices. In case of at least one of skus is not found exception will be thrown.
     * @param catalogBasePriceStorageV1GetPostRequest  (optional)
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
    public okhttp3.Call catalogBasePriceStorageV1GetPostAsync(CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest, final ApiCallback<List<CatalogDataBasePriceInterface>> _callback) throws ApiException {

        okhttp3.Call localVarCall = catalogBasePriceStorageV1GetPostValidateBeforeCall(catalogBasePriceStorageV1GetPostRequest, _callback);
        Type localVarReturnType = new TypeToken<List<CatalogDataBasePriceInterface>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
