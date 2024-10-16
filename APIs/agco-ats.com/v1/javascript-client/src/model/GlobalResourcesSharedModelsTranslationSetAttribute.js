/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
 * The GlobalResourcesSharedModelsTranslationSetAttribute model module.
 * @module model/GlobalResourcesSharedModelsTranslationSetAttribute
 * @version v1
 */
class GlobalResourcesSharedModelsTranslationSetAttribute {
    /**
     * Constructs a new <code>GlobalResourcesSharedModelsTranslationSetAttribute</code>.
     * An attribute of a
     * @alias module:model/GlobalResourcesSharedModelsTranslationSetAttribute
     * @param name {String} The name of this Attribute.
     */
    constructor(name) { 
        
        GlobalResourcesSharedModelsTranslationSetAttribute.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['Name'] = name;
    }

    /**
     * Constructs a <code>GlobalResourcesSharedModelsTranslationSetAttribute</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GlobalResourcesSharedModelsTranslationSetAttribute} obj Optional instance to populate.
     * @return {module:model/GlobalResourcesSharedModelsTranslationSetAttribute} The populated <code>GlobalResourcesSharedModelsTranslationSetAttribute</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GlobalResourcesSharedModelsTranslationSetAttribute();

            if (data.hasOwnProperty('ID')) {
                obj['ID'] = ApiClient.convertToType(data['ID'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('TranslationSetID')) {
                obj['TranslationSetID'] = ApiClient.convertToType(data['TranslationSetID'], 'Number');
            }
            if (data.hasOwnProperty('Value')) {
                obj['Value'] = ApiClient.convertToType(data['Value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GlobalResourcesSharedModelsTranslationSetAttribute</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GlobalResourcesSharedModelsTranslationSetAttribute</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GlobalResourcesSharedModelsTranslationSetAttribute.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Value'] && !(typeof data['Value'] === 'string' || data['Value'] instanceof String)) {
            throw new Error("Expected the field `Value` to be a primitive type in the JSON string but got " + data['Value']);
        }

        return true;
    }


}

GlobalResourcesSharedModelsTranslationSetAttribute.RequiredProperties = ["Name"];

/**
 * The ID of this attribute.
 * @member {Number} ID
 */
GlobalResourcesSharedModelsTranslationSetAttribute.prototype['ID'] = undefined;

/**
 * The name of this Attribute.
 * @member {String} Name
 */
GlobalResourcesSharedModelsTranslationSetAttribute.prototype['Name'] = undefined;

/**
 * The ID of the translation set to which this attribute belongs.
 * @member {Number} TranslationSetID
 */
GlobalResourcesSharedModelsTranslationSetAttribute.prototype['TranslationSetID'] = undefined;

/**
 * The value of this Attribute
 * @member {String} Value
 */
GlobalResourcesSharedModelsTranslationSetAttribute.prototype['Value'] = undefined;






export default GlobalResourcesSharedModelsTranslationSetAttribute;

