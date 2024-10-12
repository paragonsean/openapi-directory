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
import ApiV1AccountsNameVideoPlaylistsGet200Response from '../model/ApiV1AccountsNameVideoPlaylistsGet200Response';
import GetAccountVideosCategoryOneOfParameter from '../model/GetAccountVideosCategoryOneOfParameter';
import GetAccountVideosLanguageOneOfParameter from '../model/GetAccountVideosLanguageOneOfParameter';
import GetAccountVideosLicenceOneOfParameter from '../model/GetAccountVideosLicenceOneOfParameter';
import GetAccountVideosTagsAllOfParameter from '../model/GetAccountVideosTagsAllOfParameter';
import GetAccountVideosTagsOneOfParameter from '../model/GetAccountVideosTagsOneOfParameter';
import VideoChannelList from '../model/VideoChannelList';
import VideoListResponse from '../model/VideoListResponse';
import VideoPrivacySet from '../model/VideoPrivacySet';

/**
* Search service.
* @module api/SearchApi
* @version 5.1.0
*/
export default class SearchApi {

    /**
    * Constructs a new SearchApi. 
    * @alias module:api/SearchApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the searchChannels operation.
     * @callback module:api/SearchApi~searchChannelsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoChannelList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search channels
     * @param {String} search String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete channel information and interact with it. 
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:model/String} [searchTarget] If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
     * @param {String} [sort] Sort column
     * @param {module:api/SearchApi~searchChannelsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoChannelList}
     */
    searchChannels(search, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'search' is set
      if (search === undefined || search === null) {
        throw new Error("Missing the required parameter 'search' when calling searchChannels");
      }

      let pathParams = {
      };
      let queryParams = {
        'search': search,
        'start': opts['start'],
        'count': opts['count'],
        'searchTarget': opts['searchTarget'],
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
        '/api/v1/search/video-channels', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the searchPlaylists operation.
     * @callback module:api/SearchApi~searchPlaylistsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApiV1AccountsNameVideoPlaylistsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search playlists
     * @param {String} search String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete playlist information and interact with it. 
     * @param {Object} opts Optional parameters
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:model/String} [searchTarget] If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
     * @param {String} [sort] Sort column
     * @param {module:api/SearchApi~searchPlaylistsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApiV1AccountsNameVideoPlaylistsGet200Response}
     */
    searchPlaylists(search, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'search' is set
      if (search === undefined || search === null) {
        throw new Error("Missing the required parameter 'search' when calling searchPlaylists");
      }

      let pathParams = {
      };
      let queryParams = {
        'search': search,
        'start': opts['start'],
        'count': opts['count'],
        'searchTarget': opts['searchTarget'],
        'sort': opts['sort']
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
        '/api/v1/search/video-playlists', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the searchVideos operation.
     * @callback module:api/SearchApi~searchVideosCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoListResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search videos
     * @param {String} search String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete video information and interact with it. 
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
     * @param {Array.<String>} [uuids] Find videos with specific UUIDs
     * @param {Boolean} [hasHLSFiles] **PeerTube >= 4.0** Display only videos that have HLS files
     * @param {Boolean} [hasWebtorrentFiles] **PeerTube >= 4.0** Display only videos that have WebTorrent files
     * @param {module:model/String} [skipCount = 'false')] if you don't need the `total` in the response
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {module:model/String} [searchTarget] If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
     * @param {module:model/String} [sort] Sort videos by criteria (prefixing with `-` means `DESC` order): 
     * @param {Boolean} [excludeAlreadyWatched] Whether or not to exclude videos that are in the user's video history
     * @param {Date} [startDate] Get videos that are published after this date
     * @param {Date} [endDate] Get videos that are published before this date
     * @param {Date} [originallyPublishedStartDate] Get videos that are originally published after this date
     * @param {Date} [originallyPublishedEndDate] Get videos that are originally published before this date
     * @param {Number} [durationMin] Get videos that have this minimum duration
     * @param {Number} [durationMax] Get videos that have this maximum duration
     * @param {module:api/SearchApi~searchVideosCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoListResponse}
     */
    searchVideos(search, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'search' is set
      if (search === undefined || search === null) {
        throw new Error("Missing the required parameter 'search' when calling searchVideos");
      }

      let pathParams = {
      };
      let queryParams = {
        'search': search,
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
        'uuids': this.apiClient.buildCollectionParam(opts['uuids'], 'multi'),
        'hasHLSFiles': opts['hasHLSFiles'],
        'hasWebtorrentFiles': opts['hasWebtorrentFiles'],
        'skipCount': opts['skipCount'],
        'start': opts['start'],
        'count': opts['count'],
        'searchTarget': opts['searchTarget'],
        'sort': opts['sort'],
        'excludeAlreadyWatched': opts['excludeAlreadyWatched'],
        'startDate': opts['startDate'],
        'endDate': opts['endDate'],
        'originallyPublishedStartDate': opts['originallyPublishedStartDate'],
        'originallyPublishedEndDate': opts['originallyPublishedEndDate'],
        'durationMin': opts['durationMin'],
        'durationMax': opts['durationMax']
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
        '/api/v1/search/videos', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
