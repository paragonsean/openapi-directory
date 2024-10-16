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
import BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner from './BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner';

/**
 * The BuildsListToolsetProjects200ResponseUwp model module.
 * @module model/BuildsListToolsetProjects200ResponseUwp
 * @version v0.1
 */
class BuildsListToolsetProjects200ResponseUwp {
    /**
     * Constructs a new <code>BuildsListToolsetProjects200ResponseUwp</code>.
     * @alias module:model/BuildsListToolsetProjects200ResponseUwp
     * @param uwpSolutions {Array.<module:model/BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner>} The UWP solutions detected
     */
    constructor(uwpSolutions) { 
        
        BuildsListToolsetProjects200ResponseUwp.initialize(this, uwpSolutions);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, uwpSolutions) { 
        obj['uwpSolutions'] = uwpSolutions;
    }

    /**
     * Constructs a <code>BuildsListToolsetProjects200ResponseUwp</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BuildsListToolsetProjects200ResponseUwp} obj Optional instance to populate.
     * @return {module:model/BuildsListToolsetProjects200ResponseUwp} The populated <code>BuildsListToolsetProjects200ResponseUwp</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BuildsListToolsetProjects200ResponseUwp();

            if (data.hasOwnProperty('uwpSolutions')) {
                obj['uwpSolutions'] = ApiClient.convertToType(data['uwpSolutions'], [BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BuildsListToolsetProjects200ResponseUwp</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BuildsListToolsetProjects200ResponseUwp</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BuildsListToolsetProjects200ResponseUwp.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['uwpSolutions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['uwpSolutions'])) {
                throw new Error("Expected the field `uwpSolutions` to be an array in the JSON data but got " + data['uwpSolutions']);
            }
            // validate the optional field `uwpSolutions` (array)
            for (const item of data['uwpSolutions']) {
                BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner.validateJSON(item);
            };
        }

        return true;
    }


}

BuildsListToolsetProjects200ResponseUwp.RequiredProperties = ["uwpSolutions"];

/**
 * The UWP solutions detected
 * @member {Array.<module:model/BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner>} uwpSolutions
 */
BuildsListToolsetProjects200ResponseUwp.prototype['uwpSolutions'] = undefined;






export default BuildsListToolsetProjects200ResponseUwp;

