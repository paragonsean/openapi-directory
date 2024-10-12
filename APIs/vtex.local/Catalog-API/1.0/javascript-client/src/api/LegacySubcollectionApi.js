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
import ApiCatalogPvtCollectionCollectionIdPositionPostRequest from '../model/ApiCatalogPvtCollectionCollectionIdPositionPostRequest';
import ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner from '../model/ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner';
import ApiCatalogPvtSubcollectionPost200Response from '../model/ApiCatalogPvtSubcollectionPost200Response';
import ApiCatalogPvtSubcollectionPostRequest from '../model/ApiCatalogPvtSubcollectionPostRequest';
import ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response from '../model/ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response';
import ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response from '../model/ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response';
import ApiCatalogPvtSubcollectionSubCollectionIdPutRequest from '../model/ApiCatalogPvtSubcollectionSubCollectionIdPutRequest';
import ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response from '../model/ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response';
import RequestBody10 from '../model/RequestBody10';
import RequestBody11 from '../model/RequestBody11';
import RequestBody12 from '../model/RequestBody12';

/**
* LegacySubcollection service.
* @module api/LegacySubcollectionApi
* @version 1.0
*/
export default class LegacySubcollectionApi {

    /**
    * Constructs a new LegacySubcollectionApi. 
    * @alias module:api/LegacySubcollectionApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtCollectionCollectionIdPositionPost operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtCollectionCollectionIdPositionPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reposition SKU on the Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    ```json  {       \"skuId\": 1,       \"position\": 1,       \"subCollectionId\": 17  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} collectionId Collection’s unique numerical identifier.
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtCollectionCollectionIdPositionPostRequest} [apiCatalogPvtCollectionCollectionIdPositionPostRequest] 
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtCollectionCollectionIdPositionPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtCollectionCollectionIdPositionPost(contentType, accept, collectionId, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtCollectionCollectionIdPositionPostRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtCollectionCollectionIdPositionPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtCollectionCollectionIdPositionPost");
      }
      // verify the required parameter 'collectionId' is set
      if (collectionId === undefined || collectionId === null) {
        throw new Error("Missing the required parameter 'collectionId' when calling apiCatalogPvtCollectionCollectionIdPositionPost");
      }

      let pathParams = {
        'collectionId': collectionId
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/collection/{collectionId}/position', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtCollectionCollectionIdSubcollectionGet operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtCollectionCollectionIdSubcollectionGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Subcollection by Collection ID
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    ```json  [      {          \"Id\": 12,          \"CollectionId\": 149,          \"Name\": \"Subcollection\",          \"Type\": \"Inclusive\",          \"PreSale\": false,          \"Release\": true      },      {          \"Id\": 13,          \"CollectionId\": 149,          \"Name\": \"Test\",          \"Type\": \"Exclusive\",          \"PreSale\": true,          \"Release\": false      },      {          \"Id\": 14,          \"CollectionId\": 149,          \"Name\": \"asdfghj\",          \"Type\": \"Inclusive\",          \"PreSale\": false,          \"Release\": false      }  ]  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} collectionId Collection’s unique numerical identifier.
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtCollectionCollectionIdSubcollectionGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner>}
     */
    apiCatalogPvtCollectionCollectionIdSubcollectionGet(contentType, accept, collectionId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtCollectionCollectionIdSubcollectionGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtCollectionCollectionIdSubcollectionGet");
      }
      // verify the required parameter 'collectionId' is set
      if (collectionId === undefined || collectionId === null) {
        throw new Error("Missing the required parameter 'collectionId' when calling apiCatalogPvtCollectionCollectionIdSubcollectionGet");
      }

      let pathParams = {
        'collectionId': collectionId
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
      let returnType = [ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner];
      return this.apiClient.callApi(
        '/api/catalog/pvt/collection/{collectionId}/subcollection', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionPost operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtSubcollectionPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    ```json  {      \"CollectionId\": 149,      \"Name\": \"Test\",      \"Type\": \"Exclusive\",      \"PreSale\": true,      \"Release\": false  }  ```  ## Response body example    ```json  {      \"Id\": 13,      \"CollectionId\": 149,      \"Name\": \"Test\",      \"Type\": \"Exclusive\",      \"PreSale\": true,      \"Release\": false  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtSubcollectionPostRequest} [apiCatalogPvtSubcollectionPostRequest] 
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtSubcollectionPost200Response}
     */
    apiCatalogPvtSubcollectionPost(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtSubcollectionPostRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionPost");
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
      let returnType = ApiCatalogPvtSubcollectionPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/subcollection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Brand from Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {Number} brandId Brand’s unique numerical identifier.
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(contentType, accept, subCollectionId, brandId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete");
      }
      // verify the required parameter 'brandId' is set
      if (brandId === undefined || brandId === null) {
        throw new Error("Missing the required parameter 'brandId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete");
      }

      let pathParams = {
        'subCollectionId': subCollectionId,
        'brandId': brandId
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
        '/api/catalog/pvt/subcollection/{subCollectionId}/brand/{brandId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Category from Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {Number} categoryId Category’s unique numerical identifier.
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(contentType, accept, subCollectionId, categoryId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete");
      }
      // verify the required parameter 'categoryId' is set
      if (categoryId === undefined || categoryId === null) {
        throw new Error("Missing the required parameter 'categoryId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete");
      }

      let pathParams = {
        'subCollectionId': subCollectionId,
        'categoryId': categoryId
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
        '/api/catalog/pvt/subcollection/{subCollectionId}/brand/{categoryId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdBrandPost operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdBrandPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Associate Brand to Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    ```json  {      \"BrandId\": 2000000  }  ```    ## Response body example    ```json  {      \"SubCollectionId\": 17,      \"BrandId\": 2000000  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {Object} opts Optional parameters
     * @param {module:model/RequestBody10} [requestBody10] 
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdBrandPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response}
     */
    apiCatalogPvtSubcollectionSubCollectionIdBrandPost(contentType, accept, subCollectionId, opts, callback) {
      opts = opts || {};
      let postBody = opts['requestBody10'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandPost");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdBrandPost");
      }

      let pathParams = {
        'subCollectionId': subCollectionId
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
      let returnType = ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/subcollection/{subCollectionId}/brand', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdCategoryPost operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdCategoryPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Associate Category to Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    ```json  {      \"CategoryId\": 1  }  ```    ## Response body example    ```json  {      \"SubCollectionId\": 17,      \"CategoryId\": 1  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {Object} opts Optional parameters
     * @param {module:model/RequestBody11} [requestBody11] 
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdCategoryPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response}
     */
    apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(contentType, accept, subCollectionId, opts, callback) {
      opts = opts || {};
      let postBody = opts['requestBody11'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdCategoryPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdCategoryPost");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdCategoryPost");
      }

      let pathParams = {
        'subCollectionId': subCollectionId
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
      let returnType = ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/subcollection/{subCollectionId}/category', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdDelete operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtSubcollectionSubCollectionIdDelete(contentType, accept, subCollectionId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdDelete");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdDelete");
      }

      let pathParams = {
        'subCollectionId': subCollectionId
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
        '/api/catalog/pvt/subcollection/{subCollectionId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdGet operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtSubcollectionPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    ```json  {      \"Id\": 13,      \"CollectionId\": 149,      \"Name\": \"Test\",      \"Type\": \"Exclusive\",      \"PreSale\": true,      \"Release\": false  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtSubcollectionPost200Response}
     */
    apiCatalogPvtSubcollectionSubCollectionIdGet(contentType, accept, subCollectionId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdGet");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdGet");
      }

      let pathParams = {
        'subCollectionId': subCollectionId
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
      let returnType = ApiCatalogPvtSubcollectionPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/subcollection/{subCollectionId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdPut operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtSubcollectionPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    ```json  {      \"CollectionId\": 149,      \"Name\": \"Test\",      \"Type\": \"Exclusive\",      \"PreSale\": true,      \"Release\": false  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtSubcollectionSubCollectionIdPutRequest} [apiCatalogPvtSubcollectionSubCollectionIdPutRequest] 
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtSubcollectionPost200Response}
     */
    apiCatalogPvtSubcollectionSubCollectionIdPut(contentType, accept, subCollectionId, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtSubcollectionSubCollectionIdPutRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdPut");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdPut");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdPut");
      }

      let pathParams = {
        'subCollectionId': subCollectionId
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
      let returnType = ApiCatalogPvtSubcollectionPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/subcollection/{subCollectionId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add SKU to Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    ```json  {      \"SkuId\": 1  }  ```    ## Response body example    ```json  {      \"SubCollectionId\": 17,      \"SkuId\": 1  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {Object} opts Optional parameters
     * @param {module:model/RequestBody12} [requestBody12] 
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response}
     */
    apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(contentType, accept, subCollectionId, opts, callback) {
      opts = opts || {};
      let postBody = opts['requestBody12'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost");
      }

      let pathParams = {
        'subCollectionId': subCollectionId
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
      let returnType = ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete operation.
     * @callback module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete SKU from Subcollection
     *  >⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} subCollectionId Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
     * @param {Number} skuId SKU’s unique numerical identifier.
     * @param {module:api/LegacySubcollectionApi~apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(contentType, accept, subCollectionId, skuId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete");
      }
      // verify the required parameter 'subCollectionId' is set
      if (subCollectionId === undefined || subCollectionId === null) {
        throw new Error("Missing the required parameter 'subCollectionId' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete");
      }
      // verify the required parameter 'skuId' is set
      if (skuId === undefined || skuId === null) {
        throw new Error("Missing the required parameter 'skuId' when calling apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete");
      }

      let pathParams = {
        'subCollectionId': subCollectionId,
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
        '/api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit/{skuId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
