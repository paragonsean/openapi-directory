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
 * The TimeInterval model module.
 * @module model/TimeInterval
 * @version v1
 */
class TimeInterval {
    /**
     * Constructs a new <code>TimeInterval</code>.
     * @alias module:model/TimeInterval
     */
    constructor() { 
        
        TimeInterval.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TimeInterval</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TimeInterval} obj Optional instance to populate.
     * @return {module:model/TimeInterval} The populated <code>TimeInterval</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TimeInterval();

            if (data.hasOwnProperty('end')) {
                obj['end'] = 'Date'.constructFromObject(data['end']);
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
            if (data.hasOwnProperty('start')) {
                obj['start'] = 'Date'.constructFromObject(data['start']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TimeInterval</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TimeInterval</code>.
     */
    static validateJSON(data) {
        // validate the optional field `end`
        if (data['end']) { // data not null
          Date.validateJSON(data['end']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
        }
        // validate the optional field `start`
        if (data['start']) { // data not null
          Date.validateJSON(data['start']);
        }

        return true;
    }


}



/**
 * @member {Date} end
 */
TimeInterval.prototype['end'] = undefined;

/**
 * Identifies what kind of resource this is. Value: the fixed string `\"walletobjects#timeInterval\"`.
 * @member {String} kind
 */
TimeInterval.prototype['kind'] = undefined;

/**
 * @member {Date} start
 */
TimeInterval.prototype['start'] = undefined;






export default TimeInterval;

