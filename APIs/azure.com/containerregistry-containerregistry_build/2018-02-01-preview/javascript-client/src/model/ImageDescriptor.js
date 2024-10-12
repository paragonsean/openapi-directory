/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ImageDescriptor model module.
 * @module model/ImageDescriptor
 * @version 2018-02-01-preview
 */
class ImageDescriptor {
    /**
     * Constructs a new <code>ImageDescriptor</code>.
     * Properties for a registry image.
     * @alias module:model/ImageDescriptor
     */
    constructor() { 
        
        ImageDescriptor.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageDescriptor</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageDescriptor} obj Optional instance to populate.
     * @return {module:model/ImageDescriptor} The populated <code>ImageDescriptor</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageDescriptor();

            if (data.hasOwnProperty('digest')) {
                obj['digest'] = ApiClient.convertToType(data['digest'], 'String');
            }
            if (data.hasOwnProperty('registry')) {
                obj['registry'] = ApiClient.convertToType(data['registry'], 'String');
            }
            if (data.hasOwnProperty('repository')) {
                obj['repository'] = ApiClient.convertToType(data['repository'], 'String');
            }
            if (data.hasOwnProperty('tag')) {
                obj['tag'] = ApiClient.convertToType(data['tag'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageDescriptor</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageDescriptor</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['digest'] && !(typeof data['digest'] === 'string' || data['digest'] instanceof String)) {
            throw new Error("Expected the field `digest` to be a primitive type in the JSON string but got " + data['digest']);
        }
        // ensure the json data is a string
        if (data['registry'] && !(typeof data['registry'] === 'string' || data['registry'] instanceof String)) {
            throw new Error("Expected the field `registry` to be a primitive type in the JSON string but got " + data['registry']);
        }
        // ensure the json data is a string
        if (data['repository'] && !(typeof data['repository'] === 'string' || data['repository'] instanceof String)) {
            throw new Error("Expected the field `repository` to be a primitive type in the JSON string but got " + data['repository']);
        }
        // ensure the json data is a string
        if (data['tag'] && !(typeof data['tag'] === 'string' || data['tag'] instanceof String)) {
            throw new Error("Expected the field `tag` to be a primitive type in the JSON string but got " + data['tag']);
        }

        return true;
    }


}



/**
 * The sha256-based digest of the image manifest.
 * @member {String} digest
 */
ImageDescriptor.prototype['digest'] = undefined;

/**
 * The registry login server.
 * @member {String} registry
 */
ImageDescriptor.prototype['registry'] = undefined;

/**
 * The repository name.
 * @member {String} repository
 */
ImageDescriptor.prototype['repository'] = undefined;

/**
 * The tag name.
 * @member {String} tag
 */
ImageDescriptor.prototype['tag'] = undefined;






export default ImageDescriptor;

