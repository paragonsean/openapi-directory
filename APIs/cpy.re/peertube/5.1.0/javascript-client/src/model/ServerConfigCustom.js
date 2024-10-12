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
import ServerConfigCustomAdmin from './ServerConfigCustomAdmin';
import ServerConfigCustomCache from './ServerConfigCustomCache';
import ServerConfigCustomFollowers from './ServerConfigCustomFollowers';
import ServerConfigCustomImport from './ServerConfigCustomImport';
import ServerConfigCustomInstance from './ServerConfigCustomInstance';
import ServerConfigCustomServices from './ServerConfigCustomServices';
import ServerConfigCustomSignup from './ServerConfigCustomSignup';
import ServerConfigCustomTheme from './ServerConfigCustomTheme';
import ServerConfigCustomTranscoding from './ServerConfigCustomTranscoding';
import ServerConfigCustomUser from './ServerConfigCustomUser';

/**
 * The ServerConfigCustom model module.
 * @module model/ServerConfigCustom
 * @version 5.1.0
 */
class ServerConfigCustom {
    /**
     * Constructs a new <code>ServerConfigCustom</code>.
     * @alias module:model/ServerConfigCustom
     */
    constructor() { 
        
        ServerConfigCustom.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ServerConfigCustom</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServerConfigCustom} obj Optional instance to populate.
     * @return {module:model/ServerConfigCustom} The populated <code>ServerConfigCustom</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServerConfigCustom();

            if (data.hasOwnProperty('admin')) {
                obj['admin'] = ServerConfigCustomAdmin.constructFromObject(data['admin']);
            }
            if (data.hasOwnProperty('autoBlacklist')) {
                obj['autoBlacklist'] = ServerConfigAutoBlacklist.constructFromObject(data['autoBlacklist']);
            }
            if (data.hasOwnProperty('cache')) {
                obj['cache'] = ServerConfigCustomCache.constructFromObject(data['cache']);
            }
            if (data.hasOwnProperty('contactForm')) {
                obj['contactForm'] = ServerConfigAutoBlacklistVideosOfUsers.constructFromObject(data['contactForm']);
            }
            if (data.hasOwnProperty('followers')) {
                obj['followers'] = ServerConfigCustomFollowers.constructFromObject(data['followers']);
            }
            if (data.hasOwnProperty('import')) {
                obj['import'] = ServerConfigCustomImport.constructFromObject(data['import']);
            }
            if (data.hasOwnProperty('instance')) {
                obj['instance'] = ServerConfigCustomInstance.constructFromObject(data['instance']);
            }
            if (data.hasOwnProperty('services')) {
                obj['services'] = ServerConfigCustomServices.constructFromObject(data['services']);
            }
            if (data.hasOwnProperty('signup')) {
                obj['signup'] = ServerConfigCustomSignup.constructFromObject(data['signup']);
            }
            if (data.hasOwnProperty('theme')) {
                obj['theme'] = ServerConfigCustomTheme.constructFromObject(data['theme']);
            }
            if (data.hasOwnProperty('transcoding')) {
                obj['transcoding'] = ServerConfigCustomTranscoding.constructFromObject(data['transcoding']);
            }
            if (data.hasOwnProperty('user')) {
                obj['user'] = ServerConfigCustomUser.constructFromObject(data['user']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServerConfigCustom</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServerConfigCustom</code>.
     */
    static validateJSON(data) {
        // validate the optional field `admin`
        if (data['admin']) { // data not null
          ServerConfigCustomAdmin.validateJSON(data['admin']);
        }
        // validate the optional field `autoBlacklist`
        if (data['autoBlacklist']) { // data not null
          ServerConfigAutoBlacklist.validateJSON(data['autoBlacklist']);
        }
        // validate the optional field `cache`
        if (data['cache']) { // data not null
          ServerConfigCustomCache.validateJSON(data['cache']);
        }
        // validate the optional field `contactForm`
        if (data['contactForm']) { // data not null
          ServerConfigAutoBlacklistVideosOfUsers.validateJSON(data['contactForm']);
        }
        // validate the optional field `followers`
        if (data['followers']) { // data not null
          ServerConfigCustomFollowers.validateJSON(data['followers']);
        }
        // validate the optional field `import`
        if (data['import']) { // data not null
          ServerConfigCustomImport.validateJSON(data['import']);
        }
        // validate the optional field `instance`
        if (data['instance']) { // data not null
          ServerConfigCustomInstance.validateJSON(data['instance']);
        }
        // validate the optional field `services`
        if (data['services']) { // data not null
          ServerConfigCustomServices.validateJSON(data['services']);
        }
        // validate the optional field `signup`
        if (data['signup']) { // data not null
          ServerConfigCustomSignup.validateJSON(data['signup']);
        }
        // validate the optional field `theme`
        if (data['theme']) { // data not null
          ServerConfigCustomTheme.validateJSON(data['theme']);
        }
        // validate the optional field `transcoding`
        if (data['transcoding']) { // data not null
          ServerConfigCustomTranscoding.validateJSON(data['transcoding']);
        }
        // validate the optional field `user`
        if (data['user']) { // data not null
          ServerConfigCustomUser.validateJSON(data['user']);
        }

        return true;
    }


}



/**
 * @member {module:model/ServerConfigCustomAdmin} admin
 */
ServerConfigCustom.prototype['admin'] = undefined;

/**
 * @member {module:model/ServerConfigAutoBlacklist} autoBlacklist
 */
ServerConfigCustom.prototype['autoBlacklist'] = undefined;

/**
 * @member {module:model/ServerConfigCustomCache} cache
 */
ServerConfigCustom.prototype['cache'] = undefined;

/**
 * @member {module:model/ServerConfigAutoBlacklistVideosOfUsers} contactForm
 */
ServerConfigCustom.prototype['contactForm'] = undefined;

/**
 * @member {module:model/ServerConfigCustomFollowers} followers
 */
ServerConfigCustom.prototype['followers'] = undefined;

/**
 * @member {module:model/ServerConfigCustomImport} import
 */
ServerConfigCustom.prototype['import'] = undefined;

/**
 * @member {module:model/ServerConfigCustomInstance} instance
 */
ServerConfigCustom.prototype['instance'] = undefined;

/**
 * @member {module:model/ServerConfigCustomServices} services
 */
ServerConfigCustom.prototype['services'] = undefined;

/**
 * @member {module:model/ServerConfigCustomSignup} signup
 */
ServerConfigCustom.prototype['signup'] = undefined;

/**
 * @member {module:model/ServerConfigCustomTheme} theme
 */
ServerConfigCustom.prototype['theme'] = undefined;

/**
 * @member {module:model/ServerConfigCustomTranscoding} transcoding
 */
ServerConfigCustom.prototype['transcoding'] = undefined;

/**
 * @member {module:model/ServerConfigCustomUser} user
 */
ServerConfigCustom.prototype['user'] = undefined;






export default ServerConfigCustom;

