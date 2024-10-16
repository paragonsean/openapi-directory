/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ContactListPage from '../model/ContactListPage';
import ContactListUpdate from '../model/ContactListUpdate';
import ContactsGet401ResponseInner from '../model/ContactsGet401ResponseInner';
import ContactsGet404ResponseInner from '../model/ContactsGet404ResponseInner';
import ContactsGet422ResponseInner from '../model/ContactsGet422ResponseInner';
import NewId from '../model/NewId';

/**
* Lists service.
* @module api/ListsApi
* @version 0.9
*/
export default class ListsApi {

    /**
    * Constructs a new ListsApi. 
    * @alias module:api/ListsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the contactsListsGet operation.
     * @callback module:api/ListsApi~contactsListsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContactListPage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a paged result of contact lists.
     * @param {Object} opts Optional parameters
     * @param {Number} [offset] Skip that many records
     * @param {Number} [limit] Maximum number of items in page
     * @param {String} [sort] Property to sort by. Append '-' for descending order.
     * @param {module:api/ListsApi~contactsListsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContactListPage}
     */
    contactsListsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['mqApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ContactListPage;
      return this.apiClient.callApi(
        '/contacts/lists', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsListsListidDelete operation.
     * @callback module:api/ListsApi~contactsListsListidDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing contact list
     * @param {String} listid Unique 16 characters ID of the contact list
     * @param {module:api/ListsApi~contactsListsListidDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contactsListsListidDelete(listid, callback) {
      let postBody = null;
      // verify the required parameter 'listid' is set
      if (listid === undefined || listid === null) {
        throw new Error("Missing the required parameter 'listid' when calling contactsListsListidDelete");
      }

      let pathParams = {
        'listid': listid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['mqApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/contacts/lists/{listid}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsListsListidPut operation.
     * @callback module:api/ListsApi~contactsListsListidPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing contact list
     * @param {String} listid Unique 16 characters ID of the contact list
     * @param {Object} opts Optional parameters
     * @param {module:model/ContactListUpdate} [contactlist] Contact list properties to update
     * @param {module:api/ListsApi~contactsListsListidPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contactsListsListidPut(listid, opts, callback) {
      opts = opts || {};
      let postBody = opts['contactlist'];
      // verify the required parameter 'listid' is set
      if (listid === undefined || listid === null) {
        throw new Error("Missing the required parameter 'listid' when calling contactsListsListidPut");
      }

      let pathParams = {
        'listid': listid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['mqApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/contacts/lists/{listid}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsListsPost operation.
     * @callback module:api/ListsApi~contactsListsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/NewId} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a new contact list
     * @param {Object} opts Optional parameters
     * @param {module:model/ContactListUpdate} [contactlist] Contact list initial properties
     * @param {module:api/ListsApi~contactsListsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/NewId}
     */
    contactsListsPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['contactlist'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['mqApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = NewId;
      return this.apiClient.callApi(
        '/contacts/lists', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
