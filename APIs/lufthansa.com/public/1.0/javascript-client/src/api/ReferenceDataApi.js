/**
 * LH Public API
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
import AirportResponse from '../model/AirportResponse';

/**
* ReferenceData service.
* @module api/ReferenceDataApi
* @version 1.0
*/
export default class ReferenceDataApi {

    /**
    * Constructs a new ReferenceDataApi. 
    * @alias module:api/ReferenceDataApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the referencesAircraftByAircraftCodeGet operation.
     * @callback module:api/ReferenceDataApi~referencesAircraftByAircraftCodeGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Aircraft
     * List all aircraft types or one specific aircraft type.
     * @param {String} accept http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
     * @param {String} aircraftCode 3-character IATA aircraft code
     * @param {Object} opts Optional parameters
     * @param {String} [limit = '20')] Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
     * @param {String} [offset = '0')] Number of records skipped. Defaults to 0
     * @param {module:api/ReferenceDataApi~referencesAircraftByAircraftCodeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    referencesAircraftByAircraftCodeGet(accept, aircraftCode, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling referencesAircraftByAircraftCodeGet");
      }
      // verify the required parameter 'aircraftCode' is set
      if (aircraftCode === undefined || aircraftCode === null) {
        throw new Error("Missing the required parameter 'aircraftCode' when calling referencesAircraftByAircraftCodeGet");
      }

      let pathParams = {
        'aircraftCode': aircraftCode
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/references/aircraft/{aircraftCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesAirlinesByAirlineCodeGet operation.
     * @callback module:api/ReferenceDataApi~referencesAirlinesByAirlineCodeGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Airlines
     * List all airlines or one specific airline.
     * @param {String} accept http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
     * @param {String} airlineCode 2-character IATA airline/carrier code
     * @param {Object} opts Optional parameters
     * @param {String} [limit = '20')] Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
     * @param {String} [offset = '0')] Number of records skipped. Defaults to 0
     * @param {module:api/ReferenceDataApi~referencesAirlinesByAirlineCodeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    referencesAirlinesByAirlineCodeGet(accept, airlineCode, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling referencesAirlinesByAirlineCodeGet");
      }
      // verify the required parameter 'airlineCode' is set
      if (airlineCode === undefined || airlineCode === null) {
        throw new Error("Missing the required parameter 'airlineCode' when calling referencesAirlinesByAirlineCodeGet");
      }

      let pathParams = {
        'airlineCode': airlineCode
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/references/airlines/{airlineCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesAirportsByAirportCodeGet operation.
     * @callback module:api/ReferenceDataApi~referencesAirportsByAirportCodeGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AirportResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Airports
     * List all airports or one specific airport. All airports response is very large. It is possible to request the response in a specific language.
     * @param {String} accept http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
     * @param {String} airportCode 3-letter IATA airport code
     * @param {Object} opts Optional parameters
     * @param {String} [lang] 2-letter ISO 3166-1 language code
     * @param {String} [limit = '20')] Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
     * @param {String} [offset = '0')] Number of records skipped. Defaults to 0
     * @param {Boolean} [lHoperated] Restrict the results to locations with flights operated by LH (false=0, true=1)
     * @param {module:api/ReferenceDataApi~referencesAirportsByAirportCodeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AirportResponse}
     */
    referencesAirportsByAirportCodeGet(accept, airportCode, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling referencesAirportsByAirportCodeGet");
      }
      // verify the required parameter 'airportCode' is set
      if (airportCode === undefined || airportCode === null) {
        throw new Error("Missing the required parameter 'airportCode' when calling referencesAirportsByAirportCodeGet");
      }

      let pathParams = {
        'airportCode': airportCode
      };
      let queryParams = {
        'lang': opts['lang'],
        'limit': opts['limit'],
        'offset': opts['offset'],
        'LHoperated': opts['lHoperated']
      };
      let headerParams = {
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AirportResponse;
      return this.apiClient.callApi(
        '/references/airports/{airportCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesAirportsNearestByLatitudeAndLongitudeGet operation.
     * @callback module:api/ReferenceDataApi~referencesAirportsNearestByLatitudeAndLongitudeGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Nearest Airports
     * List the 5 closest airports to the given latitude and longitude, irrespective of the radius of the reference point.
     * @param {Number} latitude Latitude in decimal format to at most 3 decimal places
     * @param {Number} longitude Longitude in decimal format to at most 3 decimal places
     * @param {String} accept http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
     * @param {Object} opts Optional parameters
     * @param {String} [lang] 2 letter ISO 3166-1 language code
     * @param {module:api/ReferenceDataApi~referencesAirportsNearestByLatitudeAndLongitudeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    referencesAirportsNearestByLatitudeAndLongitudeGet(latitude, longitude, accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'latitude' is set
      if (latitude === undefined || latitude === null) {
        throw new Error("Missing the required parameter 'latitude' when calling referencesAirportsNearestByLatitudeAndLongitudeGet");
      }
      // verify the required parameter 'longitude' is set
      if (longitude === undefined || longitude === null) {
        throw new Error("Missing the required parameter 'longitude' when calling referencesAirportsNearestByLatitudeAndLongitudeGet");
      }
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling referencesAirportsNearestByLatitudeAndLongitudeGet");
      }

      let pathParams = {
        'latitude': latitude,
        'longitude': longitude
      };
      let queryParams = {
        'lang': opts['lang']
      };
      let headerParams = {
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/references/airports/nearest/{latitude},{longitude}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesCitiesByCityCodeGet operation.
     * @callback module:api/ReferenceDataApi~referencesCitiesByCityCodeGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cities
     * List all cities or one specific city. It is possible to request the response in a specific language.
     * @param {String} accept http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
     * @param {String} cityCode 3-letter IATA city code
     * @param {Object} opts Optional parameters
     * @param {String} [lang] 2 letter ISO 3166-1 language code
     * @param {String} [limit = '20')] Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
     * @param {String} [offset = '0')] Number of records skipped. Defaults to 0
     * @param {module:api/ReferenceDataApi~referencesCitiesByCityCodeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    referencesCitiesByCityCodeGet(accept, cityCode, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling referencesCitiesByCityCodeGet");
      }
      // verify the required parameter 'cityCode' is set
      if (cityCode === undefined || cityCode === null) {
        throw new Error("Missing the required parameter 'cityCode' when calling referencesCitiesByCityCodeGet");
      }

      let pathParams = {
        'cityCode': cityCode
      };
      let queryParams = {
        'lang': opts['lang'],
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/references/cities/{cityCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesCountriesByCountryCodeGet operation.
     * @callback module:api/ReferenceDataApi~referencesCountriesByCountryCodeGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Countries
     * List all countries or one specific country. It is possible to request the response in a specific language.
     * @param {String} accept http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
     * @param {String} countryCode 2-letter ISO 3166-1 country code
     * @param {Object} opts Optional parameters
     * @param {String} [lang] 2 letter ISO 3166-1 language code
     * @param {String} [limit = '20')] Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
     * @param {String} [offset = '0')] Number of records skipped. Defaults to 0
     * @param {module:api/ReferenceDataApi~referencesCountriesByCountryCodeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    referencesCountriesByCountryCodeGet(accept, countryCode, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling referencesCountriesByCountryCodeGet");
      }
      // verify the required parameter 'countryCode' is set
      if (countryCode === undefined || countryCode === null) {
        throw new Error("Missing the required parameter 'countryCode' when calling referencesCountriesByCountryCodeGet");
      }

      let pathParams = {
        'countryCode': countryCode
      };
      let queryParams = {
        'lang': opts['lang'],
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
        'Accept': accept
      };
      let formParams = {
      };

      let authNames = ['auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/references/countries/{countryCode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
