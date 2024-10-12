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

import ApiClient from '../ApiClient';
import VideoResolutionConstant from './VideoResolutionConstant';

/**
 * The VideoFile model module.
 * @module model/VideoFile
 * @version 5.1.0
 */
class VideoFile {
    /**
     * Constructs a new <code>VideoFile</code>.
     * @alias module:model/VideoFile
     */
    constructor() { 
        
        VideoFile.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VideoFile</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VideoFile} obj Optional instance to populate.
     * @return {module:model/VideoFile} The populated <code>VideoFile</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VideoFile();

            if (data.hasOwnProperty('fileDownloadUrl')) {
                obj['fileDownloadUrl'] = ApiClient.convertToType(data['fileDownloadUrl'], 'String');
            }
            if (data.hasOwnProperty('fileUrl')) {
                obj['fileUrl'] = ApiClient.convertToType(data['fileUrl'], 'String');
            }
            if (data.hasOwnProperty('fps')) {
                obj['fps'] = ApiClient.convertToType(data['fps'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('magnetUri')) {
                obj['magnetUri'] = ApiClient.convertToType(data['magnetUri'], 'String');
            }
            if (data.hasOwnProperty('metadataUrl')) {
                obj['metadataUrl'] = ApiClient.convertToType(data['metadataUrl'], 'String');
            }
            if (data.hasOwnProperty('resolution')) {
                obj['resolution'] = VideoResolutionConstant.constructFromObject(data['resolution']);
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'Number');
            }
            if (data.hasOwnProperty('torrentDownloadUrl')) {
                obj['torrentDownloadUrl'] = ApiClient.convertToType(data['torrentDownloadUrl'], 'String');
            }
            if (data.hasOwnProperty('torrentUrl')) {
                obj['torrentUrl'] = ApiClient.convertToType(data['torrentUrl'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VideoFile</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VideoFile</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['fileDownloadUrl'] && !(typeof data['fileDownloadUrl'] === 'string' || data['fileDownloadUrl'] instanceof String)) {
            throw new Error("Expected the field `fileDownloadUrl` to be a primitive type in the JSON string but got " + data['fileDownloadUrl']);
        }
        // ensure the json data is a string
        if (data['fileUrl'] && !(typeof data['fileUrl'] === 'string' || data['fileUrl'] instanceof String)) {
            throw new Error("Expected the field `fileUrl` to be a primitive type in the JSON string but got " + data['fileUrl']);
        }
        // ensure the json data is a string
        if (data['magnetUri'] && !(typeof data['magnetUri'] === 'string' || data['magnetUri'] instanceof String)) {
            throw new Error("Expected the field `magnetUri` to be a primitive type in the JSON string but got " + data['magnetUri']);
        }
        // ensure the json data is a string
        if (data['metadataUrl'] && !(typeof data['metadataUrl'] === 'string' || data['metadataUrl'] instanceof String)) {
            throw new Error("Expected the field `metadataUrl` to be a primitive type in the JSON string but got " + data['metadataUrl']);
        }
        // validate the optional field `resolution`
        if (data['resolution']) { // data not null
          VideoResolutionConstant.validateJSON(data['resolution']);
        }
        // ensure the json data is a string
        if (data['torrentDownloadUrl'] && !(typeof data['torrentDownloadUrl'] === 'string' || data['torrentDownloadUrl'] instanceof String)) {
            throw new Error("Expected the field `torrentDownloadUrl` to be a primitive type in the JSON string but got " + data['torrentDownloadUrl']);
        }
        // ensure the json data is a string
        if (data['torrentUrl'] && !(typeof data['torrentUrl'] === 'string' || data['torrentUrl'] instanceof String)) {
            throw new Error("Expected the field `torrentUrl` to be a primitive type in the JSON string but got " + data['torrentUrl']);
        }

        return true;
    }


}



/**
 * URL endpoint that transfers the video file as an attachment (so that the browser opens a download dialog)
 * @member {String} fileDownloadUrl
 */
VideoFile.prototype['fileDownloadUrl'] = undefined;

/**
 * Direct URL of the video
 * @member {String} fileUrl
 */
VideoFile.prototype['fileUrl'] = undefined;

/**
 * Frames per second of the video file
 * @member {Number} fps
 */
VideoFile.prototype['fps'] = undefined;

/**
 * @member {Number} id
 */
VideoFile.prototype['id'] = undefined;

/**
 * magnet URI allowing to resolve the video via BitTorrent without a metainfo file
 * @member {String} magnetUri
 */
VideoFile.prototype['magnetUri'] = undefined;

/**
 * URL dereferencing the output of ffprobe on the file
 * @member {String} metadataUrl
 */
VideoFile.prototype['metadataUrl'] = undefined;

/**
 * @member {module:model/VideoResolutionConstant} resolution
 */
VideoFile.prototype['resolution'] = undefined;

/**
 * Video file size in bytes
 * @member {Number} size
 */
VideoFile.prototype['size'] = undefined;

/**
 * URL endpoint that transfers the torrent file as an attachment (so that the browser opens a download dialog)
 * @member {String} torrentDownloadUrl
 */
VideoFile.prototype['torrentDownloadUrl'] = undefined;

/**
 * Direct URL of the torrent file
 * @member {String} torrentUrl
 */
VideoFile.prototype['torrentUrl'] = undefined;






export default VideoFile;

