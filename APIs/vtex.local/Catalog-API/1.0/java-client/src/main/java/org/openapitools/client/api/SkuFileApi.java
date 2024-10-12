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


import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response;
import java.io.File;
import org.openapitools.client.model.SKUFileURL;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SkuFileApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SkuFileApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SkuFileApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuIdfrom __Origin__ SKU’s unique numerical identifier. (required)
     * @param skuIdto __Target__ SKU’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutCall(String contentType, String accept, Integer skuIdfrom, Integer skuIdto, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/copy/{skuIdfrom}/{skuIdto}/file/"
            .replace("{" + "skuIdfrom" + "}", localVarApiClient.escapeString(skuIdfrom.toString()))
            .replace("{" + "skuIdto" + "}", localVarApiClient.escapeString(skuIdto.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutValidateBeforeCall(String contentType, String accept, Integer skuIdfrom, Integer skuIdto, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(Async)");
        }

        // verify the required parameter 'skuIdfrom' is set
        if (skuIdfrom == null) {
            throw new ApiException("Missing the required parameter 'skuIdfrom' when calling apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(Async)");
        }

        // verify the required parameter 'skuIdto' is set
        if (skuIdto == null) {
            throw new ApiException("Missing the required parameter 'skuIdto' when calling apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(Async)");
        }

        return apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutCall(contentType, accept, skuIdfrom, skuIdto, _callback);

    }

    /**
     * Copy Files from an SKU to another SKU
     * Copy all existing files from an SKU to another SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1964,          \&quot;ArchiveId\&quot;: 155404,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;\&quot;      },      {          \&quot;Id\&quot;: 1965,          \&quot;ArchiveId\&quot;: 155429,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuIdfrom __Origin__ SKU’s unique numerical identifier. (required)
     * @param skuIdto __Target__ SKU’s unique numerical identifier. (required)
     * @return List&lt;ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner> apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(String contentType, String accept, Integer skuIdfrom, Integer skuIdto) throws ApiException {
        ApiResponse<List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner>> localVarResp = apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutWithHttpInfo(contentType, accept, skuIdfrom, skuIdto);
        return localVarResp.getData();
    }

    /**
     * Copy Files from an SKU to another SKU
     * Copy all existing files from an SKU to another SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1964,          \&quot;ArchiveId\&quot;: 155404,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;\&quot;      },      {          \&quot;Id\&quot;: 1965,          \&quot;ArchiveId\&quot;: 155429,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuIdfrom __Origin__ SKU’s unique numerical identifier. (required)
     * @param skuIdto __Target__ SKU’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner>> apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutWithHttpInfo(String contentType, String accept, Integer skuIdfrom, Integer skuIdto) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutValidateBeforeCall(contentType, accept, skuIdfrom, skuIdto, null);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Copy Files from an SKU to another SKU (asynchronously)
     * Copy all existing files from an SKU to another SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1964,          \&quot;ArchiveId\&quot;: 155404,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;\&quot;      },      {          \&quot;Id\&quot;: 1965,          \&quot;ArchiveId\&quot;: 155429,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuIdfrom __Origin__ SKU’s unique numerical identifier. (required)
     * @param skuIdto __Target__ SKU’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutAsync(String contentType, String accept, Integer skuIdfrom, Integer skuIdto, final ApiCallback<List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutValidateBeforeCall(contentType, accept, skuIdfrom, skuIdto, _callback);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteCall(String contentType, String accept, Integer skuId, Integer skuFileId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/disassociate/{skuId}/file/{skuFileId}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()))
            .replace("{" + "skuFileId" + "}", localVarApiClient.escapeString(skuFileId.toString()));

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
    private okhttp3.Call apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteValidateBeforeCall(String contentType, String accept, Integer skuId, Integer skuFileId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(Async)");
        }

        // verify the required parameter 'skuFileId' is set
        if (skuFileId == null) {
            throw new ApiException("Missing the required parameter 'skuFileId' when calling apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(Async)");
        }

        return apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteCall(contentType, accept, skuId, skuFileId, _callback);

    }

    /**
     * Disassociate SKU File
     * Disassociates an SKU File from an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(String contentType, String accept, Integer skuId, Integer skuFileId) throws ApiException {
        apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteWithHttpInfo(contentType, accept, skuId, skuFileId);
    }

    /**
     * Disassociate SKU File
     * Disassociates an SKU File from an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteWithHttpInfo(String contentType, String accept, Integer skuId, Integer skuFileId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteValidateBeforeCall(contentType, accept, skuId, skuFileId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Disassociate SKU File (asynchronously)
     * Disassociates an SKU File from an SKU.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteAsync(String contentType, String accept, Integer skuId, Integer skuFileId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteValidateBeforeCall(contentType, accept, skuId, skuFileId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdFileDelete
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileDeleteCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/file"
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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileDeleteValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdFileDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdFileDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdFileDelete(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdFileDeleteCall(contentType, accept, skuId, _callback);

    }

    /**
     * Delete All SKU Files
     * Deletes all SKU Image Files.
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
    public void apiCatalogPvtStockkeepingunitSkuIdFileDelete(String contentType, String accept, Integer skuId) throws ApiException {
        apiCatalogPvtStockkeepingunitSkuIdFileDeleteWithHttpInfo(contentType, accept, skuId);
    }

    /**
     * Delete All SKU Files
     * Deletes all SKU Image Files.
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
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitSkuIdFileDeleteWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileDeleteValidateBeforeCall(contentType, accept, skuId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete All SKU Files (asynchronously)
     * Deletes all SKU Image Files.
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileDeleteAsync(String contentType, String accept, Integer skuId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileDeleteValidateBeforeCall(contentType, accept, skuId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdFileGet
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileGetCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/file"
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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileGetValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdFileGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdFileGet(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdFileGet(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdFileGetCall(contentType, accept, skuId, _callback);

    }

    /**
     * Get SKU Files
     * Gets general information about all Files in the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 549,          \&quot;ArchiveId\&quot;: 155485,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;chimera-cat-quimera-5\&quot;,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;miau\&quot;      },      {          \&quot;Id\&quot;: 550,          \&quot;ArchiveId\&quot;: 155486,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Gato-siames\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;Gato siames\&quot;      },      {          \&quot;Id\&quot;: 555,          \&quot;ArchiveId\&quot;: 155491,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Cat-Sleeping-Pics\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: null      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return List&lt;ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner> apiCatalogPvtStockkeepingunitSkuIdFileGet(String contentType, String accept, Integer skuId) throws ApiException {
        ApiResponse<List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner>> localVarResp = apiCatalogPvtStockkeepingunitSkuIdFileGetWithHttpInfo(contentType, accept, skuId);
        return localVarResp.getData();
    }

    /**
     * Get SKU Files
     * Gets general information about all Files in the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 549,          \&quot;ArchiveId\&quot;: 155485,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;chimera-cat-quimera-5\&quot;,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;miau\&quot;      },      {          \&quot;Id\&quot;: 550,          \&quot;ArchiveId\&quot;: 155486,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Gato-siames\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;Gato siames\&quot;      },      {          \&quot;Id\&quot;: 555,          \&quot;ArchiveId\&quot;: 155491,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Cat-Sleeping-Pics\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: null      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner>> apiCatalogPvtStockkeepingunitSkuIdFileGetWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileGetValidateBeforeCall(contentType, accept, skuId, null);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU Files (asynchronously)
     * Gets general information about all Files in the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 549,          \&quot;ArchiveId\&quot;: 155485,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;chimera-cat-quimera-5\&quot;,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;miau\&quot;      },      {          \&quot;Id\&quot;: 550,          \&quot;ArchiveId\&quot;: 155486,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Gato-siames\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;Gato siames\&quot;      },      {          \&quot;Id\&quot;: 555,          \&quot;ArchiveId\&quot;: 155491,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Cat-Sleeping-Pics\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: null      }  ]  &#x60;&#x60;&#x60;
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
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileGetAsync(String contentType, String accept, Integer skuId, final ApiCallback<List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileGetValidateBeforeCall(contentType, accept, skuId, _callback);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdFilePost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skUFileURL  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFilePostCall(String contentType, String accept, Integer skuId, SKUFileURL skUFileURL, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = skUFileURL;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/file"
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
            "application/json",
            "form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFilePostValidateBeforeCall(String contentType, String accept, Integer skuId, SKUFileURL skUFileURL, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdFilePost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdFilePost(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdFilePost(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdFilePostCall(contentType, accept, skuId, skUFileURL, _callback);

    }

    /**
     * Create SKU File
     * Creates a new Image for an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;Text\&quot;: null,        \&quot;Url\&quot;: \&quot;https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\&quot;          }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {        \&quot;Id\&quot;: 503,        \&quot;ArchiveId\&quot;: 155491,        \&quot;SkuId\&quot;: 1,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skUFileURL  (optional)
     * @return ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response apiCatalogPvtStockkeepingunitSkuIdFilePost(String contentType, String accept, Integer skuId, SKUFileURL skUFileURL) throws ApiException {
        ApiResponse<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response> localVarResp = apiCatalogPvtStockkeepingunitSkuIdFilePostWithHttpInfo(contentType, accept, skuId, skUFileURL);
        return localVarResp.getData();
    }

    /**
     * Create SKU File
     * Creates a new Image for an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;Text\&quot;: null,        \&quot;Url\&quot;: \&quot;https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\&quot;          }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {        \&quot;Id\&quot;: 503,        \&quot;ArchiveId\&quot;: 155491,        \&quot;SkuId\&quot;: 1,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skUFileURL  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response> apiCatalogPvtStockkeepingunitSkuIdFilePostWithHttpInfo(String contentType, String accept, Integer skuId, SKUFileURL skUFileURL) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFilePostValidateBeforeCall(contentType, accept, skuId, skUFileURL, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create SKU File (asynchronously)
     * Creates a new Image for an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;Text\&quot;: null,        \&quot;Url\&quot;: \&quot;https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\&quot;          }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {        \&quot;Id\&quot;: 503,        \&quot;ArchiveId\&quot;: 155491,        \&quot;SkuId\&quot;: 1,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skUFileURL  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFilePostAsync(String contentType, String accept, Integer skuId, SKUFileURL skUFileURL, final ApiCallback<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFilePostValidateBeforeCall(contentType, accept, skuId, skUFileURL, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteCall(String contentType, String accept, Integer skuId, Integer skuFileId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()))
            .replace("{" + "skuFileId" + "}", localVarApiClient.escapeString(skuFileId.toString()));

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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteValidateBeforeCall(String contentType, String accept, Integer skuId, Integer skuFileId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(Async)");
        }

        // verify the required parameter 'skuFileId' is set
        if (skuFileId == null) {
            throw new ApiException("Missing the required parameter 'skuFileId' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteCall(contentType, accept, skuId, skuFileId, _callback);

    }

    /**
     * Delete SKU Image File
     * Deletes a specific SKU Image File.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(String contentType, String accept, Integer skuId, Integer skuFileId) throws ApiException {
        apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteWithHttpInfo(contentType, accept, skuId, skuFileId);
    }

    /**
     * Delete SKU Image File
     * Deletes a specific SKU Image File.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteWithHttpInfo(String contentType, String accept, Integer skuId, Integer skuFileId) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteValidateBeforeCall(contentType, accept, skuId, skuFileId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete SKU Image File (asynchronously)
     * Deletes a specific SKU Image File.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteAsync(String contentType, String accept, Integer skuId, Integer skuFileId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteValidateBeforeCall(contentType, accept, skuId, skuFileId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param skUFileURL  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutCall(String contentType, String accept, Integer skuId, Integer skuFileId, SKUFileURL skUFileURL, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = skUFileURL;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()))
            .replace("{" + "skuFileId" + "}", localVarApiClient.escapeString(skuFileId.toString()));

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
    private okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutValidateBeforeCall(String contentType, String accept, Integer skuId, Integer skuFileId, SKUFileURL skUFileURL, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(Async)");
        }

        // verify the required parameter 'skuFileId' is set
        if (skuFileId == null) {
            throw new ApiException("Missing the required parameter 'skuFileId' when calling apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(Async)");
        }

        return apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutCall(contentType, accept, skuId, skuFileId, skUFileURL, _callback);

    }

    /**
     * Update SKU File
     * Updates a new Image on an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null,      \&quot;Name\&quot;: \&quot;toilet-paper\&quot;,      \&quot;Text\&quot;: null,      \&quot;Url\&quot;: \&quot;https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 508,      \&quot;ArchiveId\&quot;: 155491,      \&quot;SkuId\&quot;: 7,      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param skUFileURL  (optional)
     * @return ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(String contentType, String accept, Integer skuId, Integer skuFileId, SKUFileURL skUFileURL) throws ApiException {
        ApiResponse<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response> localVarResp = apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutWithHttpInfo(contentType, accept, skuId, skuFileId, skUFileURL);
        return localVarResp.getData();
    }

    /**
     * Update SKU File
     * Updates a new Image on an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null,      \&quot;Name\&quot;: \&quot;toilet-paper\&quot;,      \&quot;Text\&quot;: null,      \&quot;Url\&quot;: \&quot;https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 508,      \&quot;ArchiveId\&quot;: 155491,      \&quot;SkuId\&quot;: 7,      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param skUFileURL  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response> apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutWithHttpInfo(String contentType, String accept, Integer skuId, Integer skuFileId, SKUFileURL skUFileURL) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutValidateBeforeCall(contentType, accept, skuId, skuFileId, skUFileURL, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update SKU File (asynchronously)
     * Updates a new Image on an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null,      \&quot;Name\&quot;: \&quot;toilet-paper\&quot;,      \&quot;Text\&quot;: null,      \&quot;Url\&quot;: \&quot;https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 508,      \&quot;ArchiveId\&quot;: 155491,      \&quot;SkuId\&quot;: 7,      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @param skuFileId ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. (required)
     * @param skUFileURL  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutAsync(String contentType, String accept, Integer skuId, Integer skuFileId, SKUFileURL skUFileURL, final ApiCallback<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutValidateBeforeCall(contentType, accept, skuId, skuFileId, skUFileURL, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
