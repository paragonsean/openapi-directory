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


import org.openapitools.client.model.CatalogDataProductAttributeMediaGalleryEntryInterface;
import org.openapitools.client.model.CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest;
import org.openapitools.client.model.ErrorResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductsSkuMediaEntryIdApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductsSkuMediaEntryIdApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductsSkuMediaEntryIdApi(ApiClient apiClient) {
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
     * Build call for catalogProductAttributeMediaGalleryManagementV1GetGet
     * @param sku  (required)
     * @param entryId  (required)
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
    public okhttp3.Call catalogProductAttributeMediaGalleryManagementV1GetGetCall(String sku, Integer entryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/V1/products/{sku}/media/{entryId}"
            .replace("{" + "sku" + "}", localVarApiClient.escapeString(sku.toString()))
            .replace("{" + "entryId" + "}", localVarApiClient.escapeString(entryId.toString()));

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
    private okhttp3.Call catalogProductAttributeMediaGalleryManagementV1GetGetValidateBeforeCall(String sku, Integer entryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'sku' is set
        if (sku == null) {
            throw new ApiException("Missing the required parameter 'sku' when calling catalogProductAttributeMediaGalleryManagementV1GetGet(Async)");
        }

        // verify the required parameter 'entryId' is set
        if (entryId == null) {
            throw new ApiException("Missing the required parameter 'entryId' when calling catalogProductAttributeMediaGalleryManagementV1GetGet(Async)");
        }

        return catalogProductAttributeMediaGalleryManagementV1GetGetCall(sku, entryId, _callback);

    }

    /**
     * products/{sku}/media/{entryId}
     * Return information about gallery entry
     * @param sku  (required)
     * @param entryId  (required)
     * @return CatalogDataProductAttributeMediaGalleryEntryInterface
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
    public CatalogDataProductAttributeMediaGalleryEntryInterface catalogProductAttributeMediaGalleryManagementV1GetGet(String sku, Integer entryId) throws ApiException {
        ApiResponse<CatalogDataProductAttributeMediaGalleryEntryInterface> localVarResp = catalogProductAttributeMediaGalleryManagementV1GetGetWithHttpInfo(sku, entryId);
        return localVarResp.getData();
    }

    /**
     * products/{sku}/media/{entryId}
     * Return information about gallery entry
     * @param sku  (required)
     * @param entryId  (required)
     * @return ApiResponse&lt;CatalogDataProductAttributeMediaGalleryEntryInterface&gt;
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
    public ApiResponse<CatalogDataProductAttributeMediaGalleryEntryInterface> catalogProductAttributeMediaGalleryManagementV1GetGetWithHttpInfo(String sku, Integer entryId) throws ApiException {
        okhttp3.Call localVarCall = catalogProductAttributeMediaGalleryManagementV1GetGetValidateBeforeCall(sku, entryId, null);
        Type localVarReturnType = new TypeToken<CatalogDataProductAttributeMediaGalleryEntryInterface>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * products/{sku}/media/{entryId} (asynchronously)
     * Return information about gallery entry
     * @param sku  (required)
     * @param entryId  (required)
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
    public okhttp3.Call catalogProductAttributeMediaGalleryManagementV1GetGetAsync(String sku, Integer entryId, final ApiCallback<CatalogDataProductAttributeMediaGalleryEntryInterface> _callback) throws ApiException {

        okhttp3.Call localVarCall = catalogProductAttributeMediaGalleryManagementV1GetGetValidateBeforeCall(sku, entryId, _callback);
        Type localVarReturnType = new TypeToken<CatalogDataProductAttributeMediaGalleryEntryInterface>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for catalogProductAttributeMediaGalleryManagementV1RemoveDelete
     * @param sku  (required)
     * @param entryId  (required)
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
    public okhttp3.Call catalogProductAttributeMediaGalleryManagementV1RemoveDeleteCall(String sku, Integer entryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/V1/products/{sku}/media/{entryId}"
            .replace("{" + "sku" + "}", localVarApiClient.escapeString(sku.toString()))
            .replace("{" + "entryId" + "}", localVarApiClient.escapeString(entryId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call catalogProductAttributeMediaGalleryManagementV1RemoveDeleteValidateBeforeCall(String sku, Integer entryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'sku' is set
        if (sku == null) {
            throw new ApiException("Missing the required parameter 'sku' when calling catalogProductAttributeMediaGalleryManagementV1RemoveDelete(Async)");
        }

        // verify the required parameter 'entryId' is set
        if (entryId == null) {
            throw new ApiException("Missing the required parameter 'entryId' when calling catalogProductAttributeMediaGalleryManagementV1RemoveDelete(Async)");
        }

        return catalogProductAttributeMediaGalleryManagementV1RemoveDeleteCall(sku, entryId, _callback);

    }

    /**
     * products/{sku}/media/{entryId}
     * Remove gallery entry
     * @param sku  (required)
     * @param entryId  (required)
     * @return Boolean
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
    public Boolean catalogProductAttributeMediaGalleryManagementV1RemoveDelete(String sku, Integer entryId) throws ApiException {
        ApiResponse<Boolean> localVarResp = catalogProductAttributeMediaGalleryManagementV1RemoveDeleteWithHttpInfo(sku, entryId);
        return localVarResp.getData();
    }

    /**
     * products/{sku}/media/{entryId}
     * Remove gallery entry
     * @param sku  (required)
     * @param entryId  (required)
     * @return ApiResponse&lt;Boolean&gt;
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
    public ApiResponse<Boolean> catalogProductAttributeMediaGalleryManagementV1RemoveDeleteWithHttpInfo(String sku, Integer entryId) throws ApiException {
        okhttp3.Call localVarCall = catalogProductAttributeMediaGalleryManagementV1RemoveDeleteValidateBeforeCall(sku, entryId, null);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * products/{sku}/media/{entryId} (asynchronously)
     * Remove gallery entry
     * @param sku  (required)
     * @param entryId  (required)
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
    public okhttp3.Call catalogProductAttributeMediaGalleryManagementV1RemoveDeleteAsync(String sku, Integer entryId, final ApiCallback<Boolean> _callback) throws ApiException {

        okhttp3.Call localVarCall = catalogProductAttributeMediaGalleryManagementV1RemoveDeleteValidateBeforeCall(sku, entryId, _callback);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for catalogProductAttributeMediaGalleryManagementV1UpdatePut
     * @param sku  (required)
     * @param entryId  (required)
     * @param catalogProductAttributeMediaGalleryManagementV1CreatePostRequest  (optional)
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
    public okhttp3.Call catalogProductAttributeMediaGalleryManagementV1UpdatePutCall(String sku, String entryId, CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest catalogProductAttributeMediaGalleryManagementV1CreatePostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = catalogProductAttributeMediaGalleryManagementV1CreatePostRequest;

        // create path and map variables
        String localVarPath = "/V1/products/{sku}/media/{entryId}"
            .replace("{" + "sku" + "}", localVarApiClient.escapeString(sku.toString()))
            .replace("{" + "entryId" + "}", localVarApiClient.escapeString(entryId.toString()));

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
    private okhttp3.Call catalogProductAttributeMediaGalleryManagementV1UpdatePutValidateBeforeCall(String sku, String entryId, CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest catalogProductAttributeMediaGalleryManagementV1CreatePostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'sku' is set
        if (sku == null) {
            throw new ApiException("Missing the required parameter 'sku' when calling catalogProductAttributeMediaGalleryManagementV1UpdatePut(Async)");
        }

        // verify the required parameter 'entryId' is set
        if (entryId == null) {
            throw new ApiException("Missing the required parameter 'entryId' when calling catalogProductAttributeMediaGalleryManagementV1UpdatePut(Async)");
        }

        return catalogProductAttributeMediaGalleryManagementV1UpdatePutCall(sku, entryId, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest, _callback);

    }

    /**
     * products/{sku}/media/{entryId}
     * Update gallery entry
     * @param sku  (required)
     * @param entryId  (required)
     * @param catalogProductAttributeMediaGalleryManagementV1CreatePostRequest  (optional)
     * @return Boolean
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
    public Boolean catalogProductAttributeMediaGalleryManagementV1UpdatePut(String sku, String entryId, CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest catalogProductAttributeMediaGalleryManagementV1CreatePostRequest) throws ApiException {
        ApiResponse<Boolean> localVarResp = catalogProductAttributeMediaGalleryManagementV1UpdatePutWithHttpInfo(sku, entryId, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest);
        return localVarResp.getData();
    }

    /**
     * products/{sku}/media/{entryId}
     * Update gallery entry
     * @param sku  (required)
     * @param entryId  (required)
     * @param catalogProductAttributeMediaGalleryManagementV1CreatePostRequest  (optional)
     * @return ApiResponse&lt;Boolean&gt;
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
    public ApiResponse<Boolean> catalogProductAttributeMediaGalleryManagementV1UpdatePutWithHttpInfo(String sku, String entryId, CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest catalogProductAttributeMediaGalleryManagementV1CreatePostRequest) throws ApiException {
        okhttp3.Call localVarCall = catalogProductAttributeMediaGalleryManagementV1UpdatePutValidateBeforeCall(sku, entryId, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest, null);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * products/{sku}/media/{entryId} (asynchronously)
     * Update gallery entry
     * @param sku  (required)
     * @param entryId  (required)
     * @param catalogProductAttributeMediaGalleryManagementV1CreatePostRequest  (optional)
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
    public okhttp3.Call catalogProductAttributeMediaGalleryManagementV1UpdatePutAsync(String sku, String entryId, CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest catalogProductAttributeMediaGalleryManagementV1CreatePostRequest, final ApiCallback<Boolean> _callback) throws ApiException {

        okhttp3.Call localVarCall = catalogProductAttributeMediaGalleryManagementV1UpdatePutValidateBeforeCall(sku, entryId, catalogProductAttributeMediaGalleryManagementV1CreatePostRequest, _callback);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
