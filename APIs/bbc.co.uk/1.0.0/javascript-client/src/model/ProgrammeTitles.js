/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ProgrammeTitles model module.
 * @module model/ProgrammeTitles
 * @version 1.0.0
 */
class ProgrammeTitles {
    /**
     * Constructs a new <code>ProgrammeTitles</code>.
     * @alias module:model/ProgrammeTitles
     * @param type {String} 
     */
    constructor(type) { 
        
        ProgrammeTitles.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
        obj['type'] = type;
    }

    /**
     * Constructs a <code>ProgrammeTitles</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProgrammeTitles} obj Optional instance to populate.
     * @return {module:model/ProgrammeTitles} The populated <code>ProgrammeTitles</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProgrammeTitles();

            if (data.hasOwnProperty('display_title')) {
                obj['display_title'] = ApiClient.convertToType(data['display_title'], 'String');
            }
            if (data.hasOwnProperty('entity_title')) {
                obj['entity_title'] = ApiClient.convertToType(data['entity_title'], 'String');
            }
            if (data.hasOwnProperty('primary_title')) {
                obj['primary_title'] = ApiClient.convertToType(data['primary_title'], 'String');
            }
            if (data.hasOwnProperty('secondary_title')) {
                obj['secondary_title'] = ApiClient.convertToType(data['secondary_title'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProgrammeTitles</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProgrammeTitles</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ProgrammeTitles.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['display_title'] && !(typeof data['display_title'] === 'string' || data['display_title'] instanceof String)) {
            throw new Error("Expected the field `display_title` to be a primitive type in the JSON string but got " + data['display_title']);
        }
        // ensure the json data is a string
        if (data['entity_title'] && !(typeof data['entity_title'] === 'string' || data['entity_title'] instanceof String)) {
            throw new Error("Expected the field `entity_title` to be a primitive type in the JSON string but got " + data['entity_title']);
        }
        // ensure the json data is a string
        if (data['primary_title'] && !(typeof data['primary_title'] === 'string' || data['primary_title'] instanceof String)) {
            throw new Error("Expected the field `primary_title` to be a primitive type in the JSON string but got " + data['primary_title']);
        }
        // ensure the json data is a string
        if (data['secondary_title'] && !(typeof data['secondary_title'] === 'string' || data['secondary_title'] instanceof String)) {
            throw new Error("Expected the field `secondary_title` to be a primitive type in the JSON string but got " + data['secondary_title']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

ProgrammeTitles.RequiredProperties = ["type"];

/**
 * @member {String} display_title
 */
ProgrammeTitles.prototype['display_title'] = undefined;

/**
 * @member {String} entity_title
 */
ProgrammeTitles.prototype['entity_title'] = undefined;

/**
 * @member {String} primary_title
 */
ProgrammeTitles.prototype['primary_title'] = undefined;

/**
 * @member {String} secondary_title
 */
ProgrammeTitles.prototype['secondary_title'] = undefined;

/**
 * @member {String} type
 */
ProgrammeTitles.prototype['type'] = undefined;






export default ProgrammeTitles;

