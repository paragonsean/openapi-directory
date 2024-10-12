/**
 * FaSta - Station Facilities Status
 * A RESTful webservice to retrieve data about the operational state of public elevators and escalators in german railway stations.
 *
 * The version of the OpenAPI document: 2.1
 * Contact: michael.binzen@deutschebahn.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Facility from '../model/Facility';
import Station from '../model/Station';

/**
* Default service.
* @module api/DefaultApi
* @version 2.1
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the findFacilities operation.
     * @callback module:api/DefaultApi~findFacilitiesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Facility>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Access to public facilities (escalators and elevators) in railway stations
     * @param {Object} opts Optional parameters
     * @param {Array.<module:model/String>} [type] Type of the facility.
     * @param {Array.<module:model/String>} [state] Operational state of the facility.
     * @param {Array.<Number>} [equipmentnumbers] List of equipmentnumbers to select.
     * @param {Number} [stationnumber] Number of the station the facilities belong to.
     * @param {Array.<String>} [area] Geo coordinate rectangle in WGS84-format to filter facilities by geographical position. Parameters must be 4 numbers exactly as follows: longitudeWest, latitudeSouth, longitudeEast, latitudeNorth.
     * @param {module:api/DefaultApi~findFacilitiesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Facility>}
     */
    findFacilities(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'type': this.apiClient.buildCollectionParam(opts['type'], 'csv'),
        'state': this.apiClient.buildCollectionParam(opts['state'], 'csv'),
        'equipmentnumbers': this.apiClient.buildCollectionParam(opts['equipmentnumbers'], 'csv'),
        'stationnumber': opts['stationnumber'],
        'area': this.apiClient.buildCollectionParam(opts['area'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserSecurity'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Facility];
      return this.apiClient.callApi(
        '/facilities', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the findStationByStationNumber operation.
     * @callback module:api/DefaultApi~findStationByStationNumberCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Station} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns information about a station (and its corresponding facilities) identified by a stationnumber.
     * @param {Number} stationnumber Number of the station to fetch.
     * @param {module:api/DefaultApi~findStationByStationNumberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Station}
     */
    findStationByStationNumber(stationnumber, callback) {
      let postBody = null;
      // verify the required parameter 'stationnumber' is set
      if (stationnumber === undefined || stationnumber === null) {
        throw new Error("Missing the required parameter 'stationnumber' when calling findStationByStationNumber");
      }

      let pathParams = {
        'stationnumber': stationnumber
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserSecurity'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Station;
      return this.apiClient.callApi(
        '/stations/{stationnumber}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getFacilityByEquipmentNumber operation.
     * @callback module:api/DefaultApi~getFacilityByEquipmentNumberCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Facility} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the facility identified by its equipmentnumber.
     * @param {Number} equipmentnumber Equipmentnumber of the facility to fetch.
     * @param {module:api/DefaultApi~getFacilityByEquipmentNumberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Facility}
     */
    getFacilityByEquipmentNumber(equipmentnumber, callback) {
      let postBody = null;
      // verify the required parameter 'equipmentnumber' is set
      if (equipmentnumber === undefined || equipmentnumber === null) {
        throw new Error("Missing the required parameter 'equipmentnumber' when calling getFacilityByEquipmentNumber");
      }

      let pathParams = {
        'equipmentnumber': equipmentnumber
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['UserSecurity'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Facility;
      return this.apiClient.callApi(
        '/facilities/{equipmentnumber}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
