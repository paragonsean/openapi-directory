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
import ListRegistrations200Response from '../model/ListRegistrations200Response';
import RegisterUser from '../model/RegisterUser';
import ResendEmailToVerifyRegistrationRequest from '../model/ResendEmailToVerifyRegistrationRequest';
import ResendEmailToVerifyUserRequest from '../model/ResendEmailToVerifyUserRequest';
import UserRegistration from '../model/UserRegistration';
import UserRegistrationAcceptOrReject from '../model/UserRegistrationAcceptOrReject';
import UserRegistrationRequest from '../model/UserRegistrationRequest';
import VerifyRegistrationEmailRequest from '../model/VerifyRegistrationEmailRequest';
import VerifyUserRequest from '../model/VerifyUserRequest';

/**
* Register service.
* @module api/RegisterApi
* @version 5.1.0
*/
export default class RegisterApi {

    /**
    * Constructs a new RegisterApi. 
    * @alias module:api/RegisterApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the acceptRegistration operation.
     * @callback module:api/RegisterApi~acceptRegistrationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Accept registration
     * @param {Number} registrationId Registration ID
     * @param {Object} opts Optional parameters
     * @param {module:model/UserRegistrationAcceptOrReject} [userRegistrationAcceptOrReject] 
     * @param {module:api/RegisterApi~acceptRegistrationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    acceptRegistration(registrationId, opts, callback) {
      opts = opts || {};
      let postBody = opts['userRegistrationAcceptOrReject'];
      // verify the required parameter 'registrationId' is set
      if (registrationId === undefined || registrationId === null) {
        throw new Error("Missing the required parameter 'registrationId' when calling acceptRegistration");
      }

      let pathParams = {
        'registrationId': registrationId
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
        '/api/v1/users/registrations/{registrationId}/accept', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRegistration operation.
     * @callback module:api/RegisterApi~deleteRegistrationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete registration
     * Delete the registration entry. It will not remove the user associated with this registration (if any)
     * @param {Number} registrationId Registration ID
     * @param {module:api/RegisterApi~deleteRegistrationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteRegistration(registrationId, callback) {
      let postBody = null;
      // verify the required parameter 'registrationId' is set
      if (registrationId === undefined || registrationId === null) {
        throw new Error("Missing the required parameter 'registrationId' when calling deleteRegistration");
      }

      let pathParams = {
        'registrationId': registrationId
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
        '/api/v1/users/registrations/{registrationId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRegistrations operation.
     * @callback module:api/RegisterApi~listRegistrationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRegistrations200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List registrations
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [search] 
     * @param {module:model/String} [sort] 
     * @param {module:api/RegisterApi~listRegistrationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRegistrations200Response}
     */
    listRegistrations(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'start': opts['start'],
        'count': opts['count'],
        'search': opts['search'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListRegistrations200Response;
      return this.apiClient.callApi(
        '/api/v1/users/registrations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the registerUser operation.
     * @callback module:api/RegisterApi~registerUserCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Register a user
     * Signup has to be enabled and signup approval is not required
     * @param {module:model/RegisterUser} registerUser 
     * @param {module:api/RegisterApi~registerUserCallback} callback The callback function, accepting three arguments: error, data, response
     */
    registerUser(registerUser, callback) {
      let postBody = registerUser;
      // verify the required parameter 'registerUser' is set
      if (registerUser === undefined || registerUser === null) {
        throw new Error("Missing the required parameter 'registerUser' when calling registerUser");
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
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/register', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rejectRegistration operation.
     * @callback module:api/RegisterApi~rejectRegistrationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reject registration
     * @param {Number} registrationId Registration ID
     * @param {Object} opts Optional parameters
     * @param {module:model/UserRegistrationAcceptOrReject} [userRegistrationAcceptOrReject] 
     * @param {module:api/RegisterApi~rejectRegistrationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    rejectRegistration(registrationId, opts, callback) {
      opts = opts || {};
      let postBody = opts['userRegistrationAcceptOrReject'];
      // verify the required parameter 'registrationId' is set
      if (registrationId === undefined || registrationId === null) {
        throw new Error("Missing the required parameter 'registrationId' when calling rejectRegistration");
      }

      let pathParams = {
        'registrationId': registrationId
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
        '/api/v1/users/registrations/{registrationId}/reject', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestRegistration operation.
     * @callback module:api/RegisterApi~requestRegistrationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserRegistration} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request registration
     * Signup has to be enabled and require approval on the instance
     * @param {Object} opts Optional parameters
     * @param {module:model/UserRegistrationRequest} [userRegistrationRequest] 
     * @param {module:api/RegisterApi~requestRegistrationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserRegistration}
     */
    requestRegistration(opts, callback) {
      opts = opts || {};
      let postBody = opts['userRegistrationRequest'];

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
      let accepts = ['application/json'];
      let returnType = UserRegistration;
      return this.apiClient.callApi(
        '/api/v1/users/registrations/request', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resendEmailToVerifyRegistration operation.
     * @callback module:api/RegisterApi~resendEmailToVerifyRegistrationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Resend verification link to registration email
     * @param {Object} opts Optional parameters
     * @param {module:model/ResendEmailToVerifyRegistrationRequest} [resendEmailToVerifyRegistrationRequest] 
     * @param {module:api/RegisterApi~resendEmailToVerifyRegistrationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    resendEmailToVerifyRegistration(opts, callback) {
      opts = opts || {};
      let postBody = opts['resendEmailToVerifyRegistrationRequest'];

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
        '/api/v1/users/registrations/ask-send-verify-email', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resendEmailToVerifyUser_0 operation.
     * @callback module:api/RegisterApi~resendEmailToVerifyUser_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Resend user verification link
     * @param {Object} opts Optional parameters
     * @param {module:model/ResendEmailToVerifyUserRequest} [resendEmailToVerifyUserRequest] 
     * @param {module:api/RegisterApi~resendEmailToVerifyUser_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    resendEmailToVerifyUser_0(opts, callback) {
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
     * Callback function to receive the result of the verifyRegistrationEmail operation.
     * @callback module:api/RegisterApi~verifyRegistrationEmailCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Verify a registration email
     * Following a user registration request, the user will receive an email asking to click a link containing a secret. 
     * @param {Number} registrationId Registration ID
     * @param {Object} opts Optional parameters
     * @param {module:model/VerifyRegistrationEmailRequest} [verifyRegistrationEmailRequest] 
     * @param {module:api/RegisterApi~verifyRegistrationEmailCallback} callback The callback function, accepting three arguments: error, data, response
     */
    verifyRegistrationEmail(registrationId, opts, callback) {
      opts = opts || {};
      let postBody = opts['verifyRegistrationEmailRequest'];
      // verify the required parameter 'registrationId' is set
      if (registrationId === undefined || registrationId === null) {
        throw new Error("Missing the required parameter 'registrationId' when calling verifyRegistrationEmail");
      }

      let pathParams = {
        'registrationId': registrationId
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
        '/api/v1/users/registrations/{registrationId}/verify-email', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the verifyUser_0 operation.
     * @callback module:api/RegisterApi~verifyUser_0Callback
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
     * @param {module:api/RegisterApi~verifyUser_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    verifyUser_0(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['verifyUserRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling verifyUser_0");
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
