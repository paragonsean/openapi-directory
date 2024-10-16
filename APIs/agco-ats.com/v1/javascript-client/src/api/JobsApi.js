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
import APIPagedResponseBuildSystemSharedDTOJob from '../model/APIPagedResponseBuildSystemSharedDTOJob';
import BuildSystemSharedDTOJob from '../model/BuildSystemSharedDTOJob';

/**
* Jobs service.
* @module api/JobsApi
* @version v1
*/
export default class JobsApi {

    /**
    * Constructs a new JobsApi. 
    * @alias module:api/JobsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the jobsDeleteJob operation.
     * @callback module:api/JobsApi~jobsDeleteJobCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Mark the delete flag for the Job
     * Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.
     * @param {Number} jobID The id of the job to delete
     * @param {module:api/JobsApi~jobsDeleteJobCallback} callback The callback function, accepting three arguments: error, data, response
     */
    jobsDeleteJob(jobID, callback) {
      let postBody = null;
      // verify the required parameter 'jobID' is set
      if (jobID === undefined || jobID === null) {
        throw new Error("Missing the required parameter 'jobID' when calling jobsDeleteJob");
      }

      let pathParams = {
        'jobID': jobID
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
        '/api/v2/jobs/{jobID}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobsGetJob operation.
     * @callback module:api/JobsApi~jobsGetJobCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BuildSystemSharedDTOJob} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a Job by ID
     * Gets a Job by ID. When successful, the response is the requested Job.              If unsuccessful, an appropriate ApiError is returned.
     * @param {Number} jobID The ID of the Job to get.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [isIncludeDeleted] Does it include deleted job, or not
     * @param {module:api/JobsApi~jobsGetJobCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BuildSystemSharedDTOJob}
     */
    jobsGetJob(jobID, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'jobID' is set
      if (jobID === undefined || jobID === null) {
        throw new Error("Missing the required parameter 'jobID' when calling jobsGetJob");
      }

      let pathParams = {
        'jobID': jobID
      };
      let queryParams = {
        'isIncludeDeleted': opts['isIncludeDeleted']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = BuildSystemSharedDTOJob;
      return this.apiClient.callApi(
        '/api/v2/jobs/{jobID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobsGetJobs operation.
     * @callback module:api/JobsApi~jobsGetJobsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/APIPagedResponseBuildSystemSharedDTOJob} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Jobs
     * Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.              If unsuccessful, an appropriate ApiError is returned.               ///
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Optional. The page limit.  If not specified, the default page limit is 10.
     * @param {Number} [offset] Optional. The page offset.  If not specified, the default page offset is 0.
     * @param {Boolean} [isIncludeDeleted] Does it include deleted job, or not
     * @param {module:api/JobsApi~jobsGetJobsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/APIPagedResponseBuildSystemSharedDTOJob}
     */
    jobsGetJobs(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'isIncludeDeleted': opts['isIncludeDeleted']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = APIPagedResponseBuildSystemSharedDTOJob;
      return this.apiClient.callApi(
        '/api/v2/jobs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobsPostJob operation.
     * @callback module:api/JobsApi~jobsPostJobCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a Job
     * Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on              creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an               appropriate ApiError is returned.
     * @param {module:model/BuildSystemSharedDTOJob} buildSystemSharedDTOJob The job to create.  The JobID will be assigned on creation of the Job.
     * @param {module:api/JobsApi~jobsPostJobCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    jobsPostJob(buildSystemSharedDTOJob, callback) {
      let postBody = buildSystemSharedDTOJob;
      // verify the required parameter 'buildSystemSharedDTOJob' is set
      if (buildSystemSharedDTOJob === undefined || buildSystemSharedDTOJob === null) {
        throw new Error("Missing the required parameter 'buildSystemSharedDTOJob' when calling jobsPostJob");
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
        '/api/v2/jobs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobsPutJob operation.
     * @callback module:api/JobsApi~jobsPutJobCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Job
     * Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.
     * @param {Number} jobID The id of the job to update
     * @param {module:model/BuildSystemSharedDTOJob} buildSystemSharedDTOJob The updated job
     * @param {module:api/JobsApi~jobsPutJobCallback} callback The callback function, accepting three arguments: error, data, response
     */
    jobsPutJob(jobID, buildSystemSharedDTOJob, callback) {
      let postBody = buildSystemSharedDTOJob;
      // verify the required parameter 'jobID' is set
      if (jobID === undefined || jobID === null) {
        throw new Error("Missing the required parameter 'jobID' when calling jobsPutJob");
      }
      // verify the required parameter 'buildSystemSharedDTOJob' is set
      if (buildSystemSharedDTOJob === undefined || buildSystemSharedDTOJob === null) {
        throw new Error("Missing the required parameter 'buildSystemSharedDTOJob' when calling jobsPutJob");
      }

      let pathParams = {
        'jobID': jobID
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
        '/api/v2/jobs/{jobID}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
