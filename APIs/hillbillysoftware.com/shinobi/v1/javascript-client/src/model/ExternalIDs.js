/**
 * shinobiapi
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
 * The ExternalIDs model module.
 * @module model/ExternalIDs
 * @version v1
 */
class ExternalIDs {
    /**
     * Constructs a new <code>ExternalIDs</code>.
     * @alias module:model/ExternalIDs
     */
    constructor() { 
        
        ExternalIDs.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ExternalIDs</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExternalIDs} obj Optional instance to populate.
     * @return {module:model/ExternalIDs} The populated <code>ExternalIDs</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExternalIDs();

            if (data.hasOwnProperty('ID')) {
                obj['ID'] = ApiClient.convertToType(data['ID'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExternalIDs</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExternalIDs</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ID'] && !(typeof data['ID'] === 'string' || data['ID'] instanceof String)) {
            throw new Error("Expected the field `ID` to be a primitive type in the JSON string but got " + data['ID']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }

        return true;
    }


}



/**
 * @member {String} ID
 */
ExternalIDs.prototype['ID'] = undefined;

/**
 * @member {String} Name
 */
ExternalIDs.prototype['Name'] = undefined;






export default ExternalIDs;

