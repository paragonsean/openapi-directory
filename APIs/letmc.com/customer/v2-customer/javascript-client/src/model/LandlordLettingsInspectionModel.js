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
 * The LandlordLettingsInspectionModel model module.
 * @module model/LandlordLettingsInspectionModel
 * @version v2-customer
 */
class LandlordLettingsInspectionModel {
    /**
     * Constructs a new <code>LandlordLettingsInspectionModel</code>.
     * Lettings Inspection
     * @alias module:model/LandlordLettingsInspectionModel
     */
    constructor() { 
        
        LandlordLettingsInspectionModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LandlordLettingsInspectionModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LandlordLettingsInspectionModel} obj Optional instance to populate.
     * @return {module:model/LandlordLettingsInspectionModel} The populated <code>LandlordLettingsInspectionModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LandlordLettingsInspectionModel();

            if (data.hasOwnProperty('InspectionDate')) {
                obj['InspectionDate'] = ApiClient.convertToType(data['InspectionDate'], 'Date');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LandlordLettingsInspectionModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LandlordLettingsInspectionModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }

        return true;
    }


}



/**
 * InspectionDate
 * @member {Date} InspectionDate
 */
LandlordLettingsInspectionModel.prototype['InspectionDate'] = undefined;

/**
 * Notes
 * @member {String} Notes
 */
LandlordLettingsInspectionModel.prototype['Notes'] = undefined;






export default LandlordLettingsInspectionModel;

