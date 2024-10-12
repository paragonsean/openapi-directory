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


import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest;
import org.openapitools.client.model.RequestBody;
import org.openapitools.client.model.SKUSpecificationResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SkuSpecificationApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SkuSpecificationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SkuSpecificationApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/specification"
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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteCall(contentType, accept, skuId, _callback);

    }

    /**
     * Delete all SKU Specifications
     * Deletes all SKU Specifications.
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
    public void apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(String contentType, String accept, Integer skuId) throws ApiException {
        apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteWithHttpInfo(contentType, accept, skuId);
    }

    /**
     * Delete all SKU Specifications
     * Deletes all SKU Specifications.
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
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteValidateBeforeCall(contentType, accept, skuId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete all SKU Specifications (asynchronously)
     * Deletes all SKU Specifications.
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteAsync(String contentType, String accept, Integer skuId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationDeleteValidateBeforeCall(contentType, accept, skuId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdSpecificationGet
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationGetCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/specification"
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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationGetValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdSpecificationGetCall(contentType, accept, skuId, _callback);

    }

    /**
     * Get SKU Specifications
     * Retrieves information about an SKU&#39;s Specifications.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 427,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 32,          \&quot;FieldValueId\&quot;: 131,          \&quot;Text\&quot;: \&quot;500g\&quot;      },      {          \&quot;Id\&quot;: 428,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 40,          \&quot;FieldValueId\&quot;: 133,          \&quot;Text\&quot;: \&quot;A\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return List&lt;SKUSpecificationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<SKUSpecificationResponse> apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(String contentType, String accept, Integer skuId) throws ApiException {
        ApiResponse<List<SKUSpecificationResponse>> localVarResp = apiCatalogPvtStockkeepingunitSkuIdSpecificationGetWithHttpInfo(contentType, accept, skuId);
        return localVarResp.getData();
    }

    /**
     * Get SKU Specifications
     * Retrieves information about an SKU&#39;s Specifications.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 427,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 32,          \&quot;FieldValueId\&quot;: 131,          \&quot;Text\&quot;: \&quot;500g\&quot;      },      {          \&quot;Id\&quot;: 428,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 40,          \&quot;FieldValueId\&quot;: 133,          \&quot;Text\&quot;: \&quot;A\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;SKUSpecificationResponse&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SKUSpecificationResponse>> apiCatalogPvtStockkeepingunitSkuIdSpecificationGetWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationGetValidateBeforeCall(contentType, accept, skuId, null);
        Type localVarReturnType = new TypeToken<List<SKUSpecificationResponse>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU Specifications (asynchronously)
     * Retrieves information about an SKU&#39;s Specifications.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 427,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 32,          \&quot;FieldValueId\&quot;: 131,          \&quot;Text\&quot;: \&quot;500g\&quot;      },      {          \&quot;Id\&quot;: 428,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 40,          \&quot;FieldValueId\&quot;: 133,          \&quot;Text\&quot;: \&quot;A\&quot;      }  ]  &#x60;&#x60;&#x60;
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationGetAsync(String contentType, String accept, Integer skuId, final ApiCallback<List<SKUSpecificationResponse>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationGetValidateBeforeCall(contentType, accept, skuId, _callback);
        Type localVarReturnType = new TypeToken<List<SKUSpecificationResponse>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdSpecificationPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationPostCall(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/specification"
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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationPostValidateBeforeCall(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdSpecificationPostCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest, _callback);

    }

    /**
     * Associate SKU Specification
     * Associates a previously created Specification to an SKU.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 730,      \&quot;SkuId\&quot;: 31,      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138,      \&quot;Text\&quot;: \&quot;Size\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest  (optional)
     * @return SKUSpecificationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public SKUSpecificationResponse apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest) throws ApiException {
        ApiResponse<SKUSpecificationResponse> localVarResp = apiCatalogPvtStockkeepingunitSkuIdSpecificationPostWithHttpInfo(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest);
        return localVarResp.getData();
    }

    /**
     * Associate SKU Specification
     * Associates a previously created Specification to an SKU.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 730,      \&quot;SkuId\&quot;: 31,      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138,      \&quot;Text\&quot;: \&quot;Size\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest  (optional)
     * @return ApiResponse&lt;SKUSpecificationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SKUSpecificationResponse> apiCatalogPvtStockkeepingunitSkuIdSpecificationPostWithHttpInfo(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationPostValidateBeforeCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest, null);
        Type localVarReturnType = new TypeToken<SKUSpecificationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Associate SKU Specification (asynchronously)
     * Associates a previously created Specification to an SKU.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 730,      \&quot;SkuId\&quot;: 31,      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138,      \&quot;Text\&quot;: \&quot;Size\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationPostAsync(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest, final ApiCallback<SKUSpecificationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationPostValidateBeforeCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest, _callback);
        Type localVarReturnType = new TypeToken<SKUSpecificationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdSpecificationPut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param requestBody  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationPutCall(String contentType, String accept, Integer skuId, RequestBody requestBody, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = requestBody;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/specification"
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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationPutValidateBeforeCall(String contentType, String accept, Integer skuId, RequestBody requestBody, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdSpecificationPutCall(contentType, accept, skuId, requestBody, _callback);

    }

    /**
     * Update SKU Specification
     * Updates an existing Specification on an existing SKU. This endpoint only updates the &#x60;FieldValueId&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param requestBody  (optional)
     * @return List&lt;SKUSpecificationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<SKUSpecificationResponse> apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(String contentType, String accept, Integer skuId, RequestBody requestBody) throws ApiException {
        ApiResponse<List<SKUSpecificationResponse>> localVarResp = apiCatalogPvtStockkeepingunitSkuIdSpecificationPutWithHttpInfo(contentType, accept, skuId, requestBody);
        return localVarResp.getData();
    }

    /**
     * Update SKU Specification
     * Updates an existing Specification on an existing SKU. This endpoint only updates the &#x60;FieldValueId&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param requestBody  (optional)
     * @return ApiResponse&lt;List&lt;SKUSpecificationResponse&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SKUSpecificationResponse>> apiCatalogPvtStockkeepingunitSkuIdSpecificationPutWithHttpInfo(String contentType, String accept, Integer skuId, RequestBody requestBody) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationPutValidateBeforeCall(contentType, accept, skuId, requestBody, null);
        Type localVarReturnType = new TypeToken<List<SKUSpecificationResponse>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update SKU Specification (asynchronously)
     * Updates an existing Specification on an existing SKU. This endpoint only updates the &#x60;FieldValueId&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param requestBody  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationPutAsync(String contentType, String accept, Integer skuId, RequestBody requestBody, final ApiCallback<List<SKUSpecificationResponse>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationPutValidateBeforeCall(contentType, accept, skuId, requestBody, _callback);
        Type localVarReturnType = new TypeToken<List<SKUSpecificationResponse>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param specificationId Specification’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteCall(String contentType, String accept, Integer skuId, Integer specificationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/specification/{specificationId}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()))
            .replace("{" + "specificationId" + "}", localVarApiClient.escapeString(specificationId.toString()));

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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteValidateBeforeCall(String contentType, String accept, Integer skuId, Integer specificationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(Async)");
        }

        // verify the required parameter 'specificationId' is set
        if (specificationId == null) {
            throw new ApiException("Missing the required parameter 'specificationId' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteCall(contentType, accept, skuId, specificationId, _callback);

    }

    /**
     * Delete SKU Specification
     * Deletes a specific SKU Specification.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param specificationId Specification’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(String contentType, String accept, Integer skuId, Integer specificationId) throws ApiException {
        apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteWithHttpInfo(contentType, accept, skuId, specificationId);
    }

    /**
     * Delete SKU Specification
     * Deletes a specific SKU Specification.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param specificationId Specification’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteWithHttpInfo(String contentType, String accept, Integer skuId, Integer specificationId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteValidateBeforeCall(contentType, accept, skuId, specificationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete SKU Specification (asynchronously)
     * Deletes a specific SKU Specification.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param specificationId Specification’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteAsync(String contentType, String accept, Integer skuId, Integer specificationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDeleteValidateBeforeCall(contentType, accept, skuId, specificationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutCall(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/specificationvalue"
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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutValidateBeforeCall(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest, _callback);

    }

    /**
     * Associate SKU specification using specification name and group name
     * Associates a specification to an SKU using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Size\&quot;,      \&quot;GroupName\&quot;: \&quot;Sizes\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;M\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 419,          \&quot;SkuId\&quot;: 5,          \&quot;FieldId\&quot;: 22,          \&quot;FieldValueId\&quot;: 62,          \&quot;Text\&quot;: \&quot;M\&quot;      }  ]  &#x60;&#x60;&#x60;  
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest  (optional)
     * @return List&lt;ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner> apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest) throws ApiException {
        ApiResponse<List<ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner>> localVarResp = apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutWithHttpInfo(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest);
        return localVarResp.getData();
    }

    /**
     * Associate SKU specification using specification name and group name
     * Associates a specification to an SKU using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Size\&quot;,      \&quot;GroupName\&quot;: \&quot;Sizes\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;M\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 419,          \&quot;SkuId\&quot;: 5,          \&quot;FieldId\&quot;: 22,          \&quot;FieldValueId\&quot;: 62,          \&quot;Text\&quot;: \&quot;M\&quot;      }  ]  &#x60;&#x60;&#x60;  
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest  (optional)
     * @return ApiResponse&lt;List&lt;ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner>> apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutWithHttpInfo(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutValidateBeforeCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest, null);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Associate SKU specification using specification name and group name (asynchronously)
     * Associates a specification to an SKU using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Size\&quot;,      \&quot;GroupName\&quot;: \&quot;Sizes\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;M\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 419,          \&quot;SkuId\&quot;: 5,          \&quot;FieldId\&quot;: 22,          \&quot;FieldValueId\&quot;: 62,          \&quot;Text\&quot;: \&quot;M\&quot;      }  ]  &#x60;&#x60;&#x60;  
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutAsync(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest, final ApiCallback<List<ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutValidateBeforeCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest, _callback);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
