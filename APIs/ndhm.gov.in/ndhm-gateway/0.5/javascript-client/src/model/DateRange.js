/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DateRange model module.
 * @module model/DateRange
 * @version 0.5
 */
class DateRange {
    /**
     * Constructs a new <code>DateRange</code>.
     * @alias module:model/DateRange
     * @param from {Date} 
     * @param to {Date} 
     */
    constructor(from, to) { 
        
        DateRange.initialize(this, from, to);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, from, to) { 
        obj['from'] = from;
        obj['to'] = to;
    }

    /**
     * Constructs a <code>DateRange</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DateRange} obj Optional instance to populate.
     * @return {module:model/DateRange} The populated <code>DateRange</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DateRange();

            if (data.hasOwnProperty('from')) {
                obj['from'] = ApiClient.convertToType(data['from'], 'Date');
            }
            if (data.hasOwnProperty('to')) {
                obj['to'] = ApiClient.convertToType(data['to'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DateRange</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DateRange</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DateRange.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

DateRange.RequiredProperties = ["from", "to"];

/**
 * @member {Date} from
 */
DateRange.prototype['from'] = undefined;

/**
 * @member {Date} to
 */
DateRange.prototype['to'] = undefined;






export default DateRange;

