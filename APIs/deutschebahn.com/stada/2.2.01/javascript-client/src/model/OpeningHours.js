/**
 * Stationsdatenbereitstellung
 * An API providing master data for German railway stations by DB Station&Service AG.
 *
 * The version of the OpenAPI document: 2.2.01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OpeningHours model module.
 * @module model/OpeningHours
 * @version 2.2.01
 */
class OpeningHours {
    /**
     * Constructs a new <code>OpeningHours</code>.
     * period of time from/to
     * @alias module:model/OpeningHours
     */
    constructor() { 
        
        OpeningHours.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OpeningHours</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OpeningHours} obj Optional instance to populate.
     * @return {module:model/OpeningHours} The populated <code>OpeningHours</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OpeningHours();

            if (data.hasOwnProperty('fromTime')) {
                obj['fromTime'] = ApiClient.convertToType(data['fromTime'], 'Date');
            }
            if (data.hasOwnProperty('toTime')) {
                obj['toTime'] = ApiClient.convertToType(data['toTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OpeningHours</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OpeningHours</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Date} fromTime
 */
OpeningHours.prototype['fromTime'] = undefined;

/**
 * @member {Date} toTime
 */
OpeningHours.prototype['toTime'] = undefined;






export default OpeningHours;

