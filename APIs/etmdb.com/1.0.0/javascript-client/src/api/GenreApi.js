/**
 * EtMDB REST API v1
 * The Ethiopian Movie Database
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
* Genre service.
* @module api/GenreApi
* @version 1.0.0
*/
export default class GenreApi {

    /**
    * Constructs a new GenreApi. 
    * @alias module:api/GenreApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the genreSearchRead operation.
     * @callback module:api/GenreApi~genreSearchReadCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return movie genre search result
     * Return movie genre search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie genres * You can use both Amharic or English charset/font to search  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date
     * @param {String} movieTitle 
     * @param {module:api/GenreApi~genreSearchReadCallback} callback The callback function, accepting three arguments: error, data, response
     */
    genreSearchRead(movieTitle, callback) {
      let postBody = null;
      // verify the required parameter 'movieTitle' is set
      if (movieTitle === undefined || movieTitle === null) {
        throw new Error("Missing the required parameter 'movieTitle' when calling genreSearchRead");
      }

      let pathParams = {
        'movie_title': movieTitle
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
        '/api/v1/genre/search/{movie_title}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the genreSearchallRead operation.
     * @callback module:api/GenreApi~genreSearchallReadCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return movie genre search result
     * Return movie genre search result  ### Response Class (Status 200)  * __{movie_genre_type}__: Used as a key word to search movie genres  For more details on how movies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date
     * @param {String} movieGenreType 
     * @param {module:api/GenreApi~genreSearchallReadCallback} callback The callback function, accepting three arguments: error, data, response
     */
    genreSearchallRead(movieGenreType, callback) {
      let postBody = null;
      // verify the required parameter 'movieGenreType' is set
      if (movieGenreType === undefined || movieGenreType === null) {
        throw new Error("Missing the required parameter 'movieGenreType' when calling genreSearchallRead");
      }

      let pathParams = {
        'movie_genre_type': movieGenreType
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
        '/api/v1/genre/searchall/{movie_genre_type}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
