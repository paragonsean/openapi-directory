/**
 * Flight Delay Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.6
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
import Prediction from '../model/Prediction';

/**
* FlightDelayPrediction service.
* @module api/FlightDelayPredictionApi
* @version 1.0.6
*/
export default class FlightDelayPredictionApi {

    /**
    * Constructs a new FlightDelayPredictionApi. 
    * @alias module:api/FlightDelayPredictionApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getFlightDelayPrediction operation.
     * @callback module:api/FlightDelayPredictionApi~getFlightDelayPredictionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Prediction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the delay segment where the flight is likely to lay.
     * @param {String} originLocationCode city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler is departing, e.g. PAR for Paris
     * @param {String} destinationLocationCode city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
     * @param {Date} departureDate the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
     * @param {String} departureTime local time relative to originLocationCode on which the traveler will depart from the origin. Time respects ISO 8601 standard. e.g. 13:22:00
     * @param {Date} arrivalDate the date on which the traveler will arrive to the destination from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
     * @param {String} arrivalTime local time relative to destinationLocationCode on which the traveler will arrive to destination. Time respects ISO 8601 standard. e.g. 13:22:00
     * @param {String} aircraftCode IATA aircraft code (http://www.flugzeuginfo.net/table_accodes_iata_en.php)
     * @param {String} carrierCode airline / carrier code
     * @param {String} flightNumber flight number as assigned by the carrier
     * @param {String} duration flight duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
     * @param {module:api/FlightDelayPredictionApi~getFlightDelayPredictionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Prediction}
     */
    getFlightDelayPrediction(originLocationCode, destinationLocationCode, departureDate, departureTime, arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration, callback) {
      let postBody = null;
      // verify the required parameter 'originLocationCode' is set
      if (originLocationCode === undefined || originLocationCode === null) {
        throw new Error("Missing the required parameter 'originLocationCode' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'destinationLocationCode' is set
      if (destinationLocationCode === undefined || destinationLocationCode === null) {
        throw new Error("Missing the required parameter 'destinationLocationCode' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'departureDate' is set
      if (departureDate === undefined || departureDate === null) {
        throw new Error("Missing the required parameter 'departureDate' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'departureTime' is set
      if (departureTime === undefined || departureTime === null) {
        throw new Error("Missing the required parameter 'departureTime' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'arrivalDate' is set
      if (arrivalDate === undefined || arrivalDate === null) {
        throw new Error("Missing the required parameter 'arrivalDate' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'arrivalTime' is set
      if (arrivalTime === undefined || arrivalTime === null) {
        throw new Error("Missing the required parameter 'arrivalTime' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'aircraftCode' is set
      if (aircraftCode === undefined || aircraftCode === null) {
        throw new Error("Missing the required parameter 'aircraftCode' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'carrierCode' is set
      if (carrierCode === undefined || carrierCode === null) {
        throw new Error("Missing the required parameter 'carrierCode' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'flightNumber' is set
      if (flightNumber === undefined || flightNumber === null) {
        throw new Error("Missing the required parameter 'flightNumber' when calling getFlightDelayPrediction");
      }
      // verify the required parameter 'duration' is set
      if (duration === undefined || duration === null) {
        throw new Error("Missing the required parameter 'duration' when calling getFlightDelayPrediction");
      }

      let pathParams = {
      };
      let queryParams = {
        'originLocationCode': originLocationCode,
        'destinationLocationCode': destinationLocationCode,
        'departureDate': departureDate,
        'departureTime': departureTime,
        'arrivalDate': arrivalDate,
        'arrivalTime': arrivalTime,
        'aircraftCode': aircraftCode,
        'carrierCode': carrierCode,
        'flightNumber': flightNumber,
        'duration': duration
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/vnd.amadeus+json', 'application/json'];
      let returnType = Prediction;
      return this.apiClient.callApi(
        '/travel/predictions/flight-delay', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
