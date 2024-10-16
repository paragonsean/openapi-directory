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
 * The GlobalResourcesSharedModelsGlobalImageCategory model module.
 * @module model/GlobalResourcesSharedModelsGlobalImageCategory
 * @version v1
 */
class GlobalResourcesSharedModelsGlobalImageCategory {
    /**
     * Constructs a new <code>GlobalResourcesSharedModelsGlobalImageCategory</code>.
     * An image category from the Global Image library.
     * @alias module:model/GlobalResourcesSharedModelsGlobalImageCategory
     * @param name {String} The name of the globalImage Catetory.
     */
    constructor(name) { 
        
        GlobalResourcesSharedModelsGlobalImageCategory.initialize(this, name);
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
     * Constructs a <code>GlobalResourcesSharedModelsGlobalImageCategory</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GlobalResourcesSharedModelsGlobalImageCategory} obj Optional instance to populate.
     * @return {module:model/GlobalResourcesSharedModelsGlobalImageCategory} The populated <code>GlobalResourcesSharedModelsGlobalImageCategory</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GlobalResourcesSharedModelsGlobalImageCategory();

            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GlobalResourcesSharedModelsGlobalImageCategory</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GlobalResourcesSharedModelsGlobalImageCategory</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GlobalResourcesSharedModelsGlobalImageCategory.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['Id'] && !(typeof data['Id'] === 'string' || data['Id'] instanceof String)) {
            throw new Error("Expected the field `Id` to be a primitive type in the JSON string but got " + data['Id']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }

        return true;
    }


}

GlobalResourcesSharedModelsGlobalImageCategory.RequiredProperties = ["Name"];

/**
 * The Id of the GlobalImage Categories.
 * @member {String} Id
 */
GlobalResourcesSharedModelsGlobalImageCategory.prototype['Id'] = undefined;

/**
 * The name of the globalImage Catetory.
 * @member {String} Name
 */
GlobalResourcesSharedModelsGlobalImageCategory.prototype['Name'] = undefined;






export default GlobalResourcesSharedModelsGlobalImageCategory;

