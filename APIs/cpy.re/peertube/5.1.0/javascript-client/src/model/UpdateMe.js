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

/**
 * The UpdateMe model module.
 * @module model/UpdateMe
 * @version 5.1.0
 */
class UpdateMe {
    /**
     * Constructs a new <code>UpdateMe</code>.
     * @alias module:model/UpdateMe
     */
    constructor() { 
        
        UpdateMe.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateMe</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateMe} obj Optional instance to populate.
     * @return {module:model/UpdateMe} The populated <code>UpdateMe</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateMe();

            if (data.hasOwnProperty('autoPlayNextVideo')) {
                obj['autoPlayNextVideo'] = ApiClient.convertToType(data['autoPlayNextVideo'], 'Boolean');
            }
            if (data.hasOwnProperty('autoPlayNextVideoPlaylist')) {
                obj['autoPlayNextVideoPlaylist'] = ApiClient.convertToType(data['autoPlayNextVideoPlaylist'], 'Boolean');
            }
            if (data.hasOwnProperty('autoPlayVideo')) {
                obj['autoPlayVideo'] = ApiClient.convertToType(data['autoPlayVideo'], 'Boolean');
            }
            if (data.hasOwnProperty('currentPassword')) {
                obj['currentPassword'] = ApiClient.convertToType(data['currentPassword'], 'String');
            }
            if (data.hasOwnProperty('displayNSFW')) {
                obj['displayNSFW'] = ApiClient.convertToType(data['displayNSFW'], 'String');
            }
            if (data.hasOwnProperty('displayName')) {
                obj['displayName'] = ApiClient.convertToType(data['displayName'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
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
            if (data.hasOwnProperty('p2pEnabled')) {
                obj['p2pEnabled'] = ApiClient.convertToType(data['p2pEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('theme')) {
                obj['theme'] = ApiClient.convertToType(data['theme'], 'String');
            }
            if (data.hasOwnProperty('videoLanguages')) {
                obj['videoLanguages'] = ApiClient.convertToType(data['videoLanguages'], ['String']);
            }
            if (data.hasOwnProperty('videosHistoryEnabled')) {
                obj['videosHistoryEnabled'] = ApiClient.convertToType(data['videosHistoryEnabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateMe</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateMe</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['currentPassword'] && !(typeof data['currentPassword'] === 'string' || data['currentPassword'] instanceof String)) {
            throw new Error("Expected the field `currentPassword` to be a primitive type in the JSON string but got " + data['currentPassword']);
        }
        // ensure the json data is a string
        if (data['displayNSFW'] && !(typeof data['displayNSFW'] === 'string' || data['displayNSFW'] instanceof String)) {
            throw new Error("Expected the field `displayNSFW` to be a primitive type in the JSON string but got " + data['displayNSFW']);
        }
        // ensure the json data is a string
        if (data['displayName'] && !(typeof data['displayName'] === 'string' || data['displayName'] instanceof String)) {
            throw new Error("Expected the field `displayName` to be a primitive type in the JSON string but got " + data['displayName']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['theme'] && !(typeof data['theme'] === 'string' || data['theme'] instanceof String)) {
            throw new Error("Expected the field `theme` to be a primitive type in the JSON string but got " + data['theme']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['videoLanguages'])) {
            throw new Error("Expected the field `videoLanguages` to be an array in the JSON data but got " + data['videoLanguages']);
        }

        return true;
    }


}



/**
 * new preference regarding playing following videos automatically
 * @member {Boolean} autoPlayNextVideo
 */
UpdateMe.prototype['autoPlayNextVideo'] = undefined;

/**
 * new preference regarding playing following playlist videos automatically
 * @member {Boolean} autoPlayNextVideoPlaylist
 */
UpdateMe.prototype['autoPlayNextVideoPlaylist'] = undefined;

/**
 * new preference regarding playing videos automatically
 * @member {Boolean} autoPlayVideo
 */
UpdateMe.prototype['autoPlayVideo'] = undefined;

/**
 * @member {String} currentPassword
 */
UpdateMe.prototype['currentPassword'] = undefined;

/**
 * new NSFW display policy
 * @member {module:model/UpdateMe.DisplayNSFWEnum} displayNSFW
 */
UpdateMe.prototype['displayNSFW'] = undefined;

/**
 * new name of the user in its representations
 * @member {String} displayName
 */
UpdateMe.prototype['displayName'] = undefined;

/**
 * new email used for login and service communications
 * @member {String} email
 */
UpdateMe.prototype['email'] = undefined;

/**
 * @member {Boolean} noAccountSetupWarningModal
 */
UpdateMe.prototype['noAccountSetupWarningModal'] = undefined;

/**
 * @member {Boolean} noInstanceConfigWarningModal
 */
UpdateMe.prototype['noInstanceConfigWarningModal'] = undefined;

/**
 * @member {Boolean} noWelcomeModal
 */
UpdateMe.prototype['noWelcomeModal'] = undefined;

/**
 * whether to enable P2P in the player or not
 * @member {Boolean} p2pEnabled
 */
UpdateMe.prototype['p2pEnabled'] = undefined;

/**
 * @member {String} password
 */
UpdateMe.prototype['password'] = undefined;

/**
 * @member {String} theme
 */
UpdateMe.prototype['theme'] = undefined;

/**
 * list of languages to filter videos down to
 * @member {Array.<String>} videoLanguages
 */
UpdateMe.prototype['videoLanguages'] = undefined;

/**
 * whether to keep track of watched history or not
 * @member {Boolean} videosHistoryEnabled
 */
UpdateMe.prototype['videosHistoryEnabled'] = undefined;





/**
 * Allowed values for the <code>displayNSFW</code> property.
 * @enum {String}
 * @readonly
 */
UpdateMe['DisplayNSFWEnum'] = {

    /**
     * value: "true"
     * @const
     */
    "true": "true",

    /**
     * value: "false"
     * @const
     */
    "false": "false",

    /**
     * value: "both"
     * @const
     */
    "both": "both"
};



export default UpdateMe;

