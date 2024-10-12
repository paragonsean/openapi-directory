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
import ApiCatalogPvtSkuservicetypeattachmentPost200Response from '../model/ApiCatalogPvtSkuservicetypeattachmentPost200Response';
import RequestBody5 from '../model/RequestBody5';

/**
* SKUServiceAttachment service.
* @module api/SKUServiceAttachmentApi
* @version 1.0
*/
export default class SKUServiceAttachmentApi {

    /**
    * Constructs a new SKUServiceAttachmentApi. 
    * @alias module:api/SKUServiceAttachmentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtSkuservicetypeattachmentDelete operation.
     * @callback module:api/SKUServiceAttachmentApi~apiCatalogPvtSkuservicetypeattachmentDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Dissociate Attachment by Attachment ID or SKU Service Type ID
     * Dissociates an Attachment by its Attachment ID or SKU Service Type ID from an SKU Service Type.
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {Number} [attachmentId] SKU Service Attachment unique identifier.
     * @param {Number} [skuServiceTypeId] SKU Service Type unique identifier.
     * @param {module:api/SKUServiceAttachmentApi~apiCatalogPvtSkuservicetypeattachmentDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtSkuservicetypeattachmentDelete(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSkuservicetypeattachmentDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSkuservicetypeattachmentDelete");
      }

      let pathParams = {
      };
      let queryParams = {
        'attachmentId': opts['attachmentId'],
        'skuServiceTypeId': opts['skuServiceTypeId']
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
        '/api/catalog/pvt/skuservicetypeattachment', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSkuservicetypeattachmentPost operation.
     * @callback module:api/SKUServiceAttachmentApi~apiCatalogPvtSkuservicetypeattachmentPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtSkuservicetypeattachmentPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Associate SKU Service Attachment
     * Associates an Attachment for an existing SKU Service Type.   ## Request body example    ```json  {      \"AttachmentId\": 1,      \"SkuServiceTypeId\": 1  }  ```    ## Response body example    ```json  {      \"Id\": 1,      \"AttachmentId\": 1,      \"SkuServiceTypeId\": 1  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/RequestBody5} [requestBody5] 
     * @param {module:api/SKUServiceAttachmentApi~apiCatalogPvtSkuservicetypeattachmentPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtSkuservicetypeattachmentPost200Response}
     */
    apiCatalogPvtSkuservicetypeattachmentPost(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['requestBody5'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSkuservicetypeattachmentPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSkuservicetypeattachmentPost");
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
      let returnType = ApiCatalogPvtSkuservicetypeattachmentPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/skuservicetypeattachment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete operation.
     * @callback module:api/SKUServiceAttachmentApi~apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Dissociate Attachment from SKU Service Type
     * Dissociates an Attachment from an SKU Service Type
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} skuServiceTypeAttachmentId SKU Service Attachment unique identifier.
     * @param {module:api/SKUServiceAttachmentApi~apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete(contentType, accept, skuServiceTypeAttachmentId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete");
      }
      // verify the required parameter 'skuServiceTypeAttachmentId' is set
      if (skuServiceTypeAttachmentId === undefined || skuServiceTypeAttachmentId === null) {
        throw new Error("Missing the required parameter 'skuServiceTypeAttachmentId' when calling apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete");
      }

      let pathParams = {
        'skuServiceTypeAttachmentId': skuServiceTypeAttachmentId
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
        '/api/catalog/pvt/skuservicetypeattachment/{skuServiceTypeAttachmentId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
