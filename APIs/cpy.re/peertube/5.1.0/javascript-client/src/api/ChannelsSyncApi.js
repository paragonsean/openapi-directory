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
import AddVideoChannelSync200Response from '../model/AddVideoChannelSync200Response';
import ImportVideosInChannelCreate from '../model/ImportVideosInChannelCreate';
import VideoChannelSyncCreate from '../model/VideoChannelSyncCreate';
import VideoChannelSyncList from '../model/VideoChannelSyncList';

/**
* ChannelsSync service.
* @module api/ChannelsSyncApi
* @version 5.1.0
*/
export default class ChannelsSyncApi {

    /**
    * Constructs a new ChannelsSyncApi. 
    * @alias module:api/ChannelsSyncApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addVideoChannelSync operation.
     * @callback module:api/ChannelsSyncApi~addVideoChannelSyncCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AddVideoChannelSync200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a synchronization for a video channel
     * @param {Object} opts Optional parameters
     * @param {module:model/VideoChannelSyncCreate} [videoChannelSyncCreate] 
     * @param {module:api/ChannelsSyncApi~addVideoChannelSyncCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AddVideoChannelSync200Response}
     */
    addVideoChannelSync(opts, callback) {
      opts = opts || {};
      let postBody = opts['videoChannelSyncCreate'];

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
      let returnType = AddVideoChannelSync200Response;
      return this.apiClient.callApi(
        '/api/v1/video-channel-syncs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1AccountsNameVideoChannelSyncsGet_0 operation.
     * @callback module:api/ChannelsSyncApi~apiV1AccountsNameVideoChannelSyncsGet_0Callback
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
     * @param {module:api/ChannelsSyncApi~apiV1AccountsNameVideoChannelSyncsGet_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoChannelSyncList}
     */
    apiV1AccountsNameVideoChannelSyncsGet_0(name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling apiV1AccountsNameVideoChannelSyncsGet_0");
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
     * Callback function to receive the result of the apiV1VideoChannelsChannelHandleImportVideosPost_0 operation.
     * @callback module:api/ChannelsSyncApi~apiV1VideoChannelsChannelHandleImportVideosPost_0Callback
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
     * @param {module:api/ChannelsSyncApi~apiV1VideoChannelsChannelHandleImportVideosPost_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1VideoChannelsChannelHandleImportVideosPost_0(channelHandle, opts, callback) {
      opts = opts || {};
      let postBody = opts['importVideosInChannelCreate'];
      // verify the required parameter 'channelHandle' is set
      if (channelHandle === undefined || channelHandle === null) {
        throw new Error("Missing the required parameter 'channelHandle' when calling apiV1VideoChannelsChannelHandleImportVideosPost_0");
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
     * Callback function to receive the result of the delVideoChannelSync operation.
     * @callback module:api/ChannelsSyncApi~delVideoChannelSyncCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a video channel synchronization
     * @param {Number} channelSyncId Channel Sync id
     * @param {module:api/ChannelsSyncApi~delVideoChannelSyncCallback} callback The callback function, accepting three arguments: error, data, response
     */
    delVideoChannelSync(channelSyncId, callback) {
      let postBody = null;
      // verify the required parameter 'channelSyncId' is set
      if (channelSyncId === undefined || channelSyncId === null) {
        throw new Error("Missing the required parameter 'channelSyncId' when calling delVideoChannelSync");
      }

      let pathParams = {
        'channelSyncId': channelSyncId
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
        '/api/v1/video-channel-syncs/{channelSyncId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the triggerVideoChannelSync operation.
     * @callback module:api/ChannelsSyncApi~triggerVideoChannelSyncCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Triggers the channel synchronization job, fetching all the videos from the remote channel
     * @param {Number} channelSyncId Channel Sync id
     * @param {module:api/ChannelsSyncApi~triggerVideoChannelSyncCallback} callback The callback function, accepting three arguments: error, data, response
     */
    triggerVideoChannelSync(channelSyncId, callback) {
      let postBody = null;
      // verify the required parameter 'channelSyncId' is set
      if (channelSyncId === undefined || channelSyncId === null) {
        throw new Error("Missing the required parameter 'channelSyncId' when calling triggerVideoChannelSync");
      }

      let pathParams = {
        'channelSyncId': channelSyncId
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
        '/api/v1/video-channel-syncs/{channelSyncId}/sync', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
