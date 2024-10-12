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
 * The PhotoEditability model module.
 * @module model/PhotoEditability
 * @version 1.0.0
 */
class PhotoEditability {
    /**
     * Constructs a new <code>PhotoEditability</code>.
     * @alias module:model/PhotoEditability
     */
    constructor() { 
        
        PhotoEditability.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PhotoEditability</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PhotoEditability} obj Optional instance to populate.
     * @return {module:model/PhotoEditability} The populated <code>PhotoEditability</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PhotoEditability();

            if (data.hasOwnProperty('canaddmeta')) {
                obj['canaddmeta'] = ApiClient.convertToType(data['canaddmeta'], 'Boolean');
            }
            if (data.hasOwnProperty('cancomment')) {
                obj['cancomment'] = ApiClient.convertToType(data['cancomment'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PhotoEditability</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PhotoEditability</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Boolean} canaddmeta
 */
PhotoEditability.prototype['canaddmeta'] = undefined;

/**
 * @member {Boolean} cancomment
 */
PhotoEditability.prototype['cancomment'] = undefined;






export default PhotoEditability;

