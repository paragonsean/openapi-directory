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

import org.openapitools.client.ApiException;
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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LegacySubcollectionApi
 */
@Disabled
public class LegacySubcollectionApiTest {

    private final LegacySubcollectionApi api = new LegacySubcollectionApi();

    /**
     * Reposition SKU on the Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {       \&quot;skuId\&quot;: 1,       \&quot;position\&quot;: 1,       \&quot;subCollectionId\&quot;: 17  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtCollectionCollectionIdPositionPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer collectionId = null;
        ApiCatalogPvtCollectionCollectionIdPositionPostRequest apiCatalogPvtCollectionCollectionIdPositionPostRequest = null;
        api.apiCatalogPvtCollectionCollectionIdPositionPost(contentType, accept, collectionId, apiCatalogPvtCollectionCollectionIdPositionPostRequest);
        // TODO: test validations
    }

    /**
     * Get Subcollection by Collection ID
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 12,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Subcollection\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: true      },      {          \&quot;Id\&quot;: 13,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Test\&quot;,          \&quot;Type\&quot;: \&quot;Exclusive\&quot;,          \&quot;PreSale\&quot;: true,          \&quot;Release\&quot;: false      },      {          \&quot;Id\&quot;: 14,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;asdfghj\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: false      }  ]  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtCollectionCollectionIdSubcollectionGetTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer collectionId = null;
        List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner> response = api.apiCatalogPvtCollectionCollectionIdSubcollectionGet(contentType, accept, collectionId);
        // TODO: test validations
    }

    /**
     * Create Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        ApiCatalogPvtSubcollectionPostRequest apiCatalogPvtSubcollectionPostRequest = null;
        ApiCatalogPvtSubcollectionPost200Response response = api.apiCatalogPvtSubcollectionPost(contentType, accept, apiCatalogPvtSubcollectionPostRequest);
        // TODO: test validations
    }

    /**
     * Delete Brand from Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        Integer brandId = null;
        api.apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(contentType, accept, subCollectionId, brandId);
        // TODO: test validations
    }

    /**
     * Delete Category from Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        Integer categoryId = null;
        api.apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(contentType, accept, subCollectionId, categoryId);
        // TODO: test validations
    }

    /**
     * Associate Brand to Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdBrandPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        RequestBody10 requestBody10 = null;
        ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response response = api.apiCatalogPvtSubcollectionSubCollectionIdBrandPost(contentType, accept, subCollectionId, requestBody10);
        // TODO: test validations
    }

    /**
     * Associate Category to Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdCategoryPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        RequestBody11 requestBody11 = null;
        ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response response = api.apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(contentType, accept, subCollectionId, requestBody11);
        // TODO: test validations
    }

    /**
     * Delete Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        api.apiCatalogPvtSubcollectionSubCollectionIdDelete(contentType, accept, subCollectionId);
        // TODO: test validations
    }

    /**
     * Get Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdGetTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        ApiCatalogPvtSubcollectionPost200Response response = api.apiCatalogPvtSubcollectionSubCollectionIdGet(contentType, accept, subCollectionId);
        // TODO: test validations
    }

    /**
     * Update Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdPutTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        ApiCatalogPvtSubcollectionSubCollectionIdPutRequest apiCatalogPvtSubcollectionSubCollectionIdPutRequest = null;
        ApiCatalogPvtSubcollectionPost200Response response = api.apiCatalogPvtSubcollectionSubCollectionIdPut(contentType, accept, subCollectionId, apiCatalogPvtSubcollectionSubCollectionIdPutRequest);
        // TODO: test validations
    }

    /**
     * Add SKU to Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        RequestBody12 requestBody12 = null;
        ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response response = api.apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(contentType, accept, subCollectionId, requestBody12);
        // TODO: test validations
    }

    /**
     * Delete SKU from Subcollection
     *
     *  &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer subCollectionId = null;
        Integer skuId = null;
        api.apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(contentType, accept, subCollectionId, skuId);
        // TODO: test validations
    }

}
