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
import CustomerAccountManagementV1ActivateByIdPutRequest from '../model/CustomerAccountManagementV1ActivateByIdPutRequest';
import CustomerDataCustomerInterface from '../model/CustomerDataCustomerInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* CustomersMeActivate service.
* @module api/CustomersMeActivateApi
* @version 2.2.10
*/
export default class CustomersMeActivateApi {

    /**
    * Constructs a new CustomersMeActivateApi. 
    * @alias module:api/CustomersMeActivateApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the customerAccountManagementV1ActivateByIdPut operation.
     * @callback module:api/CustomersMeActivateApi~customerAccountManagementV1ActivateByIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomerDataCustomerInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * customers/me/activate
     * Activate a customer account using a key that was sent in a confirmation email.
     * @param {Object} opts Optional parameters
     * @param {module:model/CustomerAccountManagementV1ActivateByIdPutRequest} [customerAccountManagementV1ActivateByIdPutRequest] 
     * @param {module:api/CustomersMeActivateApi~customerAccountManagementV1ActivateByIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomerDataCustomerInterface}
     */
    customerAccountManagementV1ActivateByIdPut(opts, callback) {
      opts = opts || {};
      let postBody = opts['customerAccountManagementV1ActivateByIdPutRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = CustomerDataCustomerInterface;
      return this.apiClient.callApi(
        '/V1/customers/me/activate', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
