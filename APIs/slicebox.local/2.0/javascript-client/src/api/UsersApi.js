/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import NewUser from '../model/NewUser';
import User from '../model/User';
import UserInfo from '../model/UserInfo';
import UserPass from '../model/UserPass';

/**
* Users service.
* @module api/UsersApi
* @version 2.0
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
     * Callback function to receive the result of the usersCurrentGet operation.
     * @callback module:api/UsersApi~usersCurrentGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * obtain information on the currently logged in user as specified by the supplied session cookie, IP address and user agent.
     * @param {module:api/UsersApi~usersCurrentGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserInfo}
     */
    usersCurrentGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/octet-stream'];
      let returnType = UserInfo;
      return this.apiClient.callApi(
        '/users/current', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersGet operation.
     * @callback module:api/UsersApi~usersGetCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/User>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns all users of slicebox
     * @param {Object} opts Optional parameters
     * @param {Number} [startindex = 0)] start index of returned slice of users
     * @param {Number} [count = 20)] size of returned slice of users
     * @param {module:api/UsersApi~usersGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/User>}
     */
    usersGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'startindex': opts['startindex'],
        'count': opts['count']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/octet-stream'];
      let returnType = [User];
      return this.apiClient.callApi(
        '/users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersIdDelete operation.
     * @callback module:api/UsersApi~usersIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * deletes a single user based on the ID supplied
     * @param {Number} id ID of user to delete
     * @param {module:api/UsersApi~usersIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersIdDelete(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling usersIdDelete");
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
        '/users/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersLoginPost operation.
     * @callback module:api/UsersApi~usersLoginPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Obtain a session cookie that can be used to authenticate future API calls from the present IP address and with the present user agent.
     * @param {module:model/UserPass} userPass username and password for user logging in
     * @param {module:api/UsersApi~usersLoginPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersLoginPost(userPass, callback) {
      let postBody = userPass;
      // verify the required parameter 'userPass' is set
      if (userPass === undefined || userPass === null) {
        throw new Error("Missing the required parameter 'userPass' when calling usersLoginPost");
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
      let contentTypes = ['application/json', 'application/octet-stream', 'multipart/form-data'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/users/login', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersLogoutPost operation.
     * @callback module:api/UsersApi~usersLogoutPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Logout the current user by responding with a delete cookie header removing the session cookie for this user.
     * @param {module:api/UsersApi~usersLogoutPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    usersLogoutPost(callback) {
      let postBody = null;

      let pathParams = {
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
        '/users/logout', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersPost operation.
     * @callback module:api/UsersApi~usersPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/User} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new user. Dupicates are accepted but not added.
     * @param {module:model/NewUser} user User to add
     * @param {module:api/UsersApi~usersPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/User}
     */
    usersPost(user, callback) {
      let postBody = user;
      // verify the required parameter 'user' is set
      if (user === undefined || user === null) {
        throw new Error("Missing the required parameter 'user' when calling usersPost");
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
      let contentTypes = ['application/json', 'application/octet-stream', 'multipart/form-data'];
      let accepts = ['application/json', 'application/octet-stream'];
      let returnType = User;
      return this.apiClient.callApi(
        '/users', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
