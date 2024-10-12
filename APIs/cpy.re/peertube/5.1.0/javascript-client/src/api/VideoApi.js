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
import GetAccountVideosCategoryOneOfParameter from '../model/GetAccountVideosCategoryOneOfParameter';
import GetAccountVideosLanguageOneOfParameter from '../model/GetAccountVideosLanguageOneOfParameter';
import GetAccountVideosLicenceOneOfParameter from '../model/GetAccountVideosLicenceOneOfParameter';
import GetAccountVideosTagsAllOfParameter from '../model/GetAccountVideosTagsAllOfParameter';
import GetAccountVideosTagsOneOfParameter from '../model/GetAccountVideosTagsOneOfParameter';
import GetLiveIdIdParameter from '../model/GetLiveIdIdParameter';
import LiveVideoLatencyMode from '../model/LiveVideoLatencyMode';
import LiveVideoReplaySettings from '../model/LiveVideoReplaySettings';
import LiveVideoResponse from '../model/LiveVideoResponse';
import LiveVideoUpdate from '../model/LiveVideoUpdate';
import UserViewingVideo from '../model/UserViewingVideo';
import VideoDetails from '../model/VideoDetails';
import VideoListResponse from '../model/VideoListResponse';
import VideoPrivacySet from '../model/VideoPrivacySet';
import VideoScheduledUpdate from '../model/VideoScheduledUpdate';
import VideoSource from '../model/VideoSource';
import VideoTokenResponse from '../model/VideoTokenResponse';
import VideoUploadRequestResumable from '../model/VideoUploadRequestResumable';
import VideoUploadResponse from '../model/VideoUploadResponse';

/**
* Video service.
* @module api/VideoApi
* @version 5.1.0
*/
export default class VideoApi {

    /**
    * Constructs a new VideoApi. 
    * @alias module:api/VideoApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addLive_0 operation.
     * @callback module:api/VideoApi~addLive_0Callback
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
     * @param {module:api/VideoApi~addLive_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoUploadResponse}
     */
    addLive_0(channelId, name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelId' is set
      if (channelId === undefined || channelId === null) {
        throw new Error("Missing the required parameter 'channelId' when calling addLive_0");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling addLive_0");
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
     * Callback function to receive the result of the addView operation.
     * @callback module:api/VideoApi~addViewCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Notify user is watching a video
     * Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video's viewers counter. If the user is authenticated, PeerTube will also store the current player time.
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:model/UserViewingVideo} userViewingVideo 
     * @param {module:api/VideoApi~addViewCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addView(id, userViewingVideo, callback) {
      let postBody = userViewingVideo;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling addView");
      }
      // verify the required parameter 'userViewingVideo' is set
      if (userViewingVideo === undefined || userViewingVideo === null) {
        throw new Error("Missing the required parameter 'userViewingVideo' when calling addView");
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
        '/api/v1/videos/{id}/views', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideosIdStudioEditPost_0 operation.
     * @callback module:api/VideoApi~apiV1VideosIdStudioEditPost_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a studio task
     * Create a task to edit a video  (cut, add intro/outro etc)
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/VideoApi~apiV1VideosIdStudioEditPost_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideosIdStudioEditPost_0(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling apiV1VideosIdStudioEditPost_0");
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
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/videos/{id}/studio/edit', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1VideosIdWatchingPut operation.
     * @callback module:api/VideoApi~apiV1VideosIdWatchingPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set watching progress of a video
     * This endpoint has been deprecated. Use `/videos/{id}/views` instead
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:model/UserViewingVideo} userViewingVideo 
     * @param {module:api/VideoApi~apiV1VideosIdWatchingPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideosIdWatchingPut(id, userViewingVideo, callback) {
      let postBody = userViewingVideo;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling apiV1VideosIdWatchingPut");
      }
      // verify the required parameter 'userViewingVideo' is set
      if (userViewingVideo === undefined || userViewingVideo === null) {
        throw new Error("Missing the required parameter 'userViewingVideo' when calling apiV1VideosIdWatchingPut");
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
        '/api/v1/videos/{id}/watching', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the delVideo operation.
     * @callback module:api/VideoApi~delVideoCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a video
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/VideoApi~delVideoCallback} callback The callback function, accepting three arguments: error, data, response
     */
    delVideo(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling delVideo");
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
        '/api/v1/videos/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAccountVideos_0 operation.
     * @callback module:api/VideoApi~getAccountVideos_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoListResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videos of an account
     * @param {String} name The username or handle of the account
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
     * @param {module:api/VideoApi~getAccountVideos_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoListResponse}
     */
    getAccountVideos_0(name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling getAccountVideos_0");
      }

      let pathParams = {
        'name': name
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
        '/api/v1/accounts/{name}/videos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCategories operation.
     * @callback module:api/VideoApi~getCategoriesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available video categories
     * @param {module:api/VideoApi~getCategoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    getCategories(callback) {
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
        '/api/v1/videos/categories', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLanguages operation.
     * @callback module:api/VideoApi~getLanguagesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available video languages
     * @param {module:api/VideoApi~getLanguagesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    getLanguages(callback) {
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
        '/api/v1/videos/languages', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLicences operation.
     * @callback module:api/VideoApi~getLicencesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available video licences
     * @param {module:api/VideoApi~getLicencesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    getLicences(callback) {
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
        '/api/v1/videos/licences', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLiveId_0 operation.
     * @callback module:api/VideoApi~getLiveId_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/LiveVideoResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get information about a live
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/VideoApi~getLiveId_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LiveVideoResponse}
     */
    getLiveId_0(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getLiveId_0");
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
     * Callback function to receive the result of the getVideo operation.
     * @callback module:api/VideoApi~getVideoCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a video
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/VideoApi~getVideoCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoDetails}
     */
    getVideo(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getVideo");
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
      let accepts = ['application/json'];
      let returnType = VideoDetails;
      return this.apiClient.callApi(
        '/api/v1/videos/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoChannelVideos operation.
     * @callback module:api/VideoApi~getVideoChannelVideosCallback
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
     * @param {module:api/VideoApi~getVideoChannelVideosCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoListResponse}
     */
    getVideoChannelVideos(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling getVideoChannelVideos");
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
     * Callback function to receive the result of the getVideoDesc operation.
     * @callback module:api/VideoApi~getVideoDescCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get complete video description
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/VideoApi~getVideoDescCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    getVideoDesc(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getVideoDesc");
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
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/api/v1/videos/{id}/description', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoPrivacyPolicies operation.
     * @callback module:api/VideoApi~getVideoPrivacyPoliciesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available video privacy policies
     * @param {module:api/VideoApi~getVideoPrivacyPoliciesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    getVideoPrivacyPolicies(callback) {
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
        '/api/v1/videos/privacies', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideoSource operation.
     * @callback module:api/VideoApi~getVideoSourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoSource} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get video source file metadata
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/VideoApi~getVideoSourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoSource}
     */
    getVideoSource(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getVideoSource");
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
      let accepts = ['application/json'];
      let returnType = VideoSource;
      return this.apiClient.callApi(
        '/api/v1/videos/{id}/source', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideos operation.
     * @callback module:api/VideoApi~getVideosCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoListResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videos
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
     * @param {module:api/VideoApi~getVideosCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoListResponse}
     */
    getVideos(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
        '/api/v1/videos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the putVideo operation.
     * @callback module:api/VideoApi~putVideoCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a video
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {Object} opts Optional parameters
     * @param {Number} [category] category id of the video (see [/videos/categories](#operation/getCategories))
     * @param {Boolean} [commentsEnabled] Enable or disable comments for this video
     * @param {String} [description] Video description
     * @param {Boolean} [downloadEnabled] Enable or disable downloading for this video
     * @param {String} [language] language id of the video (see [/videos/languages](#operation/getLanguages))
     * @param {Number} [licence] licence id of the video (see [/videos/licences](#operation/getLicences))
     * @param {String} [name] Video name
     * @param {Boolean} [nsfw] Whether or not this video contains sensitive content
     * @param {Date} [originallyPublishedAt] Date when the content was originally published
     * @param {File} [previewfile] Video preview file
     * @param {module:model/VideoPrivacySet} [privacy] 
     * @param {module:model/VideoScheduledUpdate} [scheduleUpdate] 
     * @param {String} [support] A text tell the audience how to support the video creator
     * @param {Array.<String>} [tags] Video tags (maximum 5 tags each between 2 and 30 characters)
     * @param {File} [thumbnailfile] Video thumbnail file
     * @param {String} [waitTranscoding] Whether or not we wait transcoding before publish the video
     * @param {module:api/VideoApi~putVideoCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putVideo(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling putVideo");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'category': opts['category'],
        'commentsEnabled': opts['commentsEnabled'],
        'description': opts['description'],
        'downloadEnabled': opts['downloadEnabled'],
        'language': opts['language'],
        'licence': opts['licence'],
        'name': opts['name'],
        'nsfw': opts['nsfw'],
        'originallyPublishedAt': opts['originallyPublishedAt'],
        'previewfile': opts['previewfile'],
        'privacy': opts['privacy'],
        'scheduleUpdate': opts['scheduleUpdate'],
        'support': opts['support'],
        'tags': this.apiClient.buildCollectionParam(opts['tags'], 'csv'),
        'thumbnailfile': opts['thumbnailfile'],
        'waitTranscoding': opts['waitTranscoding']
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/videos/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestVideoToken operation.
     * @callback module:api/VideoApi~requestVideoTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoTokenResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request video token
     * Request special tokens that expire quickly to use them in some context (like accessing private static files)
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {module:api/VideoApi~requestVideoTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoTokenResponse}
     */
    requestVideoToken(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling requestVideoToken");
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
      let returnType = VideoTokenResponse;
      return this.apiClient.callApi(
        '/api/v1/videos/{id}/token', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateLiveId_0 operation.
     * @callback module:api/VideoApi~updateLiveId_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update information about a live
     * @param {module:model/GetLiveIdIdParameter} id The object id, uuid or short uuid
     * @param {Object} opts Optional parameters
     * @param {module:model/LiveVideoUpdate} [liveVideoUpdate] 
     * @param {module:api/VideoApi~updateLiveId_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    updateLiveId_0(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['liveVideoUpdate'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateLiveId_0");
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

    /**
     * Callback function to receive the result of the uploadLegacy operation.
     * @callback module:api/VideoApi~uploadLegacyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoUploadResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upload a video
     * Uses a single request to upload a video.
     * @param {Number} channelId Channel id that will contain this video
     * @param {String} name Video name
     * @param {File} videofile Video file
     * @param {Object} opts Optional parameters
     * @param {Number} [category] category id of the video (see [/videos/categories](#operation/getCategories))
     * @param {Boolean} [commentsEnabled] Enable or disable comments for this video
     * @param {String} [description] Video description
     * @param {Boolean} [downloadEnabled] Enable or disable downloading for this video
     * @param {String} [language] language id of the video (see [/videos/languages](#operation/getLanguages))
     * @param {Number} [licence] licence id of the video (see [/videos/licences](#operation/getLicences))
     * @param {Boolean} [nsfw] Whether or not this video contains sensitive content
     * @param {Date} [originallyPublishedAt] Date when the content was originally published
     * @param {File} [previewfile] Video preview file
     * @param {module:model/VideoPrivacySet} [privacy] 
     * @param {module:model/VideoScheduledUpdate} [scheduleUpdate] 
     * @param {String} [support] A text tell the audience how to support the video creator
     * @param {Array.<String>} [tags] Video tags (maximum 5 tags each between 2 and 30 characters)
     * @param {File} [thumbnailfile] Video thumbnail file
     * @param {Boolean} [waitTranscoding] Whether or not we wait transcoding before publish the video
     * @param {module:api/VideoApi~uploadLegacyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoUploadResponse}
     */
    uploadLegacy(channelId, name, videofile, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelId' is set
      if (channelId === undefined || channelId === null) {
        throw new Error("Missing the required parameter 'channelId' when calling uploadLegacy");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling uploadLegacy");
      }
      // verify the required parameter 'videofile' is set
      if (videofile === undefined || videofile === null) {
        throw new Error("Missing the required parameter 'videofile' when calling uploadLegacy");
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
        'licence': opts['licence'],
        'name': name,
        'nsfw': opts['nsfw'],
        'originallyPublishedAt': opts['originallyPublishedAt'],
        'previewfile': opts['previewfile'],
        'privacy': opts['privacy'],
        'scheduleUpdate': opts['scheduleUpdate'],
        'support': opts['support'],
        'tags': this.apiClient.buildCollectionParam(opts['tags'], 'csv'),
        'thumbnailfile': opts['thumbnailfile'],
        'waitTranscoding': opts['waitTranscoding'],
        'videofile': videofile
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = VideoUploadResponse;
      return this.apiClient.callApi(
        '/api/v1/videos/upload', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the uploadResumable operation.
     * @callback module:api/VideoApi~uploadResumableCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoUploadResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Send chunk for the resumable upload of a video
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video
     * @param {String} uploadId Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. 
     * @param {String} contentRange Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/1000000` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. 
     * @param {Number} contentLength Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. 
     * @param {Object} opts Optional parameters
     * @param {File} [body] 
     * @param {module:api/VideoApi~uploadResumableCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoUploadResponse}
     */
    uploadResumable(uploadId, contentRange, contentLength, opts, callback) {
      opts = opts || {};
      let postBody = opts['body'];
      // verify the required parameter 'uploadId' is set
      if (uploadId === undefined || uploadId === null) {
        throw new Error("Missing the required parameter 'uploadId' when calling uploadResumable");
      }
      // verify the required parameter 'contentRange' is set
      if (contentRange === undefined || contentRange === null) {
        throw new Error("Missing the required parameter 'contentRange' when calling uploadResumable");
      }
      // verify the required parameter 'contentLength' is set
      if (contentLength === undefined || contentLength === null) {
        throw new Error("Missing the required parameter 'contentLength' when calling uploadResumable");
      }

      let pathParams = {
      };
      let queryParams = {
        'upload_id': uploadId
      };
      let headerParams = {
        'Content-Range': contentRange,
        'Content-Length': contentLength
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['application/octet-stream'];
      let accepts = ['application/json'];
      let returnType = VideoUploadResponse;
      return this.apiClient.callApi(
        '/api/v1/videos/upload-resumable', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the uploadResumableCancel operation.
     * @callback module:api/VideoApi~uploadResumableCancelCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cancel the resumable upload of a video, deleting any data uploaded so far
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video
     * @param {String} uploadId Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
     * @param {Number} contentLength 
     * @param {module:api/VideoApi~uploadResumableCancelCallback} callback The callback function, accepting three arguments: error, data, response
     */
    uploadResumableCancel(uploadId, contentLength, callback) {
      let postBody = null;
      // verify the required parameter 'uploadId' is set
      if (uploadId === undefined || uploadId === null) {
        throw new Error("Missing the required parameter 'uploadId' when calling uploadResumableCancel");
      }
      // verify the required parameter 'contentLength' is set
      if (contentLength === undefined || contentLength === null) {
        throw new Error("Missing the required parameter 'contentLength' when calling uploadResumableCancel");
      }

      let pathParams = {
      };
      let queryParams = {
        'upload_id': uploadId
      };
      let headerParams = {
        'Content-Length': contentLength
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/videos/upload-resumable', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the uploadResumableInit operation.
     * @callback module:api/VideoApi~uploadResumableInitCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Initialize the resumable upload of a video
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video
     * @param {Number} xUploadContentLength Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.
     * @param {String} xUploadContentType MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.
     * @param {Object} opts Optional parameters
     * @param {module:model/VideoUploadRequestResumable} [videoUploadRequestResumable] 
     * @param {module:api/VideoApi~uploadResumableInitCallback} callback The callback function, accepting three arguments: error, data, response
     */
    uploadResumableInit(xUploadContentLength, xUploadContentType, opts, callback) {
      opts = opts || {};
      let postBody = opts['videoUploadRequestResumable'];
      // verify the required parameter 'xUploadContentLength' is set
      if (xUploadContentLength === undefined || xUploadContentLength === null) {
        throw new Error("Missing the required parameter 'xUploadContentLength' when calling uploadResumableInit");
      }
      // verify the required parameter 'xUploadContentType' is set
      if (xUploadContentType === undefined || xUploadContentType === null) {
        throw new Error("Missing the required parameter 'xUploadContentType' when calling uploadResumableInit");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Upload-Content-Length': xUploadContentLength,
        'X-Upload-Content-Type': xUploadContentType
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/videos/upload-resumable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
