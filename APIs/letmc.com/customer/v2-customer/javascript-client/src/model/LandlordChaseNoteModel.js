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
 * The LandlordChaseNoteModel model module.
 * @module model/LandlordChaseNoteModel
 * @version v2-customer
 */
class LandlordChaseNoteModel {
    /**
     * Constructs a new <code>LandlordChaseNoteModel</code>.
     * Landlord Arrears Chase Note.
     * @alias module:model/LandlordChaseNoteModel
     */
    constructor() { 
        
        LandlordChaseNoteModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LandlordChaseNoteModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LandlordChaseNoteModel} obj Optional instance to populate.
     * @return {module:model/LandlordChaseNoteModel} The populated <code>LandlordChaseNoteModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LandlordChaseNoteModel();

            if (data.hasOwnProperty('Date')) {
                obj['Date'] = ApiClient.convertToType(data['Date'], 'Date');
            }
            if (data.hasOwnProperty('Note')) {
                obj['Note'] = ApiClient.convertToType(data['Note'], 'String');
            }
            if (data.hasOwnProperty('NoteType')) {
                obj['NoteType'] = ApiClient.convertToType(data['NoteType'], 'String');
            }
            if (data.hasOwnProperty('TenantID')) {
                obj['TenantID'] = ApiClient.convertToType(data['TenantID'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LandlordChaseNoteModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LandlordChaseNoteModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Note'] && !(typeof data['Note'] === 'string' || data['Note'] instanceof String)) {
            throw new Error("Expected the field `Note` to be a primitive type in the JSON string but got " + data['Note']);
        }
        // ensure the json data is a string
        if (data['NoteType'] && !(typeof data['NoteType'] === 'string' || data['NoteType'] instanceof String)) {
            throw new Error("Expected the field `NoteType` to be a primitive type in the JSON string but got " + data['NoteType']);
        }
        // ensure the json data is a string
        if (data['TenantID'] && !(typeof data['TenantID'] === 'string' || data['TenantID'] instanceof String)) {
            throw new Error("Expected the field `TenantID` to be a primitive type in the JSON string but got " + data['TenantID']);
        }

        return true;
    }


}



/**
 * Created Date
 * @member {Date} Date
 */
LandlordChaseNoteModel.prototype['Date'] = undefined;

/**
 * Note.
 * @member {String} Note
 */
LandlordChaseNoteModel.prototype['Note'] = undefined;

/**
 * Note Type
 * @member {String} NoteType
 */
LandlordChaseNoteModel.prototype['NoteType'] = undefined;

/**
 * Tenant
 * @member {String} TenantID
 */
LandlordChaseNoteModel.prototype['TenantID'] = undefined;






export default LandlordChaseNoteModel;

