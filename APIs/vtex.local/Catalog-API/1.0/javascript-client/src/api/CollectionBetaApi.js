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
import RequestBody from '../model/RequestBody';

/**
* CollectionBeta service.
* @module api/CollectionBetaApi
* @version 1.0
*/
export default class CollectionBetaApi {

    /**
    * Constructs a new CollectionBetaApi. 
    * @alias module:api/CollectionBetaApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the gETAllCollections operation.
     * @callback module:api/CollectionBetaApi~gETAllCollectionsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get All Collections
     * Retrieves a list of all collections matching a filter.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} page Page number.
     * @param {Number} pageSize Number of the items of the page.
     * @param {Boolean} orderByAsc Defines if the items of the page are in ascending order.
     * @param {module:api/CollectionBetaApi~gETAllCollectionsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    gETAllCollections(contentType, accept, page, pageSize, orderByAsc, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling gETAllCollections");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling gETAllCollections");
      }
      // verify the required parameter 'page' is set
      if (page === undefined || page === null) {
        throw new Error("Missing the required parameter 'page' when calling gETAllCollections");
      }
      // verify the required parameter 'pageSize' is set
      if (pageSize === undefined || pageSize === null) {
        throw new Error("Missing the required parameter 'pageSize' when calling gETAllCollections");
      }
      // verify the required parameter 'orderByAsc' is set
      if (orderByAsc === undefined || orderByAsc === null) {
        throw new Error("Missing the required parameter 'orderByAsc' when calling gETAllCollections");
      }

      let pathParams = {
      };
      let queryParams = {
        'page': page,
        'pageSize': pageSize,
        'orderByAsc': orderByAsc
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
        '/api/catalog_system/pvt/collection/search', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the gETAllInactiveCollections operation.
     * @callback module:api/CollectionBetaApi~gETAllInactiveCollectionsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get All Inactive Collections
     * Retrieves a list of Collection IDs of the inactive Collections.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/CollectionBetaApi~gETAllInactiveCollectionsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    gETAllInactiveCollections(contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling gETAllInactiveCollections");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling gETAllInactiveCollections");
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
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/collection/inactive', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the gETCollectionsbyseachterms operation.
     * @callback module:api/CollectionBetaApi~gETCollectionsbyseachtermsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Collections by search terms
     * Retrieves a list of collections matching a filter.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} searchTerms String that will search for a collection related to it.
     * @param {Object} opts Optional parameters
     * @param {Number} [page] Page number.
     * @param {Number} [pageSize] Number of the items of the page.
     * @param {Boolean} [orderByAsc] Defines if the items of the page are in ascending order.
     * @param {module:api/CollectionBetaApi~gETCollectionsbyseachtermsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    gETCollectionsbyseachterms(contentType, accept, searchTerms, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling gETCollectionsbyseachterms");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling gETCollectionsbyseachterms");
      }
      // verify the required parameter 'searchTerms' is set
      if (searchTerms === undefined || searchTerms === null) {
        throw new Error("Missing the required parameter 'searchTerms' when calling gETCollectionsbyseachterms");
      }

      let pathParams = {
        'searchTerms': searchTerms
      };
      let queryParams = {
        'page': opts['page'],
        'pageSize': opts['pageSize'],
        'orderByAsc': opts['orderByAsc']
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
        '/api/catalog_system/pvt/collection/search/{searchTerms}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the gETImportfileexample operation.
     * @callback module:api/CollectionBetaApi~gETImportfileexampleCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Import Collection file example
     * Imports a sample of the imported XLS file. You need to save the response file to your device.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/CollectionBetaApi~gETImportfileexampleCallback} callback The callback function, accepting three arguments: error, data, response
     */
    gETImportfileexample(contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling gETImportfileexample");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling gETImportfileexample");
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
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/collection/stockkeepingunit/importfileexample', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the gETProductsfromacollection operation.
     * @callback module:api/CollectionBetaApi~gETProductsfromacollectionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get products from a collection
     * Retrieves information about the products from a collection.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} collectionId Collection's unique identifier.
     * @param {Object} opts Optional parameters
     * @param {Number} [page] Page number.
     * @param {Number} [pageSize] Number of the items of the page.
     * @param {String} [filter] Filter used to refine the Collection's products.
     * @param {Boolean} [active] Defines if the status of the product is active or not.
     * @param {Boolean} [visible] Defines if the product is visible on the store or not.
     * @param {Number} [categoryId] Product's Category unique identifier.
     * @param {Number} [brandId] Product's Brand unique identifier.
     * @param {Number} [supplierId] Product's Supplier unique identifier.
     * @param {Number} [salesChannelId] Product's Trade Policy unique identifier.
     * @param {String} [releaseFrom] Product past release date.
     * @param {String} [releaseTo] Product future release date.
     * @param {String} [specificationProduct] Product Specification Field Value. You must also fill in `SpecificationFieldId` to use this parameter.
     * @param {Number} [specificationFieldId] Product Specification Field unique identifier.
     * @param {module:api/CollectionBetaApi~gETProductsfromacollectionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    gETProductsfromacollection(contentType, accept, collectionId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling gETProductsfromacollection");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling gETProductsfromacollection");
      }
      // verify the required parameter 'collectionId' is set
      if (collectionId === undefined || collectionId === null) {
        throw new Error("Missing the required parameter 'collectionId' when calling gETProductsfromacollection");
      }

      let pathParams = {
        'collectionId': collectionId
      };
      let queryParams = {
        'page': opts['page'],
        'pageSize': opts['pageSize'],
        'Filter': opts['filter'],
        'Active': opts['active'],
        'Visible': opts['visible'],
        'CategoryId': opts['categoryId'],
        'BrandId': opts['brandId'],
        'SupplierId': opts['supplierId'],
        'SalesChannelId': opts['salesChannelId'],
        'ReleaseFrom': opts['releaseFrom'],
        'ReleaseTo': opts['releaseTo'],
        'SpecificationProduct': opts['specificationProduct'],
        'SpecificationFieldId': opts['specificationFieldId']
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
        '/api/catalog/pvt/collection/{collectionId}/products', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the pOSTAddproductsbyimportfile operation.
     * @callback module:api/CollectionBetaApi~pOSTAddproductsbyimportfileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add products to Collection by imported file
     * Adds products to a collection from the request body file. The file must be an imported template.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} collectionId Collection's unique identifier.
     * @param {Object} opts Optional parameters
     * @param {Object} [file] XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
     * @param {module:api/CollectionBetaApi~pOSTAddproductsbyimportfileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    pOSTAddproductsbyimportfile(contentType, accept, collectionId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling pOSTAddproductsbyimportfile");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling pOSTAddproductsbyimportfile");
      }
      // verify the required parameter 'collectionId' is set
      if (collectionId === undefined || collectionId === null) {
        throw new Error("Missing the required parameter 'collectionId' when calling pOSTAddproductsbyimportfile");
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
        'file': opts['file']
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = ['multipart/form-data'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importinsert', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the pOSTCreateCollection operation.
     * @callback module:api/CollectionBetaApi~pOSTCreateCollectionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create Collection
     * Creates a new collection.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:model/RequestBody} requestBody 
     * @param {module:api/CollectionBetaApi~pOSTCreateCollectionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    pOSTCreateCollection(contentType, accept, requestBody, callback) {
      let postBody = requestBody;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling pOSTCreateCollection");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling pOSTCreateCollection");
      }
      // verify the required parameter 'requestBody' is set
      if (requestBody === undefined || requestBody === null) {
        throw new Error("Missing the required parameter 'requestBody' when calling pOSTCreateCollection");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/collection/', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the pOSTRemoveproductsbyimportfile operation.
     * @callback module:api/CollectionBetaApi~pOSTRemoveproductsbyimportfileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove products from Collection by imported file
     * Removes products from a collection from the request body file. The file must be an imported template.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} collectionId Collection's unique identifier.
     * @param {Object} opts Optional parameters
     * @param {Object} [file] XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
     * @param {module:api/CollectionBetaApi~pOSTRemoveproductsbyimportfileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    pOSTRemoveproductsbyimportfile(contentType, accept, collectionId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling pOSTRemoveproductsbyimportfile");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling pOSTRemoveproductsbyimportfile");
      }
      // verify the required parameter 'collectionId' is set
      if (collectionId === undefined || collectionId === null) {
        throw new Error("Missing the required parameter 'collectionId' when calling pOSTRemoveproductsbyimportfile");
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
        'file': opts['file']
      };

      let authNames = ['appToken', 'appKey'];
      let contentTypes = ['multipart/form-data'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importexclude', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
