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
import VideoFile from './VideoFile';
import VideoStreamingPlaylistsHLS from './VideoStreamingPlaylistsHLS';
import VideoStreamingPlaylistsHLSRedundanciesInner from './VideoStreamingPlaylistsHLSRedundanciesInner';

/**
 * The VideoStreamingPlaylists model module.
 * @module model/VideoStreamingPlaylists
 * @version 5.1.0
 */
class VideoStreamingPlaylists {
    /**
     * Constructs a new <code>VideoStreamingPlaylists</code>.
     * @alias module:model/VideoStreamingPlaylists
     * @implements module:model/VideoStreamingPlaylistsHLS
     */
    constructor() { 
        VideoStreamingPlaylistsHLS.initialize(this);
        VideoStreamingPlaylists.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VideoStreamingPlaylists</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VideoStreamingPlaylists} obj Optional instance to populate.
     * @return {module:model/VideoStreamingPlaylists} The populated <code>VideoStreamingPlaylists</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VideoStreamingPlaylists();
            VideoStreamingPlaylistsHLS.constructFromObject(data, obj);

            if (data.hasOwnProperty('files')) {
                obj['files'] = ApiClient.convertToType(data['files'], [VideoFile]);
            }
            if (data.hasOwnProperty('playlistUrl')) {
                obj['playlistUrl'] = ApiClient.convertToType(data['playlistUrl'], 'String');
            }
            if (data.hasOwnProperty('redundancies')) {
                obj['redundancies'] = ApiClient.convertToType(data['redundancies'], [VideoStreamingPlaylistsHLSRedundanciesInner]);
            }
            if (data.hasOwnProperty('segmentsSha256Url')) {
                obj['segmentsSha256Url'] = ApiClient.convertToType(data['segmentsSha256Url'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VideoStreamingPlaylists</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VideoStreamingPlaylists</code>.
     */
    static validateJSON(data) {
        if (data['files']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['files'])) {
                throw new Error("Expected the field `files` to be an array in the JSON data but got " + data['files']);
            }
            // validate the optional field `files` (array)
            for (const item of data['files']) {
                VideoFile.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['playlistUrl'] && !(typeof data['playlistUrl'] === 'string' || data['playlistUrl'] instanceof String)) {
            throw new Error("Expected the field `playlistUrl` to be a primitive type in the JSON string but got " + data['playlistUrl']);
        }
        if (data['redundancies']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['redundancies'])) {
                throw new Error("Expected the field `redundancies` to be an array in the JSON data but got " + data['redundancies']);
            }
            // validate the optional field `redundancies` (array)
            for (const item of data['redundancies']) {
                VideoStreamingPlaylistsHLSRedundanciesInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['segmentsSha256Url'] && !(typeof data['segmentsSha256Url'] === 'string' || data['segmentsSha256Url'] instanceof String)) {
            throw new Error("Expected the field `segmentsSha256Url` to be a primitive type in the JSON string but got " + data['segmentsSha256Url']);
        }

        return true;
    }


}



/**
 * Video files associated to this playlist.  The difference with the root `files` property is that these files are fragmented, so they can be used in this streaming playlist (HLS, etc.) 
 * @member {Array.<module:model/VideoFile>} files
 */
VideoStreamingPlaylists.prototype['files'] = undefined;

/**
 * @member {String} playlistUrl
 */
VideoStreamingPlaylists.prototype['playlistUrl'] = undefined;

/**
 * @member {Array.<module:model/VideoStreamingPlaylistsHLSRedundanciesInner>} redundancies
 */
VideoStreamingPlaylists.prototype['redundancies'] = undefined;

/**
 * @member {String} segmentsSha256Url
 */
VideoStreamingPlaylists.prototype['segmentsSha256Url'] = undefined;

/**
 * @member {Number} id
 */
VideoStreamingPlaylists.prototype['id'] = undefined;

/**
 * Playlist type: - `1`: HLS 
 * @member {module:model/VideoStreamingPlaylists.TypeEnum} type
 */
VideoStreamingPlaylists.prototype['type'] = undefined;


// Implement VideoStreamingPlaylistsHLS interface:
/**
 * Video files associated to this playlist.  The difference with the root `files` property is that these files are fragmented, so they can be used in this streaming playlist (HLS, etc.) 
 * @member {Array.<module:model/VideoFile>} files
 */
VideoStreamingPlaylistsHLS.prototype['files'] = undefined;
/**
 * @member {String} playlistUrl
 */
VideoStreamingPlaylistsHLS.prototype['playlistUrl'] = undefined;
/**
 * @member {Array.<module:model/VideoStreamingPlaylistsHLSRedundanciesInner>} redundancies
 */
VideoStreamingPlaylistsHLS.prototype['redundancies'] = undefined;
/**
 * @member {String} segmentsSha256Url
 */
VideoStreamingPlaylistsHLS.prototype['segmentsSha256Url'] = undefined;



/**
 * Allowed values for the <code>type</code> property.
 * @enum {Number}
 * @readonly
 */
VideoStreamingPlaylists['TypeEnum'] = {

    /**
     * value: 1
     * @const
     */
    "1": 1
};



export default VideoStreamingPlaylists;

