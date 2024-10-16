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
 * The BuildSystemSharedDTOParameterMapping model module.
 * @module model/BuildSystemSharedDTOParameterMapping
 * @version v1
 */
class BuildSystemSharedDTOParameterMapping {
    /**
     * Constructs a new <code>BuildSystemSharedDTOParameterMapping</code>.
     * A DTO for an IParameterMapping
     * @alias module:model/BuildSystemSharedDTOParameterMapping
     */
    constructor() { 
        
        BuildSystemSharedDTOParameterMapping.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BuildSystemSharedDTOParameterMapping</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BuildSystemSharedDTOParameterMapping} obj Optional instance to populate.
     * @return {module:model/BuildSystemSharedDTOParameterMapping} The populated <code>BuildSystemSharedDTOParameterMapping</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BuildSystemSharedDTOParameterMapping();

            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Source')) {
                obj['Source'] = ApiClient.convertToType(data['Source'], 'String');
            }
            if (data.hasOwnProperty('SourceType')) {
                obj['SourceType'] = ApiClient.convertToType(data['SourceType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BuildSystemSharedDTOParameterMapping</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BuildSystemSharedDTOParameterMapping</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Source'] && !(typeof data['Source'] === 'string' || data['Source'] instanceof String)) {
            throw new Error("Expected the field `Source` to be a primitive type in the JSON string but got " + data['Source']);
        }
        // ensure the json data is a string
        if (data['SourceType'] && !(typeof data['SourceType'] === 'string' || data['SourceType'] instanceof String)) {
            throw new Error("Expected the field `SourceType` to be a primitive type in the JSON string but got " + data['SourceType']);
        }

        return true;
    }


}



/**
 * The name of the parameter this mapping applies to
 * @member {String} Name
 */
BuildSystemSharedDTOParameterMapping.prototype['Name'] = undefined;

/**
 * The source of the value.  The meaning of this value is determined by the source type.  When the source type is “Constant” then source is the value formatted as a string.  When the source type is “Variable” then the source is the name of the variable
 * @member {String} Source
 */
BuildSystemSharedDTOParameterMapping.prototype['Source'] = undefined;

/**
 * The source type used for supplying the parameter
 * @member {module:model/BuildSystemSharedDTOParameterMapping.SourceTypeEnum} SourceType
 */
BuildSystemSharedDTOParameterMapping.prototype['SourceType'] = undefined;





/**
 * Allowed values for the <code>SourceType</code> property.
 * @enum {String}
 * @readonly
 */
BuildSystemSharedDTOParameterMapping['SourceTypeEnum'] = {

    /**
     * value: "Constant"
     * @const
     */
    "Constant": "Constant",

    /**
     * value: "Variable"
     * @const
     */
    "Variable": "Variable"
};



export default BuildSystemSharedDTOParameterMapping;

