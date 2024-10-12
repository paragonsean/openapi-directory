/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AddWorkflowRequest from '../model/AddWorkflowRequest';
import ErrorResponse from '../model/ErrorResponse';
import GetAllWorkflowsResponse from '../model/GetAllWorkflowsResponse';
import SetWorkflowRequest from '../model/SetWorkflowRequest';

/**
* Workflows service.
* @module api/WorkflowsApi
* @version 0.4.0
*/
export default class WorkflowsApi {

    /**
    * Constructs a new WorkflowsApi. 
    * @alias module:api/WorkflowsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addWorkflow operation.
     * @callback module:api/WorkflowsApi~addWorkflowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Setup workflow
     * 
     * @param {module:model/AddWorkflowRequest} addWorkflowRequest Workflow body
     * @param {module:api/WorkflowsApi~addWorkflowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addWorkflow(addWorkflowRequest, callback) {
      let postBody = addWorkflowRequest;
      // verify the required parameter 'addWorkflowRequest' is set
      if (addWorkflowRequest === undefined || addWorkflowRequest === null) {
        throw new Error("Missing the required parameter 'addWorkflowRequest' when calling addWorkflow");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearerAuth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/workflows', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteWorkflow operation.
     * @callback module:api/WorkflowsApi~deleteWorkflowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a workflow
     * @param {String} workflow ID of the workflow
     * @param {module:api/WorkflowsApi~deleteWorkflowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteWorkflow(workflow, callback) {
      let postBody = null;
      // verify the required parameter 'workflow' is set
      if (workflow === undefined || workflow === null) {
        throw new Error("Missing the required parameter 'workflow' when calling deleteWorkflow");
      }

      let pathParams = {
        'workflow': workflow
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/workflows/{workflow}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAllWorkflows operation.
     * @callback module:api/WorkflowsApi~getAllWorkflowsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAllWorkflowsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all workflows you have access to
     * 
     * @param {module:api/WorkflowsApi~getAllWorkflowsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAllWorkflowsResponse}
     */
    getAllWorkflows(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearerAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetAllWorkflowsResponse;
      return this.apiClient.callApi(
        '/workflows', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setWorkflow operation.
     * @callback module:api/WorkflowsApi~setWorkflowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set a property on a workflow
     * @param {module:model/SetWorkflowRequest} setWorkflowRequest Set Workflow body
     * @param {module:api/WorkflowsApi~setWorkflowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    setWorkflow(setWorkflowRequest, callback) {
      let postBody = setWorkflowRequest;
      // verify the required parameter 'setWorkflowRequest' is set
      if (setWorkflowRequest === undefined || setWorkflowRequest === null) {
        throw new Error("Missing the required parameter 'setWorkflowRequest' when calling setWorkflow");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearerAuth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/workflows/set', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateWorkflow operation.
     * @callback module:api/WorkflowsApi~updateWorkflowCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an workflow
     * @param {String} workflow ID of the workflow
     * @param {module:model/AddWorkflowRequest} addWorkflowRequest Workflow body
     * @param {module:api/WorkflowsApi~updateWorkflowCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateWorkflow(workflow, addWorkflowRequest, callback) {
      let postBody = addWorkflowRequest;
      // verify the required parameter 'workflow' is set
      if (workflow === undefined || workflow === null) {
        throw new Error("Missing the required parameter 'workflow' when calling updateWorkflow");
      }
      // verify the required parameter 'addWorkflowRequest' is set
      if (addWorkflowRequest === undefined || addWorkflowRequest === null) {
        throw new Error("Missing the required parameter 'addWorkflowRequest' when calling updateWorkflow");
      }

      let pathParams = {
        'workflow': workflow
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['bearerAuth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/workflows/{workflow}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
