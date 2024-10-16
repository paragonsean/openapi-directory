/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import APIModelsApiError from '../model/APIModelsApiError';
import APIPagedResponseBuildSystemSharedDTOJobRun from '../model/APIPagedResponseBuildSystemSharedDTOJobRun';
import BuildSystemSharedDTOJobRun from '../model/BuildSystemSharedDTOJobRun';

/**
* JobRuns service.
* @module api/JobRunsApi
* @version v1
*/
export default class JobRunsApi {

    /**
    * Constructs a new JobRunsApi. 
    * @alias module:api/JobRunsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the jobRunsDeleteJobRun operation.
     * @callback module:api/JobRunsApi~jobRunsDeleteJobRunCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a JobRun
     * Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.
     * @param {Number} jobRunID The id of the JobRun to delete
     * @param {module:api/JobRunsApi~jobRunsDeleteJobRunCallback} callback The callback function, accepting three arguments: error, data, response
     */
    jobRunsDeleteJobRun(jobRunID, callback) {
      let postBody = null;
      // verify the required parameter 'jobRunID' is set
      if (jobRunID === undefined || jobRunID === null) {
        throw new Error("Missing the required parameter 'jobRunID' when calling jobRunsDeleteJobRun");
      }

      let pathParams = {
        'jobRunID': jobRunID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/jobRuns/{jobRunID}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobRunsGetJobRun operation.
     * @callback module:api/JobRunsApi~jobRunsGetJobRunCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BuildSystemSharedDTOJobRun} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a JobRun by ID
     * Gets a JobRun by ID. When successful, the response is the requested JobRun.              If unsuccessful, an appropriate ApiError is returned.
     * @param {Number} jobRunID The ID of the JobRun to get.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [includeActivityRunDetails] Optional. Indicates whether to include ActivityRun details.  Defaults to false.
     * @param {module:api/JobRunsApi~jobRunsGetJobRunCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BuildSystemSharedDTOJobRun}
     */
    jobRunsGetJobRun(jobRunID, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'jobRunID' is set
      if (jobRunID === undefined || jobRunID === null) {
        throw new Error("Missing the required parameter 'jobRunID' when calling jobRunsGetJobRun");
      }

      let pathParams = {
        'jobRunID': jobRunID
      };
      let queryParams = {
        'includeActivityRunDetails': opts['includeActivityRunDetails']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = BuildSystemSharedDTOJobRun;
      return this.apiClient.callApi(
        '/api/v2/jobRuns/{jobRunID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobRunsGetJobRuns operation.
     * @callback module:api/JobRunsApi~jobRunsGetJobRunsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/APIPagedResponseBuildSystemSharedDTOJobRun} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get JobRuns
     * Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.              If unsuccessful, an appropriate ApiError is returned.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Optional. The page limit.  If not specified, the default page limit is 10.
     * @param {Number} [offset] Optional. The page offset.  If not specified, the default page offset is 0.
     * @param {Boolean} [includeActivityRunDetails] Optional. Indicates whether to include ActivityRun details.  Defaults to false.
     * @param {module:api/JobRunsApi~jobRunsGetJobRunsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/APIPagedResponseBuildSystemSharedDTOJobRun}
     */
    jobRunsGetJobRuns(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'includeActivityRunDetails': opts['includeActivityRunDetails']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = APIPagedResponseBuildSystemSharedDTOJobRun;
      return this.apiClient.callApi(
        '/api/v2/jobRuns', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobRunsPostJobRun operation.
     * @callback module:api/JobRunsApi~jobRunsPostJobRunCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a JobRun
     * Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on              creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an               appropriate ApiError is returned.
     * @param {module:model/BuildSystemSharedDTOJobRun} buildSystemSharedDTOJobRun The JobRun to create.  The JobRunID will be assigned on creation of the JobRun.
     * @param {module:api/JobRunsApi~jobRunsPostJobRunCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    jobRunsPostJobRun(buildSystemSharedDTOJobRun, callback) {
      let postBody = buildSystemSharedDTOJobRun;
      // verify the required parameter 'buildSystemSharedDTOJobRun' is set
      if (buildSystemSharedDTOJobRun === undefined || buildSystemSharedDTOJobRun === null) {
        throw new Error("Missing the required parameter 'buildSystemSharedDTOJobRun' when calling jobRunsPostJobRun");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/api/v2/jobRuns', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobRunsPutJobRun operation.
     * @callback module:api/JobRunsApi~jobRunsPutJobRunCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a JobRun
     * ///               Updates a JobRun.  The body of the PUT is the updated JobRun.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
     * @param {Number} jobRunID The id of the JobRun to update
     * @param {module:model/BuildSystemSharedDTOJobRun} buildSystemSharedDTOJobRun The updated JobRun
     * @param {module:api/JobRunsApi~jobRunsPutJobRunCallback} callback The callback function, accepting three arguments: error, data, response
     */
    jobRunsPutJobRun(jobRunID, buildSystemSharedDTOJobRun, callback) {
      let postBody = buildSystemSharedDTOJobRun;
      // verify the required parameter 'jobRunID' is set
      if (jobRunID === undefined || jobRunID === null) {
        throw new Error("Missing the required parameter 'jobRunID' when calling jobRunsPutJobRun");
      }
      // verify the required parameter 'buildSystemSharedDTOJobRun' is set
      if (buildSystemSharedDTOJobRun === undefined || buildSystemSharedDTOJobRun === null) {
        throw new Error("Missing the required parameter 'buildSystemSharedDTOJobRun' when calling jobRunsPutJobRun");
      }

      let pathParams = {
        'jobRunID': jobRunID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/jobRuns/{jobRunID}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
