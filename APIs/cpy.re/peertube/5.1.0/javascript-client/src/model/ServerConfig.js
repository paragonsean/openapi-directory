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
import ServerConfigAutoBlacklist from './ServerConfigAutoBlacklist';
import ServerConfigAutoBlacklistVideosOfUsers from './ServerConfigAutoBlacklistVideosOfUsers';
import ServerConfigAvatar from './ServerConfigAvatar';
import ServerConfigFollowings from './ServerConfigFollowings';
import ServerConfigImport from './ServerConfigImport';
import ServerConfigInstance from './ServerConfigInstance';
import ServerConfigPlugin from './ServerConfigPlugin';
import ServerConfigSearch from './ServerConfigSearch';
import ServerConfigSignup from './ServerConfigSignup';
import ServerConfigTranscoding from './ServerConfigTranscoding';
import ServerConfigTrending from './ServerConfigTrending';
import ServerConfigUser from './ServerConfigUser';
import ServerConfigVideo from './ServerConfigVideo';
import ServerConfigVideoCaption from './ServerConfigVideoCaption';

/**
 * The ServerConfig model module.
 * @module model/ServerConfig
 * @version 5.1.0
 */
class ServerConfig {
    /**
     * Constructs a new <code>ServerConfig</code>.
     * @alias module:model/ServerConfig
     */
    constructor() { 
        
        ServerConfig.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ServerConfig</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServerConfig} obj Optional instance to populate.
     * @return {module:model/ServerConfig} The populated <code>ServerConfig</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServerConfig();

            if (data.hasOwnProperty('autoBlacklist')) {
                obj['autoBlacklist'] = ServerConfigAutoBlacklist.constructFromObject(data['autoBlacklist']);
            }
            if (data.hasOwnProperty('avatar')) {
                obj['avatar'] = ServerConfigAvatar.constructFromObject(data['avatar']);
            }
            if (data.hasOwnProperty('contactForm')) {
                obj['contactForm'] = ServerConfigAutoBlacklistVideosOfUsers.constructFromObject(data['contactForm']);
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ServerConfigAutoBlacklistVideosOfUsers.constructFromObject(data['email']);
            }
            if (data.hasOwnProperty('followings')) {
                obj['followings'] = ServerConfigFollowings.constructFromObject(data['followings']);
            }
            if (data.hasOwnProperty('homepage')) {
                obj['homepage'] = ServerConfigAutoBlacklistVideosOfUsers.constructFromObject(data['homepage']);
            }
            if (data.hasOwnProperty('import')) {
                obj['import'] = ServerConfigImport.constructFromObject(data['import']);
            }
            if (data.hasOwnProperty('instance')) {
                obj['instance'] = ServerConfigInstance.constructFromObject(data['instance']);
            }
            if (data.hasOwnProperty('plugin')) {
                obj['plugin'] = ServerConfigPlugin.constructFromObject(data['plugin']);
            }
            if (data.hasOwnProperty('search')) {
                obj['search'] = ServerConfigSearch.constructFromObject(data['search']);
            }
            if (data.hasOwnProperty('serverCommit')) {
                obj['serverCommit'] = ApiClient.convertToType(data['serverCommit'], 'String');
            }
            if (data.hasOwnProperty('serverVersion')) {
                obj['serverVersion'] = ApiClient.convertToType(data['serverVersion'], 'String');
            }
            if (data.hasOwnProperty('signup')) {
                obj['signup'] = ServerConfigSignup.constructFromObject(data['signup']);
            }
            if (data.hasOwnProperty('theme')) {
                obj['theme'] = ServerConfigPlugin.constructFromObject(data['theme']);
            }
            if (data.hasOwnProperty('tracker')) {
                obj['tracker'] = ServerConfigAutoBlacklistVideosOfUsers.constructFromObject(data['tracker']);
            }
            if (data.hasOwnProperty('transcoding')) {
                obj['transcoding'] = ServerConfigTranscoding.constructFromObject(data['transcoding']);
            }
            if (data.hasOwnProperty('trending')) {
                obj['trending'] = ServerConfigTrending.constructFromObject(data['trending']);
            }
            if (data.hasOwnProperty('user')) {
                obj['user'] = ServerConfigUser.constructFromObject(data['user']);
            }
            if (data.hasOwnProperty('video')) {
                obj['video'] = ServerConfigVideo.constructFromObject(data['video']);
            }
            if (data.hasOwnProperty('videoCaption')) {
                obj['videoCaption'] = ServerConfigVideoCaption.constructFromObject(data['videoCaption']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServerConfig</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServerConfig</code>.
     */
    static validateJSON(data) {
        // validate the optional field `autoBlacklist`
        if (data['autoBlacklist']) { // data not null
          ServerConfigAutoBlacklist.validateJSON(data['autoBlacklist']);
        }
        // validate the optional field `avatar`
        if (data['avatar']) { // data not null
          ServerConfigAvatar.validateJSON(data['avatar']);
        }
        // validate the optional field `contactForm`
        if (data['contactForm']) { // data not null
          ServerConfigAutoBlacklistVideosOfUsers.validateJSON(data['contactForm']);
        }
        // validate the optional field `email`
        if (data['email']) { // data not null
          ServerConfigAutoBlacklistVideosOfUsers.validateJSON(data['email']);
        }
        // validate the optional field `followings`
        if (data['followings']) { // data not null
          ServerConfigFollowings.validateJSON(data['followings']);
        }
        // validate the optional field `homepage`
        if (data['homepage']) { // data not null
          ServerConfigAutoBlacklistVideosOfUsers.validateJSON(data['homepage']);
        }
        // validate the optional field `import`
        if (data['import']) { // data not null
          ServerConfigImport.validateJSON(data['import']);
        }
        // validate the optional field `instance`
        if (data['instance']) { // data not null
          ServerConfigInstance.validateJSON(data['instance']);
        }
        // validate the optional field `plugin`
        if (data['plugin']) { // data not null
          ServerConfigPlugin.validateJSON(data['plugin']);
        }
        // validate the optional field `search`
        if (data['search']) { // data not null
          ServerConfigSearch.validateJSON(data['search']);
        }
        // ensure the json data is a string
        if (data['serverCommit'] && !(typeof data['serverCommit'] === 'string' || data['serverCommit'] instanceof String)) {
            throw new Error("Expected the field `serverCommit` to be a primitive type in the JSON string but got " + data['serverCommit']);
        }
        // ensure the json data is a string
        if (data['serverVersion'] && !(typeof data['serverVersion'] === 'string' || data['serverVersion'] instanceof String)) {
            throw new Error("Expected the field `serverVersion` to be a primitive type in the JSON string but got " + data['serverVersion']);
        }
        // validate the optional field `signup`
        if (data['signup']) { // data not null
          ServerConfigSignup.validateJSON(data['signup']);
        }
        // validate the optional field `theme`
        if (data['theme']) { // data not null
          ServerConfigPlugin.validateJSON(data['theme']);
        }
        // validate the optional field `tracker`
        if (data['tracker']) { // data not null
          ServerConfigAutoBlacklistVideosOfUsers.validateJSON(data['tracker']);
        }
        // validate the optional field `transcoding`
        if (data['transcoding']) { // data not null
          ServerConfigTranscoding.validateJSON(data['transcoding']);
        }
        // validate the optional field `trending`
        if (data['trending']) { // data not null
          ServerConfigTrending.validateJSON(data['trending']);
        }
        // validate the optional field `user`
        if (data['user']) { // data not null
          ServerConfigUser.validateJSON(data['user']);
        }
        // validate the optional field `video`
        if (data['video']) { // data not null
          ServerConfigVideo.validateJSON(data['video']);
        }
        // validate the optional field `videoCaption`
        if (data['videoCaption']) { // data not null
          ServerConfigVideoCaption.validateJSON(data['videoCaption']);
        }

        return true;
    }


}



/**
 * @member {module:model/ServerConfigAutoBlacklist} autoBlacklist
 */
ServerConfig.prototype['autoBlacklist'] = undefined;

/**
 * @member {module:model/ServerConfigAvatar} avatar
 */
ServerConfig.prototype['avatar'] = undefined;

/**
 * @member {module:model/ServerConfigAutoBlacklistVideosOfUsers} contactForm
 */
ServerConfig.prototype['contactForm'] = undefined;

/**
 * @member {module:model/ServerConfigAutoBlacklistVideosOfUsers} email
 */
ServerConfig.prototype['email'] = undefined;

/**
 * @member {module:model/ServerConfigFollowings} followings
 */
ServerConfig.prototype['followings'] = undefined;

/**
 * @member {module:model/ServerConfigAutoBlacklistVideosOfUsers} homepage
 */
ServerConfig.prototype['homepage'] = undefined;

/**
 * @member {module:model/ServerConfigImport} import
 */
ServerConfig.prototype['import'] = undefined;

/**
 * @member {module:model/ServerConfigInstance} instance
 */
ServerConfig.prototype['instance'] = undefined;

/**
 * @member {module:model/ServerConfigPlugin} plugin
 */
ServerConfig.prototype['plugin'] = undefined;

/**
 * @member {module:model/ServerConfigSearch} search
 */
ServerConfig.prototype['search'] = undefined;

/**
 * @member {String} serverCommit
 */
ServerConfig.prototype['serverCommit'] = undefined;

/**
 * @member {String} serverVersion
 */
ServerConfig.prototype['serverVersion'] = undefined;

/**
 * @member {module:model/ServerConfigSignup} signup
 */
ServerConfig.prototype['signup'] = undefined;

/**
 * @member {module:model/ServerConfigPlugin} theme
 */
ServerConfig.prototype['theme'] = undefined;

/**
 * @member {module:model/ServerConfigAutoBlacklistVideosOfUsers} tracker
 */
ServerConfig.prototype['tracker'] = undefined;

/**
 * @member {module:model/ServerConfigTranscoding} transcoding
 */
ServerConfig.prototype['transcoding'] = undefined;

/**
 * @member {module:model/ServerConfigTrending} trending
 */
ServerConfig.prototype['trending'] = undefined;

/**
 * @member {module:model/ServerConfigUser} user
 */
ServerConfig.prototype['user'] = undefined;

/**
 * @member {module:model/ServerConfigVideo} video
 */
ServerConfig.prototype['video'] = undefined;

/**
 * @member {module:model/ServerConfigVideoCaption} videoCaption
 */
ServerConfig.prototype['videoCaption'] = undefined;






export default ServerConfig;

