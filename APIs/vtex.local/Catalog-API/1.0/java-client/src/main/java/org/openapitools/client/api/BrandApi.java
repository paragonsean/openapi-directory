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


import org.openapitools.client.model.BrandCreateUpdate;
import org.openapitools.client.model.BrandGet;
import org.openapitools.client.model.BrandListPerPage200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BrandApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BrandApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BrandApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtBrandBrandIdDelete
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
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
    public okhttp3.Call apiCatalogPvtBrandBrandIdDeleteCall(String brandId, String contentType, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/brand/{brandId}"
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
    private okhttp3.Call apiCatalogPvtBrandBrandIdDeleteValidateBeforeCall(String brandId, String contentType, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'brandId' is set
        if (brandId == null) {
            throw new ApiException("Missing the required parameter 'brandId' when calling apiCatalogPvtBrandBrandIdDelete(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandBrandIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtBrandBrandIdDelete(Async)");
        }

        return apiCatalogPvtBrandBrandIdDeleteCall(brandId, contentType, accept, _callback);

    }

    /**
     * Delete Brand
     * Deletes an existing Brand.
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtBrandBrandIdDelete(String brandId, String contentType, String accept) throws ApiException {
        apiCatalogPvtBrandBrandIdDeleteWithHttpInfo(brandId, contentType, accept);
    }

    /**
     * Delete Brand
     * Deletes an existing Brand.
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtBrandBrandIdDeleteWithHttpInfo(String brandId, String contentType, String accept) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtBrandBrandIdDeleteValidateBeforeCall(brandId, contentType, accept, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete Brand (asynchronously)
     * Deletes an existing Brand.
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
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
    public okhttp3.Call apiCatalogPvtBrandBrandIdDeleteAsync(String brandId, String contentType, String accept, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtBrandBrandIdDeleteValidateBeforeCall(brandId, contentType, accept, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtBrandBrandIdGet
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtBrandBrandIdGetCall(String contentType, String accept, String brandId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/brand/{brandId}"
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
    private okhttp3.Call apiCatalogPvtBrandBrandIdGetValidateBeforeCall(String contentType, String accept, String brandId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandBrandIdGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtBrandBrandIdGet(Async)");
        }

        // verify the required parameter 'brandId' is set
        if (brandId == null) {
            throw new ApiException("Missing the required parameter 'brandId' when calling apiCatalogPvtBrandBrandIdGet(Async)");
        }

        return apiCatalogPvtBrandBrandIdGetCall(contentType, accept, brandId, _callback);

    }

    /**
     * Get Brand and context
     * Retrieves information about a specific Brand and its context.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @return BrandCreateUpdate
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BrandCreateUpdate apiCatalogPvtBrandBrandIdGet(String contentType, String accept, String brandId) throws ApiException {
        ApiResponse<BrandCreateUpdate> localVarResp = apiCatalogPvtBrandBrandIdGetWithHttpInfo(contentType, accept, brandId);
        return localVarResp.getData();
    }

    /**
     * Get Brand and context
     * Retrieves information about a specific Brand and its context.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @return ApiResponse&lt;BrandCreateUpdate&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BrandCreateUpdate> apiCatalogPvtBrandBrandIdGetWithHttpInfo(String contentType, String accept, String brandId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtBrandBrandIdGetValidateBeforeCall(contentType, accept, brandId, null);
        Type localVarReturnType = new TypeToken<BrandCreateUpdate>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Brand and context (asynchronously)
     * Retrieves information about a specific Brand and its context.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtBrandBrandIdGetAsync(String contentType, String accept, String brandId, final ApiCallback<BrandCreateUpdate> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtBrandBrandIdGetValidateBeforeCall(contentType, accept, brandId, _callback);
        Type localVarReturnType = new TypeToken<BrandCreateUpdate>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtBrandBrandIdPut
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtBrandBrandIdPutCall(String brandId, String contentType, String accept, BrandCreateUpdate brandCreateUpdate, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = brandCreateUpdate;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/brand/{brandId}"
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
    private okhttp3.Call apiCatalogPvtBrandBrandIdPutValidateBeforeCall(String brandId, String contentType, String accept, BrandCreateUpdate brandCreateUpdate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'brandId' is set
        if (brandId == null) {
            throw new ApiException("Missing the required parameter 'brandId' when calling apiCatalogPvtBrandBrandIdPut(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandBrandIdPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtBrandBrandIdPut(Async)");
        }

        return apiCatalogPvtBrandBrandIdPutCall(brandId, contentType, accept, brandCreateUpdate, _callback);

    }

    /**
     * Update Brand
     * Updates a previously existing Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate  (optional)
     * @return BrandCreateUpdate
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BrandCreateUpdate apiCatalogPvtBrandBrandIdPut(String brandId, String contentType, String accept, BrandCreateUpdate brandCreateUpdate) throws ApiException {
        ApiResponse<BrandCreateUpdate> localVarResp = apiCatalogPvtBrandBrandIdPutWithHttpInfo(brandId, contentType, accept, brandCreateUpdate);
        return localVarResp.getData();
    }

    /**
     * Update Brand
     * Updates a previously existing Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate  (optional)
     * @return ApiResponse&lt;BrandCreateUpdate&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BrandCreateUpdate> apiCatalogPvtBrandBrandIdPutWithHttpInfo(String brandId, String contentType, String accept, BrandCreateUpdate brandCreateUpdate) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtBrandBrandIdPutValidateBeforeCall(brandId, contentType, accept, brandCreateUpdate, null);
        Type localVarReturnType = new TypeToken<BrandCreateUpdate>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update Brand (asynchronously)
     * Updates a previously existing Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param brandId Brand’s unique numerical identifier. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtBrandBrandIdPutAsync(String brandId, String contentType, String accept, BrandCreateUpdate brandCreateUpdate, final ApiCallback<BrandCreateUpdate> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtBrandBrandIdPutValidateBeforeCall(brandId, contentType, accept, brandCreateUpdate, _callback);
        Type localVarReturnType = new TypeToken<BrandCreateUpdate>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtBrandPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate Request body. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtBrandPostCall(String contentType, String accept, BrandCreateUpdate brandCreateUpdate, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = brandCreateUpdate;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/brand";

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
    private okhttp3.Call apiCatalogPvtBrandPostValidateBeforeCall(String contentType, String accept, BrandCreateUpdate brandCreateUpdate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtBrandPost(Async)");
        }

        return apiCatalogPvtBrandPostCall(contentType, accept, brandCreateUpdate, _callback);

    }

    /**
     * Create Brand
     * Creates a new Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate Request body. (optional)
     * @return BrandCreateUpdate
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BrandCreateUpdate apiCatalogPvtBrandPost(String contentType, String accept, BrandCreateUpdate brandCreateUpdate) throws ApiException {
        ApiResponse<BrandCreateUpdate> localVarResp = apiCatalogPvtBrandPostWithHttpInfo(contentType, accept, brandCreateUpdate);
        return localVarResp.getData();
    }

    /**
     * Create Brand
     * Creates a new Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate Request body. (optional)
     * @return ApiResponse&lt;BrandCreateUpdate&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BrandCreateUpdate> apiCatalogPvtBrandPostWithHttpInfo(String contentType, String accept, BrandCreateUpdate brandCreateUpdate) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtBrandPostValidateBeforeCall(contentType, accept, brandCreateUpdate, null);
        Type localVarReturnType = new TypeToken<BrandCreateUpdate>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create Brand (asynchronously)
     * Creates a new Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandCreateUpdate Request body. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtBrandPostAsync(String contentType, String accept, BrandCreateUpdate brandCreateUpdate, final ApiCallback<BrandCreateUpdate> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtBrandPostValidateBeforeCall(contentType, accept, brandCreateUpdate, _callback);
        Type localVarReturnType = new TypeToken<BrandCreateUpdate>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for brand
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call brandCall(String contentType, String accept, String brandId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/brand/{brandId}"
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
    private okhttp3.Call brandValidateBeforeCall(String contentType, String accept, String brandId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling brand(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling brand(Async)");
        }

        // verify the required parameter 'brandId' is set
        if (brandId == null) {
            throw new ApiException("Missing the required parameter 'brandId' when calling brand(Async)");
        }

        return brandCall(contentType, accept, brandId, _callback);

    }

    /**
     * Get Brand
     * Retrieves a specific Brand by its ID.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: 7000000,    \&quot;name\&quot;: \&quot;Pedigree\&quot;,    \&quot;isActive\&quot;: true,    \&quot;title\&quot;: \&quot;Pedigree\&quot;,    \&quot;metaTagDescription\&quot;: \&quot;Pedigree\&quot;,    \&quot;imageUrl\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @return BrandGet
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BrandGet brand(String contentType, String accept, String brandId) throws ApiException {
        ApiResponse<BrandGet> localVarResp = brandWithHttpInfo(contentType, accept, brandId);
        return localVarResp.getData();
    }

    /**
     * Get Brand
     * Retrieves a specific Brand by its ID.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: 7000000,    \&quot;name\&quot;: \&quot;Pedigree\&quot;,    \&quot;isActive\&quot;: true,    \&quot;title\&quot;: \&quot;Pedigree\&quot;,    \&quot;metaTagDescription\&quot;: \&quot;Pedigree\&quot;,    \&quot;imageUrl\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @return ApiResponse&lt;BrandGet&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BrandGet> brandWithHttpInfo(String contentType, String accept, String brandId) throws ApiException {
        okhttp3.Call localVarCall = brandValidateBeforeCall(contentType, accept, brandId, null);
        Type localVarReturnType = new TypeToken<BrandGet>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Brand (asynchronously)
     * Retrieves a specific Brand by its ID.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: 7000000,    \&quot;name\&quot;: \&quot;Pedigree\&quot;,    \&quot;isActive\&quot;: true,    \&quot;title\&quot;: \&quot;Pedigree\&quot;,    \&quot;metaTagDescription\&quot;: \&quot;Pedigree\&quot;,    \&quot;imageUrl\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param brandId Brand ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call brandAsync(String contentType, String accept, String brandId, final ApiCallback<BrandGet> _callback) throws ApiException {

        okhttp3.Call localVarCall = brandValidateBeforeCall(contentType, accept, brandId, _callback);
        Type localVarReturnType = new TypeToken<BrandGet>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for brandList
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
    public okhttp3.Call brandListCall(String contentType, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/brand/list";

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
    private okhttp3.Call brandListValidateBeforeCall(String contentType, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling brandList(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling brandList(Async)");
        }

        return brandListCall(contentType, accept, _callback);

    }

    /**
     * Get Brand List
     * Retrieves all Brands registered in the store&#39;s Catalog.   &gt;⚠️ This route&#39;s response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    &#x60;&#x60;&#x60;json  [    {      \&quot;id\&quot;: 9280,      \&quot;name\&quot;: \&quot;Brand\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Brand\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Brand\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000000,      \&quot;name\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000001,      \&quot;name\&quot;: \&quot;Pedigree\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Pedigree\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;\&quot;,      \&quot;imageUrl\&quot;: null    }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return List&lt;BrandGet&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<BrandGet> brandList(String contentType, String accept) throws ApiException {
        ApiResponse<List<BrandGet>> localVarResp = brandListWithHttpInfo(contentType, accept);
        return localVarResp.getData();
    }

    /**
     * Get Brand List
     * Retrieves all Brands registered in the store&#39;s Catalog.   &gt;⚠️ This route&#39;s response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    &#x60;&#x60;&#x60;json  [    {      \&quot;id\&quot;: 9280,      \&quot;name\&quot;: \&quot;Brand\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Brand\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Brand\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000000,      \&quot;name\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000001,      \&quot;name\&quot;: \&quot;Pedigree\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Pedigree\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;\&quot;,      \&quot;imageUrl\&quot;: null    }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return ApiResponse&lt;List&lt;BrandGet&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<BrandGet>> brandListWithHttpInfo(String contentType, String accept) throws ApiException {
        okhttp3.Call localVarCall = brandListValidateBeforeCall(contentType, accept, null);
        Type localVarReturnType = new TypeToken<List<BrandGet>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Brand List (asynchronously)
     * Retrieves all Brands registered in the store&#39;s Catalog.   &gt;⚠️ This route&#39;s response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    &#x60;&#x60;&#x60;json  [    {      \&quot;id\&quot;: 9280,      \&quot;name\&quot;: \&quot;Brand\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Brand\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Brand\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000000,      \&quot;name\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000001,      \&quot;name\&quot;: \&quot;Pedigree\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Pedigree\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;\&quot;,      \&quot;imageUrl\&quot;: null    }  ]  &#x60;&#x60;&#x60;
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
    public okhttp3.Call brandListAsync(String contentType, String accept, final ApiCallback<List<BrandGet>> _callback) throws ApiException {

        okhttp3.Call localVarCall = brandListValidateBeforeCall(contentType, accept, _callback);
        Type localVarReturnType = new TypeToken<List<BrandGet>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for brandListPerPage
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param pageSize Quantity of brands per page. (required)
     * @param page Page number of the brand list. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call brandListPerPageCall(String contentType, String accept, Integer pageSize, Integer page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/brand/pagedlist";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pageSize", pageSize));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
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
    private okhttp3.Call brandListPerPageValidateBeforeCall(String contentType, String accept, Integer pageSize, Integer page, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling brandListPerPage(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling brandListPerPage(Async)");
        }

        // verify the required parameter 'pageSize' is set
        if (pageSize == null) {
            throw new ApiException("Missing the required parameter 'pageSize' when calling brandListPerPage(Async)");
        }

        // verify the required parameter 'page' is set
        if (page == null) {
            throw new ApiException("Missing the required parameter 'page' when calling brandListPerPage(Async)");
        }

        return brandListPerPageCall(contentType, accept, pageSize, page, _callback);

    }

    /**
     * Get Brand List Per Page
     * Retrieves all Brands registered in the store&#39;s Catalog by page number.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;items\&quot;: [      {        \&quot;id\&quot;: 2000000,        \&quot;name\&quot;: \&quot;Farm\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Farm\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Farm\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000001,        \&quot;name\&quot;: \&quot;Adidas\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000002,        \&quot;name\&quot;: \&quot;Brastemp\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Brastemp\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Brastemp\&quot;,        \&quot;imageUrl\&quot;: null      }    ],      \&quot;paging\&quot;: {        \&quot;page\&quot;: 1,          \&quot;perPage\&quot;: 3,            \&quot;total\&quot;: 6,              \&quot;pages\&quot;: 2      }  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param pageSize Quantity of brands per page. (required)
     * @param page Page number of the brand list. (required)
     * @return BrandListPerPage200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BrandListPerPage200Response brandListPerPage(String contentType, String accept, Integer pageSize, Integer page) throws ApiException {
        ApiResponse<BrandListPerPage200Response> localVarResp = brandListPerPageWithHttpInfo(contentType, accept, pageSize, page);
        return localVarResp.getData();
    }

    /**
     * Get Brand List Per Page
     * Retrieves all Brands registered in the store&#39;s Catalog by page number.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;items\&quot;: [      {        \&quot;id\&quot;: 2000000,        \&quot;name\&quot;: \&quot;Farm\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Farm\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Farm\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000001,        \&quot;name\&quot;: \&quot;Adidas\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000002,        \&quot;name\&quot;: \&quot;Brastemp\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Brastemp\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Brastemp\&quot;,        \&quot;imageUrl\&quot;: null      }    ],      \&quot;paging\&quot;: {        \&quot;page\&quot;: 1,          \&quot;perPage\&quot;: 3,            \&quot;total\&quot;: 6,              \&quot;pages\&quot;: 2      }  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param pageSize Quantity of brands per page. (required)
     * @param page Page number of the brand list. (required)
     * @return ApiResponse&lt;BrandListPerPage200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BrandListPerPage200Response> brandListPerPageWithHttpInfo(String contentType, String accept, Integer pageSize, Integer page) throws ApiException {
        okhttp3.Call localVarCall = brandListPerPageValidateBeforeCall(contentType, accept, pageSize, page, null);
        Type localVarReturnType = new TypeToken<BrandListPerPage200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Brand List Per Page (asynchronously)
     * Retrieves all Brands registered in the store&#39;s Catalog by page number.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;items\&quot;: [      {        \&quot;id\&quot;: 2000000,        \&quot;name\&quot;: \&quot;Farm\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Farm\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Farm\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000001,        \&quot;name\&quot;: \&quot;Adidas\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000002,        \&quot;name\&quot;: \&quot;Brastemp\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Brastemp\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Brastemp\&quot;,        \&quot;imageUrl\&quot;: null      }    ],      \&quot;paging\&quot;: {        \&quot;page\&quot;: 1,          \&quot;perPage\&quot;: 3,            \&quot;total\&quot;: 6,              \&quot;pages\&quot;: 2      }  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param pageSize Quantity of brands per page. (required)
     * @param page Page number of the brand list. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call brandListPerPageAsync(String contentType, String accept, Integer pageSize, Integer page, final ApiCallback<BrandListPerPage200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = brandListPerPageValidateBeforeCall(contentType, accept, pageSize, page, _callback);
        Type localVarReturnType = new TypeToken<BrandListPerPage200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
