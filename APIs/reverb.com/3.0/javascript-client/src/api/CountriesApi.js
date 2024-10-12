/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Countries service.
* @module api/CountriesApi
* @version 3.0
*/
export default class CountriesApi {

    /**
    * Constructs a new CountriesApi. 
    * @alias module:api/CountriesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the countriesGet operation.
     * @callback module:api/CountriesApi~countriesGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of country codes with corresponding subregions
     * Retrieve a list of country codes with corresponding subregions
     * @param {module:api/CountriesApi~countriesGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    countriesGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
        '/countries', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
