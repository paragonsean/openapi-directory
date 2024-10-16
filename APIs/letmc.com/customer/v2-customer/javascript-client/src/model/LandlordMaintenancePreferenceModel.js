/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The LandlordMaintenancePreferenceModel model module.
 * @module model/LandlordMaintenancePreferenceModel
 * @version v2-customer
 */
class LandlordMaintenancePreferenceModel {
    /**
     * Constructs a new <code>LandlordMaintenancePreferenceModel</code>.
     * Maintenance Preference
     * @alias module:model/LandlordMaintenancePreferenceModel
     */
    constructor() { 
        
        LandlordMaintenancePreferenceModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LandlordMaintenancePreferenceModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LandlordMaintenancePreferenceModel} obj Optional instance to populate.
     * @return {module:model/LandlordMaintenancePreferenceModel} The populated <code>LandlordMaintenancePreferenceModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LandlordMaintenancePreferenceModel();

            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LandlordMaintenancePreferenceModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LandlordMaintenancePreferenceModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }

        return true;
    }


}



/**
 * Name
 * @member {String} Name
 */
LandlordMaintenancePreferenceModel.prototype['Name'] = undefined;

/**
 * Notes.
 * @member {String} Notes
 */
LandlordMaintenancePreferenceModel.prototype['Notes'] = undefined;

/**
 * Type
 * @member {String} Type
 */
LandlordMaintenancePreferenceModel.prototype['Type'] = undefined;






export default LandlordMaintenancePreferenceModel;

