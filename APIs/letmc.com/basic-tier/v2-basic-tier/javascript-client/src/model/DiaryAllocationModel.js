/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DiaryAllocationModel model module.
 * @module model/DiaryAllocationModel
 * @version v2-basic-tier
 */
class DiaryAllocationModel {
    /**
     * Constructs a new <code>DiaryAllocationModel</code>.
     * Represents a single diary allocation, capable of holding a number              of appointments associated with a member of staff.
     * @alias module:model/DiaryAllocationModel
     */
    constructor() { 
        
        DiaryAllocationModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DiaryAllocationModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DiaryAllocationModel} obj Optional instance to populate.
     * @return {module:model/DiaryAllocationModel} The populated <code>DiaryAllocationModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DiaryAllocationModel();

            if (data.hasOwnProperty('AppointmentType')) {
                obj['AppointmentType'] = ApiClient.convertToType(data['AppointmentType'], 'String');
            }
            if (data.hasOwnProperty('ETag')) {
                obj['ETag'] = ApiClient.convertToType(data['ETag'], 'String');
            }
            if (data.hasOwnProperty('End')) {
                obj['End'] = ApiClient.convertToType(data['End'], 'Date');
            }
            if (data.hasOwnProperty('OID')) {
                obj['OID'] = ApiClient.convertToType(data['OID'], 'String');
            }
            if (data.hasOwnProperty('Staff')) {
                obj['Staff'] = ApiClient.convertToType(data['Staff'], 'String');
            }
            if (data.hasOwnProperty('Start')) {
                obj['Start'] = ApiClient.convertToType(data['Start'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DiaryAllocationModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DiaryAllocationModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AppointmentType'] && !(typeof data['AppointmentType'] === 'string' || data['AppointmentType'] instanceof String)) {
            throw new Error("Expected the field `AppointmentType` to be a primitive type in the JSON string but got " + data['AppointmentType']);
        }
        // ensure the json data is a string
        if (data['ETag'] && !(typeof data['ETag'] === 'string' || data['ETag'] instanceof String)) {
            throw new Error("Expected the field `ETag` to be a primitive type in the JSON string but got " + data['ETag']);
        }
        // ensure the json data is a string
        if (data['OID'] && !(typeof data['OID'] === 'string' || data['OID'] instanceof String)) {
            throw new Error("Expected the field `OID` to be a primitive type in the JSON string but got " + data['OID']);
        }
        // ensure the json data is a string
        if (data['Staff'] && !(typeof data['Staff'] === 'string' || data['Staff'] instanceof String)) {
            throw new Error("Expected the field `Staff` to be a primitive type in the JSON string but got " + data['Staff']);
        }

        return true;
    }


}



/**
 * The diary appointment type.
 * @member {String} AppointmentType
 */
DiaryAllocationModel.prototype['AppointmentType'] = undefined;

/**
 * A unique identifier defining the object and change revision.
 * @member {String} ETag
 */
DiaryAllocationModel.prototype['ETag'] = undefined;

/**
 * The end date/time of this allocation.
 * @member {Date} End
 */
DiaryAllocationModel.prototype['End'] = undefined;

/**
 * The unique Object ID (OID).
 * @member {String} OID
 */
DiaryAllocationModel.prototype['OID'] = undefined;

/**
 * The staff member holding this allocation.
 * @member {String} Staff
 */
DiaryAllocationModel.prototype['Staff'] = undefined;

/**
 * The start date/time of this allocation.
 * @member {Date} Start
 */
DiaryAllocationModel.prototype['Start'] = undefined;






export default DiaryAllocationModel;

