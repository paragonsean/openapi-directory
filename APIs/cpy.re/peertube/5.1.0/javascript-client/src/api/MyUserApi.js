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
import ApiV1UsersMeAvatarPickPost200Response from '../model/ApiV1UsersMeAvatarPickPost200Response';
import ApiV1UsersMeVideoQuotaUsedGet200Response from '../model/ApiV1UsersMeVideoQuotaUsedGet200Response';
import GetAbuses200Response from '../model/GetAbuses200Response';
import GetMeVideoRating from '../model/GetMeVideoRating';
import UpdateMe from '../model/UpdateMe';
import User from '../model/User';
import VideoImportsList from '../model/VideoImportsList';
import VideoListResponse from '../model/VideoListResponse';

/**
* MyUser service.
* @module api/MyUserApi
* @version 5.1.0
*/
export default class MyUserApi {

    /**
    * Constructs a new MyUserApi. 
    * @alias module:api/MyUserApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiV1UsersMeAvatarDelete operation.
     * @callback module:api/MyUserApi~apiV1UsersMeAvatarDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete my avatar
     * @param {module:api/MyUserApi~apiV1UsersMeAvatarDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1UsersMeAvatarDelete(callback) {
      let postBody = null;

      let pathParams = {
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
        '/api/v1/users/me/avatar', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1UsersMeAvatarPickPost operation.
     * @callback module:api/MyUserApi~apiV1UsersMeAvatarPickPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1UsersMeAvatarPickPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update my user avatar
     * @param {Object} opts Optional parameters
     * @param {File} [avatarfile] The file to upload
     * @param {module:api/MyUserApi~apiV1UsersMeAvatarPickPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1UsersMeAvatarPickPost200Response}
     */
    apiV1UsersMeAvatarPickPost(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'avatarfile': opts['avatarfile']
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = ApiV1UsersMeAvatarPickPost200Response;
      return this.apiClient.callApi(
        '/api/v1/users/me/avatar/pick', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1UsersMeVideoQuotaUsedGet operation.
     * @callback module:api/MyUserApi~apiV1UsersMeVideoQuotaUsedGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1UsersMeVideoQuotaUsedGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get my user used quota
     * @param {module:api/MyUserApi~apiV1UsersMeVideoQuotaUsedGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1UsersMeVideoQuotaUsedGet200Response}
     */
    apiV1UsersMeVideoQuotaUsedGet(callback) {
      let postBody = null;

      let pathParams = {
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
      let returnType = ApiV1UsersMeVideoQuotaUsedGet200Response;
      return this.apiClient.callApi(
        '/api/v1/users/me/video-quota-used', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1UsersMeVideosGet operation.
     * @callback module:api/MyUserApi~apiV1UsersMeVideosGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoListResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get videos of my user
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:api/MyUserApi~apiV1UsersMeVideosGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoListResponse}
     */
    apiV1UsersMeVideosGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = VideoListResponse;
      return this.apiClient.callApi(
        '/api/v1/users/me/videos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1UsersMeVideosImportsGet_0 operation.
     * @callback module:api/MyUserApi~apiV1UsersMeVideosImportsGet_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoImportsList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get video imports of my user
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {String} [targetUrl] Filter on import target URL
     * @param {Number} [videoChannelSyncId] Filter on imports created by a specific channel synchronization
     * @param {String} [search] Search in video names
     * @param {module:api/MyUserApi~apiV1UsersMeVideosImportsGet_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoImportsList}
     */
    apiV1UsersMeVideosImportsGet_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort'],
        'targetUrl': opts['targetUrl'],
        'videoChannelSyncId': opts['videoChannelSyncId'],
        'search': opts['search']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VideoImportsList;
      return this.apiClient.callApi(
        '/api/v1/users/me/videos/imports', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1UsersMeVideosVideoIdRatingGet operation.
     * @callback module:api/MyUserApi~apiV1UsersMeVideosVideoIdRatingGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetMeVideoRating} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get rate of my user for a video
     * @param {Number} videoId The video id
     * @param {module:api/MyUserApi~apiV1UsersMeVideosVideoIdRatingGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetMeVideoRating}
     */
    apiV1UsersMeVideosVideoIdRatingGet(videoId, callback) {
      let postBody = null;
      // verify the required parameter 'videoId' is set
      if (videoId === undefined || videoId === null) {
        throw new Error("Missing the required parameter 'videoId' when calling apiV1UsersMeVideosVideoIdRatingGet");
      }

      let pathParams = {
        'videoId': videoId
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
      let returnType = GetMeVideoRating;
      return this.apiClient.callApi(
        '/api/v1/users/me/videos/{videoId}/rating', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMyAbuses_0 operation.
     * @callback module:api/MyUserApi~getMyAbuses_0Callback
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
     * @param {module:api/MyUserApi~getMyAbuses_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAbuses200Response}
     */
    getMyAbuses_0(opts, callback) {
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

    /**
     * Callback function to receive the result of the getUserInfo operation.
     * @callback module:api/MyUserApi~getUserInfoCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/User>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get my user information
     * @param {module:api/MyUserApi~getUserInfoCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/User>}
     */
    getUserInfo(callback) {
      let postBody = null;

      let pathParams = {
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
      let returnType = [User];
      return this.apiClient.callApi(
        '/api/v1/users/me', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putUserInfo operation.
     * @callback module:api/MyUserApi~putUserInfoCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update my user information
     * @param {module:model/UpdateMe} updateMe 
     * @param {module:api/MyUserApi~putUserInfoCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putUserInfo(updateMe, callback) {
      let postBody = updateMe;
      // verify the required parameter 'updateMe' is set
      if (updateMe === undefined || updateMe === null) {
        throw new Error("Missing the required parameter 'updateMe' when calling putUserInfo");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/users/me', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
