/**
 * import.io
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
import APIError from '../model/APIError';
import Schedule from '../model/Schedule';
import ScheduleRequest from '../model/ScheduleRequest';

/**
* ScheduleImportIo service.
* @module api/ScheduleImportIoApi
* @version 1.0
*/
export default class ScheduleImportIoApi {

    /**
    * Constructs a new ScheduleImportIoApi. 
    * @alias module:api/ScheduleImportIoApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the extractorExtractorIdDelete operation.
     * @callback module:api/ScheduleImportIoApi~extractorExtractorIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing schedule
     * @param {String} extractorId the id of the extractor with a schedule
     * @param {module:api/ScheduleImportIoApi~extractorExtractorIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    extractorExtractorIdDelete(extractorId, callback) {
      let postBody = null;
      // verify the required parameter 'extractorId' is set
      if (extractorId === undefined || extractorId === null) {
        throw new Error("Missing the required parameter 'extractorId' when calling extractorExtractorIdDelete");
      }

      let pathParams = {
        'extractorId': extractorId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json;charset=UTF-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/extractor/{extractorId}/', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the extractorExtractorIdGet operation.
     * @callback module:api/ScheduleImportIoApi~extractorExtractorIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Schedule} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the schedule of a particular extractor
     * @param {String} extractorId the id of the extractor with a schedule
     * @param {module:api/ScheduleImportIoApi~extractorExtractorIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Schedule}
     */
    extractorExtractorIdGet(extractorId, callback) {
      let postBody = null;
      // verify the required parameter 'extractorId' is set
      if (extractorId === undefined || extractorId === null) {
        throw new Error("Missing the required parameter 'extractorId' when calling extractorExtractorIdGet");
      }

      let pathParams = {
        'extractorId': extractorId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json;charset=UTF-8'];
      let returnType = Schedule;
      return this.apiClient.callApi(
        '/extractor/{extractorId}/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the extractorGet operation.
     * @callback module:api/ScheduleImportIoApi~extractorGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Schedule} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the list of schedules for all your extractors
     * @param {module:api/ScheduleImportIoApi~extractorGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Schedule}
     */
    extractorGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json;charset=UTF-8'];
      let returnType = Schedule;
      return this.apiClient.callApi(
        '/extractor', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the extractorPost operation.
     * @callback module:api/ScheduleImportIoApi~extractorPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Schedule} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Schedule and extractor to run at a specific time
     * @param {module:model/ScheduleRequest} scheduleRequestBody Request body with the schema defined on the left. Interval is a cron string.
     * @param {module:api/ScheduleImportIoApi~extractorPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Schedule}
     */
    extractorPost(scheduleRequestBody, callback) {
      let postBody = scheduleRequestBody;
      // verify the required parameter 'scheduleRequestBody' is set
      if (scheduleRequestBody === undefined || scheduleRequestBody === null) {
        throw new Error("Missing the required parameter 'scheduleRequestBody' when calling extractorPost");
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
      let accepts = ['application/json;charset=UTF-8'];
      let returnType = Schedule;
      return this.apiClient.callApi(
        '/extractor', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
