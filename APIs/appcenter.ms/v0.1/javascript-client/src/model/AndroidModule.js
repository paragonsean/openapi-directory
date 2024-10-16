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
import BuildsListToolsetProjects200ResponseAndroidAndroidModulesInnerBuildConfigurationsInner from './BuildsListToolsetProjects200ResponseAndroidAndroidModulesInnerBuildConfigurationsInner';

/**
 * The AndroidModule model module.
 * @module model/AndroidModule
 * @version v0.1
 */
class AndroidModule {
    /**
     * Constructs a new <code>AndroidModule</code>.
     * @alias module:model/AndroidModule
     * @param name {String} Name of the Android module
     */
    constructor(name) { 
        
        AndroidModule.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>AndroidModule</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AndroidModule} obj Optional instance to populate.
     * @return {module:model/AndroidModule} The populated <code>AndroidModule</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AndroidModule();

            if (data.hasOwnProperty('buildConfigurations')) {
                obj['buildConfigurations'] = ApiClient.convertToType(data['buildConfigurations'], [BuildsListToolsetProjects200ResponseAndroidAndroidModulesInnerBuildConfigurationsInner]);
            }
            if (data.hasOwnProperty('buildTypes')) {
                obj['buildTypes'] = ApiClient.convertToType(data['buildTypes'], ['String']);
            }
            if (data.hasOwnProperty('buildVariants')) {
                obj['buildVariants'] = ApiClient.convertToType(data['buildVariants'], ['String']);
            }
            if (data.hasOwnProperty('hasBundle')) {
                obj['hasBundle'] = ApiClient.convertToType(data['hasBundle'], 'Boolean');
            }
            if (data.hasOwnProperty('isRoot')) {
                obj['isRoot'] = ApiClient.convertToType(data['isRoot'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('productFlavors')) {
                obj['productFlavors'] = ApiClient.convertToType(data['productFlavors'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AndroidModule</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AndroidModule</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AndroidModule.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['buildConfigurations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['buildConfigurations'])) {
                throw new Error("Expected the field `buildConfigurations` to be an array in the JSON data but got " + data['buildConfigurations']);
            }
            // validate the optional field `buildConfigurations` (array)
            for (const item of data['buildConfigurations']) {
                BuildsListToolsetProjects200ResponseAndroidAndroidModulesInnerBuildConfigurationsInner.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['buildTypes'])) {
            throw new Error("Expected the field `buildTypes` to be an array in the JSON data but got " + data['buildTypes']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['buildVariants'])) {
            throw new Error("Expected the field `buildVariants` to be an array in the JSON data but got " + data['buildVariants']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['productFlavors'])) {
            throw new Error("Expected the field `productFlavors` to be an array in the JSON data but got " + data['productFlavors']);
        }

        return true;
    }


}

AndroidModule.RequiredProperties = ["name"];

/**
 * The detected build configurations of the Android module
 * @member {Array.<module:model/BuildsListToolsetProjects200ResponseAndroidAndroidModulesInnerBuildConfigurationsInner>} buildConfigurations
 */
AndroidModule.prototype['buildConfigurations'] = undefined;

/**
 * The detected build types of the Android module
 * @member {Array.<String>} buildTypes
 */
AndroidModule.prototype['buildTypes'] = undefined;

/**
 * The detected build variants of the Android module (matrix of product flavor + build type (debug|release))
 * @member {Array.<String>} buildVariants
 */
AndroidModule.prototype['buildVariants'] = undefined;

/**
 * Module contains bundle settings
 * @member {Boolean} hasBundle
 */
AndroidModule.prototype['hasBundle'] = undefined;

/**
 * Whether the module is at the root level of the project
 * @member {Boolean} isRoot
 */
AndroidModule.prototype['isRoot'] = undefined;

/**
 * Name of the Android module
 * @member {String} name
 */
AndroidModule.prototype['name'] = undefined;

/**
 * The product flavors of the Android module
 * @member {Array.<String>} productFlavors
 */
AndroidModule.prototype['productFlavors'] = undefined;






export default AndroidModule;

