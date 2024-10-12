/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Size model module.
 * @module model/Size
 * @version 1.0.0
 */
class Size {
    /**
     * Constructs a new <code>Size</code>.
     * @alias module:model/Size
     */
    constructor() { 
        
        Size.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Size</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Size} obj Optional instance to populate.
     * @return {module:model/Size} The populated <code>Size</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Size();

            if (data.hasOwnProperty('units')) {
                obj['units'] = ApiClient.convertToType(data['units'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Size</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Size</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['units'] && !(typeof data['units'] === 'string' || data['units'] instanceof String)) {
            throw new Error("Expected the field `units` to be a primitive type in the JSON string but got " + data['units']);
        }

        return true;
    }


}



/**
 * @member {String} units
 */
Size.prototype['units'] = undefined;






export default Size;

