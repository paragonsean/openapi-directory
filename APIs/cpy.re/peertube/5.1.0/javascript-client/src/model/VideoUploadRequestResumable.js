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
import VideoPrivacySet from './VideoPrivacySet';
import VideoScheduledUpdate from './VideoScheduledUpdate';
import VideoUploadRequestCommon from './VideoUploadRequestCommon';

/**
 * The VideoUploadRequestResumable model module.
 * @module model/VideoUploadRequestResumable
 * @version 5.1.0
 */
class VideoUploadRequestResumable {
    /**
     * Constructs a new <code>VideoUploadRequestResumable</code>.
     * @alias module:model/VideoUploadRequestResumable
     * @implements module:model/VideoUploadRequestCommon
     * @param channelId {Number} Channel id that will contain this video
     * @param name {String} Video name
     * @param filename {String} Video filename including extension
     */
    constructor(channelId, name, filename) { 
        VideoUploadRequestCommon.initialize(this, channelId, name);
        VideoUploadRequestResumable.initialize(this, channelId, name, filename);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, channelId, name, filename) { 
        obj['channelId'] = channelId;
        obj['name'] = name;
        obj['filename'] = filename;
    }

    /**
     * Constructs a <code>VideoUploadRequestResumable</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VideoUploadRequestResumable} obj Optional instance to populate.
     * @return {module:model/VideoUploadRequestResumable} The populated <code>VideoUploadRequestResumable</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VideoUploadRequestResumable();
            VideoUploadRequestCommon.constructFromObject(data, obj);

            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], 'Number');
            }
            if (data.hasOwnProperty('channelId')) {
                obj['channelId'] = ApiClient.convertToType(data['channelId'], 'Number');
            }
            if (data.hasOwnProperty('commentsEnabled')) {
                obj['commentsEnabled'] = ApiClient.convertToType(data['commentsEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('downloadEnabled')) {
                obj['downloadEnabled'] = ApiClient.convertToType(data['downloadEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
            if (data.hasOwnProperty('licence')) {
                obj['licence'] = ApiClient.convertToType(data['licence'], 'Number');
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
            if (data.hasOwnProperty('previewfile')) {
                obj['previewfile'] = ApiClient.convertToType(data['previewfile'], File);
            }
            if (data.hasOwnProperty('privacy')) {
                obj['privacy'] = VideoPrivacySet.constructFromObject(data['privacy']);
            }
            if (data.hasOwnProperty('scheduleUpdate')) {
                obj['scheduleUpdate'] = VideoScheduledUpdate.constructFromObject(data['scheduleUpdate']);
            }
            if (data.hasOwnProperty('support')) {
                obj['support'] = ApiClient.convertToType(data['support'], 'String');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], ['String']);
            }
            if (data.hasOwnProperty('thumbnailfile')) {
                obj['thumbnailfile'] = ApiClient.convertToType(data['thumbnailfile'], File);
            }
            if (data.hasOwnProperty('waitTranscoding')) {
                obj['waitTranscoding'] = ApiClient.convertToType(data['waitTranscoding'], 'Boolean');
            }
            if (data.hasOwnProperty('filename')) {
                obj['filename'] = ApiClient.convertToType(data['filename'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VideoUploadRequestResumable</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VideoUploadRequestResumable</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of VideoUploadRequestResumable.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `scheduleUpdate`
        if (data['scheduleUpdate']) { // data not null
          VideoScheduledUpdate.validateJSON(data['scheduleUpdate']);
        }
        // ensure the json data is a string
        if (data['support'] && !(typeof data['support'] === 'string' || data['support'] instanceof String)) {
            throw new Error("Expected the field `support` to be a primitive type in the JSON string but got " + data['support']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tags'])) {
            throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
        }
        // ensure the json data is a string
        if (data['filename'] && !(typeof data['filename'] === 'string' || data['filename'] instanceof String)) {
            throw new Error("Expected the field `filename` to be a primitive type in the JSON string but got " + data['filename']);
        }

        return true;
    }


}

VideoUploadRequestResumable.RequiredProperties = ["channelId", "name", "filename"];

/**
 * category id of the video (see [/videos/categories](#operation/getCategories))
 * @member {Number} category
 */
VideoUploadRequestResumable.prototype['category'] = undefined;

/**
 * Channel id that will contain this video
 * @member {Number} channelId
 */
VideoUploadRequestResumable.prototype['channelId'] = undefined;

/**
 * Enable or disable comments for this video
 * @member {Boolean} commentsEnabled
 */
VideoUploadRequestResumable.prototype['commentsEnabled'] = undefined;

/**
 * Video description
 * @member {String} description
 */
VideoUploadRequestResumable.prototype['description'] = undefined;

/**
 * Enable or disable downloading for this video
 * @member {Boolean} downloadEnabled
 */
VideoUploadRequestResumable.prototype['downloadEnabled'] = undefined;

/**
 * language id of the video (see [/videos/languages](#operation/getLanguages))
 * @member {String} language
 */
VideoUploadRequestResumable.prototype['language'] = undefined;

/**
 * licence id of the video (see [/videos/licences](#operation/getLicences))
 * @member {Number} licence
 */
VideoUploadRequestResumable.prototype['licence'] = undefined;

/**
 * Video name
 * @member {String} name
 */
VideoUploadRequestResumable.prototype['name'] = undefined;

/**
 * Whether or not this video contains sensitive content
 * @member {Boolean} nsfw
 */
VideoUploadRequestResumable.prototype['nsfw'] = undefined;

/**
 * Date when the content was originally published
 * @member {Date} originallyPublishedAt
 */
VideoUploadRequestResumable.prototype['originallyPublishedAt'] = undefined;

/**
 * Video preview file
 * @member {File} previewfile
 */
VideoUploadRequestResumable.prototype['previewfile'] = undefined;

/**
 * @member {module:model/VideoPrivacySet} privacy
 */
VideoUploadRequestResumable.prototype['privacy'] = undefined;

/**
 * @member {module:model/VideoScheduledUpdate} scheduleUpdate
 */
VideoUploadRequestResumable.prototype['scheduleUpdate'] = undefined;

/**
 * A text tell the audience how to support the video creator
 * @member {String} support
 */
VideoUploadRequestResumable.prototype['support'] = undefined;

/**
 * Video tags (maximum 5 tags each between 2 and 30 characters)
 * @member {Array.<String>} tags
 */
VideoUploadRequestResumable.prototype['tags'] = undefined;

/**
 * Video thumbnail file
 * @member {File} thumbnailfile
 */
VideoUploadRequestResumable.prototype['thumbnailfile'] = undefined;

/**
 * Whether or not we wait transcoding before publish the video
 * @member {Boolean} waitTranscoding
 */
VideoUploadRequestResumable.prototype['waitTranscoding'] = undefined;

/**
 * Video filename including extension
 * @member {String} filename
 */
VideoUploadRequestResumable.prototype['filename'] = undefined;


// Implement VideoUploadRequestCommon interface:
/**
 * category id of the video (see [/videos/categories](#operation/getCategories))
 * @member {Number} category
 */
VideoUploadRequestCommon.prototype['category'] = undefined;
/**
 * Channel id that will contain this video
 * @member {Number} channelId
 */
VideoUploadRequestCommon.prototype['channelId'] = undefined;
/**
 * Enable or disable comments for this video
 * @member {Boolean} commentsEnabled
 */
VideoUploadRequestCommon.prototype['commentsEnabled'] = undefined;
/**
 * Video description
 * @member {String} description
 */
VideoUploadRequestCommon.prototype['description'] = undefined;
/**
 * Enable or disable downloading for this video
 * @member {Boolean} downloadEnabled
 */
VideoUploadRequestCommon.prototype['downloadEnabled'] = undefined;
/**
 * language id of the video (see [/videos/languages](#operation/getLanguages))
 * @member {String} language
 */
VideoUploadRequestCommon.prototype['language'] = undefined;
/**
 * licence id of the video (see [/videos/licences](#operation/getLicences))
 * @member {Number} licence
 */
VideoUploadRequestCommon.prototype['licence'] = undefined;
/**
 * Video name
 * @member {String} name
 */
VideoUploadRequestCommon.prototype['name'] = undefined;
/**
 * Whether or not this video contains sensitive content
 * @member {Boolean} nsfw
 */
VideoUploadRequestCommon.prototype['nsfw'] = undefined;
/**
 * Date when the content was originally published
 * @member {Date} originallyPublishedAt
 */
VideoUploadRequestCommon.prototype['originallyPublishedAt'] = undefined;
/**
 * Video preview file
 * @member {File} previewfile
 */
VideoUploadRequestCommon.prototype['previewfile'] = undefined;
/**
 * @member {module:model/VideoPrivacySet} privacy
 */
VideoUploadRequestCommon.prototype['privacy'] = undefined;
/**
 * @member {module:model/VideoScheduledUpdate} scheduleUpdate
 */
VideoUploadRequestCommon.prototype['scheduleUpdate'] = undefined;
/**
 * A text tell the audience how to support the video creator
 * @member {String} support
 */
VideoUploadRequestCommon.prototype['support'] = undefined;
/**
 * Video tags (maximum 5 tags each between 2 and 30 characters)
 * @member {Array.<String>} tags
 */
VideoUploadRequestCommon.prototype['tags'] = undefined;
/**
 * Video thumbnail file
 * @member {File} thumbnailfile
 */
VideoUploadRequestCommon.prototype['thumbnailfile'] = undefined;
/**
 * Whether or not we wait transcoding before publish the video
 * @member {Boolean} waitTranscoding
 */
VideoUploadRequestCommon.prototype['waitTranscoding'] = undefined;




export default VideoUploadRequestResumable;

