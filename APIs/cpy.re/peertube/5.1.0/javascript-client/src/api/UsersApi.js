/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AddUser from '../model/AddUser';
import AddUserResponse from '../model/AddUserResponse';
import ConfirmTwoFactorRequestRequest from '../model/ConfirmTwoFactorRequestRequest';
import DisableTwoFactorRequest from '../model/DisableTwoFactorRequest';
import GetUser200Response from '../model/GetUser200Response';
import RequestTwoFactorResponse from '../model/RequestTwoFactorResponse';
import ResendEmailToVerifyUserRequest from '../model/ResendEmailToVerifyUserRequest';
import UpdateUser from '../model/UpdateUser';
import User from '../model/User';
import VerifyUserRequest from '../model/VerifyUserRequest';

/**
* Users service.
* @module api/UsersApi
* @version 5.1.0
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
     * Callback function to receive the result of the addUser operation.
     * @callback module:api/UsersApi~addUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AddUserResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a user
     * @param {module:model/AddUser} addUser If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first. 
     * @param {module:api/UsersApi~addUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AddUserResponse}
     */
    addUser(addUser, callback) {
      let postBody = addUser;
      // verify the required parameter 'addUser' is set
      if (addUser === undefined || addUser === null) {
        throw new Error("Missing the required parameter 'addUser' when calling addUser");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AddUserResponse;
      return this.apiClient.callApi(
        '/api/v1/users', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the confirmTwoFactorRequest operation.
     * @callback module:api/UsersApi~confirmTwoFactorRequestCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Confirm two factor auth
     * Confirm a two factor authentication request
     * @param {Number} id Entity id
     * @param {Object} opts Optional parameters
     * @param {module:model/ConfirmTwoFactorRequestRequest} [confirmTwoFactorRequestRequest] 
     * @param {module:api/UsersApi~confirmTwoFactorRequestCallback} callback The callback function, accepting three arguments: error, data, response
     */
    confirmTwoFactorRequest(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['confirmTwoFactorRequestRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling confirmTwoFactorRequest");
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
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/{id}/two-factor/confirm-request', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the delUser operation.
     * @callback module:api/UsersApi~delUserCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a user
     * @param {Number} id Entity id
     * @param {module:api/UsersApi~delUserCallback} callback The callback function, accepting three arguments: error, data, response
     */
    delUser(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling delUser");
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

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the disableTwoFactor operation.
     * @callback module:api/UsersApi~disableTwoFactorCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disable two factor auth
     * Disable two factor authentication of a user
     * @param {Number} id Entity id
     * @param {Object} opts Optional parameters
     * @param {module:model/DisableTwoFactorRequest} [disableTwoFactorRequest] 
     * @param {module:api/UsersApi~disableTwoFactorCallback} callback The callback function, accepting three arguments: error, data, response
     */
    disableTwoFactor(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['disableTwoFactorRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling disableTwoFactor");
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
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/{id}/two-factor/disable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUser operation.
     * @callback module:api/UsersApi~getUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetUser200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a user
     * @param {Number} id Entity id
     * @param {Object} opts Optional parameters
     * @param {Boolean} [withStats] include statistics about the user (only available as a moderator/admin)
     * @param {module:api/UsersApi~getUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetUser200Response}
     */
    getUser(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getUser");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'withStats': opts['withStats']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetUser200Response;
      return this.apiClient.callApi(
        '/api/v1/users/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUsers operation.
     * @callback module:api/UsersApi~getUsersCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/User>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List users
     * @param {Object} opts Optional parameters
     * @param {String} [search] Plain text search that will match with user usernames or emails
     * @param {Boolean} [blocked] Filter results down to (un)banned users
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:model/String} [sort] Sort users by criteria
     * @param {module:api/UsersApi~getUsersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/User>}
     */
    getUsers(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'search': opts['search'],
        'blocked': opts['blocked'],
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [User];
      return this.apiClient.callApi(
        '/api/v1/users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putUser operation.
     * @callback module:api/UsersApi~putUserCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a user
     * @param {Number} id Entity id
     * @param {module:model/UpdateUser} updateUser 
     * @param {module:api/UsersApi~putUserCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putUser(id, updateUser, callback) {
      let postBody = updateUser;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putUser");
      }
      // verify the required parameter 'updateUser' is set
      if (updateUser === undefined || updateUser === null) {
        throw new Error("Missing the required parameter 'updateUser' when calling putUser");
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

      let authNames = ['OAuth2'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestTwoFactor operation.
     * @callback module:api/UsersApi~requestTwoFactorCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/RequestTwoFactorResponse>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request two factor auth
     * Request two factor authentication for a user
     * @param {Number} id Entity id
     * @param {Object} opts Optional parameters
     * @param {module:model/DisableTwoFactorRequest} [disableTwoFactorRequest] 
     * @param {module:api/UsersApi~requestTwoFactorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/RequestTwoFactorResponse>}
     */
    requestTwoFactor(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['disableTwoFactorRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling requestTwoFactor");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = [RequestTwoFactorResponse];
      return this.apiClient.callApi(
        '/api/v1/users/{id}/two-factor/request', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resendEmailToVerifyUser operation.
     * @callback module:api/UsersApi~resendEmailToVerifyUserCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Resend user verification link
     * @param {Object} opts Optional parameters
     * @param {module:model/ResendEmailToVerifyUserRequest} [resendEmailToVerifyUserRequest] 
     * @param {module:api/UsersApi~resendEmailToVerifyUserCallback} callback The callback function, accepting three arguments: error, data, response
     */
    resendEmailToVerifyUser(opts, callback) {
      opts = opts || {};
      let postBody = opts['resendEmailToVerifyUserRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/ask-send-verify-email', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the verifyUser operation.
     * @callback module:api/UsersApi~verifyUserCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Verify a user
     * Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 
     * @param {Number} id Entity id
     * @param {Object} opts Optional parameters
     * @param {module:model/VerifyUserRequest} [verifyUserRequest] 
     * @param {module:api/UsersApi~verifyUserCallback} callback The callback function, accepting three arguments: error, data, response
     */
    verifyUser(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['verifyUserRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling verifyUser");
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
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/{id}/verify-email', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
