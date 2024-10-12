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
import GetSKUcomplementsbytype200Response from '../model/GetSKUcomplementsbytype200Response';
import RequestBody2 from '../model/RequestBody2';
import SkuComplementInner from '../model/SkuComplementInner';

/**
* SKUComplement service.
* @module api/SKUComplementApi
* @version 1.0
*/
export default class SKUComplementApi {

    /**
    * Constructs a new SKUComplementApi. 
    * @alias module:api/SKUComplementApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createSKUComplement operation.
     * @callback module:api/SKUComplementApi~createSKUComplementCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SkuComplementInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create SKU Complement
     * Creates a new SKU Complement on a Parent SKU.     ## Request body example    ```json  {      \"SkuId\": 2,      \"ParentSkuId\": 1,      \"ComplementTypeId\": 2  }  ```     ## Response body example    ```json  {      \"Id\": 62,      \"SkuId\": 2,      \"ParentSkuId\": 1,      \"ComplementTypeId\": 2  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/RequestBody2} [requestBody2] 
     * @param {module:api/SKUComplementApi~createSKUComplementCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SkuComplementInner>}
     */
    createSKUComplement(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['requestBody2'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling createSKUComplement");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling createSKUComplement");
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
      let returnType = [SkuComplementInner];
      return this.apiClient.callApi(
        '/api/catalog/pvt/skucomplement', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteSKUComplementbySKUComplementID operation.
     * @callback module:api/SKUComplementApi~deleteSKUComplementbySKUComplementIDCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete SKU Complement by SKU Complement ID
     * Deletes a previously existing SKU Complement by SKU Complement ID.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuComplementId SKU Complement’s unique numerical identifier.
     * @param {module:api/SKUComplementApi~deleteSKUComplementbySKUComplementIDCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteSKUComplementbySKUComplementID(contentType, accept, skuComplementId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling deleteSKUComplementbySKUComplementID");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling deleteSKUComplementbySKUComplementID");
      }
      // verify the required parameter 'skuComplementId' is set
      if (skuComplementId === undefined || skuComplementId === null) {
        throw new Error("Missing the required parameter 'skuComplementId' when calling deleteSKUComplementbySKUComplementID");
      }

      let pathParams = {
        'skuComplementId': skuComplementId
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
        '/api/catalog/pvt/skucomplement/{skuComplementId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSKUComplementbySKUComplementID operation.
     * @callback module:api/SKUComplementApi~getSKUComplementbySKUComplementIDCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SkuComplementInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU Complement by SKU Complement ID
     * Retrieves an existing SKU Complement by its SKU Complement ID.      ## Response body example    ```json  {      \"Id\": 62,      \"SkuId\": 2,      \"ParentSkuId\": 1,      \"ComplementTypeId\": 2  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuComplementId SKU Complement’s unique numerical identifier.
     * @param {module:api/SKUComplementApi~getSKUComplementbySKUComplementIDCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SkuComplementInner>}
     */
    getSKUComplementbySKUComplementID(contentType, accept, skuComplementId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getSKUComplementbySKUComplementID");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getSKUComplementbySKUComplementID");
      }
      // verify the required parameter 'skuComplementId' is set
      if (skuComplementId === undefined || skuComplementId === null) {
        throw new Error("Missing the required parameter 'skuComplementId' when calling getSKUComplementbySKUComplementID");
      }

      let pathParams = {
        'skuComplementId': skuComplementId
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
      let returnType = [SkuComplementInner];
      return this.apiClient.callApi(
        '/api/catalog/pvt/skucomplement/{skuComplementId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSKUComplementbySKUID operation.
     * @callback module:api/SKUComplementApi~getSKUComplementbySKUIDCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SkuComplementInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU Complement by SKU ID
     * Retrieves an existing SKU Complement by its SKU ID.     ## Response body example    ```json  [      {          \"Id\": 61,          \"SkuId\": 7,          \"ParentSkuId\": 1,          \"ComplementTypeId\": 1      }  ]  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU’s unique numerical identifier.
     * @param {module:api/SKUComplementApi~getSKUComplementbySKUIDCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SkuComplementInner>}
     */
    getSKUComplementbySKUID(contentType, accept, skuId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getSKUComplementbySKUID");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getSKUComplementbySKUID");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling getSKUComplementbySKUID");
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
      let returnType = [SkuComplementInner];
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}/complement', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSKUComplementsbyComplementTypeID operation.
     * @callback module:api/SKUComplementApi~getSKUComplementsbyComplementTypeIDCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SkuComplementInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU Complements by Complement Type ID
     * Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU.     ## Response body example    ```json  [      {          \"Id\": 61,          \"SkuId\": 7,          \"ParentSkuId\": 1,          \"ComplementTypeId\": 1      }  ]  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId ID of the SKU which will be inserted as a Complement in the Parent SKU.
     * @param {Number} complementTypeId Complement Type ID. This represents the type of the complement. The possible values are: `1` for Accessory; `2` for Suggestion; `3` for Similar Product; `5` for Show Together.
     * @param {module:api/SKUComplementApi~getSKUComplementsbyComplementTypeIDCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SkuComplementInner>}
     */
    getSKUComplementsbyComplementTypeID(contentType, accept, skuId, complementTypeId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getSKUComplementsbyComplementTypeID");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getSKUComplementsbyComplementTypeID");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling getSKUComplementsbyComplementTypeID");
      }
      // verify the required parameter 'complementTypeId' is set
      if (complementTypeId === undefined || complementTypeId === null) {
        throw new Error("Missing the required parameter 'complementTypeId' when calling getSKUComplementsbyComplementTypeID");
      }

      let pathParams = {
        'skuId': skuId,
        'complementTypeId': complementTypeId
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
      let returnType = [SkuComplementInner];
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}/complement/{complementTypeId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSKUcomplementsbytype operation.
     * @callback module:api/SKUComplementApi~getSKUcomplementsbytypeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetSKUcomplementsbytype200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU complements by type
     * Retrieves all the existing SKU complements with the same complement type ID of a specific SKU.      ## Response body example    ```json  {      \"ParentSkuId\": 1,      \"ComplementSkuIds\": [          7      ],      \"Type\": \"1\"  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} parentSkuId ID of the Parent SKU, where the Complement is inserted.
     * @param {Number} type Complement Type ID. This represents the type of the complement. The possible values are: `1` for Accessory; `2` for Suggestion; `3` for Similar Product; `5` for Show Together.
     * @param {module:api/SKUComplementApi~getSKUcomplementsbytypeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetSKUcomplementsbytype200Response}
     */
    getSKUcomplementsbytype(contentType, accept, parentSkuId, type, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling getSKUcomplementsbytype");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling getSKUcomplementsbytype");
      }
      // verify the required parameter 'parentSkuId' is set
      if (parentSkuId === undefined || parentSkuId === null) {
        throw new Error("Missing the required parameter 'parentSkuId' when calling getSKUcomplementsbytype");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling getSKUcomplementsbytype");
      }

      let pathParams = {
        'parentSkuId': parentSkuId,
        'type': type
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
      let returnType = GetSKUcomplementsbytype200Response;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/sku/complements/{parentSkuId}/{type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
