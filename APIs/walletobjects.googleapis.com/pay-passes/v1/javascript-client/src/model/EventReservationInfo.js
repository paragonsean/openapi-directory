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

/**
 * The EventReservationInfo model module.
 * @module model/EventReservationInfo
 * @version v1
 */
class EventReservationInfo {
    /**
     * Constructs a new <code>EventReservationInfo</code>.
     * @alias module:model/EventReservationInfo
     */
    constructor() { 
        
        EventReservationInfo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EventReservationInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventReservationInfo} obj Optional instance to populate.
     * @return {module:model/EventReservationInfo} The populated <code>EventReservationInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventReservationInfo();

            if (data.hasOwnProperty('confirmationCode')) {
                obj['confirmationCode'] = ApiClient.convertToType(data['confirmationCode'], 'String');
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventReservationInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventReservationInfo</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['confirmationCode'] && !(typeof data['confirmationCode'] === 'string' || data['confirmationCode'] instanceof String)) {
            throw new Error("Expected the field `confirmationCode` to be a primitive type in the JSON string but got " + data['confirmationCode']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
        }

        return true;
    }


}



/**
 * The confirmation code of the event reservation. This may also take the form of an \"order number\", \"confirmation number\", \"reservation number\", or other equivalent.
 * @member {String} confirmationCode
 */
EventReservationInfo.prototype['confirmationCode'] = undefined;

/**
 * Identifies what kind of resource this is. Value: the fixed string `\"walletobjects#eventReservationInfo\"`.
 * @member {String} kind
 */
EventReservationInfo.prototype['kind'] = undefined;






export default EventReservationInfo;

