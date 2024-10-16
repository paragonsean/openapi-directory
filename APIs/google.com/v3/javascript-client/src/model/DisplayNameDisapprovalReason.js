/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DisplayNameDisapprovalReason model module.
 * @module model/DisplayNameDisapprovalReason
 * @version v3
 */
class DisplayNameDisapprovalReason {
    /**
     * Constructs a new <code>DisplayNameDisapprovalReason</code>.
     * Disapproval reason of the display name in a specific language.
     * @alias module:model/DisplayNameDisapprovalReason
     */
    constructor() { 
        
        DisplayNameDisapprovalReason.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DisplayNameDisapprovalReason</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DisplayNameDisapprovalReason} obj Optional instance to populate.
     * @return {module:model/DisplayNameDisapprovalReason} The populated <code>DisplayNameDisapprovalReason</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DisplayNameDisapprovalReason();

            if (data.hasOwnProperty('disapprovalReason')) {
                obj['disapprovalReason'] = ApiClient.convertToType(data['disapprovalReason'], 'String');
            }
            if (data.hasOwnProperty('languageCode')) {
                obj['languageCode'] = ApiClient.convertToType(data['languageCode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DisplayNameDisapprovalReason</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DisplayNameDisapprovalReason</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['disapprovalReason'] && !(typeof data['disapprovalReason'] === 'string' || data['disapprovalReason'] instanceof String)) {
            throw new Error("Expected the field `disapprovalReason` to be a primitive type in the JSON string but got " + data['disapprovalReason']);
        }
        // ensure the json data is a string
        if (data['languageCode'] && !(typeof data['languageCode'] === 'string' || data['languageCode'] instanceof String)) {
            throw new Error("Expected the field `languageCode` to be a primitive type in the JSON string but got " + data['languageCode']);
        }

        return true;
    }


}



/**
 * Disapproval reason.
 * @member {module:model/DisplayNameDisapprovalReason.DisapprovalReasonEnum} disapprovalReason
 */
DisplayNameDisapprovalReason.prototype['disapprovalReason'] = undefined;

/**
 * Language of the disapproved display name.
 * @member {String} languageCode
 */
DisplayNameDisapprovalReason.prototype['languageCode'] = undefined;





/**
 * Allowed values for the <code>disapprovalReason</code> property.
 * @enum {String}
 * @readonly
 */
DisplayNameDisapprovalReason['DisapprovalReasonEnum'] = {

    /**
     * value: "DISAPPROVAL_REASON_UNSPECIFIED"
     * @const
     */
    "DISAPPROVAL_REASON_UNSPECIFIED": "DISAPPROVAL_REASON_UNSPECIFIED",

    /**
     * value: "PUNCTUATION"
     * @const
     */
    "PUNCTUATION": "PUNCTUATION",

    /**
     * value: "MARKETING_LANGUAGE"
     * @const
     */
    "MARKETING_LANGUAGE": "MARKETING_LANGUAGE",

    /**
     * value: "LANDING_PAGE_NOT_MATCHED"
     * @const
     */
    "LANDING_PAGE_NOT_MATCHED": "LANDING_PAGE_NOT_MATCHED"
};



export default DisplayNameDisapprovalReason;

