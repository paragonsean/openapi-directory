# catalog_api

CatalogApi - JavaScript client for catalog_api

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
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install catalog_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your catalog_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var CatalogApi = require('catalog_api');

var defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
var appToken = defaultClient.authentications['appToken'];
appToken.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix['X-VTEX-API-AppToken'] = "Token"
// Configure API key authorization: appKey
var appKey = defaultClient.authentications['appKey'];
appKey.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix['X-VTEX-API-AppKey'] = "Token"

var api = new CatalogApi.AttachmentApi()
var attachmentid = "vtexcommercestable"; // {String} Attachment ID.
var contentType = "'application/json'"; // {String} Type of the content being sent.
var accept = "'application/json'"; // {String} HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.apiCatalogPvtAttachmentAttachmentidDelete(attachmentid, contentType, accept, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://vtex.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CatalogApi.AttachmentApi* | [**apiCatalogPvtAttachmentAttachmentidDelete**](docs/AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidDelete) | **DELETE** /api/catalog/pvt/attachment/{attachmentid} | Delete attachment
*CatalogApi.AttachmentApi* | [**apiCatalogPvtAttachmentAttachmentidGet**](docs/AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidGet) | **GET** /api/catalog/pvt/attachment/{attachmentid} | Get attachment
*CatalogApi.AttachmentApi* | [**apiCatalogPvtAttachmentAttachmentidPut**](docs/AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidPut) | **PUT** /api/catalog/pvt/attachment/{attachmentid} | Update attachment
*CatalogApi.AttachmentApi* | [**apiCatalogPvtAttachmentPost**](docs/AttachmentApi.md#apiCatalogPvtAttachmentPost) | **POST** /api/catalog/pvt/attachment | Create attachment
*CatalogApi.AttachmentApi* | [**apiCatalogPvtAttachmentsGet**](docs/AttachmentApi.md#apiCatalogPvtAttachmentsGet) | **GET** /api/catalog/pvt/attachments | Get all attachments
*CatalogApi.BrandApi* | [**apiCatalogPvtBrandBrandIdDelete**](docs/BrandApi.md#apiCatalogPvtBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/brand/{brandId} | Delete Brand
*CatalogApi.BrandApi* | [**apiCatalogPvtBrandBrandIdGet**](docs/BrandApi.md#apiCatalogPvtBrandBrandIdGet) | **GET** /api/catalog/pvt/brand/{brandId} | Get Brand and context
*CatalogApi.BrandApi* | [**apiCatalogPvtBrandBrandIdPut**](docs/BrandApi.md#apiCatalogPvtBrandBrandIdPut) | **PUT** /api/catalog/pvt/brand/{brandId} | Update Brand
*CatalogApi.BrandApi* | [**apiCatalogPvtBrandPost**](docs/BrandApi.md#apiCatalogPvtBrandPost) | **POST** /api/catalog/pvt/brand | Create Brand
*CatalogApi.BrandApi* | [**brand**](docs/BrandApi.md#brand) | **GET** /api/catalog_system/pvt/brand/{brandId} | Get Brand
*CatalogApi.BrandApi* | [**brandList**](docs/BrandApi.md#brandList) | **GET** /api/catalog_system/pvt/brand/list | Get Brand List
*CatalogApi.BrandApi* | [**brandListPerPage**](docs/BrandApi.md#brandListPerPage) | **GET** /api/catalog_system/pvt/brand/pagedlist | Get Brand List Per Page
*CatalogApi.CategoryApi* | [**apiCatalogPvtCategoryCategoryIdGet**](docs/CategoryApi.md#apiCatalogPvtCategoryCategoryIdGet) | **GET** /api/catalog/pvt/category/{categoryId} | Get Category by ID
*CatalogApi.CategoryApi* | [**apiCatalogPvtCategoryCategoryIdPut**](docs/CategoryApi.md#apiCatalogPvtCategoryCategoryIdPut) | **PUT** /api/catalog/pvt/category/{categoryId} | Update Category
*CatalogApi.CategoryApi* | [**apiCatalogPvtCategoryPost**](docs/CategoryApi.md#apiCatalogPvtCategoryPost) | **POST** /api/catalog/pvt/category | Create Category
*CatalogApi.CategoryApi* | [**categoryTree**](docs/CategoryApi.md#categoryTree) | **GET** /api/catalog_system/pub/category/tree/{categoryLevels} | Get Category Tree
*CatalogApi.CategorySpecificationApi* | [**specificationsByCategoryId**](docs/CategorySpecificationApi.md#specificationsByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listByCategoryId/{categoryId} | Get Specifications By Category ID
*CatalogApi.CategorySpecificationApi* | [**specificationsTreeByCategoryId**](docs/CategorySpecificationApi.md#specificationsTreeByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listTreeByCategoryId/{categoryId} | Get Specifications Tree By Category ID
*CatalogApi.CollectionBetaApi* | [**gETAllCollections**](docs/CollectionBetaApi.md#gETAllCollections) | **GET** /api/catalog_system/pvt/collection/search | Get All Collections
*CatalogApi.CollectionBetaApi* | [**gETAllInactiveCollections**](docs/CollectionBetaApi.md#gETAllInactiveCollections) | **GET** /api/catalog/pvt/collection/inactive | Get All Inactive Collections
*CatalogApi.CollectionBetaApi* | [**gETCollectionsbyseachterms**](docs/CollectionBetaApi.md#gETCollectionsbyseachterms) | **GET** /api/catalog_system/pvt/collection/search/{searchTerms} | Get Collections by search terms
*CatalogApi.CollectionBetaApi* | [**gETImportfileexample**](docs/CollectionBetaApi.md#gETImportfileexample) | **GET** /api/catalog/pvt/collection/stockkeepingunit/importfileexample | Import Collection file example
*CatalogApi.CollectionBetaApi* | [**gETProductsfromacollection**](docs/CollectionBetaApi.md#gETProductsfromacollection) | **GET** /api/catalog/pvt/collection/{collectionId}/products | Get products from a collection
*CatalogApi.CollectionBetaApi* | [**pOSTAddproductsbyimportfile**](docs/CollectionBetaApi.md#pOSTAddproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importinsert | Add products to Collection by imported file
*CatalogApi.CollectionBetaApi* | [**pOSTCreateCollection**](docs/CollectionBetaApi.md#pOSTCreateCollection) | **POST** /api/catalog/pvt/collection/ | Create Collection
*CatalogApi.CollectionBetaApi* | [**pOSTRemoveproductsbyimportfile**](docs/CollectionBetaApi.md#pOSTRemoveproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importexclude | Remove products from Collection by imported file
*CatalogApi.CommercialConditionsApi* | [**getAllCommercialConditions**](docs/CommercialConditionsApi.md#getAllCommercialConditions) | **GET** /api/catalog_system/pvt/commercialcondition/list | Get all commercial conditions
*CatalogApi.CommercialConditionsApi* | [**getCommercialConditions**](docs/CommercialConditionsApi.md#getCommercialConditions) | **GET** /api/catalog_system/pvt/commercialcondition/{commercialConditionId} | Get commercial condition
*CatalogApi.GiftListApi* | [**getGiftList**](docs/GiftListApi.md#getGiftList) | **GET** /api/addon/pvt/giftlist/get/{listId} | Get Gift List
*CatalogApi.LegacyCollectionApi* | [**apiCatalogPvtCollectionCollectionIdDelete**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdDelete) | **DELETE** /api/catalog/pvt/collection/{collectionId} | Delete Collection
*CatalogApi.LegacyCollectionApi* | [**apiCatalogPvtCollectionCollectionIdGet**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdGet) | **GET** /api/catalog/pvt/collection/{collectionId} | Get Collection
*CatalogApi.LegacyCollectionApi* | [**apiCatalogPvtCollectionCollectionIdPut**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdPut) | **PUT** /api/catalog/pvt/collection/{collectionId} | Update Collection
*CatalogApi.LegacyCollectionApi* | [**apiCatalogPvtCollectionPost**](docs/LegacyCollectionApi.md#apiCatalogPvtCollectionPost) | **POST** /api/catalog/pvt/collection | Create Collection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtCollectionCollectionIdPositionPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdPositionPost) | **POST** /api/catalog/pvt/collection/{collectionId}/position | Reposition SKU on the Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtCollectionCollectionIdSubcollectionGet**](docs/LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdSubcollectionGet) | **GET** /api/catalog/pvt/collection/{collectionId}/subcollection | Get Subcollection by Collection ID
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionPost) | **POST** /api/catalog/pvt/subcollection | Create Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{brandId} | Delete Brand from Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{categoryId} | Delete Category from Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdBrandPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/brand | Associate Brand to Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdCategoryPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdCategoryPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/category | Associate Category to Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId} | Delete Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdGet**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdGet) | **GET** /api/catalog/pvt/subcollection/{subCollectionId} | Get Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdPut**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdPut) | **PUT** /api/catalog/pvt/subcollection/{subCollectionId} | Update Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit | Add SKU to Subcollection
*CatalogApi.LegacySubcollectionApi* | [**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete**](docs/LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit/{skuId} | Delete SKU from Subcollection
*CatalogApi.NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredDelete**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured | Delete Non Structured Specification by SKU ID
*CatalogApi.NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredGet**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredGet) | **GET** /api/catalog/pvt/specification/nonstructured | Get Non Structured Specification by SKU ID
*CatalogApi.NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredIdDelete**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured/{Id} | Delete Non Structured Specification
*CatalogApi.NonStructuredSpecificationApi* | [**apiCatalogPvtSpecificationNonstructuredIdGet**](docs/NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdGet) | **GET** /api/catalog/pvt/specification/nonstructured/{Id} | Get Non Structured Specification by ID
*CatalogApi.ProductApi* | [**apiCatalogPvtProductPost**](docs/ProductApi.md#apiCatalogPvtProductPost) | **POST** /api/catalog/pvt/product | Create Product with Category and Brand
*CatalogApi.ProductApi* | [**apiCatalogPvtProductProductIdPut**](docs/ProductApi.md#apiCatalogPvtProductProductIdPut) | **PUT** /api/catalog/pvt/product/{productId} | Update Product
*CatalogApi.ProductApi* | [**getProductbyid**](docs/ProductApi.md#getProductbyid) | **GET** /api/catalog/pvt/product/{productId} | Get Product by ID
*CatalogApi.ProductApi* | [**productAndSkuIds**](docs/ProductApi.md#productAndSkuIds) | **GET** /api/catalog_system/pvt/products/GetProductAndSkuIds | Get Product and SKU IDs
*CatalogApi.ProductApi* | [**productVariations**](docs/ProductApi.md#productVariations) | **GET** /api/catalog_system/pub/products/variations/{productId} | Get Product&#39;s SKUs by Product ID
*CatalogApi.ProductApi* | [**productandTradePolicy**](docs/ProductApi.md#productandTradePolicy) | **GET** /api/catalog_system/pvt/products/productget/{productId} | Get Product and its general context
*CatalogApi.ProductApi* | [**productbyRefId**](docs/ProductApi.md#productbyRefId) | **GET** /api/catalog_system/pvt/products/productgetbyrefid/{refId} | Get Product by RefId
*CatalogApi.ProductApi* | [**reviewRateProduct**](docs/ProductApi.md#reviewRateProduct) | **GET** /api/addon/pvt/review/GetProductRate/{productId} | Get Product Review Rate by Product ID
*CatalogApi.ProductIndexingApi* | [**indexedInfo**](docs/ProductIndexingApi.md#indexedInfo) | **GET** /api/catalog_system/pvt/products/GetIndexedInfo/{productId} | Get Product Indexed Information
*CatalogApi.ProductSpecificationApi* | [**apiCatalogPvtProductProductIdSpecificationPost**](docs/ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationPost) | **POST** /api/catalog/pvt/product/{productId}/specification | Associate Product Specification
*CatalogApi.ProductSpecificationApi* | [**apiCatalogPvtProductProductIdSpecificationvaluePut**](docs/ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/product/{productId}/specificationvalue | Associate product specification using specification name and group name
*CatalogApi.ProductSpecificationApi* | [**deleteAllProductSpecifications**](docs/ProductSpecificationApi.md#deleteAllProductSpecifications) | **DELETE** /api/catalog/pvt/product/{productId}/specification | Delete all Product Specifications by Product ID
*CatalogApi.ProductSpecificationApi* | [**deleteaProductSpecification**](docs/ProductSpecificationApi.md#deleteaProductSpecification) | **DELETE** /api/catalog/pvt/product/{productId}/specification/{specificationId} | Delete a specific Product Specification
*CatalogApi.ProductSpecificationApi* | [**getProductSpecification**](docs/ProductSpecificationApi.md#getProductSpecification) | **GET** /api/catalog_system/pvt/products/{productId}/specification | Get Product Specification by Product ID
*CatalogApi.ProductSpecificationApi* | [**getProductSpecificationbyProductID**](docs/ProductSpecificationApi.md#getProductSpecificationbyProductID) | **GET** /api/catalog/pvt/product/{productId}/specification | Get Product Specification and its information by Product ID
*CatalogApi.ProductSpecificationApi* | [**updateProductSpecification**](docs/ProductSpecificationApi.md#updateProductSpecification) | **POST** /api/catalog_system/pvt/products/{productId}/specification | Update Product Specification by Product ID
*CatalogApi.SKUApi* | [**apiCatalogPvtStockkeepingunitGet**](docs/SKUApi.md#apiCatalogPvtStockkeepingunitGet) | **GET** /api/catalog/pvt/stockkeepingunit | Get SKU by RefId
*CatalogApi.SKUApi* | [**apiCatalogPvtStockkeepingunitPost**](docs/SKUApi.md#apiCatalogPvtStockkeepingunitPost) | **POST** /api/catalog/pvt/stockkeepingunit | Create SKU
*CatalogApi.SKUApi* | [**apiCatalogPvtStockkeepingunitSkuIdPut**](docs/SKUApi.md#apiCatalogPvtStockkeepingunitSkuIdPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId} | Update SKU
*CatalogApi.SKUApi* | [**listallSKUIDs**](docs/SKUApi.md#listallSKUIDs) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitids | List all SKU IDs
*CatalogApi.SKUApi* | [**sku**](docs/SKUApi.md#sku) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId} | Get SKU
*CatalogApi.SKUApi* | [**skuContext**](docs/SKUApi.md#skuContext) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyid/{skuId} | Get SKU and context
*CatalogApi.SKUApi* | [**skuIdbyRefId**](docs/SKUApi.md#skuIdbyRefId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/{refId} | Get SKU ID by Reference ID
*CatalogApi.SKUApi* | [**skuIdlistbyRefIdlist**](docs/SKUApi.md#skuIdlistbyRefIdlist) | **POST** /api/catalog_system/pub/sku/stockkeepingunitidsbyrefids | Retrieve SKU ID list by Reference ID list
*CatalogApi.SKUApi* | [**skubyAlternateId**](docs/SKUApi.md#skubyAlternateId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyalternateId/{alternateId} | Get SKU by Alternate ID
*CatalogApi.SKUApi* | [**skulistbyProductId**](docs/SKUApi.md#skulistbyProductId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitByProductId/{productId} | Get SKU list by Product ID
*CatalogApi.SKUAttachmentApi* | [**apiCatalogPvtSkuattachmentDelete**](docs/SKUAttachmentApi.md#apiCatalogPvtSkuattachmentDelete) | **DELETE** /api/catalog/pvt/skuattachment | Dissociate attachments and SKUs
*CatalogApi.SKUAttachmentApi* | [**apiCatalogPvtSkuattachmentPost**](docs/SKUAttachmentApi.md#apiCatalogPvtSkuattachmentPost) | **POST** /api/catalog/pvt/skuattachment | Associate SKU Attachment
*CatalogApi.SKUAttachmentApi* | [**apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete**](docs/SKUAttachmentApi.md#apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete) | **DELETE** /api/catalog/pvt/skuattachment/{skuAttachmentAssociationId} | Delete SKU Attachment by Attachment Association ID
*CatalogApi.SKUAttachmentApi* | [**apiCatalogPvtStockkeepingunitSkuIdAttachmentGet**](docs/SKUAttachmentApi.md#apiCatalogPvtStockkeepingunitSkuIdAttachmentGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/attachment | Get SKU Attachments by SKU ID
*CatalogApi.SKUAttachmentApi* | [**associateattachmentstoSKU**](docs/SKUAttachmentApi.md#associateattachmentstoSKU) | **POST** /api/catalog_system/pvt/sku/associateattachments | Associate attachments to an SKU
*CatalogApi.SKUComplementApi* | [**createSKUComplement**](docs/SKUComplementApi.md#createSKUComplement) | **POST** /api/catalog/pvt/skucomplement | Create SKU Complement
*CatalogApi.SKUComplementApi* | [**deleteSKUComplementbySKUComplementID**](docs/SKUComplementApi.md#deleteSKUComplementbySKUComplementID) | **DELETE** /api/catalog/pvt/skucomplement/{skuComplementId} | Delete SKU Complement by SKU Complement ID
*CatalogApi.SKUComplementApi* | [**getSKUComplementbySKUComplementID**](docs/SKUComplementApi.md#getSKUComplementbySKUComplementID) | **GET** /api/catalog/pvt/skucomplement/{skuComplementId} | Get SKU Complement by SKU Complement ID
*CatalogApi.SKUComplementApi* | [**getSKUComplementbySKUID**](docs/SKUComplementApi.md#getSKUComplementbySKUID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement | Get SKU Complement by SKU ID
*CatalogApi.SKUComplementApi* | [**getSKUComplementsbyComplementTypeID**](docs/SKUComplementApi.md#getSKUComplementsbyComplementTypeID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement/{complementTypeId} | Get SKU Complements by Complement Type ID
*CatalogApi.SKUComplementApi* | [**getSKUcomplementsbytype**](docs/SKUComplementApi.md#getSKUcomplementsbytype) | **GET** /api/catalog_system/pvt/sku/complements/{parentSkuId}/{type} | Get SKU complements by type
*CatalogApi.SKUEANApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanDelete**](docs/SKUEANApi.md#apiCatalogPvtStockkeepingunitSkuIdEanDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/ean | Delete all SKU EAN values
*CatalogApi.SKUEANApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanEanDelete**](docs/SKUEANApi.md#apiCatalogPvtStockkeepingunitSkuIdEanEanDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean} | Delete SKU EAN
*CatalogApi.SKUEANApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanEanPost**](docs/SKUEANApi.md#apiCatalogPvtStockkeepingunitSkuIdEanEanPost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean} | Create SKU EAN
*CatalogApi.SKUEANApi* | [**apiCatalogPvtStockkeepingunitSkuIdEanGet**](docs/SKUEANApi.md#apiCatalogPvtStockkeepingunitSkuIdEanGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/ean | Get EAN by SKU ID
*CatalogApi.SKUEANApi* | [**skubyEAN**](docs/SKUEANApi.md#skubyEAN) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyean/{ean} | Get SKU by EAN
*CatalogApi.SKUFileApi* | [**apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut**](docs/SKUFileApi.md#apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut) | **PUT** /api/catalog/pvt/stockkeepingunit/copy/{skuIdfrom}/{skuIdto}/file/ | Copy Files from an SKU to another SKU
*CatalogApi.SKUFileApi* | [**apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete**](docs/SKUFileApi.md#apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/disassociate/{skuId}/file/{skuFileId} | Disassociate SKU File
*CatalogApi.SKUFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileDelete**](docs/SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Delete All SKU Files
*CatalogApi.SKUFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileGet**](docs/SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Get SKU Files
*CatalogApi.SKUFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFilePost**](docs/SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFilePost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Create SKU File
*CatalogApi.SKUFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete**](docs/SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Delete SKU Image File
*CatalogApi.SKUFileApi* | [**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut**](docs/SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Update SKU File
*CatalogApi.SKUKitApi* | [**apiCatalogPvtStockkeepingunitkitDelete**](docs/SKUKitApi.md#apiCatalogPvtStockkeepingunitkitDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit | Delete SKU Kit by SKU ID or Parent SKU ID
*CatalogApi.SKUKitApi* | [**apiCatalogPvtStockkeepingunitkitGet**](docs/SKUKitApi.md#apiCatalogPvtStockkeepingunitkitGet) | **GET** /api/catalog/pvt/stockkeepingunitkit | Get SKU Kit by SKU ID or Parent SKU ID
*CatalogApi.SKUKitApi* | [**apiCatalogPvtStockkeepingunitkitKitIdDelete**](docs/SKUKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Delete SKU Kit by KitId
*CatalogApi.SKUKitApi* | [**apiCatalogPvtStockkeepingunitkitKitIdGet**](docs/SKUKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdGet) | **GET** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Get SKU Kit
*CatalogApi.SKUKitApi* | [**apiCatalogPvtStockkeepingunitkitPost**](docs/SKUKitApi.md#apiCatalogPvtStockkeepingunitkitPost) | **POST** /api/catalog/pvt/stockkeepingunitkit | Create SKU Kit
*CatalogApi.SKUSellerApi* | [**apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost**](docs/SKUSellerApi.md#apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost) | **POST** /api/catalog_system/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId} | Change Notification with Seller ID and Seller SKU ID
*CatalogApi.SKUSellerApi* | [**changeNotification**](docs/SKUSellerApi.md#changeNotification) | **POST** /api/catalog_system/pvt/skuseller/changenotification/{skuId} | Change Notification with SKU ID
*CatalogApi.SKUSellerApi* | [**deleteSKUsellerassociation**](docs/SKUSellerApi.md#deleteSKUsellerassociation) | **POST** /api/catalog_system/pvt/skuseller/remove/{sellerId}/{sellerSkuId} | Remove a seller&#39;s SKU binding
*CatalogApi.SKUSellerApi* | [**getSKUseller**](docs/SKUSellerApi.md#getSKUseller) | **GET** /api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId} | Get details of a seller&#39;s SKU
*CatalogApi.SKUServiceApi* | [**apiCatalogPvtSkuservicePost**](docs/SKUServiceApi.md#apiCatalogPvtSkuservicePost) | **POST** /api/catalog/pvt/skuservice | Associate SKU Service
*CatalogApi.SKUServiceApi* | [**apiCatalogPvtSkuserviceSkuServiceIdDelete**](docs/SKUServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdDelete) | **DELETE** /api/catalog/pvt/skuservice/{skuServiceId} | Dissociate SKU Service
*CatalogApi.SKUServiceApi* | [**apiCatalogPvtSkuserviceSkuServiceIdGet**](docs/SKUServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdGet) | **GET** /api/catalog/pvt/skuservice/{skuServiceId} | Get SKU Service
*CatalogApi.SKUServiceApi* | [**apiCatalogPvtSkuserviceSkuServiceIdPut**](docs/SKUServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdPut) | **PUT** /api/catalog/pvt/skuservice/{skuServiceId} | Update SKU Service
*CatalogApi.SKUServiceAttachmentApi* | [**apiCatalogPvtSkuservicetypeattachmentDelete**](docs/SKUServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment | Dissociate Attachment by Attachment ID or SKU Service Type ID
*CatalogApi.SKUServiceAttachmentApi* | [**apiCatalogPvtSkuservicetypeattachmentPost**](docs/SKUServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentPost) | **POST** /api/catalog/pvt/skuservicetypeattachment | Associate SKU Service Attachment
*CatalogApi.SKUServiceAttachmentApi* | [**apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete**](docs/SKUServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment/{skuServiceTypeAttachmentId} | Dissociate Attachment from SKU Service Type
*CatalogApi.SKUServiceTypeApi* | [**apiCatalogPvtSkuservicetypePost**](docs/SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypePost) | **POST** /api/catalog/pvt/skuservicetype | Create SKU Service Type
*CatalogApi.SKUServiceTypeApi* | [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete**](docs/SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete) | **DELETE** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Delete SKU Service Type
*CatalogApi.SKUServiceTypeApi* | [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet**](docs/SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet) | **GET** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Get SKU Service Type
*CatalogApi.SKUServiceTypeApi* | [**apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut**](docs/SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut) | **PUT** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Update SKU Service Type
*CatalogApi.SKUServiceValueApi* | [**apiCatalogPvtSkuservicevaluePost**](docs/SKUServiceValueApi.md#apiCatalogPvtSkuservicevaluePost) | **POST** /api/catalog/pvt/skuservicevalue | Create SKU Service Value
*CatalogApi.SKUServiceValueApi* | [**apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete**](docs/SKUServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete) | **DELETE** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Delete SKU Service Value
*CatalogApi.SKUServiceValueApi* | [**apiCatalogPvtSkuservicevalueSkuServiceValueIdGet**](docs/SKUServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdGet) | **GET** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Get SKU Service Value
*CatalogApi.SKUServiceValueApi* | [**apiCatalogPvtSkuservicevalueSkuServiceValueIdPut**](docs/SKUServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdPut) | **PUT** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Update SKU Service Value
*CatalogApi.SKUSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete**](docs/SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Delete all SKU Specifications
*CatalogApi.SKUSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationGet**](docs/SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Get SKU Specifications
*CatalogApi.SKUSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationPost**](docs/SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Associate SKU Specification
*CatalogApi.SKUSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationPut**](docs/SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Update SKU Specification
*CatalogApi.SKUSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete**](docs/SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification/{specificationId} | Delete SKU Specification
*CatalogApi.SKUSpecificationApi* | [**apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut**](docs/SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specificationvalue | Associate SKU specification using specification name and group name
*CatalogApi.SalesChannelApi* | [**salesChannelList**](docs/SalesChannelApi.md#salesChannelList) | **GET** /api/catalog_system/pvt/saleschannel/list | Get Sales Channel List
*CatalogApi.SalesChannelApi* | [**salesChannelbyId**](docs/SalesChannelApi.md#salesChannelbyId) | **GET** /api/catalog_system/pub/saleschannel/{salesChannelId} | Get Sales Channel by ID
*CatalogApi.SellerApi* | [**createSeller**](docs/SellerApi.md#createSeller) | **POST** /api/catalog_system/pvt/seller | Create Seller
*CatalogApi.SellerApi* | [**getSellerbyId**](docs/SellerApi.md#getSellerbyId) | **GET** /api/catalog_system/pvt/seller/{sellerId} | Get Seller by ID
*CatalogApi.SellerApi* | [**getSellersbyId**](docs/SellerApi.md#getSellersbyId) | **GET** /api/catalog_system/pvt/sellers/{sellerId} | Get Seller by ID
*CatalogApi.SellerApi* | [**sellerList**](docs/SellerApi.md#sellerList) | **GET** /api/catalog_system/pvt/seller/list | Get Seller List
*CatalogApi.SellerApi* | [**updateSeller**](docs/SellerApi.md#updateSeller) | **PUT** /api/catalog_system/pvt/seller | Update Seller
*CatalogApi.SimilarCategoryApi* | [**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete**](docs/SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Delete Similar Category
*CatalogApi.SimilarCategoryApi* | [**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost**](docs/SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost) | **POST** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Add Similar Category
*CatalogApi.SimilarCategoryApi* | [**apiCatalogPvtProductProductIdSimilarcategoryGet**](docs/SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryGet) | **GET** /api/catalog/pvt/product/{productId}/similarcategory/ | Get Similar Categories
*CatalogApi.SpecificationApi* | [**apiCatalogPvtSpecificationPost**](docs/SpecificationApi.md#apiCatalogPvtSpecificationPost) | **POST** /api/catalog/pvt/specification | Create Specification
*CatalogApi.SpecificationApi* | [**apiCatalogPvtSpecificationSpecificationIdGet**](docs/SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdGet) | **GET** /api/catalog/pvt/specification/{specificationId} | Get Specification
*CatalogApi.SpecificationApi* | [**apiCatalogPvtSpecificationSpecificationIdPut**](docs/SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdPut) | **PUT** /api/catalog/pvt/specification/{specificationId} | Update Specification
*CatalogApi.SpecificationFieldApi* | [**specificationsField**](docs/SpecificationFieldApi.md#specificationsField) | **GET** /api/catalog_system/pub/specification/fieldGet/{fieldId} | Get Specification Field
*CatalogApi.SpecificationFieldApi* | [**specificationsInsertField**](docs/SpecificationFieldApi.md#specificationsInsertField) | **POST** /api/catalog_system/pvt/specification/field | Create Specification Field
*CatalogApi.SpecificationFieldApi* | [**specificationsInsertFieldUpdate**](docs/SpecificationFieldApi.md#specificationsInsertFieldUpdate) | **PUT** /api/catalog_system/pvt/specification/field | Update Specification Field
*CatalogApi.SpecificationFieldValueApi* | [**specificationsGetFieldValue**](docs/SpecificationFieldValueApi.md#specificationsGetFieldValue) | **GET** /api/catalog_system/pvt/specification/fieldValue/{fieldValueId} | Get Specification Field Value
*CatalogApi.SpecificationFieldValueApi* | [**specificationsInsertFieldValue**](docs/SpecificationFieldValueApi.md#specificationsInsertFieldValue) | **POST** /api/catalog_system/pvt/specification/fieldValue | Create Specification Field Value
*CatalogApi.SpecificationFieldValueApi* | [**specificationsUpdateFieldValue**](docs/SpecificationFieldValueApi.md#specificationsUpdateFieldValue) | **PUT** /api/catalog_system/pvt/specification/fieldValue | Update Specification Field Value
*CatalogApi.SpecificationFieldValueApi* | [**specificationsValuesByFieldId**](docs/SpecificationFieldValueApi.md#specificationsValuesByFieldId) | **GET** /api/catalog_system/pub/specification/fieldvalue/{fieldId} | Get Specification Values By Field ID
*CatalogApi.SpecificationGroupApi* | [**apiCatalogPvtSpecificationgroupGroupIdPut**](docs/SpecificationGroupApi.md#apiCatalogPvtSpecificationgroupGroupIdPut) | **PUT** /api/catalog/pvt/specificationgroup/{groupId} | Update Specification Group
*CatalogApi.SpecificationGroupApi* | [**specificationGroupInsert2**](docs/SpecificationGroupApi.md#specificationGroupInsert2) | **POST** /api/catalog/pvt/specificationgroup | Create Specification Group
*CatalogApi.SpecificationGroupApi* | [**specificationsGroupGet**](docs/SpecificationGroupApi.md#specificationsGroupGet) | **GET** /api/catalog_system/pub/specification/groupGet/{groupId} | Get Specification Group
*CatalogApi.SpecificationGroupApi* | [**specificationsGroupListbyCategory**](docs/SpecificationGroupApi.md#specificationsGroupListbyCategory) | **GET** /api/catalog_system/pvt/specification/groupbycategory/{categoryId} | List Specification Group by Category
*CatalogApi.SpecificationValueApi* | [**apiCatalogPvtSpecificationvaluePost**](docs/SpecificationValueApi.md#apiCatalogPvtSpecificationvaluePost) | **POST** /api/catalog/pvt/specificationvalue | Create Specification Value
*CatalogApi.SpecificationValueApi* | [**apiCatalogPvtSpecificationvalueSpecificationValueIdGet**](docs/SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdGet) | **GET** /api/catalog/pvt/specificationvalue/{specificationValueId} | Get Specification Value
*CatalogApi.SpecificationValueApi* | [**apiCatalogPvtSpecificationvalueSpecificationValueIdPut**](docs/SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdPut) | **PUT** /api/catalog/pvt/specificationvalue/{specificationValueId} | Update Specification Value
*CatalogApi.SupplierApi* | [**apiCatalogPvtSupplierPost**](docs/SupplierApi.md#apiCatalogPvtSupplierPost) | **POST** /api/catalog/pvt/supplier | Create Supplier
*CatalogApi.SupplierApi* | [**apiCatalogPvtSupplierSupplierIdDelete**](docs/SupplierApi.md#apiCatalogPvtSupplierSupplierIdDelete) | **DELETE** /api/catalog/pvt/supplier/{supplierId} | Delete Supplier
*CatalogApi.SupplierApi* | [**apiCatalogPvtSupplierSupplierIdPut**](docs/SupplierApi.md#apiCatalogPvtSupplierSupplierIdPut) | **PUT** /api/catalog/pvt/supplier/{supplierId} | Update Supplier
*CatalogApi.TradePolicyApi* | [**apiCatalogPvtProductProductIdSalespolicyGet**](docs/TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyGet) | **GET** /api/catalog/pvt/product/{productId}/salespolicy | Get Trade Policies by Product ID
*CatalogApi.TradePolicyApi* | [**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete**](docs/TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Remove Product from Trade Policy
*CatalogApi.TradePolicyApi* | [**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost**](docs/TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost) | **POST** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Associate Product with Trade Policy
*CatalogApi.TradePolicyApi* | [**apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet**](docs/TradePolicyApi.md#apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel | List all SKUs of a Trade Policy


## Documentation for Models

 - [CatalogApi.AlternateIds](docs/AlternateIds.md)
 - [CatalogApi.ApiCatalogPvtAttachmentsGet200Response](docs/ApiCatalogPvtAttachmentsGet200Response.md)
 - [CatalogApi.ApiCatalogPvtCategoryCategoryIdPutRequest](docs/ApiCatalogPvtCategoryCategoryIdPutRequest.md)
 - [CatalogApi.ApiCatalogPvtCollectionCollectionIdPositionPostRequest](docs/ApiCatalogPvtCollectionCollectionIdPositionPostRequest.md)
 - [CatalogApi.ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner](docs/ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtCollectionPost200Response](docs/ApiCatalogPvtCollectionPost200Response.md)
 - [CatalogApi.ApiCatalogPvtProductPost200Response](docs/ApiCatalogPvtProductPost200Response.md)
 - [CatalogApi.ApiCatalogPvtProductPostRequest](docs/ApiCatalogPvtProductPostRequest.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdPutRequest](docs/ApiCatalogPvtProductProductIdPutRequest.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner](docs/ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response](docs/ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner](docs/ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdSpecificationPost200Response](docs/ApiCatalogPvtProductProductIdSpecificationPost200Response.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdSpecificationPostRequest](docs/ApiCatalogPvtProductProductIdSpecificationPostRequest.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner](docs/ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtProductProductIdSpecificationvaluePutRequest](docs/ApiCatalogPvtProductProductIdSpecificationvaluePutRequest.md)
 - [CatalogApi.ApiCatalogPvtSkuattachmentPost200Response](docs/ApiCatalogPvtSkuattachmentPost200Response.md)
 - [CatalogApi.ApiCatalogPvtSkuservicetypeattachmentPost200Response](docs/ApiCatalogPvtSkuservicetypeattachmentPost200Response.md)
 - [CatalogApi.ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner](docs/ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtSpecificationPost200Response](docs/ApiCatalogPvtSpecificationPost200Response.md)
 - [CatalogApi.ApiCatalogPvtSpecificationPostRequest](docs/ApiCatalogPvtSpecificationPostRequest.md)
 - [CatalogApi.ApiCatalogPvtSpecificationgroupGroupIdPut200Response](docs/ApiCatalogPvtSpecificationgroupGroupIdPut200Response.md)
 - [CatalogApi.ApiCatalogPvtSpecificationvaluePost200Response](docs/ApiCatalogPvtSpecificationvaluePost200Response.md)
 - [CatalogApi.ApiCatalogPvtSpecificationvaluePostRequest](docs/ApiCatalogPvtSpecificationvaluePostRequest.md)
 - [CatalogApi.ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response](docs/ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner](docs/ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitGet200Response](docs/ApiCatalogPvtStockkeepingunitGet200Response.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitPost200Response](docs/ApiCatalogPvtStockkeepingunitPost200Response.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitPostRequest](docs/ApiCatalogPvtStockkeepingunitPostRequest.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner](docs/ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response](docs/ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdPut200Response](docs/ApiCatalogPvtStockkeepingunitSkuIdPut200Response.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdPutRequest](docs/ApiCatalogPvtStockkeepingunitSkuIdPutRequest.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest](docs/ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner](docs/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner.md)
 - [CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest](docs/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest.md)
 - [CatalogApi.ApiCatalogPvtSubcollectionPost200Response](docs/ApiCatalogPvtSubcollectionPost200Response.md)
 - [CatalogApi.ApiCatalogPvtSubcollectionPostRequest](docs/ApiCatalogPvtSubcollectionPostRequest.md)
 - [CatalogApi.ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response](docs/ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response.md)
 - [CatalogApi.ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response](docs/ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response.md)
 - [CatalogApi.ApiCatalogPvtSubcollectionSubCollectionIdPutRequest](docs/ApiCatalogPvtSubcollectionSubCollectionIdPutRequest.md)
 - [CatalogApi.ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response](docs/ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response.md)
 - [CatalogApi.ArrayWithInformationOfAllTheCommercialConditionsInner](docs/ArrayWithInformationOfAllTheCommercialConditionsInner.md)
 - [CatalogApi.AssociateattachmentstoSKURequest](docs/AssociateattachmentstoSKURequest.md)
 - [CatalogApi.Attachment](docs/Attachment.md)
 - [CatalogApi.AttachmentRequest](docs/AttachmentRequest.md)
 - [CatalogApi.AttachmentResponse](docs/AttachmentResponse.md)
 - [CatalogApi.BrandCreateUpdate](docs/BrandCreateUpdate.md)
 - [CatalogApi.BrandGet](docs/BrandGet.md)
 - [CatalogApi.BrandListPerPage200Response](docs/BrandListPerPage200Response.md)
 - [CatalogApi.Category](docs/Category.md)
 - [CatalogApi.CategorySpecificationInner](docs/CategorySpecificationInner.md)
 - [CatalogApi.CreateCategoryRequest](docs/CreateCategoryRequest.md)
 - [CatalogApi.CreateSeller200Response](docs/CreateSeller200Response.md)
 - [CatalogApi.CreateSellerRequest](docs/CreateSellerRequest.md)
 - [CatalogApi.CurrencyFormatInfo](docs/CurrencyFormatInfo.md)
 - [CatalogApi.Dimension](docs/Dimension.md)
 - [CatalogApi.DomainsInner](docs/DomainsInner.md)
 - [CatalogApi.Field](docs/Field.md)
 - [CatalogApi.GetCategoryTree](docs/GetCategoryTree.md)
 - [CatalogApi.GetCategoryTreeChild](docs/GetCategoryTreeChild.md)
 - [CatalogApi.GetCommercialConditions200Response](docs/GetCommercialConditions200Response.md)
 - [CatalogApi.GetGiftList200Response](docs/GetGiftList200Response.md)
 - [CatalogApi.GetProductSpecificationbyProductID200ResponseInner](docs/GetProductSpecificationbyProductID200ResponseInner.md)
 - [CatalogApi.GetProductbyid200Response](docs/GetProductbyid200Response.md)
 - [CatalogApi.GetSKUAltID](docs/GetSKUAltID.md)
 - [CatalogApi.GetSKUandContext](docs/GetSKUandContext.md)
 - [CatalogApi.GetSKUcomplementsbytype200Response](docs/GetSKUcomplementsbytype200Response.md)
 - [CatalogApi.GetSKUseller200Response](docs/GetSKUseller200Response.md)
 - [CatalogApi.GetSellerbyId200Response](docs/GetSellerbyId200Response.md)
 - [CatalogApi.GetSellersbyId200Response](docs/GetSellersbyId200Response.md)
 - [CatalogApi.GetSpecFieldValue](docs/GetSpecFieldValue.md)
 - [CatalogApi.GetorUpdateProductSpecification](docs/GetorUpdateProductSpecification.md)
 - [CatalogApi.GiftListMembersInner](docs/GiftListMembersInner.md)
 - [CatalogApi.Image](docs/Image.md)
 - [CatalogApi.Paging](docs/Paging.md)
 - [CatalogApi.ProductAndSkuIds200Response](docs/ProductAndSkuIds200Response.md)
 - [CatalogApi.ProductAndSkuIds200ResponseData](docs/ProductAndSkuIds200ResponseData.md)
 - [CatalogApi.ProductAndSkuIds200ResponseRange](docs/ProductAndSkuIds200ResponseRange.md)
 - [CatalogApi.ProductSpecification](docs/ProductSpecification.md)
 - [CatalogApi.ProductVariations200Response](docs/ProductVariations200Response.md)
 - [CatalogApi.ProductVariations200ResponseSkusInner](docs/ProductVariations200ResponseSkusInner.md)
 - [CatalogApi.ProductVariations200ResponseSkusInnerMeasures](docs/ProductVariations200ResponseSkusInnerMeasures.md)
 - [CatalogApi.ProductandTradePolicy200Response](docs/ProductandTradePolicy200Response.md)
 - [CatalogApi.ProductbyRefId200Response](docs/ProductbyRefId200Response.md)
 - [CatalogApi.RealDimension](docs/RealDimension.md)
 - [CatalogApi.RequestBody](docs/RequestBody.md)
 - [CatalogApi.RequestBody1](docs/RequestBody1.md)
 - [CatalogApi.RequestBody10](docs/RequestBody10.md)
 - [CatalogApi.RequestBody11](docs/RequestBody11.md)
 - [CatalogApi.RequestBody12](docs/RequestBody12.md)
 - [CatalogApi.RequestBody2](docs/RequestBody2.md)
 - [CatalogApi.RequestBody3](docs/RequestBody3.md)
 - [CatalogApi.RequestBody4](docs/RequestBody4.md)
 - [CatalogApi.RequestBody5](docs/RequestBody5.md)
 - [CatalogApi.RequestBody6](docs/RequestBody6.md)
 - [CatalogApi.RequestBody7](docs/RequestBody7.md)
 - [CatalogApi.RequestBody8](docs/RequestBody8.md)
 - [CatalogApi.RequestBody9](docs/RequestBody9.md)
 - [CatalogApi.ResquestBody](docs/ResquestBody.md)
 - [CatalogApi.ResquestBody1](docs/ResquestBody1.md)
 - [CatalogApi.SKUFileURL](docs/SKUFileURL.md)
 - [CatalogApi.SKUService](docs/SKUService.md)
 - [CatalogApi.SKUServiceTypeRequest](docs/SKUServiceTypeRequest.md)
 - [CatalogApi.SKUServiceTypeResponse](docs/SKUServiceTypeResponse.md)
 - [CatalogApi.SKUServiceValueRequest](docs/SKUServiceValueRequest.md)
 - [CatalogApi.SKUServiceValueResponse](docs/SKUServiceValueResponse.md)
 - [CatalogApi.SKUSpecificationResponse](docs/SKUSpecificationResponse.md)
 - [CatalogApi.SalesChannelbyId200Response](docs/SalesChannelbyId200Response.md)
 - [CatalogApi.Sku200Response](docs/Sku200Response.md)
 - [CatalogApi.SkuComplementInner](docs/SkuComplementInner.md)
 - [CatalogApi.SkuKit](docs/SkuKit.md)
 - [CatalogApi.SkuSeller](docs/SkuSeller.md)
 - [CatalogApi.SkuSpecification](docs/SkuSpecification.md)
 - [CatalogApi.SkulistbyProductId](docs/SkulistbyProductId.md)
 - [CatalogApi.SpecificationGroupInsert2200Response](docs/SpecificationGroupInsert2200Response.md)
 - [CatalogApi.SpecificationGroupInsertRequest](docs/SpecificationGroupInsertRequest.md)
 - [CatalogApi.SpecificationsField200Response](docs/SpecificationsField200Response.md)
 - [CatalogApi.SpecificationsGroup](docs/SpecificationsGroup.md)
 - [CatalogApi.SpecificationsInsertFieldRequest](docs/SpecificationsInsertFieldRequest.md)
 - [CatalogApi.SpecificationsInsertFieldUpdateRequest](docs/SpecificationsInsertFieldUpdateRequest.md)
 - [CatalogApi.SpecificationsInsertFieldValueRequest](docs/SpecificationsInsertFieldValueRequest.md)
 - [CatalogApi.SpecificationsUpdateFieldValueRequest](docs/SpecificationsUpdateFieldValueRequest.md)
 - [CatalogApi.SupplierRequest](docs/SupplierRequest.md)
 - [CatalogApi.SupplierResponse](docs/SupplierResponse.md)
 - [CatalogApi.UpdateSeller200Response](docs/UpdateSeller200Response.md)
 - [CatalogApi.UpdateSellerRequest](docs/UpdateSellerRequest.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### appKey


- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppKey
- **Location**: HTTP header

### appToken


- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppToken
- **Location**: HTTP header

