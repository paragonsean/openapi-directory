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
 * The ServerConfigCustomTranscodingResolutions model module.
 * @module model/ServerConfigCustomTranscodingResolutions
 * @version 5.1.0
 */
class ServerConfigCustomTranscodingResolutions {
    /**
     * Constructs a new <code>ServerConfigCustomTranscodingResolutions</code>.
     * Resolutions to transcode _new videos_ to
     * @alias module:model/ServerConfigCustomTranscodingResolutions
     */
    constructor() { 
        
        ServerConfigCustomTranscodingResolutions.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ServerConfigCustomTranscodingResolutions</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServerConfigCustomTranscodingResolutions} obj Optional instance to populate.
     * @return {module:model/ServerConfigCustomTranscodingResolutions} The populated <code>ServerConfigCustomTranscodingResolutions</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServerConfigCustomTranscodingResolutions();

            if (data.hasOwnProperty('0p')) {
                obj['0p'] = ApiClient.convertToType(data['0p'], 'Boolean');
            }
            if (data.hasOwnProperty('1080p')) {
                obj['1080p'] = ApiClient.convertToType(data['1080p'], 'Boolean');
            }
            if (data.hasOwnProperty('1440p')) {
                obj['1440p'] = ApiClient.convertToType(data['1440p'], 'Boolean');
            }
            if (data.hasOwnProperty('144p')) {
                obj['144p'] = ApiClient.convertToType(data['144p'], 'Boolean');
            }
            if (data.hasOwnProperty('2160p')) {
                obj['2160p'] = ApiClient.convertToType(data['2160p'], 'Boolean');
            }
            if (data.hasOwnProperty('240p')) {
                obj['240p'] = ApiClient.convertToType(data['240p'], 'Boolean');
            }
            if (data.hasOwnProperty('360p')) {
                obj['360p'] = ApiClient.convertToType(data['360p'], 'Boolean');
            }
            if (data.hasOwnProperty('480p')) {
                obj['480p'] = ApiClient.convertToType(data['480p'], 'Boolean');
            }
            if (data.hasOwnProperty('720p')) {
                obj['720p'] = ApiClient.convertToType(data['720p'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServerConfigCustomTranscodingResolutions</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServerConfigCustomTranscodingResolutions</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Boolean} 0p
 */
ServerConfigCustomTranscodingResolutions.prototype['0p'] = undefined;

/**
 * @member {Boolean} 1080p
 */
ServerConfigCustomTranscodingResolutions.prototype['1080p'] = undefined;

/**
 * @member {Boolean} 1440p
 */
ServerConfigCustomTranscodingResolutions.prototype['1440p'] = undefined;

/**
 * @member {Boolean} 144p
 */
ServerConfigCustomTranscodingResolutions.prototype['144p'] = undefined;

/**
 * @member {Boolean} 2160p
 */
ServerConfigCustomTranscodingResolutions.prototype['2160p'] = undefined;

/**
 * @member {Boolean} 240p
 */
ServerConfigCustomTranscodingResolutions.prototype['240p'] = undefined;

/**
 * @member {Boolean} 360p
 */
ServerConfigCustomTranscodingResolutions.prototype['360p'] = undefined;

/**
 * @member {Boolean} 480p
 */
ServerConfigCustomTranscodingResolutions.prototype['480p'] = undefined;

/**
 * @member {Boolean} 720p
 */
ServerConfigCustomTranscodingResolutions.prototype['720p'] = undefined;






export default ServerConfigCustomTranscodingResolutions;

