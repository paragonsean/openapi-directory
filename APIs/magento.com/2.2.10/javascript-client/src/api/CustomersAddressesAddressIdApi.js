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
import CustomerDataAddressInterface from '../model/CustomerDataAddressInterface';
import ErrorResponse from '../model/ErrorResponse';

/**
* CustomersAddressesAddressId service.
* @module api/CustomersAddressesAddressIdApi
* @version 2.2.10
*/
export default class CustomersAddressesAddressIdApi {

    /**
    * Constructs a new CustomersAddressesAddressIdApi. 
    * @alias module:api/CustomersAddressesAddressIdApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the customerAddressRepositoryV1GetByIdGet operation.
     * @callback module:api/CustomersAddressesAddressIdApi~customerAddressRepositoryV1GetByIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomerDataAddressInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * customers/addresses/{addressId}
     * Retrieve customer address.
     * @param {Number} addressId 
     * @param {module:api/CustomersAddressesAddressIdApi~customerAddressRepositoryV1GetByIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomerDataAddressInterface}
     */
    customerAddressRepositoryV1GetByIdGet(addressId, callback) {
      let postBody = null;
      // verify the required parameter 'addressId' is set
      if (addressId === undefined || addressId === null) {
        throw new Error("Missing the required parameter 'addressId' when calling customerAddressRepositoryV1GetByIdGet");
      }

      let pathParams = {
        'addressId': addressId
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
      let returnType = CustomerDataAddressInterface;
      return this.apiClient.callApi(
        '/V1/customers/addresses/{addressId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
