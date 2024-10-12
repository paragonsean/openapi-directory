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
import CatalogDataCategoryAttributeInterface from '../model/CatalogDataCategoryAttributeInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* CategoriesAttributesAttributeCode service.
* @module api/CategoriesAttributesAttributeCodeApi
* @version 2.2.10
*/
export default class CategoriesAttributesAttributeCodeApi {

    /**
    * Constructs a new CategoriesAttributesAttributeCodeApi. 
    * @alias module:api/CategoriesAttributesAttributeCodeApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the catalogCategoryAttributeRepositoryV1GetGet operation.
     * @callback module:api/CategoriesAttributesAttributeCodeApi~catalogCategoryAttributeRepositoryV1GetGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CatalogDataCategoryAttributeInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * categories/attributes/{attributeCode}
     * Retrieve specific attribute
     * @param {String} attributeCode 
     * @param {module:api/CategoriesAttributesAttributeCodeApi~catalogCategoryAttributeRepositoryV1GetGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CatalogDataCategoryAttributeInterface}
     */
    catalogCategoryAttributeRepositoryV1GetGet(attributeCode, callback) {
      let postBody = null;
      // verify the required parameter 'attributeCode' is set
      if (attributeCode === undefined || attributeCode === null) {
        throw new Error("Missing the required parameter 'attributeCode' when calling catalogCategoryAttributeRepositoryV1GetGet");
      }

      let pathParams = {
        'attributeCode': attributeCode
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
      let returnType = CatalogDataCategoryAttributeInterface;
      return this.apiClient.callApi(
        '/V1/categories/attributes/{attributeCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
