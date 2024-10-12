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
* AttributeMetadataCustomerAddressCustom service.
* @module api/AttributeMetadataCustomerAddressCustomApi
* @version 2.2.10
*/
export default class AttributeMetadataCustomerAddressCustomApi {

    /**
    * Constructs a new AttributeMetadataCustomerAddressCustomApi. 
    * @alias module:api/AttributeMetadataCustomerAddressCustomApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the customerAddressMetadataV1GetCustomAttributesMetadataGet operation.
     * @callback module:api/AttributeMetadataCustomerAddressCustomApi~customerAddressMetadataV1GetCustomAttributesMetadataGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/CustomerDataAttributeMetadataInterface>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * attributeMetadata/customerAddress/custom
     * Get custom attributes metadata for the given data interface.
     * @param {Object} opts Optional parameters
     * @param {String} [dataInterfaceName] 
     * @param {module:api/AttributeMetadataCustomerAddressCustomApi~customerAddressMetadataV1GetCustomAttributesMetadataGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/CustomerDataAttributeMetadataInterface>}
     */
    customerAddressMetadataV1GetCustomAttributesMetadataGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'dataInterfaceName': opts['dataInterfaceName']
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
        '/V1/attributeMetadata/customerAddress/custom', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
