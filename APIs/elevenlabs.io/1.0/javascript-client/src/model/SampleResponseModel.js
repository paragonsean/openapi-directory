/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
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

/**
 * The SampleResponseModel model module.
 * @module model/SampleResponseModel
 * @version 1.0
 */
class SampleResponseModel {
    /**
     * Constructs a new <code>SampleResponseModel</code>.
     * @alias module:model/SampleResponseModel
     * @param fileName {String} 
     * @param hash {String} 
     * @param mimeType {String} 
     * @param sampleId {String} 
     * @param sizeBytes {Number} 
     */
    constructor(fileName, hash, mimeType, sampleId, sizeBytes) { 
        
        SampleResponseModel.initialize(this, fileName, hash, mimeType, sampleId, sizeBytes);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, fileName, hash, mimeType, sampleId, sizeBytes) { 
        obj['file_name'] = fileName;
        obj['hash'] = hash;
        obj['mime_type'] = mimeType;
        obj['sample_id'] = sampleId;
        obj['size_bytes'] = sizeBytes;
    }

    /**
     * Constructs a <code>SampleResponseModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SampleResponseModel} obj Optional instance to populate.
     * @return {module:model/SampleResponseModel} The populated <code>SampleResponseModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SampleResponseModel();

            if (data.hasOwnProperty('file_name')) {
                obj['file_name'] = ApiClient.convertToType(data['file_name'], 'String');
            }
            if (data.hasOwnProperty('hash')) {
                obj['hash'] = ApiClient.convertToType(data['hash'], 'String');
            }
            if (data.hasOwnProperty('mime_type')) {
                obj['mime_type'] = ApiClient.convertToType(data['mime_type'], 'String');
            }
            if (data.hasOwnProperty('sample_id')) {
                obj['sample_id'] = ApiClient.convertToType(data['sample_id'], 'String');
            }
            if (data.hasOwnProperty('size_bytes')) {
                obj['size_bytes'] = ApiClient.convertToType(data['size_bytes'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SampleResponseModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SampleResponseModel</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SampleResponseModel.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['file_name'] && !(typeof data['file_name'] === 'string' || data['file_name'] instanceof String)) {
            throw new Error("Expected the field `file_name` to be a primitive type in the JSON string but got " + data['file_name']);
        }
        // ensure the json data is a string
        if (data['hash'] && !(typeof data['hash'] === 'string' || data['hash'] instanceof String)) {
            throw new Error("Expected the field `hash` to be a primitive type in the JSON string but got " + data['hash']);
        }
        // ensure the json data is a string
        if (data['mime_type'] && !(typeof data['mime_type'] === 'string' || data['mime_type'] instanceof String)) {
            throw new Error("Expected the field `mime_type` to be a primitive type in the JSON string but got " + data['mime_type']);
        }
        // ensure the json data is a string
        if (data['sample_id'] && !(typeof data['sample_id'] === 'string' || data['sample_id'] instanceof String)) {
            throw new Error("Expected the field `sample_id` to be a primitive type in the JSON string but got " + data['sample_id']);
        }

        return true;
    }


}

SampleResponseModel.RequiredProperties = ["file_name", "hash", "mime_type", "sample_id", "size_bytes"];

/**
 * @member {String} file_name
 */
SampleResponseModel.prototype['file_name'] = undefined;

/**
 * @member {String} hash
 */
SampleResponseModel.prototype['hash'] = undefined;

/**
 * @member {String} mime_type
 */
SampleResponseModel.prototype['mime_type'] = undefined;

/**
 * @member {String} sample_id
 */
SampleResponseModel.prototype['sample_id'] = undefined;

/**
 * @member {Number} size_bytes
 */
SampleResponseModel.prototype['size_bytes'] = undefined;






export default SampleResponseModel;

