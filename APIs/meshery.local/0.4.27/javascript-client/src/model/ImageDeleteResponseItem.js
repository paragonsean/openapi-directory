/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ImageDeleteResponseItem model module.
 * @module model/ImageDeleteResponseItem
 * @version 0.4.27
 */
class ImageDeleteResponseItem {
    /**
     * Constructs a new <code>ImageDeleteResponseItem</code>.
     * ImageDeleteResponseItem image delete response item
     * @alias module:model/ImageDeleteResponseItem
     */
    constructor() { 
        
        ImageDeleteResponseItem.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageDeleteResponseItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageDeleteResponseItem} obj Optional instance to populate.
     * @return {module:model/ImageDeleteResponseItem} The populated <code>ImageDeleteResponseItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageDeleteResponseItem();

            if (data.hasOwnProperty('Deleted')) {
                obj['Deleted'] = ApiClient.convertToType(data['Deleted'], 'String');
            }
            if (data.hasOwnProperty('Untagged')) {
                obj['Untagged'] = ApiClient.convertToType(data['Untagged'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageDeleteResponseItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageDeleteResponseItem</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Deleted'] && !(typeof data['Deleted'] === 'string' || data['Deleted'] instanceof String)) {
            throw new Error("Expected the field `Deleted` to be a primitive type in the JSON string but got " + data['Deleted']);
        }
        // ensure the json data is a string
        if (data['Untagged'] && !(typeof data['Untagged'] === 'string' || data['Untagged'] instanceof String)) {
            throw new Error("Expected the field `Untagged` to be a primitive type in the JSON string but got " + data['Untagged']);
        }

        return true;
    }


}



/**
 * The image ID of an image that was deleted
 * @member {String} Deleted
 */
ImageDeleteResponseItem.prototype['Deleted'] = undefined;

/**
 * The image ID of an image that was untagged
 * @member {String} Untagged
 */
ImageDeleteResponseItem.prototype['Untagged'] = undefined;






export default ImageDeleteResponseItem;

