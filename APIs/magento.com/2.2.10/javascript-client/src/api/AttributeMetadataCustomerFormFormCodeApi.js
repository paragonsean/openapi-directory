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
import CustomerDataAttributeMetadataInterface from '../model/CustomerDataAttributeMetadataInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* AttributeMetadataCustomerFormFormCode service.
* @module api/AttributeMetadataCustomerFormFormCodeApi
* @version 2.2.10
*/
export default class AttributeMetadataCustomerFormFormCodeApi {

    /**
    * Constructs a new AttributeMetadataCustomerFormFormCodeApi. 
    * @alias module:api/AttributeMetadataCustomerFormFormCodeApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the customerCustomerMetadataV1GetAttributesGet operation.
     * @callback module:api/AttributeMetadataCustomerFormFormCodeApi~customerCustomerMetadataV1GetAttributesGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/CustomerDataAttributeMetadataInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * attributeMetadata/customer/form/{formCode}
     * Retrieve all attributes filtered by form code
     * @param {String} formCode 
     * @param {module:api/AttributeMetadataCustomerFormFormCodeApi~customerCustomerMetadataV1GetAttributesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/CustomerDataAttributeMetadataInterface>}
     */
    customerCustomerMetadataV1GetAttributesGet(formCode, callback) {
      let postBody = null;
      // verify the required parameter 'formCode' is set
      if (formCode === undefined || formCode === null) {
        throw new Error("Missing the required parameter 'formCode' when calling customerCustomerMetadataV1GetAttributesGet");
      }

      let pathParams = {
        'formCode': formCode
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
      let returnType = [CustomerDataAttributeMetadataInterface];
      return this.apiClient.callApi(
        '/V1/attributeMetadata/customer/form/{formCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
