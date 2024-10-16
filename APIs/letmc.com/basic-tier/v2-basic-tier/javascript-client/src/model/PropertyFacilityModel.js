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
 * The PropertyFacilityModel model module.
 * @module model/PropertyFacilityModel
 * @version v2-basic-tier
 */
class PropertyFacilityModel {
    /**
     * Constructs a new <code>PropertyFacilityModel</code>.
     * Stores the information about a single property facility.
     * @alias module:model/PropertyFacilityModel
     */
    constructor() { 
        
        PropertyFacilityModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PropertyFacilityModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PropertyFacilityModel} obj Optional instance to populate.
     * @return {module:model/PropertyFacilityModel} The populated <code>PropertyFacilityModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PropertyFacilityModel();

            if (data.hasOwnProperty('ETag')) {
                obj['ETag'] = ApiClient.convertToType(data['ETag'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('OID')) {
                obj['OID'] = ApiClient.convertToType(data['OID'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PropertyFacilityModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PropertyFacilityModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ETag'] && !(typeof data['ETag'] === 'string' || data['ETag'] instanceof String)) {
            throw new Error("Expected the field `ETag` to be a primitive type in the JSON string but got " + data['ETag']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['OID'] && !(typeof data['OID'] === 'string' || data['OID'] instanceof String)) {
            throw new Error("Expected the field `OID` to be a primitive type in the JSON string but got " + data['OID']);
        }

        return true;
    }


}



/**
 * A unique identifier defining the object and change revision.
 * @member {String} ETag
 */
PropertyFacilityModel.prototype['ETag'] = undefined;

/**
 * Display Name
 * @member {String} Name
 */
PropertyFacilityModel.prototype['Name'] = undefined;

/**
 * The unique Object ID (OID).
 * @member {String} OID
 */
PropertyFacilityModel.prototype['OID'] = undefined;






export default PropertyFacilityModel;

