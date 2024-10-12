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
import VideoConstantNumberCategory from './VideoConstantNumberCategory';
import VideoConstantNumberLicence from './VideoConstantNumberLicence';
import VideoConstantStringLanguage from './VideoConstantStringLanguage';
import VideoPrivacyConstant from './VideoPrivacyConstant';
import VideoScheduledUpdate from './VideoScheduledUpdate';
import VideoStateConstant from './VideoStateConstant';
import VideoUserHistory from './VideoUserHistory';

/**
 * The Video model module.
 * @module model/Video
 * @version 5.1.0
 */
class Video {
    /**
     * Constructs a new <code>Video</code>.
     * @alias module:model/Video
     */
    constructor() { 
        
        Video.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Video</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Video} obj Optional instance to populate.
     * @return {module:model/Video} The populated <code>Video</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Video();

            if (data.hasOwnProperty('account')) {
                obj['account'] = AccountSummary.constructFromObject(data['account']);
            }
            if (data.hasOwnProperty('blacklisted')) {
                obj['blacklisted'] = ApiClient.convertToType(data['blacklisted'], 'Boolean');
            }
            if (data.hasOwnProperty('blacklistedReason')) {
                obj['blacklistedReason'] = ApiClient.convertToType(data['blacklistedReason'], 'String');
            }
            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], VideoConstantNumberCategory);
            }
            if (data.hasOwnProperty('channel')) {
                obj['channel'] = VideoChannelSummary.constructFromObject(data['channel']);
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('dislikes')) {
                obj['dislikes'] = ApiClient.convertToType(data['dislikes'], 'Number');
            }
            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'Number');
            }
            if (data.hasOwnProperty('embedPath')) {
                obj['embedPath'] = ApiClient.convertToType(data['embedPath'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('isLive')) {
                obj['isLive'] = ApiClient.convertToType(data['isLive'], 'Boolean');
            }
            if (data.hasOwnProperty('isLocal')) {
                obj['isLocal'] = ApiClient.convertToType(data['isLocal'], 'Boolean');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], VideoConstantStringLanguage);
            }
            if (data.hasOwnProperty('licence')) {
                obj['licence'] = ApiClient.convertToType(data['licence'], VideoConstantNumberLicence);
            }
            if (data.hasOwnProperty('likes')) {
                obj['likes'] = ApiClient.convertToType(data['likes'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('nsfw')) {
                obj['nsfw'] = ApiClient.convertToType(data['nsfw'], 'Boolean');
            }
            if (data.hasOwnProperty('originallyPublishedAt')) {
                obj['originallyPublishedAt'] = ApiClient.convertToType(data['originallyPublishedAt'], 'Date');
            }
            if (data.hasOwnProperty('previewPath')) {
                obj['previewPath'] = ApiClient.convertToType(data['previewPath'], 'String');
            }
            if (data.hasOwnProperty('privacy')) {
                obj['privacy'] = ApiClient.convertToType(data['privacy'], VideoPrivacyConstant);
            }
            if (data.hasOwnProperty('publishedAt')) {
                obj['publishedAt'] = ApiClient.convertToType(data['publishedAt'], 'Date');
            }
            if (data.hasOwnProperty('scheduledUpdate')) {
                obj['scheduledUpdate'] = ApiClient.convertToType(data['scheduledUpdate'], VideoScheduledUpdate);
            }
            if (data.hasOwnProperty('shortUUID')) {
                obj['shortUUID'] = ApiClient.convertToType(data['shortUUID'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], VideoStateConstant);
            }
            if (data.hasOwnProperty('thumbnailPath')) {
                obj['thumbnailPath'] = ApiClient.convertToType(data['thumbnailPath'], 'String');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('userHistory')) {
                obj['userHistory'] = VideoUserHistory.constructFromObject(data['userHistory']);
            }
            if (data.hasOwnProperty('uuid')) {
                obj['uuid'] = ApiClient.convertToType(data['uuid'], 'String');
            }
            if (data.hasOwnProperty('views')) {
                obj['views'] = ApiClient.convertToType(data['views'], 'Number');
            }
            if (data.hasOwnProperty('waitTranscoding')) {
                obj['waitTranscoding'] = ApiClient.convertToType(data['waitTranscoding'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Video</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Video</code>.
     */
    static validateJSON(data) {
        // validate the optional field `account`
        if (data['account']) { // data not null
          AccountSummary.validateJSON(data['account']);
        }
        // ensure the json data is a string
        if (data['blacklistedReason'] && !(typeof data['blacklistedReason'] === 'string' || data['blacklistedReason'] instanceof String)) {
            throw new Error("Expected the field `blacklistedReason` to be a primitive type in the JSON string but got " + data['blacklistedReason']);
        }
        // validate the optional field `category`
        if (data['category']) { // data not null
          VideoConstantNumberCategory.validateJSON(data['category']);
        }
        // validate the optional field `channel`
        if (data['channel']) { // data not null
          VideoChannelSummary.validateJSON(data['channel']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['embedPath'] && !(typeof data['embedPath'] === 'string' || data['embedPath'] instanceof String)) {
            throw new Error("Expected the field `embedPath` to be a primitive type in the JSON string but got " + data['embedPath']);
        }
        // validate the optional field `language`
        if (data['language']) { // data not null
          VideoConstantStringLanguage.validateJSON(data['language']);
        }
        // validate the optional field `licence`
        if (data['licence']) { // data not null
          VideoConstantNumberLicence.validateJSON(data['licence']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['previewPath'] && !(typeof data['previewPath'] === 'string' || data['previewPath'] instanceof String)) {
            throw new Error("Expected the field `previewPath` to be a primitive type in the JSON string but got " + data['previewPath']);
        }
        // validate the optional field `privacy`
        if (data['privacy']) { // data not null
          VideoPrivacyConstant.validateJSON(data['privacy']);
        }
        // validate the optional field `scheduledUpdate`
        if (data['scheduledUpdate']) { // data not null
          VideoScheduledUpdate.validateJSON(data['scheduledUpdate']);
        }
        // ensure the json data is a string
        if (data['shortUUID'] && !(typeof data['shortUUID'] === 'string' || data['shortUUID'] instanceof String)) {
            throw new Error("Expected the field `shortUUID` to be a primitive type in the JSON string but got " + data['shortUUID']);
        }
        // validate the optional field `state`
        if (data['state']) { // data not null
          VideoStateConstant.validateJSON(data['state']);
        }
        // ensure the json data is a string
        if (data['thumbnailPath'] && !(typeof data['thumbnailPath'] === 'string' || data['thumbnailPath'] instanceof String)) {
            throw new Error("Expected the field `thumbnailPath` to be a primitive type in the JSON string but got " + data['thumbnailPath']);
        }
        // validate the optional field `userHistory`
        if (data['userHistory']) { // data not null
          VideoUserHistory.validateJSON(data['userHistory']);
        }
        // ensure the json data is a string
        if (data['uuid'] && !(typeof data['uuid'] === 'string' || data['uuid'] instanceof String)) {
            throw new Error("Expected the field `uuid` to be a primitive type in the JSON string but got " + data['uuid']);
        }

        return true;
    }


}



/**
 * @member {module:model/AccountSummary} account
 */
Video.prototype['account'] = undefined;

/**
 * @member {Boolean} blacklisted
 */
Video.prototype['blacklisted'] = undefined;

/**
 * @member {String} blacklistedReason
 */
Video.prototype['blacklistedReason'] = undefined;

/**
 * category in which the video is classified
 * @member {module:model/VideoConstantNumberCategory} category
 */
Video.prototype['category'] = undefined;

/**
 * @member {module:model/VideoChannelSummary} channel
 */
Video.prototype['channel'] = undefined;

/**
 * time at which the video object was first drafted
 * @member {Date} createdAt
 */
Video.prototype['createdAt'] = undefined;

/**
 * truncated description of the video, written in Markdown. Resolve `descriptionPath` to get the full description of maximum `10000` characters. 
 * @member {String} description
 */
Video.prototype['description'] = undefined;

/**
 * @member {Number} dislikes
 */
Video.prototype['dislikes'] = undefined;

/**
 * duration of the video in seconds
 * @member {Number} duration
 */
Video.prototype['duration'] = undefined;

/**
 * @member {String} embedPath
 */
Video.prototype['embedPath'] = undefined;

/**
 * object id for the video
 * @member {Number} id
 */
Video.prototype['id'] = undefined;

/**
 * @member {Boolean} isLive
 */
Video.prototype['isLive'] = undefined;

/**
 * @member {Boolean} isLocal
 */
Video.prototype['isLocal'] = undefined;

/**
 * main language used in the video
 * @member {module:model/VideoConstantStringLanguage} language
 */
Video.prototype['language'] = undefined;

/**
 * licence under which the video is distributed
 * @member {module:model/VideoConstantNumberLicence} licence
 */
Video.prototype['licence'] = undefined;

/**
 * @member {Number} likes
 */
Video.prototype['likes'] = undefined;

/**
 * title of the video
 * @member {String} name
 */
Video.prototype['name'] = undefined;

/**
 * @member {Boolean} nsfw
 */
Video.prototype['nsfw'] = undefined;

/**
 * used to represent a date of first publication, prior to the practical publication date of `publishedAt`
 * @member {Date} originallyPublishedAt
 */
Video.prototype['originallyPublishedAt'] = undefined;

/**
 * @member {String} previewPath
 */
Video.prototype['previewPath'] = undefined;

/**
 * privacy policy used to distribute the video
 * @member {module:model/VideoPrivacyConstant} privacy
 */
Video.prototype['privacy'] = undefined;

/**
 * time at which the video was marked as ready for playback (with restrictions depending on `privacy`). Usually set after a `state` evolution.
 * @member {Date} publishedAt
 */
Video.prototype['publishedAt'] = undefined;

/**
 * @member {module:model/VideoScheduledUpdate} scheduledUpdate
 */
Video.prototype['scheduledUpdate'] = undefined;

/**
 * translation of a uuid v4 with a bigger alphabet to have a shorter uuid
 * @member {String} shortUUID
 */
Video.prototype['shortUUID'] = undefined;

/**
 * represents the internal state of the video processing within the PeerTube instance
 * @member {module:model/VideoStateConstant} state
 */
Video.prototype['state'] = undefined;

/**
 * @member {String} thumbnailPath
 */
Video.prototype['thumbnailPath'] = undefined;

/**
 * last time the video's metadata was modified
 * @member {Date} updatedAt
 */
Video.prototype['updatedAt'] = undefined;

/**
 * @member {module:model/VideoUserHistory} userHistory
 */
Video.prototype['userHistory'] = undefined;

/**
 * universal identifier for the video, that can be used across instances
 * @member {String} uuid
 */
Video.prototype['uuid'] = undefined;

/**
 * @member {Number} views
 */
Video.prototype['views'] = undefined;

/**
 * @member {Boolean} waitTranscoding
 */
Video.prototype['waitTranscoding'] = undefined;






export default Video;

