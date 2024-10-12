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
import VideoCommentsForXMLInner from '../model/VideoCommentsForXMLInner';
import VideoPrivacySet from '../model/VideoPrivacySet';
import VideosForXMLInner from '../model/VideosForXMLInner';

/**
* VideoFeeds service.
* @module api/VideoFeedsApi
* @version 5.1.0
*/
export default class VideoFeedsApi {

    /**
    * Constructs a new VideoFeedsApi. 
    * @alias module:api/VideoFeedsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getSyndicatedComments operation.
     * @callback module:api/VideoFeedsApi~getSyndicatedCommentsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/VideoCommentsForXMLInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List comments on videos
     * @param {module:model/String} format format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
     * @param {Object} opts Optional parameters
     * @param {String} [videoId] limit listing to a specific video
     * @param {String} [accountId] limit listing to a specific account
     * @param {String} [accountName] limit listing to a specific account
     * @param {String} [videoChannelId] limit listing to a specific video channel
     * @param {String} [videoChannelName] limit listing to a specific video channel
     * @param {module:api/VideoFeedsApi~getSyndicatedCommentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/VideoCommentsForXMLInner>}
     */
    getSyndicatedComments(format, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling getSyndicatedComments");
      }

      let pathParams = {
        'format': format
      };
      let queryParams = {
        'videoId': opts['videoId'],
        'accountId': opts['accountId'],
        'accountName': opts['accountName'],
        'videoChannelId': opts['videoChannelId'],
        'videoChannelName': opts['videoChannelName']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/atom+xml', 'application/json', 'application/rss+xml', 'application/xml', 'text/xml'];
      let returnType = [VideoCommentsForXMLInner];
      return this.apiClient.callApi(
        '/feeds/video-comments.{format}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSyndicatedSubscriptionVideos operation.
     * @callback module:api/VideoFeedsApi~getSyndicatedSubscriptionVideosCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/VideosForXMLInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videos of subscriptions tied to a token
     * @param {module:model/String} format format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
     * @param {String} accountId limit listing to a specific account
     * @param {String} token private token allowing access
     * @param {Object} opts Optional parameters
     * @param {String} [sort] Sort column
     * @param {module:model/String} [nsfw] whether to include nsfw videos, if any
     * @param {Boolean} [isLocal] **PeerTube >= 4.0** Display only local or remote videos
     * @param {module:model/Number} [include] **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
     * @param {module:model/VideoPrivacySet} [privacyOneOf] **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
     * @param {Boolean} [hasHLSFiles] **PeerTube >= 4.0** Display only videos that have HLS files
     * @param {Boolean} [hasWebtorrentFiles] **PeerTube >= 4.0** Display only videos that have WebTorrent files
     * @param {module:api/VideoFeedsApi~getSyndicatedSubscriptionVideosCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/VideosForXMLInner>}
     */
    getSyndicatedSubscriptionVideos(format, accountId, token, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling getSyndicatedSubscriptionVideos");
      }
      // verify the required parameter 'accountId' is set
      if (accountId === undefined || accountId === null) {
        throw new Error("Missing the required parameter 'accountId' when calling getSyndicatedSubscriptionVideos");
      }
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling getSyndicatedSubscriptionVideos");
      }

      let pathParams = {
        'format': format
      };
      let queryParams = {
        'accountId': accountId,
        'token': token,
        'sort': opts['sort'],
        'nsfw': opts['nsfw'],
        'isLocal': opts['isLocal'],
        'include': opts['include'],
        'privacyOneOf': opts['privacyOneOf'],
        'hasHLSFiles': opts['hasHLSFiles'],
        'hasWebtorrentFiles': opts['hasWebtorrentFiles']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/atom+xml', 'application/json', 'application/rss+xml', 'application/xml', 'text/xml'];
      let returnType = [VideosForXMLInner];
      return this.apiClient.callApi(
        '/feeds/subscriptions.{format}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSyndicatedVideos operation.
     * @callback module:api/VideoFeedsApi~getSyndicatedVideosCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/VideosForXMLInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videos
     * @param {module:model/String} format format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
     * @param {Object} opts Optional parameters
     * @param {String} [accountId] limit listing to a specific account
     * @param {String} [accountName] limit listing to a specific account
     * @param {String} [videoChannelId] limit listing to a specific video channel
     * @param {String} [videoChannelName] limit listing to a specific video channel
     * @param {String} [sort] Sort column
     * @param {module:model/String} [nsfw] whether to include nsfw videos, if any
     * @param {Boolean} [isLocal] **PeerTube >= 4.0** Display only local or remote videos
     * @param {module:model/Number} [include] **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
     * @param {module:model/VideoPrivacySet} [privacyOneOf] **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
     * @param {Boolean} [hasHLSFiles] **PeerTube >= 4.0** Display only videos that have HLS files
     * @param {Boolean} [hasWebtorrentFiles] **PeerTube >= 4.0** Display only videos that have WebTorrent files
     * @param {module:api/VideoFeedsApi~getSyndicatedVideosCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/VideosForXMLInner>}
     */
    getSyndicatedVideos(format, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling getSyndicatedVideos");
      }

      let pathParams = {
        'format': format
      };
      let queryParams = {
        'accountId': opts['accountId'],
        'accountName': opts['accountName'],
        'videoChannelId': opts['videoChannelId'],
        'videoChannelName': opts['videoChannelName'],
        'sort': opts['sort'],
        'nsfw': opts['nsfw'],
        'isLocal': opts['isLocal'],
        'include': opts['include'],
        'privacyOneOf': opts['privacyOneOf'],
        'hasHLSFiles': opts['hasHLSFiles'],
        'hasWebtorrentFiles': opts['hasWebtorrentFiles']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/atom+xml', 'application/json', 'application/rss+xml', 'application/xml', 'text/xml'];
      let returnType = [VideosForXMLInner];
      return this.apiClient.callApi(
        '/feeds/videos.{format}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
