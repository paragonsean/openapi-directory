/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FrameworkDataImageContentInterface model module.
 * @module model/FrameworkDataImageContentInterface
 * @version 2.2.10
 */
class FrameworkDataImageContentInterface {
    /**
     * Constructs a new <code>FrameworkDataImageContentInterface</code>.
     * Image Content data interface
     * @alias module:model/FrameworkDataImageContentInterface
     * @param base64EncodedData {String} Media data (base64 encoded content)
     * @param name {String} Image name
     * @param type {String} MIME type
     */
    constructor(base64EncodedData, name, type) { 
        
        FrameworkDataImageContentInterface.initialize(this, base64EncodedData, name, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, base64EncodedData, name, type) { 
        obj['base64_encoded_data'] = base64EncodedData;
        obj['name'] = name;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>FrameworkDataImageContentInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FrameworkDataImageContentInterface} obj Optional instance to populate.
     * @return {module:model/FrameworkDataImageContentInterface} The populated <code>FrameworkDataImageContentInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FrameworkDataImageContentInterface();

            if (data.hasOwnProperty('base64_encoded_data')) {
                obj['base64_encoded_data'] = ApiClient.convertToType(data['base64_encoded_data'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FrameworkDataImageContentInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FrameworkDataImageContentInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FrameworkDataImageContentInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['base64_encoded_data'] && !(typeof data['base64_encoded_data'] === 'string' || data['base64_encoded_data'] instanceof String)) {
            throw new Error("Expected the field `base64_encoded_data` to be a primitive type in the JSON string but got " + data['base64_encoded_data']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

FrameworkDataImageContentInterface.RequiredProperties = ["base64_encoded_data", "name", "type"];

/**
 * Media data (base64 encoded content)
 * @member {String} base64_encoded_data
 */
FrameworkDataImageContentInterface.prototype['base64_encoded_data'] = undefined;

/**
 * Image name
 * @member {String} name
 */
FrameworkDataImageContentInterface.prototype['name'] = undefined;

/**
 * MIME type
 * @member {String} type
 */
FrameworkDataImageContentInterface.prototype['type'] = undefined;






export default FrameworkDataImageContentInterface;

