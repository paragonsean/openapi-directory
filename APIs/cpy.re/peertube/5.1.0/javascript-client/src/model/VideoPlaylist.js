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
import AccountSummary from './AccountSummary';
import VideoChannelSummary from './VideoChannelSummary';
import VideoPlaylistPrivacyConstant from './VideoPlaylistPrivacyConstant';
import VideoPlaylistTypeConstant from './VideoPlaylistTypeConstant';

/**
 * The VideoPlaylist model module.
 * @module model/VideoPlaylist
 * @version 5.1.0
 */
class VideoPlaylist {
    /**
     * Constructs a new <code>VideoPlaylist</code>.
     * @alias module:model/VideoPlaylist
     */
    constructor() { 
        
        VideoPlaylist.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VideoPlaylist</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VideoPlaylist} obj Optional instance to populate.
     * @return {module:model/VideoPlaylist} The populated <code>VideoPlaylist</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VideoPlaylist();

            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('displayName')) {
                obj['displayName'] = ApiClient.convertToType(data['displayName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('isLocal')) {
                obj['isLocal'] = ApiClient.convertToType(data['isLocal'], 'Boolean');
            }
            if (data.hasOwnProperty('ownerAccount')) {
                obj['ownerAccount'] = AccountSummary.constructFromObject(data['ownerAccount']);
            }
            if (data.hasOwnProperty('privacy')) {
                obj['privacy'] = VideoPlaylistPrivacyConstant.constructFromObject(data['privacy']);
            }
            if (data.hasOwnProperty('shortUUID')) {
                obj['shortUUID'] = ApiClient.convertToType(data['shortUUID'], 'String');
            }
            if (data.hasOwnProperty('thumbnailPath')) {
                obj['thumbnailPath'] = ApiClient.convertToType(data['thumbnailPath'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = VideoPlaylistTypeConstant.constructFromObject(data['type']);
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('uuid')) {
                obj['uuid'] = ApiClient.convertToType(data['uuid'], 'String');
            }
            if (data.hasOwnProperty('videoChannel')) {
                obj['videoChannel'] = VideoChannelSummary.constructFromObject(data['videoChannel']);
            }
            if (data.hasOwnProperty('videoLength')) {
                obj['videoLength'] = ApiClient.convertToType(data['videoLength'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VideoPlaylist</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VideoPlaylist</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['displayName'] && !(typeof data['displayName'] === 'string' || data['displayName'] instanceof String)) {
            throw new Error("Expected the field `displayName` to be a primitive type in the JSON string but got " + data['displayName']);
        }
        // validate the optional field `ownerAccount`
        if (data['ownerAccount']) { // data not null
          AccountSummary.validateJSON(data['ownerAccount']);
        }
        // validate the optional field `privacy`
        if (data['privacy']) { // data not null
          VideoPlaylistPrivacyConstant.validateJSON(data['privacy']);
        }
        // ensure the json data is a string
        if (data['shortUUID'] && !(typeof data['shortUUID'] === 'string' || data['shortUUID'] instanceof String)) {
            throw new Error("Expected the field `shortUUID` to be a primitive type in the JSON string but got " + data['shortUUID']);
        }
        // ensure the json data is a string
        if (data['thumbnailPath'] && !(typeof data['thumbnailPath'] === 'string' || data['thumbnailPath'] instanceof String)) {
            throw new Error("Expected the field `thumbnailPath` to be a primitive type in the JSON string but got " + data['thumbnailPath']);
        }
        // validate the optional field `type`
        if (data['type']) { // data not null
          VideoPlaylistTypeConstant.validateJSON(data['type']);
        }
        // ensure the json data is a string
        if (data['uuid'] && !(typeof data['uuid'] === 'string' || data['uuid'] instanceof String)) {
            throw new Error("Expected the field `uuid` to be a primitive type in the JSON string but got " + data['uuid']);
        }
        // validate the optional field `videoChannel`
        if (data['videoChannel']) { // data not null
          VideoChannelSummary.validateJSON(data['videoChannel']);
        }

        return true;
    }


}



/**
 * @member {Date} createdAt
 */
VideoPlaylist.prototype['createdAt'] = undefined;

/**
 * @member {String} description
 */
VideoPlaylist.prototype['description'] = undefined;

/**
 * @member {String} displayName
 */
VideoPlaylist.prototype['displayName'] = undefined;

/**
 * @member {Number} id
 */
VideoPlaylist.prototype['id'] = undefined;

/**
 * @member {Boolean} isLocal
 */
VideoPlaylist.prototype['isLocal'] = undefined;

/**
 * @member {module:model/AccountSummary} ownerAccount
 */
VideoPlaylist.prototype['ownerAccount'] = undefined;

/**
 * @member {module:model/VideoPlaylistPrivacyConstant} privacy
 */
VideoPlaylist.prototype['privacy'] = undefined;

/**
 * translation of a uuid v4 with a bigger alphabet to have a shorter uuid
 * @member {String} shortUUID
 */
VideoPlaylist.prototype['shortUUID'] = undefined;

/**
 * @member {String} thumbnailPath
 */
VideoPlaylist.prototype['thumbnailPath'] = undefined;

/**
 * @member {module:model/VideoPlaylistTypeConstant} type
 */
VideoPlaylist.prototype['type'] = undefined;

/**
 * @member {Date} updatedAt
 */
VideoPlaylist.prototype['updatedAt'] = undefined;

/**
 * @member {String} uuid
 */
VideoPlaylist.prototype['uuid'] = undefined;

/**
 * @member {module:model/VideoChannelSummary} videoChannel
 */
VideoPlaylist.prototype['videoChannel'] = undefined;

/**
 * @member {Number} videoLength
 */
VideoPlaylist.prototype['videoLength'] = undefined;






export default VideoPlaylist;

