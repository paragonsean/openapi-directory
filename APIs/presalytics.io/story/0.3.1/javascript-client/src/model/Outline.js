/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Outline model module.
 * @module model/Outline
 * @version 0.3.1
 */
class Outline {
    /**
     * Constructs a new <code>Outline</code>.
     * story_outline (json object)
     * @alias module:model/Outline
     */
    constructor() { 
        
        Outline.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Outline</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Outline} obj Optional instance to populate.
     * @return {module:model/Outline} The populated <code>Outline</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Outline();

            if (data.hasOwnProperty('outline')) {
                obj['outline'] = ApiClient.convertToType(data['outline'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Outline</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Outline</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['outline'] && !(typeof data['outline'] === 'string' || data['outline'] instanceof String)) {
            throw new Error("Expected the field `outline` to be a primitive type in the JSON string but got " + data['outline']);
        }

        return true;
    }


}



/**
 * @member {String} outline
 */
Outline.prototype['outline'] = undefined;






export default Outline;

