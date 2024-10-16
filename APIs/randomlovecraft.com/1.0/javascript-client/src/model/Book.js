/**
 * Random Lovecraft
 * Random sentences from the complete works of H.P. Lovecraft. CORS-enabled.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Book model module.
 * @module model/Book
 * @version 1.0
 */
class Book {
    /**
     * Constructs a new <code>Book</code>.
     * @alias module:model/Book
     */
    constructor() { 
        
        Book.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Book</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Book} obj Optional instance to populate.
     * @return {module:model/Book} The populated <code>Book</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Book();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('year')) {
                obj['year'] = ApiClient.convertToType(data['year'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Book</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Book</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['year'] && !(typeof data['year'] === 'string' || data['year'] instanceof String)) {
            throw new Error("Expected the field `year` to be a primitive type in the JSON string but got " + data['year']);
        }

        return true;
    }


}



/**
 * @member {String} id
 */
Book.prototype['id'] = undefined;

/**
 * @member {String} name
 */
Book.prototype['name'] = undefined;

/**
 * @member {String} year
 */
Book.prototype['year'] = undefined;






export default Book;

