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
import org.openapitools.client.model.ApiCatalogPvtProductPost200Response;
import org.openapitools.client.model.ApiCatalogPvtProductPostRequest;
import org.openapitools.client.model.ApiCatalogPvtProductProductIdPutRequest;
import java.math.BigDecimal;
import org.openapitools.client.model.GetProductbyid200Response;
import org.openapitools.client.model.ProductAndSkuIds200Response;
import org.openapitools.client.model.ProductVariations200Response;
import org.openapitools.client.model.ProductandTradePolicy200Response;
import org.openapitools.client.model.ProductbyRefId200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProductApi
 */
@Disabled
public class ProductApiTest {

    private final ProductApi api = new ProductApi();

    /**
     * Create Product with Category and Brand
     *
     * This endpoint allows two types of request:    **Type 1:** Creating a new Product as well as a new Category path (including subcategories) and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60; parameters.    **Type 2:** Creating a new Product given an existing &#x60;BrandId&#x60; and an existing &#x60;CategoryId&#x60;.    When creating a product, regardless of the type of request, if there is a need to create a new product with a specific custom product ID, specify the &#x60;Id&#x60; (integer) in the request body. Otherwise, VTEX will generate the ID automatically.     ## Request body examples     ### Type 1     Request to create a product, associating it to a new Category and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60;:    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;CategoryPath\&quot;: \&quot;Mens/Clothing/T-Shirts\&quot;,      \&quot;BrandName\&quot;: \&quot;Nike\&quot;,      \&quot;RefId\&quot;: \&quot;31011706925\&quot;,      \&quot;Title\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;LinkId\&quot;: \&quot;tshirt-black\&quot;,      \&quot;Description\&quot;: \&quot;This is a cool Tshirt\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2022-01-01T00:00:00\&quot;,      \&quot;IsVisible\&quot;: true,      \&quot;IsActive\&quot;: true,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;MetaTagDescription\&quot;: \&quot;tshirt black\&quot;,      \&quot;ShowWithoutStock\&quot;: true,      \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ### Type 2    Request to create a product, associating it to an existing &#x60;CategoryId&#x60; and &#x60;BrandId&#x60;:    &#x60;&#x60;&#x60;json  {     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 52,     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;      &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtProductPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        ApiCatalogPvtProductPostRequest apiCatalogPvtProductPostRequest = null;
        ApiCatalogPvtProductPost200Response response = api.apiCatalogPvtProductPost(contentType, accept, apiCatalogPvtProductPostRequest);
        // TODO: test validations
    }

    /**
     * Update Product
     *
     * Updates an existing Product.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtProductProductIdPutTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer productId = null;
        ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest = null;
        ApiCatalogPvtProductPost200Response response = api.apiCatalogPvtProductProductIdPut(contentType, accept, productId, apiCatalogPvtProductProductIdPutRequest);
        // TODO: test validations
    }

    /**
     * Get Product by ID
     *
     * Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getProductbyidTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String productId = null;
        GetProductbyid200Response response = api.getProductbyid(contentType, accept, productId);
        // TODO: test validations
    }

    /**
     * Get Product and SKU IDs
     *
     * Retrieves the IDs of products and SKUs.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productAndSkuIdsTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer categoryId = null;
        Integer from = null;
        Integer to = null;
        ProductAndSkuIds200Response response = api.productAndSkuIds(contentType, accept, categoryId, from, to);
        // TODO: test validations
    }

    /**
     * Get Product&#39;s SKUs by Product ID
     *
     * Retrieves data about the product and all SKUs related to it by the product&#39;s ID.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: 9,      \&quot;name\&quot;: \&quot;Camisa Masculina\&quot;,      \&quot;salesChannel\&quot;: \&quot;2\&quot;,      \&quot;available\&quot;: true,      \&quot;displayMode\&quot;: \&quot;lista\&quot;,      \&quot;dimensions\&quot;: [          \&quot;Cores\&quot;,          \&quot;Tamanho\&quot;,          \&quot;País de origem\&quot;,          \&quot;Gênero\&quot;      ],      \&quot;dimensionsInputType\&quot;: {          \&quot;Cores\&quot;: \&quot;Combo\&quot;,          \&quot;Tamanho\&quot;: \&quot;Combo\&quot;,          \&quot;País de origem\&quot;: \&quot;Combo\&quot;,          \&quot;Gênero\&quot;: \&quot;Combo\&quot;      },      \&quot;dimensionsMap\&quot;: {          \&quot;Cores\&quot;: [              \&quot;Amarelo\&quot;,              \&quot;Azul\&quot;,              \&quot;Vermelho\&quot;          ],          \&quot;Tamanho\&quot;: [              \&quot;P\&quot;,              \&quot;M\&quot;,              \&quot;G\&quot;          ],          \&quot;País de origem\&quot;: [              \&quot;Brasil\&quot;          ],          \&quot;Gênero\&quot;: [              \&quot;Masculino\&quot;          ]      },      \&quot;skus\&quot;: [          {              \&quot;sku\&quot;: 310118454,              \&quot;skuname\&quot;: \&quot;Amarela - G\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Amarelo\&quot;,                  \&quot;Tamanho\&quot;: \&quot;G\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: false,              \&quot;availablequantity\&quot;: 0,              \&quot;cacheVersionUsedToCallCheckout\&quot;: null,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 9.999.876,00\&quot;,              \&quot;bestPrice\&quot;: 999987600,              \&quot;spotPrice\&quot;: 999987600,              \&quot;installments\&quot;: 0,              \&quot;installmentsValue\&quot;: 0,              \&quot;installmentsInsterestRate\&quot;: null,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155467-292-292/image-5d7ad76ad1954c53adecab4138319034.jpg?v&#x3D;637321899584500000\&quot;,              \&quot;sellerId\&quot;: \&quot;1\&quot;,              \&quot;seller\&quot;: \&quot;lojadobreno\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 1.0000,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          },          {              \&quot;sku\&quot;: 310118455,              \&quot;skuname\&quot;: \&quot;Vermelha - M\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Vermelho\&quot;,                  \&quot;Tamanho\&quot;: \&quot;M\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: true,              \&quot;availablequantity\&quot;: 99999,              \&quot;cacheVersionUsedToCallCheckout\&quot;: \&quot;38395F1AEF59DF5CEAEDE472328145CD_\&quot;,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 20,00\&quot;,              \&quot;bestPrice\&quot;: 2000,              \&quot;spotPrice\&quot;: 2000,              \&quot;installments\&quot;: 1,              \&quot;installmentsValue\&quot;: 2000,              \&quot;installmentsInsterestRate\&quot;: 0,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155468-292-292/image-601a6099aace48b89d26fc9f22e8e611.jpg?v&#x3D;637321906602470000\&quot;,              \&quot;sellerId\&quot;: \&quot;pedrostore\&quot;,              \&quot;seller\&quot;: \&quot;pedrostore\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 0.4167,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          }      ]  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productVariationsTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer productId = null;
        ProductVariations200Response response = api.productVariations(contentType, accept, productId);
        // TODO: test validations
    }

    /**
     * Get Product and its general context
     *
     * Retrieves a specific product&#39;s general information as name, description and the trade policies that it is included.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productandTradePolicyTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer productId = null;
        ProductandTradePolicy200Response response = api.productandTradePolicy(contentType, accept, productId);
        // TODO: test validations
    }

    /**
     * Get Product by RefId
     *
     * Retrieves a specific product by its Reference ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productbyRefIdTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String refId = null;
        ProductbyRefId200Response response = api.productbyRefId(contentType, accept, refId);
        // TODO: test validations
    }

    /**
     * Get Product Review Rate by Product ID
     *
     * Retrieves the review rate of a product by this product&#39;s ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reviewRateProductTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer productId = null;
        BigDecimal response = api.reviewRateProduct(contentType, accept, productId);
        // TODO: test validations
    }

}
