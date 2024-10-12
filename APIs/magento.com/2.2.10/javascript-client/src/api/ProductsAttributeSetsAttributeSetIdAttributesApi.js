/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CatalogDataProductAttributeInterface from '../model/CatalogDataProductAttributeInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* ProductsAttributeSetsAttributeSetIdAttributes service.
* @module api/ProductsAttributeSetsAttributeSetIdAttributesApi
* @version 2.2.10
*/
export default class ProductsAttributeSetsAttributeSetIdAttributesApi {

    /**
    * Constructs a new ProductsAttributeSetsAttributeSetIdAttributesApi. 
    * @alias module:api/ProductsAttributeSetsAttributeSetIdAttributesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the catalogProductAttributeManagementV1GetAttributesGet operation.
     * @callback module:api/ProductsAttributeSetsAttributeSetIdAttributesApi~catalogProductAttributeManagementV1GetAttributesGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/CatalogDataProductAttributeInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/attribute-sets/{attributeSetId}/attributes
     * Retrieve related attributes based on given attribute set ID
     * @param {String} attributeSetId 
     * @param {module:api/ProductsAttributeSetsAttributeSetIdAttributesApi~catalogProductAttributeManagementV1GetAttributesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/CatalogDataProductAttributeInterface>}
     */
    catalogProductAttributeManagementV1GetAttributesGet(attributeSetId, callback) {
      let postBody = null;
      // verify the required parameter 'attributeSetId' is set
      if (attributeSetId === undefined || attributeSetId === null) {
        throw new Error("Missing the required parameter 'attributeSetId' when calling catalogProductAttributeManagementV1GetAttributesGet");
      }

      let pathParams = {
        'attributeSetId': attributeSetId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = [CatalogDataProductAttributeInterface];
      return this.apiClient.callApi(
        '/V1/products/attribute-sets/{attributeSetId}/attributes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
