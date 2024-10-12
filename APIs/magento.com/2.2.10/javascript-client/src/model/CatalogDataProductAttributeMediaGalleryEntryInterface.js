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
import CatalogDataProductAttributeMediaGalleryEntryExtensionInterface from './CatalogDataProductAttributeMediaGalleryEntryExtensionInterface';
import FrameworkDataImageContentInterface from './FrameworkDataImageContentInterface';

/**
 * The CatalogDataProductAttributeMediaGalleryEntryInterface model module.
 * @module model/CatalogDataProductAttributeMediaGalleryEntryInterface
 * @version 2.2.10
 */
class CatalogDataProductAttributeMediaGalleryEntryInterface {
    /**
     * Constructs a new <code>CatalogDataProductAttributeMediaGalleryEntryInterface</code>.
     * 
     * @alias module:model/CatalogDataProductAttributeMediaGalleryEntryInterface
     * @param disabled {Boolean} If gallery entry is hidden from product page
     * @param label {String} Gallery entry alternative text
     * @param mediaType {String} Media type
     * @param position {Number} Gallery entry position (sort order)
     * @param types {Array.<String>} Gallery entry image types (thumbnail, image, small_image etc)
     */
    constructor(disabled, label, mediaType, position, types) { 
        
        CatalogDataProductAttributeMediaGalleryEntryInterface.initialize(this, disabled, label, mediaType, position, types);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, disabled, label, mediaType, position, types) { 
        obj['disabled'] = disabled;
        obj['label'] = label;
        obj['media_type'] = mediaType;
        obj['position'] = position;
        obj['types'] = types;
    }

    /**
     * Constructs a <code>CatalogDataProductAttributeMediaGalleryEntryInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogDataProductAttributeMediaGalleryEntryInterface} obj Optional instance to populate.
     * @return {module:model/CatalogDataProductAttributeMediaGalleryEntryInterface} The populated <code>CatalogDataProductAttributeMediaGalleryEntryInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogDataProductAttributeMediaGalleryEntryInterface();

            if (data.hasOwnProperty('content')) {
                obj['content'] = FrameworkDataImageContentInterface.constructFromObject(data['content']);
            }
            if (data.hasOwnProperty('disabled')) {
                obj['disabled'] = ApiClient.convertToType(data['disabled'], 'Boolean');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = CatalogDataProductAttributeMediaGalleryEntryExtensionInterface.constructFromObject(data['extension_attributes']);
            }
            if (data.hasOwnProperty('file')) {
                obj['file'] = ApiClient.convertToType(data['file'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
            if (data.hasOwnProperty('media_type')) {
                obj['media_type'] = ApiClient.convertToType(data['media_type'], 'String');
            }
            if (data.hasOwnProperty('position')) {
                obj['position'] = ApiClient.convertToType(data['position'], 'Number');
            }
            if (data.hasOwnProperty('types')) {
                obj['types'] = ApiClient.convertToType(data['types'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogDataProductAttributeMediaGalleryEntryInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogDataProductAttributeMediaGalleryEntryInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CatalogDataProductAttributeMediaGalleryEntryInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `content`
        if (data['content']) { // data not null
          FrameworkDataImageContentInterface.validateJSON(data['content']);
        }
        // validate the optional field `extension_attributes`
        if (data['extension_attributes']) { // data not null
          CatalogDataProductAttributeMediaGalleryEntryExtensionInterface.validateJSON(data['extension_attributes']);
        }
        // ensure the json data is a string
        if (data['file'] && !(typeof data['file'] === 'string' || data['file'] instanceof String)) {
            throw new Error("Expected the field `file` to be a primitive type in the JSON string but got " + data['file']);
        }
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }
        // ensure the json data is a string
        if (data['media_type'] && !(typeof data['media_type'] === 'string' || data['media_type'] instanceof String)) {
            throw new Error("Expected the field `media_type` to be a primitive type in the JSON string but got " + data['media_type']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['types'])) {
            throw new Error("Expected the field `types` to be an array in the JSON data but got " + data['types']);
        }

        return true;
    }


}

CatalogDataProductAttributeMediaGalleryEntryInterface.RequiredProperties = ["disabled", "label", "media_type", "position", "types"];

/**
 * @member {module:model/FrameworkDataImageContentInterface} content
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['content'] = undefined;

/**
 * If gallery entry is hidden from product page
 * @member {Boolean} disabled
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['disabled'] = undefined;

/**
 * @member {module:model/CatalogDataProductAttributeMediaGalleryEntryExtensionInterface} extension_attributes
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['extension_attributes'] = undefined;

/**
 * File path
 * @member {String} file
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['file'] = undefined;

/**
 * Gallery entry ID
 * @member {Number} id
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['id'] = undefined;

/**
 * Gallery entry alternative text
 * @member {String} label
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['label'] = undefined;

/**
 * Media type
 * @member {String} media_type
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['media_type'] = undefined;

/**
 * Gallery entry position (sort order)
 * @member {Number} position
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['position'] = undefined;

/**
 * Gallery entry image types (thumbnail, image, small_image etc)
 * @member {Array.<String>} types
 */
CatalogDataProductAttributeMediaGalleryEntryInterface.prototype['types'] = undefined;






export default CatalogDataProductAttributeMediaGalleryEntryInterface;

