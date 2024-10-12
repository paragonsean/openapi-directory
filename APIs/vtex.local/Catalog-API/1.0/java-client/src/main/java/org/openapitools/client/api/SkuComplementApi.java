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


import org.openapitools.client.model.GetSKUcomplementsbytype200Response;
import org.openapitools.client.model.RequestBody2;
import org.openapitools.client.model.SkuComplementInner;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SkuComplementApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SkuComplementApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SkuComplementApi(ApiClient apiClient) {
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
     * Build call for createSKUComplement
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody2  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createSKUComplementCall(String contentType, String accept, RequestBody2 requestBody2, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = requestBody2;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/skucomplement";

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
    private okhttp3.Call createSKUComplementValidateBeforeCall(String contentType, String accept, RequestBody2 requestBody2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling createSKUComplement(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling createSKUComplement(Async)");
        }

        return createSKUComplementCall(contentType, accept, requestBody2, _callback);

    }

    /**
     * Create SKU Complement
     * Creates a new SKU Complement on a Parent SKU.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody2  (optional)
     * @return List&lt;SkuComplementInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<SkuComplementInner> createSKUComplement(String contentType, String accept, RequestBody2 requestBody2) throws ApiException {
        ApiResponse<List<SkuComplementInner>> localVarResp = createSKUComplementWithHttpInfo(contentType, accept, requestBody2);
        return localVarResp.getData();
    }

    /**
     * Create SKU Complement
     * Creates a new SKU Complement on a Parent SKU.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody2  (optional)
     * @return ApiResponse&lt;List&lt;SkuComplementInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SkuComplementInner>> createSKUComplementWithHttpInfo(String contentType, String accept, RequestBody2 requestBody2) throws ApiException {
        okhttp3.Call localVarCall = createSKUComplementValidateBeforeCall(contentType, accept, requestBody2, null);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create SKU Complement (asynchronously)
     * Creates a new SKU Complement on a Parent SKU.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param requestBody2  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createSKUComplementAsync(String contentType, String accept, RequestBody2 requestBody2, final ApiCallback<List<SkuComplementInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = createSKUComplementValidateBeforeCall(contentType, accept, requestBody2, _callback);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteSKUComplementbySKUComplementID
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteSKUComplementbySKUComplementIDCall(String contentType, String accept, Integer skuComplementId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/skucomplement/{skuComplementId}"
            .replace("{" + "skuComplementId" + "}", localVarApiClient.escapeString(skuComplementId.toString()));

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
    private okhttp3.Call deleteSKUComplementbySKUComplementIDValidateBeforeCall(String contentType, String accept, Integer skuComplementId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling deleteSKUComplementbySKUComplementID(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling deleteSKUComplementbySKUComplementID(Async)");
        }

        // verify the required parameter 'skuComplementId' is set
        if (skuComplementId == null) {
            throw new ApiException("Missing the required parameter 'skuComplementId' when calling deleteSKUComplementbySKUComplementID(Async)");
        }

        return deleteSKUComplementbySKUComplementIDCall(contentType, accept, skuComplementId, _callback);

    }

    /**
     * Delete SKU Complement by SKU Complement ID
     * Deletes a previously existing SKU Complement by SKU Complement ID.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void deleteSKUComplementbySKUComplementID(String contentType, String accept, Integer skuComplementId) throws ApiException {
        deleteSKUComplementbySKUComplementIDWithHttpInfo(contentType, accept, skuComplementId);
    }

    /**
     * Delete SKU Complement by SKU Complement ID
     * Deletes a previously existing SKU Complement by SKU Complement ID.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteSKUComplementbySKUComplementIDWithHttpInfo(String contentType, String accept, Integer skuComplementId) throws ApiException {
        okhttp3.Call localVarCall = deleteSKUComplementbySKUComplementIDValidateBeforeCall(contentType, accept, skuComplementId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete SKU Complement by SKU Complement ID (asynchronously)
     * Deletes a previously existing SKU Complement by SKU Complement ID.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteSKUComplementbySKUComplementIDAsync(String contentType, String accept, Integer skuComplementId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteSKUComplementbySKUComplementIDValidateBeforeCall(contentType, accept, skuComplementId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSKUComplementbySKUComplementID
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSKUComplementbySKUComplementIDCall(String contentType, String accept, Integer skuComplementId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/skucomplement/{skuComplementId}"
            .replace("{" + "skuComplementId" + "}", localVarApiClient.escapeString(skuComplementId.toString()));

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
    private okhttp3.Call getSKUComplementbySKUComplementIDValidateBeforeCall(String contentType, String accept, Integer skuComplementId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getSKUComplementbySKUComplementID(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getSKUComplementbySKUComplementID(Async)");
        }

        // verify the required parameter 'skuComplementId' is set
        if (skuComplementId == null) {
            throw new ApiException("Missing the required parameter 'skuComplementId' when calling getSKUComplementbySKUComplementID(Async)");
        }

        return getSKUComplementbySKUComplementIDCall(contentType, accept, skuComplementId, _callback);

    }

    /**
     * Get SKU Complement by SKU Complement ID
     * Retrieves an existing SKU Complement by its SKU Complement ID.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @return List&lt;SkuComplementInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<SkuComplementInner> getSKUComplementbySKUComplementID(String contentType, String accept, Integer skuComplementId) throws ApiException {
        ApiResponse<List<SkuComplementInner>> localVarResp = getSKUComplementbySKUComplementIDWithHttpInfo(contentType, accept, skuComplementId);
        return localVarResp.getData();
    }

    /**
     * Get SKU Complement by SKU Complement ID
     * Retrieves an existing SKU Complement by its SKU Complement ID.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;SkuComplementInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SkuComplementInner>> getSKUComplementbySKUComplementIDWithHttpInfo(String contentType, String accept, Integer skuComplementId) throws ApiException {
        okhttp3.Call localVarCall = getSKUComplementbySKUComplementIDValidateBeforeCall(contentType, accept, skuComplementId, null);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU Complement by SKU Complement ID (asynchronously)
     * Retrieves an existing SKU Complement by its SKU Complement ID.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuComplementId SKU Complement’s unique numerical identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSKUComplementbySKUComplementIDAsync(String contentType, String accept, Integer skuComplementId, final ApiCallback<List<SkuComplementInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSKUComplementbySKUComplementIDValidateBeforeCall(contentType, accept, skuComplementId, _callback);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSKUComplementbySKUID
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
    public okhttp3.Call getSKUComplementbySKUIDCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/complement"
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
    private okhttp3.Call getSKUComplementbySKUIDValidateBeforeCall(String contentType, String accept, Integer skuId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getSKUComplementbySKUID(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getSKUComplementbySKUID(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling getSKUComplementbySKUID(Async)");
        }

        return getSKUComplementbySKUIDCall(contentType, accept, skuId, _callback);

    }

    /**
     * Get SKU Complement by SKU ID
     * Retrieves an existing SKU Complement by its SKU ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return List&lt;SkuComplementInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<SkuComplementInner> getSKUComplementbySKUID(String contentType, String accept, Integer skuId) throws ApiException {
        ApiResponse<List<SkuComplementInner>> localVarResp = getSKUComplementbySKUIDWithHttpInfo(contentType, accept, skuId);
        return localVarResp.getData();
    }

    /**
     * Get SKU Complement by SKU ID
     * Retrieves an existing SKU Complement by its SKU ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId SKU’s unique numerical identifier. (required)
     * @return ApiResponse&lt;List&lt;SkuComplementInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SkuComplementInner>> getSKUComplementbySKUIDWithHttpInfo(String contentType, String accept, Integer skuId) throws ApiException {
        okhttp3.Call localVarCall = getSKUComplementbySKUIDValidateBeforeCall(contentType, accept, skuId, null);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU Complement by SKU ID (asynchronously)
     * Retrieves an existing SKU Complement by its SKU ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;
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
    public okhttp3.Call getSKUComplementbySKUIDAsync(String contentType, String accept, Integer skuId, final ApiCallback<List<SkuComplementInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSKUComplementbySKUIDValidateBeforeCall(contentType, accept, skuId, _callback);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSKUComplementsbyComplementTypeID
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId ID of the SKU which will be inserted as a Complement in the Parent SKU. (required)
     * @param complementTypeId Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSKUComplementsbyComplementTypeIDCall(String contentType, String accept, Integer skuId, Integer complementTypeId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/stockkeepingunit/{skuId}/complement/{complementTypeId}"
            .replace("{" + "skuId" + "}", localVarApiClient.escapeString(skuId.toString()))
            .replace("{" + "complementTypeId" + "}", localVarApiClient.escapeString(complementTypeId.toString()));

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
    private okhttp3.Call getSKUComplementsbyComplementTypeIDValidateBeforeCall(String contentType, String accept, Integer skuId, Integer complementTypeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getSKUComplementsbyComplementTypeID(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getSKUComplementsbyComplementTypeID(Async)");
        }

        // verify the required parameter 'skuId' is set
        if (skuId == null) {
            throw new ApiException("Missing the required parameter 'skuId' when calling getSKUComplementsbyComplementTypeID(Async)");
        }

        // verify the required parameter 'complementTypeId' is set
        if (complementTypeId == null) {
            throw new ApiException("Missing the required parameter 'complementTypeId' when calling getSKUComplementsbyComplementTypeID(Async)");
        }

        return getSKUComplementsbyComplementTypeIDCall(contentType, accept, skuId, complementTypeId, _callback);

    }

    /**
     * Get SKU Complements by Complement Type ID
     * Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId ID of the SKU which will be inserted as a Complement in the Parent SKU. (required)
     * @param complementTypeId Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @return List&lt;SkuComplementInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<SkuComplementInner> getSKUComplementsbyComplementTypeID(String contentType, String accept, Integer skuId, Integer complementTypeId) throws ApiException {
        ApiResponse<List<SkuComplementInner>> localVarResp = getSKUComplementsbyComplementTypeIDWithHttpInfo(contentType, accept, skuId, complementTypeId);
        return localVarResp.getData();
    }

    /**
     * Get SKU Complements by Complement Type ID
     * Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId ID of the SKU which will be inserted as a Complement in the Parent SKU. (required)
     * @param complementTypeId Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @return ApiResponse&lt;List&lt;SkuComplementInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SkuComplementInner>> getSKUComplementsbyComplementTypeIDWithHttpInfo(String contentType, String accept, Integer skuId, Integer complementTypeId) throws ApiException {
        okhttp3.Call localVarCall = getSKUComplementsbyComplementTypeIDValidateBeforeCall(contentType, accept, skuId, complementTypeId, null);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU Complements by Complement Type ID (asynchronously)
     * Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param skuId ID of the SKU which will be inserted as a Complement in the Parent SKU. (required)
     * @param complementTypeId Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSKUComplementsbyComplementTypeIDAsync(String contentType, String accept, Integer skuId, Integer complementTypeId, final ApiCallback<List<SkuComplementInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSKUComplementsbyComplementTypeIDValidateBeforeCall(contentType, accept, skuId, complementTypeId, _callback);
        Type localVarReturnType = new TypeToken<List<SkuComplementInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSKUcomplementsbytype
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param parentSkuId ID of the Parent SKU, where the Complement is inserted. (required)
     * @param type Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSKUcomplementsbytypeCall(String contentType, String accept, Integer parentSkuId, Integer type, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/sku/complements/{parentSkuId}/{type}"
            .replace("{" + "parentSkuId" + "}", localVarApiClient.escapeString(parentSkuId.toString()))
            .replace("{" + "type" + "}", localVarApiClient.escapeString(type.toString()));

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
    private okhttp3.Call getSKUcomplementsbytypeValidateBeforeCall(String contentType, String accept, Integer parentSkuId, Integer type, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getSKUcomplementsbytype(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getSKUcomplementsbytype(Async)");
        }

        // verify the required parameter 'parentSkuId' is set
        if (parentSkuId == null) {
            throw new ApiException("Missing the required parameter 'parentSkuId' when calling getSKUcomplementsbytype(Async)");
        }

        // verify the required parameter 'type' is set
        if (type == null) {
            throw new ApiException("Missing the required parameter 'type' when calling getSKUcomplementsbytype(Async)");
        }

        return getSKUcomplementsbytypeCall(contentType, accept, parentSkuId, type, _callback);

    }

    /**
     * Get SKU complements by type
     * Retrieves all the existing SKU complements with the same complement type ID of a specific SKU.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementSkuIds\&quot;: [          7      ],      \&quot;Type\&quot;: \&quot;1\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param parentSkuId ID of the Parent SKU, where the Complement is inserted. (required)
     * @param type Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @return GetSKUcomplementsbytype200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetSKUcomplementsbytype200Response getSKUcomplementsbytype(String contentType, String accept, Integer parentSkuId, Integer type) throws ApiException {
        ApiResponse<GetSKUcomplementsbytype200Response> localVarResp = getSKUcomplementsbytypeWithHttpInfo(contentType, accept, parentSkuId, type);
        return localVarResp.getData();
    }

    /**
     * Get SKU complements by type
     * Retrieves all the existing SKU complements with the same complement type ID of a specific SKU.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementSkuIds\&quot;: [          7      ],      \&quot;Type\&quot;: \&quot;1\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param parentSkuId ID of the Parent SKU, where the Complement is inserted. (required)
     * @param type Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @return ApiResponse&lt;GetSKUcomplementsbytype200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetSKUcomplementsbytype200Response> getSKUcomplementsbytypeWithHttpInfo(String contentType, String accept, Integer parentSkuId, Integer type) throws ApiException {
        okhttp3.Call localVarCall = getSKUcomplementsbytypeValidateBeforeCall(contentType, accept, parentSkuId, type, null);
        Type localVarReturnType = new TypeToken<GetSKUcomplementsbytype200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SKU complements by type (asynchronously)
     * Retrieves all the existing SKU complements with the same complement type ID of a specific SKU.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementSkuIds\&quot;: [          7      ],      \&quot;Type\&quot;: \&quot;1\&quot;  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param parentSkuId ID of the Parent SKU, where the Complement is inserted. (required)
     * @param type Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSKUcomplementsbytypeAsync(String contentType, String accept, Integer parentSkuId, Integer type, final ApiCallback<GetSKUcomplementsbytype200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSKUcomplementsbytypeValidateBeforeCall(contentType, accept, parentSkuId, type, _callback);
        Type localVarReturnType = new TypeToken<GetSKUcomplementsbytype200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
