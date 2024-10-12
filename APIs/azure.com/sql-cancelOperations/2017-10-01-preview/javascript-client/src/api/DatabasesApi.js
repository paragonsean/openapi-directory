/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import DatabaseOperationListResult from '../model/DatabaseOperationListResult';

/**
* Databases service.
* @module api/DatabasesApi
* @version 2017-10-01-preview
*/
export default class DatabasesApi {

    /**
    * Constructs a new DatabasesApi. 
    * @alias module:api/DatabasesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the databaseOperationsCancel operation.
     * @callback module:api/DatabasesApi~databaseOperationsCancelCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cancels the asynchronous operation on the database.
     * @param {String} resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
     * @param {String} serverName The name of the server.
     * @param {String} databaseName The name of the database.
     * @param {String} operationId The operation identifier.
     * @param {String} subscriptionId The subscription ID that identifies an Azure subscription.
     * @param {String} apiVersion The API version to use for the request.
     * @param {module:api/DatabasesApi~databaseOperationsCancelCallback} callback The callback function, accepting three arguments: error, data, response
     */
    databaseOperationsCancel(resourceGroupName, serverName, databaseName, operationId, subscriptionId, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling databaseOperationsCancel");
      }
      // verify the required parameter 'serverName' is set
      if (serverName === undefined || serverName === null) {
        throw new Error("Missing the required parameter 'serverName' when calling databaseOperationsCancel");
      }
      // verify the required parameter 'databaseName' is set
      if (databaseName === undefined || databaseName === null) {
        throw new Error("Missing the required parameter 'databaseName' when calling databaseOperationsCancel");
      }
      // verify the required parameter 'operationId' is set
      if (operationId === undefined || operationId === null) {
        throw new Error("Missing the required parameter 'operationId' when calling databaseOperationsCancel");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling databaseOperationsCancel");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling databaseOperationsCancel");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serverName': serverName,
        'databaseName': databaseName,
        'operationId': operationId,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/operations/{operationId}/cancel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the databaseOperationsListByDatabase operation.
     * @callback module:api/DatabasesApi~databaseOperationsListByDatabaseCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseOperationListResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a list of operations performed on the database.
     * @param {String} resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
     * @param {String} serverName The name of the server.
     * @param {String} databaseName The name of the database.
     * @param {String} subscriptionId The subscription ID that identifies an Azure subscription.
     * @param {String} apiVersion The API version to use for the request.
     * @param {module:api/DatabasesApi~databaseOperationsListByDatabaseCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseOperationListResult}
     */
    databaseOperationsListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling databaseOperationsListByDatabase");
      }
      // verify the required parameter 'serverName' is set
      if (serverName === undefined || serverName === null) {
        throw new Error("Missing the required parameter 'serverName' when calling databaseOperationsListByDatabase");
      }
      // verify the required parameter 'databaseName' is set
      if (databaseName === undefined || databaseName === null) {
        throw new Error("Missing the required parameter 'databaseName' when calling databaseOperationsListByDatabase");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling databaseOperationsListByDatabase");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling databaseOperationsListByDatabase");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serverName': serverName,
        'databaseName': databaseName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DatabaseOperationListResult;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/operations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
