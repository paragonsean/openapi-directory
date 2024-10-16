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
import BuildsListToolsetProjects200ResponseAndroidAndroidModulesInner from './BuildsListToolsetProjects200ResponseAndroidAndroidModulesInner';

/**
 * The AndroidProject model module.
 * @module model/AndroidProject
 * @version v0.1
 */
class AndroidProject {
    /**
     * Constructs a new <code>AndroidProject</code>.
     * @alias module:model/AndroidProject
     * @param androidModules {Array.<module:model/BuildsListToolsetProjects200ResponseAndroidAndroidModulesInner>} Android Gradle modules
     */
    constructor(androidModules) { 
        
        AndroidProject.initialize(this, androidModules);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, androidModules) { 
        obj['androidModules'] = androidModules;
    }

    /**
     * Constructs a <code>AndroidProject</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AndroidProject} obj Optional instance to populate.
     * @return {module:model/AndroidProject} The populated <code>AndroidProject</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AndroidProject();

            if (data.hasOwnProperty('androidModules')) {
                obj['androidModules'] = ApiClient.convertToType(data['androidModules'], [BuildsListToolsetProjects200ResponseAndroidAndroidModulesInner]);
            }
            if (data.hasOwnProperty('gradleWrapperPath')) {
                obj['gradleWrapperPath'] = ApiClient.convertToType(data['gradleWrapperPath'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AndroidProject</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AndroidProject</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AndroidProject.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['androidModules']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['androidModules'])) {
                throw new Error("Expected the field `androidModules` to be an array in the JSON data but got " + data['androidModules']);
            }
            // validate the optional field `androidModules` (array)
            for (const item of data['androidModules']) {
                BuildsListToolsetProjects200ResponseAndroidAndroidModulesInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['gradleWrapperPath'] && !(typeof data['gradleWrapperPath'] === 'string' || data['gradleWrapperPath'] instanceof String)) {
            throw new Error("Expected the field `gradleWrapperPath` to be a primitive type in the JSON string but got " + data['gradleWrapperPath']);
        }

        return true;
    }


}

AndroidProject.RequiredProperties = ["androidModules"];

/**
 * Android Gradle modules
 * @member {Array.<module:model/BuildsListToolsetProjects200ResponseAndroidAndroidModulesInner>} androidModules
 */
AndroidProject.prototype['androidModules'] = undefined;

/**
 * The path of the Gradle wrapper
 * @member {String} gradleWrapperPath
 */
AndroidProject.prototype['gradleWrapperPath'] = undefined;






export default AndroidProject;

