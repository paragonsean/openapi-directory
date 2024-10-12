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
 * The ApiV1UsersMeNotificationSettingsPutRequest model module.
 * @module model/ApiV1UsersMeNotificationSettingsPutRequest
 * @version 5.1.0
 */
class ApiV1UsersMeNotificationSettingsPutRequest {
    /**
     * Constructs a new <code>ApiV1UsersMeNotificationSettingsPutRequest</code>.
     * @alias module:model/ApiV1UsersMeNotificationSettingsPutRequest
     */
    constructor() { 
        
        ApiV1UsersMeNotificationSettingsPutRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiV1UsersMeNotificationSettingsPutRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiV1UsersMeNotificationSettingsPutRequest} obj Optional instance to populate.
     * @return {module:model/ApiV1UsersMeNotificationSettingsPutRequest} The populated <code>ApiV1UsersMeNotificationSettingsPutRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiV1UsersMeNotificationSettingsPutRequest();

            if (data.hasOwnProperty('abuseAsModerator')) {
                obj['abuseAsModerator'] = ApiClient.convertToType(data['abuseAsModerator'], 'Number');
            }
            if (data.hasOwnProperty('autoInstanceFollowing')) {
                obj['autoInstanceFollowing'] = ApiClient.convertToType(data['autoInstanceFollowing'], 'Number');
            }
            if (data.hasOwnProperty('blacklistOnMyVideo')) {
                obj['blacklistOnMyVideo'] = ApiClient.convertToType(data['blacklistOnMyVideo'], 'Number');
            }
            if (data.hasOwnProperty('commentMention')) {
                obj['commentMention'] = ApiClient.convertToType(data['commentMention'], 'Number');
            }
            if (data.hasOwnProperty('myVideoImportFinished')) {
                obj['myVideoImportFinished'] = ApiClient.convertToType(data['myVideoImportFinished'], 'Number');
            }
            if (data.hasOwnProperty('myVideoPublished')) {
                obj['myVideoPublished'] = ApiClient.convertToType(data['myVideoPublished'], 'Number');
            }
            if (data.hasOwnProperty('newCommentOnMyVideo')) {
                obj['newCommentOnMyVideo'] = ApiClient.convertToType(data['newCommentOnMyVideo'], 'Number');
            }
            if (data.hasOwnProperty('newFollow')) {
                obj['newFollow'] = ApiClient.convertToType(data['newFollow'], 'Number');
            }
            if (data.hasOwnProperty('newInstanceFollower')) {
                obj['newInstanceFollower'] = ApiClient.convertToType(data['newInstanceFollower'], 'Number');
            }
            if (data.hasOwnProperty('newUserRegistration')) {
                obj['newUserRegistration'] = ApiClient.convertToType(data['newUserRegistration'], 'Number');
            }
            if (data.hasOwnProperty('newVideoFromSubscription')) {
                obj['newVideoFromSubscription'] = ApiClient.convertToType(data['newVideoFromSubscription'], 'Number');
            }
            if (data.hasOwnProperty('videoAutoBlacklistAsModerator')) {
                obj['videoAutoBlacklistAsModerator'] = ApiClient.convertToType(data['videoAutoBlacklistAsModerator'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiV1UsersMeNotificationSettingsPutRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiV1UsersMeNotificationSettingsPutRequest</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} abuseAsModerator
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['abuseAsModerator'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} autoInstanceFollowing
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['autoInstanceFollowing'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} blacklistOnMyVideo
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['blacklistOnMyVideo'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} commentMention
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['commentMention'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} myVideoImportFinished
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['myVideoImportFinished'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} myVideoPublished
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['myVideoPublished'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} newCommentOnMyVideo
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['newCommentOnMyVideo'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} newFollow
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['newFollow'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} newInstanceFollower
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['newInstanceFollower'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} newUserRegistration
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['newUserRegistration'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} newVideoFromSubscription
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['newVideoFromSubscription'] = undefined;

/**
 * Notification type. One of the following values, or a sum of multiple values: - `0` NONE - `1` WEB - `2` EMAIL 
 * @member {Number} videoAutoBlacklistAsModerator
 */
ApiV1UsersMeNotificationSettingsPutRequest.prototype['videoAutoBlacklistAsModerator'] = undefined;






export default ApiV1UsersMeNotificationSettingsPutRequest;

