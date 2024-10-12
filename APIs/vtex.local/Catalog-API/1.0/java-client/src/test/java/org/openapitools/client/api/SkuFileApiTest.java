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
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner;
import org.openapitools.client.model.ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response;
import java.io.File;
import org.openapitools.client.model.SKUFileURL;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SkuFileApi
 */
@Disabled
public class SkuFileApiTest {

    private final SkuFileApi api = new SkuFileApi();

    /**
     * Copy Files from an SKU to another SKU
     *
     * Copy all existing files from an SKU to another SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1964,          \&quot;ArchiveId\&quot;: 155404,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;\&quot;      },      {          \&quot;Id\&quot;: 1965,          \&quot;ArchiveId\&quot;: 155429,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePutTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuIdfrom = null;
        Integer skuIdto = null;
        List<ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner> response = api.apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(contentType, accept, skuIdfrom, skuIdto);
        // TODO: test validations
    }

    /**
     * Disassociate SKU File
     *
     * Disassociates an SKU File from an SKU.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        Integer skuFileId = null;
        api.apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId);
        // TODO: test validations
    }

    /**
     * Delete All SKU Files
     *
     * Deletes all SKU Image Files.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdFileDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        api.apiCatalogPvtStockkeepingunitSkuIdFileDelete(contentType, accept, skuId);
        // TODO: test validations
    }

    /**
     * Get SKU Files
     *
     * Gets general information about all Files in the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 549,          \&quot;ArchiveId\&quot;: 155485,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;chimera-cat-quimera-5\&quot;,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;miau\&quot;      },      {          \&quot;Id\&quot;: 550,          \&quot;ArchiveId\&quot;: 155486,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Gato-siames\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;Gato siames\&quot;      },      {          \&quot;Id\&quot;: 555,          \&quot;ArchiveId\&quot;: 155491,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Cat-Sleeping-Pics\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: null      }  ]  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdFileGetTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        List<ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner> response = api.apiCatalogPvtStockkeepingunitSkuIdFileGet(contentType, accept, skuId);
        // TODO: test validations
    }

    /**
     * Create SKU File
     *
     * Creates a new Image for an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;Text\&quot;: null,        \&quot;Url\&quot;: \&quot;https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\&quot;          }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {        \&quot;Id\&quot;: 503,        \&quot;ArchiveId\&quot;: 155491,        \&quot;SkuId\&quot;: 1,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdFilePostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        SKUFileURL skUFileURL = null;
        ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response response = api.apiCatalogPvtStockkeepingunitSkuIdFilePost(contentType, accept, skuId, skUFileURL);
        // TODO: test validations
    }

    /**
     * Delete SKU Image File
     *
     * Deletes a specific SKU Image File.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        Integer skuFileId = null;
        api.apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId);
        // TODO: test validations
    }

    /**
     * Update SKU File
     *
     * Updates a new Image on an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null,      \&quot;Name\&quot;: \&quot;toilet-paper\&quot;,      \&quot;Text\&quot;: null,      \&quot;Url\&quot;: \&quot;https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 508,      \&quot;ArchiveId\&quot;: 155491,      \&quot;SkuId\&quot;: 7,      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPutTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        Integer skuFileId = null;
        SKUFileURL skUFileURL = null;
        ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response response = api.apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(contentType, accept, skuId, skuFileId, skUFileURL);
        // TODO: test validations
    }

}
