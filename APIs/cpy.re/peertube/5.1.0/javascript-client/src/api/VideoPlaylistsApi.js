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
import AddPlaylist200Response from '../model/AddPlaylist200Response';
import AddVideoPlaylistVideo200Response from '../model/AddVideoPlaylistVideo200Response';
import AddVideoPlaylistVideoRequest from '../model/AddVideoPlaylistVideoRequest';
import ApiV1AccountsNameVideoPlaylistsGet200Response from '../model/ApiV1AccountsNameVideoPlaylistsGet200Response';
import ApiV1UsersMeVideoPlaylistsVideosExistGet200Response from '../model/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response';
import PutVideoPlaylistVideoRequest from '../model/PutVideoPlaylistVideoRequest';
import ReorderVideoPlaylistRequest from '../model/ReorderVideoPlaylistRequest';
import VideoListResponse from '../model/VideoListResponse';
import VideoPlaylist from '../model/VideoPlaylist';
import VideoPlaylistPrivacySet from '../model/VideoPlaylistPrivacySet';
import VideoPlaylistTypeSet from '../model/VideoPlaylistTypeSet';

/**
* VideoPlaylists service.
* @module api/VideoPlaylistsApi
* @version 5.1.0
*/
export default class VideoPlaylistsApi {

    /**
    * Constructs a new VideoPlaylistsApi. 
    * @alias module:api/VideoPlaylistsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addPlaylist operation.
     * @callback module:api/VideoPlaylistsApi~addPlaylistCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AddPlaylist200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a video playlist
     * If the video playlist is set as public, `videoChannelId` is mandatory.
     * @param {String} displayName Video playlist display name
     * @param {Object} opts Optional parameters
     * @param {String} [description] Video playlist description
     * @param {module:model/VideoPlaylistPrivacySet} [privacy] 
     * @param {File} [thumbnailfile] Video playlist thumbnail file
     * @param {Number} [videoChannelId] Video channel in which the playlist will be published
     * @param {module:api/VideoPlaylistsApi~addPlaylistCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AddPlaylist200Response}
     */
    addPlaylist(displayName, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'displayName' is set
      if (displayName === undefined || displayName === null) {
        throw new Error("Missing the required parameter 'displayName' when calling addPlaylist");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'description': opts['description'],
        'displayName': displayName,
        'privacy': opts['privacy'],
        'thumbnailfile': opts['thumbnailfile'],
        'videoChannelId': opts['videoChannelId']
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = AddPlaylist200Response;
      return this.apiClient.callApi(
        '/api/v1/video-playlists', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addVideoPlaylistVideo_0 operation.
     * @callback module:api/VideoPlaylistsApi~addVideoPlaylistVideo_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/AddVideoPlaylistVideo200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a video in a playlist
     * @param {Number} playlistId Playlist id
     * @param {Object} opts Optional parameters
     * @param {module:model/AddVideoPlaylistVideoRequest} [addVideoPlaylistVideoRequest] 
     * @param {module:api/VideoPlaylistsApi~addVideoPlaylistVideo_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AddVideoPlaylistVideo200Response}
     */
    addVideoPlaylistVideo_0(playlistId, opts, callback) {
      opts = opts || {};
      let postBody = opts['addVideoPlaylistVideoRequest'];
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling addVideoPlaylistVideo_0");
      }

      let pathParams = {
        'playlistId': playlistId
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
      let returnType = AddVideoPlaylistVideo200Response;
      return this.apiClient.callApi(
        '/api/v1/video-playlists/{playlistId}/videos', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AccountsNameVideoPlaylistsGet operation.
     * @callback module:api/VideoPlaylistsApi~apiV1AccountsNameVideoPlaylistsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1AccountsNameVideoPlaylistsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List playlists of an account
     * @param {String} name The username or handle of the account
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {String} [search] Plain text search, applied to various parts of the model depending on endpoint
     * @param {module:model/VideoPlaylistTypeSet} [playlistType] 
     * @param {module:api/VideoPlaylistsApi~apiV1AccountsNameVideoPlaylistsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1AccountsNameVideoPlaylistsGet200Response}
     */
    apiV1AccountsNameVideoPlaylistsGet(name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling apiV1AccountsNameVideoPlaylistsGet");
      }

      let pathParams = {
        'name': name
      };
      let queryParams = {
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort'],
        'search': opts['search'],
        'playlistType': opts['playlistType']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ApiV1AccountsNameVideoPlaylistsGet200Response;
      return this.apiClient.callApi(
        '/api/v1/accounts/{name}/video-playlists', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1UsersMeVideoPlaylistsVideosExistGet operation.
     * @callback module:api/VideoPlaylistsApi~apiV1UsersMeVideoPlaylistsVideosExistGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Check video exists in my playlists
     * @param {Array.<Number>} videoIds The video ids to check
     * @param {module:api/VideoPlaylistsApi~apiV1UsersMeVideoPlaylistsVideosExistGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response}
     */
    apiV1UsersMeVideoPlaylistsVideosExistGet(videoIds, callback) {
      let postBody = null;
      // verify the required parameter 'videoIds' is set
      if (videoIds === undefined || videoIds === null) {
        throw new Error("Missing the required parameter 'videoIds' when calling apiV1UsersMeVideoPlaylistsVideosExistGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'videoIds': this.apiClient.buildCollectionParam(videoIds, 'multi')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ApiV1UsersMeVideoPlaylistsVideosExistGet200Response;
      return this.apiClient.callApi(
        '/api/v1/users/me/video-playlists/videos-exist', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleVideoPlaylistsGet operation.
     * @callback module:api/VideoPlaylistsApi~apiV1VideoChannelsChannelHandleVideoPlaylistsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1AccountsNameVideoPlaylistsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List playlists of a channel
     * @param {String} channelHandle The video channel handle
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:model/VideoPlaylistTypeSet} [playlistType] 
     * @param {module:api/VideoPlaylistsApi~apiV1VideoChannelsChannelHandleVideoPlaylistsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1AccountsNameVideoPlaylistsGet200Response}
     */
    apiV1VideoChannelsChannelHandleVideoPlaylistsGet(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleVideoPlaylistsGet");
      }

      let pathParams = {
        'channelHandle': channelHandle
      };
      let queryParams = {
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort'],
        'playlistType': opts['playlistType']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ApiV1AccountsNameVideoPlaylistsGet200Response;
      return this.apiClient.callApi(
        '/api/v1/video-channels/{channelHandle}/video-playlists', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoPlaylistsPlaylistIdDelete operation.
     * @callback module:api/VideoPlaylistsApi~apiV1VideoPlaylistsPlaylistIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a video playlist
     * @param {Number} playlistId Playlist id
     * @param {module:api/VideoPlaylistsApi~apiV1VideoPlaylistsPlaylistIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideoPlaylistsPlaylistIdDelete(playlistId, callback) {
      let postBody = null;
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling apiV1VideoPlaylistsPlaylistIdDelete");
      }

      let pathParams = {
        'playlistId': playlistId
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
        '/api/v1/video-playlists/{playlistId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoPlaylistsPlaylistIdGet operation.
     * @callback module:api/VideoPlaylistsApi~apiV1VideoPlaylistsPlaylistIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoPlaylist} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a video playlist
     * @param {Number} playlistId Playlist id
     * @param {module:api/VideoPlaylistsApi~apiV1VideoPlaylistsPlaylistIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoPlaylist}
     */
    apiV1VideoPlaylistsPlaylistIdGet(playlistId, callback) {
      let postBody = null;
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling apiV1VideoPlaylistsPlaylistIdGet");
      }

      let pathParams = {
        'playlistId': playlistId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VideoPlaylist;
      return this.apiClient.callApi(
        '/api/v1/video-playlists/{playlistId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoPlaylistsPlaylistIdPut operation.
     * @callback module:api/VideoPlaylistsApi~apiV1VideoPlaylistsPlaylistIdPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a video playlist
     * If the video playlist is set as public, the playlist must have a assigned channel.
     * @param {Number} playlistId Playlist id
     * @param {Object} opts Optional parameters
     * @param {String} [description] Video playlist description
     * @param {String} [displayName] Video playlist display name
     * @param {module:model/VideoPlaylistPrivacySet} [privacy] 
     * @param {File} [thumbnailfile] Video playlist thumbnail file
     * @param {Number} [videoChannelId] Video channel in which the playlist will be published
     * @param {module:api/VideoPlaylistsApi~apiV1VideoPlaylistsPlaylistIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideoPlaylistsPlaylistIdPut(playlistId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling apiV1VideoPlaylistsPlaylistIdPut");
      }

      let pathParams = {
        'playlistId': playlistId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'description': opts['description'],
        'displayName': opts['displayName'],
        'privacy': opts['privacy'],
        'thumbnailfile': opts['thumbnailfile'],
        'videoChannelId': opts['videoChannelId']
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/video-playlists/{playlistId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the delVideoPlaylistVideo operation.
     * @callback module:api/VideoPlaylistsApi~delVideoPlaylistVideoCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an element from a playlist
     * @param {Number} playlistId Playlist id
     * @param {Number} playlistElementId Playlist element id
     * @param {module:api/VideoPlaylistsApi~delVideoPlaylistVideoCallback} callback The callback function, accepting three arguments: error, data, response
     */
    delVideoPlaylistVideo(playlistId, playlistElementId, callback) {
      let postBody = null;
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling delVideoPlaylistVideo");
      }
      // verify the required parameter 'playlistElementId' is set
      if (playlistElementId === undefined || playlistElementId === null) {
        throw new Error("Missing the required parameter 'playlistElementId' when calling delVideoPlaylistVideo");
      }

      let pathParams = {
        'playlistId': playlistId,
        'playlistElementId': playlistElementId
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
        '/api/v1/video-playlists/{playlistId}/videos/{playlistElementId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPlaylistPrivacyPolicies operation.
     * @callback module:api/VideoPlaylistsApi~getPlaylistPrivacyPoliciesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available playlist privacy policies
     * @param {module:api/VideoPlaylistsApi~getPlaylistPrivacyPoliciesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    getPlaylistPrivacyPolicies(callback) {
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
      let accepts = ['application/json'];
      let returnType = ['String'];
      return this.apiClient.callApi(
        '/api/v1/video-playlists/privacies', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPlaylists operation.
     * @callback module:api/VideoPlaylistsApi~getPlaylistsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1AccountsNameVideoPlaylistsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List video playlists
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:model/VideoPlaylistTypeSet} [playlistType] 
     * @param {module:api/VideoPlaylistsApi~getPlaylistsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1AccountsNameVideoPlaylistsGet200Response}
     */
    getPlaylists(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort'],
        'playlistType': opts['playlistType']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ApiV1AccountsNameVideoPlaylistsGet200Response;
      return this.apiClient.callApi(
        '/api/v1/video-playlists', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoPlaylistVideos_0 operation.
     * @callback module:api/VideoPlaylistsApi~getVideoPlaylistVideos_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoListResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videos of a playlist
     * @param {Number} playlistId Playlist id
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:api/VideoPlaylistsApi~getVideoPlaylistVideos_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoListResponse}
     */
    getVideoPlaylistVideos_0(playlistId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling getVideoPlaylistVideos_0");
      }

      let pathParams = {
        'playlistId': playlistId
      };
      let queryParams = {
        'start': opts['start'],
        'count': opts['count']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VideoListResponse;
      return this.apiClient.callApi(
        '/api/v1/video-playlists/{playlistId}/videos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putVideoPlaylistVideo operation.
     * @callback module:api/VideoPlaylistsApi~putVideoPlaylistVideoCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a playlist element
     * @param {Number} playlistId Playlist id
     * @param {Number} playlistElementId Playlist element id
     * @param {Object} opts Optional parameters
     * @param {module:model/PutVideoPlaylistVideoRequest} [putVideoPlaylistVideoRequest] 
     * @param {module:api/VideoPlaylistsApi~putVideoPlaylistVideoCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putVideoPlaylistVideo(playlistId, playlistElementId, opts, callback) {
      opts = opts || {};
      let postBody = opts['putVideoPlaylistVideoRequest'];
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling putVideoPlaylistVideo");
      }
      // verify the required parameter 'playlistElementId' is set
      if (playlistElementId === undefined || playlistElementId === null) {
        throw new Error("Missing the required parameter 'playlistElementId' when calling putVideoPlaylistVideo");
      }

      let pathParams = {
        'playlistId': playlistId,
        'playlistElementId': playlistElementId
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
        '/api/v1/video-playlists/{playlistId}/videos/{playlistElementId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reorderVideoPlaylist operation.
     * @callback module:api/VideoPlaylistsApi~reorderVideoPlaylistCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reorder a playlist
     * @param {Number} playlistId Playlist id
     * @param {Object} opts Optional parameters
     * @param {module:model/ReorderVideoPlaylistRequest} [reorderVideoPlaylistRequest] 
     * @param {module:api/VideoPlaylistsApi~reorderVideoPlaylistCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reorderVideoPlaylist(playlistId, opts, callback) {
      opts = opts || {};
      let postBody = opts['reorderVideoPlaylistRequest'];
      // verify the required parameter 'playlistId' is set
      if (playlistId === undefined || playlistId === null) {
        throw new Error("Missing the required parameter 'playlistId' when calling reorderVideoPlaylist");
      }

      let pathParams = {
        'playlistId': playlistId
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
        '/api/v1/video-playlists/{playlistId}/videos/reorder', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
