/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import HeartbeatResponse from '../model/HeartbeatResponse';

/**
* Monitoring service.
* @module api/MonitoringApi
* @version 0.5
*/
export default class MonitoringApi {

    /**
    * Constructs a new MonitoringApi. 
    * @alias module:api/MonitoringApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v05HeartbeatGet operation.
     * @callback module:api/MonitoringApi~v05HeartbeatGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/HeartbeatResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get consent request status
     * @param {module:api/MonitoringApi~v05HeartbeatGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/HeartbeatResponse}
     */
    v05HeartbeatGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = HeartbeatResponse;
      return this.apiClient.callApi(
        '/v0.5/heartbeat', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
