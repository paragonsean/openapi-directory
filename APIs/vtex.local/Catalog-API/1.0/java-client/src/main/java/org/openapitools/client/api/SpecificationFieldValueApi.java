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


import org.openapitools.client.model.ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response;
import org.openapitools.client.model.GetSpecFieldValue;
import org.openapitools.client.model.SpecificationsInsertFieldValueRequest;
import org.openapitools.client.model.SpecificationsUpdateFieldValueRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpecificationFieldValueApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SpecificationFieldValueApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SpecificationFieldValueApi(ApiClient apiClient) {
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
     * Build call for specificationsGetFieldValue
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldValueId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsGetFieldValueCall(String contentType, String accept, String fieldValueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/specification/fieldValue/{fieldValueId}"
            .replace("{" + "fieldValueId" + "}", localVarApiClient.escapeString(fieldValueId.toString()));

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
    private okhttp3.Call specificationsGetFieldValueValidateBeforeCall(String contentType, String accept, String fieldValueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling specificationsGetFieldValue(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling specificationsGetFieldValue(Async)");
        }

        // verify the required parameter 'fieldValueId' is set
        if (fieldValueId == null) {
            throw new ApiException("Missing the required parameter 'fieldValueId' when calling specificationsGetFieldValue(Async)");
        }

        return specificationsGetFieldValueCall(contentType, accept, fieldValueId, _callback);

    }

    /**
     * Get Specification Field Value
     * Retrieves details from a specification field&#39;s value by this value&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-value-id) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;TesteInsert\&quot;,      \&quot;Text\&quot;: \&quot;Value Description\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldValueId  (required)
     * @return ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response specificationsGetFieldValue(String contentType, String accept, String fieldValueId) throws ApiException {
        ApiResponse<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response> localVarResp = specificationsGetFieldValueWithHttpInfo(contentType, accept, fieldValueId);
        return localVarResp.getData();
    }

    /**
     * Get Specification Field Value
     * Retrieves details from a specification field&#39;s value by this value&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-value-id) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;TesteInsert\&quot;,      \&quot;Text\&quot;: \&quot;Value Description\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldValueId  (required)
     * @return ApiResponse&lt;ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response> specificationsGetFieldValueWithHttpInfo(String contentType, String accept, String fieldValueId) throws ApiException {
        okhttp3.Call localVarCall = specificationsGetFieldValueValidateBeforeCall(contentType, accept, fieldValueId, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Specification Field Value (asynchronously)
     * Retrieves details from a specification field&#39;s value by this value&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-value-id) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;TesteInsert\&quot;,      \&quot;Text\&quot;: \&quot;Value Description\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldValueId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsGetFieldValueAsync(String contentType, String accept, String fieldValueId, final ApiCallback<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = specificationsGetFieldValueValidateBeforeCall(contentType, accept, fieldValueId, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for specificationsInsertFieldValue
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsInsertFieldValueRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsInsertFieldValueCall(String contentType, String accept, SpecificationsInsertFieldValueRequest specificationsInsertFieldValueRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = specificationsInsertFieldValueRequest;

        // create path and map variables
        String localVarPath = "/api/catalog_system/pvt/specification/fieldValue";

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
    private okhttp3.Call specificationsInsertFieldValueValidateBeforeCall(String contentType, String accept, SpecificationsInsertFieldValueRequest specificationsInsertFieldValueRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling specificationsInsertFieldValue(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling specificationsInsertFieldValue(Async)");
        }

        // verify the required parameter 'specificationsInsertFieldValueRequest' is set
        if (specificationsInsertFieldValueRequest == null) {
            throw new ApiException("Missing the required parameter 'specificationsInsertFieldValueRequest' when calling specificationsInsertFieldValue(Async)");
        }

        return specificationsInsertFieldValueCall(contentType, accept, specificationsInsertFieldValueRequest, _callback);

    }

    /**
     * Create Specification Field Value
     * Creates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsInsertFieldValueRequest  (required)
     * @return ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response specificationsInsertFieldValue(String contentType, String accept, SpecificationsInsertFieldValueRequest specificationsInsertFieldValueRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response> localVarResp = specificationsInsertFieldValueWithHttpInfo(contentType, accept, specificationsInsertFieldValueRequest);
        return localVarResp.getData();
    }

    /**
     * Create Specification Field Value
     * Creates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsInsertFieldValueRequest  (required)
     * @return ApiResponse&lt;ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response> specificationsInsertFieldValueWithHttpInfo(String contentType, String accept, SpecificationsInsertFieldValueRequest specificationsInsertFieldValueRequest) throws ApiException {
        okhttp3.Call localVarCall = specificationsInsertFieldValueValidateBeforeCall(contentType, accept, specificationsInsertFieldValueRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create Specification Field Value (asynchronously)
     * Creates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsInsertFieldValueRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsInsertFieldValueAsync(String contentType, String accept, SpecificationsInsertFieldValueRequest specificationsInsertFieldValueRequest, final ApiCallback<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = specificationsInsertFieldValueValidateBeforeCall(contentType, accept, specificationsInsertFieldValueRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for specificationsUpdateFieldValue
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsUpdateFieldValueRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsUpdateFieldValueCall(String contentType, String accept, SpecificationsUpdateFieldValueRequest specificationsUpdateFieldValueRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = specificationsUpdateFieldValueRequest;

        // create path and map variables
        String localVarPath = "/api/catalog_system/pvt/specification/fieldValue";

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
    private okhttp3.Call specificationsUpdateFieldValueValidateBeforeCall(String contentType, String accept, SpecificationsUpdateFieldValueRequest specificationsUpdateFieldValueRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling specificationsUpdateFieldValue(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling specificationsUpdateFieldValue(Async)");
        }

        // verify the required parameter 'specificationsUpdateFieldValueRequest' is set
        if (specificationsUpdateFieldValueRequest == null) {
            throw new ApiException("Missing the required parameter 'specificationsUpdateFieldValueRequest' when calling specificationsUpdateFieldValue(Async)");
        }

        return specificationsUpdateFieldValueCall(contentType, accept, specificationsUpdateFieldValueRequest, _callback);

    }

    /**
     * Update Specification Field Value
     * Updates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification Field Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification-value-id) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 1,      \&quot;FieldValueId\&quot;: 143,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example (200 OK)    &#x60;&#x60;&#x60;json  \&quot;Field Value Updated\&quot;  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsUpdateFieldValueRequest  (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public String specificationsUpdateFieldValue(String contentType, String accept, SpecificationsUpdateFieldValueRequest specificationsUpdateFieldValueRequest) throws ApiException {
        ApiResponse<String> localVarResp = specificationsUpdateFieldValueWithHttpInfo(contentType, accept, specificationsUpdateFieldValueRequest);
        return localVarResp.getData();
    }

    /**
     * Update Specification Field Value
     * Updates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification Field Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification-value-id) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 1,      \&quot;FieldValueId\&quot;: 143,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example (200 OK)    &#x60;&#x60;&#x60;json  \&quot;Field Value Updated\&quot;  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsUpdateFieldValueRequest  (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> specificationsUpdateFieldValueWithHttpInfo(String contentType, String accept, SpecificationsUpdateFieldValueRequest specificationsUpdateFieldValueRequest) throws ApiException {
        okhttp3.Call localVarCall = specificationsUpdateFieldValueValidateBeforeCall(contentType, accept, specificationsUpdateFieldValueRequest, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update Specification Field Value (asynchronously)
     * Updates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification Field Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification-value-id) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 1,      \&quot;FieldValueId\&quot;: 143,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example (200 OK)    &#x60;&#x60;&#x60;json  \&quot;Field Value Updated\&quot;  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param specificationsUpdateFieldValueRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsUpdateFieldValueAsync(String contentType, String accept, SpecificationsUpdateFieldValueRequest specificationsUpdateFieldValueRequest, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = specificationsUpdateFieldValueValidateBeforeCall(contentType, accept, specificationsUpdateFieldValueRequest, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for specificationsValuesByFieldId
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldId Specification Field ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsValuesByFieldIdCall(String contentType, String accept, Integer fieldId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pub/specification/fieldvalue/{fieldId}"
            .replace("{" + "fieldId" + "}", localVarApiClient.escapeString(fieldId.toString()));

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
    private okhttp3.Call specificationsValuesByFieldIdValidateBeforeCall(String contentType, String accept, Integer fieldId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling specificationsValuesByFieldId(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling specificationsValuesByFieldId(Async)");
        }

        // verify the required parameter 'fieldId' is set
        if (fieldId == null) {
            throw new ApiException("Missing the required parameter 'fieldId' when calling specificationsValuesByFieldId(Async)");
        }

        return specificationsValuesByFieldIdCall(contentType, accept, fieldId, _callback);

    }

    /**
     * Get Specification Values By Field ID
     * Gets a list of all specification values from a Specification Field by this field&#39;s ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;FieldValueId\&quot;: 52,          \&quot;Value\&quot;: \&quot;0 a 6 meses\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 1      },      {          \&quot;FieldValueId\&quot;: 53,          \&quot;Value\&quot;: \&quot;1 a 2 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 4      },      {          \&quot;FieldValueId\&quot;: 54,          \&quot;Value\&quot;: \&quot;3 a 4 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 3      },      {          \&quot;FieldValueId\&quot;: 55,          \&quot;Value\&quot;: \&quot;5 a 6 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 2      },      {          \&quot;FieldValueId\&quot;: 56,          \&quot;Value\&quot;: \&quot;7 a 8 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 5      },      {          \&quot;FieldValueId\&quot;: 57,          \&quot;Value\&quot;: \&quot;9 a 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 6      },      {          \&quot;FieldValueId\&quot;: 58,          \&quot;Value\&quot;: \&quot;Acima de 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 7      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldId Specification Field ID. (required)
     * @return List&lt;GetSpecFieldValue&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<GetSpecFieldValue> specificationsValuesByFieldId(String contentType, String accept, Integer fieldId) throws ApiException {
        ApiResponse<List<GetSpecFieldValue>> localVarResp = specificationsValuesByFieldIdWithHttpInfo(contentType, accept, fieldId);
        return localVarResp.getData();
    }

    /**
     * Get Specification Values By Field ID
     * Gets a list of all specification values from a Specification Field by this field&#39;s ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;FieldValueId\&quot;: 52,          \&quot;Value\&quot;: \&quot;0 a 6 meses\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 1      },      {          \&quot;FieldValueId\&quot;: 53,          \&quot;Value\&quot;: \&quot;1 a 2 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 4      },      {          \&quot;FieldValueId\&quot;: 54,          \&quot;Value\&quot;: \&quot;3 a 4 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 3      },      {          \&quot;FieldValueId\&quot;: 55,          \&quot;Value\&quot;: \&quot;5 a 6 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 2      },      {          \&quot;FieldValueId\&quot;: 56,          \&quot;Value\&quot;: \&quot;7 a 8 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 5      },      {          \&quot;FieldValueId\&quot;: 57,          \&quot;Value\&quot;: \&quot;9 a 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 6      },      {          \&quot;FieldValueId\&quot;: 58,          \&quot;Value\&quot;: \&quot;Acima de 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 7      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldId Specification Field ID. (required)
     * @return ApiResponse&lt;List&lt;GetSpecFieldValue&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<GetSpecFieldValue>> specificationsValuesByFieldIdWithHttpInfo(String contentType, String accept, Integer fieldId) throws ApiException {
        okhttp3.Call localVarCall = specificationsValuesByFieldIdValidateBeforeCall(contentType, accept, fieldId, null);
        Type localVarReturnType = new TypeToken<List<GetSpecFieldValue>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Specification Values By Field ID (asynchronously)
     * Gets a list of all specification values from a Specification Field by this field&#39;s ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;FieldValueId\&quot;: 52,          \&quot;Value\&quot;: \&quot;0 a 6 meses\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 1      },      {          \&quot;FieldValueId\&quot;: 53,          \&quot;Value\&quot;: \&quot;1 a 2 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 4      },      {          \&quot;FieldValueId\&quot;: 54,          \&quot;Value\&quot;: \&quot;3 a 4 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 3      },      {          \&quot;FieldValueId\&quot;: 55,          \&quot;Value\&quot;: \&quot;5 a 6 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 2      },      {          \&quot;FieldValueId\&quot;: 56,          \&quot;Value\&quot;: \&quot;7 a 8 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 5      },      {          \&quot;FieldValueId\&quot;: 57,          \&quot;Value\&quot;: \&quot;9 a 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 6      },      {          \&quot;FieldValueId\&quot;: 58,          \&quot;Value\&quot;: \&quot;Acima de 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 7      }  ]  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param fieldId Specification Field ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call specificationsValuesByFieldIdAsync(String contentType, String accept, Integer fieldId, final ApiCallback<List<GetSpecFieldValue>> _callback) throws ApiException {

        okhttp3.Call localVarCall = specificationsValuesByFieldIdValidateBeforeCall(contentType, accept, fieldId, _callback);
        Type localVarReturnType = new TypeToken<List<GetSpecFieldValue>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
