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
import VideoPrivacySet from '../model/VideoPrivacySet';
import VideoScheduledUpdate from '../model/VideoScheduledUpdate';
import VideoUploadRequestResumable from '../model/VideoUploadRequestResumable';
import VideoUploadResponse from '../model/VideoUploadResponse';

/**
* VideoUpload service.
* @module api/VideoUploadApi
* @version 5.1.0
*/
export default class VideoUploadApi {

    /**
    * Constructs a new VideoUploadApi. 
    * @alias module:api/VideoUploadApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the importVideo_0 operation.
     * @callback module:api/VideoUploadApi~importVideo_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/VideoUploadResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Import a video
     * Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)
     * @param {Number} channelId Channel id that will contain this video
     * @param {String} name Video name
     * @param {Object} opts Optional parameters
     * @param {String} [targetUrl] remote URL where to find the import's source video
     * @param {String} [magnetUri] magnet URI allowing to resolve the import's source video
     * @param {File} [torrentfile] Torrent file containing only the video file
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
     * @param {module:api/VideoUploadApi~importVideo_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoUploadResponse}
     */
    importVideo_0(channelId, name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelId' is set
      if (channelId === undefined || channelId === null) {
        throw new Error("Missing the required parameter 'channelId' when calling importVideo_0");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling importVideo_0");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'targetUrl': opts['targetUrl'],
        'magnetUri': opts['magnetUri'],
        'torrentfile': opts['torrentfile'],
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
        'waitTranscoding': opts['waitTranscoding']
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = VideoUploadResponse;
      return this.apiClient.callApi(
        '/api/v1/videos/imports', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the uploadLegacy_0 operation.
     * @callback module:api/VideoUploadApi~uploadLegacy_0Callback
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
     * @param {module:api/VideoUploadApi~uploadLegacy_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoUploadResponse}
     */
    uploadLegacy_0(channelId, name, videofile, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'channelId' is set
      if (channelId === undefined || channelId === null) {
        throw new Error("Missing the required parameter 'channelId' when calling uploadLegacy_0");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling uploadLegacy_0");
      }
      // verify the required parameter 'videofile' is set
      if (videofile === undefined || videofile === null) {
        throw new Error("Missing the required parameter 'videofile' when calling uploadLegacy_0");
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
     * Callback function to receive the result of the uploadResumableCancel_0 operation.
     * @callback module:api/VideoUploadApi~uploadResumableCancel_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cancel the resumable upload of a video, deleting any data uploaded so far
     * Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video
     * @param {String} uploadId Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
     * @param {Number} contentLength 
     * @param {module:api/VideoUploadApi~uploadResumableCancel_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    uploadResumableCancel_0(uploadId, contentLength, callback) {
      let postBody = null;
      // verify the required parameter 'uploadId' is set
      if (uploadId === undefined || uploadId === null) {
        throw new Error("Missing the required parameter 'uploadId' when calling uploadResumableCancel_0");
      }
      // verify the required parameter 'contentLength' is set
      if (contentLength === undefined || contentLength === null) {
        throw new Error("Missing the required parameter 'contentLength' when calling uploadResumableCancel_0");
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
     * Callback function to receive the result of the uploadResumableInit_0 operation.
     * @callback module:api/VideoUploadApi~uploadResumableInit_0Callback
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
     * @param {module:api/VideoUploadApi~uploadResumableInit_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    uploadResumableInit_0(xUploadContentLength, xUploadContentType, opts, callback) {
      opts = opts || {};
      let postBody = opts['videoUploadRequestResumable'];
      // verify the required parameter 'xUploadContentLength' is set
      if (xUploadContentLength === undefined || xUploadContentLength === null) {
        throw new Error("Missing the required parameter 'xUploadContentLength' when calling uploadResumableInit_0");
      }
      // verify the required parameter 'xUploadContentType' is set
      if (xUploadContentType === undefined || xUploadContentType === null) {
        throw new Error("Missing the required parameter 'xUploadContentType' when calling uploadResumableInit_0");
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

    /**
     * Callback function to receive the result of the uploadResumable_0 operation.
     * @callback module:api/VideoUploadApi~uploadResumable_0Callback
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
     * @param {module:api/VideoUploadApi~uploadResumable_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VideoUploadResponse}
     */
    uploadResumable_0(uploadId, contentRange, contentLength, opts, callback) {
      opts = opts || {};
      let postBody = opts['body'];
      // verify the required parameter 'uploadId' is set
      if (uploadId === undefined || uploadId === null) {
        throw new Error("Missing the required parameter 'uploadId' when calling uploadResumable_0");
      }
      // verify the required parameter 'contentRange' is set
      if (contentRange === undefined || contentRange === null) {
        throw new Error("Missing the required parameter 'contentRange' when calling uploadResumable_0");
      }
      // verify the required parameter 'contentLength' is set
      if (contentLength === undefined || contentLength === null) {
        throw new Error("Missing the required parameter 'contentLength' when calling uploadResumable_0");
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


}
