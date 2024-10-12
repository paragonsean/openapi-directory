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


import org.openapitools.client.model.ApiCatalogPvtProductPost200Response;
import org.openapitools.client.model.ApiCatalogPvtProductPostRequest;
import org.openapitools.client.model.ApiCatalogPvtProductProductIdPutRequest;
import java.math.BigDecimal;
import org.openapitools.client.model.GetProductbyid200Response;
import org.openapitools.client.model.ProductAndSkuIds200Response;
import org.openapitools.client.model.ProductVariations200Response;
import org.openapitools.client.model.ProductandTradePolicy200Response;
import org.openapitools.client.model.ProductbyRefId200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductApi(ApiClient apiClient) {
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
     * Build call for apiCatalogPvtProductPost
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtProductPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductPostCall(String contentType, String accept, ApiCatalogPvtProductPostRequest apiCatalogPvtProductPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtProductPostRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/product";

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
    private okhttp3.Call apiCatalogPvtProductPostValidateBeforeCall(String contentType, String accept, ApiCatalogPvtProductPostRequest apiCatalogPvtProductPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtProductPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtProductPost(Async)");
        }

        return apiCatalogPvtProductPostCall(contentType, accept, apiCatalogPvtProductPostRequest, _callback);

    }

    /**
     * Create Product with Category and Brand
     * This endpoint allows two types of request:    **Type 1:** Creating a new Product as well as a new Category path (including subcategories) and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60; parameters.    **Type 2:** Creating a new Product given an existing &#x60;BrandId&#x60; and an existing &#x60;CategoryId&#x60;.    When creating a product, regardless of the type of request, if there is a need to create a new product with a specific custom product ID, specify the &#x60;Id&#x60; (integer) in the request body. Otherwise, VTEX will generate the ID automatically.     ## Request body examples     ### Type 1     Request to create a product, associating it to a new Category and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60;:    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;CategoryPath\&quot;: \&quot;Mens/Clothing/T-Shirts\&quot;,      \&quot;BrandName\&quot;: \&quot;Nike\&quot;,      \&quot;RefId\&quot;: \&quot;31011706925\&quot;,      \&quot;Title\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;LinkId\&quot;: \&quot;tshirt-black\&quot;,      \&quot;Description\&quot;: \&quot;This is a cool Tshirt\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2022-01-01T00:00:00\&quot;,      \&quot;IsVisible\&quot;: true,      \&quot;IsActive\&quot;: true,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;MetaTagDescription\&quot;: \&quot;tshirt black\&quot;,      \&quot;ShowWithoutStock\&quot;: true,      \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ### Type 2    Request to create a product, associating it to an existing &#x60;CategoryId&#x60; and &#x60;BrandId&#x60;:    &#x60;&#x60;&#x60;json  {     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 52,     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;      &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtProductPostRequest  (optional)
     * @return ApiCatalogPvtProductPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtProductPost200Response apiCatalogPvtProductPost(String contentType, String accept, ApiCatalogPvtProductPostRequest apiCatalogPvtProductPostRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtProductPost200Response> localVarResp = apiCatalogPvtProductPostWithHttpInfo(contentType, accept, apiCatalogPvtProductPostRequest);
        return localVarResp.getData();
    }

    /**
     * Create Product with Category and Brand
     * This endpoint allows two types of request:    **Type 1:** Creating a new Product as well as a new Category path (including subcategories) and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60; parameters.    **Type 2:** Creating a new Product given an existing &#x60;BrandId&#x60; and an existing &#x60;CategoryId&#x60;.    When creating a product, regardless of the type of request, if there is a need to create a new product with a specific custom product ID, specify the &#x60;Id&#x60; (integer) in the request body. Otherwise, VTEX will generate the ID automatically.     ## Request body examples     ### Type 1     Request to create a product, associating it to a new Category and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60;:    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;CategoryPath\&quot;: \&quot;Mens/Clothing/T-Shirts\&quot;,      \&quot;BrandName\&quot;: \&quot;Nike\&quot;,      \&quot;RefId\&quot;: \&quot;31011706925\&quot;,      \&quot;Title\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;LinkId\&quot;: \&quot;tshirt-black\&quot;,      \&quot;Description\&quot;: \&quot;This is a cool Tshirt\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2022-01-01T00:00:00\&quot;,      \&quot;IsVisible\&quot;: true,      \&quot;IsActive\&quot;: true,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;MetaTagDescription\&quot;: \&quot;tshirt black\&quot;,      \&quot;ShowWithoutStock\&quot;: true,      \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ### Type 2    Request to create a product, associating it to an existing &#x60;CategoryId&#x60; and &#x60;BrandId&#x60;:    &#x60;&#x60;&#x60;json  {     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 52,     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;      &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtProductPostRequest  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtProductPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtProductPost200Response> apiCatalogPvtProductPostWithHttpInfo(String contentType, String accept, ApiCatalogPvtProductPostRequest apiCatalogPvtProductPostRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtProductPostValidateBeforeCall(contentType, accept, apiCatalogPvtProductPostRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtProductPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create Product with Category and Brand (asynchronously)
     * This endpoint allows two types of request:    **Type 1:** Creating a new Product as well as a new Category path (including subcategories) and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60; parameters.    **Type 2:** Creating a new Product given an existing &#x60;BrandId&#x60; and an existing &#x60;CategoryId&#x60;.    When creating a product, regardless of the type of request, if there is a need to create a new product with a specific custom product ID, specify the &#x60;Id&#x60; (integer) in the request body. Otherwise, VTEX will generate the ID automatically.     ## Request body examples     ### Type 1     Request to create a product, associating it to a new Category and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60;:    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;CategoryPath\&quot;: \&quot;Mens/Clothing/T-Shirts\&quot;,      \&quot;BrandName\&quot;: \&quot;Nike\&quot;,      \&quot;RefId\&quot;: \&quot;31011706925\&quot;,      \&quot;Title\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;LinkId\&quot;: \&quot;tshirt-black\&quot;,      \&quot;Description\&quot;: \&quot;This is a cool Tshirt\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2022-01-01T00:00:00\&quot;,      \&quot;IsVisible\&quot;: true,      \&quot;IsActive\&quot;: true,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;MetaTagDescription\&quot;: \&quot;tshirt black\&quot;,      \&quot;ShowWithoutStock\&quot;: true,      \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ### Type 2    Request to create a product, associating it to an existing &#x60;CategoryId&#x60; and &#x60;BrandId&#x60;:    &#x60;&#x60;&#x60;json  {     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 52,     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;      &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param apiCatalogPvtProductPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductPostAsync(String contentType, String accept, ApiCatalogPvtProductPostRequest apiCatalogPvtProductPostRequest, final ApiCallback<ApiCatalogPvtProductPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtProductPostValidateBeforeCall(contentType, accept, apiCatalogPvtProductPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtProductPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiCatalogPvtProductProductIdPut
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdPutCall(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiCatalogPvtProductProductIdPutRequest;

        // create path and map variables
        String localVarPath = "/api/catalog/pvt/product/{productId}"
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
    private okhttp3.Call apiCatalogPvtProductProductIdPutValidateBeforeCall(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiCatalogPvtProductProductIdPut(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiCatalogPvtProductProductIdPut(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling apiCatalogPvtProductProductIdPut(Async)");
        }

        return apiCatalogPvtProductProductIdPutCall(contentType, accept, productId, apiCatalogPvtProductProductIdPutRequest, _callback);

    }

    /**
     * Update Product
     * Updates an existing Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdPutRequest  (optional)
     * @return ApiCatalogPvtProductPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiCatalogPvtProductPost200Response apiCatalogPvtProductProductIdPut(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest) throws ApiException {
        ApiResponse<ApiCatalogPvtProductPost200Response> localVarResp = apiCatalogPvtProductProductIdPutWithHttpInfo(contentType, accept, productId, apiCatalogPvtProductProductIdPutRequest);
        return localVarResp.getData();
    }

    /**
     * Update Product
     * Updates an existing Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdPutRequest  (optional)
     * @return ApiResponse&lt;ApiCatalogPvtProductPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApiCatalogPvtProductPost200Response> apiCatalogPvtProductProductIdPutWithHttpInfo(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdPutValidateBeforeCall(contentType, accept, productId, apiCatalogPvtProductProductIdPutRequest, null);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtProductPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update Product (asynchronously)
     * Updates an existing Product.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @param apiCatalogPvtProductProductIdPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiCatalogPvtProductProductIdPutAsync(String contentType, String accept, Integer productId, ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest, final ApiCallback<ApiCatalogPvtProductPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiCatalogPvtProductProductIdPutValidateBeforeCall(contentType, accept, productId, apiCatalogPvtProductProductIdPutRequest, _callback);
        Type localVarReturnType = new TypeToken<ApiCatalogPvtProductPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProductbyid
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
    public okhttp3.Call getProductbyidCall(String contentType, String accept, String productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog/pvt/product/{productId}"
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
    private okhttp3.Call getProductbyidValidateBeforeCall(String contentType, String accept, String productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getProductbyid(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getProductbyid(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling getProductbyid(Async)");
        }

        return getProductbyidCall(contentType, accept, productId, _callback);

    }

    /**
     * Get Product by ID
     * Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return GetProductbyid200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetProductbyid200Response getProductbyid(String contentType, String accept, String productId) throws ApiException {
        ApiResponse<GetProductbyid200Response> localVarResp = getProductbyidWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get Product by ID
     * Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;GetProductbyid200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetProductbyid200Response> getProductbyidWithHttpInfo(String contentType, String accept, String productId) throws ApiException {
        okhttp3.Call localVarCall = getProductbyidValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<GetProductbyid200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product by ID (asynchronously)
     * Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
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
    public okhttp3.Call getProductbyidAsync(String contentType, String accept, String productId, final ApiCallback<GetProductbyid200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProductbyidValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<GetProductbyid200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productAndSkuIds
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId ID of the category from which you need to retrieve Products and SKUs. (optional)
     * @param from Insert the ID that will start the request result. (optional)
     * @param to Insert the ID that will end the request result. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productAndSkuIdsCall(String contentType, String accept, Integer categoryId, Integer from, Integer to, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/products/GetProductAndSkuIds";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (categoryId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("categoryId", categoryId));
        }

        if (from != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("_from", from));
        }

        if (to != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("_to", to));
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
    private okhttp3.Call productAndSkuIdsValidateBeforeCall(String contentType, String accept, Integer categoryId, Integer from, Integer to, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling productAndSkuIds(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling productAndSkuIds(Async)");
        }

        return productAndSkuIdsCall(contentType, accept, categoryId, from, to, _callback);

    }

    /**
     * Get Product and SKU IDs
     * Retrieves the IDs of products and SKUs.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId ID of the category from which you need to retrieve Products and SKUs. (optional)
     * @param from Insert the ID that will start the request result. (optional)
     * @param to Insert the ID that will end the request result. (optional)
     * @return ProductAndSkuIds200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProductAndSkuIds200Response productAndSkuIds(String contentType, String accept, Integer categoryId, Integer from, Integer to) throws ApiException {
        ApiResponse<ProductAndSkuIds200Response> localVarResp = productAndSkuIdsWithHttpInfo(contentType, accept, categoryId, from, to);
        return localVarResp.getData();
    }

    /**
     * Get Product and SKU IDs
     * Retrieves the IDs of products and SKUs.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId ID of the category from which you need to retrieve Products and SKUs. (optional)
     * @param from Insert the ID that will start the request result. (optional)
     * @param to Insert the ID that will end the request result. (optional)
     * @return ApiResponse&lt;ProductAndSkuIds200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductAndSkuIds200Response> productAndSkuIdsWithHttpInfo(String contentType, String accept, Integer categoryId, Integer from, Integer to) throws ApiException {
        okhttp3.Call localVarCall = productAndSkuIdsValidateBeforeCall(contentType, accept, categoryId, from, to, null);
        Type localVarReturnType = new TypeToken<ProductAndSkuIds200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product and SKU IDs (asynchronously)
     * Retrieves the IDs of products and SKUs.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param categoryId ID of the category from which you need to retrieve Products and SKUs. (optional)
     * @param from Insert the ID that will start the request result. (optional)
     * @param to Insert the ID that will end the request result. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productAndSkuIdsAsync(String contentType, String accept, Integer categoryId, Integer from, Integer to, final ApiCallback<ProductAndSkuIds200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = productAndSkuIdsValidateBeforeCall(contentType, accept, categoryId, from, to, _callback);
        Type localVarReturnType = new TypeToken<ProductAndSkuIds200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productVariations
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
    public okhttp3.Call productVariationsCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pub/products/variations/{productId}"
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
    private okhttp3.Call productVariationsValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling productVariations(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling productVariations(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling productVariations(Async)");
        }

        return productVariationsCall(contentType, accept, productId, _callback);

    }

    /**
     * Get Product&#39;s SKUs by Product ID
     * Retrieves data about the product and all SKUs related to it by the product&#39;s ID.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: 9,      \&quot;name\&quot;: \&quot;Camisa Masculina\&quot;,      \&quot;salesChannel\&quot;: \&quot;2\&quot;,      \&quot;available\&quot;: true,      \&quot;displayMode\&quot;: \&quot;lista\&quot;,      \&quot;dimensions\&quot;: [          \&quot;Cores\&quot;,          \&quot;Tamanho\&quot;,          \&quot;País de origem\&quot;,          \&quot;Gênero\&quot;      ],      \&quot;dimensionsInputType\&quot;: {          \&quot;Cores\&quot;: \&quot;Combo\&quot;,          \&quot;Tamanho\&quot;: \&quot;Combo\&quot;,          \&quot;País de origem\&quot;: \&quot;Combo\&quot;,          \&quot;Gênero\&quot;: \&quot;Combo\&quot;      },      \&quot;dimensionsMap\&quot;: {          \&quot;Cores\&quot;: [              \&quot;Amarelo\&quot;,              \&quot;Azul\&quot;,              \&quot;Vermelho\&quot;          ],          \&quot;Tamanho\&quot;: [              \&quot;P\&quot;,              \&quot;M\&quot;,              \&quot;G\&quot;          ],          \&quot;País de origem\&quot;: [              \&quot;Brasil\&quot;          ],          \&quot;Gênero\&quot;: [              \&quot;Masculino\&quot;          ]      },      \&quot;skus\&quot;: [          {              \&quot;sku\&quot;: 310118454,              \&quot;skuname\&quot;: \&quot;Amarela - G\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Amarelo\&quot;,                  \&quot;Tamanho\&quot;: \&quot;G\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: false,              \&quot;availablequantity\&quot;: 0,              \&quot;cacheVersionUsedToCallCheckout\&quot;: null,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 9.999.876,00\&quot;,              \&quot;bestPrice\&quot;: 999987600,              \&quot;spotPrice\&quot;: 999987600,              \&quot;installments\&quot;: 0,              \&quot;installmentsValue\&quot;: 0,              \&quot;installmentsInsterestRate\&quot;: null,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155467-292-292/image-5d7ad76ad1954c53adecab4138319034.jpg?v&#x3D;637321899584500000\&quot;,              \&quot;sellerId\&quot;: \&quot;1\&quot;,              \&quot;seller\&quot;: \&quot;lojadobreno\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 1.0000,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          },          {              \&quot;sku\&quot;: 310118455,              \&quot;skuname\&quot;: \&quot;Vermelha - M\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Vermelho\&quot;,                  \&quot;Tamanho\&quot;: \&quot;M\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: true,              \&quot;availablequantity\&quot;: 99999,              \&quot;cacheVersionUsedToCallCheckout\&quot;: \&quot;38395F1AEF59DF5CEAEDE472328145CD_\&quot;,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 20,00\&quot;,              \&quot;bestPrice\&quot;: 2000,              \&quot;spotPrice\&quot;: 2000,              \&quot;installments\&quot;: 1,              \&quot;installmentsValue\&quot;: 2000,              \&quot;installmentsInsterestRate\&quot;: 0,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155468-292-292/image-601a6099aace48b89d26fc9f22e8e611.jpg?v&#x3D;637321906602470000\&quot;,              \&quot;sellerId\&quot;: \&quot;pedrostore\&quot;,              \&quot;seller\&quot;: \&quot;pedrostore\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 0.4167,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          }      ]  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ProductVariations200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProductVariations200Response productVariations(String contentType, String accept, Integer productId) throws ApiException {
        ApiResponse<ProductVariations200Response> localVarResp = productVariationsWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get Product&#39;s SKUs by Product ID
     * Retrieves data about the product and all SKUs related to it by the product&#39;s ID.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: 9,      \&quot;name\&quot;: \&quot;Camisa Masculina\&quot;,      \&quot;salesChannel\&quot;: \&quot;2\&quot;,      \&quot;available\&quot;: true,      \&quot;displayMode\&quot;: \&quot;lista\&quot;,      \&quot;dimensions\&quot;: [          \&quot;Cores\&quot;,          \&quot;Tamanho\&quot;,          \&quot;País de origem\&quot;,          \&quot;Gênero\&quot;      ],      \&quot;dimensionsInputType\&quot;: {          \&quot;Cores\&quot;: \&quot;Combo\&quot;,          \&quot;Tamanho\&quot;: \&quot;Combo\&quot;,          \&quot;País de origem\&quot;: \&quot;Combo\&quot;,          \&quot;Gênero\&quot;: \&quot;Combo\&quot;      },      \&quot;dimensionsMap\&quot;: {          \&quot;Cores\&quot;: [              \&quot;Amarelo\&quot;,              \&quot;Azul\&quot;,              \&quot;Vermelho\&quot;          ],          \&quot;Tamanho\&quot;: [              \&quot;P\&quot;,              \&quot;M\&quot;,              \&quot;G\&quot;          ],          \&quot;País de origem\&quot;: [              \&quot;Brasil\&quot;          ],          \&quot;Gênero\&quot;: [              \&quot;Masculino\&quot;          ]      },      \&quot;skus\&quot;: [          {              \&quot;sku\&quot;: 310118454,              \&quot;skuname\&quot;: \&quot;Amarela - G\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Amarelo\&quot;,                  \&quot;Tamanho\&quot;: \&quot;G\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: false,              \&quot;availablequantity\&quot;: 0,              \&quot;cacheVersionUsedToCallCheckout\&quot;: null,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 9.999.876,00\&quot;,              \&quot;bestPrice\&quot;: 999987600,              \&quot;spotPrice\&quot;: 999987600,              \&quot;installments\&quot;: 0,              \&quot;installmentsValue\&quot;: 0,              \&quot;installmentsInsterestRate\&quot;: null,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155467-292-292/image-5d7ad76ad1954c53adecab4138319034.jpg?v&#x3D;637321899584500000\&quot;,              \&quot;sellerId\&quot;: \&quot;1\&quot;,              \&quot;seller\&quot;: \&quot;lojadobreno\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 1.0000,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          },          {              \&quot;sku\&quot;: 310118455,              \&quot;skuname\&quot;: \&quot;Vermelha - M\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Vermelho\&quot;,                  \&quot;Tamanho\&quot;: \&quot;M\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: true,              \&quot;availablequantity\&quot;: 99999,              \&quot;cacheVersionUsedToCallCheckout\&quot;: \&quot;38395F1AEF59DF5CEAEDE472328145CD_\&quot;,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 20,00\&quot;,              \&quot;bestPrice\&quot;: 2000,              \&quot;spotPrice\&quot;: 2000,              \&quot;installments\&quot;: 1,              \&quot;installmentsValue\&quot;: 2000,              \&quot;installmentsInsterestRate\&quot;: 0,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155468-292-292/image-601a6099aace48b89d26fc9f22e8e611.jpg?v&#x3D;637321906602470000\&quot;,              \&quot;sellerId\&quot;: \&quot;pedrostore\&quot;,              \&quot;seller\&quot;: \&quot;pedrostore\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 0.4167,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          }      ]  }  &#x60;&#x60;&#x60;
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;ProductVariations200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductVariations200Response> productVariationsWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = productVariationsValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<ProductVariations200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product&#39;s SKUs by Product ID (asynchronously)
     * Retrieves data about the product and all SKUs related to it by the product&#39;s ID.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: 9,      \&quot;name\&quot;: \&quot;Camisa Masculina\&quot;,      \&quot;salesChannel\&quot;: \&quot;2\&quot;,      \&quot;available\&quot;: true,      \&quot;displayMode\&quot;: \&quot;lista\&quot;,      \&quot;dimensions\&quot;: [          \&quot;Cores\&quot;,          \&quot;Tamanho\&quot;,          \&quot;País de origem\&quot;,          \&quot;Gênero\&quot;      ],      \&quot;dimensionsInputType\&quot;: {          \&quot;Cores\&quot;: \&quot;Combo\&quot;,          \&quot;Tamanho\&quot;: \&quot;Combo\&quot;,          \&quot;País de origem\&quot;: \&quot;Combo\&quot;,          \&quot;Gênero\&quot;: \&quot;Combo\&quot;      },      \&quot;dimensionsMap\&quot;: {          \&quot;Cores\&quot;: [              \&quot;Amarelo\&quot;,              \&quot;Azul\&quot;,              \&quot;Vermelho\&quot;          ],          \&quot;Tamanho\&quot;: [              \&quot;P\&quot;,              \&quot;M\&quot;,              \&quot;G\&quot;          ],          \&quot;País de origem\&quot;: [              \&quot;Brasil\&quot;          ],          \&quot;Gênero\&quot;: [              \&quot;Masculino\&quot;          ]      },      \&quot;skus\&quot;: [          {              \&quot;sku\&quot;: 310118454,              \&quot;skuname\&quot;: \&quot;Amarela - G\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Amarelo\&quot;,                  \&quot;Tamanho\&quot;: \&quot;G\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: false,              \&quot;availablequantity\&quot;: 0,              \&quot;cacheVersionUsedToCallCheckout\&quot;: null,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 9.999.876,00\&quot;,              \&quot;bestPrice\&quot;: 999987600,              \&quot;spotPrice\&quot;: 999987600,              \&quot;installments\&quot;: 0,              \&quot;installmentsValue\&quot;: 0,              \&quot;installmentsInsterestRate\&quot;: null,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155467-292-292/image-5d7ad76ad1954c53adecab4138319034.jpg?v&#x3D;637321899584500000\&quot;,              \&quot;sellerId\&quot;: \&quot;1\&quot;,              \&quot;seller\&quot;: \&quot;lojadobreno\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 1.0000,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          },          {              \&quot;sku\&quot;: 310118455,              \&quot;skuname\&quot;: \&quot;Vermelha - M\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Vermelho\&quot;,                  \&quot;Tamanho\&quot;: \&quot;M\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: true,              \&quot;availablequantity\&quot;: 99999,              \&quot;cacheVersionUsedToCallCheckout\&quot;: \&quot;38395F1AEF59DF5CEAEDE472328145CD_\&quot;,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 20,00\&quot;,              \&quot;bestPrice\&quot;: 2000,              \&quot;spotPrice\&quot;: 2000,              \&quot;installments\&quot;: 1,              \&quot;installmentsValue\&quot;: 2000,              \&quot;installmentsInsterestRate\&quot;: 0,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155468-292-292/image-601a6099aace48b89d26fc9f22e8e611.jpg?v&#x3D;637321906602470000\&quot;,              \&quot;sellerId\&quot;: \&quot;pedrostore\&quot;,              \&quot;seller\&quot;: \&quot;pedrostore\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 0.4167,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          }      ]  }  &#x60;&#x60;&#x60;
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
    public okhttp3.Call productVariationsAsync(String contentType, String accept, Integer productId, final ApiCallback<ProductVariations200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = productVariationsValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<ProductVariations200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productandTradePolicy
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
    public okhttp3.Call productandTradePolicyCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/products/productget/{productId}"
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
    private okhttp3.Call productandTradePolicyValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling productandTradePolicy(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling productandTradePolicy(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling productandTradePolicy(Async)");
        }

        return productandTradePolicyCall(contentType, accept, productId, _callback);

    }

    /**
     * Get Product and its general context
     * Retrieves a specific product&#39;s general information as name, description and the trade policies that it is included.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ProductandTradePolicy200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProductandTradePolicy200Response productandTradePolicy(String contentType, String accept, Integer productId) throws ApiException {
        ApiResponse<ProductandTradePolicy200Response> localVarResp = productandTradePolicyWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get Product and its general context
     * Retrieves a specific product&#39;s general information as name, description and the trade policies that it is included.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;ProductandTradePolicy200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductandTradePolicy200Response> productandTradePolicyWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = productandTradePolicyValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<ProductandTradePolicy200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product and its general context (asynchronously)
     * Retrieves a specific product&#39;s general information as name, description and the trade policies that it is included.
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
    public okhttp3.Call productandTradePolicyAsync(String contentType, String accept, Integer productId, final ApiCallback<ProductandTradePolicy200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = productandTradePolicyValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<ProductandTradePolicy200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productbyRefId
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId Product Referecial Code (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productbyRefIdCall(String contentType, String accept, String refId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/catalog_system/pvt/products/productgetbyrefid/{refId}"
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
    private okhttp3.Call productbyRefIdValidateBeforeCall(String contentType, String accept, String refId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling productbyRefId(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling productbyRefId(Async)");
        }

        // verify the required parameter 'refId' is set
        if (refId == null) {
            throw new ApiException("Missing the required parameter 'refId' when calling productbyRefId(Async)");
        }

        return productbyRefIdCall(contentType, accept, refId, _callback);

    }

    /**
     * Get Product by RefId
     * Retrieves a specific product by its Reference ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId Product Referecial Code (required)
     * @return ProductbyRefId200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProductbyRefId200Response productbyRefId(String contentType, String accept, String refId) throws ApiException {
        ApiResponse<ProductbyRefId200Response> localVarResp = productbyRefIdWithHttpInfo(contentType, accept, refId);
        return localVarResp.getData();
    }

    /**
     * Get Product by RefId
     * Retrieves a specific product by its Reference ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId Product Referecial Code (required)
     * @return ApiResponse&lt;ProductbyRefId200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductbyRefId200Response> productbyRefIdWithHttpInfo(String contentType, String accept, String refId) throws ApiException {
        okhttp3.Call localVarCall = productbyRefIdValidateBeforeCall(contentType, accept, refId, null);
        Type localVarReturnType = new TypeToken<ProductbyRefId200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product by RefId (asynchronously)
     * Retrieves a specific product by its Reference ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param refId Product Referecial Code (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productbyRefIdAsync(String contentType, String accept, String refId, final ApiCallback<ProductbyRefId200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = productbyRefIdValidateBeforeCall(contentType, accept, refId, _callback);
        Type localVarReturnType = new TypeToken<ProductbyRefId200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for reviewRateProduct
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
    public okhttp3.Call reviewRateProductCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/addon/pvt/review/GetProductRate/{productId}"
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
    private okhttp3.Call reviewRateProductValidateBeforeCall(String contentType, String accept, Integer productId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling reviewRateProduct(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling reviewRateProduct(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling reviewRateProduct(Async)");
        }

        return reviewRateProductCall(contentType, accept, productId, _callback);

    }

    /**
     * Get Product Review Rate by Product ID
     * Retrieves the review rate of a product by this product&#39;s ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return BigDecimal
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BigDecimal reviewRateProduct(String contentType, String accept, Integer productId) throws ApiException {
        ApiResponse<BigDecimal> localVarResp = reviewRateProductWithHttpInfo(contentType, accept, productId);
        return localVarResp.getData();
    }

    /**
     * Get Product Review Rate by Product ID
     * Retrieves the review rate of a product by this product&#39;s ID.
     * @param contentType Describes the type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param productId Product’s unique numerical identifier. (required)
     * @return ApiResponse&lt;BigDecimal&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BigDecimal> reviewRateProductWithHttpInfo(String contentType, String accept, Integer productId) throws ApiException {
        okhttp3.Call localVarCall = reviewRateProductValidateBeforeCall(contentType, accept, productId, null);
        Type localVarReturnType = new TypeToken<BigDecimal>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Product Review Rate by Product ID (asynchronously)
     * Retrieves the review rate of a product by this product&#39;s ID.
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
    public okhttp3.Call reviewRateProductAsync(String contentType, String accept, Integer productId, final ApiCallback<BigDecimal> _callback) throws ApiException {

        okhttp3.Call localVarCall = reviewRateProductValidateBeforeCall(contentType, accept, productId, _callback);
        Type localVarReturnType = new TypeToken<BigDecimal>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
