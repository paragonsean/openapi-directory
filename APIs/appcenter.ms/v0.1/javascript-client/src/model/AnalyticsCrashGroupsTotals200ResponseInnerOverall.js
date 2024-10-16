/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AnalyticsCrashGroupsTotals200ResponseInnerOverall model module.
 * @module model/AnalyticsCrashGroupsTotals200ResponseInnerOverall
 * @version v0.1
 */
class AnalyticsCrashGroupsTotals200ResponseInnerOverall {
    /**
     * Constructs a new <code>AnalyticsCrashGroupsTotals200ResponseInnerOverall</code>.
     * @alias module:model/AnalyticsCrashGroupsTotals200ResponseInnerOverall
     */
    constructor() { 
        
        AnalyticsCrashGroupsTotals200ResponseInnerOverall.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalyticsCrashGroupsTotals200ResponseInnerOverall</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalyticsCrashGroupsTotals200ResponseInnerOverall} obj Optional instance to populate.
     * @return {module:model/AnalyticsCrashGroupsTotals200ResponseInnerOverall} The populated <code>AnalyticsCrashGroupsTotals200ResponseInnerOverall</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalyticsCrashGroupsTotals200ResponseInnerOverall();

            if (data.hasOwnProperty('crash_count')) {
                obj['crash_count'] = ApiClient.convertToType(data['crash_count'], 'Number');
            }
            if (data.hasOwnProperty('device_count')) {
                obj['device_count'] = ApiClient.convertToType(data['device_count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnalyticsCrashGroupsTotals200ResponseInnerOverall</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnalyticsCrashGroupsTotals200ResponseInnerOverall</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Number} crash_count
 */
AnalyticsCrashGroupsTotals200ResponseInnerOverall.prototype['crash_count'] = undefined;

/**
 * @member {Number} device_count
 */
AnalyticsCrashGroupsTotals200ResponseInnerOverall.prototype['device_count'] = undefined;






export default AnalyticsCrashGroupsTotals200ResponseInnerOverall;

