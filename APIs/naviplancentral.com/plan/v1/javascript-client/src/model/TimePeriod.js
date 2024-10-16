/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
 * The TimePeriod model module.
 * @module model/TimePeriod
 * @version v1
 */
class TimePeriod {
    /**
     * Constructs a new <code>TimePeriod</code>.
     * @alias module:model/TimePeriod
     */
    constructor() { 
        
        TimePeriod.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TimePeriod</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TimePeriod} obj Optional instance to populate.
     * @return {module:model/TimePeriod} The populated <code>TimePeriod</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TimePeriod();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TimePeriod</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TimePeriod</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['duration'] && !(typeof data['duration'] === 'string' || data['duration'] instanceof String)) {
            throw new Error("Expected the field `duration` to be a primitive type in the JSON string but got " + data['duration']);
        }

        return true;
    }


}



/**
 * @member {Number} count
 */
TimePeriod.prototype['count'] = undefined;

/**
 * @member {module:model/TimePeriod.DurationEnum} duration
 */
TimePeriod.prototype['duration'] = undefined;





/**
 * Allowed values for the <code>duration</code> property.
 * @enum {String}
 * @readonly
 */
TimePeriod['DurationEnum'] = {

    /**
     * value: "Days"
     * @const
     */
    "Days": "Days",

    /**
     * value: "Weeks"
     * @const
     */
    "Weeks": "Weeks",

    /**
     * value: "Months"
     * @const
     */
    "Months": "Months",

    /**
     * value: "Years"
     * @const
     */
    "Years": "Years",

    /**
     * value: "YearsOfAge"
     * @const
     */
    "YearsOfAge": "YearsOfAge"
};



export default TimePeriod;

