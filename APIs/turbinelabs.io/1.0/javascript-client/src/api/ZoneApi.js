/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
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
import Error from '../model/Error';
import MultiZoneResult from '../model/MultiZoneResult';
import ZoneCreate from '../model/ZoneCreate';
import ZoneResult from '../model/ZoneResult';

/**
* Zone service.
* @module api/ZoneApi
* @version 1.0
*/
export default class ZoneApi {

    /**
    * Constructs a new ZoneApi. 
    * @alias module:api/ZoneApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the zoneGet operation.
     * @callback module:api/ZoneApi~zoneGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MultiZoneResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get a list of zones
     * Get all zones. possibly with filters 
     * @param {Object} opts Optional parameters
     * @param {String} [filters] A JSON encoded array of ZoneFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ZoneFilter will be included. 
     * @param {module:api/ZoneApi~zoneGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MultiZoneResult}
     */
    zoneGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filters': opts['filters']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = MultiZoneResult;
      return this.apiClient.callApi(
        '/zone', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the zonePost operation.
     * @callback module:api/ZoneApi~zonePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ZoneResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * create zone
     * Create a new zone. 
     * @param {module:model/ZoneCreate} zone the zone to create
     * @param {module:api/ZoneApi~zonePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ZoneResult}
     */
    zonePost(zone, callback) {
      let postBody = zone;
      // verify the required parameter 'zone' is set
      if (zone === undefined || zone === null) {
        throw new Error("Missing the required parameter 'zone' when calling zonePost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ZoneResult;
      return this.apiClient.callApi(
        '/zone', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the zoneZoneKeyDelete operation.
     * @callback module:api/ZoneApi~zoneZoneKeyDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * delete zone
     * Delete a zone. 
     * @param {String} zoneKey the zone key
     * @param {String} checksum the current checksum of the zone to be deleted
     * @param {module:api/ZoneApi~zoneZoneKeyDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    zoneZoneKeyDelete(zoneKey, checksum, callback) {
      let postBody = null;
      // verify the required parameter 'zoneKey' is set
      if (zoneKey === undefined || zoneKey === null) {
        throw new Error("Missing the required parameter 'zoneKey' when calling zoneZoneKeyDelete");
      }
      // verify the required parameter 'checksum' is set
      if (checksum === undefined || checksum === null) {
        throw new Error("Missing the required parameter 'checksum' when calling zoneZoneKeyDelete");
      }

      let pathParams = {
        'zoneKey': zoneKey
      };
      let queryParams = {
        'checksum': checksum
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/zone/{zoneKey}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the zoneZoneKeyGet operation.
     * @callback module:api/ZoneApi~zoneZoneKeyGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ZoneResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get zone
     * Get details for a single zone 
     * @param {String} zoneKey the zone key
     * @param {module:api/ZoneApi~zoneZoneKeyGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ZoneResult}
     */
    zoneZoneKeyGet(zoneKey, callback) {
      let postBody = null;
      // verify the required parameter 'zoneKey' is set
      if (zoneKey === undefined || zoneKey === null) {
        throw new Error("Missing the required parameter 'zoneKey' when calling zoneZoneKeyGet");
      }

      let pathParams = {
        'zoneKey': zoneKey
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ZoneResult;
      return this.apiClient.callApi(
        '/zone/{zoneKey}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
