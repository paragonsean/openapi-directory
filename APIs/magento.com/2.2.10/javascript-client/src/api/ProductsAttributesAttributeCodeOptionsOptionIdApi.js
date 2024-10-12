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
import ErrorResponse from '../model/ErrorResponse';

/**
* ProductsAttributesAttributeCodeOptionsOptionId service.
* @module api/ProductsAttributesAttributeCodeOptionsOptionIdApi
* @version 2.2.10
*/
export default class ProductsAttributesAttributeCodeOptionsOptionIdApi {

    /**
    * Constructs a new ProductsAttributesAttributeCodeOptionsOptionIdApi. 
    * @alias module:api/ProductsAttributesAttributeCodeOptionsOptionIdApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the catalogProductAttributeOptionManagementV1DeleteDelete operation.
     * @callback module:api/ProductsAttributesAttributeCodeOptionsOptionIdApi~catalogProductAttributeOptionManagementV1DeleteDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Boolean} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * products/attributes/{attributeCode}/options/{optionId}
     * Delete option from attribute
     * @param {String} attributeCode 
     * @param {String} optionId 
     * @param {module:api/ProductsAttributesAttributeCodeOptionsOptionIdApi~catalogProductAttributeOptionManagementV1DeleteDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Boolean}
     */
    catalogProductAttributeOptionManagementV1DeleteDelete(attributeCode, optionId, callback) {
      let postBody = null;
      // verify the required parameter 'attributeCode' is set
      if (attributeCode === undefined || attributeCode === null) {
        throw new Error("Missing the required parameter 'attributeCode' when calling catalogProductAttributeOptionManagementV1DeleteDelete");
      }
      // verify the required parameter 'optionId' is set
      if (optionId === undefined || optionId === null) {
        throw new Error("Missing the required parameter 'optionId' when calling catalogProductAttributeOptionManagementV1DeleteDelete");
      }

      let pathParams = {
        'attributeCode': attributeCode,
        'optionId': optionId
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
      let returnType = 'Boolean';
      return this.apiClient.callApi(
        '/V1/products/attributes/{attributeCode}/options/{optionId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
