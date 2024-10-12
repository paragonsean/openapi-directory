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
import ApiCatalogPvtProductPost200Response from '../model/ApiCatalogPvtProductPost200Response';
import ApiCatalogPvtProductPostRequest from '../model/ApiCatalogPvtProductPostRequest';
import ApiCatalogPvtProductProductIdPutRequest from '../model/ApiCatalogPvtProductProductIdPutRequest';
import GetProductbyid200Response from '../model/GetProductbyid200Response';
import ProductAndSkuIds200Response from '../model/ProductAndSkuIds200Response';
import ProductVariations200Response from '../model/ProductVariations200Response';
import ProductandTradePolicy200Response from '../model/ProductandTradePolicy200Response';
import ProductbyRefId200Response from '../model/ProductbyRefId200Response';

/**
* Product service.
* @module api/ProductApi
* @version 1.0
*/
export default class ProductApi {

    /**
    * Constructs a new ProductApi. 
    * @alias module:api/ProductApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtProductPost operation.
     * @callback module:api/ProductApi~apiCatalogPvtProductPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtProductPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create Product with Category and Brand
     * This endpoint allows two types of request:    **Type 1:** Creating a new Product as well as a new Category path (including subcategories) and a new Brand by using `CategoryPath` and `BrandName` parameters.    **Type 2:** Creating a new Product given an existing `BrandId` and an existing `CategoryId`.    When creating a product, regardless of the type of request, if there is a need to create a new product with a specific custom product ID, specify the `Id` (integer) in the request body. Otherwise, VTEX will generate the ID automatically.     ## Request body examples     ### Type 1     Request to create a product, associating it to a new Category and a new Brand by using `CategoryPath` and `BrandName`:    ```json  {      \"Name\": \"Black T-Shirt\",      \"CategoryPath\": \"Mens/Clothing/T-Shirts\",      \"BrandName\": \"Nike\",      \"RefId\": \"31011706925\",      \"Title\": \"Black T-Shirt\",      \"LinkId\": \"tshirt-black\",      \"Description\": \"This is a cool Tshirt\",      \"ReleaseDate\": \"2022-01-01T00:00:00\",      \"IsVisible\": true,      \"IsActive\": true,      \"TaxCode\": \"\",      \"MetaTagDescription\": \"tshirt black\",      \"ShowWithoutStock\": true,      \"Score\": 1  }  ```     ### Type 2    Request to create a product, associating it to an existing `CategoryId` and `BrandId`:    ```json  {     \"Name\": \"insert product test\",     \"DepartmentId\": 1,     \"CategoryId\": 2,     \"BrandId\": 2000000,     \"LinkId\": \"insert-product-test\",     \"RefId\": \"310117869\",     \"IsVisible\": true,     \"Description\": \"texto de descrição\",     \"DescriptionShort\": \"Utilize o CEP 04548-005 para frete grátis\",     \"ReleaseDate\": \"2019-01-01T00:00:00\",     \"KeyWords\": \"teste,teste2\",     \"Title\": \"product de teste\",     \"IsActive\": true,     \"TaxCode\": \"\",     \"MetaTagDescription\": \"tag test\",     \"SupplierId\": 1,     \"ShowWithoutStock\": true,     \"AdWordsRemarketingCode\": null,     \"LomadeeCampaignCode\": null,     \"Score\": 1  }  ```     ## Response body example    ```json  {     \"Id\": 52,     \"Name\": \"insert product test\",     \"DepartmentId\": 1,     \"CategoryId\": 2,     \"BrandId\": 2000000,     \"LinkId\": \"insert-product-test\",     \"RefId\": \"310117869\",     \"IsVisible\": true,     \"Description\": \"texto de descrição\",     \"DescriptionShort\": \"Utilize o CEP 04548-005 para frete grátis\",     \"ReleaseDate\": \"2019-01-01T00:00:00\",     \"KeyWords\": \"teste,teste2\",     \"Title\": \"product de teste\",     \"IsActive\": true,     \"TaxCode\": \"\",     \"MetaTagDescription\": \"tag test\",     \"SupplierId\": 1,     \"ShowWithoutStock\": true,     \"AdWordsRemarketingCode\": null,     \"LomadeeCampaignCode\": null,     \"Score\": 1  }  ```      > 📘 Onboarding guide   >  > Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtProductPostRequest} [apiCatalogPvtProductPostRequest] 
     * @param {module:api/ProductApi~apiCatalogPvtProductPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtProductPost200Response}
     */
    apiCatalogPvtProductPost(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtProductPostRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtProductPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtProductPost");
      }

      let pathParams = {
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ApiCatalogPvtProductPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/product', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtProductProductIdPut operation.
     * @callback module:api/ProductApi~apiCatalogPvtProductProductIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtProductPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Product
     * Updates an existing Product.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} productId Product’s unique numerical identifier.
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtProductProductIdPutRequest} [apiCatalogPvtProductProductIdPutRequest] 
     * @param {module:api/ProductApi~apiCatalogPvtProductProductIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtProductPost200Response}
     */
    apiCatalogPvtProductProductIdPut(contentType, accept, productId, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtProductProductIdPutRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtProductProductIdPut");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtProductProductIdPut");
      }
      // verify the required parameter 'productId' is set
      if (productId === undefined || productId === null) {
        throw new Error("Missing the required parameter 'productId' when calling apiCatalogPvtProductProductIdPut");
      }

      let pathParams = {
        'productId': productId
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ApiCatalogPvtProductPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/product/{productId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProductbyid operation.
     * @callback module:api/ProductApi~getProductbyidCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetProductbyid200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Product by ID
     * Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product.   > 📘 Onboarding guide   >  > Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} productId Product’s unique numerical identifier.
     * @param {module:api/ProductApi~getProductbyidCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetProductbyid200Response}
     */
    getProductbyid(contentType, accept, productId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getProductbyid");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getProductbyid");
      }
      // verify the required parameter 'productId' is set
      if (productId === undefined || productId === null) {
        throw new Error("Missing the required parameter 'productId' when calling getProductbyid");
      }

      let pathParams = {
        'productId': productId
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
      let returnType = GetProductbyid200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/product/{productId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productAndSkuIds operation.
     * @callback module:api/ProductApi~productAndSkuIdsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProductAndSkuIds200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Product and SKU IDs
     * Retrieves the IDs of products and SKUs.   > 📘 Onboarding guide   >  > Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Number} [categoryId] ID of the category from which you need to retrieve Products and SKUs.
     * @param {Number} [from] Insert the ID that will start the request result.
     * @param {Number} [to] Insert the ID that will end the request result.
     * @param {module:api/ProductApi~productAndSkuIdsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProductAndSkuIds200Response}
     */
    productAndSkuIds(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling productAndSkuIds");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling productAndSkuIds");
      }

      let pathParams = {
      };
      let queryParams = {
        'categoryId': opts['categoryId'],
        '_from': opts['from'],
        '_to': opts['to']
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
      let returnType = ProductAndSkuIds200Response;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/products/GetProductAndSkuIds', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productVariations operation.
     * @callback module:api/ProductApi~productVariationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProductVariations200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Product's SKUs by Product ID
     * Retrieves data about the product and all SKUs related to it by the product's ID.  ## Response body example    ```json  {      \"productId\": 9,      \"name\": \"Camisa Masculina\",      \"salesChannel\": \"2\",      \"available\": true,      \"displayMode\": \"lista\",      \"dimensions\": [          \"Cores\",          \"Tamanho\",          \"País de origem\",          \"Gênero\"      ],      \"dimensionsInputType\": {          \"Cores\": \"Combo\",          \"Tamanho\": \"Combo\",          \"País de origem\": \"Combo\",          \"Gênero\": \"Combo\"      },      \"dimensionsMap\": {          \"Cores\": [              \"Amarelo\",              \"Azul\",              \"Vermelho\"          ],          \"Tamanho\": [              \"P\",              \"M\",              \"G\"          ],          \"País de origem\": [              \"Brasil\"          ],          \"Gênero\": [              \"Masculino\"          ]      },      \"skus\": [          {              \"sku\": 310118454,              \"skuname\": \"Amarela - G\",              \"dimensions\": {                  \"Cores\": \"Amarelo\",                  \"Tamanho\": \"G\",                  \"País de origem\": \"Brasil\",                  \"Gênero\": \"Masculino\"              },              \"available\": false,              \"availablequantity\": 0,              \"cacheVersionUsedToCallCheckout\": null,              \"listPriceFormated\": \"R$ 0,00\",              \"listPrice\": 0,              \"taxFormated\": \"R$ 0,00\",              \"taxAsInt\": 0,              \"bestPriceFormated\": \"R$ 9.999.876,00\",              \"bestPrice\": 999987600,              \"spotPrice\": 999987600,              \"installments\": 0,              \"installmentsValue\": 0,              \"installmentsInsterestRate\": null,              \"image\": \"https://lojadobreno.vteximg.com.br/arquivos/ids/155467-292-292/image-5d7ad76ad1954c53adecab4138319034.jpg?v=637321899584500000\",              \"sellerId\": \"1\",              \"seller\": \"lojadobreno\",              \"measures\": {                  \"cubicweight\": 1.0000,                  \"height\": 5.0000,                  \"length\": 20.0000,                  \"weight\": 200.0000,                  \"width\": 20.0000              },              \"unitMultiplier\": 1.0000,              \"rewardValue\": 0          },          {              \"sku\": 310118455,              \"skuname\": \"Vermelha - M\",              \"dimensions\": {                  \"Cores\": \"Vermelho\",                  \"Tamanho\": \"M\",                  \"País de origem\": \"Brasil\",                  \"Gênero\": \"Masculino\"              },              \"available\": true,              \"availablequantity\": 99999,              \"cacheVersionUsedToCallCheckout\": \"38395F1AEF59DF5CEAEDE472328145CD_\",              \"listPriceFormated\": \"R$ 0,00\",              \"listPrice\": 0,              \"taxFormated\": \"R$ 0,00\",              \"taxAsInt\": 0,              \"bestPriceFormated\": \"R$ 20,00\",              \"bestPrice\": 2000,              \"spotPrice\": 2000,              \"installments\": 1,              \"installmentsValue\": 2000,              \"installmentsInsterestRate\": 0,              \"image\": \"https://lojadobreno.vteximg.com.br/arquivos/ids/155468-292-292/image-601a6099aace48b89d26fc9f22e8e611.jpg?v=637321906602470000\",              \"sellerId\": \"pedrostore\",              \"seller\": \"pedrostore\",              \"measures\": {                  \"cubicweight\": 0.4167,                  \"height\": 5.0000,                  \"length\": 20.0000,                  \"weight\": 200.0000,                  \"width\": 20.0000              },              \"unitMultiplier\": 1.0000,              \"rewardValue\": 0          }      ]  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} productId Product’s unique numerical identifier.
     * @param {module:api/ProductApi~productVariationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProductVariations200Response}
     */
    productVariations(contentType, accept, productId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling productVariations");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling productVariations");
      }
      // verify the required parameter 'productId' is set
      if (productId === undefined || productId === null) {
        throw new Error("Missing the required parameter 'productId' when calling productVariations");
      }

      let pathParams = {
        'productId': productId
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
      let returnType = ProductVariations200Response;
      return this.apiClient.callApi(
        '/api/catalog_system/pub/products/variations/{productId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productandTradePolicy operation.
     * @callback module:api/ProductApi~productandTradePolicyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProductandTradePolicy200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Product and its general context
     * Retrieves a specific product's general information as name, description and the trade policies that it is included.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} productId Product’s unique numerical identifier.
     * @param {module:api/ProductApi~productandTradePolicyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProductandTradePolicy200Response}
     */
    productandTradePolicy(contentType, accept, productId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling productandTradePolicy");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling productandTradePolicy");
      }
      // verify the required parameter 'productId' is set
      if (productId === undefined || productId === null) {
        throw new Error("Missing the required parameter 'productId' when calling productandTradePolicy");
      }

      let pathParams = {
        'productId': productId
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
      let returnType = ProductandTradePolicy200Response;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/products/productget/{productId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the productbyRefId operation.
     * @callback module:api/ProductApi~productbyRefIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProductbyRefId200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Product by RefId
     * Retrieves a specific product by its Reference ID.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} refId Product Referecial Code
     * @param {module:api/ProductApi~productbyRefIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProductbyRefId200Response}
     */
    productbyRefId(contentType, accept, refId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling productbyRefId");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling productbyRefId");
      }
      // verify the required parameter 'refId' is set
      if (refId === undefined || refId === null) {
        throw new Error("Missing the required parameter 'refId' when calling productbyRefId");
      }

      let pathParams = {
        'refId': refId
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
      let returnType = ProductbyRefId200Response;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/products/productgetbyrefid/{refId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reviewRateProduct operation.
     * @callback module:api/ProductApi~reviewRateProductCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Product Review Rate by Product ID
     * Retrieves the review rate of a product by this product's ID.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} productId Product’s unique numerical identifier.
     * @param {module:api/ProductApi~reviewRateProductCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    reviewRateProduct(contentType, accept, productId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling reviewRateProduct");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling reviewRateProduct");
      }
      // verify the required parameter 'productId' is set
      if (productId === undefined || productId === null) {
        throw new Error("Missing the required parameter 'productId' when calling reviewRateProduct");
      }

      let pathParams = {
        'productId': productId
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
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/api/addon/pvt/review/GetProductRate/{productId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
