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
import org.openapitools.client.model.GetSKUAltID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SkuEanApi
 */
@Disabled
public class SkuEanApiTest {

    private final SkuEanApi api = new SkuEanApi();

    /**
     * Delete all SKU EAN values
     *
     * Deletes all EAN values of an SKU.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdEanDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        api.apiCatalogPvtStockkeepingunitSkuIdEanDelete(contentType, accept, skuId);
        // TODO: test validations
    }

    /**
     * Delete SKU EAN
     *
     * Deletes the EAN value of an SKU.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        String ean = null;
        api.apiCatalogPvtStockkeepingunitSkuIdEanEanDelete(contentType, accept, skuId, ean);
        // TODO: test validations
    }

    /**
     * Create SKU EAN
     *
     * Creates or updates the EAN value of an SKU.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdEanEanPostTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        String ean = null;
        api.apiCatalogPvtStockkeepingunitSkuIdEanEanPost(contentType, accept, skuId, ean);
        // TODO: test validations
    }

    /**
     * Get EAN by SKU ID
     *
     * Retrieves the EAN of the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      \&quot;1234567890123\&quot;  ]  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiCatalogPvtStockkeepingunitSkuIdEanGetTest() throws ApiException {
        String contentType = null;
        String accept = null;
        Integer skuId = null;
        List<String> response = api.apiCatalogPvtStockkeepingunitSkuIdEanGet(contentType, accept, skuId);
        // TODO: test validations
    }

    /**
     * Get SKU by EAN
     *
     * Retrieves an SKU by its EAN ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ]          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ]          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ]          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void skubyEANTest() throws ApiException {
        String contentType = null;
        String accept = null;
        String ean = null;
        GetSKUAltID response = api.skubyEAN(contentType, accept, ean);
        // TODO: test validations
    }

}
