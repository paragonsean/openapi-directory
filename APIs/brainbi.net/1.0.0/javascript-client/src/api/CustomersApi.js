/**
 * brainbi
 * Welcome to the official API of the brainbi platform. Using this API you can freely integrate our analytics platform with any other solution.  Please refer to the following documentation and in case of any issues, please contact us at service@brainbi.net.  Please note: for this API you will use your email and password from the brainbi.net platform to gather a Bearer Token for any API calls (use Login and get token). Once you are finished with your calls, please do a logout to remove your token and keep your account safe (use logout).
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Customers service.
* @module api/CustomersApi
* @version 1.0.0
*/
export default class CustomersApi {

    /**
    * Constructs a new CustomersApi. 
    * @alias module:api/CustomersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the customers operation.
     * @callback module:api/CustomersApi~customersCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Customers
     * This resource lists all cusomters that are currently saved in your account.
     * @param {Object} opts Optional parameters
     * @param {String} [] 
     * @param {module:api/CustomersApi~customersCallback} callback The callback function, accepting three arguments: error, data, response
     */
    customers(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        '': opts['']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/customers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
