/*
 * Catalog API
 *   > Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.    Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.      ## Index    - [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).  - [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).  - [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).  - [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.  - [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).  - [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.  - [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).  - [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).  - [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.  - [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.  - [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.  - [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).  - [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).  - [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).  - [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).  - [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).  - [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).  - [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).  - [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).  - [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).  - [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items.   - [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value.   - [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.  - [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.  - [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.  - [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.  - [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.  - [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).  - [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.  - [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.      ## Common parameters    | Parameter name              | Description                                                                             |  |---------------------------|-----------------------------------------------------------------------------------------|  | `{{accountName}}`         | Store account name                                                                      |  | `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |  | `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |  | `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |
 *
 * The version of the OpenAPI document: 1.0
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


import org.openapitools.client.model.GetSKUAltID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SkuEanApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SkuEanApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SkuEanApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtStockkeepingunitSkuIdEanDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanDeleteCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/ean"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanDeleteValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanDelete(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdEanDeleteCall(contentType, accept, skuId, _callback);

    }

    /**
     * Delete all SKU EAN values
     * Deletes all EAN values of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtStockkeepingunitSkuIdEanDelete(String contentType, String accept, Integer skuId) throws ApiException {
        apiCatalogPvtStockkeepingunitSkuIdEanDeleteWithHttpInfo(contentType, accept, skuId);
    }

    /**
     * Delete all SKU EAN values
     * Deletes all EAN values of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitSkuIdEanDeleteWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanDeleteValidateBeforeCall(contentType, accept, skuId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete all SKU EAN values (asynchronously)
     * Deletes all EAN values of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanDeleteAsync(String contentType, String accept, Integer skuId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanDeleteValidateBeforeCall(contentType, accept, skuId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdEanEanDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN number. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteCall(String contentType, String accept, Integer skuId, String ean, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()))
            .replace("{" + "ean" + "}", localVarApiClient.escapeString(ean.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteValidateBeforeCall(String contentType, String accept, Integer skuId, String ean, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete(Async)");
        }

        // verify the required parameter 'ean' is set
        if (ean == null) {
            throw new ApiException("Missing the required parameter 'ean' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteCall(contentType, accept, skuId, ean, _callback);

    }

    /**
     * Delete SKU EAN
     * Deletes the EAN value of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN number. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtStockkeepingunitSkuIdEanEanDelete(String contentType, String accept, Integer skuId, String ean) throws ApiException {
        apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteWithHttpInfo(contentType, accept, skuId, ean);
    }

    /**
     * Delete SKU EAN
     * Deletes the EAN value of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN number. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteWithHttpInfo(String contentType, String accept, Integer skuId, String ean) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteValidateBeforeCall(contentType, accept, skuId, ean, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete SKU EAN (asynchronously)
     * Deletes the EAN value of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN number. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteAsync(String contentType, String accept, Integer skuId, String ean, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteValidateBeforeCall(contentType, accept, skuId, ean, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdEanEanPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanEanPostCall(String contentType, String accept, Integer skuId, String ean, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()))
            .replace("{" + "ean" + "}", localVarApiClient.escapeString(ean.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanEanPostValidateBeforeCall(String contentType, String accept, Integer skuId, String ean, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost(Async)");
        }

        // verify the required parameter 'ean' is set
        if (ean == null) {
            throw new ApiException("Missing the required parameter 'ean' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdEanEanPostCall(contentType, accept, skuId, ean, _callback);

    }

    /**
     * Create SKU EAN
     * Creates or updates the EAN value of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtStockkeepingunitSkuIdEanEanPost(String contentType, String accept, Integer skuId, String ean) throws ApiException {
        apiCatalogPvtStockkeepingunitSkuIdEanEanPostWithHttpInfo(contentType, accept, skuId, ean);
    }

    /**
     * Create SKU EAN
     * Creates or updates the EAN value of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitSkuIdEanEanPostWithHttpInfo(String contentType, String accept, Integer skuId, String ean) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanEanPostValidateBeforeCall(contentType, accept, skuId, ean, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create SKU EAN (asynchronously)
     * Creates or updates the EAN value of an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param ean EAN. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanEanPostAsync(String contentType, String accept, Integer skuId, String ean, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanEanPostValidateBeforeCall(contentType, accept, skuId, ean, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdEanGet
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanGetCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/ean"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
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

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanGetValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanGet(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanGet(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdEanGetCall(contentType, accept, skuId, _callback);

    }

    /**
     * Get EAN by SKU ID
     * Retrieves the EAN of the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      \&quot;1234567890123\&quot;  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return List&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<String> apiCatalogPvtStockkeepingunitSkuIdEanGet(String contentType, String accept, Integer skuId) throws ApiException {
        ApiResponse<List<String>> localVarResp = apiCatalogPvtStockkeepingunitSkuIdEanGetWithHttpInfo(contentType, accept, skuId);
        return localVarResp.getData();
    }

    /**
     * Get EAN by SKU ID
     * Retrieves the EAN of the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      \&quot;1234567890123\&quot;  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;String&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<String>> apiCatalogPvtStockkeepingunitSkuIdEanGetWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanGetValidateBeforeCall(contentType, accept, skuId, null);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get EAN by SKU ID (asynchronously)
     * Retrieves the EAN of the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      \&quot;1234567890123\&quot;  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdEanGetAsync(String contentType, String accept, Integer skuId, final ApiCallback<List<String>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdEanGetValidateBeforeCall(contentType, accept, skuId, _callback);
        Type localVarReturnType = new TypeToken<List<String>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for skubyEAN
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ean EAN of the SKU which you need to retrieve details from. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skubyEANCall(String contentType, String accept, String ean, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/stockkeepingunitbyean/{ean}"
            .replace("{" + "ean" + "}", localVarApiClient.escapeString(ean.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
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

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call skubyEANValidateBeforeCall(String contentType, String accept, String ean, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling skubyEAN(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling skubyEAN(Async)");
        }

        // verify the required parameter 'ean' is set
        if (ean == null) {
            throw new ApiException("Missing the required parameter 'ean' when calling skubyEAN(Async)");
        }

        return skubyEANCall(contentType, accept, ean, _callback);

    }

    /**
     * Get SKU by EAN
     * Retrieves an SKU by its EAN ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ]          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ]          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ]          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ean EAN of the SKU which you need to retrieve details from. (required)
     * @return GetSKUAltID
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public GetSKUAltID skubyEAN(String contentType, String accept, String ean) throws ApiException {
        ApiResponse<GetSKUAltID> localVarResp = skubyEANWithHttpInfo(contentType, accept, ean);
        return localVarResp.getData();
    }

    /**
     * Get SKU by EAN
     * Retrieves an SKU by its EAN ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ]          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ]          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ]          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ean EAN of the SKU which you need to retrieve details from. (required)
     * @return ApiResponse&lt;GetSKUAltID&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetSKUAltID> skubyEANWithHttpInfo(String contentType, String accept, String ean) throws ApiException {
        okhttp3.Call localVarCall = skubyEANValidateBeforeCall(contentType, accept, ean, null);
        Type localVarReturnType = new TypeToken<GetSKUAltID>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU by EAN (asynchronously)
     * Retrieves an SKU by its EAN ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ]          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ]          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ]          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param ean EAN of the SKU which you need to retrieve details from. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skubyEANAsync(String contentType, String accept, String ean, final ApiCallback<GetSKUAltID> _callback) throws ApiException {

        okhttp3.Call localVarCall = skubyEANValidateBeforeCall(contentType, accept, ean, _callback);
        Type localVarReturnType = new TypeToken<GetSKUAltID>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
