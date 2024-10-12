/**
 * Catalog API
 *   > Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.    Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.      ## Index    - [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).  - [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).  - [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).  - [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.  - [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).  - [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.  - [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).  - [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).  - [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.  - [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.  - [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.  - [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).  - [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).  - [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).  - [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).  - [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).  - [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).  - [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).  - [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).  - [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).  - [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items.   - [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value.   - [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.  - [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.  - [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.  - [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.  - [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.  - [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).  - [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.  - [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.      ## Common parameters    | Parameter name              | Description                                                                             |  |---------------------------|-----------------------------------------------------------------------------------------|  | `{{accountName}}`         | Store account name                                                                      |  | `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |  | `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |  | `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import GetSKUAltID from '../model/GetSKUAltID';

/**
* SKUEAN service.
* @module api/SKUEANApi
* @version 1.0
*/
export default class SKUEANApi {

    /**
    * Constructs a new SKUEANApi. 
    * @alias module:api/SKUEANApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtStockkeepingunitSkuIdEanDelete operation.
     * @callback module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete all SKU EAN values
     * Deletes all EAN values of an SKU.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU’s unique numerical identifier.
     * @param {module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtStockkeepingunitSkuIdEanDelete(contentType, accept, skuId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanDelete");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanDelete");
      }

      let pathParams = {
        'skuId': skuId
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}/ean', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtStockkeepingunitSkuIdEanEanDelete operation.
     * @callback module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete SKU EAN
     * Deletes the EAN value of an SKU.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU’s unique numerical identifier.
     * @param {String} ean EAN number.
     * @param {module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanEanDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtStockkeepingunitSkuIdEanEanDelete(contentType, accept, skuId, ean, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete");
      }
      // verify the required parameter 'ean' is set
      if (ean === undefined || ean === null) {
        throw new Error("Missing the required parameter 'ean' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanDelete");
      }

      let pathParams = {
        'skuId': skuId,
        'ean': ean
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtStockkeepingunitSkuIdEanEanPost operation.
     * @callback module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanEanPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create SKU EAN
     * Creates or updates the EAN value of an SKU.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU’s unique numerical identifier.
     * @param {String} ean EAN.
     * @param {module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanEanPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtStockkeepingunitSkuIdEanEanPost(contentType, accept, skuId, ean, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost");
      }
      // verify the required parameter 'ean' is set
      if (ean === undefined || ean === null) {
        throw new Error("Missing the required parameter 'ean' when calling apiCatalogPvtStockkeepingunitSkuIdEanEanPost");
      }

      let pathParams = {
        'skuId': skuId,
        'ean': ean
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}/ean/{ean}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtStockkeepingunitSkuIdEanGet operation.
     * @callback module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get EAN by SKU ID
     * Retrieves the EAN of the SKU.   ## Response body example    ```json  [      \"1234567890123\"  ]  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU’s unique numerical identifier.
     * @param {module:api/SKUEANApi~apiCatalogPvtStockkeepingunitSkuIdEanGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    apiCatalogPvtStockkeepingunitSkuIdEanGet(contentType, accept, skuId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdEanGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdEanGet");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdEanGet");
      }

      let pathParams = {
        'skuId': skuId
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ['String'];
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}/ean', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the skubyEAN operation.
     * @callback module:api/SKUEANApi~skubyEANCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetSKUAltID} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU by EAN
     * Retrieves an SKU by its EAN ID.   ## Response body example    ```json  {      \"Id\": 2001773,      \"ProductId\": 2001426,      \"NameComplete\": \"Tabela de Basquete\",      \"ProductName\": \"Tabela de Basquete\",      \"ProductDescription\": \"Tabela de Basquete\",      \"SkuName\": \"Tabela de Basquete\",      \"IsActive\": true,      \"IsTransported\": true,      \"IsInventoried\": true,      \"IsGiftCardRecharge\": false,      \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\",      \"DetailUrl\": \"/tabela-de-basquete/p\",      \"CSCIdentification\": null,      \"BrandId\": \"2000018\",      \"BrandName\": \"MARCA ARGOLO TESTE\",      \"Dimension\": {          \"cubicweight\": 81.6833,          \"height\": 65,          \"length\": 58,          \"weight\": 10000,          \"width\": 130      },      \"RealDimension\": {          \"realCubicWeight\": 274.1375,          \"realHeight\": 241,          \"realLength\": 65,          \"realWeight\": 9800,          \"realWidth\": 105      },      \"ManufacturerCode\": \"\",      \"IsKit\": false,      \"KitItems\": [],      \"Services\": [],      \"Categories\": [],      \"Attachments\": [          {              \"Id\": 3,              \"Name\": \"Mensagem\",              \"Keys\": [                  \"nome;20\",                  \"foto;40\"              ],              \"Fields\": [                  {                      \"FieldName\": \"nome\",                      \"MaxCaracters\": \"20\",                      \"DomainValues\": \"Adalberto,Pedro,João\"                  },                  {                      \"FieldName\": \"foto\",                      \"MaxCaracters\": \"40\",                      \"DomainValues\": null                  }              ],              \"IsActive\": true,              \"IsRequired\": false          }      ],      \"Collections\": [],      \"SkuSellers\": [          {              \"SellerId\": \"1\",              \"StockKeepingUnitId\": 2001773,              \"SellerStockKeepingUnitId\": \"2001773\",              \"IsActive\": true,              \"FreightCommissionPercentage\": 0,              \"ProductCommissionPercentage\": 0          }      ],      \"SalesChannels\": [          1,          2,          3,          10      ],      \"Images\": [          {              \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\",              \"ImageName\": \"\",              \"FileId\": 168952          },          {              \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\",              \"ImageName\": \"\",              \"FileId\": 168953          },          {              \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\",              \"ImageName\": \"\",              \"FileId\": 168954          }      ],      \"SkuSpecifications\": [          {              \"FieldId\": 102,              \"FieldName\": \"Cor\",              \"FieldValueIds\": [                  266              ],              \"FieldValues\": [                  \"Padrão\"              ]          }      ],      \"ProductSpecifications\": [          {              \"FieldId\": 7,              \"FieldName\": \"Faixa Etária\",              \"FieldValueIds\": [                  58,                  56,                  55,                  52              ],              \"FieldValues\": [                  \"5 a 6 anos\",                  \"7 a 8 anos\",                  \"9 a 10 anos\",                  \"Acima de 10 anos\"              ]          },          {              \"FieldId\": 23,              \"FieldName\": \"Fabricante\",              \"FieldValueIds\": [],              \"FieldValues\": [                  \"Xalingo\"              ]          }      ],      \"ProductClustersIds\": \"176,187,192,194,211,217,235,242\",      \"ProductCategoryIds\": \"/59/\",      \"ProductGlobalCategoryId\": null,      \"ProductCategories\": {          \"59\": \"Brinquedos\"      },      \"CommercialConditionId\": 1,      \"RewardValue\": 100.0,      \"AlternateIds\": {          \"Ean\": \"8781\",          \"RefId\": \"878181\"      },      \"AlternateIdValues\": [          \"8781\",          \"878181\"      ],      \"EstimatedDateArrival\": \"\",      \"MeasurementUnit\": \"un\",      \"UnitMultiplier\": 2.0000,      \"InformationSource\": null,      \"ModalType\": \"\"  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} ean EAN of the SKU which you need to retrieve details from.
     * @param {module:api/SKUEANApi~skubyEANCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetSKUAltID}
     */
    skubyEAN(contentType, accept, ean, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling skubyEAN");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling skubyEAN");
      }
      // verify the required parameter 'ean' is set
      if (ean === undefined || ean === null) {
        throw new Error("Missing the required parameter 'ean' when calling skubyEAN");
      }

      let pathParams = {
        'ean': ean
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Type': contentType,
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetSKUAltID;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/sku/stockkeepingunitbyean/{ean}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
