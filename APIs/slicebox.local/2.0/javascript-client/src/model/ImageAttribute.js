/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ImageAttribute model module.
 * @module model/ImageAttribute
 * @version 2.0
 */
class ImageAttribute {
    /**
     * Constructs a new <code>ImageAttribute</code>.
     * @alias module:model/ImageAttribute
     */
    constructor() { 
        
        ImageAttribute.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageAttribute</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageAttribute} obj Optional instance to populate.
     * @return {module:model/ImageAttribute} The populated <code>ImageAttribute</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageAttribute();

            if (data.hasOwnProperty('depth')) {
                obj['depth'] = ApiClient.convertToType(data['depth'], 'Number');
            }
            if (data.hasOwnProperty('element')) {
                obj['element'] = ApiClient.convertToType(data['element'], 'String');
            }
            if (data.hasOwnProperty('group')) {
                obj['group'] = ApiClient.convertToType(data['group'], 'String');
            }
            if (data.hasOwnProperty('length')) {
                obj['length'] = ApiClient.convertToType(data['length'], 'Number');
            }
            if (data.hasOwnProperty('multiplicity')) {
                obj['multiplicity'] = ApiClient.convertToType(data['multiplicity'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
            if (data.hasOwnProperty('vr')) {
                obj['vr'] = ApiClient.convertToType(data['vr'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageAttribute</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageAttribute</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['element'] && !(typeof data['element'] === 'string' || data['element'] instanceof String)) {
            throw new Error("Expected the field `element` to be a primitive type in the JSON string but got " + data['element']);
        }
        // ensure the json data is a string
        if (data['group'] && !(typeof data['group'] === 'string' || data['group'] instanceof String)) {
            throw new Error("Expected the field `group` to be a primitive type in the JSON string but got " + data['group']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }
        // ensure the json data is a string
        if (data['vr'] && !(typeof data['vr'] === 'string' || data['vr'] instanceof String)) {
            throw new Error("Expected the field `vr` to be a primitive type in the JSON string but got " + data['vr']);
        }

        return true;
    }


}



/**
 * @member {Number} depth
 */
ImageAttribute.prototype['depth'] = undefined;

/**
 * @member {String} element
 */
ImageAttribute.prototype['element'] = undefined;

/**
 * @member {String} group
 */
ImageAttribute.prototype['group'] = undefined;

/**
 * @member {Number} length
 */
ImageAttribute.prototype['length'] = undefined;

/**
 * @member {Number} multiplicity
 */
ImageAttribute.prototype['multiplicity'] = undefined;

/**
 * @member {String} name
 */
ImageAttribute.prototype['name'] = undefined;

/**
 * @member {String} path
 */
ImageAttribute.prototype['path'] = undefined;

/**
 * @member {String} value
 */
ImageAttribute.prototype['value'] = undefined;

/**
 * @member {String} vr
 */
ImageAttribute.prototype['vr'] = undefined;






export default ImageAttribute;

