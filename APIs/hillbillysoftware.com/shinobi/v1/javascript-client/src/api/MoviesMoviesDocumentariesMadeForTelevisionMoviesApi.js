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
import MovieInformation from '../model/MovieInformation';

/**
* MoviesMoviesDocumentariesMadeForTelevisionMovies service.
* @module api/MoviesMoviesDocumentariesMadeForTelevisionMoviesApi
* @version v1
*/
export default class MoviesMoviesDocumentariesMadeForTelevisionMoviesApi {

    /**
    * Constructs a new MoviesMoviesDocumentariesMadeForTelevisionMoviesApi. 
    * @alias module:api/MoviesMoviesDocumentariesMadeForTelevisionMoviesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the movieIDGet operation.
     * @callback module:api/MoviesMoviesDocumentariesMadeForTelevisionMoviesApi~movieIDGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MovieInformation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} accesstoken 
     * @param {String} imdbID 
     * @param {module:api/MoviesMoviesDocumentariesMadeForTelevisionMoviesApi~movieIDGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MovieInformation}
     */
    movieIDGet(accesstoken, imdbID, callback) {
      let postBody = null;
      // verify the required parameter 'accesstoken' is set
      if (accesstoken === undefined || accesstoken === null) {
        throw new Error("Missing the required parameter 'accesstoken' when calling movieIDGet");
      }
      // verify the required parameter 'imdbID' is set
      if (imdbID === undefined || imdbID === null) {
        throw new Error("Missing the required parameter 'imdbID' when calling movieIDGet");
      }

      let pathParams = {
        'accesstoken': accesstoken,
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
      let returnType = MovieInformation;
      return this.apiClient.callApi(
        '/Movie/ByID/{accesstoken}/{imdbID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the movieSearchGetAsync operation.
     * @callback module:api/MoviesMoviesDocumentariesMadeForTelevisionMoviesApi~movieSearchGetAsyncCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/MovieInformation>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Searches for movies, result set limited to 5 records
     * @param {String} accessToken 
     * @param {String} query 
     * @param {module:api/MoviesMoviesDocumentariesMadeForTelevisionMoviesApi~movieSearchGetAsyncCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/MovieInformation>}
     */
    movieSearchGetAsync(accessToken, query, callback) {
      let postBody = null;
      // verify the required parameter 'accessToken' is set
      if (accessToken === undefined || accessToken === null) {
        throw new Error("Missing the required parameter 'accessToken' when calling movieSearchGetAsync");
      }
      // verify the required parameter 'query' is set
      if (query === undefined || query === null) {
        throw new Error("Missing the required parameter 'query' when calling movieSearchGetAsync");
      }

      let pathParams = {
        'AccessToken': accessToken,
        'Query': query
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
      let returnType = [MovieInformation];
      return this.apiClient.callApi(
        '/Movie/Search/{AccessToken}/{Query}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
