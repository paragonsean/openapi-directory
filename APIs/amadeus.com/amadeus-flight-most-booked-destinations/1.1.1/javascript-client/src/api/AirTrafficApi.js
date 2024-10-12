/**
 * Flight Most Booked Destinations
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.1
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
import Success from '../model/Success';

/**
* AirTraffic service.
* @module api/AirTrafficApi
* @version 1.1.1
*/
export default class AirTrafficApi {

    /**
    * Constructs a new AirTrafficApi. 
    * @alias module:api/AirTrafficApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getAirTraffic operation.
     * @callback module:api/AirTrafficApi~getAirTrafficCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Success} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a list of air traffic reports.
     * @param {String} originCityCode Code for the origin city following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). - e.g. BOS for Boston
     * @param {String} period period when consumers are traveling. * It can be a month only.  * ISO format must be used - e.g. 2015-05.  * Period ranges are not supported.  * Only periods from 2011-01 up to previous month are valid.  * Future dates are not supported. 
     * @param {Object} opts Optional parameters
     * @param {Number} [max = 10.0)] maximum number of destinations in the response. Default value is 10 and maximum value is 50.
     * @param {String} [fields] list of attributes desired in the response or list of attributes to remove from the response (with \"-\" before fields)  * The attributes names must contain the whole path (except resource name) e.g. travelers
     * @param {Number} [pageLimit = 10)] maximum items in one page
     * @param {Number} [pageOffset = 0)] start index of the requested page
     * @param {module:model/String} [sort = 'analytics.travelers.score')] defines on which attribute the sorting will be done: * analytics.flights.score - sort destinations by flights score (decreasing) * analytics.travelers.score - sort destination by traveler's score (decreasing) 
     * @param {module:api/AirTrafficApi~getAirTrafficCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Success}
     */
    getAirTraffic(originCityCode, period, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'originCityCode' is set
      if (originCityCode === undefined || originCityCode === null) {
        throw new Error("Missing the required parameter 'originCityCode' when calling getAirTraffic");
      }
      // verify the required parameter 'period' is set
      if (period === undefined || period === null) {
        throw new Error("Missing the required parameter 'period' when calling getAirTraffic");
      }

      let pathParams = {
      };
      let queryParams = {
        'originCityCode': originCityCode,
        'period': period,
        'max': opts['max'],
        'fields': opts['fields'],
        'page[limit]': opts['pageLimit'],
        'page[offset]': opts['pageOffset'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/vnd.amadeus+json'];
      let returnType = Success;
      return this.apiClient.callApi(
        '/travel/analytics/air-traffic/booked', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
