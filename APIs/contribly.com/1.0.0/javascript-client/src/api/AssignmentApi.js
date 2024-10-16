/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Assignment from '../model/Assignment';
import AssignmentSubmission from '../model/AssignmentSubmission';
import ErrorResponse from '../model/ErrorResponse';

/**
* Assignment service.
* @module api/AssignmentApi
* @version 1.0.0
*/
export default class AssignmentApi {

    /**
    * Constructs a new AssignmentApi. 
    * @alias module:api/AssignmentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the assignmentsGet operation.
     * @callback module:api/AssignmentApi~assignmentsGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Assignment>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List assignments
     * @param {Object} opts Optional parameters
     * @param {String} [ownedBy] Restrict results to assignments owned by this user.
     * @param {Number} [page] Pagination page
     * @param {Number} [pageSize] Pagination page size
     * @param {String} [q] Restrict results to assignments whose name or description matches this keyword.
     * @param {String} [urlWords] Select an assignment by urlWords.
     * @param {Boolean} [open] Select open or closed assignments
     * @param {Boolean} [alwaysOpen] Select assignments with no closing date.
     * @param {String} [tag] Restrict results to assignments which are tagged with this tag.
     * @param {String} [name] Restrict results to the assignment (or potentially assignments) with this exact name
     * @param {module:api/AssignmentApi~assignmentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Assignment>}
     */
    assignmentsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'ownedBy': opts['ownedBy'],
        'page': opts['page'],
        'pageSize': opts['pageSize'],
        'q': opts['q'],
        'urlWords': opts['urlWords'],
        'open': opts['open'],
        'alwaysOpen': opts['alwaysOpen'],
        'tag': opts['tag'],
        'name': opts['name']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Assignment];
      return this.apiClient.callApi(
        '/assignments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the assignmentsIdDelete operation.
     * @callback module:api/AssignmentApi~assignmentsIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete this assignment and all of it's contributions
     * @param {String} id Id of the assignment to return
     * @param {module:api/AssignmentApi~assignmentsIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    assignmentsIdDelete(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling assignmentsIdDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/assignments/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the assignmentsIdGet operation.
     * @callback module:api/AssignmentApi~assignmentsIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Assignment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a single assigment by id
     * @param {String} id Id of the assignment to return
     * @param {module:api/AssignmentApi~assignmentsIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Assignment}
     */
    assignmentsIdGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling assignmentsIdGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Assignment;
      return this.apiClient.callApi(
        '/assignments/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the assignmentsPost operation.
     * @callback module:api/AssignmentApi~assignmentsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Assignment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new assignment
     * @param {module:model/AssignmentSubmission} assignmentSubmission Assignment object to be created
     * @param {module:api/AssignmentApi~assignmentsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Assignment}
     */
    assignmentsPost(assignmentSubmission, callback) {
      let postBody = assignmentSubmission;
      // verify the required parameter 'assignmentSubmission' is set
      if (assignmentSubmission === undefined || assignmentSubmission === null) {
        throw new Error("Missing the required parameter 'assignmentSubmission' when calling assignmentsPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Assignment;
      return this.apiClient.callApi(
        '/assignments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
