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


import org.openapitools.client.model.ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TradePolicyApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TradePolicyApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TradePolicyApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtProductProductIdSalespolicyGet
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSalespolicyGetCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/product/{productId}/salespolicy"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()));

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
    private okhttp3.Call apiCatalogPvtProductProductIdSalespolicyGetValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtProductProductIdSalespolicyGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtProductProductIdSalespolicyGet(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling apiCatalogPvtProductProductIdSalespolicyGet(Async)");
        }

        return apiCatalogPvtProductProductIdSalespolicyGetCall(contentType, accept, productId, _callback);

    }

    /**
     * Get Trade Policies by Product ID
     * Retrieves a list of Trade Policies associated to a Product based on the Product&#39;s ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 2      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 3      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 4      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return List&lt;ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner> apiCatalogPvtProductProductIdSalespolicyGet(String contentType, String accept, Integer productId) throws ApiException {
        ApiResponse<List<ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner>> localVarResp = apiCatalogPvtProductProductIdSalespolicyGetWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get Trade Policies by Product ID
     * Retrieves a list of Trade Policies associated to a Product based on the Product&#39;s ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 2      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 3      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 4      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner>> apiCatalogPvtProductProductIdSalespolicyGetWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSalespolicyGetValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Trade Policies by Product ID (asynchronously)
     * Retrieves a list of Trade Policies associated to a Product based on the Product&#39;s ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 2      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 3      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 4      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSalespolicyGetAsync(String contentType, String accept, Integer productId, final ApiCallback<List<ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSalespolicyGetValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteCall(String contentType, String accept, Integer productId, Integer tradepolicyId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId}"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "tradepolicyId" + "}", localVarApiClient.escapeString(tradepolicyId.toString()));

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
    private okhttp3.Call apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteValidateBeforeCall(String contentType, String accept, Integer productId, Integer tradepolicyId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(Async)");
        }

        // verify the required parameter 'tradepolicyId' is set
        if (tradepolicyId == null) {
            throw new ApiException("Missing the required parameter 'tradepolicyId' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(Async)");
        }

        return apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteCall(contentType, accept, productId, tradepolicyId, _callback);

    }

    /**
     * Remove Product from Trade Policy
     * Disassociates a Trade Policy of a Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(String contentType, String accept, Integer productId, Integer tradepolicyId) throws ApiException {
        apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteWithHttpInfo(contentType, accept, productId, tradepolicyId);
    }

    /**
     * Remove Product from Trade Policy
     * Disassociates a Trade Policy of a Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteWithHttpInfo(String contentType, String accept, Integer productId, Integer tradepolicyId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteValidateBeforeCall(contentType, accept, productId, tradepolicyId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Remove Product from Trade Policy (asynchronously)
     * Disassociates a Trade Policy of a Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteAsync(String contentType, String accept, Integer productId, Integer tradepolicyId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDeleteValidateBeforeCall(contentType, accept, productId, tradepolicyId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostCall(String contentType, String accept, Integer productId, Integer tradepolicyId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId}"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "tradepolicyId" + "}", localVarApiClient.escapeString(tradepolicyId.toString()));

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
    private okhttp3.Call apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostValidateBeforeCall(String contentType, String accept, Integer productId, Integer tradepolicyId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(Async)");
        }

        // verify the required parameter 'tradepolicyId' is set
        if (tradepolicyId == null) {
            throw new ApiException("Missing the required parameter 'tradepolicyId' when calling apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(Async)");
        }

        return apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostCall(contentType, accept, productId, tradepolicyId, _callback);

    }

    /**
     * Associate Product with Trade Policy
     * Associates an existing Trade Policy with a Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(String contentType, String accept, Integer productId, Integer tradepolicyId) throws ApiException {
        apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostWithHttpInfo(contentType, accept, productId, tradepolicyId);
    }

    /**
     * Associate Product with Trade Policy
     * Associates an existing Trade Policy with a Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostWithHttpInfo(String contentType, String accept, Integer productId, Integer tradepolicyId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostValidateBeforeCall(contentType, accept, productId, tradepolicyId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Associate Product with Trade Policy (asynchronously)
     * Associates an existing Trade Policy with a Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param tradepolicyId Trade Policy’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostAsync(String contentType, String accept, Integer productId, Integer tradepolicyId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPostValidateBeforeCall(contentType, accept, productId, tradepolicyId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy’s unique numerical identifier. (required)
     * @param page Page number. (optional)
     * @param pageSize Number of items in the page. (optional)
     * @param onlyAssigned If set as &#x60;false&#x60;, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetCall(String contentType, String accept, Integer sc, Integer page, Integer pageSize, Boolean onlyAssigned, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (sc != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sc", sc));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pageSize", pageSize));
        }

        if (onlyAssigned != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("onlyAssigned", onlyAssigned));
        }

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
    private okhttp3.Call apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetValidateBeforeCall(String contentType, String accept, Integer sc, Integer page, Integer pageSize, Boolean onlyAssigned, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(Async)");
        }

        // verify the required parameter 'sc' is set
        if (sc == null) {
            throw new ApiException("Missing the required parameter 'sc' when calling apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(Async)");
        }

        return apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetCall(contentType, accept, sc, page, pageSize, onlyAssigned, _callback);

    }

    /**
     * List all SKUs of a Trade Policy
     * Retrieves a list of SKU IDs of a Trade Policy.   ## Response body example    &#x60;&#x60;&#x60;json  [      405380,      405381,      405382,      405383,      405384,      405385,      405386,      405387,      405388,      405389,      405390,      405391,      405392,      405393,      405394,      405395,      405396,      405397,      405398,      405399,      405400,      405556  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy’s unique numerical identifier. (required)
     * @param page Page number. (optional)
     * @param pageSize Number of items in the page. (optional)
     * @param onlyAssigned If set as &#x60;false&#x60;, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned. (optional)
     * @return List&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<Integer> apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(String contentType, String accept, Integer sc, Integer page, Integer pageSize, Boolean onlyAssigned) throws ApiException {
        ApiResponse<List<Integer>> localVarResp = apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetWithHttpInfo(contentType, accept, sc, page, pageSize, onlyAssigned);
        return localVarResp.getData();
    }

    /**
     * List all SKUs of a Trade Policy
     * Retrieves a list of SKU IDs of a Trade Policy.   ## Response body example    &#x60;&#x60;&#x60;json  [      405380,      405381,      405382,      405383,      405384,      405385,      405386,      405387,      405388,      405389,      405390,      405391,      405392,      405393,      405394,      405395,      405396,      405397,      405398,      405399,      405400,      405556  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy’s unique numerical identifier. (required)
     * @param page Page number. (optional)
     * @param pageSize Number of items in the page. (optional)
     * @param onlyAssigned If set as &#x60;false&#x60;, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned. (optional)
     * @return ApiResponse&lt;List&lt;Integer&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Integer>> apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetWithHttpInfo(String contentType, String accept, Integer sc, Integer page, Integer pageSize, Boolean onlyAssigned) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetValidateBeforeCall(contentType, accept, sc, page, pageSize, onlyAssigned, null);
        Type localVarReturnType = new TypeToken<List<Integer>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all SKUs of a Trade Policy (asynchronously)
     * Retrieves a list of SKU IDs of a Trade Policy.   ## Response body example    &#x60;&#x60;&#x60;json  [      405380,      405381,      405382,      405383,      405384,      405385,      405386,      405387,      405388,      405389,      405390,      405391,      405392,      405393,      405394,      405395,      405396,      405397,      405398,      405399,      405400,      405556  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param sc Trade Policy’s unique numerical identifier. (required)
     * @param page Page number. (optional)
     * @param pageSize Number of items in the page. (optional)
     * @param onlyAssigned If set as &#x60;false&#x60;, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetAsync(String contentType, String accept, Integer sc, Integer page, Integer pageSize, Boolean onlyAssigned, final ApiCallback<List<Integer>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGetValidateBeforeCall(contentType, accept, sc, page, pageSize, onlyAssigned, _callback);
        Type localVarReturnType = new TypeToken<List<Integer>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
