/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApiV1AccountsIdMutePostRequest model module.
 * @module model/ApiV1AccountsIdMutePostRequest
 * @version 1.0
 */
class ApiV1AccountsIdMutePostRequest {
    /**
     * Constructs a new <code>ApiV1AccountsIdMutePostRequest</code>.
     * @alias module:model/ApiV1AccountsIdMutePostRequest
     */
    constructor() { 
        
        ApiV1AccountsIdMutePostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['duration'] = 0;
        obj['notifications'] = true;
    }

    /**
     * Constructs a <code>ApiV1AccountsIdMutePostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiV1AccountsIdMutePostRequest} obj Optional instance to populate.
     * @return {module:model/ApiV1AccountsIdMutePostRequest} The populated <code>ApiV1AccountsIdMutePostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiV1AccountsIdMutePostRequest();

            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'Number');
            }
            if (data.hasOwnProperty('notifications')) {
                obj['notifications'] = ApiClient.convertToType(data['notifications'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiV1AccountsIdMutePostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiV1AccountsIdMutePostRequest</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * How long the mute should last, in seconds. Defaults to 0 (indefinite).
 * @member {Number} duration
 * @default 0
 */
ApiV1AccountsIdMutePostRequest.prototype['duration'] = 0;

/**
 * Mute notifications in addition to statuses? Defaults to true.
 * @member {Boolean} notifications
 * @default true
 */
ApiV1AccountsIdMutePostRequest.prototype['notifications'] = true;






export default ApiV1AccountsIdMutePostRequest;

