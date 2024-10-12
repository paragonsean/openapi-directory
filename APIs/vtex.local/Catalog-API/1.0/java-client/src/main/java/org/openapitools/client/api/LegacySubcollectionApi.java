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


import org.openapitools.client.model.ApiCatalogPvtCollectionCollectionIdPositionPostRequest;
import org.openapitools.client.model.ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner;
import org.openapitools.client.model.ApiCatalogPvtSubcollectionPost200Response;
import org.openapitools.client.model.ApiCatalogPvtSubcollectionPostRequest;
import org.openapitools.client.model.ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response;
import org.openapitools.client.model.ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response;
import org.openapitools.client.model.ApiCatalogPvtSubcollectionSubCollectionIdPutRequest;
import org.openapitools.client.model.ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response;
import org.openapitools.client.model.RequestBody10;
import org.openapitools.client.model.RequestBody11;
import org.openapitools.client.model.RequestBody12;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LegacySubcollectionApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LegacySubcollectionApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LegacySubcollectionApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtCollectionCollectionIdPositionPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @param apiCatalogPvtCollectionCollectionIdPositionPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCollectionCollectionIdPositionPostCall(String contentType, String accept, Integer collectionId, ApiCatalogPvtCollectionCollectionIdPositionPostRequest apiCatalogPvtCollectionCollectionIdPositionPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtCollectionCollectionIdPositionPostRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/collection/{collectionId}/position"
            .replace("{" + "collectionId" + "}", localVarApiClient.escapeString(collectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtCollectionCollectionIdPositionPostValidateBeforeCall(String contentType, String accept, Integer collectionId, ApiCatalogPvtCollectionCollectionIdPositionPostRequest apiCatalogPvtCollectionCollectionIdPositionPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtCollectionCollectionIdPositionPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtCollectionCollectionIdPositionPost(Async)");
        }

        // verify the required parameter 'collectionId' is set
        if (collectionId == null) {
            throw new ApiException("Missing the required parameter 'collectionId' when calling apiCatalogPvtCollectionCollectionIdPositionPost(Async)");
        }

        return apiCatalogPvtCollectionCollectionIdPositionPostCall(contentType, accept, collectionId, apiCatalogPvtCollectionCollectionIdPositionPostRequest, _callback);

    }

    /**
     * Reposition SKU on the Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {       \&quot;skuId\&quot;: 1,       \&quot;position\&quot;: 1,       \&quot;subCollectionId\&quot;: 17  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @param apiCatalogPvtCollectionCollectionIdPositionPostRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtCollectionCollectionIdPositionPost(String contentType, String accept, Integer collectionId, ApiCatalogPvtCollectionCollectionIdPositionPostRequest apiCatalogPvtCollectionCollectionIdPositionPostRequest) throws ApiException {
        apiCatalogPvtCollectionCollectionIdPositionPostWithHttpInfo(contentType, accept, collectionId, apiCatalogPvtCollectionCollectionIdPositionPostRequest);
    }

    /**
     * Reposition SKU on the Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {       \&quot;skuId\&quot;: 1,       \&quot;position\&quot;: 1,       \&quot;subCollectionId\&quot;: 17  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @param apiCatalogPvtCollectionCollectionIdPositionPostRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtCollectionCollectionIdPositionPostWithHttpInfo(String contentType, String accept, Integer collectionId, ApiCatalogPvtCollectionCollectionIdPositionPostRequest apiCatalogPvtCollectionCollectionIdPositionPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtCollectionCollectionIdPositionPostValidateBeforeCall(contentType, accept, collectionId, apiCatalogPvtCollectionCollectionIdPositionPostRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Reposition SKU on the Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {       \&quot;skuId\&quot;: 1,       \&quot;position\&quot;: 1,       \&quot;subCollectionId\&quot;: 17  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @param apiCatalogPvtCollectionCollectionIdPositionPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCollectionCollectionIdPositionPostAsync(String contentType, String accept, Integer collectionId, ApiCatalogPvtCollectionCollectionIdPositionPostRequest apiCatalogPvtCollectionCollectionIdPositionPostRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtCollectionCollectionIdPositionPostValidateBeforeCall(contentType, accept, collectionId, apiCatalogPvtCollectionCollectionIdPositionPostRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtCollectionCollectionIdSubcollectionGet
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCollectionCollectionIdSubcollectionGetCall(String contentType, String accept, Integer collectionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/collection/{collectionId}/subcollection"
            .replace("{" + "collectionId" + "}", localVarApiClient.escapeString(collectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtCollectionCollectionIdSubcollectionGetValidateBeforeCall(String contentType, String accept, Integer collectionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtCollectionCollectionIdSubcollectionGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtCollectionCollectionIdSubcollectionGet(Async)");
        }

        // verify the required parameter 'collectionId' is set
        if (collectionId == null) {
            throw new ApiException("Missing the required parameter 'collectionId' when calling apiCatalogPvtCollectionCollectionIdSubcollectionGet(Async)");
        }

        return apiCatalogPvtCollectionCollectionIdSubcollectionGetCall(contentType, accept, collectionId, _callback);

    }

    /**
     * Get Subcollection by Collection ID
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 12,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Subcollection\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: true      },      {          \&quot;Id\&quot;: 13,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Test\&quot;,          \&quot;Type\&quot;: \&quot;Exclusive\&quot;,          \&quot;PreSale\&quot;: true,          \&quot;Release\&quot;: false      },      {          \&quot;Id\&quot;: 14,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;asdfghj\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: false      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @return List&lt;ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner> apiCatalogPvtCollectionCollectionIdSubcollectionGet(String contentType, String accept, Integer collectionId) throws ApiException {
        ApiResponse<List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner>> localVarResp = apiCatalogPvtCollectionCollectionIdSubcollectionGetWithHttpInfo(contentType, accept, collectionId);
        return localVarResp.getData();
    }

    /**
     * Get Subcollection by Collection ID
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 12,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Subcollection\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: true      },      {          \&quot;Id\&quot;: 13,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Test\&quot;,          \&quot;Type\&quot;: \&quot;Exclusive\&quot;,          \&quot;PreSale\&quot;: true,          \&quot;Release\&quot;: false      },      {          \&quot;Id\&quot;: 14,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;asdfghj\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: false      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner>> apiCatalogPvtCollectionCollectionIdSubcollectionGetWithHttpInfo(String contentType, String accept, Integer collectionId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtCollectionCollectionIdSubcollectionGetValidateBeforeCall(contentType, accept, collectionId, null);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Subcollection by Collection ID (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 12,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Subcollection\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: true      },      {          \&quot;Id\&quot;: 13,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Test\&quot;,          \&quot;Type\&quot;: \&quot;Exclusive\&quot;,          \&quot;PreSale\&quot;: true,          \&quot;Release\&quot;: false      },      {          \&quot;Id\&quot;: 14,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;asdfghj\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: false      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param collectionId Collection’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtCollectionCollectionIdSubcollectionGetAsync(String contentType, String accept, Integer collectionId, final ApiCallback<List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtCollectionCollectionIdSubcollectionGetValidateBeforeCall(contentType, accept, collectionId, _callback);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtSubcollectionPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionPostCall(String contentType, String accept, ApiCatalogPvtSubcollectionPostRequest apiCatalogPvtSubcollectionPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtSubcollectionPostRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/subcollection";

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
    private okhttp3.Call apiCatalogPvtSubcollectionPostValidateBeforeCall(String contentType, String accept, ApiCatalogPvtSubcollectionPostRequest apiCatalogPvtSubcollectionPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionPost(Async)");
        }

        return apiCatalogPvtSubcollectionPostCall(contentType, accept, apiCatalogPvtSubcollectionPostRequest, _callback);

    }

    /**
     * Create Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtSubcollectionPostRequest  (optional)
     * @return ApiCatalogPvtSubcollectionPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionPost(String contentType, String accept, ApiCatalogPvtSubcollectionPostRequest apiCatalogPvtSubcollectionPostRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtSubcollectionPost200Response> localVarResp = apiCatalogPvtSubcollectionPostWithHttpInfo(contentType, accept, apiCatalogPvtSubcollectionPostRequest);
        return localVarResp.getData();
    }

    /**
     * Create Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtSubcollectionPostRequest  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtSubcollectionPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSubcollectionPost200Response> apiCatalogPvtSubcollectionPostWithHttpInfo(String contentType, String accept, ApiCatalogPvtSubcollectionPostRequest apiCatalogPvtSubcollectionPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionPostValidateBeforeCall(contentType, accept, apiCatalogPvtSubcollectionPostRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtSubcollectionPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionPostAsync(String contentType, String accept, ApiCatalogPvtSubcollectionPostRequest apiCatalogPvtSubcollectionPostRequest, final ApiCallback<ApiCatalogPvtSubcollectionPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionPostValidateBeforeCall(contentType, accept, apiCatalogPvtSubcollectionPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteCall(String contentType, String accept, Integer subCollectionId, Integer brandId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}/brand/{brandId}"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()))
            .replace("{" + "brandId" + "}", localVarApiClient.escapeString(brandId.toString()));

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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteValidateBeforeCall(String contentType, String accept, Integer subCollectionId, Integer brandId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(Async)");
        }

        // verify the required parameter 'brandId' is set
        if (brandId == null) {
            throw new ApiException("Missing the required parameter 'brandId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteCall(contentType, accept, subCollectionId, brandId, _callback);

    }

    /**
     * Delete Brand from Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param brandId Brand’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(String contentType, String accept, Integer subCollectionId, Integer brandId) throws ApiException {
        apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteWithHttpInfo(contentType, accept, subCollectionId, brandId);
    }

    /**
     * Delete Brand from Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param brandId Brand’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteWithHttpInfo(String contentType, String accept, Integer subCollectionId, Integer brandId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, brandId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete Brand from Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteAsync(String contentType, String accept, Integer subCollectionId, Integer brandId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, brandId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
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
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteCall(String contentType, String accept, Integer subCollectionId, Integer categoryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}/brand/{categoryId}"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()))
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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteValidateBeforeCall(String contentType, String accept, Integer subCollectionId, Integer categoryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(Async)");
        }

        // verify the required parameter 'categoryId' is set
        if (categoryId == null) {
            throw new ApiException("Missing the required parameter 'categoryId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteCall(contentType, accept, subCollectionId, categoryId, _callback);

    }

    /**
     * Delete Category from Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(String contentType, String accept, Integer subCollectionId, Integer categoryId) throws ApiException {
        apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteWithHttpInfo(contentType, accept, subCollectionId, categoryId);
    }

    /**
     * Delete Category from Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param categoryId Category’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteWithHttpInfo(String contentType, String accept, Integer subCollectionId, Integer categoryId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, categoryId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete Category from Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
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
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteAsync(String contentType, String accept, Integer subCollectionId, Integer categoryId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, categoryId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdBrandPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody10  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandPostCall(String contentType, String accept, Integer subCollectionId, RequestBody10 requestBody10, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = requestBody10;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}/brand"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandPostValidateBeforeCall(String contentType, String accept, Integer subCollectionId, RequestBody10 requestBody10, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandPost(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandPost(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdBrandPostCall(contentType, accept, subCollectionId, requestBody10, _callback);

    }

    /**
     * Associate Brand to Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody10  (optional)
     * @return ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response apiCatalogPvtSubcollectionSubCollectionIdBrandPost(String contentType, String accept, Integer subCollectionId, RequestBody10 requestBody10) throws ApiException {
        ApiResponse<ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response> localVarResp = apiCatalogPvtSubcollectionSubCollectionIdBrandPostWithHttpInfo(contentType, accept, subCollectionId, requestBody10);
        return localVarResp.getData();
    }

    /**
     * Associate Brand to Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody10  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response> apiCatalogPvtSubcollectionSubCollectionIdBrandPostWithHttpInfo(String contentType, String accept, Integer subCollectionId, RequestBody10 requestBody10) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdBrandPostValidateBeforeCall(contentType, accept, subCollectionId, requestBody10, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Associate Brand to Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody10  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdBrandPostAsync(String contentType, String accept, Integer subCollectionId, RequestBody10 requestBody10, final ApiCallback<ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdBrandPostValidateBeforeCall(contentType, accept, subCollectionId, requestBody10, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdCategoryPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody11  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdCategoryPostCall(String contentType, String accept, Integer subCollectionId, RequestBody11 requestBody11, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = requestBody11;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}/category"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdCategoryPostValidateBeforeCall(String contentType, String accept, Integer subCollectionId, RequestBody11 requestBody11, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdCategoryPostCall(contentType, accept, subCollectionId, requestBody11, _callback);

    }

    /**
     * Associate Category to Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody11  (optional)
     * @return ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(String contentType, String accept, Integer subCollectionId, RequestBody11 requestBody11) throws ApiException {
        ApiResponse<ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response> localVarResp = apiCatalogPvtSubcollectionSubCollectionIdCategoryPostWithHttpInfo(contentType, accept, subCollectionId, requestBody11);
        return localVarResp.getData();
    }

    /**
     * Associate Category to Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody11  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response> apiCatalogPvtSubcollectionSubCollectionIdCategoryPostWithHttpInfo(String contentType, String accept, Integer subCollectionId, RequestBody11 requestBody11) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdCategoryPostValidateBeforeCall(contentType, accept, subCollectionId, requestBody11, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Associate Category to Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody11  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdCategoryPostAsync(String contentType, String accept, Integer subCollectionId, RequestBody11 requestBody11, final ApiCallback<ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdCategoryPostValidateBeforeCall(contentType, accept, subCollectionId, requestBody11, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdDeleteCall(String contentType, String accept, Integer subCollectionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdDeleteValidateBeforeCall(String contentType, String accept, Integer subCollectionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdDelete(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdDelete(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdDeleteCall(contentType, accept, subCollectionId, _callback);

    }

    /**
     * Delete Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtSubcollectionSubCollectionIdDelete(String contentType, String accept, Integer subCollectionId) throws ApiException {
        apiCatalogPvtSubcollectionSubCollectionIdDeleteWithHttpInfo(contentType, accept, subCollectionId);
    }

    /**
     * Delete Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtSubcollectionSubCollectionIdDeleteWithHttpInfo(String contentType, String accept, Integer subCollectionId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdDeleteAsync(String contentType, String accept, Integer subCollectionId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdGet
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdGetCall(String contentType, String accept, Integer subCollectionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdGetValidateBeforeCall(String contentType, String accept, Integer subCollectionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdGet(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdGet(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdGetCall(contentType, accept, subCollectionId, _callback);

    }

    /**
     * Get Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @return ApiCatalogPvtSubcollectionPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionSubCollectionIdGet(String contentType, String accept, Integer subCollectionId) throws ApiException {
        ApiResponse<ApiCatalogPvtSubcollectionPost200Response> localVarResp = apiCatalogPvtSubcollectionSubCollectionIdGetWithHttpInfo(contentType, accept, subCollectionId);
        return localVarResp.getData();
    }

    /**
     * Get Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @return ApiResponse&lt;ApiCatalogPvtSubcollectionPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSubcollectionPost200Response> apiCatalogPvtSubcollectionSubCollectionIdGetWithHttpInfo(String contentType, String accept, Integer subCollectionId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdGetValidateBeforeCall(contentType, accept, subCollectionId, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdGetAsync(String contentType, String accept, Integer subCollectionId, final ApiCallback<ApiCatalogPvtSubcollectionPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdGetValidateBeforeCall(contentType, accept, subCollectionId, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdPut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param apiCatalogPvtSubcollectionSubCollectionIdPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdPutCall(String contentType, String accept, Integer subCollectionId, ApiCatalogPvtSubcollectionSubCollectionIdPutRequest apiCatalogPvtSubcollectionSubCollectionIdPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtSubcollectionSubCollectionIdPutRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdPutValidateBeforeCall(String contentType, String accept, Integer subCollectionId, ApiCatalogPvtSubcollectionSubCollectionIdPutRequest apiCatalogPvtSubcollectionSubCollectionIdPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdPut(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdPut(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdPutCall(contentType, accept, subCollectionId, apiCatalogPvtSubcollectionSubCollectionIdPutRequest, _callback);

    }

    /**
     * Update Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param apiCatalogPvtSubcollectionSubCollectionIdPutRequest  (optional)
     * @return ApiCatalogPvtSubcollectionPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionSubCollectionIdPut(String contentType, String accept, Integer subCollectionId, ApiCatalogPvtSubcollectionSubCollectionIdPutRequest apiCatalogPvtSubcollectionSubCollectionIdPutRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtSubcollectionPost200Response> localVarResp = apiCatalogPvtSubcollectionSubCollectionIdPutWithHttpInfo(contentType, accept, subCollectionId, apiCatalogPvtSubcollectionSubCollectionIdPutRequest);
        return localVarResp.getData();
    }

    /**
     * Update Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param apiCatalogPvtSubcollectionSubCollectionIdPutRequest  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtSubcollectionPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSubcollectionPost200Response> apiCatalogPvtSubcollectionSubCollectionIdPutWithHttpInfo(String contentType, String accept, Integer subCollectionId, ApiCatalogPvtSubcollectionSubCollectionIdPutRequest apiCatalogPvtSubcollectionSubCollectionIdPutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdPutValidateBeforeCall(contentType, accept, subCollectionId, apiCatalogPvtSubcollectionSubCollectionIdPutRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param apiCatalogPvtSubcollectionSubCollectionIdPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdPutAsync(String contentType, String accept, Integer subCollectionId, ApiCatalogPvtSubcollectionSubCollectionIdPutRequest apiCatalogPvtSubcollectionSubCollectionIdPutRequest, final ApiCallback<ApiCatalogPvtSubcollectionPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdPutValidateBeforeCall(contentType, accept, subCollectionId, apiCatalogPvtSubcollectionSubCollectionIdPutRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody12  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostCall(String contentType, String accept, Integer subCollectionId, RequestBody12 requestBody12, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = requestBody12;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()));

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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostValidateBeforeCall(String contentType, String accept, Integer subCollectionId, RequestBody12 requestBody12, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostCall(contentType, accept, subCollectionId, requestBody12, _callback);

    }

    /**
     * Add SKU to Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody12  (optional)
     * @return ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(String contentType, String accept, Integer subCollectionId, RequestBody12 requestBody12) throws ApiException {
        ApiResponse<ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response> localVarResp = apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostWithHttpInfo(contentType, accept, subCollectionId, requestBody12);
        return localVarResp.getData();
    }

    /**
     * Add SKU to Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody12  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response> apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostWithHttpInfo(String contentType, String accept, Integer subCollectionId, RequestBody12 requestBody12) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostValidateBeforeCall(contentType, accept, subCollectionId, requestBody12, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add SKU to Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param requestBody12  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostAsync(String contentType, String accept, Integer subCollectionId, RequestBody12 requestBody12, final ApiCallback<ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostValidateBeforeCall(contentType, accept, subCollectionId, requestBody12, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
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
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteCall(String contentType, String accept, Integer subCollectionId, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit/{skuId}"
            .replace("{" + "subCollectionId" + "}", localVarApiClient.escapeString(subCollectionId.toString()))
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
    private okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteValidateBeforeCall(String contentType, String accept, Integer subCollectionId, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(Async)");
        }

        // verify the required parameter 'subCollectionId' is set
        if (subCollectionId == null) {
            throw new ApiException("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(Async)");
        }

        return apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteCall(contentType, accept, subCollectionId, skuId, _callback);

    }

    /**
     * Delete SKU from Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(String contentType, String accept, Integer subCollectionId, Integer skuId) throws ApiException {
        apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteWithHttpInfo(contentType, accept, subCollectionId, skuId);
    }

    /**
     * Delete SKU from Subcollection
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteWithHttpInfo(String contentType, String accept, Integer subCollectionId, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, skuId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete SKU from Subcollection (asynchronously)
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). (required)
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
    public okhttp3.Call apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteAsync(String contentType, String accept, Integer subCollectionId, Integer skuId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteValidateBeforeCall(contentType, accept, subCollectionId, skuId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
