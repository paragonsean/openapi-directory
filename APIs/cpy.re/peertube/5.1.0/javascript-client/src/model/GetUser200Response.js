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
import UserWithStats from './UserWithStats';
import VideoChannel from './VideoChannel';

/**
 * The GetUser200Response model module.
 * @module model/GetUser200Response
 * @version 5.1.0
 */
class GetUser200Response {
    /**
     * Constructs a new <code>GetUser200Response</code>.
     * @alias module:model/GetUser200Response
     * @param {(module:model/User|module:model/UserWithStats)} instance The actual instance to initialize GetUser200Response.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "User") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                User.validateJSON(instance); // throw an exception if no match
                // create User from JS object
                this.actualInstance = User.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into User
            errorMessages.push("Failed to construct User: " + err)
        }

        try {
            if (typeof instance === "UserWithStats") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                UserWithStats.validateJSON(instance); // throw an exception if no match
                // create UserWithStats from JS object
                this.actualInstance = UserWithStats.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into UserWithStats
            errorMessages.push("Failed to construct UserWithStats: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `GetUser200Response` with oneOf schemas User, UserWithStats. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `GetUser200Response` with oneOf schemas User, UserWithStats. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>GetUser200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetUser200Response} obj Optional instance to populate.
     * @return {module:model/GetUser200Response} The populated <code>GetUser200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        return new GetUser200Response(data);
    }

    /**
     * Gets the actual instance, which can be <code>User</code>, <code>UserWithStats</code>.
     * @return {(module:model/User|module:model/UserWithStats)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>User</code>, <code>UserWithStats</code>.
     * @param {(module:model/User|module:model/UserWithStats)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = GetUser200Response.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of GetUser200Response from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/GetUser200Response} An instance of GetUser200Response.
     */
    static fromJSON = function(json_string){
        return GetUser200Response.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {module:model/Account} account
 */
GetUser200Response.prototype['account'] = undefined;

/**
 * Automatically start playing the upcoming video after the currently playing video
 * @member {Boolean} autoPlayNextVideo
 */
GetUser200Response.prototype['autoPlayNextVideo'] = undefined;

/**
 * Automatically start playing the video on the playlist after the currently playing video
 * @member {Boolean} autoPlayNextVideoPlaylist
 */
GetUser200Response.prototype['autoPlayNextVideoPlaylist'] = undefined;

/**
 * Automatically start playing the video on the watch page
 * @member {Boolean} autoPlayVideo
 */
GetUser200Response.prototype['autoPlayVideo'] = undefined;

/**
 * @member {Boolean} blocked
 */
GetUser200Response.prototype['blocked'] = undefined;

/**
 * @member {String} blockedReason
 */
GetUser200Response.prototype['blockedReason'] = undefined;

/**
 * @member {String} createdAt
 */
GetUser200Response.prototype['createdAt'] = undefined;

/**
 * The user email
 * @member {String} email
 */
GetUser200Response.prototype['email'] = undefined;

/**
 * Has the user confirmed their email address?
 * @member {Boolean} emailVerified
 */
GetUser200Response.prototype['emailVerified'] = undefined;

/**
 * @member {Number} id
 */
GetUser200Response.prototype['id'] = undefined;

/**
 * @member {Date} lastLoginDate
 */
GetUser200Response.prototype['lastLoginDate'] = undefined;

/**
 * @member {Boolean} noAccountSetupWarningModal
 */
GetUser200Response.prototype['noAccountSetupWarningModal'] = undefined;

/**
 * @member {Boolean} noInstanceConfigWarningModal
 */
GetUser200Response.prototype['noInstanceConfigWarningModal'] = undefined;

/**
 * @member {Boolean} noWelcomeModal
 */
GetUser200Response.prototype['noWelcomeModal'] = undefined;

/**
 * @member {module:model/NSFWPolicy} nsfwPolicy
 */
GetUser200Response.prototype['nsfwPolicy'] = undefined;

/**
 * Enable P2P in the player
 * @member {Boolean} p2pEnabled
 */
GetUser200Response.prototype['p2pEnabled'] = undefined;

/**
 * Auth plugin to use to authenticate the user
 * @member {String} pluginAuth
 */
GetUser200Response.prototype['pluginAuth'] = undefined;

/**
 * @member {module:model/UserRole} role
 */
GetUser200Response.prototype['role'] = undefined;

/**
 * Theme enabled by this user
 * @member {String} theme
 */
GetUser200Response.prototype['theme'] = undefined;

/**
 * immutable name of the user, used to find or mention its actor
 * @member {String} username
 */
GetUser200Response.prototype['username'] = undefined;

/**
 * @member {Array.<module:model/VideoChannel>} videoChannels
 */
GetUser200Response.prototype['videoChannels'] = undefined;

/**
 * The user video quota in bytes
 * @member {Number} videoQuota
 */
GetUser200Response.prototype['videoQuota'] = undefined;

/**
 * The user daily video quota in bytes
 * @member {Number} videoQuotaDaily
 */
GetUser200Response.prototype['videoQuotaDaily'] = undefined;

/**
 * Count of reports/abuses created by the user and accepted/acted upon by the moderation team
 * @member {Number} abusesAcceptedCount
 */
GetUser200Response.prototype['abusesAcceptedCount'] = undefined;

/**
 * Count of reports/abuses of which the user is a target
 * @member {Number} abusesCount
 */
GetUser200Response.prototype['abusesCount'] = undefined;

/**
 * Count of reports/abuses created by the user
 * @member {Number} abusesCreatedCount
 */
GetUser200Response.prototype['abusesCreatedCount'] = undefined;

/**
 * Count of comments published
 * @member {Number} videoCommentsCount
 */
GetUser200Response.prototype['videoCommentsCount'] = undefined;

/**
 * Count of videos published
 * @member {Number} videosCount
 */
GetUser200Response.prototype['videosCount'] = undefined;


GetUser200Response.OneOf = ["User", "UserWithStats"];

export default GetUser200Response;

