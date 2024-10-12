/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GiftCardClass from './GiftCardClass';

/**
 * The GiftCardClassAddMessageResponse model module.
 * @module model/GiftCardClassAddMessageResponse
 * @version v1
 */
class GiftCardClassAddMessageResponse {
    /**
     * Constructs a new <code>GiftCardClassAddMessageResponse</code>.
     * @alias module:model/GiftCardClassAddMessageResponse
     */
    constructor() { 
        
        GiftCardClassAddMessageResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GiftCardClassAddMessageResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GiftCardClassAddMessageResponse} obj Optional instance to populate.
     * @return {module:model/GiftCardClassAddMessageResponse} The populated <code>GiftCardClassAddMessageResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GiftCardClassAddMessageResponse();

            if (data.hasOwnProperty('resource')) {
                obj['resource'] = GiftCardClass.constructFromObject(data['resource']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GiftCardClassAddMessageResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GiftCardClassAddMessageResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `resource`
        if (data['resource']) { // data not null
          GiftCardClass.validateJSON(data['resource']);
        }

        return true;
    }


}



/**
 * @member {module:model/GiftCardClass} resource
 */
GiftCardClassAddMessageResponse.prototype['resource'] = undefined;






export default GiftCardClassAddMessageResponse;

