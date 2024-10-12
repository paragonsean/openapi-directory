/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TableBorders model module.
 * @module model/TableBorders
 * @version 0.1.0
 */
class TableBorders {
    /**
     * Constructs a new <code>TableBorders</code>.
     * @alias module:model/TableBorders
     */
    constructor() { 
        
        TableBorders.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TableBorders</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TableBorders} obj Optional instance to populate.
     * @return {module:model/TableBorders} The populated <code>TableBorders</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TableBorders();

            if (data.hasOwnProperty('cellId')) {
                obj['cellId'] = ApiClient.convertToType(data['cellId'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TableBorders</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TableBorders</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['cellId'] && !(typeof data['cellId'] === 'string' || data['cellId'] instanceof String)) {
            throw new Error("Expected the field `cellId` to be a primitive type in the JSON string but got " + data['cellId']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * @member {String} cellId
 */
TableBorders.prototype['cellId'] = undefined;

/**
 * @member {String} id
 */
TableBorders.prototype['id'] = undefined;






export default TableBorders;

