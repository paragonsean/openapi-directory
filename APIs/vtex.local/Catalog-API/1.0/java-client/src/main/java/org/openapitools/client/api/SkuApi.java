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


import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitGet200Response;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitPost200Response;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitPostRequest;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdPut200Response;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdPutRequest;
import org.openapitools.client.model.GetSKUAltID;
import org.openapitools.client.model.GetSKUandContext;
import org.openapitools.client.model.Sku200Response;
import org.openapitools.client.model.SkulistbyProductId;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SkuApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SkuApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SkuApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtStockkeepingunitGet
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitGetCall(String contentType, String accept, String refId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (refId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("refId", refId));
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
    private okhttp3.Call apiCatalogPvtStockkeepingunitGetValidateBeforeCall(String contentType, String accept, String refId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitGet(Async)");
        }

        // verify the required parameter 'refId' is set
        if (refId == null) {
            throw new ApiException("Missing the required parameter 'refId' when calling apiCatalogPvtStockkeepingunitGet(Async)");
        }

        return apiCatalogPvtStockkeepingunitGetCall(contentType, accept, refId, _callback);

    }

    /**
     * Get SKU by RefId
     * Retrieves information about a specific SKU by its &#x60;RefId&#x60;.     ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;Name\&quot;: \&quot;Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.0000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 1.0000,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-03-12T15:42:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @return ApiCatalogPvtStockkeepingunitGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtStockkeepingunitGet200Response apiCatalogPvtStockkeepingunitGet(String contentType, String accept, String refId) throws ApiException {
        ApiResponse<ApiCatalogPvtStockkeepingunitGet200Response> localVarResp = apiCatalogPvtStockkeepingunitGetWithHttpInfo(contentType, accept, refId);
        return localVarResp.getData();
    }

    /**
     * Get SKU by RefId
     * Retrieves information about a specific SKU by its &#x60;RefId&#x60;.     ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;Name\&quot;: \&quot;Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.0000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 1.0000,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-03-12T15:42:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @return ApiResponse&lt;ApiCatalogPvtStockkeepingunitGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtStockkeepingunitGet200Response> apiCatalogPvtStockkeepingunitGetWithHttpInfo(String contentType, String accept, String refId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitGetValidateBeforeCall(contentType, accept, refId, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU by RefId (asynchronously)
     * Retrieves information about a specific SKU by its &#x60;RefId&#x60;.     ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;Name\&quot;: \&quot;Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.0000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 1.0000,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-03-12T15:42:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitGetAsync(String contentType, String accept, String refId, final ApiCallback<ApiCatalogPvtStockkeepingunitGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitGetValidateBeforeCall(contentType, accept, refId, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtStockkeepingunitPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitPostCall(String contentType, String accept, ApiCatalogPvtStockkeepingunitPostRequest apiCatalogPvtStockkeepingunitPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtStockkeepingunitPostRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/stockkeepingunit";

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
    private okhttp3.Call apiCatalogPvtStockkeepingunitPostValidateBeforeCall(String contentType, String accept, ApiCatalogPvtStockkeepingunitPostRequest apiCatalogPvtStockkeepingunitPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitPost(Async)");
        }

        return apiCatalogPvtStockkeepingunitPostCall(contentType, accept, apiCatalogPvtStockkeepingunitPostRequest, _callback);

    }

    /**
     * Create SKU
     *     Creates a new SKU.    If there is a need to create a new SKU with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ### Request body example (custom ID)    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;:1,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtStockkeepingunitPostRequest  (optional)
     * @return ApiCatalogPvtStockkeepingunitPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtStockkeepingunitPost200Response apiCatalogPvtStockkeepingunitPost(String contentType, String accept, ApiCatalogPvtStockkeepingunitPostRequest apiCatalogPvtStockkeepingunitPostRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtStockkeepingunitPost200Response> localVarResp = apiCatalogPvtStockkeepingunitPostWithHttpInfo(contentType, accept, apiCatalogPvtStockkeepingunitPostRequest);
        return localVarResp.getData();
    }

    /**
     * Create SKU
     *     Creates a new SKU.    If there is a need to create a new SKU with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ### Request body example (custom ID)    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;:1,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtStockkeepingunitPostRequest  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtStockkeepingunitPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtStockkeepingunitPost200Response> apiCatalogPvtStockkeepingunitPostWithHttpInfo(String contentType, String accept, ApiCatalogPvtStockkeepingunitPostRequest apiCatalogPvtStockkeepingunitPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitPostValidateBeforeCall(contentType, accept, apiCatalogPvtStockkeepingunitPostRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create SKU (asynchronously)
     *     Creates a new SKU.    If there is a need to create a new SKU with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ### Request body example (custom ID)    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;:1,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtStockkeepingunitPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitPostAsync(String contentType, String accept, ApiCatalogPvtStockkeepingunitPostRequest apiCatalogPvtStockkeepingunitPostRequest, final ApiCallback<ApiCatalogPvtStockkeepingunitPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitPostValidateBeforeCall(contentType, accept, apiCatalogPvtStockkeepingunitPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdPut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdPutCall(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdPutRequest apiCatalogPvtStockkeepingunitSkuIdPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtStockkeepingunitSkuIdPutRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}"
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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdPutValidateBeforeCall(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdPutRequest apiCatalogPvtStockkeepingunitSkuIdPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdPut(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdPut(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdPutCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdPutRequest, _callback);

    }

    /**
     * Update SKU
     * Updates an existing SKU.     ### Request body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 310118448,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118449,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;sku test\&quot;,      \&quot;RefId\&quot;: \&quot;1254789\&quot;,      \&quot;PackagedHeight\&quot;: 10.0,      \&quot;PackagedLength\&quot;: 10.0,      \&quot;PackagedWidth\&quot;: 10.0,      \&quot;PackagedWeightKg\&quot;: 10.0,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 0.1667,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-04-22T12:12:47.5219561\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdPutRequest  (optional)
     * @return ApiCatalogPvtStockkeepingunitSkuIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtStockkeepingunitSkuIdPut200Response apiCatalogPvtStockkeepingunitSkuIdPut(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdPutRequest apiCatalogPvtStockkeepingunitSkuIdPutRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtStockkeepingunitSkuIdPut200Response> localVarResp = apiCatalogPvtStockkeepingunitSkuIdPutWithHttpInfo(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdPutRequest);
        return localVarResp.getData();
    }

    /**
     * Update SKU
     * Updates an existing SKU.     ### Request body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 310118448,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118449,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;sku test\&quot;,      \&quot;RefId\&quot;: \&quot;1254789\&quot;,      \&quot;PackagedHeight\&quot;: 10.0,      \&quot;PackagedLength\&quot;: 10.0,      \&quot;PackagedWidth\&quot;: 10.0,      \&quot;PackagedWeightKg\&quot;: 10.0,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 0.1667,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-04-22T12:12:47.5219561\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdPutRequest  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtStockkeepingunitSkuIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtStockkeepingunitSkuIdPut200Response> apiCatalogPvtStockkeepingunitSkuIdPutWithHttpInfo(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdPutRequest apiCatalogPvtStockkeepingunitSkuIdPutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdPutValidateBeforeCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdPutRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitSkuIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update SKU (asynchronously)
     * Updates an existing SKU.     ### Request body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 310118448,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118449,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;sku test\&quot;,      \&quot;RefId\&quot;: \&quot;1254789\&quot;,      \&quot;PackagedHeight\&quot;: 10.0,      \&quot;PackagedLength\&quot;: 10.0,      \&quot;PackagedWidth\&quot;: 10.0,      \&quot;PackagedWeightKg\&quot;: 10.0,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 0.1667,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-04-22T12:12:47.5219561\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param apiCatalogPvtStockkeepingunitSkuIdPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdPutAsync(String contentType, String accept, Integer skuId, ApiCatalogPvtStockkeepingunitSkuIdPutRequest apiCatalogPvtStockkeepingunitSkuIdPutRequest, final ApiCallback<ApiCatalogPvtStockkeepingunitSkuIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdPutValidateBeforeCall(contentType, accept, skuId, apiCatalogPvtStockkeepingunitSkuIdPutRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitSkuIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listallSKUIDs
     * @param page Number of the page from where you need to retrieve SKU IDs. (required)
     * @param pagesize Size of the page from where you need retrieve SKU IDs. The maximum value is &#x60;1000&#x60;. (required)
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listallSKUIDsCall(Integer page, Integer pagesize, String contentType, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/stockkeepingunitids";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pagesize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pagesize", pagesize));
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
    private okhttp3.Call listallSKUIDsValidateBeforeCall(Integer page, Integer pagesize, String contentType, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'page' is set
        if (page == null) {
            throw new ApiException("Missing the required parameter 'page' when calling listallSKUIDs(Async)");
        }

        // verify the required parameter 'pagesize' is set
        if (pagesize == null) {
            throw new ApiException("Missing the required parameter 'pagesize' when calling listallSKUIDs(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling listallSKUIDs(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling listallSKUIDs(Async)");
        }

        return listallSKUIDsCall(page, pagesize, contentType, accept, _callback);

    }

    /**
     * List all SKU IDs
     * Retrieves the IDs of all SKUs in your store. Presents the results with page size and pagination.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [    1,    2,    3,    4,    5,    6,    7,    8,    9,    10  ]  &#x60;&#x60;&#x60;
     * @param page Number of the page from where you need to retrieve SKU IDs. (required)
     * @param pagesize Size of the page from where you need retrieve SKU IDs. The maximum value is &#x60;1000&#x60;. (required)
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return List&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<Integer> listallSKUIDs(Integer page, Integer pagesize, String contentType, String accept) throws ApiException {
        ApiResponse<List<Integer>> localVarResp = listallSKUIDsWithHttpInfo(page, pagesize, contentType, accept);
        return localVarResp.getData();
    }

    /**
     * List all SKU IDs
     * Retrieves the IDs of all SKUs in your store. Presents the results with page size and pagination.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [    1,    2,    3,    4,    5,    6,    7,    8,    9,    10  ]  &#x60;&#x60;&#x60;
     * @param page Number of the page from where you need to retrieve SKU IDs. (required)
     * @param pagesize Size of the page from where you need retrieve SKU IDs. The maximum value is &#x60;1000&#x60;. (required)
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return ApiResponse&lt;List&lt;Integer&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Integer>> listallSKUIDsWithHttpInfo(Integer page, Integer pagesize, String contentType, String accept) throws ApiException {
        okhttp3.Call localVarCall = listallSKUIDsValidateBeforeCall(page, pagesize, contentType, accept, null);
        Type localVarReturnType = new TypeToken<List<Integer>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all SKU IDs (asynchronously)
     * Retrieves the IDs of all SKUs in your store. Presents the results with page size and pagination.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [    1,    2,    3,    4,    5,    6,    7,    8,    9,    10  ]  &#x60;&#x60;&#x60;
     * @param page Number of the page from where you need to retrieve SKU IDs. (required)
     * @param pagesize Size of the page from where you need retrieve SKU IDs. The maximum value is &#x60;1000&#x60;. (required)
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listallSKUIDsAsync(Integer page, Integer pagesize, String contentType, String accept, final ApiCallback<List<Integer>> _callback) throws ApiException {

        okhttp3.Call localVarCall = listallSKUIDsValidateBeforeCall(page, pagesize, contentType, accept, _callback);
        Type localVarReturnType = new TypeToken<List<Integer>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for sku
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU unique identifier number. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skuCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}"
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
    private okhttp3.Call skuValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling sku(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling sku(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling sku(Async)");
        }

        return skuCall(contentType, accept, skuId, _callback);

    }

    /**
     * Get SKU
     * Retrieves a specific SKU by its ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;Ração Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.5000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: 2.2000,      \&quot;Length\&quot;: 4.4000,      \&quot;Width\&quot;: 3.3000,      \&quot;WeightKg\&quot;: 1.1000,      \&quot;CubicWeight\&quot;: 0.4550,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2021-06-08T15:25:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 300.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ]  }  &#x60;&#x60;&#x60;    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU unique identifier number. (required)
     * @return Sku200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Sku200Response sku(String contentType, String accept, Integer skuId) throws ApiException {
        ApiResponse<Sku200Response> localVarResp = skuWithHttpInfo(contentType, accept, skuId);
        return localVarResp.getData();
    }

    /**
     * Get SKU
     * Retrieves a specific SKU by its ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;Ração Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.5000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: 2.2000,      \&quot;Length\&quot;: 4.4000,      \&quot;Width\&quot;: 3.3000,      \&quot;WeightKg\&quot;: 1.1000,      \&quot;CubicWeight\&quot;: 0.4550,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2021-06-08T15:25:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 300.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ]  }  &#x60;&#x60;&#x60;    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU unique identifier number. (required)
     * @return ApiResponse&lt;Sku200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Sku200Response> skuWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = skuValidateBeforeCall(contentType, accept, skuId, null);
        Type localVarReturnType = new TypeToken<Sku200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU (asynchronously)
     * Retrieves a specific SKU by its ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;Ração Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.5000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: 2.2000,      \&quot;Length\&quot;: 4.4000,      \&quot;Width\&quot;: 3.3000,      \&quot;WeightKg\&quot;: 1.1000,      \&quot;CubicWeight\&quot;: 0.4550,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2021-06-08T15:25:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 300.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ]  }  &#x60;&#x60;&#x60;    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU unique identifier number. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skuAsync(String contentType, String accept, Integer skuId, final ApiCallback<Sku200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = skuValidateBeforeCall(contentType, accept, skuId, _callback);
        Type localVarReturnType = new TypeToken<Sku200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for skuContext
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU&#39;s unique identifier number. (required)
     * @param sc Trade Policy&#39;s unique identifier number. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Last-Modified -  <br>  * Vary -  <br>  * X-Powered-By-VTEX-Cache -  <br>  * X-VTEX-Cache-Backend-Connect-Time -  <br>  * X-VTEX-Cache-Backend-Header-Time -  <br>  * X-VTEX-Cache-Server -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Time -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skuContextCall(String contentType, String accept, Integer skuId, Integer sc, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/stockkeepingunitbyid/{skuId}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (sc != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sc", sc));
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
    private okhttp3.Call skuContextValidateBeforeCall(String contentType, String accept, Integer skuId, Integer sc, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling skuContext(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling skuContext(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling skuContext(Async)");
        }

        return skuContextCall(contentType, accept, skuId, sc, _callback);

    }

    /**
     * Get SKU and context
     * Retrieves context of an SKU.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductRefId\&quot;: \&quot;0987\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/1/10/\&quot;,          \&quot;/1/\&quot;,          \&quot;/20/\&quot;      ],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 11,              \&quot;FieldGroupName\&quot;: \&quot;Especificações\&quot;          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ],              \&quot;IsFilter\&quot;: true,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 3,          \&quot;152\&quot;: 0,          \&quot;158\&quot;: 1      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: false,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: \&quot;Indexer\&quot;,      \&quot;ModalType\&quot;: \&quot;\&quot;,      \&quot;KeyWords\&quot;: \&quot;basquete, tabela\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU&#39;s unique identifier number. (required)
     * @param sc Trade Policy&#39;s unique identifier number. (optional)
     * @return GetSKUandContext
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Last-Modified -  <br>  * Vary -  <br>  * X-Powered-By-VTEX-Cache -  <br>  * X-VTEX-Cache-Backend-Connect-Time -  <br>  * X-VTEX-Cache-Backend-Header-Time -  <br>  * X-VTEX-Cache-Server -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Time -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  </td></tr>
     </table>
     */
    public GetSKUandContext skuContext(String contentType, String accept, Integer skuId, Integer sc) throws ApiException {
        ApiResponse<GetSKUandContext> localVarResp = skuContextWithHttpInfo(contentType, accept, skuId, sc);
        return localVarResp.getData();
    }

    /**
     * Get SKU and context
     * Retrieves context of an SKU.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductRefId\&quot;: \&quot;0987\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/1/10/\&quot;,          \&quot;/1/\&quot;,          \&quot;/20/\&quot;      ],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 11,              \&quot;FieldGroupName\&quot;: \&quot;Especificações\&quot;          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ],              \&quot;IsFilter\&quot;: true,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 3,          \&quot;152\&quot;: 0,          \&quot;158\&quot;: 1      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: false,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: \&quot;Indexer\&quot;,      \&quot;ModalType\&quot;: \&quot;\&quot;,      \&quot;KeyWords\&quot;: \&quot;basquete, tabela\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU&#39;s unique identifier number. (required)
     * @param sc Trade Policy&#39;s unique identifier number. (optional)
     * @return ApiResponse&lt;GetSKUandContext&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Last-Modified -  <br>  * Vary -  <br>  * X-Powered-By-VTEX-Cache -  <br>  * X-VTEX-Cache-Backend-Connect-Time -  <br>  * X-VTEX-Cache-Backend-Header-Time -  <br>  * X-VTEX-Cache-Server -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Time -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetSKUandContext> skuContextWithHttpInfo(String contentType, String accept, Integer skuId, Integer sc) throws ApiException {
        okhttp3.Call localVarCall = skuContextValidateBeforeCall(contentType, accept, skuId, sc, null);
        Type localVarReturnType = new TypeToken<GetSKUandContext>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU and context (asynchronously)
     * Retrieves context of an SKU.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductRefId\&quot;: \&quot;0987\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/1/10/\&quot;,          \&quot;/1/\&quot;,          \&quot;/20/\&quot;      ],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 11,              \&quot;FieldGroupName\&quot;: \&quot;Especificações\&quot;          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ],              \&quot;IsFilter\&quot;: true,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 3,          \&quot;152\&quot;: 0,          \&quot;158\&quot;: 1      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: false,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: \&quot;Indexer\&quot;,      \&quot;ModalType\&quot;: \&quot;\&quot;,      \&quot;KeyWords\&quot;: \&quot;basquete, tabela\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU&#39;s unique identifier number. (required)
     * @param sc Trade Policy&#39;s unique identifier number. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * Date -  <br>  * Last-Modified -  <br>  * Vary -  <br>  * X-Powered-By-VTEX-Cache -  <br>  * X-VTEX-Cache-Backend-Connect-Time -  <br>  * X-VTEX-Cache-Backend-Header-Time -  <br>  * X-VTEX-Cache-Server -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Time -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skuContextAsync(String contentType, String accept, Integer skuId, Integer sc, final ApiCallback<GetSKUandContext> _callback) throws ApiException {

        okhttp3.Call localVarCall = skuContextValidateBeforeCall(contentType, accept, skuId, sc, _callback);
        Type localVarReturnType = new TypeToken<GetSKUandContext>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for skuIdbyRefId
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skuIdbyRefIdCall(String contentType, String accept, String refId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/{refId}"
            .replace("{" + "refId" + "}", localVarApiClient.escapeString(refId.toString()));

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
    private okhttp3.Call skuIdbyRefIdValidateBeforeCall(String contentType, String accept, String refId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling skuIdbyRefId(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling skuIdbyRefId(Async)");
        }

        // verify the required parameter 'refId' is set
        if (refId == null) {
            throw new ApiException("Missing the required parameter 'refId' when calling skuIdbyRefId(Async)");
        }

        return skuIdbyRefIdCall(contentType, accept, refId, _callback);

    }

    /**
     * Get SKU ID by Reference ID
     * Retrieves an SKU ID by the SKU&#39;s Reference ID.     ### Response body example    &#x60;&#x60;&#x60;json  \&quot;310118450\&quot;  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public String skuIdbyRefId(String contentType, String accept, String refId) throws ApiException {
        ApiResponse<String> localVarResp = skuIdbyRefIdWithHttpInfo(contentType, accept, refId);
        return localVarResp.getData();
    }

    /**
     * Get SKU ID by Reference ID
     * Retrieves an SKU ID by the SKU&#39;s Reference ID.     ### Response body example    &#x60;&#x60;&#x60;json  \&quot;310118450\&quot;  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> skuIdbyRefIdWithHttpInfo(String contentType, String accept, String refId) throws ApiException {
        okhttp3.Call localVarCall = skuIdbyRefIdValidateBeforeCall(contentType, accept, refId, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU ID by Reference ID (asynchronously)
     * Retrieves an SKU ID by the SKU&#39;s Reference ID.     ### Response body example    &#x60;&#x60;&#x60;json  \&quot;310118450\&quot;  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId SKU Reference ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skuIdbyRefIdAsync(String contentType, String accept, String refId, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = skuIdbyRefIdValidateBeforeCall(contentType, accept, refId, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for skuIdlistbyRefIdlist
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skuIdlistbyRefIdlistCall(String contentType, String accept, List<String> requestBody, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pub/sku/stockkeepingunitidsbyrefids";

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
    private okhttp3.Call skuIdlistbyRefIdlistValidateBeforeCall(String contentType, String accept, List<String> requestBody, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling skuIdlistbyRefIdlist(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling skuIdlistbyRefIdlist(Async)");
        }

        return skuIdlistbyRefIdlistCall(contentType, accept, requestBody, _callback);

    }

    /**
     * Retrieve SKU ID list by Reference ID list
     * Receives a list of Reference IDs and returns a list with the corresponding SKU IDs.    &gt;⚠️ The list of Reference IDs in the request body cannot have repeated Reference IDs, or the API will return an error 500.     ## Request body example    &#x60;&#x60;&#x60;json  [      \&quot;123\&quot;,      \&quot;D25133K-B2\&quot;,      \&quot;14-556\&quot;,      \&quot;DCF880L2-BR\&quot;  ]  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;123\&quot;: \&quot;435\&quot;,      \&quot;D25133K-B2\&quot;: \&quot;4351\&quot;,      \&quot;14-556\&quot;: \&quot;3155\&quot;,      \&quot;DCF880L2-BR\&quot;: \&quot;4500\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody  (optional)
     * @return Map&lt;String, String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public Map<String, String> skuIdlistbyRefIdlist(String contentType, String accept, List<String> requestBody) throws ApiException {
        ApiResponse<Map<String, String>> localVarResp = skuIdlistbyRefIdlistWithHttpInfo(contentType, accept, requestBody);
        return localVarResp.getData();
    }

    /**
     * Retrieve SKU ID list by Reference ID list
     * Receives a list of Reference IDs and returns a list with the corresponding SKU IDs.    &gt;⚠️ The list of Reference IDs in the request body cannot have repeated Reference IDs, or the API will return an error 500.     ## Request body example    &#x60;&#x60;&#x60;json  [      \&quot;123\&quot;,      \&quot;D25133K-B2\&quot;,      \&quot;14-556\&quot;,      \&quot;DCF880L2-BR\&quot;  ]  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;123\&quot;: \&quot;435\&quot;,      \&quot;D25133K-B2\&quot;: \&quot;4351\&quot;,      \&quot;14-556\&quot;: \&quot;3155\&quot;,      \&quot;DCF880L2-BR\&quot;: \&quot;4500\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody  (optional)
     * @return ApiResponse&lt;Map&lt;String, String&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Map<String, String>> skuIdlistbyRefIdlistWithHttpInfo(String contentType, String accept, List<String> requestBody) throws ApiException {
        okhttp3.Call localVarCall = skuIdlistbyRefIdlistValidateBeforeCall(contentType, accept, requestBody, null);
        Type localVarReturnType = new TypeToken<Map<String, String>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve SKU ID list by Reference ID list (asynchronously)
     * Receives a list of Reference IDs and returns a list with the corresponding SKU IDs.    &gt;⚠️ The list of Reference IDs in the request body cannot have repeated Reference IDs, or the API will return an error 500.     ## Request body example    &#x60;&#x60;&#x60;json  [      \&quot;123\&quot;,      \&quot;D25133K-B2\&quot;,      \&quot;14-556\&quot;,      \&quot;DCF880L2-BR\&quot;  ]  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;123\&quot;: \&quot;435\&quot;,      \&quot;D25133K-B2\&quot;: \&quot;4351\&quot;,      \&quot;14-556\&quot;: \&quot;3155\&quot;,      \&quot;DCF880L2-BR\&quot;: \&quot;4500\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skuIdlistbyRefIdlistAsync(String contentType, String accept, List<String> requestBody, final ApiCallback<Map<String, String>> _callback) throws ApiException {

        okhttp3.Call localVarCall = skuIdlistbyRefIdlistValidateBeforeCall(contentType, accept, requestBody, _callback);
        Type localVarReturnType = new TypeToken<Map<String, String>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for skubyAlternateId
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param alternateId Product EAN or RefId. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skubyAlternateIdCall(String contentType, String accept, Integer alternateId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/stockkeepingunitbyalternateId/{alternateId}"
            .replace("{" + "alternateId" + "}", localVarApiClient.escapeString(alternateId.toString()));

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
    private okhttp3.Call skubyAlternateIdValidateBeforeCall(String contentType, String accept, Integer alternateId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling skubyAlternateId(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling skubyAlternateId(Async)");
        }

        // verify the required parameter 'alternateId' is set
        if (alternateId == null) {
            throw new ApiException("Missing the required parameter 'alternateId' when calling skubyAlternateId(Async)");
        }

        return skubyAlternateIdCall(contentType, accept, alternateId, _callback);

    }

    /**
     * Get SKU by Alternate ID
     * Retrieves an SKU by its Alternate ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118450,      \&quot;ProductId\&quot;: 2,      \&quot;NameComplete\&quot;: \&quot;Caixa de Areia Azul Petmate sku test\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Caixa de Areia Azul Petmate\&quot;,      \&quot;ProductDescription\&quot;: \&quot;\&quot;,      \&quot;ProductRefId\&quot;: \&quot;\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;SkuName\&quot;: \&quot;sku test\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451-55-55/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/caixa-de-areia-azul-petmate/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000005\&quot;,      \&quot;BrandName\&quot;: \&quot;Petmate\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 0.2083,          \&quot;height\&quot;: 10.0000,          \&quot;length\&quot;: 10.0000,          \&quot;weight\&quot;: 10.0000,          \&quot;width\&quot;: 10.0000      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 0.000,          \&quot;realHeight\&quot;: 0.0,          \&quot;realLength\&quot;: 0.0,          \&quot;realWeight\&quot;: 0.0,          \&quot;realWidth\&quot;: 0.0      },      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/3/15/\&quot;,          \&quot;/3/\&quot;,          \&quot;/1/\&quot;      ],      \&quot;Attachments\&quot;: [],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 310118450,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;310118450\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0.0,              \&quot;ProductCommissionPercentage\&quot;: 0.0          }      ],      \&quot;SalesChannels\&quot;: [          1,          3      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,              \&quot;ImageName\&quot;: null,              \&quot;FileId\&quot;: 155451          }      ],      \&quot;Videos\&quot;: [],      \&quot;SkuSpecifications\&quot;: [],      \&quot;ProductSpecifications\&quot;: [],      \&quot;ProductClustersIds\&quot;: \&quot;151,158\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 1,          \&quot;158\&quot;: 2      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/3/15/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: true,      \&quot;ProductGlobalCategoryId\&quot;: 5000,      \&quot;ProductCategories\&quot;: {          \&quot;15\&quot;: \&quot;Caixa de Areia\&quot;,          \&quot;3\&quot;: \&quot;Higiene\&quot;,          \&quot;1\&quot;: \&quot;Alimentação\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 0.0,      \&quot;AlternateIds\&quot;: {          \&quot;RefId\&quot;: \&quot;1\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;1\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: null,      \&quot;KeyWords\&quot;: \&quot;\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00Z\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param alternateId Product EAN or RefId. (required)
     * @return GetSKUAltID
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public GetSKUAltID skubyAlternateId(String contentType, String accept, Integer alternateId) throws ApiException {
        ApiResponse<GetSKUAltID> localVarResp = skubyAlternateIdWithHttpInfo(contentType, accept, alternateId);
        return localVarResp.getData();
    }

    /**
     * Get SKU by Alternate ID
     * Retrieves an SKU by its Alternate ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118450,      \&quot;ProductId\&quot;: 2,      \&quot;NameComplete\&quot;: \&quot;Caixa de Areia Azul Petmate sku test\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Caixa de Areia Azul Petmate\&quot;,      \&quot;ProductDescription\&quot;: \&quot;\&quot;,      \&quot;ProductRefId\&quot;: \&quot;\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;SkuName\&quot;: \&quot;sku test\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451-55-55/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/caixa-de-areia-azul-petmate/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000005\&quot;,      \&quot;BrandName\&quot;: \&quot;Petmate\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 0.2083,          \&quot;height\&quot;: 10.0000,          \&quot;length\&quot;: 10.0000,          \&quot;weight\&quot;: 10.0000,          \&quot;width\&quot;: 10.0000      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 0.000,          \&quot;realHeight\&quot;: 0.0,          \&quot;realLength\&quot;: 0.0,          \&quot;realWeight\&quot;: 0.0,          \&quot;realWidth\&quot;: 0.0      },      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/3/15/\&quot;,          \&quot;/3/\&quot;,          \&quot;/1/\&quot;      ],      \&quot;Attachments\&quot;: [],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 310118450,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;310118450\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0.0,              \&quot;ProductCommissionPercentage\&quot;: 0.0          }      ],      \&quot;SalesChannels\&quot;: [          1,          3      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,              \&quot;ImageName\&quot;: null,              \&quot;FileId\&quot;: 155451          }      ],      \&quot;Videos\&quot;: [],      \&quot;SkuSpecifications\&quot;: [],      \&quot;ProductSpecifications\&quot;: [],      \&quot;ProductClustersIds\&quot;: \&quot;151,158\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 1,          \&quot;158\&quot;: 2      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/3/15/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: true,      \&quot;ProductGlobalCategoryId\&quot;: 5000,      \&quot;ProductCategories\&quot;: {          \&quot;15\&quot;: \&quot;Caixa de Areia\&quot;,          \&quot;3\&quot;: \&quot;Higiene\&quot;,          \&quot;1\&quot;: \&quot;Alimentação\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 0.0,      \&quot;AlternateIds\&quot;: {          \&quot;RefId\&quot;: \&quot;1\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;1\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: null,      \&quot;KeyWords\&quot;: \&quot;\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00Z\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param alternateId Product EAN or RefId. (required)
     * @return ApiResponse&lt;GetSKUAltID&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetSKUAltID> skubyAlternateIdWithHttpInfo(String contentType, String accept, Integer alternateId) throws ApiException {
        okhttp3.Call localVarCall = skubyAlternateIdValidateBeforeCall(contentType, accept, alternateId, null);
        Type localVarReturnType = new TypeToken<GetSKUAltID>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU by Alternate ID (asynchronously)
     * Retrieves an SKU by its Alternate ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118450,      \&quot;ProductId\&quot;: 2,      \&quot;NameComplete\&quot;: \&quot;Caixa de Areia Azul Petmate sku test\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Caixa de Areia Azul Petmate\&quot;,      \&quot;ProductDescription\&quot;: \&quot;\&quot;,      \&quot;ProductRefId\&quot;: \&quot;\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;SkuName\&quot;: \&quot;sku test\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451-55-55/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/caixa-de-areia-azul-petmate/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000005\&quot;,      \&quot;BrandName\&quot;: \&quot;Petmate\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 0.2083,          \&quot;height\&quot;: 10.0000,          \&quot;length\&quot;: 10.0000,          \&quot;weight\&quot;: 10.0000,          \&quot;width\&quot;: 10.0000      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 0.000,          \&quot;realHeight\&quot;: 0.0,          \&quot;realLength\&quot;: 0.0,          \&quot;realWeight\&quot;: 0.0,          \&quot;realWidth\&quot;: 0.0      },      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/3/15/\&quot;,          \&quot;/3/\&quot;,          \&quot;/1/\&quot;      ],      \&quot;Attachments\&quot;: [],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 310118450,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;310118450\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0.0,              \&quot;ProductCommissionPercentage\&quot;: 0.0          }      ],      \&quot;SalesChannels\&quot;: [          1,          3      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,              \&quot;ImageName\&quot;: null,              \&quot;FileId\&quot;: 155451          }      ],      \&quot;Videos\&quot;: [],      \&quot;SkuSpecifications\&quot;: [],      \&quot;ProductSpecifications\&quot;: [],      \&quot;ProductClustersIds\&quot;: \&quot;151,158\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 1,          \&quot;158\&quot;: 2      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/3/15/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: true,      \&quot;ProductGlobalCategoryId\&quot;: 5000,      \&quot;ProductCategories\&quot;: {          \&quot;15\&quot;: \&quot;Caixa de Areia\&quot;,          \&quot;3\&quot;: \&quot;Higiene\&quot;,          \&quot;1\&quot;: \&quot;Alimentação\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 0.0,      \&quot;AlternateIds\&quot;: {          \&quot;RefId\&quot;: \&quot;1\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;1\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: null,      \&quot;KeyWords\&quot;: \&quot;\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00Z\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param alternateId Product EAN or RefId. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skubyAlternateIdAsync(String contentType, String accept, Integer alternateId, final ApiCallback<GetSKUAltID> _callback) throws ApiException {

        okhttp3.Call localVarCall = skubyAlternateIdValidateBeforeCall(contentType, accept, alternateId, _callback);
        Type localVarReturnType = new TypeToken<GetSKUAltID>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for skulistbyProductId
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skulistbyProductIdCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/stockkeepingunitByProductId/{productId}"
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
    private okhttp3.Call skulistbyProductIdValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling skulistbyProductId(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling skulistbyProductId(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling skulistbyProductId(Async)");
        }

        return skulistbyProductIdCall(contentType, accept, productId, _callback);

    }

    /**
     * Get SKU list by Product ID
     * Retrieves a list with the SKUs related to a product by the product&#39;s ID.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;IsPersisted\&quot;: true,          \&quot;IsRemoved\&quot;: false,          \&quot;Id\&quot;: 2000035,          \&quot;ProductId\&quot;: 2000024,          \&quot;IsActive\&quot;: true,          \&quot;Name\&quot;: \&quot;33 - Preto\&quot;,          \&quot;Height\&quot;: 8,          \&quot;RealHeight\&quot;: null,          \&quot;Width\&quot;: 15,          \&quot;RealWidth\&quot;: null,          \&quot;Length\&quot;: 8,          \&quot;RealLength\&quot;: null,          \&quot;WeightKg\&quot;: 340,          \&quot;RealWeightKg\&quot;: null,          \&quot;ModalId\&quot;: 1,          \&quot;RefId\&quot;: \&quot;\&quot;,          \&quot;CubicWeight\&quot;: 0.2,          \&quot;IsKit\&quot;: false,          \&quot;IsDynamicKit\&quot;: null,          \&quot;InternalNote\&quot;: null,          \&quot;DateUpdated\&quot;: \&quot;2015-11-06T19:10:00\&quot;,          \&quot;RewardValue\&quot;: 0.01,          \&quot;CommercialConditionId\&quot;: 1,          \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,          \&quot;FlagKitItensSellApart\&quot;: false,          \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,          \&quot;ReferenceStockKeepingUnitId\&quot;: null,          \&quot;Position\&quot;: 0,          \&quot;EditionSkuId\&quot;: null,          \&quot;ApprovedAdminId\&quot;: 123,          \&quot;EditionAdminId\&quot;: 123,          \&quot;ActivateIfPossible\&quot;: true,          \&quot;SupplierCode\&quot;: null,          \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,          \&quot;UnitMultiplier\&quot;: 2.0000,          \&quot;IsInventoried\&quot;: null,          \&quot;IsTransported\&quot;: null,          \&quot;IsGiftCardRecharge\&quot;: null,          \&quot;ModalType\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return List&lt;SkulistbyProductId&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public List<SkulistbyProductId> skulistbyProductId(String contentType, String accept, Integer productId) throws ApiException {
        ApiResponse<List<SkulistbyProductId>> localVarResp = skulistbyProductIdWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get SKU list by Product ID
     * Retrieves a list with the SKUs related to a product by the product&#39;s ID.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;IsPersisted\&quot;: true,          \&quot;IsRemoved\&quot;: false,          \&quot;Id\&quot;: 2000035,          \&quot;ProductId\&quot;: 2000024,          \&quot;IsActive\&quot;: true,          \&quot;Name\&quot;: \&quot;33 - Preto\&quot;,          \&quot;Height\&quot;: 8,          \&quot;RealHeight\&quot;: null,          \&quot;Width\&quot;: 15,          \&quot;RealWidth\&quot;: null,          \&quot;Length\&quot;: 8,          \&quot;RealLength\&quot;: null,          \&quot;WeightKg\&quot;: 340,          \&quot;RealWeightKg\&quot;: null,          \&quot;ModalId\&quot;: 1,          \&quot;RefId\&quot;: \&quot;\&quot;,          \&quot;CubicWeight\&quot;: 0.2,          \&quot;IsKit\&quot;: false,          \&quot;IsDynamicKit\&quot;: null,          \&quot;InternalNote\&quot;: null,          \&quot;DateUpdated\&quot;: \&quot;2015-11-06T19:10:00\&quot;,          \&quot;RewardValue\&quot;: 0.01,          \&quot;CommercialConditionId\&quot;: 1,          \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,          \&quot;FlagKitItensSellApart\&quot;: false,          \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,          \&quot;ReferenceStockKeepingUnitId\&quot;: null,          \&quot;Position\&quot;: 0,          \&quot;EditionSkuId\&quot;: null,          \&quot;ApprovedAdminId\&quot;: 123,          \&quot;EditionAdminId\&quot;: 123,          \&quot;ActivateIfPossible\&quot;: true,          \&quot;SupplierCode\&quot;: null,          \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,          \&quot;UnitMultiplier\&quot;: 2.0000,          \&quot;IsInventoried\&quot;: null,          \&quot;IsTransported\&quot;: null,          \&quot;IsGiftCardRecharge\&quot;: null,          \&quot;ModalType\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;SkulistbyProductId&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<List<SkulistbyProductId>> skulistbyProductIdWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = skulistbyProductIdValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<List<SkulistbyProductId>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU list by Product ID (asynchronously)
     * Retrieves a list with the SKUs related to a product by the product&#39;s ID.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;IsPersisted\&quot;: true,          \&quot;IsRemoved\&quot;: false,          \&quot;Id\&quot;: 2000035,          \&quot;ProductId\&quot;: 2000024,          \&quot;IsActive\&quot;: true,          \&quot;Name\&quot;: \&quot;33 - Preto\&quot;,          \&quot;Height\&quot;: 8,          \&quot;RealHeight\&quot;: null,          \&quot;Width\&quot;: 15,          \&quot;RealWidth\&quot;: null,          \&quot;Length\&quot;: 8,          \&quot;RealLength\&quot;: null,          \&quot;WeightKg\&quot;: 340,          \&quot;RealWeightKg\&quot;: null,          \&quot;ModalId\&quot;: 1,          \&quot;RefId\&quot;: \&quot;\&quot;,          \&quot;CubicWeight\&quot;: 0.2,          \&quot;IsKit\&quot;: false,          \&quot;IsDynamicKit\&quot;: null,          \&quot;InternalNote\&quot;: null,          \&quot;DateUpdated\&quot;: \&quot;2015-11-06T19:10:00\&quot;,          \&quot;RewardValue\&quot;: 0.01,          \&quot;CommercialConditionId\&quot;: 1,          \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,          \&quot;FlagKitItensSellApart\&quot;: false,          \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,          \&quot;ReferenceStockKeepingUnitId\&quot;: null,          \&quot;Position\&quot;: 0,          \&quot;EditionSkuId\&quot;: null,          \&quot;ApprovedAdminId\&quot;: 123,          \&quot;EditionAdminId\&quot;: 123,          \&quot;ActivateIfPossible\&quot;: true,          \&quot;SupplierCode\&quot;: null,          \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,          \&quot;UnitMultiplier\&quot;: 2.0000,          \&quot;IsInventoried\&quot;: null,          \&quot;IsTransported\&quot;: null,          \&quot;IsGiftCardRecharge\&quot;: null,          \&quot;ModalType\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * Vary -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Cache-Status-Janus-Edge -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call skulistbyProductIdAsync(String contentType, String accept, Integer productId, final ApiCallback<List<SkulistbyProductId>> _callback) throws ApiException {

        okhttp3.Call localVarCall = skulistbyProductIdValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<List<SkulistbyProductId>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
