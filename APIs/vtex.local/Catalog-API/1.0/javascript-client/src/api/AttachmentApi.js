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
import ApiCatalogPvtAttachmentsGet200Response from '../model/ApiCatalogPvtAttachmentsGet200Response';
import AttachmentRequest from '../model/AttachmentRequest';
import AttachmentResponse from '../model/AttachmentResponse';

/**
* Attachment service.
* @module api/AttachmentApi
* @version 1.0
*/
export default class AttachmentApi {

    /**
    * Constructs a new AttachmentApi. 
    * @alias module:api/AttachmentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiCatalogPvtAttachmentAttachmentidDelete operation.
     * @callback module:api/AttachmentApi~apiCatalogPvtAttachmentAttachmentidDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete attachment
     * Deletes a previously existing SKU attachment.
     * @param {String} attachmentid Attachment ID.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/AttachmentApi~apiCatalogPvtAttachmentAttachmentidDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiCatalogPvtAttachmentAttachmentidDelete(attachmentid, contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'attachmentid' is set
      if (attachmentid === undefined || attachmentid === null) {
        throw new Error("Missing the required parameter 'attachmentid' when calling apiCatalogPvtAttachmentAttachmentidDelete");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentAttachmentidDelete");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentAttachmentidDelete");
      }

      let pathParams = {
        'attachmentid': attachmentid
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
        '/api/catalog/pvt/attachment/{attachmentid}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtAttachmentAttachmentidGet operation.
     * @callback module:api/AttachmentApi~apiCatalogPvtAttachmentAttachmentidGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AttachmentResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get attachment
     * Gets information about a registered attachment.    >⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.  ## Response body example    ```json  {    \"Id\": 8,    \"Name\": \"Test\",    \"IsRequired\": true,    \"IsActive\": true,    \"Domains\": [      {        \"FieldName\": \"Basic test\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"      },      {        \"FieldName\": \"teste\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"      }    ]  }  ```
     * @param {String} attachmentid Attachment ID.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/AttachmentApi~apiCatalogPvtAttachmentAttachmentidGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AttachmentResponse}
     */
    apiCatalogPvtAttachmentAttachmentidGet(attachmentid, contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'attachmentid' is set
      if (attachmentid === undefined || attachmentid === null) {
        throw new Error("Missing the required parameter 'attachmentid' when calling apiCatalogPvtAttachmentAttachmentidGet");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentAttachmentidGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentAttachmentidGet");
      }

      let pathParams = {
        'attachmentid': attachmentid
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
      let returnType = AttachmentResponse;
      return this.apiClient.callApi(
        '/api/catalog/pvt/attachment/{attachmentid}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtAttachmentAttachmentidPut operation.
     * @callback module:api/AttachmentApi~apiCatalogPvtAttachmentAttachmentidPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AttachmentResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update attachment
     * Updates a previously existing SKU attachment with new information.    >⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    ```json  {    \"Name\": \"Test\",    \"IsRequired\": true,    \"IsActive\": true,    \"Domains\": [      {        \"FieldName\": \"Basic test\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"      },      {        \"FieldName\": \"teste\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"      }    ]  }  ```  ## Response body example    ```json  {    \"Id\": 8,    \"Name\": \"Test\",    \"IsRequired\": true,    \"IsActive\": true,    \"Domains\": [      {        \"FieldName\": \"Basic test\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"      },      {        \"FieldName\": \"teste\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"      }    ]  }  ```
     * @param {String} attachmentid Attachment ID.
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/AttachmentRequest} [attachmentRequest] 
     * @param {module:api/AttachmentApi~apiCatalogPvtAttachmentAttachmentidPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AttachmentResponse}
     */
    apiCatalogPvtAttachmentAttachmentidPut(attachmentid, contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['attachmentRequest'];
      // verify the required parameter 'attachmentid' is set
      if (attachmentid === undefined || attachmentid === null) {
        throw new Error("Missing the required parameter 'attachmentid' when calling apiCatalogPvtAttachmentAttachmentidPut");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentAttachmentidPut");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentAttachmentidPut");
      }

      let pathParams = {
        'attachmentid': attachmentid
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
      let returnType = AttachmentResponse;
      return this.apiClient.callApi(
        '/api/catalog/pvt/attachment/{attachmentid}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtAttachmentPost operation.
     * @callback module:api/AttachmentApi~apiCatalogPvtAttachmentPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AttachmentResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create attachment
     * Creates a new SKU attachment.   >⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    ```json  {    \"Name\": \"Test\",    \"IsRequired\": true,    \"IsActive\": true,    \"Domains\": [      {        \"FieldName\": \"Basic test\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"      },      {        \"FieldName\": \"teste\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"      }    ]  }  ```  ## Response body example    ```json  {    \"Id\": 8,    \"Name\": \"Test\",    \"IsRequired\": true,    \"IsActive\": true,    \"Domains\": [      {        \"FieldName\": \"Basic test\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"      },      {        \"FieldName\": \"teste\",        \"MaxCaracters\": \"\",        \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"      }    ]  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {Object} opts Optional parameters
     * @param {module:model/AttachmentRequest} [attachmentRequest] 
     * @param {module:api/AttachmentApi~apiCatalogPvtAttachmentPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AttachmentResponse}
     */
    apiCatalogPvtAttachmentPost(contentType, accept, opts, callback) {
      opts = opts || {};
      let postBody = opts['attachmentRequest'];
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentPost");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentPost");
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
      let returnType = AttachmentResponse;
      return this.apiClient.callApi(
        '/api/catalog/pvt/attachment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiCatalogPvtAttachmentsGet operation.
     * @callback module:api/AttachmentApi~apiCatalogPvtAttachmentsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiCatalogPvtAttachmentsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all attachments
     * Retrieves information about all registered attachments.    >⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Response body example    ```json  {      \"Page\": 1,      \"Size\": 11,      \"TotalRows\": 11,      \"TotalPage\": 1,      \"Data\": [          {              \"Id\": 1,              \"Name\": \"Acessórios do bicho\",              \"IsRequired\": true,              \"IsActive\": true,              \"Domains\": [                  {                      \"FieldName\": \"extra\",                      \"MaxCaracters\": \"\",                      \"DomainValues\": \"[0-3]#1[1-2][1]pricetable1;#3[0-2][0]pricetable2;#5[0-2][0]pricetable3\"                  }              ]          },          {              \"Id\": 2,              \"Name\": \"Sobrenome\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": []          },          {              \"Id\": 3,              \"Name\": \"Assinatura Teste\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": [                  {                      \"FieldName\": \" vtex.subscription.key.frequency\",                      \"MaxCaracters\": \"\",                      \"DomainValues\": \"1 day, 7 day, 1 month, 6 month\"                  },                  {                      \"FieldName\": \"vtex.subscription.key.validity.begin\",                      \"MaxCaracters\": \"\",                      \"DomainValues\": \"1\"                  },                  {                      \"FieldName\": \"vtex.subscription.key.validity.end\",                      \"MaxCaracters\": \"\",                      \"DomainValues\": \"31\"                  },                  {                      \"FieldName\": \"vtex.subscription.key.purchaseday\",                      \"MaxCaracters\": \"\",                      \"DomainValues\": \"1, 2, 20, 31\"                  }              ]          },          {              \"Id\": 5,              \"Name\": \"teste\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": []          },          {              \"Id\": 6,              \"Name\": \"teste2\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": []          },          {              \"Id\": 7,              \"Name\": \"vtex.subscription.teste3\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": []          },          {              \"Id\": 8,              \"Name\": \"teste api nova\",              \"IsRequired\": true,              \"IsActive\": true,              \"Domains\": [                  {                      \"FieldName\": \"Basic teste\",                      \"MaxCaracters\": \"\",                      \"DomainValues\": \"[1-2]#9[1-1][1]basic;#11[0-1][1]basic\"                  },                  {                      \"FieldName\": \"teste\",                      \"MaxCaracters\": \"\",                      \"DomainValues\": \"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\"                  }              ]          },          {              \"Id\": 9,              \"Name\": \"vtex.subscription.teste\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": []          },          {              \"Id\": 10,              \"Name\": \"Montagens\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": []          },          {              \"Id\": 11,              \"Name\": \"vtex.subscription.subscription\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": [                  {                      \"FieldName\": \"vtex.subscription.key.frequency\",                      \"MaxCaracters\": \"15\",                      \"DomainValues\": \"1 month\"                  },                  {                      \"FieldName\": \"vtex.subscription.key.purchaseday\",                      \"MaxCaracters\": \"15\",                      \"DomainValues\": \"1,15,28\"                  }              ]          },          {              \"Id\": 12,              \"Name\": \"T-Shirt Customization\",              \"IsRequired\": false,              \"IsActive\": true,              \"Domains\": [                  {                      \"FieldName\": \"T-Shirt Name\",                      \"MaxCaracters\": \"15\",                      \"DomainValues\": \"[]\"                  }              ]          }      ]  }  ```
     * @param {String} contentType Type of the content being sent.
     * @param {String} accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
     * @param {module:api/AttachmentApi~apiCatalogPvtAttachmentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiCatalogPvtAttachmentsGet200Response}
     */
    apiCatalogPvtAttachmentsGet(contentType, accept, callback) {
      let postBody = null;
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling apiCatalogPvtAttachmentsGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling apiCatalogPvtAttachmentsGet");
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
      let returnType = ApiCatalogPvtAttachmentsGet200Response;
      return this.apiClient.callApi(
        '/api/catalog/pvt/attachments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
