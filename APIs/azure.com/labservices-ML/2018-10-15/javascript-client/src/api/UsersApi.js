/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CloudError from '../model/CloudError';
import ResponseWithContinuationUser from '../model/ResponseWithContinuationUser';
import User from '../model/User';
import UserFragment from '../model/UserFragment';

/**
* Users service.
* @module api/UsersApi
* @version 2018-10-15
*/
export default class UsersApi {

    /**
    * Constructs a new UsersApi. 
    * @alias module:api/UsersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the usersCreateOrUpdate operation.
     * @callback module:api/UsersApi~usersCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/User} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create or replace an existing User.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} userName The name of the user.
     * @param {String} apiVersion Client API version.
     * @param {module:model/User} user The User registered to a lab
     * @param {module:api/UsersApi~usersCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/User}
     */
    usersCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user, callback) {
      let postBody = user;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling usersCreateOrUpdate");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling usersCreateOrUpdate");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling usersCreateOrUpdate");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling usersCreateOrUpdate");
      }
      // verify the required parameter 'userName' is set
      if (userName === undefined || userName === null) {
        throw new Error("Missing the required parameter 'userName' when calling usersCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling usersCreateOrUpdate");
      }
      // verify the required parameter 'user' is set
      if (user === undefined || user === null) {
        throw new Error("Missing the required parameter 'user' when calling usersCreateOrUpdate");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'userName': userName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = User;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersDelete operation.
     * @callback module:api/UsersApi~usersDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete user. This operation can take a while to complete
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} userName The name of the user.
     * @param {String} apiVersion Client API version.
     * @param {module:api/UsersApi~usersDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersDelete(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling usersDelete");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling usersDelete");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling usersDelete");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling usersDelete");
      }
      // verify the required parameter 'userName' is set
      if (userName === undefined || userName === null) {
        throw new Error("Missing the required parameter 'userName' when calling usersDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling usersDelete");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'userName': userName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersGet operation.
     * @callback module:api/UsersApi~usersGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/User} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get user
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} userName The name of the user.
     * @param {String} apiVersion Client API version.
     * @param {Object} opts Optional parameters
     * @param {String} [expand] Specify the $expand query. Example: 'properties($select=email)'
     * @param {module:api/UsersApi~usersGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/User}
     */
    usersGet(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling usersGet");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling usersGet");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling usersGet");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling usersGet");
      }
      // verify the required parameter 'userName' is set
      if (userName === undefined || userName === null) {
        throw new Error("Missing the required parameter 'userName' when calling usersGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling usersGet");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'userName': userName
      };
      let queryParams = {
        '$expand': opts['expand'],
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = User;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersList operation.
     * @callback module:api/UsersApi~usersListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ResponseWithContinuationUser} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List users in a given lab.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} apiVersion Client API version.
     * @param {Object} opts Optional parameters
     * @param {String} [expand] Specify the $expand query. Example: 'properties($select=email)'
     * @param {String} [filter] The filter to apply to the operation.
     * @param {Number} [top] The maximum number of resources to return from the operation.
     * @param {String} [orderby] The ordering expression for the results, using OData notation.
     * @param {module:api/UsersApi~usersListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ResponseWithContinuationUser}
     */
    usersList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling usersList");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling usersList");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling usersList");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling usersList");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling usersList");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName
      };
      let queryParams = {
        '$expand': opts['expand'],
        '$filter': opts['filter'],
        '$top': opts['top'],
        '$orderby': opts['orderby'],
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ResponseWithContinuationUser;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUpdate operation.
     * @callback module:api/UsersApi~usersUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/User} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify properties of users.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} userName The name of the user.
     * @param {String} apiVersion Client API version.
     * @param {module:model/UserFragment} user The User registered to a lab
     * @param {module:api/UsersApi~usersUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/User}
     */
    usersUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user, callback) {
      let postBody = user;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling usersUpdate");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling usersUpdate");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling usersUpdate");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling usersUpdate");
      }
      // verify the required parameter 'userName' is set
      if (userName === undefined || userName === null) {
        throw new Error("Missing the required parameter 'userName' when calling usersUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling usersUpdate");
      }
      // verify the required parameter 'user' is set
      if (user === undefined || user === null) {
        throw new Error("Missing the required parameter 'user' when calling usersUpdate");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'userName': userName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = User;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
