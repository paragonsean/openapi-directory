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
import ContactPage from '../model/ContactPage';
import ContactUpdate from '../model/ContactUpdate';
import ContactsGet401ResponseInner from '../model/ContactsGet401ResponseInner';
import ContactsGet404ResponseInner from '../model/ContactsGet404ResponseInner';
import ContactsGet422ResponseInner from '../model/ContactsGet422ResponseInner';

/**
* Contacts service.
* @module api/ContactsApi
* @version 0.9
*/
export default class ContactsApi {

    /**
    * Constructs a new ContactsApi. 
    * @alias module:api/ContactsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the contactsContactidDelete operation.
     * @callback module:api/ContactsApi~contactsContactidDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing contact
     * @param {String} contactid Unique 16 characters ID of the contact
     * @param {module:api/ContactsApi~contactsContactidDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contactsContactidDelete(contactid, callback) {
      let postBody = null;
      // verify the required parameter 'contactid' is set
      if (contactid === undefined || contactid === null) {
        throw new Error("Missing the required parameter 'contactid' when calling contactsContactidDelete");
      }

      let pathParams = {
        'contactid': contactid
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
        '/contacts/{contactid}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsContactidPut operation.
     * @callback module:api/ContactsApi~contactsContactidPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing contact
     * @param {String} contactid Unique 16 characters ID of the contact
     * @param {module:model/ContactUpdate} contact Contact properties to update
     * @param {module:api/ContactsApi~contactsContactidPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contactsContactidPut(contactid, contact, callback) {
      let postBody = contact;
      // verify the required parameter 'contactid' is set
      if (contactid === undefined || contactid === null) {
        throw new Error("Missing the required parameter 'contactid' when calling contactsContactidPut");
      }
      // verify the required parameter 'contact' is set
      if (contact === undefined || contact === null) {
        throw new Error("Missing the required parameter 'contact' when calling contactsContactidPut");
      }

      let pathParams = {
        'contactid': contactid
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
        '/contacts/{contactid}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsGet operation.
     * @callback module:api/ContactsApi~contactsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContactPage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a paged result of contacts from a list
     * @param {Object} opts Optional parameters
     * @param {String} [listid] Unique 16 characters ID of the contact list to get contacts of
     * @param {Number} [offset] Skip that many records
     * @param {Number} [limit] Maximum number of items in page
     * @param {String} [sort] Property to sort by. Append '-' for descending order.
     * @param {module:api/ContactsApi~contactsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContactPage}
     */
    contactsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'listid': opts['listid'],
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
      let returnType = ContactPage;
      return this.apiClient.callApi(
        '/contacts', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
