/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HidOtpRequestPaylaod model module.
 * @module model/HidOtpRequestPaylaod
 * @version 1.0
 */
class HidOtpRequestPaylaod {
    /**
     * Constructs a new <code>HidOtpRequestPaylaod</code>.
     * @alias module:model/HidOtpRequestPaylaod
     */
    constructor() { 
        
        HidOtpRequestPaylaod.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HidOtpRequestPaylaod</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HidOtpRequestPaylaod} obj Optional instance to populate.
     * @return {module:model/HidOtpRequestPaylaod} The populated <code>HidOtpRequestPaylaod</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HidOtpRequestPaylaod();

            if (data.hasOwnProperty('newPassword')) {
                obj['newPassword'] = ApiClient.convertToType(data['newPassword'], 'String');
            }
            if (data.hasOwnProperty('otp')) {
                obj['otp'] = ApiClient.convertToType(data['otp'], 'String');
            }
            if (data.hasOwnProperty('txnId')) {
                obj['txnId'] = ApiClient.convertToType(data['txnId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HidOtpRequestPaylaod</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HidOtpRequestPaylaod</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['newPassword'] && !(typeof data['newPassword'] === 'string' || data['newPassword'] instanceof String)) {
            throw new Error("Expected the field `newPassword` to be a primitive type in the JSON string but got " + data['newPassword']);
        }
        // ensure the json data is a string
        if (data['otp'] && !(typeof data['otp'] === 'string' || data['otp'] instanceof String)) {
            throw new Error("Expected the field `otp` to be a primitive type in the JSON string but got " + data['otp']);
        }
        // ensure the json data is a string
        if (data['txnId'] && !(typeof data['txnId'] === 'string' || data['txnId'] instanceof String)) {
            throw new Error("Expected the field `txnId` to be a primitive type in the JSON string but got " + data['txnId']);
        }

        return true;
    }


}



/**
 * @member {String} newPassword
 */
HidOtpRequestPaylaod.prototype['newPassword'] = undefined;

/**
 * @member {String} otp
 */
HidOtpRequestPaylaod.prototype['otp'] = undefined;

/**
 * @member {String} txnId
 */
HidOtpRequestPaylaod.prototype['txnId'] = undefined;






export default HidOtpRequestPaylaod;

