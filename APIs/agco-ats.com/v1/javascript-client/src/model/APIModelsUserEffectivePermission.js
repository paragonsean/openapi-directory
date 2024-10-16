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
 * The APIModelsUserEffectivePermission model module.
 * @module model/APIModelsUserEffectivePermission
 * @version v1
 */
class APIModelsUserEffectivePermission {
    /**
     * Constructs a new <code>APIModelsUserEffectivePermission</code>.
     * @alias module:model/APIModelsUserEffectivePermission
     */
    constructor() { 
        
        APIModelsUserEffectivePermission.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>APIModelsUserEffectivePermission</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/APIModelsUserEffectivePermission} obj Optional instance to populate.
     * @return {module:model/APIModelsUserEffectivePermission} The populated <code>APIModelsUserEffectivePermission</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new APIModelsUserEffectivePermission();

            if (data.hasOwnProperty('PermissionId')) {
                obj['PermissionId'] = ApiClient.convertToType(data['PermissionId'], 'Number');
            }
            if (data.hasOwnProperty('PermissionName')) {
                obj['PermissionName'] = ApiClient.convertToType(data['PermissionName'], 'String');
            }
            if (data.hasOwnProperty('UserID')) {
                obj['UserID'] = ApiClient.convertToType(data['UserID'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>APIModelsUserEffectivePermission</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>APIModelsUserEffectivePermission</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['PermissionName'] && !(typeof data['PermissionName'] === 'string' || data['PermissionName'] instanceof String)) {
            throw new Error("Expected the field `PermissionName` to be a primitive type in the JSON string but got " + data['PermissionName']);
        }

        return true;
    }


}



/**
 * @member {Number} PermissionId
 */
APIModelsUserEffectivePermission.prototype['PermissionId'] = undefined;

/**
 * @member {String} PermissionName
 */
APIModelsUserEffectivePermission.prototype['PermissionName'] = undefined;

/**
 * @member {Number} UserID
 */
APIModelsUserEffectivePermission.prototype['UserID'] = undefined;






export default APIModelsUserEffectivePermission;

