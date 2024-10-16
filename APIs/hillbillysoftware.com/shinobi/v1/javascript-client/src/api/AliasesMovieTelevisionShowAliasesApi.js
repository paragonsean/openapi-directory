/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Aliases from '../model/Aliases';

/**
* AliasesMovieTelevisionShowAliases service.
* @module api/AliasesMovieTelevisionShowAliasesApi
* @version v1
*/
export default class AliasesMovieTelevisionShowAliasesApi {

    /**
    * Constructs a new AliasesMovieTelevisionShowAliasesApi. 
    * @alias module:api/AliasesMovieTelevisionShowAliasesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the aliasesByIDGet operation.
     * @callback module:api/AliasesMovieTelevisionShowAliasesApi~aliasesByIDGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Aliases>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get known aliases for Movies or Television shows from passed imdbID
     * @param {String} accessToken 
     * @param {String} imdbID 
     * @param {module:api/AliasesMovieTelevisionShowAliasesApi~aliasesByIDGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Aliases>}
     */
    aliasesByIDGet(accessToken, imdbID, callback) {
      let postBody = null;
      // verify the required parameter 'accessToken' is set
      if (accessToken === undefined || accessToken === null) {
        throw new Error("Missing the required parameter 'accessToken' when calling aliasesByIDGet");
      }
      // verify the required parameter 'imdbID' is set
      if (imdbID === undefined || imdbID === null) {
        throw new Error("Missing the required parameter 'imdbID' when calling aliasesByIDGet");
      }

      let pathParams = {
        'AccessToken': accessToken,
        'imdbID': imdbID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = [Aliases];
      return this.apiClient.callApi(
        '/Aliases/ByID/{AccessToken}/{imdbID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the aliasesGet operation.
     * @callback module:api/AliasesMovieTelevisionShowAliasesApi~aliasesGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Aliases>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get known aliases for Movies or Television shows
     * @param {String} accessToken 
     * @param {String} title Title of movie or television show
     * @param {module:api/AliasesMovieTelevisionShowAliasesApi~aliasesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Aliases>}
     */
    aliasesGet(accessToken, title, callback) {
      let postBody = null;
      // verify the required parameter 'accessToken' is set
      if (accessToken === undefined || accessToken === null) {
        throw new Error("Missing the required parameter 'accessToken' when calling aliasesGet");
      }
      // verify the required parameter 'title' is set
      if (title === undefined || title === null) {
        throw new Error("Missing the required parameter 'title' when calling aliasesGet");
      }

      let pathParams = {
        'AccessToken': accessToken,
        'Title': title
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = [Aliases];
      return this.apiClient.callApi(
        '/Aliases/ByName/{AccessToken}/{Title}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
