/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import GetCountriesDictOut from '../model/GetCountriesDictOut';
import GetCurrenciesDictOut from '../model/GetCurrenciesDictOut';
import GetProductTypesDictOut from '../model/GetProductTypesDictOut';

/**
* Dictionaries service.
* @module api/DictionariesApi
* @version 1
*/
export default class DictionariesApi {

    /**
    * Constructs a new DictionariesApi. 
    * @alias module:api/DictionariesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getCountriesDict operation.
     * @callback module:api/DictionariesApi~getCountriesDictCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCountriesDictOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Countries
     * @param {Object} opts Optional parameters
     * @param {Boolean} [taxSupported] Should only countries with tax supported be listed?
     * @param {module:api/DictionariesApi~getCountriesDictCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCountriesDictOut}
     */
    getCountriesDict(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'tax_supported': opts['taxSupported']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetCountriesDictOut;
      return this.apiClient.callApi(
        '/api/v1/dictionaries/countries', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCurrenciesDict operation.
     * @callback module:api/DictionariesApi~getCurrenciesDictCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCurrenciesDictOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Currencies
     * @param {module:api/DictionariesApi~getCurrenciesDictCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCurrenciesDictOut}
     */
    getCurrenciesDict(callback) {
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
      let accepts = ['application/json'];
      let returnType = GetCurrenciesDictOut;
      return this.apiClient.callApi(
        '/api/v1/dictionaries/currencies', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProductTypesDict operation.
     * @callback module:api/DictionariesApi~getProductTypesDictCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetProductTypesDictOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Product types
     * @param {module:api/DictionariesApi~getProductTypesDictCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetProductTypesDictOut}
     */
    getProductTypesDict(callback) {
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
      let accepts = ['application/json'];
      let returnType = GetProductTypesDictOut;
      return this.apiClient.callApi(
        '/api/v1/dictionaries/product_types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
