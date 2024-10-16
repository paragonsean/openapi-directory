/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AddNotificationRequestBody from '../model/AddNotificationRequestBody';
import EmptyResponse from '../model/EmptyResponse';
import NotificationCollectionResponse from '../model/NotificationCollectionResponse';
import NotificationResponse from '../model/NotificationResponse';
import UpdateNotificationByIdRequestBody from '../model/UpdateNotificationByIdRequestBody';

/**
* Notifications service.
* @module api/NotificationsApi
* @version 2.0
*/
export default class NotificationsApi {

    /**
    * Constructs a new NotificationsApi. 
    * @alias module:api/NotificationsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addNotification operation.
     * @callback module:api/NotificationsApi~addNotificationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NotificationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new notification
     * Create a new notification for a [resource](#section/Identifying-Resources) in your account. Notifications can be sent via email or webhook;  - To enable email, pass an array of email addresses to the `recipients` parameter of this call.  - To enable webhooks, setup the webhook callback URL in your account settings via [PATCH /account](#operation/updateAccount).   **Notes:**   - Authenticated user should have [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) 
     * @param {String} evApiKey API Key required to make API call. 
     * @param {String} evAccessToken Access token required to make the API call.
     * @param {Object} opts Optional parameters
     * @param {module:model/AddNotificationRequestBody} [addNotificationRequestBody] 
     * @param {module:api/NotificationsApi~addNotificationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NotificationResponse}
     */
    addNotification(evApiKey, evAccessToken, opts, callback) {
      opts = opts || {};
      let postBody = opts['addNotificationRequestBody'];
      // verify the required parameter 'evApiKey' is set
      if (evApiKey === undefined || evApiKey === null) {
        throw new Error("Missing the required parameter 'evApiKey' when calling addNotification");
      }
      // verify the required parameter 'evAccessToken' is set
      if (evAccessToken === undefined || evAccessToken === null) {
        throw new Error("Missing the required parameter 'evAccessToken' when calling addNotification");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'ev-api-key': evApiKey,
        'ev-access-token': evAccessToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = NotificationResponse;
      return this.apiClient.callApi(
        '/notifications', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNotificationById operation.
     * @callback module:api/NotificationsApi~deleteNotificationByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptyResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a notification
     * Deletes a notification. Note that deleting a notification _only_ deletes the notification &ndash; it does not delete any underlying files or folders.  **Notes:**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to update a notification. - You can only delete notifications owned by your user account.
     * @param {String} evApiKey API Key required to make the API call.
     * @param {String} evAccessToken Access token required to make the API call.
     * @param {Number} id ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
     * @param {module:api/NotificationsApi~deleteNotificationByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptyResponse}
     */
    deleteNotificationById(evApiKey, evAccessToken, id, callback) {
      let postBody = null;
      // verify the required parameter 'evApiKey' is set
      if (evApiKey === undefined || evApiKey === null) {
        throw new Error("Missing the required parameter 'evApiKey' when calling deleteNotificationById");
      }
      // verify the required parameter 'evAccessToken' is set
      if (evAccessToken === undefined || evAccessToken === null) {
        throw new Error("Missing the required parameter 'evAccessToken' when calling deleteNotificationById");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteNotificationById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'ev-api-key': evApiKey,
        'ev-access-token': evAccessToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = EmptyResponse;
      return this.apiClient.callApi(
        '/notifications/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNotificationById operation.
     * @callback module:api/NotificationsApi~getNotificationByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NotificationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get notification details
     * Get the details for a notification with a specific ID number. You'll be able to review its path, triggers and who's getting the notification.   **Notes**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to view the detail for a notification. - You can only retrieve notifications owned by your user account.
     * @param {String} evApiKey API Key required to make the API call.
     * @param {String} evAccessToken Access token required to make the API call.
     * @param {Number} id ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
     * @param {Object} opts Optional parameters
     * @param {String} [include] Related record types to include in the response. You can include multiple types by separating them with commas. Valid options are **ownerUser**, **resource**, and **share**.
     * @param {module:api/NotificationsApi~getNotificationByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NotificationResponse}
     */
    getNotificationById(evApiKey, evAccessToken, id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'evApiKey' is set
      if (evApiKey === undefined || evApiKey === null) {
        throw new Error("Missing the required parameter 'evApiKey' when calling getNotificationById");
      }
      // verify the required parameter 'evAccessToken' is set
      if (evAccessToken === undefined || evAccessToken === null) {
        throw new Error("Missing the required parameter 'evAccessToken' when calling getNotificationById");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getNotificationById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'include': opts['include']
      };
      let headerParams = {
        'ev-api-key': evApiKey,
        'ev-access-token': evAccessToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = NotificationResponse;
      return this.apiClient.callApi(
        '/notifications/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listNotifications operation.
     * @callback module:api/NotificationsApi~listNotificationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NotificationCollectionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of notifications
     * Get a list of all the [notifications](/docs/account/06-notifications) you have access to. You can use sorting and filtering to limit the returned list.  **Notes:**   - Authenticated user should have [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions)
     * @param {String} evApiKey API Key required to make the API call. 
     * @param {String} evAccessToken Access token required to make the API call.
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [type] Type of notification include in the list. Valid options are **file**, **folder**, **send_receipt**, **share_receipt**, **file_drop**  If this parameter is not used, only **file** and **folder** type notifications are included in the list.
     * @param {Number} [offset = 0)] Starting notification record in the result set. Can be used for pagination.
     * @param {String} [sort] What order the list of matches should be in. Valid sort fields are **resourcename**, **date**, **action** and **type**. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  You can chose multiple options for the sort by separating them with commmas, such as \"type,-date\" to sort by type, then most recent.
     * @param {Number} [limit = 25)] Number of notification records to return. Can be used for pagination.
     * @param {module:model/String} [include] Related records to include in the response. Valid options are **ownerUser**, **resource**, **share**
     * @param {module:model/String} [action] The kind of action which triggers the notification. Valid choices are **connect** (only for delivery receipts), **download**, **upload**, **delete**, or **all**   **Note** The **all** action matches notifications set to \"all\", not all notifications. For example, notifications set to trigger only on delete are not included if you filter for action=all
     * @param {module:api/NotificationsApi~listNotificationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NotificationCollectionResponse}
     */
    listNotifications(evApiKey, evAccessToken, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'evApiKey' is set
      if (evApiKey === undefined || evApiKey === null) {
        throw new Error("Missing the required parameter 'evApiKey' when calling listNotifications");
      }
      // verify the required parameter 'evAccessToken' is set
      if (evAccessToken === undefined || evAccessToken === null) {
        throw new Error("Missing the required parameter 'evAccessToken' when calling listNotifications");
      }

      let pathParams = {
      };
      let queryParams = {
        'type': opts['type'],
        'offset': opts['offset'],
        'sort': opts['sort'],
        'limit': opts['limit'],
        'include': opts['include'],
        'action': opts['action']
      };
      let headerParams = {
        'ev-api-key': evApiKey,
        'ev-access-token': evAccessToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = NotificationCollectionResponse;
      return this.apiClient.callApi(
        '/notifications', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNotificationById operation.
     * @callback module:api/NotificationsApi~updateNotificationByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NotificationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a notification
     * Update an existing notification. You can add additional emails or change the action or users that cause a notification to trigger.   When updating recipient emails, make sure your `recipients` parameter contains the full list of people who should be included on the notification. If you resend the list without an existing recipient, they will be deleted from the notification emails.   **Notes:**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to update a notification. - You can only change notifications owned by your user account.
     * @param {String} evApiKey API Key required to make the API call.
     * @param {String} evAccessToken Access token required to make the API call.
     * @param {Number} id ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNotificationByIdRequestBody} [updateNotificationByIdRequestBody] 
     * @param {module:api/NotificationsApi~updateNotificationByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NotificationResponse}
     */
    updateNotificationById(evApiKey, evAccessToken, id, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNotificationByIdRequestBody'];
      // verify the required parameter 'evApiKey' is set
      if (evApiKey === undefined || evApiKey === null) {
        throw new Error("Missing the required parameter 'evApiKey' when calling updateNotificationById");
      }
      // verify the required parameter 'evAccessToken' is set
      if (evAccessToken === undefined || evAccessToken === null) {
        throw new Error("Missing the required parameter 'evAccessToken' when calling updateNotificationById");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateNotificationById");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
        'ev-api-key': evApiKey,
        'ev-access-token': evAccessToken
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = NotificationResponse;
      return this.apiClient.callApi(
        '/notifications/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
