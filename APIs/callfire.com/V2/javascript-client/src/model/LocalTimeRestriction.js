/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The LocalTimeRestriction model module.
 * @module model/LocalTimeRestriction
 * @version V2
 */
class LocalTimeRestriction {
    /**
     * Constructs a new <code>LocalTimeRestriction</code>.
     * Represents a range of time during which CallFire will send a call or text to recipients. Timeframe uses the local timezone of recipient&#39;s number
     * @alias module:model/LocalTimeRestriction
     */
    constructor() { 
        
        LocalTimeRestriction.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LocalTimeRestriction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LocalTimeRestriction} obj Optional instance to populate.
     * @return {module:model/LocalTimeRestriction} The populated <code>LocalTimeRestriction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LocalTimeRestriction();

            if (data.hasOwnProperty('beginHour')) {
                obj['beginHour'] = ApiClient.convertToType(data['beginHour'], 'Number');
            }
            if (data.hasOwnProperty('beginMinute')) {
                obj['beginMinute'] = ApiClient.convertToType(data['beginMinute'], 'Number');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('endHour')) {
                obj['endHour'] = ApiClient.convertToType(data['endHour'], 'Number');
            }
            if (data.hasOwnProperty('endMinute')) {
                obj['endMinute'] = ApiClient.convertToType(data['endMinute'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LocalTimeRestriction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LocalTimeRestriction</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * An hour of restriction start
 * @member {Number} beginHour
 */
LocalTimeRestriction.prototype['beginHour'] = undefined;

/**
 * The minutes to start a restriction
 * @member {Number} beginMinute
 */
LocalTimeRestriction.prototype['beginMinute'] = undefined;

/**
 * A restriction enabled
 * @member {Boolean} enabled
 */
LocalTimeRestriction.prototype['enabled'] = undefined;

/**
 * An hour of restriction end
 * @member {Number} endHour
 */
LocalTimeRestriction.prototype['endHour'] = undefined;

/**
 * The minutes of restriction end
 * @member {Number} endMinute
 */
LocalTimeRestriction.prototype['endMinute'] = undefined;






export default LocalTimeRestriction;

