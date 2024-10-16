/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
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
 * The Tag model module.
 * @module model/Tag
 * @version 1.0.0
 */
class Tag {
    /**
     * Constructs a new <code>Tag</code>.
     * @alias module:model/Tag
     */
    constructor() { 
        
        Tag.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Tag</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Tag} obj Optional instance to populate.
     * @return {module:model/Tag} The populated <code>Tag</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Tag();

            if (data.hasOwnProperty('_content')) {
                obj['_content'] = ApiClient.convertToType(data['_content'], 'String');
            }
            if (data.hasOwnProperty('author')) {
                obj['author'] = ApiClient.convertToType(data['author'], 'String');
            }
            if (data.hasOwnProperty('authorname')) {
                obj['authorname'] = ApiClient.convertToType(data['authorname'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('machine_tag')) {
                obj['machine_tag'] = ApiClient.convertToType(data['machine_tag'], 'Boolean');
            }
            if (data.hasOwnProperty('raw')) {
                obj['raw'] = ApiClient.convertToType(data['raw'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Tag</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Tag</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['_content'] && !(typeof data['_content'] === 'string' || data['_content'] instanceof String)) {
            throw new Error("Expected the field `_content` to be a primitive type in the JSON string but got " + data['_content']);
        }
        // ensure the json data is a string
        if (data['author'] && !(typeof data['author'] === 'string' || data['author'] instanceof String)) {
            throw new Error("Expected the field `author` to be a primitive type in the JSON string but got " + data['author']);
        }
        // ensure the json data is a string
        if (data['authorname'] && !(typeof data['authorname'] === 'string' || data['authorname'] instanceof String)) {
            throw new Error("Expected the field `authorname` to be a primitive type in the JSON string but got " + data['authorname']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['raw'] && !(typeof data['raw'] === 'string' || data['raw'] instanceof String)) {
            throw new Error("Expected the field `raw` to be a primitive type in the JSON string but got " + data['raw']);
        }

        return true;
    }


}



/**
 * @member {String} _content
 */
Tag.prototype['_content'] = undefined;

/**
 * @member {String} author
 */
Tag.prototype['author'] = undefined;

/**
 * @member {String} authorname
 */
Tag.prototype['authorname'] = undefined;

/**
 * @member {String} id
 */
Tag.prototype['id'] = undefined;

/**
 * @member {Boolean} machine_tag
 */
Tag.prototype['machine_tag'] = undefined;

/**
 * @member {String} raw
 */
Tag.prototype['raw'] = undefined;






export default Tag;

