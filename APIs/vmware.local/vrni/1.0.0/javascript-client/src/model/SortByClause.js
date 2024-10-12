/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
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
 * The SortByClause model module.
 * @module model/SortByClause
 * @version 1.0.0
 */
class SortByClause {
    /**
     * Constructs a new <code>SortByClause</code>.
     * @alias module:model/SortByClause
     */
    constructor() { 
        
        SortByClause.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SortByClause</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SortByClause} obj Optional instance to populate.
     * @return {module:model/SortByClause} The populated <code>SortByClause</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SortByClause();

            if (data.hasOwnProperty('field')) {
                obj['field'] = ApiClient.convertToType(data['field'], 'String');
            }
            if (data.hasOwnProperty('order')) {
                obj['order'] = ApiClient.convertToType(data['order'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SortByClause</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SortByClause</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['field'] && !(typeof data['field'] === 'string' || data['field'] instanceof String)) {
            throw new Error("Expected the field `field` to be a primitive type in the JSON string but got " + data['field']);
        }
        // ensure the json data is a string
        if (data['order'] && !(typeof data['order'] === 'string' || data['order'] instanceof String)) {
            throw new Error("Expected the field `order` to be a primitive type in the JSON string but got " + data['order']);
        }

        return true;
    }


}



/**
 * @member {String} field
 */
SortByClause.prototype['field'] = undefined;

/**
 * @member {module:model/SortByClause.OrderEnum} order
 */
SortByClause.prototype['order'] = undefined;





/**
 * Allowed values for the <code>order</code> property.
 * @enum {String}
 * @readonly
 */
SortByClause['OrderEnum'] = {

    /**
     * value: "ASC"
     * @const
     */
    "ASC": "ASC",

    /**
     * value: "DESC"
     * @const
     */
    "DESC": "DESC"
};



export default SortByClause;

