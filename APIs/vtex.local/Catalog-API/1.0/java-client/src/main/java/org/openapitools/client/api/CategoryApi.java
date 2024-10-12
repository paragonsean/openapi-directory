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


import org.openapitools.client.model.ApiCatalogPvtCategoryCategoryIdPutRequest;
import org.openapitools.client.model.Category;
import org.openapitools.client.model.CreateCategoryRequest;
import org.openapitools.client.model.GetCategoryTree;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CategoryApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CategoryApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CategoryApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtCategoryCategoryIdGet
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCategoryCategoryIdGetCall(String contentType, String accept, Integer categoryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/category/{categoryId}"
            .replace("{" + "categoryId" + "}", localVarApiClient.escapeString(categoryId.toString()));

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
    private okhttp3.Call apiCatalogPvtCategoryCategoryIdGetValidateBeforeCall(String contentType, String accept, Integer categoryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtCategoryCategoryIdGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtCategoryCategoryIdGet(Async)");
        }

        // verify the required parameter 'categoryId' is set
        if (categoryId == null) {
            throw new ApiException("Missing the required parameter 'categoryId' when calling apiCatalogPvtCategoryCategoryIdGet(Async)");
        }

        return apiCatalogPvtCategoryCategoryIdGetCall(contentType, accept, categoryId, _callback);

    }

    /**
     * Get Category by ID
     * Retrieves general information about a Category.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 3367,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @return Category
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Category apiCatalogPvtCategoryCategoryIdGet(String contentType, String accept, Integer categoryId) throws ApiException {
        ApiResponse<Category> localVarResp = apiCatalogPvtCategoryCategoryIdGetWithHttpInfo(contentType, accept, categoryId);
        return localVarResp.getData();
    }

    /**
     * Get Category by ID
     * Retrieves general information about a Category.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 3367,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Category&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Category> apiCatalogPvtCategoryCategoryIdGetWithHttpInfo(String contentType, String accept, Integer categoryId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtCategoryCategoryIdGetValidateBeforeCall(contentType, accept, categoryId, null);
        Type localVarReturnType = new TypeToken<Category>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Category by ID (asynchronously)
     * Retrieves general information about a Category.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 3367,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCategoryCategoryIdGetAsync(String contentType, String accept, Integer categoryId, final ApiCallback<Category> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtCategoryCategoryIdGetValidateBeforeCall(contentType, accept, categoryId, _callback);
        Type localVarReturnType = new TypeToken<Category>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtCategoryCategoryIdPut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @param apiCatalogPvtCategoryCategoryIdPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCategoryCategoryIdPutCall(String contentType, String accept, Integer categoryId, ApiCatalogPvtCategoryCategoryIdPutRequest apiCatalogPvtCategoryCategoryIdPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtCategoryCategoryIdPutRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/category/{categoryId}"
            .replace("{" + "categoryId" + "}", localVarApiClient.escapeString(categoryId.toString()));

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
    private okhttp3.Call apiCatalogPvtCategoryCategoryIdPutValidateBeforeCall(String contentType, String accept, Integer categoryId, ApiCatalogPvtCategoryCategoryIdPutRequest apiCatalogPvtCategoryCategoryIdPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtCategoryCategoryIdPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtCategoryCategoryIdPut(Async)");
        }

        // verify the required parameter 'categoryId' is set
        if (categoryId == null) {
            throw new ApiException("Missing the required parameter 'categoryId' when calling apiCatalogPvtCategoryCategoryIdPut(Async)");
        }

        return apiCatalogPvtCategoryCategoryIdPutCall(contentType, accept, categoryId, apiCatalogPvtCategoryCategoryIdPutRequest, _callback);

    }

    /**
     * Update Category
     * Updates a previously existing Category.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @param apiCatalogPvtCategoryCategoryIdPutRequest  (optional)
     * @return Category
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Category apiCatalogPvtCategoryCategoryIdPut(String contentType, String accept, Integer categoryId, ApiCatalogPvtCategoryCategoryIdPutRequest apiCatalogPvtCategoryCategoryIdPutRequest) throws ApiException {
        ApiResponse<Category> localVarResp = apiCatalogPvtCategoryCategoryIdPutWithHttpInfo(contentType, accept, categoryId, apiCatalogPvtCategoryCategoryIdPutRequest);
        return localVarResp.getData();
    }

    /**
     * Update Category
     * Updates a previously existing Category.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @param apiCatalogPvtCategoryCategoryIdPutRequest  (optional)
     * @return ApiResponse&lt;Category&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Category> apiCatalogPvtCategoryCategoryIdPutWithHttpInfo(String contentType, String accept, Integer categoryId, ApiCatalogPvtCategoryCategoryIdPutRequest apiCatalogPvtCategoryCategoryIdPutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtCategoryCategoryIdPutValidateBeforeCall(contentType, accept, categoryId, apiCatalogPvtCategoryCategoryIdPutRequest, null);
        Type localVarReturnType = new TypeToken<Category>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update Category (asynchronously)
     * Updates a previously existing Category.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @param apiCatalogPvtCategoryCategoryIdPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCategoryCategoryIdPutAsync(String contentType, String accept, Integer categoryId, ApiCatalogPvtCategoryCategoryIdPutRequest apiCatalogPvtCategoryCategoryIdPutRequest, final ApiCallback<Category> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtCategoryCategoryIdPutValidateBeforeCall(contentType, accept, categoryId, apiCatalogPvtCategoryCategoryIdPutRequest, _callback);
        Type localVarReturnType = new TypeToken<Category>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtCategoryPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param createCategoryRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCategoryPostCall(String contentType, String accept, CreateCategoryRequest createCategoryRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createCategoryRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/category";

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
    private okhttp3.Call apiCatalogPvtCategoryPostValidateBeforeCall(String contentType, String accept, CreateCategoryRequest createCategoryRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtCategoryPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtCategoryPost(Async)");
        }

        return apiCatalogPvtCategoryPostCall(contentType, accept, createCategoryRequest, _callback);

    }

    /**
     * Create Category
     * Creates a new Category.    If there is a need to create a new category with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ## Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Request body example (custom ID)    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param createCategoryRequest  (optional)
     * @return Category
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Category apiCatalogPvtCategoryPost(String contentType, String accept, CreateCategoryRequest createCategoryRequest) throws ApiException {
        ApiResponse<Category> localVarResp = apiCatalogPvtCategoryPostWithHttpInfo(contentType, accept, createCategoryRequest);
        return localVarResp.getData();
    }

    /**
     * Create Category
     * Creates a new Category.    If there is a need to create a new category with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ## Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Request body example (custom ID)    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param createCategoryRequest  (optional)
     * @return ApiResponse&lt;Category&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Category> apiCatalogPvtCategoryPostWithHttpInfo(String contentType, String accept, CreateCategoryRequest createCategoryRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtCategoryPostValidateBeforeCall(contentType, accept, createCategoryRequest, null);
        Type localVarReturnType = new TypeToken<Category>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create Category (asynchronously)
     * Creates a new Category.    If there is a need to create a new category with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ## Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Request body example (custom ID)    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param createCategoryRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCategoryPostAsync(String contentType, String accept, CreateCategoryRequest createCategoryRequest, final ApiCallback<Category> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtCategoryPostValidateBeforeCall(contentType, accept, createCategoryRequest, _callback);
        Type localVarReturnType = new TypeToken<Category>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for categoryTree
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryLevels Value of the category level you need to retrieve. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call categoryTreeCall(String contentType, String accept, String categoryLevels, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pub/category/tree/{categoryLevels}"
            .replace("{" + "categoryLevels" + "}", localVarApiClient.escapeString(categoryLevels.toString()));

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
    private okhttp3.Call categoryTreeValidateBeforeCall(String contentType, String accept, String categoryLevels, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling categoryTree(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling categoryTree(Async)");
        }

        // verify the required parameter 'categoryLevels' is set
        if (categoryLevels == null) {
            throw new ApiException("Missing the required parameter 'categoryLevels' when calling categoryTree(Async)");
        }

        return categoryTreeCall(contentType, accept, categoryLevels, _callback);

    }

    /**
     * Get Category Tree
     * Retrieves the Category Tree of your store. Get all the category levels registered in the Catalog or define the level up to which you want to get.    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;id\&quot;: 1,          \&quot;name\&quot;: \&quot;Alimentação\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 6,                  \&quot;name\&quot;: \&quot;Bebedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/bebedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bebedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 7,                  \&quot;name\&quot;: \&quot;Comedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/comedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Comedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 8,                  \&quot;name\&quot;: \&quot;Biscoitos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/biscoitos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Biscoitos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 9,                  \&quot;name\&quot;: \&quot;Petiscos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/petiscos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Petiscos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 10,                  \&quot;name\&quot;: \&quot;Ração Seca\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-seca\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Seca para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 11,                  \&quot;name\&quot;: \&quot;Ração Úmida\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-umida\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Úmida para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Alimentação para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      },      {          \&quot;id\&quot;: 2,          \&quot;name\&quot;: \&quot;Brinquedos\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 12,                  \&quot;name\&quot;: \&quot;Bolinhas\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/bolinhas\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bolinhas para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 13,                  \&quot;name\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/ratinhos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 19,                  \&quot;name\&quot;: \&quot;Arranhador para gato\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/arranhador-para-gato\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Brinquedo Arranhador para gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;Arranhador gatos é indispensável no lar com felinos. Ideais para afiar as unhas e garantir a diversão\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Brinquedos para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryLevels Value of the category level you need to retrieve. (required)
     * @return List&lt;GetCategoryTree&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<GetCategoryTree> categoryTree(String contentType, String accept, String categoryLevels) throws ApiException {
        ApiResponse<List<GetCategoryTree>> localVarResp = categoryTreeWithHttpInfo(contentType, accept, categoryLevels);
        return localVarResp.getData();
    }

    /**
     * Get Category Tree
     * Retrieves the Category Tree of your store. Get all the category levels registered in the Catalog or define the level up to which you want to get.    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;id\&quot;: 1,          \&quot;name\&quot;: \&quot;Alimentação\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 6,                  \&quot;name\&quot;: \&quot;Bebedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/bebedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bebedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 7,                  \&quot;name\&quot;: \&quot;Comedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/comedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Comedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 8,                  \&quot;name\&quot;: \&quot;Biscoitos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/biscoitos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Biscoitos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 9,                  \&quot;name\&quot;: \&quot;Petiscos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/petiscos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Petiscos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 10,                  \&quot;name\&quot;: \&quot;Ração Seca\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-seca\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Seca para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 11,                  \&quot;name\&quot;: \&quot;Ração Úmida\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-umida\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Úmida para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Alimentação para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      },      {          \&quot;id\&quot;: 2,          \&quot;name\&quot;: \&quot;Brinquedos\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 12,                  \&quot;name\&quot;: \&quot;Bolinhas\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/bolinhas\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bolinhas para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 13,                  \&quot;name\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/ratinhos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 19,                  \&quot;name\&quot;: \&quot;Arranhador para gato\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/arranhador-para-gato\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Brinquedo Arranhador para gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;Arranhador gatos é indispensável no lar com felinos. Ideais para afiar as unhas e garantir a diversão\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Brinquedos para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryLevels Value of the category level you need to retrieve. (required)
     * @return ApiResponse&lt;List&lt;GetCategoryTree&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<GetCategoryTree>> categoryTreeWithHttpInfo(String contentType, String accept, String categoryLevels) throws ApiException {
        okhttp3.Call localVarCall = categoryTreeValidateBeforeCall(contentType, accept, categoryLevels, null);
        Type localVarReturnType = new TypeToken<List<GetCategoryTree>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Category Tree (asynchronously)
     * Retrieves the Category Tree of your store. Get all the category levels registered in the Catalog or define the level up to which you want to get.    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;id\&quot;: 1,          \&quot;name\&quot;: \&quot;Alimentação\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 6,                  \&quot;name\&quot;: \&quot;Bebedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/bebedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bebedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 7,                  \&quot;name\&quot;: \&quot;Comedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/comedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Comedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 8,                  \&quot;name\&quot;: \&quot;Biscoitos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/biscoitos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Biscoitos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 9,                  \&quot;name\&quot;: \&quot;Petiscos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/petiscos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Petiscos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 10,                  \&quot;name\&quot;: \&quot;Ração Seca\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-seca\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Seca para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 11,                  \&quot;name\&quot;: \&quot;Ração Úmida\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-umida\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Úmida para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Alimentação para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      },      {          \&quot;id\&quot;: 2,          \&quot;name\&quot;: \&quot;Brinquedos\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 12,                  \&quot;name\&quot;: \&quot;Bolinhas\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/bolinhas\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bolinhas para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 13,                  \&quot;name\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/ratinhos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 19,                  \&quot;name\&quot;: \&quot;Arranhador para gato\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/arranhador-para-gato\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Brinquedo Arranhador para gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;Arranhador gatos é indispensável no lar com felinos. Ideais para afiar as unhas e garantir a diversão\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Brinquedos para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryLevels Value of the category level you need to retrieve. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call categoryTreeAsync(String contentType, String accept, String categoryLevels, final ApiCallback<List<GetCategoryTree>> _callback) throws ApiException {

        okhttp3.Call localVarCall = categoryTreeValidateBeforeCall(contentType, accept, categoryLevels, _callback);
        Type localVarReturnType = new TypeToken<List<GetCategoryTree>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
