/**
 * PdfBroker.io API
 * PdfBroker.io is an api for creating pdf files from Xsl-Fo or Html and other useful pdf utilities.
 *
 * The version of the OpenAPI document: v1
 * Contact: support@pdfbroker.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FontStyle from './FontStyle';

/**
 * The FontDto model module.
 * @module model/FontDto
 * @version v1
 */
class FontDto {
    /**
     * Constructs a new <code>FontDto</code>.
     * The Font dto object
     * @alias module:model/FontDto
     */
    constructor() { 
        
        FontDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FontDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FontDto} obj Optional instance to populate.
     * @return {module:model/FontDto} The populated <code>FontDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FontDto();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'Number');
            }
            if (data.hasOwnProperty('style')) {
                obj['style'] = FontStyle.constructFromObject(data['style']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FontDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FontDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * Gets the name of the font
 * @member {String} name
 */
FontDto.prototype['name'] = undefined;

/**
 * Gets the size of the font
 * @member {Number} size
 */
FontDto.prototype['size'] = undefined;

/**
 * @member {module:model/FontStyle} style
 */
FontDto.prototype['style'] = undefined;






export default FontDto;

