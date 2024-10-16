/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TagVO from './TagVO';

/**
 * The FileVO model module.
 * @module model/FileVO
 * @version 1.0
 */
class FileVO {
    /**
     * Constructs a new <code>FileVO</code>.
     * Java type: com.noosh.nooshapi.vo.file.FileVO
     * @alias module:model/FileVO
     */
    constructor() { 
        
        FileVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FileVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FileVO} obj Optional instance to populate.
     * @return {module:model/FileVO} The populated <code>FileVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FileVO();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('download_link')) {
                obj['download_link'] = ApiClient.convertToType(data['download_link'], 'String');
            }
            if (data.hasOwnProperty('file_id')) {
                obj['file_id'] = ApiClient.convertToType(data['file_id'], 'Number');
            }
            if (data.hasOwnProperty('file_name')) {
                obj['file_name'] = ApiClient.convertToType(data['file_name'], 'String');
            }
            if (data.hasOwnProperty('file_size')) {
                obj['file_size'] = ApiClient.convertToType(data['file_size'], Object);
            }
            if (data.hasOwnProperty('file_type')) {
                obj['file_type'] = ApiClient.convertToType(data['file_type'], 'String');
            }
            if (data.hasOwnProperty('is_remote')) {
                obj['is_remote'] = ApiClient.convertToType(data['is_remote'], 'Boolean');
            }
            if (data.hasOwnProperty('modified_date')) {
                obj['modified_date'] = ApiClient.convertToType(data['modified_date'], 'String');
            }
            if (data.hasOwnProperty('tagList')) {
                obj['tagList'] = ApiClient.convertToType(data['tagList'], [TagVO]);
            }
            if (data.hasOwnProperty('upload_date')) {
                obj['upload_date'] = ApiClient.convertToType(data['upload_date'], 'String');
            }
            if (data.hasOwnProperty('uploaded_by')) {
                obj['uploaded_by'] = ApiClient.convertToType(data['uploaded_by'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FileVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FileVO</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['download_link'] && !(typeof data['download_link'] === 'string' || data['download_link'] instanceof String)) {
            throw new Error("Expected the field `download_link` to be a primitive type in the JSON string but got " + data['download_link']);
        }
        // ensure the json data is a string
        if (data['file_name'] && !(typeof data['file_name'] === 'string' || data['file_name'] instanceof String)) {
            throw new Error("Expected the field `file_name` to be a primitive type in the JSON string but got " + data['file_name']);
        }
        // ensure the json data is a string
        if (data['file_type'] && !(typeof data['file_type'] === 'string' || data['file_type'] instanceof String)) {
            throw new Error("Expected the field `file_type` to be a primitive type in the JSON string but got " + data['file_type']);
        }
        // ensure the json data is a string
        if (data['modified_date'] && !(typeof data['modified_date'] === 'string' || data['modified_date'] instanceof String)) {
            throw new Error("Expected the field `modified_date` to be a primitive type in the JSON string but got " + data['modified_date']);
        }
        if (data['tagList']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tagList'])) {
                throw new Error("Expected the field `tagList` to be an array in the JSON data but got " + data['tagList']);
            }
            // validate the optional field `tagList` (array)
            for (const item of data['tagList']) {
                TagVO.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['upload_date'] && !(typeof data['upload_date'] === 'string' || data['upload_date'] instanceof String)) {
            throw new Error("Expected the field `upload_date` to be a primitive type in the JSON string but got " + data['upload_date']);
        }
        // ensure the json data is a string
        if (data['uploaded_by'] && !(typeof data['uploaded_by'] === 'string' || data['uploaded_by'] instanceof String)) {
            throw new Error("Expected the field `uploaded_by` to be a primitive type in the JSON string but got " + data['uploaded_by']);
        }

        return true;
    }


}



/**
 * 
 * @member {String} description
 */
FileVO.prototype['description'] = undefined;

/**
 * 
 * @member {String} download_link
 */
FileVO.prototype['download_link'] = undefined;

/**
 * 
 * @member {Number} file_id
 */
FileVO.prototype['file_id'] = undefined;

/**
 * 
 * @member {String} file_name
 */
FileVO.prototype['file_name'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} file_size
 */
FileVO.prototype['file_size'] = undefined;

/**
 * 
 * @member {String} file_type
 */
FileVO.prototype['file_type'] = undefined;

/**
 * 
 * @member {Boolean} is_remote
 */
FileVO.prototype['is_remote'] = undefined;

/**
 * 
 * @member {String} modified_date
 */
FileVO.prototype['modified_date'] = undefined;

/**
 * 
 * @member {Array.<module:model/TagVO>} tagList
 */
FileVO.prototype['tagList'] = undefined;

/**
 * 
 * @member {String} upload_date
 */
FileVO.prototype['upload_date'] = undefined;

/**
 * 
 * @member {String} uploaded_by
 */
FileVO.prototype['uploaded_by'] = undefined;






export default FileVO;

