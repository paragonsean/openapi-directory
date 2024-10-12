/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import NotificationListByServiceDefaultResponse from '../model/NotificationListByServiceDefaultResponse';
import NotificationRecipientUserCreateOrUpdate200Response from '../model/NotificationRecipientUserCreateOrUpdate200Response';
import NotificationRecipientUserListByNotification200Response from '../model/NotificationRecipientUserListByNotification200Response';

/**
* NotificationRecipientUser service.
* @module api/NotificationRecipientUserApi
* @version 2019-01-01
*/
export default class NotificationRecipientUserApi {

    /**
    * Constructs a new NotificationRecipientUserApi. 
    * @alias module:api/NotificationRecipientUserApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the notificationRecipientUserCheckEntityExists operation.
     * @callback module:api/NotificationRecipientUserApi~notificationRecipientUserCheckEntityExistsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Determine if the Notification Recipient User is subscribed to the notification.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} notificationName Notification Name Identifier.
     * @param {String} userId User identifier. Must be unique in the current API Management service instance.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/NotificationRecipientUserApi~notificationRecipientUserCheckEntityExistsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    notificationRecipientUserCheckEntityExists(resourceGroupName, serviceName, notificationName, userId, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling notificationRecipientUserCheckEntityExists");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling notificationRecipientUserCheckEntityExists");
      }
      // verify the required parameter 'notificationName' is set
      if (notificationName === undefined || notificationName === null) {
        throw new Error("Missing the required parameter 'notificationName' when calling notificationRecipientUserCheckEntityExists");
      }
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling notificationRecipientUserCheckEntityExists");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling notificationRecipientUserCheckEntityExists");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling notificationRecipientUserCheckEntityExists");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'notificationName': notificationName,
        'userId': userId,
        'subscriptionId': subscriptionId
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientUsers/{userId}', 'HEAD',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the notificationRecipientUserCreateOrUpdate operation.
     * @callback module:api/NotificationRecipientUserApi~notificationRecipientUserCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NotificationRecipientUserCreateOrUpdate200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Adds the API Management User to the list of Recipients for the Notification.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} notificationName Notification Name Identifier.
     * @param {String} userId User identifier. Must be unique in the current API Management service instance.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/NotificationRecipientUserApi~notificationRecipientUserCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NotificationRecipientUserCreateOrUpdate200Response}
     */
    notificationRecipientUserCreateOrUpdate(resourceGroupName, serviceName, notificationName, userId, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling notificationRecipientUserCreateOrUpdate");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling notificationRecipientUserCreateOrUpdate");
      }
      // verify the required parameter 'notificationName' is set
      if (notificationName === undefined || notificationName === null) {
        throw new Error("Missing the required parameter 'notificationName' when calling notificationRecipientUserCreateOrUpdate");
      }
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling notificationRecipientUserCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling notificationRecipientUserCreateOrUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling notificationRecipientUserCreateOrUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'notificationName': notificationName,
        'userId': userId,
        'subscriptionId': subscriptionId
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
      let returnType = NotificationRecipientUserCreateOrUpdate200Response;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientUsers/{userId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the notificationRecipientUserDelete operation.
     * @callback module:api/NotificationRecipientUserApi~notificationRecipientUserDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes the API Management user from the list of Notification.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} notificationName Notification Name Identifier.
     * @param {String} userId User identifier. Must be unique in the current API Management service instance.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/NotificationRecipientUserApi~notificationRecipientUserDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    notificationRecipientUserDelete(resourceGroupName, serviceName, notificationName, userId, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling notificationRecipientUserDelete");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling notificationRecipientUserDelete");
      }
      // verify the required parameter 'notificationName' is set
      if (notificationName === undefined || notificationName === null) {
        throw new Error("Missing the required parameter 'notificationName' when calling notificationRecipientUserDelete");
      }
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling notificationRecipientUserDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling notificationRecipientUserDelete");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling notificationRecipientUserDelete");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'notificationName': notificationName,
        'userId': userId,
        'subscriptionId': subscriptionId
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientUsers/{userId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the notificationRecipientUserListByNotification operation.
     * @callback module:api/NotificationRecipientUserApi~notificationRecipientUserListByNotificationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NotificationRecipientUserListByNotification200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the list of the Notification Recipient User subscribed to the notification.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} notificationName Notification Name Identifier.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/NotificationRecipientUserApi~notificationRecipientUserListByNotificationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NotificationRecipientUserListByNotification200Response}
     */
    notificationRecipientUserListByNotification(resourceGroupName, serviceName, notificationName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling notificationRecipientUserListByNotification");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling notificationRecipientUserListByNotification");
      }
      // verify the required parameter 'notificationName' is set
      if (notificationName === undefined || notificationName === null) {
        throw new Error("Missing the required parameter 'notificationName' when calling notificationRecipientUserListByNotification");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling notificationRecipientUserListByNotification");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling notificationRecipientUserListByNotification");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'notificationName': notificationName,
        'subscriptionId': subscriptionId
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
      let returnType = NotificationRecipientUserListByNotification200Response;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/notifications/{notificationName}/recipientUsers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
