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
import AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner from './AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner';

/**
 * The CrashGroupOperatingSystems model module.
 * @module model/CrashGroupOperatingSystems
 * @version v0.1
 */
class CrashGroupOperatingSystems {
    /**
     * Constructs a new <code>CrashGroupOperatingSystems</code>.
     * @alias module:model/CrashGroupOperatingSystems
     */
    constructor() { 
        
        CrashGroupOperatingSystems.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CrashGroupOperatingSystems</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CrashGroupOperatingSystems} obj Optional instance to populate.
     * @return {module:model/CrashGroupOperatingSystems} The populated <code>CrashGroupOperatingSystems</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CrashGroupOperatingSystems();

            if (data.hasOwnProperty('crash_count')) {
                obj['crash_count'] = ApiClient.convertToType(data['crash_count'], 'Number');
            }
            if (data.hasOwnProperty('operating_systems')) {
                obj['operating_systems'] = ApiClient.convertToType(data['operating_systems'], [AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CrashGroupOperatingSystems</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CrashGroupOperatingSystems</code>.
     */
    static validateJSON(data) {
        if (data['operating_systems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['operating_systems'])) {
                throw new Error("Expected the field `operating_systems` to be an array in the JSON data but got " + data['operating_systems']);
            }
            // validate the optional field `operating_systems` (array)
            for (const item of data['operating_systems']) {
                AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} crash_count
 */
CrashGroupOperatingSystems.prototype['crash_count'] = undefined;

/**
 * @member {Array.<module:model/AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner>} operating_systems
 */
CrashGroupOperatingSystems.prototype['operating_systems'] = undefined;






export default CrashGroupOperatingSystems;

