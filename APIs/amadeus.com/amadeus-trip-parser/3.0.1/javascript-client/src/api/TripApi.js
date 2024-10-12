/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import DocumentEnvelope from '../model/DocumentEnvelope';
import Error400 from '../model/Error400';
import Error500 from '../model/Error500';
import Error501 from '../model/Error501';
import PostTripParserRequest200Response from '../model/PostTripParserRequest200Response';

/**
* Trip service.
* @module api/TripApi
* @version 3.0.1
*/
export default class TripApi {

    /**
    * Constructs a new TripApi. 
    * @alias module:api/TripApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the postTripParserRequest operation.
     * @callback module:api/TripApi~postTripParserRequestCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PostTripParserRequest200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * POST Trip Parser request
     * 
     * @param {Object} opts Optional parameters
     * @param {module:model/DocumentEnvelope} [documentEnvelope] 
     * @param {module:api/TripApi~postTripParserRequestCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PostTripParserRequest200Response}
     */
    postTripParserRequest(opts, callback) {
      opts = opts || {};
      let postBody = opts['documentEnvelope'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/vnd.amadeus+json'];
      let accepts = ['application/vnd.amadeus+json'];
      let returnType = PostTripParserRequest200Response;
      return this.apiClient.callApi(
        '/travel/trip-parser', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
