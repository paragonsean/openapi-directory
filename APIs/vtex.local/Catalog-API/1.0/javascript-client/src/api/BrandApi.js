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
import BrandCreateUpdate from '../model/BrandCreateUpdate';
import BrandGet from '../model/BrandGet';
import BrandListPerPage200Response from '../model/BrandListPerPage200Response';

/**
* Brand service.
* @module api/BrandApi
* @version 1.0
*/
export default class BrandApi {

    /**
    * Constructs a new BrandApi. 
    * @alias module:api/BrandApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtBrandBrandIdDelete operation.
     * @callback module:api/BrandApi~apiCatalogPvtBrandBrandIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Brand
     * Deletes an existing Brand.
     * @param {String} brandId Brand’s unique numerical identifier.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/BrandApi~apiCatalogPvtBrandBrandIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtBrandBrandIdDelete(brandId, contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'brandId' is set
      if (brandId === undefined || brandId === null) {
        throw new Error("Missing the required parameter 'brandId' when calling apiCatalogPvtBrandBrandIdDelete");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandBrandIdDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtBrandBrandIdDelete");
      }

      let pathParams = {
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
        '/api/catalog/pvt/brand/{brandId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtBrandBrandIdGet operation.
     * @callback module:api/BrandApi~apiCatalogPvtBrandBrandIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandCreateUpdate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Brand and context
     * Retrieves information about a specific Brand and its context.  ## Response body example    ```json  {    \"Id\": 2000013,    \"Name\": \"Orma Carbon\",    \"Text\": \"Orma Carbon\",    \"Keywords\": \"orma\",    \"SiteTitle\": \"Orma Carbon\",    \"Active\": true,    \"MenuHome\": true,    \"AdWordsRemarketingCode\": \"\",    \"LomadeeCampaignCode\": \"\",    \"Score\": null,    \"LinkId\": \"orma-carbon\"  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} brandId Brand ID.
     * @param {module:api/BrandApi~apiCatalogPvtBrandBrandIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandCreateUpdate}
     */
    apiCatalogPvtBrandBrandIdGet(contentType, accept, brandId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandBrandIdGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtBrandBrandIdGet");
      }
      // verify the required parameter 'brandId' is set
      if (brandId === undefined || brandId === null) {
        throw new Error("Missing the required parameter 'brandId' when calling apiCatalogPvtBrandBrandIdGet");
      }

      let pathParams = {
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
      let accepts = ['application/json'];
      let returnType = BrandCreateUpdate;
      return this.apiClient.callApi(
        '/api/catalog/pvt/brand/{brandId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtBrandBrandIdPut operation.
     * @callback module:api/BrandApi~apiCatalogPvtBrandBrandIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandCreateUpdate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Brand
     * Updates a previously existing Brand.  ## Request and response body example    ```json  {    \"Id\": 2000013,    \"Name\": \"Orma Carbon\",    \"Text\": \"Orma Carbon\",    \"Keywords\": \"orma\",    \"SiteTitle\": \"Orma Carbon\",    \"Active\": true,    \"MenuHome\": true,    \"AdWordsRemarketingCode\": \"\",    \"LomadeeCampaignCode\": \"\",    \"Score\": null,    \"LinkId\": \"orma-carbon\"  }  ```
     * @param {String} brandId Brand’s unique numerical identifier.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/BrandCreateUpdate} [brandCreateUpdate] 
     * @param {module:api/BrandApi~apiCatalogPvtBrandBrandIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandCreateUpdate}
     */
    apiCatalogPvtBrandBrandIdPut(brandId, contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['brandCreateUpdate'];
      // verify the required parameter 'brandId' is set
      if (brandId === undefined || brandId === null) {
        throw new Error("Missing the required parameter 'brandId' when calling apiCatalogPvtBrandBrandIdPut");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandBrandIdPut");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtBrandBrandIdPut");
      }

      let pathParams = {
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = BrandCreateUpdate;
      return this.apiClient.callApi(
        '/api/catalog/pvt/brand/{brandId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtBrandPost operation.
     * @callback module:api/BrandApi~apiCatalogPvtBrandPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandCreateUpdate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create Brand
     * Creates a new Brand.  ## Request and response body example    ```json  {    \"Id\": 2000013,    \"Name\": \"Orma Carbon\",    \"Text\": \"Orma Carbon\",    \"Keywords\": \"orma\",    \"SiteTitle\": \"Orma Carbon\",    \"Active\": true,    \"MenuHome\": true,    \"AdWordsRemarketingCode\": \"\",    \"LomadeeCampaignCode\": \"\",    \"Score\": null,    \"LinkId\": \"orma-carbon\"  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/BrandCreateUpdate} [brandCreateUpdate] Request body.
     * @param {module:api/BrandApi~apiCatalogPvtBrandPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandCreateUpdate}
     */
    apiCatalogPvtBrandPost(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['brandCreateUpdate'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtBrandPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtBrandPost");
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
      let returnType = BrandCreateUpdate;
      return this.apiClient.callApi(
        '/api/catalog/pvt/brand', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the brand operation.
     * @callback module:api/BrandApi~brandCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandGet} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Brand
     * Retrieves a specific Brand by its ID.  ## Response body example    ```json  {    \"id\": 7000000,    \"name\": \"Pedigree\",    \"isActive\": true,    \"title\": \"Pedigree\",    \"metaTagDescription\": \"Pedigree\",    \"imageUrl\": null  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} brandId Brand ID.
     * @param {module:api/BrandApi~brandCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandGet}
     */
    brand(contentType, accept, brandId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling brand");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling brand");
      }
      // verify the required parameter 'brandId' is set
      if (brandId === undefined || brandId === null) {
        throw new Error("Missing the required parameter 'brandId' when calling brand");
      }

      let pathParams = {
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
      let accepts = ['application/json'];
      let returnType = BrandGet;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/brand/{brandId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the brandList operation.
     * @callback module:api/BrandApi~brandListCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/BrandGet>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Brand List
     * Retrieves all Brands registered in the store's Catalog.   >⚠️ This route's response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    ```json  [    {      \"id\": 9280,      \"name\": \"Brand\",      \"isActive\": true,      \"title\": \"Brand\",      \"metaTagDescription\": \"Brand\",      \"imageUrl\": null    },    {      \"id\": 2000000,      \"name\": \"Orma Carbon\",      \"isActive\": true,      \"title\": \"Orma Carbon\",      \"metaTagDescription\": \"Orma Carbon\",      \"imageUrl\": null    },    {      \"id\": 2000001,      \"name\": \"Pedigree\",      \"isActive\": true,      \"title\": \"Pedigree\",      \"metaTagDescription\": \"\",      \"imageUrl\": null    }  ]  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/BrandApi~brandListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/BrandGet>}
     */
    brandList(contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling brandList");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling brandList");
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
      let accepts = ['application/json'];
      let returnType = [BrandGet];
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/brand/list', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the brandListPerPage operation.
     * @callback module:api/BrandApi~brandListPerPageCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BrandListPerPage200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Brand List Per Page
     * Retrieves all Brands registered in the store's Catalog by page number.  ## Response body example    ```json  {    \"items\": [      {        \"id\": 2000000,        \"name\": \"Farm\",        \"isActive\": true,        \"title\": \"Farm\",        \"metaTagDescription\": \"Farm\",        \"imageUrl\": null      },      {        \"id\": 2000001,        \"name\": \"Adidas\",        \"isActive\": true,        \"title\": \"\",        \"metaTagDescription\": \"\",        \"imageUrl\": null      },      {        \"id\": 2000002,        \"name\": \"Brastemp\",        \"isActive\": true,        \"title\": \"Brastemp\",        \"metaTagDescription\": \"Brastemp\",        \"imageUrl\": null      }    ],      \"paging\": {        \"page\": 1,          \"perPage\": 3,            \"total\": 6,              \"pages\": 2      }  }  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} pageSize Quantity of brands per page.
     * @param {Number} page Page number of the brand list.
     * @param {module:api/BrandApi~brandListPerPageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BrandListPerPage200Response}
     */
    brandListPerPage(contentType, accept, pageSize, page, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling brandListPerPage");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling brandListPerPage");
      }
      // verify the required parameter 'pageSize' is set
      if (pageSize === undefined || pageSize === null) {
        throw new Error("Missing the required parameter 'pageSize' when calling brandListPerPage");
      }
      // verify the required parameter 'page' is set
      if (page === undefined || page === null) {
        throw new Error("Missing the required parameter 'page' when calling brandListPerPage");
      }

      let pathParams = {
      };
      let queryParams = {
        'pageSize': pageSize,
        'page': page
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
      let returnType = BrandListPerPage200Response;
      return this.apiClient.callApi(
        '/api/catalog_system/pvt/brand/pagedlist', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
