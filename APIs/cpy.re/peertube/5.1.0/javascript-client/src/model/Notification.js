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
import ActorInfo from './ActorInfo';
import NotificationActorFollow from './NotificationActorFollow';
import NotificationComment from './NotificationComment';
import NotificationVideo from './NotificationVideo';
import NotificationVideoAbuse from './NotificationVideoAbuse';
import NotificationVideoImport from './NotificationVideoImport';

/**
 * The Notification model module.
 * @module model/Notification
 * @version 5.1.0
 */
class Notification {
    /**
     * Constructs a new <code>Notification</code>.
     * @alias module:model/Notification
     */
    constructor() { 
        
        Notification.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Notification</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Notification} obj Optional instance to populate.
     * @return {module:model/Notification} The populated <code>Notification</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Notification();

            if (data.hasOwnProperty('account')) {
                obj['account'] = ApiClient.convertToType(data['account'], ActorInfo);
            }
            if (data.hasOwnProperty('actorFollow')) {
                obj['actorFollow'] = NotificationActorFollow.constructFromObject(data['actorFollow']);
            }
            if (data.hasOwnProperty('comment')) {
                obj['comment'] = NotificationComment.constructFromObject(data['comment']);
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('read')) {
                obj['read'] = ApiClient.convertToType(data['read'], 'Boolean');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'Number');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('video')) {
                obj['video'] = NotificationVideo.constructFromObject(data['video']);
            }
            if (data.hasOwnProperty('videoAbuse')) {
                obj['videoAbuse'] = NotificationVideoAbuse.constructFromObject(data['videoAbuse']);
            }
            if (data.hasOwnProperty('videoBlacklist')) {
                obj['videoBlacklist'] = NotificationVideoAbuse.constructFromObject(data['videoBlacklist']);
            }
            if (data.hasOwnProperty('videoImport')) {
                obj['videoImport'] = NotificationVideoImport.constructFromObject(data['videoImport']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Notification</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Notification</code>.
     */
    static validateJSON(data) {
        // validate the optional field `account`
        if (data['account']) { // data not null
          ActorInfo.validateJSON(data['account']);
        }
        // validate the optional field `actorFollow`
        if (data['actorFollow']) { // data not null
          NotificationActorFollow.validateJSON(data['actorFollow']);
        }
        // validate the optional field `comment`
        if (data['comment']) { // data not null
          NotificationComment.validateJSON(data['comment']);
        }
        // validate the optional field `video`
        if (data['video']) { // data not null
          NotificationVideo.validateJSON(data['video']);
        }
        // validate the optional field `videoAbuse`
        if (data['videoAbuse']) { // data not null
          NotificationVideoAbuse.validateJSON(data['videoAbuse']);
        }
        // validate the optional field `videoBlacklist`
        if (data['videoBlacklist']) { // data not null
          NotificationVideoAbuse.validateJSON(data['videoBlacklist']);
        }
        // validate the optional field `videoImport`
        if (data['videoImport']) { // data not null
          NotificationVideoImport.validateJSON(data['videoImport']);
        }

        return true;
    }


}



/**
 * @member {module:model/ActorInfo} account
 */
Notification.prototype['account'] = undefined;

/**
 * @member {module:model/NotificationActorFollow} actorFollow
 */
Notification.prototype['actorFollow'] = undefined;

/**
 * @member {module:model/NotificationComment} comment
 */
Notification.prototype['comment'] = undefined;

/**
 * @member {Date} createdAt
 */
Notification.prototype['createdAt'] = undefined;

/**
 * @member {Number} id
 */
Notification.prototype['id'] = undefined;

/**
 * @member {Boolean} read
 */
Notification.prototype['read'] = undefined;

/**
 * Notification type, following the `UserNotificationType` enum: - `1` NEW_VIDEO_FROM_SUBSCRIPTION - `2` NEW_COMMENT_ON_MY_VIDEO - `3` NEW_ABUSE_FOR_MODERATORS - `4` BLACKLIST_ON_MY_VIDEO - `5` UNBLACKLIST_ON_MY_VIDEO - `6` MY_VIDEO_PUBLISHED - `7` MY_VIDEO_IMPORT_SUCCESS - `8` MY_VIDEO_IMPORT_ERROR - `9` NEW_USER_REGISTRATION - `10` NEW_FOLLOW - `11` COMMENT_MENTION - `12` VIDEO_AUTO_BLACKLIST_FOR_MODERATORS - `13` NEW_INSTANCE_FOLLOWER - `14` AUTO_INSTANCE_FOLLOWING - `15` ABUSE_STATE_CHANGE - `16` ABUSE_NEW_MESSAGE - `17` NEW_PLUGIN_VERSION - `18` NEW_PEERTUBE_VERSION 
 * @member {Number} type
 */
Notification.prototype['type'] = undefined;

/**
 * @member {Date} updatedAt
 */
Notification.prototype['updatedAt'] = undefined;

/**
 * @member {module:model/NotificationVideo} video
 */
Notification.prototype['video'] = undefined;

/**
 * @member {module:model/NotificationVideoAbuse} videoAbuse
 */
Notification.prototype['videoAbuse'] = undefined;

/**
 * @member {module:model/NotificationVideoAbuse} videoBlacklist
 */
Notification.prototype['videoBlacklist'] = undefined;

/**
 * @member {module:model/NotificationVideoImport} videoImport
 */
Notification.prototype['videoImport'] = undefined;






export default Notification;

