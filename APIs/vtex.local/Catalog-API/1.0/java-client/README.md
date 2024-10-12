# openapi-java-client

Catalog API
- API version: 1.0
  - Build date: 2024-10-12T11:55:15.452014-04:00[America/New_York]
  - Generator version: 7.9.0


> Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.

Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.


## Index

- [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).
- [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).
- [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).
- [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.
- [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).
- [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).
- [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.
- [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).
- [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).
- [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).
- [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.
- [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.
- [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.
- [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).
- [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).
- [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).
- [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).
- [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).
- [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).
- [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).
- [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).
- [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).
- [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).
- [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items. 
- [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value. 
- [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.
- [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.
- [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.
- [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.
- [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).
- [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.
- [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).
- [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.
- [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.


## Common parameters

| Parameter name              | Description                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------|
| `{{accountName}}`         | Store account name                                                                      |
| `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |
| `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |
| `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AttachmentApi apiInstance = new AttachmentApi(defaultClient);
    String attachmentid = "vtexcommercestable"; // String | Attachment ID.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.apiCatalogPvtAttachmentAttachmentidDelete(attachmentid, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentApi#apiCatalogPvtAttachmentAttachmentidDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://vtex.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttachmentApi* | [**apiCatalogPvtAttachmentAttachmentidDelete**](docs/AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidDelete) | **DELETE** /api/catalog/pvt/attachment/{attachmentid} | Delete attachment
*AttachmentApi* | [**apiCatalogPvtAttachmentAttachmentidGet**](docs/AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidGet) | **GET** /api/catalog/pvt/attachment/{attachmentid} | Get attachment
*AttachmentApi* | [**apiCatalogPvtAttachmentAttachmentidPut**](docs/AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidPut) | **PUT** /api/catalog/pvt/attachment/{attachmentid} | Update attachment
*AttachmentApi* | [**apiCatalogPvtAttachmentPost**](docs/AttachmentApi.md#apiCatalogPvtAttachmentPost) | **POST** /api/catalog/pvt/attachment | Create attachment
*AttachmentApi* | [**apiCatalogPvtAttachmentsGet**](docs/AttachmentApi.md#apiCatalogPvtAttachmentsGet) | **GET** /api/catalog/pvt/attachments | Get all attachments
*BrandApi* | [**apiCatalogPvtBrandBrandIdDelete**](docs/BrandApi.md#apiCatalogPvtBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/brand/{brandId} | Delete Brand
*BrandApi* | [**apiCatalogPvtBrandBrandIdGet**](docs/BrandApi.md#apiCatalogPvtBrandBrandIdGet) | **GET** /api/catalog/pvt/brand/{brandId} | Get Brand and context
*BrandApi* | [**apiCatalogPvtBrandBrandIdPut**](docs/BrandApi.md#apiCatalogPvtBrandBrandIdPut) | **PUT** /api/catalog/pvt/brand/{brandId} | Update Brand
*BrandApi* | [**apiCatalogPvtBrandPost**](docs/BrandApi.md#apiCatalogPvtBrandPost) | **POST** /api/catalog/pvt/brand | Create Brand
*BrandApi* | [**brand**](docs/BrandApi.md#brand) | **GET** /api/catalog_system/pvt/brand/{brandId} | Get Brand
*BrandApi* | [**brandList**](docs/BrandApi.md#brandList) | **GET** /api/catalog_system/pvt/brand/list | Get Brand List
*BrandApi* | [**brandListPerPage**](docs/BrandApi.md#brandListPerPage) | **GET** /api/catalog_system/pvt/brand/pagedlist | Get Brand List Per Page
*CategoryApi* | [**apiCatalogPvtCategoryCategoryIdGet**](docs/CategoryApi.md#apiCatalogPvtCategoryCategoryIdGet) | **GET** /api/catalog/pvt/category/{categoryId} | Get Category by ID
*CategoryApi* | [**apiCatalogPvtCategoryCategoryIdPut**](docs/CategoryApi.md#apiCatalogPvtCategoryCategoryIdPut) | **PUT** /api/catalog/pvt/category/{categoryId} | Update Category
*CategoryApi* | [**apiCatalogPvtCategoryPost**](docs/CategoryApi.md#apiCatalogPvtCategoryPost) | **POST** /api/catalog/pvt/category | Create Category
*CategoryApi* | [**categoryTree**](docs/CategoryApi.md#categoryTree) | **GET** /api/catalog_system/pub/category/tree/{categoryLevels} | Get Category Tree
*CategorySpecificationApi* | [**specificationsByCategoryId**](docs/CategorySpecificationApi.md#specificationsByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listByCategoryId/{categoryId} | Get Specifications By Category ID
*CategorySpecificationApi* | [**specificationsTreeByCategoryId**](docs/CategorySpecificationApi.md#specificationsTreeByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listTreeByCategoryId/{categoryId} | Get Specifications Tree By Category ID
*CollectionBetaApi* | [**gETAllCollections**](docs/CollectionBetaApi.md#gETAllCollections) | **GET** /api/catalog_system/pvt/collection/search | Get All Collections
*CollectionBetaApi* | [**gETAllInactiveCollections**](docs/CollectionBetaApi.md#gETAllInactiveCollections) | **GET** /api/catalog/pvt/collection/inactive | Get All Inactive Collections
*CollectionBetaApi* | [**gETCollectionsbyseachterms**](docs/CollectionBetaApi.md#gETCollectionsbyseachterms) | **GET** /api/catalog_system/pvt/collection/search/{searchTerms} | Get Collections by search terms
*CollectionBetaApi* | [**gETImportfileexample**](docs/CollectionBetaApi.md#gETImportfileexample) | **GET** /api/catalog/pvt/collection/stockkeepingunit/importfileexample | Import Collection file example
*CollectionBetaApi* | [**gETProductsfromacollection**](docs/CollectionBetaApi.md#gETProductsfromacollection) | **GET** /api/catalog/pvt/collection/{collectionId}/products | Get products from a collection
*CollectionBetaApi* | [**pOSTAddproductsbyimportfile**](docs/CollectionBetaApi.md#pOSTAddproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importinsert | Add products to Collection by imported file
*CollectionBetaApi* | [**pOSTCreateCollection**](docs/CollectionBetaApi.md#pOSTCreateCollection) | **POST** /api/catalog/pvt/collection/ | Create Collection
*CollectionBetaApi* | [**pOSTRemoveproductsbyimportfile**](docs/CollectionBetaApi.md#pOSTRemoveproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importexclude | Remove products from Collection by imported file
*CommercialConditionsApi* | [**getAllCommercialConditions**](docs/CommercialConditionsApi.md#getAllCommercialConditions) | **GET** /api/catalog_system/pvt/commercialcondition/list | Get all commercial conditions
*CommercialConditionsApi* | [**getCommercialConditions**](docs/CommercialConditionsApi.md#getCommercialConditions) | **GET** /api/catalog_system/pvt/commercialcondition/{commercialConditionId} | Get commercial condition
*GiftListApi* | [**getGiftList**](docs/GiftListApi.md#getGiftList) | **GET** /api/addon/pvt/giftlist/get/{listId} | Get Gift List
*LegacyCollectionApi* | [**apiCatalogPvtCollectionCollectionIdDelete**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdDelete) | **DELETE** /api/catalog/pvt/collection/{collectionId} | Delete Collection
*LegacyCollectionApi* | [**apiCatalogPvtCollectionCollectionIdGet**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdGet) | **GET** /api/catalog/pvt/collection/{collectionId} | Get Collection
*LegacyCollectionApi* | [**apiCatalogPvtCollectionCollectionIdPut**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdPut) | **PUT** /api/catalog/pvt/collection/{collectionId} | Update Collection
*LegacyCollectionApi* | [**apiCatalogPvtCollectionPost**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionPost) | **POST** /api/catalog/pvt/collection | Create Collection
*LegacySubcollectionApi* | [**apiCatalogPvtCollectionCollectionIdPositionPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdPositionPost) | **POST** /api/catalog/pvt/collection/{collectionId}/position | Reposition SKU on the Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtCollectionCollectionIdSubcollectionGet**](docs/LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdSubcollectionGet) | **GET** /api/catalog/pvt/collection/{collectionId}/subcollection | Get Subcollection by Collection ID
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionPost) | **POST** /api/catalog/pvt/subcollection | Create Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{brandId} | Delete Brand from Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{categoryId} | Delete Category from Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdBrandPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/brand | Associate Brand to Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdCategoryPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdCategoryPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/category | Associate Category to Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId} | Delete Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdGet**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdGet) | **GET** /api/catalog/pvt/subcollection/{subCollectionId} | Get Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdPut**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdPut) | **PUT** /api/catalog/pvt/subcollection/{subCollectionId} | Update Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit | Add SKU to Subcollection
*LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit/{skuId} | Delete SKU from Subcollection
*NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredDelete**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured | Delete Non Structured Specification by SKU ID
*NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredGet**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredGet) | **GET** /api/catalog/pvt/specification/nonstructured | Get Non Structured Specification by SKU ID
*NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredIdDelete**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured/{Id} | Delete Non Structured Specification
*NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredIdGet**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdGet) | **GET** /api/catalog/pvt/specification/nonstructured/{Id} | Get Non Structured Specification by ID
*ProductApi* | [**apiCatalogPvtProductPost**](docs/ProductApi.md#apiCatalogPvtProductPost) | **POST** /api/catalog/pvt/product | Create Product with Category and Brand
*ProductApi* | [**apiCatalogPvtProductProductIdPut**](docs/ProductApi.md#apiCatalogPvtProductProductIdPut) | **PUT** /api/catalog/pvt/product/{productId} | Update Product
*ProductApi* | [**getProductbyid**](docs/ProductApi.md#getProductbyid) | **GET** /api/catalog/pvt/product/{productId} | Get Product by ID
*ProductApi* | [**productAndSkuIds**](docs/ProductApi.md#productAndSkuIds) | **GET** /api/catalog_system/pvt/products/GetProductAndSkuIds | Get Product and SKU IDs
*ProductApi* | [**productVariations**](docs/ProductApi.md#productVariations) | **GET** /api/catalog_system/pub/products/variations/{productId} | Get Product&#39;s SKUs by Product ID
*ProductApi* | [**productandTradePolicy**](docs/ProductApi.md#productandTradePolicy) | **GET** /api/catalog_system/pvt/products/productget/{productId} | Get Product and its general context
*ProductApi* | [**productbyRefId**](docs/ProductApi.md#productbyRefId) | **GET** /api/catalog_system/pvt/products/productgetbyrefid/{refId} | Get Product by RefId
*ProductApi* | [**reviewRateProduct**](docs/ProductApi.md#reviewRateProduct) | **GET** /api/addon/pvt/review/GetProductRate/{productId} | Get Product Review Rate by Product ID
*ProductIndexingApi* | [**indexedInfo**](docs/ProductIndexingApi.md#indexedInfo) | **GET** /api/catalog_system/pvt/products/GetIndexedInfo/{productId} | Get Product Indexed Information
*ProductSpecificationApi* | [**apiCatalogPvtProductProductIdSpecificationPost**](docs/ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationPost) | **POST** /api/catalog/pvt/product/{productId}/specification | Associate Product Specification
*ProductSpecificationApi* | [**apiCatalogPvtProductProductIdSpecificationvaluePut**](docs/ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/product/{productId}/specificationvalue | Associate product specification using specification name and group name
*ProductSpecificationApi* | [**deleteAllProductSpecifications**](docs/ProductSpecificationApi.md#deleteAllProductSpecifications) | **DELETE** /api/catalog/pvt/product/{productId}/specification | Delete all Product Specifications by Product ID
*ProductSpecificationApi* | [**deleteaProductSpecification**](docs/ProductSpecificationApi.md#deleteaProductSpecification) | **DELETE** /api/catalog/pvt/product/{productId}/specification/{specificationId} | Delete a specific Product Specification
*ProductSpecificationApi* | [**getProductSpecification**](docs/ProductSpecificationApi.md#getProductSpecification) | **GET** /api/catalog_system/pvt/products/{productId}/specification | Get Product Specification by Product ID
*ProductSpecificationApi* | [**getProductSpecificationbyProductID**](docs/ProductSpecificationApi.md#getProductSpecificationbyProductID) | **GET** /api/catalog/pvt/product/{productId}/specification | Get Product Specification and its information by Product ID
*ProductSpecificationApi* | [**updateProductSpecification**](docs/ProductSpecificationApi.md#updateProductSpecification) | **POST** /api/catalog_system/pvt/products/{productId}/specification | Update Product Specification by Product ID
*SalesChannelApi* | [**salesChannelList**](docs/SalesChannelApi.md#salesChannelList) | **GET** /api/catalog_system/pvt/saleschannel/list | Get Sales Channel List
*SalesChannelApi* | [**salesChannelbyId**](docs/SalesChannelApi.md#salesChannelbyId) | **GET** /api/catalog_system/pub/saleschannel/{salesChannelId} | Get Sales Channel by ID
*SellerApi* | [**createSeller**](docs/SellerApi.md#createSeller) | **POST** /api/catalog_system/pvt/seller | Create Seller
*SellerApi* | [**getSellerbyId**](docs/SellerApi.md#getSellerbyId) | **GET** /api/catalog_system/pvt/seller/{sellerId} | Get Seller by ID
*SellerApi* | [**getSellersbyId**](docs/SellerApi.md#getSellersbyId) | **GET** /api/catalog_system/pvt/sellers/{sellerId} | Get Seller by ID
*SellerApi* | [**sellerList**](docs/SellerApi.md#sellerList) | **GET** /api/catalog_system/pvt/seller/list | Get Seller List
*SellerApi* | [**updateSeller**](docs/SellerApi.md#updateSeller) | **PUT** /api/catalog_system/pvt/seller | Update Seller
*SimilarCategoryApi* | [**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete**](docs/SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Delete Similar Category
*SimilarCategoryApi* | [**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost**](docs/SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost) | **POST** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Add Similar Category
*SimilarCategoryApi* | [**apiCatalogPvtProductProductIdSimilarcategoryGet**](docs/SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryGet) | **GET** /api/catalog/pvt/product/{productId}/similarcategory/ | Get Similar Categories
*SkuApi* | [**apiCatalogPvtStockkeepingunitGet**](docs/SkuApi.md#apiCatalogPvtStockkeepingunitGet) | **GET** /api/catalog/pvt/stockkeepingunit | Get SKU by RefId
*SkuApi* | [**apiCatalogPvtStockkeepingunitPost**](docs/SkuApi.md#apiCatalogPvtStockkeepingunitPost) | **POST** /api/catalog/pvt/stockkeepingunit | Create SKU
*SkuApi* | [**apiCatalogPvtStockkeepingunitSkuIdPut**](docs/SkuApi.md#apiCatalogPvtStockkeepingunitSkuIdPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId} | Update SKU
*SkuApi* | [**listallSKUIDs**](docs/SkuApi.md#listallSKUIDs) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitids | List all SKU IDs
*SkuApi* | [**sku**](docs/SkuApi.md#sku) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId} | Get SKU
*SkuApi* | [**skuContext**](docs/SkuApi.md#skuContext) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyid/{skuId} | Get SKU and context
*SkuApi* | [**skuIdbyRefId**](docs/SkuApi.md#skuIdbyRefId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/{refId} | Get SKU ID by Reference ID
*SkuApi* | [**skuIdlistbyRefIdlist**](docs/SkuApi.md#skuIdlistbyRefIdlist) | **POST** /api/catalog_system/pub/sku/stockkeepingunitidsbyrefids | Retrieve SKU ID list by Reference ID list
*SkuApi* | [**skubyAlternateId**](docs/SkuApi.md#skubyAlternateId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyalternateId/{alternateId} | Get SKU by Alternate ID
*SkuApi* | [**skulistbyProductId**](docs/SkuApi.md#skulistbyProductId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitByProductId/{productId} | Get SKU list by Product ID
*SkuAttachmentApi* | [**apiCatalogPvtSkuattachmentDelete**](docs/SkuAttachmentApi.md#apiCatalogPvtSkuattachmentDelete) | **DELETE** /api/catalog/pvt/skuattachment | Dissociate attachments and SKUs
*SkuAttachmentApi* | [**apiCatalogPvtSkuattachmentPost**](docs/SkuAttachmentApi.md#apiCatalogPvtSkuattachmentPost) | **POST** /api/catalog/pvt/skuattachment | Associate SKU Attachment
*SkuAttachmentApi* | [**apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete**](docs/SkuAttachmentApi.md#apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete) | **DELETE** /api/catalog/pvt/skuattachment/{skuAttachmentAssociationId} | Delete SKU Attachment by Attachment Association ID
*SkuAttachmentApi* | [**apiCatalogPvtStockkeepingunitSkuIdAttachmentGet**](docs/SkuAttachmentApi.md#apiCatalogPvtStockkeepingunitSkuIdAttachmentGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/attachment | Get SKU Attachments by SKU ID
*SkuAttachmentApi* | [**associateattachmentstoSKU**](docs/SkuAttachmentApi.md#associateattachmentstoSKU) | **POST** /api/catalog_system/pvt/sku/associateattachments | Associate attachments to an SKU
*SkuComplementApi* | [**createSKUComplement**](docs/SkuComplementApi.md#createSKUComplement) | **POST** /api/catalog/pvt/skucomplement | Create SKU Complement
*SkuComplementApi* | [**deleteSKUComplementbySKUComplementID**](docs/SkuComplementApi.md#deleteSKUComplementbySKUComplementID) | **DELETE** /api/catalog/pvt/skucomplement/{skuComplementId} | Delete SKU Complement by SKU Complement ID
*SkuComplementApi* | [**getSKUComplementbySKUComplementID**](docs/SkuComplementApi.md#getSKUComplementbySKUComplementID) | **GET** /api/catalog/pvt/skucomplement/{skuComplementId} | Get SKU Complement by SKU Complement ID
*SkuComplementApi* | [**getSKUComplementbySKUID**](docs/SkuComplementApi.md#getSKUComplementbySKUID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement | Get SKU Complement by SKU ID
*SkuComplementApi* | [**getSKUComplementsbyComplementTypeID**](docs/SkuComplementApi.md#getSKUComplementsbyComplementTypeID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement/{complementTypeId} | Get SKU Complements by Complement Type ID
*SkuComplementApi* | [**getSKUcomplementsbytype**](docs/SkuComplementApi.md#getSKUcomplementsbytype) | **GET** /api/catalog_system/pvt/sku/complements/{parentSkuId}/{type} | Get SKU complements by type
*SkuEanApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanDelete**](docs/SkuEanApi.md#apiCatalogPvtStockkeepingunitSkuIdEanDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/ean | Delete all SKU EAN values
*SkuEanApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanEanDelete**](docs/SkuEanApi.md#apiCatalogPvtStockkeepingunitSkuIdEanEanDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean} | Delete SKU EAN
*SkuEanApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanEanPost**](docs/SkuEanApi.md#apiCatalogPvtStockkeepingunitSkuIdEanEanPost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean} | Create SKU EAN
*SkuEanApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanGet**](docs/SkuEanApi.md#apiCatalogPvtStockkeepingunitSkuIdEanGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/ean | Get EAN by SKU ID
*SkuEanApi* | [**skubyEAN**](docs/SkuEanApi.md#skubyEAN) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyean/{ean} | Get SKU by EAN
*SkuFileApi* | [**apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut**](docs/SkuFileApi.md#apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut) | **PUT** /api/catalog/pvt/stockkeepingunit/copy/{skuIdfrom}/{skuIdto}/file/ | Copy Files from an SKU to another SKU
*SkuFileApi* | [**apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete**](docs/SkuFileApi.md#apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/disassociate/{skuId}/file/{skuFileId} | Disassociate SKU File
*SkuFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileDelete**](docs/SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Delete All SKU Files
*SkuFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileGet**](docs/SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Get SKU Files
*SkuFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFilePost**](docs/SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFilePost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Create SKU File
*SkuFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete**](docs/SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Delete SKU Image File
*SkuFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut**](docs/SkuFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Update SKU File
*SkuKitApi* | [**apiCatalogPvtStockkeepingunitkitDelete**](docs/SkuKitApi.md#apiCatalogPvtStockkeepingunitkitDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit | Delete SKU Kit by SKU ID or Parent SKU ID
*SkuKitApi* | [**apiCatalogPvtStockkeepingunitkitGet**](docs/SkuKitApi.md#apiCatalogPvtStockkeepingunitkitGet) | **GET** /api/catalog/pvt/stockkeepingunitkit | Get SKU Kit by SKU ID or Parent SKU ID
*SkuKitApi* | [**apiCatalogPvtStockkeepingunitkitKitIdDelete**](docs/SkuKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Delete SKU Kit by KitId
*SkuKitApi* | [**apiCatalogPvtStockkeepingunitkitKitIdGet**](docs/SkuKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdGet) | **GET** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Get SKU Kit
*SkuKitApi* | [**apiCatalogPvtStockkeepingunitkitPost**](docs/SkuKitApi.md#apiCatalogPvtStockkeepingunitkitPost) | **POST** /api/catalog/pvt/stockkeepingunitkit | Create SKU Kit
*SkuSellerApi* | [**apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost**](docs/SkuSellerApi.md#apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost) | **POST** /api/catalog_system/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId} | Change Notification with Seller ID and Seller SKU ID
*SkuSellerApi* | [**changeNotification**](docs/SkuSellerApi.md#changeNotification) | **POST** /api/catalog_system/pvt/skuseller/changenotification/{skuId} | Change Notification with SKU ID
*SkuSellerApi* | [**deleteSKUsellerassociation**](docs/SkuSellerApi.md#deleteSKUsellerassociation) | **POST** /api/catalog_system/pvt/skuseller/remove/{sellerId}/{sellerSkuId} | Remove a seller&#39;s SKU binding
*SkuSellerApi* | [**getSKUseller**](docs/SkuSellerApi.md#getSKUseller) | **GET** /api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId} | Get details of a seller&#39;s SKU
*SkuServiceApi* | [**apiCatalogPvtSkuservicePost**](docs/SkuServiceApi.md#apiCatalogPvtSkuservicePost) | **POST** /api/catalog/pvt/skuservice | Associate SKU Service
*SkuServiceApi* | [**apiCatalogPvtSkuserviceSkuServiceIdDelete**](docs/SkuServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdDelete) | **DELETE** /api/catalog/pvt/skuservice/{skuServiceId} | Dissociate SKU Service
*SkuServiceApi* | [**apiCatalogPvtSkuserviceSkuServiceIdGet**](docs/SkuServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdGet) | **GET** /api/catalog/pvt/skuservice/{skuServiceId} | Get SKU Service
*SkuServiceApi* | [**apiCatalogPvtSkuserviceSkuServiceIdPut**](docs/SkuServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdPut) | **PUT** /api/catalog/pvt/skuservice/{skuServiceId} | Update SKU Service
*SkuServiceAttachmentApi* | [**apiCatalogPvtSkuservicetypeattachmentDelete**](docs/SkuServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment | Dissociate Attachment by Attachment ID or SKU Service Type ID
*SkuServiceAttachmentApi* | [**apiCatalogPvtSkuservicetypeattachmentPost**](docs/SkuServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentPost) | **POST** /api/catalog/pvt/skuservicetypeattachment | Associate SKU Service Attachment
*SkuServiceAttachmentApi* | [**apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete**](docs/SkuServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment/{skuServiceTypeAttachmentId} | Dissociate Attachment from SKU Service Type
*SkuServiceTypeApi* | [**apiCatalogPvtSkuservicetypePost**](docs/SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypePost) | **POST** /api/catalog/pvt/skuservicetype | Create SKU Service Type
*SkuServiceTypeApi* | [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete**](docs/SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete) | **DELETE** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Delete SKU Service Type
*SkuServiceTypeApi* | [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet**](docs/SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet) | **GET** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Get SKU Service Type
*SkuServiceTypeApi* | [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut**](docs/SkuServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut) | **PUT** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Update SKU Service Type
*SkuServiceValueApi* | [**apiCatalogPvtSkuservicevaluePost**](docs/SkuServiceValueApi.md#apiCatalogPvtSkuservicevaluePost) | **POST** /api/catalog/pvt/skuservicevalue | Create SKU Service Value
*SkuServiceValueApi* | [**apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete**](docs/SkuServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete) | **DELETE** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Delete SKU Service Value
*SkuServiceValueApi* | [**apiCatalogPvtSkuservicevalueSkuServiceValueIdGet**](docs/SkuServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdGet) | **GET** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Get SKU Service Value
*SkuServiceValueApi* | [**apiCatalogPvtSkuservicevalueSkuServiceValueIdPut**](docs/SkuServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdPut) | **PUT** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Update SKU Service Value
*SkuSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete**](docs/SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Delete all SKU Specifications
*SkuSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationGet**](docs/SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Get SKU Specifications
*SkuSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationPost**](docs/SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Associate SKU Specification
*SkuSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationPut**](docs/SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Update SKU Specification
*SkuSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete**](docs/SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification/{specificationId} | Delete SKU Specification
*SkuSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut**](docs/SkuSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specificationvalue | Associate SKU specification using specification name and group name
*SpecificationApi* | [**apiCatalogPvtSpecificationPost**](docs/SpecificationApi.md#apiCatalogPvtSpecificationPost) | **POST** /api/catalog/pvt/specification | Create Specification
*SpecificationApi* | [**apiCatalogPvtSpecificationSpecificationIdGet**](docs/SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdGet) | **GET** /api/catalog/pvt/specification/{specificationId} | Get Specification
*SpecificationApi* | [**apiCatalogPvtSpecificationSpecificationIdPut**](docs/SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdPut) | **PUT** /api/catalog/pvt/specification/{specificationId} | Update Specification
*SpecificationFieldApi* | [**specificationsField**](docs/SpecificationFieldApi.md#specificationsField) | **GET** /api/catalog_system/pub/specification/fieldGet/{fieldId} | Get Specification Field
*SpecificationFieldApi* | [**specificationsInsertField**](docs/SpecificationFieldApi.md#specificationsInsertField) | **POST** /api/catalog_system/pvt/specification/field | Create Specification Field
*SpecificationFieldApi* | [**specificationsInsertFieldUpdate**](docs/SpecificationFieldApi.md#specificationsInsertFieldUpdate) | **PUT** /api/catalog_system/pvt/specification/field | Update Specification Field
*SpecificationFieldValueApi* | [**specificationsGetFieldValue**](docs/SpecificationFieldValueApi.md#specificationsGetFieldValue) | **GET** /api/catalog_system/pvt/specification/fieldValue/{fieldValueId} | Get Specification Field Value
*SpecificationFieldValueApi* | [**specificationsInsertFieldValue**](docs/SpecificationFieldValueApi.md#specificationsInsertFieldValue) | **POST** /api/catalog_system/pvt/specification/fieldValue | Create Specification Field Value
*SpecificationFieldValueApi* | [**specificationsUpdateFieldValue**](docs/SpecificationFieldValueApi.md#specificationsUpdateFieldValue) | **PUT** /api/catalog_system/pvt/specification/fieldValue | Update Specification Field Value
*SpecificationFieldValueApi* | [**specificationsValuesByFieldId**](docs/SpecificationFieldValueApi.md#specificationsValuesByFieldId) | **GET** /api/catalog_system/pub/specification/fieldvalue/{fieldId} | Get Specification Values By Field ID
*SpecificationGroupApi* | [**apiCatalogPvtSpecificationgroupGroupIdPut**](docs/SpecificationGroupApi.md#apiCatalogPvtSpecificationgroupGroupIdPut) | **PUT** /api/catalog/pvt/specificationgroup/{groupId} | Update Specification Group
*SpecificationGroupApi* | [**specificationGroupInsert2**](docs/SpecificationGroupApi.md#specificationGroupInsert2) | **POST** /api/catalog/pvt/specificationgroup | Create Specification Group
*SpecificationGroupApi* | [**specificationsGroupGet**](docs/SpecificationGroupApi.md#specificationsGroupGet) | **GET** /api/catalog_system/pub/specification/groupGet/{groupId} | Get Specification Group
*SpecificationGroupApi* | [**specificationsGroupListbyCategory**](docs/SpecificationGroupApi.md#specificationsGroupListbyCategory) | **GET** /api/catalog_system/pvt/specification/groupbycategory/{categoryId} | List Specification Group by Category
*SpecificationValueApi* | [**apiCatalogPvtSpecificationvaluePost**](docs/SpecificationValueApi.md#apiCatalogPvtSpecificationvaluePost) | **POST** /api/catalog/pvt/specificationvalue | Create Specification Value
*SpecificationValueApi* | [**apiCatalogPvtSpecificationvalueSpecificationValueIdGet**](docs/SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdGet) | **GET** /api/catalog/pvt/specificationvalue/{specificationValueId} | Get Specification Value
*SpecificationValueApi* | [**apiCatalogPvtSpecificationvalueSpecificationValueIdPut**](docs/SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdPut) | **PUT** /api/catalog/pvt/specificationvalue/{specificationValueId} | Update Specification Value
*SupplierApi* | [**apiCatalogPvtSupplierPost**](docs/SupplierApi.md#apiCatalogPvtSupplierPost) | **POST** /api/catalog/pvt/supplier | Create Supplier
*SupplierApi* | [**apiCatalogPvtSupplierSupplierIdDelete**](docs/SupplierApi.md#apiCatalogPvtSupplierSupplierIdDelete) | **DELETE** /api/catalog/pvt/supplier/{supplierId} | Delete Supplier
*SupplierApi* | [**apiCatalogPvtSupplierSupplierIdPut**](docs/SupplierApi.md#apiCatalogPvtSupplierSupplierIdPut) | **PUT** /api/catalog/pvt/supplier/{supplierId} | Update Supplier
*TradePolicyApi* | [**apiCatalogPvtProductProductIdSalespolicyGet**](docs/TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyGet) | **GET** /api/catalog/pvt/product/{productId}/salespolicy | Get Trade Policies by Product ID
*TradePolicyApi* | [**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete**](docs/TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Remove Product from Trade Policy
*TradePolicyApi* | [**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost**](docs/TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost) | **POST** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Associate Product with Trade Policy
*TradePolicyApi* | [**apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet**](docs/TradePolicyApi.md#apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel | List all SKUs of a Trade Policy


## Documentation for Models

 - [AlternateIds](docs/AlternateIds.md)
 - [ApiCatalogPvtAttachmentsGet200Response](docs/ApiCatalogPvtAttachmentsGet200Response.md)
 - [ApiCatalogPvtCategoryCategoryIdPutRequest](docs/ApiCatalogPvtCategoryCategoryIdPutRequest.md)
 - [ApiCatalogPvtCollectionCollectionIdPositionPostRequest](docs/ApiCatalogPvtCollectionCollectionIdPositionPostRequest.md)
 - [ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner](docs/ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner.md)
 - [ApiCatalogPvtCollectionPost200Response](docs/ApiCatalogPvtCollectionPost200Response.md)
 - [ApiCatalogPvtProductPost200Response](docs/ApiCatalogPvtProductPost200Response.md)
 - [ApiCatalogPvtProductPostRequest](docs/ApiCatalogPvtProductPostRequest.md)
 - [ApiCatalogPvtProductProductIdPutRequest](docs/ApiCatalogPvtProductProductIdPutRequest.md)
 - [ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner](docs/ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner.md)
 - [ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response](docs/ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response.md)
 - [ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner](docs/ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner.md)
 - [ApiCatalogPvtProductProductIdSpecificationPost200Response](docs/ApiCatalogPvtProductProductIdSpecificationPost200Response.md)
 - [ApiCatalogPvtProductProductIdSpecificationPostRequest](docs/ApiCatalogPvtProductProductIdSpecificationPostRequest.md)
 - [ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner](docs/ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner.md)
 - [ApiCatalogPvtProductProductIdSpecificationvaluePutRequest](docs/ApiCatalogPvtProductProductIdSpecificationvaluePutRequest.md)
 - [ApiCatalogPvtSkuattachmentPost200Response](docs/ApiCatalogPvtSkuattachmentPost200Response.md)
 - [ApiCatalogPvtSkuservicetypeattachmentPost200Response](docs/ApiCatalogPvtSkuservicetypeattachmentPost200Response.md)
 - [ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner](docs/ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner.md)
 - [ApiCatalogPvtSpecificationPost200Response](docs/ApiCatalogPvtSpecificationPost200Response.md)
 - [ApiCatalogPvtSpecificationPostRequest](docs/ApiCatalogPvtSpecificationPostRequest.md)
 - [ApiCatalogPvtSpecificationgroupGroupIdPut200Response](docs/ApiCatalogPvtSpecificationgroupGroupIdPut200Response.md)
 - [ApiCatalogPvtSpecificationvaluePost200Response](docs/ApiCatalogPvtSpecificationvaluePost200Response.md)
 - [ApiCatalogPvtSpecificationvaluePostRequest](docs/ApiCatalogPvtSpecificationvaluePostRequest.md)
 - [ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response](docs/ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response.md)
 - [ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner](docs/ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner.md)
 - [ApiCatalogPvtStockkeepingunitGet200Response](docs/ApiCatalogPvtStockkeepingunitGet200Response.md)
 - [ApiCatalogPvtStockkeepingunitPost200Response](docs/ApiCatalogPvtStockkeepingunitPost200Response.md)
 - [ApiCatalogPvtStockkeepingunitPostRequest](docs/ApiCatalogPvtStockkeepingunitPostRequest.md)
 - [ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner](docs/ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner.md)
 - [ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response](docs/ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response.md)
 - [ApiCatalogPvtStockkeepingunitSkuIdPut200Response](docs/ApiCatalogPvtStockkeepingunitSkuIdPut200Response.md)
 - [ApiCatalogPvtStockkeepingunitSkuIdPutRequest](docs/ApiCatalogPvtStockkeepingunitSkuIdPutRequest.md)
 - [ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest](docs/ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest.md)
 - [ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner](docs/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner.md)
 - [ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest](docs/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest.md)
 - [ApiCatalogPvtSubcollectionPost200Response](docs/ApiCatalogPvtSubcollectionPost200Response.md)
 - [ApiCatalogPvtSubcollectionPostRequest](docs/ApiCatalogPvtSubcollectionPostRequest.md)
 - [ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response](docs/ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response.md)
 - [ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response](docs/ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response.md)
 - [ApiCatalogPvtSubcollectionSubCollectionIdPutRequest](docs/ApiCatalogPvtSubcollectionSubCollectionIdPutRequest.md)
 - [ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response](docs/ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response.md)
 - [ArrayWithInformationOfAllTheCommercialConditionsInner](docs/ArrayWithInformationOfAllTheCommercialConditionsInner.md)
 - [AssociateattachmentstoSKURequest](docs/AssociateattachmentstoSKURequest.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentRequest](docs/AttachmentRequest.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [BrandCreateUpdate](docs/BrandCreateUpdate.md)
 - [BrandGet](docs/BrandGet.md)
 - [BrandListPerPage200Response](docs/BrandListPerPage200Response.md)
 - [Category](docs/Category.md)
 - [CategorySpecificationInner](docs/CategorySpecificationInner.md)
 - [CreateCategoryRequest](docs/CreateCategoryRequest.md)
 - [CreateSeller200Response](docs/CreateSeller200Response.md)
 - [CreateSellerRequest](docs/CreateSellerRequest.md)
 - [CurrencyFormatInfo](docs/CurrencyFormatInfo.md)
 - [Dimension](docs/Dimension.md)
 - [DomainsInner](docs/DomainsInner.md)
 - [Field](docs/Field.md)
 - [GetCategoryTree](docs/GetCategoryTree.md)
 - [GetCategoryTreeChild](docs/GetCategoryTreeChild.md)
 - [GetCommercialConditions200Response](docs/GetCommercialConditions200Response.md)
 - [GetGiftList200Response](docs/GetGiftList200Response.md)
 - [GetProductSpecificationbyProductID200ResponseInner](docs/GetProductSpecificationbyProductID200ResponseInner.md)
 - [GetProductbyid200Response](docs/GetProductbyid200Response.md)
 - [GetSKUAltID](docs/GetSKUAltID.md)
 - [GetSKUandContext](docs/GetSKUandContext.md)
 - [GetSKUcomplementsbytype200Response](docs/GetSKUcomplementsbytype200Response.md)
 - [GetSKUseller200Response](docs/GetSKUseller200Response.md)
 - [GetSellerbyId200Response](docs/GetSellerbyId200Response.md)
 - [GetSellersbyId200Response](docs/GetSellersbyId200Response.md)
 - [GetSpecFieldValue](docs/GetSpecFieldValue.md)
 - [GetorUpdateProductSpecification](docs/GetorUpdateProductSpecification.md)
 - [GiftListMembersInner](docs/GiftListMembersInner.md)
 - [Image](docs/Image.md)
 - [Paging](docs/Paging.md)
 - [ProductAndSkuIds200Response](docs/ProductAndSkuIds200Response.md)
 - [ProductAndSkuIds200ResponseData](docs/ProductAndSkuIds200ResponseData.md)
 - [ProductAndSkuIds200ResponseRange](docs/ProductAndSkuIds200ResponseRange.md)
 - [ProductSpecification](docs/ProductSpecification.md)
 - [ProductVariations200Response](docs/ProductVariations200Response.md)
 - [ProductVariations200ResponseSkusInner](docs/ProductVariations200ResponseSkusInner.md)
 - [ProductVariations200ResponseSkusInnerMeasures](docs/ProductVariations200ResponseSkusInnerMeasures.md)
 - [ProductandTradePolicy200Response](docs/ProductandTradePolicy200Response.md)
 - [ProductbyRefId200Response](docs/ProductbyRefId200Response.md)
 - [RealDimension](docs/RealDimension.md)
 - [RequestBody](docs/RequestBody.md)
 - [RequestBody1](docs/RequestBody1.md)
 - [RequestBody10](docs/RequestBody10.md)
 - [RequestBody11](docs/RequestBody11.md)
 - [RequestBody12](docs/RequestBody12.md)
 - [RequestBody2](docs/RequestBody2.md)
 - [RequestBody3](docs/RequestBody3.md)
 - [RequestBody4](docs/RequestBody4.md)
 - [RequestBody5](docs/RequestBody5.md)
 - [RequestBody6](docs/RequestBody6.md)
 - [RequestBody7](docs/RequestBody7.md)
 - [RequestBody8](docs/RequestBody8.md)
 - [RequestBody9](docs/RequestBody9.md)
 - [ResquestBody](docs/ResquestBody.md)
 - [ResquestBody1](docs/ResquestBody1.md)
 - [SKUFileURL](docs/SKUFileURL.md)
 - [SKUService](docs/SKUService.md)
 - [SKUServiceTypeRequest](docs/SKUServiceTypeRequest.md)
 - [SKUServiceTypeResponse](docs/SKUServiceTypeResponse.md)
 - [SKUServiceValueRequest](docs/SKUServiceValueRequest.md)
 - [SKUServiceValueResponse](docs/SKUServiceValueResponse.md)
 - [SKUSpecificationResponse](docs/SKUSpecificationResponse.md)
 - [SalesChannelbyId200Response](docs/SalesChannelbyId200Response.md)
 - [Sku200Response](docs/Sku200Response.md)
 - [SkuComplementInner](docs/SkuComplementInner.md)
 - [SkuKit](docs/SkuKit.md)
 - [SkuSeller](docs/SkuSeller.md)
 - [SkuSpecification](docs/SkuSpecification.md)
 - [SkulistbyProductId](docs/SkulistbyProductId.md)
 - [SpecificationGroupInsert2200Response](docs/SpecificationGroupInsert2200Response.md)
 - [SpecificationGroupInsertRequest](docs/SpecificationGroupInsertRequest.md)
 - [SpecificationsField200Response](docs/SpecificationsField200Response.md)
 - [SpecificationsGroup](docs/SpecificationsGroup.md)
 - [SpecificationsInsertFieldRequest](docs/SpecificationsInsertFieldRequest.md)
 - [SpecificationsInsertFieldUpdateRequest](docs/SpecificationsInsertFieldUpdateRequest.md)
 - [SpecificationsInsertFieldValueRequest](docs/SpecificationsInsertFieldValueRequest.md)
 - [SpecificationsUpdateFieldValueRequest](docs/SpecificationsUpdateFieldValueRequest.md)
 - [SupplierRequest](docs/SupplierRequest.md)
 - [SupplierResponse](docs/SupplierResponse.md)
 - [UpdateSeller200Response](docs/UpdateSeller200Response.md)
 - [UpdateSellerRequest](docs/UpdateSellerRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="appKey"></a>
### appKey

- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppKey
- **Location**: HTTP header

<a id="appToken"></a>
### appToken

- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppToken
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



