/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Error400 from '../model/Error400';
import Error500 from '../model/Error500';
import FlightOffersSearchReply from '../model/FlightOffersSearchReply';
import Success from '../model/Success';

/**
* FlightChoicePrediction service.
* @module api/FlightChoicePredictionApi
* @version 2.0.2
*/
export default class FlightChoicePredictionApi {

    /**
    * Constructs a new FlightChoicePredictionApi. 
    * @alias module:api/FlightChoicePredictionApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getFlightChoicePredict operation.
     * @callback module:api/FlightChoicePredictionApi~getFlightChoicePredictCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Success} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Predict the choice of flight offers.
     * @param {String} xHTTPMethodOverride the HTTP method to apply
     * @param {module:model/FlightOffersSearchReply} body 
     * @param {module:api/FlightChoicePredictionApi~getFlightChoicePredictCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Success}
     */
    getFlightChoicePredict(xHTTPMethodOverride, body, callback) {
      let postBody = body;
      // verify the required parameter 'xHTTPMethodOverride' is set
      if (xHTTPMethodOverride === undefined || xHTTPMethodOverride === null) {
        throw new Error("Missing the required parameter 'xHTTPMethodOverride' when calling getFlightChoicePredict");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling getFlightChoicePredict");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-HTTP-Method-Override': xHTTPMethodOverride
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/vnd.amadeus+json', 'application/json'];
      let accepts = ['application/vnd.amadeus+json', 'application/json'];
      let returnType = Success;
      return this.apiClient.callApi(
        '/shopping/flight-offers/prediction', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
