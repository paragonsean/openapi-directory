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
import ApiCatalogPvtStockkeepingunitGet200Response from '../model/ApiCatalogPvtStockkeepingunitGet200Response';
import ApiCatalogPvtStockkeepingunitPost200Response from '../model/ApiCatalogPvtStockkeepingunitPost200Response';
import ApiCatalogPvtStockkeepingunitPostRequest from '../model/ApiCatalogPvtStockkeepingunitPostRequest';
import ApiCatalogPvtStockkeepingunitSkuIdPut200Response from '../model/ApiCatalogPvtStockkeepingunitSkuIdPut200Response';
import ApiCatalogPvtStockkeepingunitSkuIdPutRequest from '../model/ApiCatalogPvtStockkeepingunitSkuIdPutRequest';
import GetSKUAltID from '../model/GetSKUAltID';
import GetSKUandContext from '../model/GetSKUandContext';
import Sku200Response from '../model/Sku200Response';
import SkulistbyProductId from '../model/SkulistbyProductId';

/**
* SKU service.
* @module api/SKUApi
* @version 1.0
*/
export default class SKUApi {

    /**
    * Constructs a new SKUApi. 
    * @alias module:api/SKUApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtStockkeepingunitGet operation.
     * @callback module:api/SKUApi~apiCatalogPvtStockkeepingunitGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtStockkeepingunitGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU by RefId
     * Retrieves information about a specific SKU by its `RefId`.     ### Response body example    ```json  {      \"Id\": 1,      \"ProductId\": 1,      \"IsActive\": true,      \"Name\": \"Royal Canin Feline Urinary 500g\",      \"RefId\": \"0001\",      \"PackagedHeight\": 6.0000,      \"PackagedLength\": 24.0000,      \"PackagedWidth\": 14.0000,      \"PackagedWeightKg\": 550.0000,      \"Height\": null,      \"Length\": null,      \"Width\": null,      \"WeightKg\": null,      \"CubicWeight\": 1.0000,      \"IsKit\": false,      \"CreationDate\": \"2020-03-12T15:42:00\",      \"RewardValue\": null,      \"EstimatedDateArrival\": null,      \"ManufacturerCode\": \"\",      \"CommercialConditionId\": 1,      \"MeasurementUnit\": \"un\",      \"UnitMultiplier\": 1.0000,      \"ModalType\": null,      \"KitItensSellApart\": false,      \"Videos\": null  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} refId SKU Reference ID.
     * @param {module:api/SKUApi~apiCatalogPvtStockkeepingunitGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtStockkeepingunitGet200Response}
     */
    apiCatalogPvtStockkeepingunitGet(contentType, accept, refId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitGet");
      }
      // verify the required parameter 'refId' is set
      if (refId === undefined || refId === null) {
        throw new Error("Missing the required parameter 'refId' when calling apiCatalogPvtStockkeepingunitGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'refId': refId
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
      let returnType = ApiCatalogPvtStockkeepingunitGet200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtStockkeepingunitPost operation.
     * @callback module:api/SKUApi~apiCatalogPvtStockkeepingunitPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtStockkeepingunitPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create SKU
     *     Creates a new SKU.    If there is a need to create a new SKU with a specific custom ID, specify the `Id` (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ### Request body example (custom ID)    ```json  {     \"Id\": 1,      \"ProductId\": 310117069,     \"IsActive\": true,     \"ActivateIfPossible\": true,     \"Name\": \"sku test\",     \"RefId\": \"125478\",     \"Ean\": \"8949461894984\",     \"PackagedHeight\": 10,     \"PackagedLength\": 10,     \"PackagedWidth\": 10,     \"PackagedWeightKg\": 10,     \"Height\": null,     \"Length\": null,     \"Width\": null,     \"WeightKg\": null,     \"CubicWeight\": 0.1667,     \"IsKit\": false,     \"CreationDate\": null,     \"RewardValue\": null,     \"EstimatedDateArrival\": null,     \"ManufacturerCode\": \"123\",     \"CommercialConditionId\": 1,     \"MeasurementUnit\": \"un\",     \"UnitMultiplier\": 2.0000,     \"ModalType\": null,     \"KitItensSellApart\": false,     \"Videos\": [ \"https://www.youtube.com/\" ]  }  ```     ### Request body example (automatically generated ID)    ```json  {     \"ProductId\": 310117069,     \"IsActive\": true,     \"ActivateIfPossible\": true,     \"Name\": \"sku test\",     \"RefId\": \"125478\",     \"Ean\": \"8949461894984\",     \"PackagedHeight\": 10,     \"PackagedLength\": 10,     \"PackagedWidth\": 10,     \"PackagedWeightKg\": 10,     \"Height\": null,     \"Length\": null,     \"Width\": null,     \"WeightKg\": null,     \"CubicWeight\": 0.1667,     \"IsKit\": false,     \"CreationDate\": null,     \"RewardValue\": null,     \"EstimatedDateArrival\": null,     \"ManufacturerCode\": \"123\",     \"CommercialConditionId\": 1,     \"MeasurementUnit\": \"un\",     \"UnitMultiplier\": 2.0000,     \"ModalType\": null,     \"KitItensSellApart\": false,     \"Videos\": [ \"https://www.youtube.com/\" ]  }  ```     ### Response body example    ```json  {     \"Id\":1,     \"ProductId\": 310117069,     \"IsActive\": true,     \"ActivateIfPossible\": true,     \"Name\": \"sku test\",     \"RefId\": \"125478\",     \"Ean\": \"8949461894984\",     \"PackagedHeight\": 10,     \"PackagedLength\": 10,     \"PackagedWidth\": 10,     \"PackagedWeightKg\": 10,     \"Height\": null,     \"Length\": null,     \"Width\": null,     \"WeightKg\": null,     \"CubicWeight\": 0.1667,     \"IsKit\": false,     \"CreationDate\": null,     \"RewardValue\": null,     \"EstimatedDateArrival\": null,     \"ManufacturerCode\": \"123\",     \"CommercialConditionId\": 1,     \"MeasurementUnit\": \"un\",     \"UnitMultiplier\": 2.0000,     \"ModalType\": null,     \"KitItensSellApart\": false,     \"Videos\": [ \"https://www.youtube.com/\" ]  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtStockkeepingunitPostRequest} [apiCatalogPvtStockkeepingunitPostRequest] 
     * @param {module:api/SKUApi~apiCatalogPvtStockkeepingunitPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtStockkeepingunitPost200Response}
     */
    apiCatalogPvtStockkeepingunitPost(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtStockkeepingunitPostRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitPost");
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
      let returnType = ApiCatalogPvtStockkeepingunitPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtStockkeepingunitSkuIdPut operation.
     * @callback module:api/SKUApi~apiCatalogPvtStockkeepingunitSkuIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtStockkeepingunitSkuIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update SKU
     * Updates an existing SKU.     ### Request body example    ```json  {     \"Id\": 310118448,     \"ProductId\": 310117069,     \"IsActive\": true,     \"ActivateIfPossible\": true,     \"Name\": \"sku test\",     \"RefId\": \"125478\",     \"PackagedHeight\": 10,     \"PackagedLength\": 10,     \"PackagedWidth\": 10,     \"PackagedWeightKg\": 10,     \"Height\": null,     \"Length\": null,     \"Width\": null,     \"WeightKg\": null,     \"CubicWeight\": 0.1667,     \"IsKit\": false,     \"CreationDate\": null,     \"RewardValue\": null,     \"EstimatedDateArrival\": null,     \"ManufacturerCode\": \"123\",     \"CommercialConditionId\": 1,     \"MeasurementUnit\": \"un\",     \"UnitMultiplier\": 2.0000,     \"ModalType\": null,     \"KitItensSellApart\": false,     \"Videos\": [ \"https://www.youtube.com/\" ]  }  ```    ### Response body example    ```json  {      \"Id\": 310118449,      \"ProductId\": 1,      \"IsActive\": true,      \"ActivateIfPossible\": true,      \"Name\": \"sku test\",      \"RefId\": \"1254789\",      \"PackagedHeight\": 10.0,      \"PackagedLength\": 10.0,      \"PackagedWidth\": 10.0,      \"PackagedWeightKg\": 10.0,      \"Height\": null,      \"Length\": null,      \"Width\": null,      \"WeightKg\": null,      \"CubicWeight\": 0.1667,      \"IsKit\": false,      \"CreationDate\": \"2020-04-22T12:12:47.5219561\",      \"RewardValue\": null,      \"EstimatedDateArrival\": null,      \"ManufacturerCode\": \"123\",      \"CommercialConditionId\": 1,      \"MeasurementUnit\": \"un\",      \"UnitMultiplier\": 2.0000,      \"ModalType\": null,      \"KitItensSellApart\": false,      \"Videos\": [ \"https://www.youtube.com/\" ]  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU’s unique numerical identifier.
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtStockkeepingunitSkuIdPutRequest} [apiCatalogPvtStockkeepingunitSkuIdPutRequest] 
     * @param {module:api/SKUApi~apiCatalogPvtStockkeepingunitSkuIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtStockkeepingunitSkuIdPut200Response}
     */
    apiCatalogPvtStockkeepingunitSkuIdPut(contentType, accept, skuId, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtStockkeepingunitSkuIdPutRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtStockkeepingunitSkuIdPut");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtStockkeepingunitSkuIdPut");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling apiCatalogPvtStockkeepingunitSkuIdPut");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ApiCatalogPvtStockkeepingunitSkuIdPut200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listallSKUIDs operation.
     * @callback module:api/SKUApi~listallSKUIDsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<Number>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all SKU IDs
     * Retrieves the IDs of all SKUs in your store. Presents the results with page size and pagination.  > 📘 Onboarding guide   >  > Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.    ### Response body example    ```json  [    1,    2,    3,    4,    5,    6,    7,    8,    9,    10  ]  ```
     * @param {Number} page Number of the page from where you need to retrieve SKU IDs.
     * @param {Number} pagesize Size of the page from where you need retrieve SKU IDs. The maximum value is `1000`.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/SKUApi~listallSKUIDsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Number>}
     */
    listallSKUIDs(page, pagesize, contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'page' is set
      if (page === undefined || page === null) {
        throw new Error("Missing the required parameter 'page' when calling listallSKUIDs");
      }
      // verify the required parameter 'pagesize' is set
      if (pagesize === undefined || pagesize === null) {
        throw new Error("Missing the required parameter 'pagesize' when calling listallSKUIDs");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling listallSKUIDs");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling listallSKUIDs");
      }

      let pathParams = {
      };
      let queryParams = {
        'page': page,
        'pagesize': pagesize
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
      let returnType = ['Number'];
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/sku/stockkeepingunitids', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sku operation.
     * @callback module:api/SKUApi~skuCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Sku200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU
     * Retrieves a specific SKU by its ID.    ### Response body example    ```json  {      \"Id\": 1,      \"ProductId\": 1,      \"IsActive\": true,      \"ActivateIfPossible\": true,      \"Name\": \"Ração Royal Canin Feline Urinary 500g\",      \"RefId\": \"0001\",      \"PackagedHeight\": 6.5000,      \"PackagedLength\": 24.0000,      \"PackagedWidth\": 14.0000,      \"PackagedWeightKg\": 550.0000,      \"Height\": 2.2000,      \"Length\": 4.4000,      \"Width\": 3.3000,      \"WeightKg\": 1.1000,      \"CubicWeight\": 0.4550,      \"IsKit\": false,      \"CreationDate\": \"2021-06-08T15:25:00\",      \"RewardValue\": null,      \"EstimatedDateArrival\": null,      \"ManufacturerCode\": \"\",      \"CommercialConditionId\": 1,      \"MeasurementUnit\": \"un\",      \"UnitMultiplier\": 300.0000,      \"ModalType\": null,      \"KitItensSellApart\": false,      \"Videos\": [          \"www.google.com\"      ]  }  ```    > 📘 Onboarding guide   >  > Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU unique identifier number.
     * @param {module:api/SKUApi~skuCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Sku200Response}
     */
    sku(contentType, accept, skuId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling sku");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling sku");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling sku");
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
      let returnType = Sku200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/stockkeepingunit/{skuId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the skuContext operation.
     * @callback module:api/SKUApi~skuContextCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetSKUandContext} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU and context
     * Retrieves context of an SKU.  > 📘 Onboarding guide   >  > Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.     ## Response body example    ```json  {      \"Id\": 2001773,      \"ProductId\": 2001426,      \"NameComplete\": \"Tabela de Basquete\",      \"ComplementName\": \"\",      \"ProductName\": \"Tabela de Basquete\",      \"ProductDescription\": \"Tabela de Basquete\",      \"SkuName\": \"Tabela de Basquete\",      \"ProductRefId\": \"0987\",      \"TaxCode\": \"\",      \"IsActive\": true,      \"IsTransported\": true,      \"IsInventoried\": true,      \"IsGiftCardRecharge\": false,      \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\",      \"DetailUrl\": \"/tabela-de-basquete/p\",      \"CSCIdentification\": null,      \"BrandId\": \"2000018\",      \"BrandName\": \"MARCA ARGOLO TESTE\",      \"IsBrandActive\": true,      \"Dimension\": {          \"cubicweight\": 81.6833,          \"height\": 65,          \"length\": 58,          \"weight\": 10000,          \"width\": 130      },      \"RealDimension\": {          \"realCubicWeight\": 274.1375,          \"realHeight\": 241,          \"realLength\": 65,          \"realWeight\": 9800,          \"realWidth\": 105      },      \"ManufacturerCode\": \"\",      \"IsKit\": false,      \"KitItems\": [],      \"Services\": [],      \"Categories\": [],      \"CategoriesFullPath\": [          \"/1/10/\",          \"/1/\",          \"/20/\"      ],      \"Attachments\": [          {              \"Id\": 3,              \"Name\": \"Mensagem\",              \"Keys\": [                  \"nome;20\",                  \"foto;40\"              ],              \"Fields\": [                  {                      \"FieldName\": \"nome\",                      \"MaxCaracters\": \"20\",                      \"DomainValues\": \"Adalberto,Pedro,João\"                  },                  {                      \"FieldName\": \"foto\",                      \"MaxCaracters\": \"40\",                      \"DomainValues\": null                  }              ],              \"IsActive\": true,              \"IsRequired\": false          }      ],      \"Collections\": [],      \"SkuSellers\": [          {              \"SellerId\": \"1\",              \"StockKeepingUnitId\": 2001773,              \"SellerStockKeepingUnitId\": \"2001773\",              \"IsActive\": true,              \"FreightCommissionPercentage\": 0,              \"ProductCommissionPercentage\": 0          }      ],      \"SalesChannels\": [          1,          2,          3,          10      ],      \"Images\": [          {              \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\",              \"ImageName\": \"\",              \"FileId\": 168952          },          {              \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\",              \"ImageName\": \"\",              \"FileId\": 168953          },          {              \"ImageUrl\": \"http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\",              \"ImageName\": \"\",              \"FileId\": 168954          }      ],      \"Videos\": [          \"www.google.com\"      ],      \"SkuSpecifications\": [          {              \"FieldId\": 102,              \"FieldName\": \"Cor\",              \"FieldValueIds\": [                  266              ],              \"FieldValues\": [                  \"Padrão\"              ],              \"IsFilter\": false,              \"FieldGroupId\": 11,              \"FieldGroupName\": \"Especificações\"          }      ],      \"ProductSpecifications\": [          {              \"FieldId\": 7,              \"FieldName\": \"Faixa Etária\",              \"FieldValueIds\": [                  58,                  56,                  55,                  52              ],              \"FieldValues\": [                  \"5 a 6 anos\",                  \"7 a 8 anos\",                  \"9 a 10 anos\",                  \"Acima de 10 anos\"              ],              \"IsFilter\": true,              \"FieldGroupId\": 17,              \"FieldGroupName\": \"NewGroupName 2\"          },          {              \"FieldId\": 23,              \"FieldName\": \"Fabricante\",              \"FieldValueIds\": [],              \"FieldValues\": [                  \"Xalingo\"              ],              \"IsFilter\": false,              \"FieldGroupId\": 17,              \"FieldGroupName\": \"NewGroupName 2\"          }      ],      \"ProductClustersIds\": \"176,187,192,194,211,217,235,242\",      \"PositionsInClusters\": {          \"151\": 3,          \"152\": 0,          \"158\": 1      },      \"ProductClusterNames\": {          \"151\": \"asdfghj\",          \"152\": \"George\",          \"158\": \"Coleção halloween\"      },      \"ProductClusterHighlights\": {          \"151\": \"asdfghj\",          \"152\": \"George\"      },      \"ProductCategoryIds\": \"/59/\",      \"IsDirectCategoryActive\": false,      \"ProductGlobalCategoryId\": null,      \"ProductCategories\": {          \"59\": \"Brinquedos\"      },      \"CommercialConditionId\": 1,      \"RewardValue\": 100.0,      \"AlternateIds\": {          \"Ean\": \"8781\",          \"RefId\": \"878181\"      },      \"AlternateIdValues\": [          \"8781\",          \"878181\"      ],      \"EstimatedDateArrival\": \"\",      \"MeasurementUnit\": \"un\",      \"UnitMultiplier\": 2.0000,      \"InformationSource\": \"Indexer\",      \"ModalType\": \"\",      \"KeyWords\": \"basquete, tabela\",      \"ReleaseDate\": \"2020-01-06T00:00:00\",      \"ProductIsVisible\": true,      \"ShowIfNotAvailable\": true,      \"IsProductActive\": true,      \"ProductFinalScore\": 0  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuId SKU's unique identifier number.
     * @param {Object} opts Optional parameters
     * @param {Number} [sc] Trade Policy's unique identifier number.
     * @param {module:api/SKUApi~skuContextCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetSKUandContext}
     */
    skuContext(contentType, accept, skuId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling skuContext");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling skuContext");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling skuContext");
      }

      let pathParams = {
        'skuId': skuId
      };
      let queryParams = {
        'sc': opts['sc']
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
      let returnType = GetSKUandContext;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/sku/stockkeepingunitbyid/{skuId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the skuIdbyRefId operation.
     * @callback module:api/SKUApi~skuIdbyRefIdCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU ID by Reference ID
     * Retrieves an SKU ID by the SKU's Reference ID.     ### Response body example    ```json  \"310118450\"  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} refId SKU Reference ID.
     * @param {module:api/SKUApi~skuIdbyRefIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    skuIdbyRefId(contentType, accept, refId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling skuIdbyRefId");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling skuIdbyRefId");
      }
      // verify the required parameter 'refId' is set
      if (refId === undefined || refId === null) {
        throw new Error("Missing the required parameter 'refId' when calling skuIdbyRefId");
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
      let returnType = 'String';
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/{refId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the skuIdlistbyRefIdlist operation.
     * @callback module:api/SKUApi~skuIdlistbyRefIdlistCallback
     * @param {String} error Error message, if any.
     * @param {Object.<String, {String: String}>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve SKU ID list by Reference ID list
     * Receives a list of Reference IDs and returns a list with the corresponding SKU IDs.    >⚠️ The list of Reference IDs in the request body cannot have repeated Reference IDs, or the API will return an error 500.     ## Request body example    ```json  [      \"123\",      \"D25133K-B2\",      \"14-556\",      \"DCF880L2-BR\"  ]  ```    ### Response body example    ```json  {      \"123\": \"435\",      \"D25133K-B2\": \"4351\",      \"14-556\": \"3155\",      \"DCF880L2-BR\": \"4500\"  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [requestBody] 
     * @param {module:api/SKUApi~skuIdlistbyRefIdlistCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object.<String, {String: String}>}
     */
    skuIdlistbyRefIdlist(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['requestBody'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling skuIdlistbyRefIdlist");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling skuIdlistbyRefIdlist");
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
      let returnType = {'String': 'String'};
      return this.apiClient.callApi(
        '/api/catalog_system/pub/sku/stockkeepingunitidsbyrefids', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the skubyAlternateId operation.
     * @callback module:api/SKUApi~skubyAlternateIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetSKUAltID} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU by Alternate ID
     * Retrieves an SKU by its Alternate ID.    ### Response body example    ```json  {      \"Id\": 310118450,      \"ProductId\": 2,      \"NameComplete\": \"Caixa de Areia Azul Petmate sku test\",      \"ComplementName\": \"\",      \"ProductName\": \"Caixa de Areia Azul Petmate\",      \"ProductDescription\": \"\",      \"ProductRefId\": \"\",      \"TaxCode\": \"\",      \"SkuName\": \"sku test\",      \"IsActive\": true,      \"IsTransported\": true,      \"IsInventoried\": true,      \"IsGiftCardRecharge\": false,      \"ImageUrl\": \"https://lojadobreno.vteximg.com.br/arquivos/ids/155451-55-55/caixa-areia-azul-petmate.jpg?v=637139451191670000\",      \"DetailUrl\": \"/caixa-de-areia-azul-petmate/p\",      \"CSCIdentification\": null,      \"BrandId\": \"2000005\",      \"BrandName\": \"Petmate\",      \"IsBrandActive\": true,      \"Dimension\": {          \"cubicweight\": 0.2083,          \"height\": 10.0000,          \"length\": 10.0000,          \"weight\": 10.0000,          \"width\": 10.0000      },      \"RealDimension\": {          \"realCubicWeight\": 0.000,          \"realHeight\": 0.0,          \"realLength\": 0.0,          \"realWeight\": 0.0,          \"realWidth\": 0.0      },      \"ManufacturerCode\": \"123\",      \"IsKit\": false,      \"KitItems\": [],      \"Services\": [],      \"Categories\": [],      \"CategoriesFullPath\": [          \"/3/15/\",          \"/3/\",          \"/1/\"      ],      \"Attachments\": [],      \"Collections\": [],      \"SkuSellers\": [          {              \"SellerId\": \"1\",              \"StockKeepingUnitId\": 310118450,              \"SellerStockKeepingUnitId\": \"310118450\",              \"IsActive\": true,              \"FreightCommissionPercentage\": 0.0,              \"ProductCommissionPercentage\": 0.0          }      ],      \"SalesChannels\": [          1,          3      ],      \"Images\": [          {              \"ImageUrl\": \"https://lojadobreno.vteximg.com.br/arquivos/ids/155451/caixa-areia-azul-petmate.jpg?v=637139451191670000\",              \"ImageName\": null,              \"FileId\": 155451          }      ],      \"Videos\": [],      \"SkuSpecifications\": [],      \"ProductSpecifications\": [],      \"ProductClustersIds\": \"151,158\",      \"PositionsInClusters\": {          \"151\": 1,          \"158\": 2      },      \"ProductClusterNames\": {          \"151\": \"asdfghj\",          \"158\": \"Coleção halloween\"      },      \"ProductClusterHighlights\": {          \"151\": \"asdfghj\"      },      \"ProductCategoryIds\": \"/3/15/\",      \"IsDirectCategoryActive\": true,      \"ProductGlobalCategoryId\": 5000,      \"ProductCategories\": {          \"15\": \"Caixa de Areia\",          \"3\": \"Higiene\",          \"1\": \"Alimentação\"      },      \"CommercialConditionId\": 1,      \"RewardValue\": 0.0,      \"AlternateIds\": {          \"RefId\": \"1\"      },      \"AlternateIdValues\": [          \"1\"      ],      \"EstimatedDateArrival\": null,      \"MeasurementUnit\": \"un\",      \"UnitMultiplier\": 1.0000,      \"InformationSource\": null,      \"ModalType\": null,      \"KeyWords\": \"\",      \"ReleaseDate\": \"2020-01-06T00:00:00Z\",      \"ProductIsVisible\": true,      \"ShowIfNotAvailable\": true,      \"IsProductActive\": true,      \"ProductFinalScore\": 0  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} alternateId Product EAN or RefId.
     * @param {module:api/SKUApi~skubyAlternateIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetSKUAltID}
     */
    skubyAlternateId(contentType, accept, alternateId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling skubyAlternateId");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling skubyAlternateId");
      }
      // verify the required parameter 'alternateId' is set
      if (alternateId === undefined || alternateId === null) {
        throw new Error("Missing the required parameter 'alternateId' when calling skubyAlternateId");
      }

      let pathParams = {
        'alternateId': alternateId
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
        '/api/catalog_system/pvt/sku/stockkeepingunitbyalternateId/{alternateId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the skulistbyProductId operation.
     * @callback module:api/SKUApi~skulistbyProductIdCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SkulistbyProductId>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get SKU list by Product ID
     * Retrieves a list with the SKUs related to a product by the product's ID.    ### Response body example    ```json  [      {          \"IsPersisted\": true,          \"IsRemoved\": false,          \"Id\": 2000035,          \"ProductId\": 2000024,          \"IsActive\": true,          \"Name\": \"33 - Preto\",          \"Height\": 8,          \"RealHeight\": null,          \"Width\": 15,          \"RealWidth\": null,          \"Length\": 8,          \"RealLength\": null,          \"WeightKg\": 340,          \"RealWeightKg\": null,          \"ModalId\": 1,          \"RefId\": \"\",          \"CubicWeight\": 0.2,          \"IsKit\": false,          \"IsDynamicKit\": null,          \"InternalNote\": null,          \"DateUpdated\": \"2015-11-06T19:10:00\",          \"RewardValue\": 0.01,          \"CommercialConditionId\": 1,          \"EstimatedDateArrival\": \"\",          \"FlagKitItensSellApart\": false,          \"ManufacturerCode\": \"\",          \"ReferenceStockKeepingUnitId\": null,          \"Position\": 0,          \"EditionSkuId\": null,          \"ApprovedAdminId\": 123,          \"EditionAdminId\": 123,          \"ActivateIfPossible\": true,          \"SupplierCode\": null,          \"MeasurementUnit\": \"un\",          \"UnitMultiplier\": 2.0000,          \"IsInventoried\": null,          \"IsTransported\": null,          \"IsGiftCardRecharge\": null,          \"ModalType\": \"\"      }  ]  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} productId Product’s unique numerical identifier.
     * @param {module:api/SKUApi~skulistbyProductIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SkulistbyProductId>}
     */
    skulistbyProductId(contentType, accept, productId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling skulistbyProductId");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling skulistbyProductId");
      }
      // verify the required parameter 'productId' is set
      if (productId === undefined || productId === null) {
        throw new Error("Missing the required parameter 'productId' when calling skulistbyProductId");
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
      let returnType = [SkulistbyProductId];
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/sku/stockkeepingunitByProductId/{productId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
