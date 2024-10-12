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
import org.openapitools.client.model.QuoteCartItemRepositoryV1SavePostRequest;
import org.openapitools.client.model.QuoteDataCartItemInterface;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CartsCartIdItemsItemIdApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CartsCartIdItemsItemIdApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CartsCartIdItemsItemIdApi(ApiClient apiClient) {
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
     * Build call for v1CartsCartIdItemsItemIdDelete
     * @param cartId The cart ID. (required)
     * @param itemId The item ID of the item to be removed. (required)
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
    public okhttp3.Call v1CartsCartIdItemsItemIdDeleteCall(Integer cartId, Integer itemId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/V1/carts/{cartId}/items/{itemId}"
            .replace("{" + "cartId" + "}", localVarApiClient.escapeString(cartId.toString()))
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v1CartsCartIdItemsItemIdDeleteValidateBeforeCall(Integer cartId, Integer itemId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'cartId' is set
        if (cartId == null) {
            throw new ApiException("Missing the required parameter 'cartId' when calling v1CartsCartIdItemsItemIdDelete(Async)");
        }

        // verify the required parameter 'itemId' is set
        if (itemId == null) {
            throw new ApiException("Missing the required parameter 'itemId' when calling v1CartsCartIdItemsItemIdDelete(Async)");
        }

        return v1CartsCartIdItemsItemIdDeleteCall(cartId, itemId, _callback);

    }

    /**
     * carts/{cartId}/items/{itemId}
     * Removes the specified item from the specified cart.
     * @param cartId The cart ID. (required)
     * @param itemId The item ID of the item to be removed. (required)
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
    public Boolean v1CartsCartIdItemsItemIdDelete(Integer cartId, Integer itemId) throws ApiException {
        ApiResponse<Boolean> localVarResp = v1CartsCartIdItemsItemIdDeleteWithHttpInfo(cartId, itemId);
        return localVarResp.getData();
    }

    /**
     * carts/{cartId}/items/{itemId}
     * Removes the specified item from the specified cart.
     * @param cartId The cart ID. (required)
     * @param itemId The item ID of the item to be removed. (required)
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
    public ApiResponse<Boolean> v1CartsCartIdItemsItemIdDeleteWithHttpInfo(Integer cartId, Integer itemId) throws ApiException {
        okhttp3.Call localVarCall = v1CartsCartIdItemsItemIdDeleteValidateBeforeCall(cartId, itemId, null);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * carts/{cartId}/items/{itemId} (asynchronously)
     * Removes the specified item from the specified cart.
     * @param cartId The cart ID. (required)
     * @param itemId The item ID of the item to be removed. (required)
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
    public okhttp3.Call v1CartsCartIdItemsItemIdDeleteAsync(Integer cartId, Integer itemId, final ApiCallback<Boolean> _callback) throws ApiException {

        okhttp3.Call localVarCall = v1CartsCartIdItemsItemIdDeleteValidateBeforeCall(cartId, itemId, _callback);
        Type localVarReturnType = new TypeToken<Boolean>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v1CartsCartIdItemsItemIdPut
     * @param cartId  (required)
     * @param itemId  (required)
     * @param quoteCartItemRepositoryV1SavePostRequest  (optional)
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
    public okhttp3.Call v1CartsCartIdItemsItemIdPutCall(String cartId, String itemId, QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = quoteCartItemRepositoryV1SavePostRequest;

        // create path and map variables
        String localVarPath = "/V1/carts/{cartId}/items/{itemId}"
            .replace("{" + "cartId" + "}", localVarApiClient.escapeString(cartId.toString()))
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
    private okhttp3.Call v1CartsCartIdItemsItemIdPutValidateBeforeCall(String cartId, String itemId, QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'cartId' is set
        if (cartId == null) {
            throw new ApiException("Missing the required parameter 'cartId' when calling v1CartsCartIdItemsItemIdPut(Async)");
        }

        // verify the required parameter 'itemId' is set
        if (itemId == null) {
            throw new ApiException("Missing the required parameter 'itemId' when calling v1CartsCartIdItemsItemIdPut(Async)");
        }

        return v1CartsCartIdItemsItemIdPutCall(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest, _callback);

    }

    /**
     * carts/{cartId}/items/{itemId}
     * Add/update the specified cart item.
     * @param cartId  (required)
     * @param itemId  (required)
     * @param quoteCartItemRepositoryV1SavePostRequest  (optional)
     * @return QuoteDataCartItemInterface
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
    public QuoteDataCartItemInterface v1CartsCartIdItemsItemIdPut(String cartId, String itemId, QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest) throws ApiException {
        ApiResponse<QuoteDataCartItemInterface> localVarResp = v1CartsCartIdItemsItemIdPutWithHttpInfo(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest);
        return localVarResp.getData();
    }

    /**
     * carts/{cartId}/items/{itemId}
     * Add/update the specified cart item.
     * @param cartId  (required)
     * @param itemId  (required)
     * @param quoteCartItemRepositoryV1SavePostRequest  (optional)
     * @return ApiResponse&lt;QuoteDataCartItemInterface&gt;
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
    public ApiResponse<QuoteDataCartItemInterface> v1CartsCartIdItemsItemIdPutWithHttpInfo(String cartId, String itemId, QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest) throws ApiException {
        okhttp3.Call localVarCall = v1CartsCartIdItemsItemIdPutValidateBeforeCall(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest, null);
        Type localVarReturnType = new TypeToken<QuoteDataCartItemInterface>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * carts/{cartId}/items/{itemId} (asynchronously)
     * Add/update the specified cart item.
     * @param cartId  (required)
     * @param itemId  (required)
     * @param quoteCartItemRepositoryV1SavePostRequest  (optional)
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
    public okhttp3.Call v1CartsCartIdItemsItemIdPutAsync(String cartId, String itemId, QuoteCartItemRepositoryV1SavePostRequest quoteCartItemRepositoryV1SavePostRequest, final ApiCallback<QuoteDataCartItemInterface> _callback) throws ApiException {

        okhttp3.Call localVarCall = v1CartsCartIdItemsItemIdPutValidateBeforeCall(cartId, itemId, quoteCartItemRepositoryV1SavePostRequest, _callback);
        Type localVarReturnType = new TypeToken<QuoteDataCartItemInterface>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
