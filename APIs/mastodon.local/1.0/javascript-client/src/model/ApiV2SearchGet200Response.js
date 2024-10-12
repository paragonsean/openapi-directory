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
import Account from './Account';
import Status from './Status';
import Tag from './Tag';

/**
 * The ApiV2SearchGet200Response model module.
 * @module model/ApiV2SearchGet200Response
 * @version 1.0
 */
class ApiV2SearchGet200Response {
    /**
     * Constructs a new <code>ApiV2SearchGet200Response</code>.
     * @alias module:model/ApiV2SearchGet200Response
     */
    constructor() { 
        
        ApiV2SearchGet200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiV2SearchGet200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiV2SearchGet200Response} obj Optional instance to populate.
     * @return {module:model/ApiV2SearchGet200Response} The populated <code>ApiV2SearchGet200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiV2SearchGet200Response();

            if (data.hasOwnProperty('accounts')) {
                obj['accounts'] = ApiClient.convertToType(data['accounts'], [Account]);
            }
            if (data.hasOwnProperty('hashtags')) {
                obj['hashtags'] = ApiClient.convertToType(data['hashtags'], [Status]);
            }
            if (data.hasOwnProperty('statuses')) {
                obj['statuses'] = ApiClient.convertToType(data['statuses'], [Tag]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiV2SearchGet200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiV2SearchGet200Response</code>.
     */
    static validateJSON(data) {
        if (data['accounts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['accounts'])) {
                throw new Error("Expected the field `accounts` to be an array in the JSON data but got " + data['accounts']);
            }
            // validate the optional field `accounts` (array)
            for (const item of data['accounts']) {
                Account.validateJSON(item);
            };
        }
        if (data['hashtags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['hashtags'])) {
                throw new Error("Expected the field `hashtags` to be an array in the JSON data but got " + data['hashtags']);
            }
            // validate the optional field `hashtags` (array)
            for (const item of data['hashtags']) {
                Status.validateJSON(item);
            };
        }
        if (data['statuses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['statuses'])) {
                throw new Error("Expected the field `statuses` to be an array in the JSON data but got " + data['statuses']);
            }
            // validate the optional field `statuses` (array)
            for (const item of data['statuses']) {
                Tag.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Account>} accounts
 */
ApiV2SearchGet200Response.prototype['accounts'] = undefined;

/**
 * @member {Array.<module:model/Status>} hashtags
 */
ApiV2SearchGet200Response.prototype['hashtags'] = undefined;

/**
 * @member {Array.<module:model/Tag>} statuses
 */
ApiV2SearchGet200Response.prototype['statuses'] = undefined;






export default ApiV2SearchGet200Response;

