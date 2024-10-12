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


import org.openapitools.client.model.ApiCatalogPvtProductProductIdSpecificationPost200Response;
import org.openapitools.client.model.ApiCatalogPvtProductProductIdSpecificationPostRequest;
import org.openapitools.client.model.ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner;
import org.openapitools.client.model.ApiCatalogPvtProductProductIdSpecificationvaluePutRequest;
import org.openapitools.client.model.GetProductSpecificationbyProductID200ResponseInner;
import org.openapitools.client.model.GetorUpdateProductSpecification;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductSpecificationApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductSpecificationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductSpecificationApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtProductProductIdSpecificationPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSpecificationPostCall(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationPostRequest apiCatalogPvtProductProductIdSpecificationPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtProductProductIdSpecificationPostRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/product/{productId}/specification"
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
    private okhttp3.Call apiCatalogPvtProductProductIdSpecificationPostValidateBeforeCall(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationPostRequest apiCatalogPvtProductProductIdSpecificationPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtProductProductIdSpecificationPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtProductProductIdSpecificationPost(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling apiCatalogPvtProductProductIdSpecificationPost(Async)");
        }

        return apiCatalogPvtProductProductIdSpecificationPostCall(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationPostRequest, _callback);

    }

    /**
     * Associate Product Specification
     * Associates a previously defined Specification to a Product.    ### Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 41,      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationPostRequest  (optional)
     * @return ApiCatalogPvtProductProductIdSpecificationPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtProductProductIdSpecificationPost200Response apiCatalogPvtProductProductIdSpecificationPost(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationPostRequest apiCatalogPvtProductProductIdSpecificationPostRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtProductProductIdSpecificationPost200Response> localVarResp = apiCatalogPvtProductProductIdSpecificationPostWithHttpInfo(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationPostRequest);
        return localVarResp.getData();
    }

    /**
     * Associate Product Specification
     * Associates a previously defined Specification to a Product.    ### Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 41,      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationPostRequest  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtProductProductIdSpecificationPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtProductProductIdSpecificationPost200Response> apiCatalogPvtProductProductIdSpecificationPostWithHttpInfo(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationPostRequest apiCatalogPvtProductProductIdSpecificationPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSpecificationPostValidateBeforeCall(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationPostRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtProductProductIdSpecificationPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Associate Product Specification (asynchronously)
     * Associates a previously defined Specification to a Product.    ### Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 41,      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSpecificationPostAsync(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationPostRequest apiCatalogPvtProductProductIdSpecificationPostRequest, final ApiCallback<ApiCatalogPvtProductProductIdSpecificationPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSpecificationPostValidateBeforeCall(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtProductProductIdSpecificationPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtProductProductIdSpecificationvaluePut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationvaluePutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSpecificationvaluePutCall(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationvaluePutRequest apiCatalogPvtProductProductIdSpecificationvaluePutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtProductProductIdSpecificationvaluePutRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/product/{productId}/specificationvalue"
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
    private okhttp3.Call apiCatalogPvtProductProductIdSpecificationvaluePutValidateBeforeCall(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationvaluePutRequest apiCatalogPvtProductProductIdSpecificationvaluePutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtProductProductIdSpecificationvaluePut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtProductProductIdSpecificationvaluePut(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling apiCatalogPvtProductProductIdSpecificationvaluePut(Async)");
        }

        return apiCatalogPvtProductProductIdSpecificationvaluePutCall(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationvaluePutRequest, _callback);

    }

    /**
     * Associate product specification using specification name and group name
     * Associates a specification to a product using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Material\&quot;,      \&quot;GroupName\&quot;: \&quot;Additional Information\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;Cotton\&quot;,         \&quot;Polyester\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 53,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 60,          \&quot;Text\&quot;: \&quot;Cotton\&quot;      },      {          \&quot;Id\&quot;: 54,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 61,          \&quot;Text\&quot;: \&quot;Polyester\&quot;      }  ]  &#x60;&#x60;&#x60;  
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationvaluePutRequest  (optional)
     * @return List&lt;ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner> apiCatalogPvtProductProductIdSpecificationvaluePut(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationvaluePutRequest apiCatalogPvtProductProductIdSpecificationvaluePutRequest) throws ApiException {
        ApiResponse<List<ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner>> localVarResp = apiCatalogPvtProductProductIdSpecificationvaluePutWithHttpInfo(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationvaluePutRequest);
        return localVarResp.getData();
    }

    /**
     * Associate product specification using specification name and group name
     * Associates a specification to a product using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Material\&quot;,      \&quot;GroupName\&quot;: \&quot;Additional Information\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;Cotton\&quot;,         \&quot;Polyester\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 53,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 60,          \&quot;Text\&quot;: \&quot;Cotton\&quot;      },      {          \&quot;Id\&quot;: 54,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 61,          \&quot;Text\&quot;: \&quot;Polyester\&quot;      }  ]  &#x60;&#x60;&#x60;  
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationvaluePutRequest  (optional)
     * @return ApiResponse&lt;List&lt;ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner>> apiCatalogPvtProductProductIdSpecificationvaluePutWithHttpInfo(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationvaluePutRequest apiCatalogPvtProductProductIdSpecificationvaluePutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSpecificationvaluePutValidateBeforeCall(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationvaluePutRequest, null);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Associate product specification using specification name and group name (asynchronously)
     * Associates a specification to a product using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Material\&quot;,      \&quot;GroupName\&quot;: \&quot;Additional Information\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;Cotton\&quot;,         \&quot;Polyester\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 53,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 60,          \&quot;Text\&quot;: \&quot;Cotton\&quot;      },      {          \&quot;Id\&quot;: 54,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 61,          \&quot;Text\&quot;: \&quot;Polyester\&quot;      }  ]  &#x60;&#x60;&#x60;  
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdSpecificationvaluePutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdSpecificationvaluePutAsync(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdSpecificationvaluePutRequest apiCatalogPvtProductProductIdSpecificationvaluePutRequest, final ApiCallback<List<ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdSpecificationvaluePutValidateBeforeCall(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationvaluePutRequest, _callback);
        Type localVarReturnType = new TypeToken<List<ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteAllProductSpecifications
     * @param contentType Describes the type of the content being sent. (required)
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
    public okhttp3.Call deleteAllProductSpecificationsCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/product/{productId}/specification"
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
    private okhttp3.Call deleteAllProductSpecificationsValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling deleteAllProductSpecifications(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling deleteAllProductSpecifications(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling deleteAllProductSpecifications(Async)");
        }

        return deleteAllProductSpecificationsCall(contentType, accept, productId, _callback);

    }

    /**
     * Delete all Product Specifications by Product ID
     * Deletes all Product Specifications given a specific Product ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void deleteAllProductSpecifications(String contentType, String accept, Integer productId) throws ApiException {
        deleteAllProductSpecificationsWithHttpInfo(contentType, accept, productId);
    }

    /**
     * Delete all Product Specifications by Product ID
     * Deletes all Product Specifications given a specific Product ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteAllProductSpecificationsWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = deleteAllProductSpecificationsValidateBeforeCall(contentType, accept, productId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete all Product Specifications by Product ID (asynchronously)
     * Deletes all Product Specifications given a specific Product ID.
     * @param contentType Describes the type of the content being sent. (required)
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
    public okhttp3.Call deleteAllProductSpecificationsAsync(String contentType, String accept, Integer productId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteAllProductSpecificationsValidateBeforeCall(contentType, accept, productId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteaProductSpecification
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param specificationId Product Specification’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteaProductSpecificationCall(String contentType, String accept, Integer productId, Integer specificationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/product/{productId}/specification/{specificationId}"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
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
    private okhttp3.Call deleteaProductSpecificationValidateBeforeCall(String contentType, String accept, Integer productId, Integer specificationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling deleteaProductSpecification(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling deleteaProductSpecification(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling deleteaProductSpecification(Async)");
        }

        // verify the required parameter 'specificationId' is set
        if (specificationId == null) {
            throw new ApiException("Missing the required parameter 'specificationId' when calling deleteaProductSpecification(Async)");
        }

        return deleteaProductSpecificationCall(contentType, accept, productId, specificationId, _callback);

    }

    /**
     * Delete a specific Product Specification
     * Deletes a specific Product Specification given a Product ID and a Specification ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param specificationId Product Specification’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void deleteaProductSpecification(String contentType, String accept, Integer productId, Integer specificationId) throws ApiException {
        deleteaProductSpecificationWithHttpInfo(contentType, accept, productId, specificationId);
    }

    /**
     * Delete a specific Product Specification
     * Deletes a specific Product Specification given a Product ID and a Specification ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param specificationId Product Specification’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteaProductSpecificationWithHttpInfo(String contentType, String accept, Integer productId, Integer specificationId) throws ApiException {
        okhttp3.Call localVarCall = deleteaProductSpecificationValidateBeforeCall(contentType, accept, productId, specificationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a specific Product Specification (asynchronously)
     * Deletes a specific Product Specification given a Product ID and a Specification ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param specificationId Product Specification’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteaProductSpecificationAsync(String contentType, String accept, Integer productId, Integer specificationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteaProductSpecificationValidateBeforeCall(contentType, accept, productId, specificationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProductSpecification
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getProductSpecificationCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/products/{productId}/specification"
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
    private okhttp3.Call getProductSpecificationValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getProductSpecification(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getProductSpecification(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling getProductSpecification(Async)");
        }

        return getProductSpecificationCall(contentType, accept, productId, _callback);

    }

    /**
     * Get Product Specification by Product ID
     * Retrieves all specifications of a product by the product&#39;s ID.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return List&lt;GetorUpdateProductSpecification&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public List<GetorUpdateProductSpecification> getProductSpecification(String contentType, String accept, Integer productId) throws ApiException {
        ApiResponse<List<GetorUpdateProductSpecification>> localVarResp = getProductSpecificationWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get Product Specification by Product ID
     * Retrieves all specifications of a product by the product&#39;s ID.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;GetorUpdateProductSpecification&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<List<GetorUpdateProductSpecification>> getProductSpecificationWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = getProductSpecificationValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<List<GetorUpdateProductSpecification>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product Specification by Product ID (asynchronously)
     * Retrieves all specifications of a product by the product&#39;s ID.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getProductSpecificationAsync(String contentType, String accept, Integer productId, final ApiCallback<List<GetorUpdateProductSpecification>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProductSpecificationValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<List<GetorUpdateProductSpecification>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProductSpecificationbyProductID
     * @param contentType Describes the type of the content being sent. (required)
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
    public okhttp3.Call getProductSpecificationbyProductIDCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/product/{productId}/specification"
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
    private okhttp3.Call getProductSpecificationbyProductIDValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getProductSpecificationbyProductID(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getProductSpecificationbyProductID(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling getProductSpecificationbyProductID(Async)");
        }

        return getProductSpecificationbyProductIDCall(contentType, accept, productId, _callback);

    }

    /**
     * Get Product Specification and its information by Product ID
     * Retrieves information of all specifications of a product by the product&#39;s ID.     ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 227,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;FieldValueId\&quot;: 135,          \&quot;Text\&quot;: \&quot;ValueA\&quot;      },      {          \&quot;Id\&quot;: 228,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;FieldValueId\&quot;: 1,          \&quot;Text\&quot;: \&quot;Giant\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return List&lt;GetProductSpecificationbyProductID200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<GetProductSpecificationbyProductID200ResponseInner> getProductSpecificationbyProductID(String contentType, String accept, Integer productId) throws ApiException {
        ApiResponse<List<GetProductSpecificationbyProductID200ResponseInner>> localVarResp = getProductSpecificationbyProductIDWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get Product Specification and its information by Product ID
     * Retrieves information of all specifications of a product by the product&#39;s ID.     ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 227,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;FieldValueId\&quot;: 135,          \&quot;Text\&quot;: \&quot;ValueA\&quot;      },      {          \&quot;Id\&quot;: 228,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;FieldValueId\&quot;: 1,          \&quot;Text\&quot;: \&quot;Giant\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;GetProductSpecificationbyProductID200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<GetProductSpecificationbyProductID200ResponseInner>> getProductSpecificationbyProductIDWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = getProductSpecificationbyProductIDValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<List<GetProductSpecificationbyProductID200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product Specification and its information by Product ID (asynchronously)
     * Retrieves information of all specifications of a product by the product&#39;s ID.     ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 227,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;FieldValueId\&quot;: 135,          \&quot;Text\&quot;: \&quot;ValueA\&quot;      },      {          \&quot;Id\&quot;: 228,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;FieldValueId\&quot;: 1,          \&quot;Text\&quot;: \&quot;Giant\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
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
    public okhttp3.Call getProductSpecificationbyProductIDAsync(String contentType, String accept, Integer productId, final ApiCallback<List<GetProductSpecificationbyProductID200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProductSpecificationbyProductIDValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<List<GetProductSpecificationbyProductID200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateProductSpecification
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique identifier. (required)
     * @param getorUpdateProductSpecification  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateProductSpecificationCall(String contentType, String accept, Integer productId, List<GetorUpdateProductSpecification> getorUpdateProductSpecification, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = getorUpdateProductSpecification;

        // create path and map variables
        String localVarPath = "/api/catalog_system/pvt/products/{productId}/specification"
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
    private okhttp3.Call updateProductSpecificationValidateBeforeCall(String contentType, String accept, Integer productId, List<GetorUpdateProductSpecification> getorUpdateProductSpecification, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling updateProductSpecification(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling updateProductSpecification(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling updateProductSpecification(Async)");
        }

        // verify the required parameter 'getorUpdateProductSpecification' is set
        if (getorUpdateProductSpecification == null) {
            throw new ApiException("Missing the required parameter 'getorUpdateProductSpecification' when calling updateProductSpecification(Async)");
        }

        return updateProductSpecificationCall(contentType, accept, productId, getorUpdateProductSpecification, _callback);

    }

    /**
     * Update Product Specification by Product ID
     * Updates the value of a product specification by the product&#39;s ID. The ID or name can be used to identify what product specification will be updated. Specification fields must be previously created in your Catalog.    ### Request body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique identifier. (required)
     * @param getorUpdateProductSpecification  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void updateProductSpecification(String contentType, String accept, Integer productId, List<GetorUpdateProductSpecification> getorUpdateProductSpecification) throws ApiException {
        updateProductSpecificationWithHttpInfo(contentType, accept, productId, getorUpdateProductSpecification);
    }

    /**
     * Update Product Specification by Product ID
     * Updates the value of a product specification by the product&#39;s ID. The ID or name can be used to identify what product specification will be updated. Specification fields must be previously created in your Catalog.    ### Request body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique identifier. (required)
     * @param getorUpdateProductSpecification  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updateProductSpecificationWithHttpInfo(String contentType, String accept, Integer productId, List<GetorUpdateProductSpecification> getorUpdateProductSpecification) throws ApiException {
        okhttp3.Call localVarCall = updateProductSpecificationValidateBeforeCall(contentType, accept, productId, getorUpdateProductSpecification, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update Product Specification by Product ID (asynchronously)
     * Updates the value of a product specification by the product&#39;s ID. The ID or name can be used to identify what product specification will be updated. Specification fields must be previously created in your Catalog.    ### Request body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique identifier. (required)
     * @param getorUpdateProductSpecification  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateProductSpecificationAsync(String contentType, String accept, Integer productId, List<GetorUpdateProductSpecification> getorUpdateProductSpecification, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateProductSpecificationValidateBeforeCall(contentType, accept, productId, getorUpdateProductSpecification, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
