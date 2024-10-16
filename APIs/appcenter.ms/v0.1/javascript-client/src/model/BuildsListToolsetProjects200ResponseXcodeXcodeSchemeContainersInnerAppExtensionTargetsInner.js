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
 * The BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner model module.
 * @module model/BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner
 * @version v0.1
 */
class BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner {
    /**
     * Constructs a new <code>BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner</code>.
     * App extension information
     * @alias module:model/BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner
     * @param name {String} App extension name
     * @param targetBundleIdentifier {String} App extension bundle identifier
     */
    constructor(name, targetBundleIdentifier) { 
        
        BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner.initialize(this, name, targetBundleIdentifier);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, targetBundleIdentifier) { 
        obj['name'] = name;
        obj['targetBundleIdentifier'] = targetBundleIdentifier;
    }

    /**
     * Constructs a <code>BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner} obj Optional instance to populate.
     * @return {module:model/BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner} The populated <code>BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('targetBundleIdentifier')) {
                obj['targetBundleIdentifier'] = ApiClient.convertToType(data['targetBundleIdentifier'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['targetBundleIdentifier'] && !(typeof data['targetBundleIdentifier'] === 'string' || data['targetBundleIdentifier'] instanceof String)) {
            throw new Error("Expected the field `targetBundleIdentifier` to be a primitive type in the JSON string but got " + data['targetBundleIdentifier']);
        }

        return true;
    }


}

BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner.RequiredProperties = ["name", "targetBundleIdentifier"];

/**
 * App extension name
 * @member {String} name
 */
BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner.prototype['name'] = undefined;

/**
 * App extension bundle identifier
 * @member {String} targetBundleIdentifier
 */
BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner.prototype['targetBundleIdentifier'] = undefined;






export default BuildsListToolsetProjects200ResponseXcodeXcodeSchemeContainersInnerAppExtensionTargetsInner;

