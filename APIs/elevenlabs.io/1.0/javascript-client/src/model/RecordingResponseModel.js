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
 * The RecordingResponseModel model module.
 * @module model/RecordingResponseModel
 * @version 1.0
 */
class RecordingResponseModel {
    /**
     * Constructs a new <code>RecordingResponseModel</code>.
     * @alias module:model/RecordingResponseModel
     * @param mimeType {String} 
     * @param recordingId {String} 
     * @param sizeBytes {Number} 
     * @param transcription {String} 
     * @param uploadDateUnix {Number} 
     */
    constructor(mimeType, recordingId, sizeBytes, transcription, uploadDateUnix) { 
        
        RecordingResponseModel.initialize(this, mimeType, recordingId, sizeBytes, transcription, uploadDateUnix);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, mimeType, recordingId, sizeBytes, transcription, uploadDateUnix) { 
        obj['mime_type'] = mimeType;
        obj['recording_id'] = recordingId;
        obj['size_bytes'] = sizeBytes;
        obj['transcription'] = transcription;
        obj['upload_date_unix'] = uploadDateUnix;
    }

    /**
     * Constructs a <code>RecordingResponseModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RecordingResponseModel} obj Optional instance to populate.
     * @return {module:model/RecordingResponseModel} The populated <code>RecordingResponseModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RecordingResponseModel();

            if (data.hasOwnProperty('mime_type')) {
                obj['mime_type'] = ApiClient.convertToType(data['mime_type'], 'String');
            }
            if (data.hasOwnProperty('recording_id')) {
                obj['recording_id'] = ApiClient.convertToType(data['recording_id'], 'String');
            }
            if (data.hasOwnProperty('size_bytes')) {
                obj['size_bytes'] = ApiClient.convertToType(data['size_bytes'], 'Number');
            }
            if (data.hasOwnProperty('transcription')) {
                obj['transcription'] = ApiClient.convertToType(data['transcription'], 'String');
            }
            if (data.hasOwnProperty('upload_date_unix')) {
                obj['upload_date_unix'] = ApiClient.convertToType(data['upload_date_unix'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RecordingResponseModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RecordingResponseModel</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RecordingResponseModel.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['mime_type'] && !(typeof data['mime_type'] === 'string' || data['mime_type'] instanceof String)) {
            throw new Error("Expected the field `mime_type` to be a primitive type in the JSON string but got " + data['mime_type']);
        }
        // ensure the json data is a string
        if (data['recording_id'] && !(typeof data['recording_id'] === 'string' || data['recording_id'] instanceof String)) {
            throw new Error("Expected the field `recording_id` to be a primitive type in the JSON string but got " + data['recording_id']);
        }
        // ensure the json data is a string
        if (data['transcription'] && !(typeof data['transcription'] === 'string' || data['transcription'] instanceof String)) {
            throw new Error("Expected the field `transcription` to be a primitive type in the JSON string but got " + data['transcription']);
        }

        return true;
    }


}

RecordingResponseModel.RequiredProperties = ["mime_type", "recording_id", "size_bytes", "transcription", "upload_date_unix"];

/**
 * @member {String} mime_type
 */
RecordingResponseModel.prototype['mime_type'] = undefined;

/**
 * @member {String} recording_id
 */
RecordingResponseModel.prototype['recording_id'] = undefined;

/**
 * @member {Number} size_bytes
 */
RecordingResponseModel.prototype['size_bytes'] = undefined;

/**
 * @member {String} transcription
 */
RecordingResponseModel.prototype['transcription'] = undefined;

/**
 * @member {Number} upload_date_unix
 */
RecordingResponseModel.prototype['upload_date_unix'] = undefined;






export default RecordingResponseModel;

