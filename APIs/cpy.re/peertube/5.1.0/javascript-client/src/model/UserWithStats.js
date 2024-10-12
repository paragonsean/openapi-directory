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
import Account from './Account';
import NSFWPolicy from './NSFWPolicy';
import User from './User';
import UserRole from './UserRole';
import VideoChannel from './VideoChannel';

/**
 * The UserWithStats model module.
 * @module model/UserWithStats
 * @version 5.1.0
 */
class UserWithStats {
    /**
     * Constructs a new <code>UserWithStats</code>.
     * @alias module:model/UserWithStats
     * @implements module:model/User
     */
    constructor() { 
        User.initialize(this);
        UserWithStats.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UserWithStats</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserWithStats} obj Optional instance to populate.
     * @return {module:model/UserWithStats} The populated <code>UserWithStats</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserWithStats();
            User.constructFromObject(data, obj);

            if (data.hasOwnProperty('account')) {
                obj['account'] = Account.constructFromObject(data['account']);
            }
            if (data.hasOwnProperty('autoPlayNextVideo')) {
                obj['autoPlayNextVideo'] = ApiClient.convertToType(data['autoPlayNextVideo'], 'Boolean');
            }
            if (data.hasOwnProperty('autoPlayNextVideoPlaylist')) {
                obj['autoPlayNextVideoPlaylist'] = ApiClient.convertToType(data['autoPlayNextVideoPlaylist'], 'Boolean');
            }
            if (data.hasOwnProperty('autoPlayVideo')) {
                obj['autoPlayVideo'] = ApiClient.convertToType(data['autoPlayVideo'], 'Boolean');
            }
            if (data.hasOwnProperty('blocked')) {
                obj['blocked'] = ApiClient.convertToType(data['blocked'], 'Boolean');
            }
            if (data.hasOwnProperty('blockedReason')) {
                obj['blockedReason'] = ApiClient.convertToType(data['blockedReason'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('emailVerified')) {
                obj['emailVerified'] = ApiClient.convertToType(data['emailVerified'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('lastLoginDate')) {
                obj['lastLoginDate'] = ApiClient.convertToType(data['lastLoginDate'], 'Date');
            }
            if (data.hasOwnProperty('noAccountSetupWarningModal')) {
                obj['noAccountSetupWarningModal'] = ApiClient.convertToType(data['noAccountSetupWarningModal'], 'Boolean');
            }
            if (data.hasOwnProperty('noInstanceConfigWarningModal')) {
                obj['noInstanceConfigWarningModal'] = ApiClient.convertToType(data['noInstanceConfigWarningModal'], 'Boolean');
            }
            if (data.hasOwnProperty('noWelcomeModal')) {
                obj['noWelcomeModal'] = ApiClient.convertToType(data['noWelcomeModal'], 'Boolean');
            }
            if (data.hasOwnProperty('nsfwPolicy')) {
                obj['nsfwPolicy'] = NSFWPolicy.constructFromObject(data['nsfwPolicy']);
            }
            if (data.hasOwnProperty('p2pEnabled')) {
                obj['p2pEnabled'] = ApiClient.convertToType(data['p2pEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('pluginAuth')) {
                obj['pluginAuth'] = ApiClient.convertToType(data['pluginAuth'], 'String');
            }
            if (data.hasOwnProperty('role')) {
                obj['role'] = UserRole.constructFromObject(data['role']);
            }
            if (data.hasOwnProperty('theme')) {
                obj['theme'] = ApiClient.convertToType(data['theme'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
            if (data.hasOwnProperty('videoChannels')) {
                obj['videoChannels'] = ApiClient.convertToType(data['videoChannels'], [VideoChannel]);
            }
            if (data.hasOwnProperty('videoQuota')) {
                obj['videoQuota'] = ApiClient.convertToType(data['videoQuota'], 'Number');
            }
            if (data.hasOwnProperty('videoQuotaDaily')) {
                obj['videoQuotaDaily'] = ApiClient.convertToType(data['videoQuotaDaily'], 'Number');
            }
            if (data.hasOwnProperty('abusesAcceptedCount')) {
                obj['abusesAcceptedCount'] = ApiClient.convertToType(data['abusesAcceptedCount'], 'Number');
            }
            if (data.hasOwnProperty('abusesCount')) {
                obj['abusesCount'] = ApiClient.convertToType(data['abusesCount'], 'Number');
            }
            if (data.hasOwnProperty('abusesCreatedCount')) {
                obj['abusesCreatedCount'] = ApiClient.convertToType(data['abusesCreatedCount'], 'Number');
            }
            if (data.hasOwnProperty('videoCommentsCount')) {
                obj['videoCommentsCount'] = ApiClient.convertToType(data['videoCommentsCount'], 'Number');
            }
            if (data.hasOwnProperty('videosCount')) {
                obj['videosCount'] = ApiClient.convertToType(data['videosCount'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UserWithStats</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserWithStats</code>.
     */
    static validateJSON(data) {
        // validate the optional field `account`
        if (data['account']) { // data not null
          Account.validateJSON(data['account']);
        }
        // ensure the json data is a string
        if (data['blockedReason'] && !(typeof data['blockedReason'] === 'string' || data['blockedReason'] instanceof String)) {
            throw new Error("Expected the field `blockedReason` to be a primitive type in the JSON string but got " + data['blockedReason']);
        }
        // ensure the json data is a string
        if (data['createdAt'] && !(typeof data['createdAt'] === 'string' || data['createdAt'] instanceof String)) {
            throw new Error("Expected the field `createdAt` to be a primitive type in the JSON string but got " + data['createdAt']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['pluginAuth'] && !(typeof data['pluginAuth'] === 'string' || data['pluginAuth'] instanceof String)) {
            throw new Error("Expected the field `pluginAuth` to be a primitive type in the JSON string but got " + data['pluginAuth']);
        }
        // validate the optional field `role`
        if (data['role']) { // data not null
          UserRole.validateJSON(data['role']);
        }
        // ensure the json data is a string
        if (data['theme'] && !(typeof data['theme'] === 'string' || data['theme'] instanceof String)) {
            throw new Error("Expected the field `theme` to be a primitive type in the JSON string but got " + data['theme']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }
        if (data['videoChannels']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['videoChannels'])) {
                throw new Error("Expected the field `videoChannels` to be an array in the JSON data but got " + data['videoChannels']);
            }
            // validate the optional field `videoChannels` (array)
            for (const item of data['videoChannels']) {
                VideoChannel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/Account} account
 */
UserWithStats.prototype['account'] = undefined;

/**
 * Automatically start playing the upcoming video after the currently playing video
 * @member {Boolean} autoPlayNextVideo
 */
UserWithStats.prototype['autoPlayNextVideo'] = undefined;

/**
 * Automatically start playing the video on the playlist after the currently playing video
 * @member {Boolean} autoPlayNextVideoPlaylist
 */
UserWithStats.prototype['autoPlayNextVideoPlaylist'] = undefined;

/**
 * Automatically start playing the video on the watch page
 * @member {Boolean} autoPlayVideo
 */
UserWithStats.prototype['autoPlayVideo'] = undefined;

/**
 * @member {Boolean} blocked
 */
UserWithStats.prototype['blocked'] = undefined;

/**
 * @member {String} blockedReason
 */
UserWithStats.prototype['blockedReason'] = undefined;

/**
 * @member {String} createdAt
 */
UserWithStats.prototype['createdAt'] = undefined;

/**
 * The user email
 * @member {String} email
 */
UserWithStats.prototype['email'] = undefined;

/**
 * Has the user confirmed their email address?
 * @member {Boolean} emailVerified
 */
UserWithStats.prototype['emailVerified'] = undefined;

/**
 * @member {Number} id
 */
UserWithStats.prototype['id'] = undefined;

/**
 * @member {Date} lastLoginDate
 */
UserWithStats.prototype['lastLoginDate'] = undefined;

/**
 * @member {Boolean} noAccountSetupWarningModal
 */
UserWithStats.prototype['noAccountSetupWarningModal'] = undefined;

/**
 * @member {Boolean} noInstanceConfigWarningModal
 */
UserWithStats.prototype['noInstanceConfigWarningModal'] = undefined;

/**
 * @member {Boolean} noWelcomeModal
 */
UserWithStats.prototype['noWelcomeModal'] = undefined;

/**
 * @member {module:model/NSFWPolicy} nsfwPolicy
 */
UserWithStats.prototype['nsfwPolicy'] = undefined;

/**
 * Enable P2P in the player
 * @member {Boolean} p2pEnabled
 */
UserWithStats.prototype['p2pEnabled'] = undefined;

/**
 * Auth plugin to use to authenticate the user
 * @member {String} pluginAuth
 */
UserWithStats.prototype['pluginAuth'] = undefined;

/**
 * @member {module:model/UserRole} role
 */
UserWithStats.prototype['role'] = undefined;

/**
 * Theme enabled by this user
 * @member {String} theme
 */
UserWithStats.prototype['theme'] = undefined;

/**
 * immutable name of the user, used to find or mention its actor
 * @member {String} username
 */
UserWithStats.prototype['username'] = undefined;

/**
 * @member {Array.<module:model/VideoChannel>} videoChannels
 */
UserWithStats.prototype['videoChannels'] = undefined;

/**
 * The user video quota in bytes
 * @member {Number} videoQuota
 */
UserWithStats.prototype['videoQuota'] = undefined;

/**
 * The user daily video quota in bytes
 * @member {Number} videoQuotaDaily
 */
UserWithStats.prototype['videoQuotaDaily'] = undefined;

/**
 * Count of reports/abuses created by the user and accepted/acted upon by the moderation team
 * @member {Number} abusesAcceptedCount
 */
UserWithStats.prototype['abusesAcceptedCount'] = undefined;

/**
 * Count of reports/abuses of which the user is a target
 * @member {Number} abusesCount
 */
UserWithStats.prototype['abusesCount'] = undefined;

/**
 * Count of reports/abuses created by the user
 * @member {Number} abusesCreatedCount
 */
UserWithStats.prototype['abusesCreatedCount'] = undefined;

/**
 * Count of comments published
 * @member {Number} videoCommentsCount
 */
UserWithStats.prototype['videoCommentsCount'] = undefined;

/**
 * Count of videos published
 * @member {Number} videosCount
 */
UserWithStats.prototype['videosCount'] = undefined;


// Implement User interface:
/**
 * @member {module:model/Account} account
 */
User.prototype['account'] = undefined;
/**
 * Automatically start playing the upcoming video after the currently playing video
 * @member {Boolean} autoPlayNextVideo
 */
User.prototype['autoPlayNextVideo'] = undefined;
/**
 * Automatically start playing the video on the playlist after the currently playing video
 * @member {Boolean} autoPlayNextVideoPlaylist
 */
User.prototype['autoPlayNextVideoPlaylist'] = undefined;
/**
 * Automatically start playing the video on the watch page
 * @member {Boolean} autoPlayVideo
 */
User.prototype['autoPlayVideo'] = undefined;
/**
 * @member {Boolean} blocked
 */
User.prototype['blocked'] = undefined;
/**
 * @member {String} blockedReason
 */
User.prototype['blockedReason'] = undefined;
/**
 * @member {String} createdAt
 */
User.prototype['createdAt'] = undefined;
/**
 * The user email
 * @member {String} email
 */
User.prototype['email'] = undefined;
/**
 * Has the user confirmed their email address?
 * @member {Boolean} emailVerified
 */
User.prototype['emailVerified'] = undefined;
/**
 * @member {Number} id
 */
User.prototype['id'] = undefined;
/**
 * @member {Date} lastLoginDate
 */
User.prototype['lastLoginDate'] = undefined;
/**
 * @member {Boolean} noAccountSetupWarningModal
 */
User.prototype['noAccountSetupWarningModal'] = undefined;
/**
 * @member {Boolean} noInstanceConfigWarningModal
 */
User.prototype['noInstanceConfigWarningModal'] = undefined;
/**
 * @member {Boolean} noWelcomeModal
 */
User.prototype['noWelcomeModal'] = undefined;
/**
 * @member {module:model/NSFWPolicy} nsfwPolicy
 */
User.prototype['nsfwPolicy'] = undefined;
/**
 * Enable P2P in the player
 * @member {Boolean} p2pEnabled
 */
User.prototype['p2pEnabled'] = undefined;
/**
 * Auth plugin to use to authenticate the user
 * @member {String} pluginAuth
 */
User.prototype['pluginAuth'] = undefined;
/**
 * @member {module:model/UserRole} role
 */
User.prototype['role'] = undefined;
/**
 * Theme enabled by this user
 * @member {String} theme
 */
User.prototype['theme'] = undefined;
/**
 * immutable name of the user, used to find or mention its actor
 * @member {String} username
 */
User.prototype['username'] = undefined;
/**
 * @member {Array.<module:model/VideoChannel>} videoChannels
 */
User.prototype['videoChannels'] = undefined;
/**
 * The user video quota in bytes
 * @member {Number} videoQuota
 */
User.prototype['videoQuota'] = undefined;
/**
 * The user daily video quota in bytes
 * @member {Number} videoQuotaDaily
 */
User.prototype['videoQuotaDaily'] = undefined;




export default UserWithStats;

