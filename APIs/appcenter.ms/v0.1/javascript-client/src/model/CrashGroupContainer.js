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
import AnalyticsCrashGroupsTotalsRequestCrashGroupsInner from './AnalyticsCrashGroupsTotalsRequestCrashGroupsInner';

/**
 * The CrashGroupContainer model module.
 * @module model/CrashGroupContainer
 * @version v0.1
 */
class CrashGroupContainer {
    /**
     * Constructs a new <code>CrashGroupContainer</code>.
     * @alias module:model/CrashGroupContainer
     * @param crashGroups {Array.<module:model/AnalyticsCrashGroupsTotalsRequestCrashGroupsInner>} 
     */
    constructor(crashGroups) { 
        
        CrashGroupContainer.initialize(this, crashGroups);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, crashGroups) { 
        obj['crash_groups'] = crashGroups;
    }

    /**
     * Constructs a <code>CrashGroupContainer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CrashGroupContainer} obj Optional instance to populate.
     * @return {module:model/CrashGroupContainer} The populated <code>CrashGroupContainer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CrashGroupContainer();

            if (data.hasOwnProperty('crash_groups')) {
                obj['crash_groups'] = ApiClient.convertToType(data['crash_groups'], [AnalyticsCrashGroupsTotalsRequestCrashGroupsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CrashGroupContainer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CrashGroupContainer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CrashGroupContainer.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['crash_groups']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['crash_groups'])) {
                throw new Error("Expected the field `crash_groups` to be an array in the JSON data but got " + data['crash_groups']);
            }
            // validate the optional field `crash_groups` (array)
            for (const item of data['crash_groups']) {
                AnalyticsCrashGroupsTotalsRequestCrashGroupsInner.validateJSON(item);
            };
        }

        return true;
    }


}

CrashGroupContainer.RequiredProperties = ["crash_groups"];

/**
 * @member {Array.<module:model/AnalyticsCrashGroupsTotalsRequestCrashGroupsInner>} crash_groups
 */
CrashGroupContainer.prototype['crash_groups'] = undefined;






export default CrashGroupContainer;

