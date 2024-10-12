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
import AbuseStateSet from '../model/AbuseStateSet';
import ApiV1AbusesAbuseIdMessagesGet200Response from '../model/ApiV1AbusesAbuseIdMessagesGet200Response';
import ApiV1AbusesAbuseIdMessagesPostRequest from '../model/ApiV1AbusesAbuseIdMessagesPostRequest';
import ApiV1AbusesAbuseIdPutRequest from '../model/ApiV1AbusesAbuseIdPutRequest';
import ApiV1AbusesPost200Response from '../model/ApiV1AbusesPost200Response';
import ApiV1AbusesPostRequest from '../model/ApiV1AbusesPostRequest';
import GetAbuses200Response from '../model/GetAbuses200Response';

/**
* Abuses service.
* @module api/AbusesApi
* @version 5.1.0
*/
export default class AbusesApi {

    /**
    * Constructs a new AbusesApi. 
    * @alias module:api/AbusesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiV1AbusesAbuseIdDelete operation.
     * @callback module:api/AbusesApi~apiV1AbusesAbuseIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an abuse
     * @param {Number} abuseId Abuse id
     * @param {module:api/AbusesApi~apiV1AbusesAbuseIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1AbusesAbuseIdDelete(abuseId, callback) {
      let postBody = null;
      // verify the required parameter 'abuseId' is set
      if (abuseId === undefined || abuseId === null) {
        throw new Error("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdDelete");
      }

      let pathParams = {
        'abuseId': abuseId
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
        '/api/v1/abuses/{abuseId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete operation.
     * @callback module:api/AbusesApi~apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an abuse message
     * @param {Number} abuseId Abuse id
     * @param {Number} abuseMessageId Abuse message id
     * @param {module:api/AbusesApi~apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(abuseId, abuseMessageId, callback) {
      let postBody = null;
      // verify the required parameter 'abuseId' is set
      if (abuseId === undefined || abuseId === null) {
        throw new Error("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete");
      }
      // verify the required parameter 'abuseMessageId' is set
      if (abuseMessageId === undefined || abuseMessageId === null) {
        throw new Error("Missing the required parameter 'abuseMessageId' when calling apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete");
      }

      let pathParams = {
        'abuseId': abuseId,
        'abuseMessageId': abuseMessageId
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
        '/api/v1/abuses/{abuseId}/messages/{abuseMessageId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AbusesAbuseIdMessagesGet operation.
     * @callback module:api/AbusesApi~apiV1AbusesAbuseIdMessagesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1AbusesAbuseIdMessagesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List messages of an abuse
     * @param {Number} abuseId Abuse id
     * @param {module:api/AbusesApi~apiV1AbusesAbuseIdMessagesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1AbusesAbuseIdMessagesGet200Response}
     */
    apiV1AbusesAbuseIdMessagesGet(abuseId, callback) {
      let postBody = null;
      // verify the required parameter 'abuseId' is set
      if (abuseId === undefined || abuseId === null) {
        throw new Error("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdMessagesGet");
      }

      let pathParams = {
        'abuseId': abuseId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ApiV1AbusesAbuseIdMessagesGet200Response;
      return this.apiClient.callApi(
        '/api/v1/abuses/{abuseId}/messages', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AbusesAbuseIdMessagesPost operation.
     * @callback module:api/AbusesApi~apiV1AbusesAbuseIdMessagesPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add message to an abuse
     * @param {Number} abuseId Abuse id
     * @param {module:model/ApiV1AbusesAbuseIdMessagesPostRequest} apiV1AbusesAbuseIdMessagesPostRequest 
     * @param {module:api/AbusesApi~apiV1AbusesAbuseIdMessagesPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1AbusesAbuseIdMessagesPost(abuseId, apiV1AbusesAbuseIdMessagesPostRequest, callback) {
      let postBody = apiV1AbusesAbuseIdMessagesPostRequest;
      // verify the required parameter 'abuseId' is set
      if (abuseId === undefined || abuseId === null) {
        throw new Error("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdMessagesPost");
      }
      // verify the required parameter 'apiV1AbusesAbuseIdMessagesPostRequest' is set
      if (apiV1AbusesAbuseIdMessagesPostRequest === undefined || apiV1AbusesAbuseIdMessagesPostRequest === null) {
        throw new Error("Missing the required parameter 'apiV1AbusesAbuseIdMessagesPostRequest' when calling apiV1AbusesAbuseIdMessagesPost");
      }

      let pathParams = {
        'abuseId': abuseId
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
        '/api/v1/abuses/{abuseId}/messages', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AbusesAbuseIdPut operation.
     * @callback module:api/AbusesApi~apiV1AbusesAbuseIdPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an abuse
     * @param {Number} abuseId Abuse id
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiV1AbusesAbuseIdPutRequest} [apiV1AbusesAbuseIdPutRequest] 
     * @param {module:api/AbusesApi~apiV1AbusesAbuseIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1AbusesAbuseIdPut(abuseId, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiV1AbusesAbuseIdPutRequest'];
      // verify the required parameter 'abuseId' is set
      if (abuseId === undefined || abuseId === null) {
        throw new Error("Missing the required parameter 'abuseId' when calling apiV1AbusesAbuseIdPut");
      }

      let pathParams = {
        'abuseId': abuseId
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
        '/api/v1/abuses/{abuseId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AbusesPost operation.
     * @callback module:api/AbusesApi~apiV1AbusesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1AbusesPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Report an abuse
     * @param {module:model/ApiV1AbusesPostRequest} apiV1AbusesPostRequest 
     * @param {module:api/AbusesApi~apiV1AbusesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1AbusesPost200Response}
     */
    apiV1AbusesPost(apiV1AbusesPostRequest, callback) {
      let postBody = apiV1AbusesPostRequest;
      // verify the required parameter 'apiV1AbusesPostRequest' is set
      if (apiV1AbusesPostRequest === undefined || apiV1AbusesPostRequest === null) {
        throw new Error("Missing the required parameter 'apiV1AbusesPostRequest' when calling apiV1AbusesPost");
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
      let returnType = ApiV1AbusesPost200Response;
      return this.apiClient.callApi(
        '/api/v1/abuses', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAbuses operation.
     * @callback module:api/AbusesApi~getAbusesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAbuses200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List abuses
     * @param {Object} opts Optional parameters
     * @param {Number} [id] only list the report with this id
     * @param {Array.<module:model/String>} [predefinedReason] predefined reason the listed reports should contain
     * @param {String} [search] plain search that will match with video titles, reporter names and more
     * @param {module:model/AbuseStateSet} [state] 
     * @param {String} [searchReporter] only list reports of a specific reporter
     * @param {String} [searchReportee] only list reports of a specific reportee
     * @param {String} [searchVideo] only list reports of a specific video
     * @param {String} [searchVideoChannel] only list reports of a specific video channel
     * @param {module:model/String} [videoIs] only list deleted or blocklisted videos
     * @param {module:model/String} [filter] only list account, comment or video reports
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:model/String} [sort] Sort abuses by criteria
     * @param {module:api/AbusesApi~getAbusesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAbuses200Response}
     */
    getAbuses(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'id': opts['id'],
        'predefinedReason': this.apiClient.buildCollectionParam(opts['predefinedReason'], 'multi'),
        'search': opts['search'],
        'state': opts['state'],
        'searchReporter': opts['searchReporter'],
        'searchReportee': opts['searchReportee'],
        'searchVideo': opts['searchVideo'],
        'searchVideoChannel': opts['searchVideoChannel'],
        'videoIs': opts['videoIs'],
        'filter': opts['filter'],
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
      let returnType = GetAbuses200Response;
      return this.apiClient.callApi(
        '/api/v1/abuses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMyAbuses operation.
     * @callback module:api/AbusesApi~getMyAbusesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAbuses200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List my abuses
     * @param {Object} opts Optional parameters
     * @param {Number} [id] only list the report with this id
     * @param {module:model/AbuseStateSet} [state] 
     * @param {module:model/String} [sort] Sort abuses by criteria
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:api/AbusesApi~getMyAbusesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAbuses200Response}
     */
    getMyAbuses(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'id': opts['id'],
        'state': opts['state'],
        'sort': opts['sort'],
        'start': opts['start'],
        'count': opts['count']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetAbuses200Response;
      return this.apiClient.callApi(
        '/api/v1/users/me/abuses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
