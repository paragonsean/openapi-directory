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
import AddVideoChannel200Response from '../model/AddVideoChannel200Response';
import ApiV1AccountsNameVideoPlaylistsGet200Response from '../model/ApiV1AccountsNameVideoPlaylistsGet200Response';
import ApiV1UsersMeAvatarPickPost200Response from '../model/ApiV1UsersMeAvatarPickPost200Response';
import ApiV1VideoChannelsChannelHandleBannerPickPost200Response from '../model/ApiV1VideoChannelsChannelHandleBannerPickPost200Response';
import GetAccountFollowers200Response from '../model/GetAccountFollowers200Response';
import GetAccountVideosCategoryOneOfParameter from '../model/GetAccountVideosCategoryOneOfParameter';
import GetAccountVideosLanguageOneOfParameter from '../model/GetAccountVideosLanguageOneOfParameter';
import GetAccountVideosLicenceOneOfParameter from '../model/GetAccountVideosLicenceOneOfParameter';
import GetAccountVideosTagsAllOfParameter from '../model/GetAccountVideosTagsAllOfParameter';
import GetAccountVideosTagsOneOfParameter from '../model/GetAccountVideosTagsOneOfParameter';
import ImportVideosInChannelCreate from '../model/ImportVideosInChannelCreate';
import VideoChannel from '../model/VideoChannel';
import VideoChannelCreate from '../model/VideoChannelCreate';
import VideoChannelList from '../model/VideoChannelList';
import VideoChannelSyncList from '../model/VideoChannelSyncList';
import VideoChannelUpdate from '../model/VideoChannelUpdate';
import VideoListResponse from '../model/VideoListResponse';
import VideoPlaylistTypeSet from '../model/VideoPlaylistTypeSet';
import VideoPrivacySet from '../model/VideoPrivacySet';

/**
* VideoChannels service.
* @module api/VideoChannelsApi
* @version 5.1.0
*/
export default class VideoChannelsApi {

    /**
    * Constructs a new VideoChannelsApi. 
    * @alias module:api/VideoChannelsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addVideoChannel operation.
     * @callback module:api/VideoChannelsApi~addVideoChannelCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AddVideoChannel200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a video channel
     * @param {Object} opts Optional parameters
     * @param {module:model/VideoChannelCreate} [videoChannelCreate] 
     * @param {module:api/VideoChannelsApi~addVideoChannelCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AddVideoChannel200Response}
     */
    addVideoChannel(opts, callback) {
      opts = opts || {};
      let postBody = opts['videoChannelCreate'];

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
      let returnType = AddVideoChannel200Response;
      return this.apiClient.callApi(
        '/api/v1/video-channels', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AccountsNameVideoChannelSyncsGet operation.
     * @callback module:api/VideoChannelsApi~apiV1AccountsNameVideoChannelSyncsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoChannelSyncList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the synchronizations of video channels of an account
     * @param {String} name The username or handle of the account
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:api/VideoChannelsApi~apiV1AccountsNameVideoChannelSyncsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoChannelSyncList}
     */
    apiV1AccountsNameVideoChannelSyncsGet(name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling apiV1AccountsNameVideoChannelSyncsGet");
      }

      let pathParams = {
        'name': name
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VideoChannelSyncList;
      return this.apiClient.callApi(
        '/api/v1/accounts/{name}/video-channel-syncs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AccountsNameVideoChannelsGet operation.
     * @callback module:api/VideoChannelsApi~apiV1AccountsNameVideoChannelsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoChannelList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List video channels of an account
     * @param {String} name The username or handle of the account
     * @param {Object} opts Optional parameters
     * @param {Boolean} [withStats] include daily view statistics for the last 30 days and total views (only if authentified as the account user)
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:api/VideoChannelsApi~apiV1AccountsNameVideoChannelsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoChannelList}
     */
    apiV1AccountsNameVideoChannelsGet(name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling apiV1AccountsNameVideoChannelsGet");
      }

      let pathParams = {
        'name': name
      };
      let queryParams = {
        'withStats': opts['withStats'],
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VideoChannelList;
      return this.apiClient.callApi(
        '/api/v1/accounts/{name}/video-channels', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleAvatarDelete operation.
     * @callback module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleAvatarDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete channel avatar
     * @param {String} channelHandle The video channel handle
     * @param {module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleAvatarDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideoChannelsChannelHandleAvatarDelete(channelHandle, callback) {
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleAvatarDelete");
      }

      let pathParams = {
        'channelHandle': channelHandle
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
        '/api/v1/video-channels/{channelHandle}/avatar', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleAvatarPickPost operation.
     * @callback module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleAvatarPickPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1UsersMeAvatarPickPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update channel avatar
     * @param {String} channelHandle The video channel handle
     * @param {Object} opts Optional parameters
     * @param {File} [avatarfile] The file to upload.
     * @param {module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleAvatarPickPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1UsersMeAvatarPickPost200Response}
     */
    apiV1VideoChannelsChannelHandleAvatarPickPost(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleAvatarPickPost");
      }

      let pathParams = {
        'channelHandle': channelHandle
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
        '/api/v1/video-channels/{channelHandle}/avatar/pick', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleBannerDelete operation.
     * @callback module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleBannerDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete channel banner
     * @param {String} channelHandle The video channel handle
     * @param {module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleBannerDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideoChannelsChannelHandleBannerDelete(channelHandle, callback) {
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleBannerDelete");
      }

      let pathParams = {
        'channelHandle': channelHandle
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
        '/api/v1/video-channels/{channelHandle}/banner', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleBannerPickPost operation.
     * @callback module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleBannerPickPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1VideoChannelsChannelHandleBannerPickPost200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update channel banner
     * @param {String} channelHandle The video channel handle
     * @param {Object} opts Optional parameters
     * @param {File} [bannerfile] The file to upload.
     * @param {module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleBannerPickPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1VideoChannelsChannelHandleBannerPickPost200Response}
     */
    apiV1VideoChannelsChannelHandleBannerPickPost(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleBannerPickPost");
      }

      let pathParams = {
        'channelHandle': channelHandle
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'bannerfile': opts['bannerfile']
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = ApiV1VideoChannelsChannelHandleBannerPickPost200Response;
      return this.apiClient.callApi(
        '/api/v1/video-channels/{channelHandle}/banner/pick', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleImportVideosPost operation.
     * @callback module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleImportVideosPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Import videos in channel
     * Import a remote channel/playlist videos into a channel
     * @param {String} channelHandle The video channel handle
     * @param {Object} opts Optional parameters
     * @param {module:model/ImportVideosInChannelCreate} [importVideosInChannelCreate] 
     * @param {module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleImportVideosPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideoChannelsChannelHandleImportVideosPost(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = opts['importVideosInChannelCreate'];
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleImportVideosPost");
      }

      let pathParams = {
        'channelHandle': channelHandle
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
        '/api/v1/video-channels/{channelHandle}/import-videos', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0 operation.
     * @callback module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0Callback
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
     * @param {module:api/VideoChannelsApi~apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1AccountsNameVideoPlaylistsGet200Response}
     */
    apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0");
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
     * Callback function to receive the result of the delVideoChannel operation.
     * @callback module:api/VideoChannelsApi~delVideoChannelCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a video channel
     * @param {String} channelHandle The video channel handle
     * @param {module:api/VideoChannelsApi~delVideoChannelCallback} callback The callback function, accepting three arguments: error, data, response
     */
    delVideoChannel(channelHandle, callback) {
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling delVideoChannel");
      }

      let pathParams = {
        'channelHandle': channelHandle
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
        '/api/v1/video-channels/{channelHandle}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoChannel operation.
     * @callback module:api/VideoChannelsApi~getVideoChannelCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoChannel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a video channel
     * @param {String} channelHandle The video channel handle
     * @param {module:api/VideoChannelsApi~getVideoChannelCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoChannel}
     */
    getVideoChannel(channelHandle, callback) {
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling getVideoChannel");
      }

      let pathParams = {
        'channelHandle': channelHandle
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
      let returnType = VideoChannel;
      return this.apiClient.callApi(
        '/api/v1/video-channels/{channelHandle}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoChannelFollowers operation.
     * @callback module:api/VideoChannelsApi~getVideoChannelFollowersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAccountFollowers200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List followers of a video channel
     * @param {String} channelHandle The video channel handle
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:model/String} [sort] Sort followers by criteria
     * @param {String} [search] Plain text search, applied to various parts of the model depending on endpoint
     * @param {module:api/VideoChannelsApi~getVideoChannelFollowersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAccountFollowers200Response}
     */
    getVideoChannelFollowers(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling getVideoChannelFollowers");
      }

      let pathParams = {
        'channelHandle': channelHandle
      };
      let queryParams = {
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort'],
        'search': opts['search']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetAccountFollowers200Response;
      return this.apiClient.callApi(
        '/api/v1/video-channels/{channelHandle}/followers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoChannelVideos_0 operation.
     * @callback module:api/VideoChannelsApi~getVideoChannelVideos_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoListResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videos of a video channel
     * @param {String} channelHandle The video channel handle
     * @param {Object} opts Optional parameters
     * @param {module:model/GetAccountVideosCategoryOneOfParameter} [categoryOneOf] category id of the video (see [/videos/categories](#operation/getCategories))
     * @param {Boolean} [isLive] whether or not the video is a live
     * @param {module:model/GetAccountVideosTagsOneOfParameter} [tagsOneOf] tag(s) of the video
     * @param {module:model/GetAccountVideosTagsAllOfParameter} [tagsAllOf] tag(s) of the video, where all should be present in the video
     * @param {module:model/GetAccountVideosLicenceOneOfParameter} [licenceOneOf] licence id of the video (see [/videos/licences](#operation/getLicences))
     * @param {module:model/GetAccountVideosLanguageOneOfParameter} [languageOneOf] language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
     * @param {module:model/String} [nsfw] whether to include nsfw videos, if any
     * @param {Boolean} [isLocal] **PeerTube >= 4.0** Display only local or remote videos
     * @param {module:model/Number} [include] **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
     * @param {module:model/VideoPrivacySet} [privacyOneOf] **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
     * @param {Boolean} [hasHLSFiles] **PeerTube >= 4.0** Display only videos that have HLS files
     * @param {Boolean} [hasWebtorrentFiles] **PeerTube >= 4.0** Display only videos that have WebTorrent files
     * @param {module:model/String} [skipCount = 'false')] if you don't need the `total` in the response
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:model/String} [sort] 
     * @param {Boolean} [excludeAlreadyWatched] Whether or not to exclude videos that are in the user's video history
     * @param {module:api/VideoChannelsApi~getVideoChannelVideos_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoListResponse}
     */
    getVideoChannelVideos_0(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling getVideoChannelVideos_0");
      }

      let pathParams = {
        'channelHandle': channelHandle
      };
      let queryParams = {
        'categoryOneOf': opts['categoryOneOf'],
        'isLive': opts['isLive'],
        'tagsOneOf': opts['tagsOneOf'],
        'tagsAllOf': opts['tagsAllOf'],
        'licenceOneOf': opts['licenceOneOf'],
        'languageOneOf': opts['languageOneOf'],
        'nsfw': opts['nsfw'],
        'isLocal': opts['isLocal'],
        'include': opts['include'],
        'privacyOneOf': opts['privacyOneOf'],
        'hasHLSFiles': opts['hasHLSFiles'],
        'hasWebtorrentFiles': opts['hasWebtorrentFiles'],
        'skipCount': opts['skipCount'],
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort'],
        'excludeAlreadyWatched': opts['excludeAlreadyWatched']
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
        '/api/v1/video-channels/{channelHandle}/videos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoChannels operation.
     * @callback module:api/VideoChannelsApi~getVideoChannelsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoChannelList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List video channels
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:api/VideoChannelsApi~getVideoChannelsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoChannelList}
     */
    getVideoChannels(opts, callback) {
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VideoChannelList;
      return this.apiClient.callApi(
        '/api/v1/video-channels', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putVideoChannel operation.
     * @callback module:api/VideoChannelsApi~putVideoChannelCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a video channel
     * @param {String} channelHandle The video channel handle
     * @param {Object} opts Optional parameters
     * @param {module:model/VideoChannelUpdate} [videoChannelUpdate] 
     * @param {module:api/VideoChannelsApi~putVideoChannelCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putVideoChannel(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = opts['videoChannelUpdate'];
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling putVideoChannel");
      }

      let pathParams = {
        'channelHandle': channelHandle
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
        '/api/v1/video-channels/{channelHandle}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
