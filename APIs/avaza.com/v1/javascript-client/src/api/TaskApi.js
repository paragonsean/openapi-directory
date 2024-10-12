/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
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
import NewTask from '../model/NewTask';
import TaskDetails from '../model/TaskDetails';
import TaskDropdownList from '../model/TaskDropdownList';
import TaskList from '../model/TaskList';
import UpdateTask from '../model/UpdateTask';

/**
* Task service.
* @module api/TaskApi
* @version v1
*/
export default class TaskApi {

    /**
    * Constructs a new TaskApi. 
    * @alias module:api/TaskApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the taskDelete operation.
     * @callback module:api/TaskApi~taskDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Task
     * @param {Number} taskID 
     * @param {module:api/TaskApi~taskDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    taskDelete(taskID, callback) {
      let postBody = null;
      // verify the required parameter 'taskID' is set
      if (taskID === undefined || taskID === null) {
        throw new Error("Missing the required parameter 'taskID' when calling taskDelete");
      }

      let pathParams = {
      };
      let queryParams = {
        'TaskID': taskID
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/api/Task', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskGet operation.
     * @callback module:api/TaskApi~taskGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets list of Tasks
     * @param {Object} opts Optional parameters
     * @param {Date} [updatedAfter] Optional filter to records updated after a specific date.
     * @param {Number} [pageSize] Number of items per page. Defaults to 20.
     * @param {Number} [pageNumber] Page to display. Starts from 1. Defaults to 1
     * @param {String} [sort] Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\", \"SectionTitle\", \"Title\"
     * @param {Boolean} [isComplete] Optional filter to only display tasks linked to a Task Status where isComplete=false, or where isComplete=true
     * @param {Number} [projectID] Optional filter to only display tasks belonging to a specific ProjectID
     * @param {module:api/TaskApi~taskGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskList}
     */
    taskGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'UpdatedAfter': opts['updatedAfter'],
        'pageSize': opts['pageSize'],
        'pageNumber': opts['pageNumber'],
        'Sort': opts['sort'],
        'isComplete': opts['isComplete'],
        'ProjectID': opts['projectID']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TaskList;
      return this.apiClient.callApi(
        '/api/Task', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskGetByID operation.
     * @callback module:api/TaskApi~taskGetByIDCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets Task by Task ID
     * @param {Number} id Task ID number
     * @param {module:api/TaskApi~taskGetByIDCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskDetails}
     */
    taskGetByID(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskGetByID");
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

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TaskDetails;
      return this.apiClient.callApi(
        '/api/Task/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskLookup operation.
     * @callback module:api/TaskApi~taskLookupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskDropdownList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets minimal list of Tasks for the current user
     * Groups Tasks by Section. Default sort is by Section Title followed by Task Title
     * @param {Number} projectID (required) The ProjectID to use when filtering Tasks
     * @param {Object} opts Optional parameters
     * @param {Number} [pageSize] Number of items per page (max 1000)
     * @param {Number} [pageNumber] Page to display. Starts from 1.
     * @param {Boolean} [hideCompleted] (optional) true/false to hide completed tasks. Defaults false
     * @param {String} [search] (optional) Search string to match against Task title. Performs begins-with match
     * @param {module:api/TaskApi~taskLookupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskDropdownList}
     */
    taskLookup(projectID, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectID' is set
      if (projectID === undefined || projectID === null) {
        throw new Error("Missing the required parameter 'projectID' when calling taskLookup");
      }

      let pathParams = {
      };
      let queryParams = {
        'projectID': projectID,
        'pageSize': opts['pageSize'],
        'pageNumber': opts['pageNumber'],
        'hideCompleted': opts['hideCompleted'],
        'search': opts['search']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TaskDropdownList;
      return this.apiClient.callApi(
        '/api/Task/Lookup', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskPost operation.
     * @callback module:api/TaskApi~taskPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a Task
     * @param {module:model/NewTask} model 
     * @param {module:api/TaskApi~taskPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskDetails}
     */
    taskPost(model, callback) {
      let postBody = model;
      // verify the required parameter 'model' is set
      if (model === undefined || model === null) {
        throw new Error("Missing the required parameter 'model' when calling taskPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TaskDetails;
      return this.apiClient.callApi(
        '/api/Task', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskPut operation.
     * @callback module:api/TaskApi~taskPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Task.
     * Requires TaskID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.
     * @param {module:model/UpdateTask} model 
     * @param {module:api/TaskApi~taskPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskDetails}
     */
    taskPut(model, callback) {
      let postBody = model;
      // verify the required parameter 'model' is set
      if (model === undefined || model === null) {
        throw new Error("Missing the required parameter 'model' when calling taskPut");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = TaskDetails;
      return this.apiClient.callApi(
        '/api/Task', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
