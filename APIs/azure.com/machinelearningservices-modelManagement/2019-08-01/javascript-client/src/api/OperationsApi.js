/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AsyncOperationStatus from '../model/AsyncOperationStatus';
import ModelErrorResponse from '../model/ModelErrorResponse';

/**
* Operations service.
* @module api/OperationsApi
* @version 2019-08-01
*/
export default class OperationsApi {

    /**
    * Constructs a new OperationsApi. 
    * @alias module:api/OperationsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the operationsGet operation.
     * @callback module:api/OperationsApi~operationsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AsyncOperationStatus} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the status of an async operation.
     * Get the status of an async operation by operation id.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {String} id The operation id.
     * @param {module:api/OperationsApi~operationsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AsyncOperationStatus}
     */
    operationsGet(subscriptionId, resourceGroup, workspace, id, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling operationsGet");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling operationsGet");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling operationsGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling operationsGet");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AsyncOperationStatus;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/operations/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
