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


import org.openapitools.client.model.ApiCatalogPvtAttachmentsGet200Response;
import org.openapitools.client.model.AttachmentRequest;
import org.openapitools.client.model.AttachmentResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AttachmentApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AttachmentApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AttachmentApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtAttachmentAttachmentidDelete
     * @param attachmentid Attachment ID. (required)
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
    public okhttp3.Call apiCatalogPvtAttachmentAttachmentidDeleteCall(String attachmentid, String contentType, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/attachment/{attachmentid}"
            .replace("{" + "attachmentid" + "}", localVarApiClient.escapeString(attachmentid.toString()));

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
    private okhttp3.Call apiCatalogPvtAttachmentAttachmentidDeleteValidateBeforeCall(String attachmentid, String contentType, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'attachmentid' is set
        if (attachmentid == null) {
            throw new ApiException("Missing the required parameter 'attachmentid' when calling apiCatalogPvtAttachmentAttachmentidDelete(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentAttachmentidDelete(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentAttachmentidDelete(Async)");
        }

        return apiCatalogPvtAttachmentAttachmentidDeleteCall(attachmentid, contentType, accept, _callback);

    }

    /**
     * Delete attachment
     * Deletes a previously existing SKU attachment.
     * @param attachmentid Attachment ID. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void apiCatalogPvtAttachmentAttachmentidDelete(String attachmentid, String contentType, String accept) throws ApiException {
        apiCatalogPvtAttachmentAttachmentidDeleteWithHttpInfo(attachmentid, contentType, accept);
    }

    /**
     * Delete attachment
     * Deletes a previously existing SKU attachment.
     * @param attachmentid Attachment ID. (required)
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
    public ApiResponse<Void> apiCatalogPvtAttachmentAttachmentidDeleteWithHttpInfo(String attachmentid, String contentType, String accept) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtAttachmentAttachmentidDeleteValidateBeforeCall(attachmentid, contentType, accept, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete attachment (asynchronously)
     * Deletes a previously existing SKU attachment.
     * @param attachmentid Attachment ID. (required)
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
    public okhttp3.Call apiCatalogPvtAttachmentAttachmentidDeleteAsync(String attachmentid, String contentType, String accept, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtAttachmentAttachmentidDeleteValidateBeforeCall(attachmentid, contentType, accept, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtAttachmentAttachmentidGet
     * @param attachmentid Attachment ID. (required)
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
    public okhttp3.Call apiCatalogPvtAttachmentAttachmentidGetCall(String attachmentid, String contentType, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/attachment/{attachmentid}"
            .replace("{" + "attachmentid" + "}", localVarApiClient.escapeString(attachmentid.toString()));

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
    private okhttp3.Call apiCatalogPvtAttachmentAttachmentidGetValidateBeforeCall(String attachmentid, String contentType, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'attachmentid' is set
        if (attachmentid == null) {
            throw new ApiException("Missing the required parameter 'attachmentid' when calling apiCatalogPvtAttachmentAttachmentidGet(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentAttachmentidGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentAttachmentidGet(Async)");
        }

        return apiCatalogPvtAttachmentAttachmentidGetCall(attachmentid, contentType, accept, _callback);

    }

    /**
     * Get attachment
     * Gets information about a registered attachment.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param attachmentid Attachment ID. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return AttachmentResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public AttachmentResponse apiCatalogPvtAttachmentAttachmentidGet(String attachmentid, String contentType, String accept) throws ApiException {
        ApiResponse<AttachmentResponse> localVarResp = apiCatalogPvtAttachmentAttachmentidGetWithHttpInfo(attachmentid, contentType, accept);
        return localVarResp.getData();
    }

    /**
     * Get attachment
     * Gets information about a registered attachment.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param attachmentid Attachment ID. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return ApiResponse&lt;AttachmentResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AttachmentResponse> apiCatalogPvtAttachmentAttachmentidGetWithHttpInfo(String attachmentid, String contentType, String accept) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtAttachmentAttachmentidGetValidateBeforeCall(attachmentid, contentType, accept, null);
        Type localVarReturnType = new TypeToken<AttachmentResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get attachment (asynchronously)
     * Gets information about a registered attachment.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param attachmentid Attachment ID. (required)
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
    public okhttp3.Call apiCatalogPvtAttachmentAttachmentidGetAsync(String attachmentid, String contentType, String accept, final ApiCallback<AttachmentResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtAttachmentAttachmentidGetValidateBeforeCall(attachmentid, contentType, accept, _callback);
        Type localVarReturnType = new TypeToken<AttachmentResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtAttachmentAttachmentidPut
     * @param attachmentid Attachment ID. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtAttachmentAttachmentidPutCall(String attachmentid, String contentType, String accept, AttachmentRequest attachmentRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = attachmentRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/attachment/{attachmentid}"
            .replace("{" + "attachmentid" + "}", localVarApiClient.escapeString(attachmentid.toString()));

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
    private okhttp3.Call apiCatalogPvtAttachmentAttachmentidPutValidateBeforeCall(String attachmentid, String contentType, String accept, AttachmentRequest attachmentRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'attachmentid' is set
        if (attachmentid == null) {
            throw new ApiException("Missing the required parameter 'attachmentid' when calling apiCatalogPvtAttachmentAttachmentidPut(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentAttachmentidPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentAttachmentidPut(Async)");
        }

        return apiCatalogPvtAttachmentAttachmentidPutCall(attachmentid, contentType, accept, attachmentRequest, _callback);

    }

    /**
     * Update attachment
     * Updates a previously existing SKU attachment with new information.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param attachmentid Attachment ID. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @return AttachmentResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public AttachmentResponse apiCatalogPvtAttachmentAttachmentidPut(String attachmentid, String contentType, String accept, AttachmentRequest attachmentRequest) throws ApiException {
        ApiResponse<AttachmentResponse> localVarResp = apiCatalogPvtAttachmentAttachmentidPutWithHttpInfo(attachmentid, contentType, accept, attachmentRequest);
        return localVarResp.getData();
    }

    /**
     * Update attachment
     * Updates a previously existing SKU attachment with new information.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param attachmentid Attachment ID. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @return ApiResponse&lt;AttachmentResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AttachmentResponse> apiCatalogPvtAttachmentAttachmentidPutWithHttpInfo(String attachmentid, String contentType, String accept, AttachmentRequest attachmentRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtAttachmentAttachmentidPutValidateBeforeCall(attachmentid, contentType, accept, attachmentRequest, null);
        Type localVarReturnType = new TypeToken<AttachmentResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update attachment (asynchronously)
     * Updates a previously existing SKU attachment with new information.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param attachmentid Attachment ID. (required)
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtAttachmentAttachmentidPutAsync(String attachmentid, String contentType, String accept, AttachmentRequest attachmentRequest, final ApiCallback<AttachmentResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtAttachmentAttachmentidPutValidateBeforeCall(attachmentid, contentType, accept, attachmentRequest, _callback);
        Type localVarReturnType = new TypeToken<AttachmentResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtAttachmentPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtAttachmentPostCall(String contentType, String accept, AttachmentRequest attachmentRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = attachmentRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/attachment";

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
    private okhttp3.Call apiCatalogPvtAttachmentPostValidateBeforeCall(String contentType, String accept, AttachmentRequest attachmentRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentPost(Async)");
        }

        return apiCatalogPvtAttachmentPostCall(contentType, accept, attachmentRequest, _callback);

    }

    /**
     * Create attachment
     * Creates a new SKU attachment.   &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @return AttachmentResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public AttachmentResponse apiCatalogPvtAttachmentPost(String contentType, String accept, AttachmentRequest attachmentRequest) throws ApiException {
        ApiResponse<AttachmentResponse> localVarResp = apiCatalogPvtAttachmentPostWithHttpInfo(contentType, accept, attachmentRequest);
        return localVarResp.getData();
    }

    /**
     * Create attachment
     * Creates a new SKU attachment.   &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @return ApiResponse&lt;AttachmentResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AttachmentResponse> apiCatalogPvtAttachmentPostWithHttpInfo(String contentType, String accept, AttachmentRequest attachmentRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtAttachmentPostValidateBeforeCall(contentType, accept, attachmentRequest, null);
        Type localVarReturnType = new TypeToken<AttachmentResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create attachment (asynchronously)
     * Creates a new SKU attachment.   &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param attachmentRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtAttachmentPostAsync(String contentType, String accept, AttachmentRequest attachmentRequest, final ApiCallback<AttachmentResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtAttachmentPostValidateBeforeCall(contentType, accept, attachmentRequest, _callback);
        Type localVarReturnType = new TypeToken<AttachmentResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtAttachmentsGet
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
    public okhttp3.Call apiCatalogPvtAttachmentsGetCall(String contentType, String accept, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/attachments";

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
    private okhttp3.Call apiCatalogPvtAttachmentsGetValidateBeforeCall(String contentType, String accept, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentsGet(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentsGet(Async)");
        }

        return apiCatalogPvtAttachmentsGetCall(contentType, accept, _callback);

    }

    /**
     * Get all attachments
     * Retrieves information about all registered attachments.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Page\&quot;: 1,      \&quot;Size\&quot;: 11,      \&quot;TotalRows\&quot;: 11,      \&quot;TotalPage\&quot;: 1,      \&quot;Data\&quot;: [          {              \&quot;Id\&quot;: 1,              \&quot;Name\&quot;: \&quot;Acessórios do bicho\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;extra\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-3]#1[1-2][1]pricetable1;#3[0-2][0]pricetable2;#5[0-2][0]pricetable3\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 2,              \&quot;Name\&quot;: \&quot;Sobrenome\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Assinatura Teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot; vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 day, 7 day, 1 month, 6 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.begin\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.end\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;31\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1, 2, 20, 31\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 5,              \&quot;Name\&quot;: \&quot;teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 6,              \&quot;Name\&quot;: \&quot;teste2\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 7,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste3\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 8,              \&quot;Name\&quot;: \&quot;teste api nova\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;Basic teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 9,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 10,              \&quot;Name\&quot;: \&quot;Montagens\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 11,              \&quot;Name\&quot;: \&quot;vtex.subscription.subscription\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1,15,28\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 12,              \&quot;Name\&quot;: \&quot;T-Shirt Customization\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;T-Shirt Name\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[]\&quot;                  }              ]          }      ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return ApiCatalogPvtAttachmentsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtAttachmentsGet200Response apiCatalogPvtAttachmentsGet(String contentType, String accept) throws ApiException {
        ApiResponse<ApiCatalogPvtAttachmentsGet200Response> localVarResp = apiCatalogPvtAttachmentsGetWithHttpInfo(contentType, accept);
        return localVarResp.getData();
    }

    /**
     * Get all attachments
     * Retrieves information about all registered attachments.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Page\&quot;: 1,      \&quot;Size\&quot;: 11,      \&quot;TotalRows\&quot;: 11,      \&quot;TotalPage\&quot;: 1,      \&quot;Data\&quot;: [          {              \&quot;Id\&quot;: 1,              \&quot;Name\&quot;: \&quot;Acessórios do bicho\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;extra\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-3]#1[1-2][1]pricetable1;#3[0-2][0]pricetable2;#5[0-2][0]pricetable3\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 2,              \&quot;Name\&quot;: \&quot;Sobrenome\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Assinatura Teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot; vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 day, 7 day, 1 month, 6 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.begin\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.end\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;31\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1, 2, 20, 31\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 5,              \&quot;Name\&quot;: \&quot;teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 6,              \&quot;Name\&quot;: \&quot;teste2\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 7,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste3\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 8,              \&quot;Name\&quot;: \&quot;teste api nova\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;Basic teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 9,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 10,              \&quot;Name\&quot;: \&quot;Montagens\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 11,              \&quot;Name\&quot;: \&quot;vtex.subscription.subscription\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1,15,28\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 12,              \&quot;Name\&quot;: \&quot;T-Shirt Customization\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;T-Shirt Name\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[]\&quot;                  }              ]          }      ]  }  &#x60;&#x60;&#x60;
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @return ApiResponse&lt;ApiCatalogPvtAttachmentsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtAttachmentsGet200Response> apiCatalogPvtAttachmentsGetWithHttpInfo(String contentType, String accept) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtAttachmentsGetValidateBeforeCall(contentType, accept, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtAttachmentsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get all attachments (asynchronously)
     * Retrieves information about all registered attachments.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Page\&quot;: 1,      \&quot;Size\&quot;: 11,      \&quot;TotalRows\&quot;: 11,      \&quot;TotalPage\&quot;: 1,      \&quot;Data\&quot;: [          {              \&quot;Id\&quot;: 1,              \&quot;Name\&quot;: \&quot;Acessórios do bicho\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;extra\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-3]#1[1-2][1]pricetable1;#3[0-2][0]pricetable2;#5[0-2][0]pricetable3\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 2,              \&quot;Name\&quot;: \&quot;Sobrenome\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Assinatura Teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot; vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 day, 7 day, 1 month, 6 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.begin\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.end\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;31\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1, 2, 20, 31\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 5,              \&quot;Name\&quot;: \&quot;teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 6,              \&quot;Name\&quot;: \&quot;teste2\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 7,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste3\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 8,              \&quot;Name\&quot;: \&quot;teste api nova\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;Basic teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 9,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 10,              \&quot;Name\&quot;: \&quot;Montagens\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 11,              \&quot;Name\&quot;: \&quot;vtex.subscription.subscription\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1,15,28\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 12,              \&quot;Name\&quot;: \&quot;T-Shirt Customization\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;T-Shirt Name\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[]\&quot;                  }              ]          }      ]  }  &#x60;&#x60;&#x60;
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
    public okhttp3.Call apiCatalogPvtAttachmentsGetAsync(String contentType, String accept, final ApiCallback<ApiCatalogPvtAttachmentsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtAttachmentsGetValidateBeforeCall(contentType, accept, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtAttachmentsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
