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
import ServerConfigCustomTranscodingHls from './ServerConfigCustomTranscodingHls';
import ServerConfigCustomTranscodingResolutions from './ServerConfigCustomTranscodingResolutions';
import ServerConfigCustomTranscodingWebtorrent from './ServerConfigCustomTranscodingWebtorrent';

/**
 * The ServerConfigCustomTranscoding model module.
 * @module model/ServerConfigCustomTranscoding
 * @version 5.1.0
 */
class ServerConfigCustomTranscoding {
    /**
     * Constructs a new <code>ServerConfigCustomTranscoding</code>.
     * Settings pertaining to transcoding jobs
     * @alias module:model/ServerConfigCustomTranscoding
     */
    constructor() { 
        
        ServerConfigCustomTranscoding.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ServerConfigCustomTranscoding</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServerConfigCustomTranscoding} obj Optional instance to populate.
     * @return {module:model/ServerConfigCustomTranscoding} The populated <code>ServerConfigCustomTranscoding</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServerConfigCustomTranscoding();

            if (data.hasOwnProperty('allowAdditionalExtensions')) {
                obj['allowAdditionalExtensions'] = ApiClient.convertToType(data['allowAdditionalExtensions'], 'Boolean');
            }
            if (data.hasOwnProperty('allowAudioFiles')) {
                obj['allowAudioFiles'] = ApiClient.convertToType(data['allowAudioFiles'], 'Boolean');
            }
            if (data.hasOwnProperty('concurrency')) {
                obj['concurrency'] = ApiClient.convertToType(data['concurrency'], 'Number');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('hls')) {
                obj['hls'] = ServerConfigCustomTranscodingHls.constructFromObject(data['hls']);
            }
            if (data.hasOwnProperty('profile')) {
                obj['profile'] = ApiClient.convertToType(data['profile'], 'String');
            }
            if (data.hasOwnProperty('resolutions')) {
                obj['resolutions'] = ServerConfigCustomTranscodingResolutions.constructFromObject(data['resolutions']);
            }
            if (data.hasOwnProperty('threads')) {
                obj['threads'] = ApiClient.convertToType(data['threads'], 'Number');
            }
            if (data.hasOwnProperty('webtorrent')) {
                obj['webtorrent'] = ServerConfigCustomTranscodingWebtorrent.constructFromObject(data['webtorrent']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServerConfigCustomTranscoding</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServerConfigCustomTranscoding</code>.
     */
    static validateJSON(data) {
        // validate the optional field `hls`
        if (data['hls']) { // data not null
          ServerConfigCustomTranscodingHls.validateJSON(data['hls']);
        }
        // ensure the json data is a string
        if (data['profile'] && !(typeof data['profile'] === 'string' || data['profile'] instanceof String)) {
            throw new Error("Expected the field `profile` to be a primitive type in the JSON string but got " + data['profile']);
        }
        // validate the optional field `resolutions`
        if (data['resolutions']) { // data not null
          ServerConfigCustomTranscodingResolutions.validateJSON(data['resolutions']);
        }
        // validate the optional field `webtorrent`
        if (data['webtorrent']) { // data not null
          ServerConfigCustomTranscodingWebtorrent.validateJSON(data['webtorrent']);
        }

        return true;
    }


}



/**
 * Allow your users to upload .mkv, .mov, .avi, .wmv, .flv, .f4v, .3g2, .3gp, .mts, m2ts, .mxf, .nut videos
 * @member {Boolean} allowAdditionalExtensions
 */
ServerConfigCustomTranscoding.prototype['allowAdditionalExtensions'] = undefined;

/**
 * If a user uploads an audio file, PeerTube will create a video by merging the preview file and the audio file
 * @member {Boolean} allowAudioFiles
 */
ServerConfigCustomTranscoding.prototype['allowAudioFiles'] = undefined;

/**
 * Amount of transcoding jobs to execute in parallel
 * @member {Number} concurrency
 */
ServerConfigCustomTranscoding.prototype['concurrency'] = undefined;

/**
 * @member {Boolean} enabled
 */
ServerConfigCustomTranscoding.prototype['enabled'] = undefined;

/**
 * @member {module:model/ServerConfigCustomTranscodingHls} hls
 */
ServerConfigCustomTranscoding.prototype['hls'] = undefined;

/**
 * New profiles can be added by plugins ; available in core PeerTube: 'default'. 
 * @member {module:model/ServerConfigCustomTranscoding.ProfileEnum} profile
 */
ServerConfigCustomTranscoding.prototype['profile'] = undefined;

/**
 * @member {module:model/ServerConfigCustomTranscodingResolutions} resolutions
 */
ServerConfigCustomTranscoding.prototype['resolutions'] = undefined;

/**
 * Amount of threads used by ffmpeg for 1 transcoding job
 * @member {Number} threads
 */
ServerConfigCustomTranscoding.prototype['threads'] = undefined;

/**
 * @member {module:model/ServerConfigCustomTranscodingWebtorrent} webtorrent
 */
ServerConfigCustomTranscoding.prototype['webtorrent'] = undefined;





/**
 * Allowed values for the <code>profile</code> property.
 * @enum {String}
 * @readonly
 */
ServerConfigCustomTranscoding['ProfileEnum'] = {

    /**
     * value: "default"
     * @const
     */
    "default": "default"
};



export default ServerConfigCustomTranscoding;

