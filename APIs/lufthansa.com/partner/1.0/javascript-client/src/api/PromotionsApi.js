/**
 * LH Partner API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Promotions service.
* @module api/PromotionsApi
* @version 1.0
*/
export default class PromotionsApi {

    /**
    * Constructs a new PromotionsApi. 
    * @alias module:api/PromotionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the priceOffers operation.
     * @callback module:api/PromotionsApi~priceOffersCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Price Offers
     * Retrieve a best price offer given an origin and destination.
     * @param {String} origin Departure city. 3-letter IATA city code
     * @param {String} destination Destination city. 3-letter IATA city code
     * @param {String} departureDate Departure date in local time (YYYY-MM-DD)
     * @param {String} returnDate Return date in local time (YYYY-MM-DD)
     * @param {Object} opts Optional parameters
     * @param {String} [service = 'amadeusBestPrice')] Optional parameter.
     * @param {module:api/PromotionsApi~priceOffersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    priceOffers(origin, destination, departureDate, returnDate, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'origin' is set
      if (origin === undefined || origin === null) {
        throw new Error("Missing the required parameter 'origin' when calling priceOffers");
      }
      // verify the required parameter 'destination' is set
      if (destination === undefined || destination === null) {
        throw new Error("Missing the required parameter 'destination' when calling priceOffers");
      }
      // verify the required parameter 'departureDate' is set
      if (departureDate === undefined || departureDate === null) {
        throw new Error("Missing the required parameter 'departureDate' when calling priceOffers");
      }
      // verify the required parameter 'returnDate' is set
      if (returnDate === undefined || returnDate === null) {
        throw new Error("Missing the required parameter 'returnDate' when calling priceOffers");
      }

      let pathParams = {
        'origin': origin,
        'destination': destination
      };
      let queryParams = {
        'departureDate': departureDate,
        'returnDate': returnDate,
        'service': opts['service']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/promotions/priceoffers/flights/ond/{origin}/{destination}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
