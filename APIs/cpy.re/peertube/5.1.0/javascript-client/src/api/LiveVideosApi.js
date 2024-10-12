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
import ApiV1VideosLiveIdSessionsGet200Response from '../model/ApiV1VideosLiveIdSessionsGet200Response';
import GetLiveIdIdParameter from '../model/GetLiveIdIdParameter';
import LiveVideoLatencyMode from '../model/LiveVideoLatencyMode';
import LiveVideoReplaySettings from '../model/LiveVideoReplaySettings';
import LiveVideoResponse from '../model/LiveVideoResponse';
import LiveVideoSessionResponse from '../model/LiveVideoSessionResponse';
import LiveVideoUpdate from '../model/LiveVideoUpdate';
import VideoPrivacySet from '../model/VideoPrivacySet';
import VideoUploadResponse from '../model/VideoUploadResponse';

/**
* LiveVideos service.
* @module api/LiveVideosApi
* @version 5.1.0
*/
export default class LiveVideosApi {

    /**
    * Constructs a new LiveVideosApi. 
    * @alias module:api/LiveVideosApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addLive operation.
     * @callback module:api/LiveVideosApi~addLiveCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoUploadResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a live
     * @param {Number} channelId Channel id that will contain this live video
     * @param {String} name Live video/replay name
     * @param {Object} opts Optional parameters
     * @param {Number} [category] category id of the video (see [/videos/categories](#operation/getCategories))
     * @param {Boolean} [commentsEnabled] Enable or disable comments for this live video/replay
     * @param {String} [description] Live video/replay description
     * @param {Boolean} [downloadEnabled] Enable or disable downloading for the replay of this live video
     * @param {String} [language] language id of the video (see [/videos/languages](#operation/getLanguages))
     * @param {module:model/LiveVideoLatencyMode} [latencyMode] 
     * @param {Number} [licence] licence id of the video (see [/videos/licences](#operation/getLicences))
     * @param {Boolean} [nsfw] Whether or not this live video/replay contains sensitive content
     * @param {Boolean} [permanentLive] User can stream multiple times in a permanent live
     * @param {File} [previewfile] Live video/replay preview file
     * @param {module:model/VideoPrivacySet} [privacy] 
     * @param {module:model/LiveVideoReplaySettings} [replaySettings] 
     * @param {Boolean} [saveReplay] 
     * @param {String} [support] A text tell the audience how to support the creator
     * @param {Array.<String>} [tags] Live video/replay tags (maximum 5 tags each between 2 and 30 characters)
     * @param {File} [thumbnailfile] Live video/replay thumbnail file
     * @param {module:api/LiveVideosApi~addLiveCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoUploadResponse}
     */
    addLive(channelId, name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelId' is set
      if (channelId === undefined || channelId === null) {
        throw new Error("Missing the required parameter 'channelId' when calling addLive");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling addLive");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'category': opts['category'],
        'channelId': channelId,
        'commentsEnabled': opts['commentsEnabled'],
        'description': opts['description'],
        'downloadEnabled': opts['downloadEnabled'],
        'language': opts['language'],
        'latencyMode': opts['latencyMode'],
        'licence': opts['licence'],
        'name': name,
        'nsfw': opts['nsfw'],
        'permanentLive': opts['permanentLive'],
        'previewfile': opts['previewfile'],
        'privacy': opts['privacy'],
        'replaySettings': opts['replaySettings'],
        'saveReplay': opts['saveReplay'],
        'support': opts['support'],
        'tags': this.apiClient.buildCollectionParam(opts['tags'], 'csv'),
        'thumbnailfile': opts['thumbnailfile']
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = VideoUploadResponse;
      return this.apiClient.callApi(
        '/api/v1/videos/live', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideosIdLiveSessionGet operation.
     * @callback module:api/LiveVideosApi~apiV1VideosIdLiveSessionGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LiveVideoSessionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get live session of a replay
     * If the video is a replay of a live, you can find the associated live session using this endpoint
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/LiveVideosApi~apiV1VideosIdLiveSessionGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LiveVideoSessionResponse}
     */
    apiV1VideosIdLiveSessionGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling apiV1VideosIdLiveSessionGet");
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
      let accepts = ['application/json'];
      let returnType = LiveVideoSessionResponse;
      return this.apiClient.callApi(
        '/api/v1/videos/{id}/live-session', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideosLiveIdSessionsGet operation.
     * @callback module:api/LiveVideosApi~apiV1VideosLiveIdSessionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1VideosLiveIdSessionsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List live sessions
     * List all sessions created in a particular live
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/LiveVideosApi~apiV1VideosLiveIdSessionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1VideosLiveIdSessionsGet200Response}
     */
    apiV1VideosLiveIdSessionsGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling apiV1VideosLiveIdSessionsGet");
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
      let accepts = ['application/json'];
      let returnType = ApiV1VideosLiveIdSessionsGet200Response;
      return this.apiClient.callApi(
        '/api/v1/videos/live/{id}/sessions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLiveId operation.
     * @callback module:api/LiveVideosApi~getLiveIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LiveVideoResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get information about a live
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/LiveVideosApi~getLiveIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LiveVideoResponse}
     */
    getLiveId(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getLiveId");
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
      let accepts = ['application/json'];
      let returnType = LiveVideoResponse;
      return this.apiClient.callApi(
        '/api/v1/videos/live/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateLiveId operation.
     * @callback module:api/LiveVideosApi~updateLiveIdCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update information about a live
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {Object} opts Optional parameters
     * @param {module:model/LiveVideoUpdate} [liveVideoUpdate] 
     * @param {module:api/LiveVideosApi~updateLiveIdCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateLiveId(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['liveVideoUpdate'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateLiveId");
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
        '/api/v1/videos/live/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
