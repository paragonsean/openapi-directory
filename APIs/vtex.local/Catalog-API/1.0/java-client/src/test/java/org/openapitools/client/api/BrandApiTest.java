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
import org.openapitools.client.model.BrandCreateUpdate;
import org.openapitools.client.model.BrandGet;
import org.openapitools.client.model.BrandListPerPage200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for BrandApi
 */
@Disabled
public class BrandApiTest {

    private final BrandApi api = new BrandApi();

    /**
     * Delete Brand
     *
     * Deletes an existing Brand.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtBrandBrandIdDeleteTest() throws ApiException {
        String brandId = null;
        String contentType = null;
        String accept = null;
        api.apiCatalogPvtBrandBrandIdDelete(brandId, contentType, accept);
        // TODO: test validations
    }

    /**
     * Get Brand and context
     *
     * Retrieves information about a specific Brand and its context.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtBrandBrandIdGetTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String brandId = null;
        BrandCreateUpdate response = api.apiCatalogPvtBrandBrandIdGet(contentType, accept, brandId);
        // TODO: test validations
    }

    /**
     * Update Brand
     *
     * Updates a previously existing Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtBrandBrandIdPutTest() throws ApiException {
        String brandId = null;
        String contentType = null;
        String accept = null;
        BrandCreateUpdate brandCreateUpdate = null;
        BrandCreateUpdate response = api.apiCatalogPvtBrandBrandIdPut(brandId, contentType, accept, brandCreateUpdate);
        // TODO: test validations
    }

    /**
     * Create Brand
     *
     * Creates a new Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtBrandPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        BrandCreateUpdate brandCreateUpdate = null;
        BrandCreateUpdate response = api.apiCatalogPvtBrandPost(contentType, accept, brandCreateUpdate);
        // TODO: test validations
    }

    /**
     * Get Brand
     *
     * Retrieves a specific Brand by its ID.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: 7000000,    \&quot;name\&quot;: \&quot;Pedigree\&quot;,    \&quot;isActive\&quot;: true,    \&quot;title\&quot;: \&quot;Pedigree\&quot;,    \&quot;metaTagDescription\&quot;: \&quot;Pedigree\&quot;,    \&quot;imageUrl\&quot;: null  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void brandTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String brandId = null;
        BrandGet response = api.brand(contentType, accept, brandId);
        // TODO: test validations
    }

    /**
     * Get Brand List
     *
     * Retrieves all Brands registered in the store&#39;s Catalog.   &gt;⚠️ This route&#39;s response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    &#x60;&#x60;&#x60;json  [    {      \&quot;id\&quot;: 9280,      \&quot;name\&quot;: \&quot;Brand\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Brand\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Brand\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000000,      \&quot;name\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000001,      \&quot;name\&quot;: \&quot;Pedigree\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Pedigree\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;\&quot;,      \&quot;imageUrl\&quot;: null    }  ]  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void brandListTest() throws ApiException {
        String contentType = null;
        String accept = null;
        List<BrandGet> response = api.brandList(contentType, accept);
        // TODO: test validations
    }

    /**
     * Get Brand List Per Page
     *
     * Retrieves all Brands registered in the store&#39;s Catalog by page number.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;items\&quot;: [      {        \&quot;id\&quot;: 2000000,        \&quot;name\&quot;: \&quot;Farm\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Farm\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Farm\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000001,        \&quot;name\&quot;: \&quot;Adidas\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000002,        \&quot;name\&quot;: \&quot;Brastemp\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Brastemp\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Brastemp\&quot;,        \&quot;imageUrl\&quot;: null      }    ],      \&quot;paging\&quot;: {        \&quot;page\&quot;: 1,          \&quot;perPage\&quot;: 3,            \&quot;total\&quot;: 6,              \&quot;pages\&quot;: 2      }  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void brandListPerPageTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer pageSize = null;
        Integer page = null;
        BrandListPerPage200Response response = api.brandListPerPage(contentType, accept, pageSize, page);
        // TODO: test validations
    }

}
