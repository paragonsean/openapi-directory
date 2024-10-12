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
import ApiCatalogPvtCategoryCategoryIdPutRequest from '../model/ApiCatalogPvtCategoryCategoryIdPutRequest';
import Category from '../model/Category';
import CreateCategoryRequest from '../model/CreateCategoryRequest';
import GetCategoryTree from '../model/GetCategoryTree';

/**
* Category service.
* @module api/CategoryApi
* @version 1.0
*/
export default class CategoryApi {

    /**
    * Constructs a new CategoryApi. 
    * @alias module:api/CategoryApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtCategoryCategoryIdGet operation.
     * @callback module:api/CategoryApi~apiCatalogPvtCategoryCategoryIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Category} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Category by ID
     * Retrieves general information about a Category.   ## Response body example    ```json  {      \"Id\": 1,      \"Name\": \"Home Appliances\",      \"FatherCategoryId\": null,      \"Title\": \"Home Appliances\",      \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",      \"Keywords\": \"Kitchen, Laundry, Appliances\",      \"IsActive\": true,      \"LomadeeCampaignCode\": \"\",      \"AdWordsRemarketingCode\": \"\",      \"ShowInStoreFront\": true,      \"ShowBrandFilter\": true,      \"ActiveStoreFrontLink\": true,      \"GlobalCategoryId\": 3367,      \"StockKeepingUnitSelectionMode\": \"LIST\",      \"Score\": null,      \"LinkId\": \"Alimentacao\",      \"HasChildren\": true  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} categoryId Category’s unique numerical identifier.
     * @param {module:api/CategoryApi~apiCatalogPvtCategoryCategoryIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Category}
     */
    apiCatalogPvtCategoryCategoryIdGet(contentType, accept, categoryId, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtCategoryCategoryIdGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtCategoryCategoryIdGet");
      }
      // verify the required parameter 'categoryId' is set
      if (categoryId === undefined || categoryId === null) {
        throw new Error("Missing the required parameter 'categoryId' when calling apiCatalogPvtCategoryCategoryIdGet");
      }

      let pathParams = {
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
      let accepts = ['application/json'];
      let returnType = Category;
      return this.apiClient.callApi(
        '/api/catalog/pvt/category/{categoryId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtCategoryCategoryIdPut operation.
     * @callback module:api/CategoryApi~apiCatalogPvtCategoryCategoryIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Category} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Category
     * Updates a previously existing Category.    ## Request body example    ```json  {      \"Name\": \"Home Appliances\",      \"FatherCategoryId\": null,      \"Title\": \"Home Appliances\",      \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",      \"Keywords\": \"Kitchen, Laundry, Appliances\",      \"IsActive\": true,      \"LomadeeCampaignCode\": null,      \"AdWordsRemarketingCode\": null,      \"ShowInStoreFront\": true,      \"ShowBrandFilter\": true,      \"ActiveStoreFrontLink\": true,      \"GlobalCategoryId\": 604,      \"StockKeepingUnitSelectionMode\": \"SPECIFICATION\",      \"Score\": null  }  ```    ## Response body example    ```json  {      \"Id\": 1,      \"Name\": \"Home Appliances\",      \"FatherCategoryId\": null,      \"Title\": \"Home Appliances\",      \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",      \"Keywords\": \"Kitchen, Laundry, Appliances\",      \"IsActive\": true,      \"LomadeeCampaignCode\": \"\",      \"AdWordsRemarketingCode\": \"\",      \"ShowInStoreFront\": true,      \"ShowBrandFilter\": true,      \"ActiveStoreFrontLink\": true,      \"GlobalCategoryId\": 604,      \"StockKeepingUnitSelectionMode\": \"LIST\",      \"Score\": null,      \"LinkId\": \"Alimentacao\",      \"HasChildren\": true  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Number} categoryId Category’s unique numerical identifier.
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiCatalogPvtCategoryCategoryIdPutRequest} [apiCatalogPvtCategoryCategoryIdPutRequest] 
     * @param {module:api/CategoryApi~apiCatalogPvtCategoryCategoryIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Category}
     */
    apiCatalogPvtCategoryCategoryIdPut(contentType, accept, categoryId, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiCatalogPvtCategoryCategoryIdPutRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtCategoryCategoryIdPut");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtCategoryCategoryIdPut");
      }
      // verify the required parameter 'categoryId' is set
      if (categoryId === undefined || categoryId === null) {
        throw new Error("Missing the required parameter 'categoryId' when calling apiCatalogPvtCategoryCategoryIdPut");
      }

      let pathParams = {
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Category;
      return this.apiClient.callApi(
        '/api/catalog/pvt/category/{categoryId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtCategoryPost operation.
     * @callback module:api/CategoryApi~apiCatalogPvtCategoryPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Category} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create Category
     * Creates a new Category.    If there is a need to create a new category with a specific custom ID, specify the `Id` (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ## Request body example (automatically generated ID)    ```json  {      \"Name\": \"Home Appliances\",      \"FatherCategoryId\": null,      \"Title\": \"Home Appliances\",      \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",      \"Keywords\": \"Kitchen, Laundry, Appliances\",      \"IsActive\": true,      \"LomadeeCampaignCode\": null,      \"AdWordsRemarketingCode\": null,      \"ShowInStoreFront\": true,      \"ShowBrandFilter\": true,      \"ActiveStoreFrontLink\": true,      \"GlobalCategoryId\": 604,      \"StockKeepingUnitSelectionMode\": \"SPECIFICATION\",      \"Score\": null  }  ```    ## Request body example (custom ID)    ```json  {      \"Id\": 1,      \"Name\": \"Home Appliances\",      \"FatherCategoryId\": null,      \"Title\": \"Home Appliances\",      \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",      \"Keywords\": \"Kitchen, Laundry, Appliances\",      \"IsActive\": true,      \"LomadeeCampaignCode\": null,      \"AdWordsRemarketingCode\": null,      \"ShowInStoreFront\": true,      \"ShowBrandFilter\": true,      \"ActiveStoreFrontLink\": true,      \"GlobalCategoryId\": 604,      \"StockKeepingUnitSelectionMode\": \"SPECIFICATION\",      \"Score\": null  }  ```    ## Response body example    ```json  {      \"Id\": 1,      \"Name\": \"Home Appliances\",      \"FatherCategoryId\": null,      \"Title\": \"Home Appliances\",      \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",      \"Keywords\": \"Kitchen, Laundry, Appliances\",      \"IsActive\": true,      \"LomadeeCampaignCode\": \"\",      \"AdWordsRemarketingCode\": \"\",      \"ShowInStoreFront\": true,      \"ShowBrandFilter\": true,      \"ActiveStoreFrontLink\": true,      \"GlobalCategoryId\": 604,      \"StockKeepingUnitSelectionMode\": \"LIST\",      \"Score\": null,      \"LinkId\": \"Alimentacao\",      \"HasChildren\": true  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateCategoryRequest} [createCategoryRequest] 
     * @param {module:api/CategoryApi~apiCatalogPvtCategoryPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Category}
     */
    apiCatalogPvtCategoryPost(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['createCategoryRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtCategoryPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtCategoryPost");
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
      let returnType = Category;
      return this.apiClient.callApi(
        '/api/catalog/pvt/category', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the categoryTree operation.
     * @callback module:api/CategoryApi~categoryTreeCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetCategoryTree>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Category Tree
     * Retrieves the Category Tree of your store. Get all the category levels registered in the Catalog or define the level up to which you want to get.    > 📘 Onboarding guide   >  > Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.   ## Response body example    ```json  [      {          \"id\": 1,          \"name\": \"Alimentação\",          \"hasChildren\": true,          \"url\": \"https://lojadobreno.vtexcommercestable.com.br/alimentacao\",          \"children\": [              {                  \"id\": 6,                  \"name\": \"Bebedouro\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/alimentacao/bebedouro\",                  \"children\": [],                  \"Title\": \"Bebedouro para Gatos\",                  \"MetaTagDescription\": \"\"              },              {                  \"id\": 7,                  \"name\": \"Comedouro\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/alimentacao/comedouro\",                  \"children\": [],                  \"Title\": \"Comedouro para Gatos\",                  \"MetaTagDescription\": \"\"              },              {                  \"id\": 8,                  \"name\": \"Biscoitos\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/alimentacao/biscoitos\",                  \"children\": [],                  \"Title\": \"Biscoitos para Gatos\",                  \"MetaTagDescription\": \"\"              },              {                  \"id\": 9,                  \"name\": \"Petiscos\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/alimentacao/petiscos\",                  \"children\": [],                  \"Title\": \"Petiscos para Gatos\",                  \"MetaTagDescription\": \"\"              },              {                  \"id\": 10,                  \"name\": \"Ração Seca\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-seca\",                  \"children\": [],                  \"Title\": \"Ração Seca para Gatos\",                  \"MetaTagDescription\": \"\"              },              {                  \"id\": 11,                  \"name\": \"Ração Úmida\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-umida\",                  \"children\": [],                  \"Title\": \"Ração Úmida para Gatos\",                  \"MetaTagDescription\": \"\"              }          ],          \"Title\": \"Alimentação para Gatos\",          \"MetaTagDescription\": \"\"      },      {          \"id\": 2,          \"name\": \"Brinquedos\",          \"hasChildren\": true,          \"url\": \"https://lojadobreno.vtexcommercestable.com.br/brinquedos\",          \"children\": [              {                  \"id\": 12,                  \"name\": \"Bolinhas\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/brinquedos/bolinhas\",                  \"children\": [],                  \"Title\": \"Bolinhas para Gatos\",                  \"MetaTagDescription\": \"\"              },              {                  \"id\": 13,                  \"name\": \"Ratinhos\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/brinquedos/ratinhos\",                  \"children\": [],                  \"Title\": \"Ratinhos\",                  \"MetaTagDescription\": \"\"              },              {                  \"id\": 19,                  \"name\": \"Arranhador para gato\",                  \"hasChildren\": false,                  \"url\": \"https://lojadobreno.vtexcommercestable.com.br/brinquedos/arranhador-para-gato\",                  \"children\": [],                  \"Title\": \"Brinquedo Arranhador para gatos\",                  \"MetaTagDescription\": \"Arranhador gatos é indispensável no lar com felinos. Ideais para afiar as unhas e garantir a diversão\"              }          ],          \"Title\": \"Brinquedos para Gatos\",          \"MetaTagDescription\": \"\"      }  ]  ```
     * @param {String} contentType Describes the type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {String} categoryLevels Value of the category level you need to retrieve.
     * @param {module:api/CategoryApi~categoryTreeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetCategoryTree>}
     */
    categoryTree(contentType, accept, categoryLevels, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling categoryTree");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling categoryTree");
      }
      // verify the required parameter 'categoryLevels' is set
      if (categoryLevels === undefined || categoryLevels === null) {
        throw new Error("Missing the required parameter 'categoryLevels' when calling categoryTree");
      }

      let pathParams = {
        'categoryLevels': categoryLevels
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
      let returnType = [GetCategoryTree];
      return this.apiClient.callApi(
        '/api/catalog_system/pub/category/tree/{categoryLevels}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
