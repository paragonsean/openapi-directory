/**
 * Face Client
 * An API for face detection, verification, and identification.
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
 * The VerifyFaceToPersonRequest model module.
 * @module model/VerifyFaceToPersonRequest
 * @version 1.0
 */
class VerifyFaceToPersonRequest {
    /**
     * Constructs a new <code>VerifyFaceToPersonRequest</code>.
     * Request body for face to person verification.
     * @alias module:model/VerifyFaceToPersonRequest
     * @param faceId {String} FaceId of the face, comes from Face - Detect
     * @param personId {String} Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create.
     */
    constructor(faceId, personId) { 
        
        VerifyFaceToPersonRequest.initialize(this, faceId, personId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, faceId, personId) { 
        obj['faceId'] = faceId;
        obj['personId'] = personId;
    }

    /**
     * Constructs a <code>VerifyFaceToPersonRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VerifyFaceToPersonRequest} obj Optional instance to populate.
     * @return {module:model/VerifyFaceToPersonRequest} The populated <code>VerifyFaceToPersonRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VerifyFaceToPersonRequest();

            if (data.hasOwnProperty('faceId')) {
                obj['faceId'] = ApiClient.convertToType(data['faceId'], 'String');
            }
            if (data.hasOwnProperty('largePersonGroupId')) {
                obj['largePersonGroupId'] = ApiClient.convertToType(data['largePersonGroupId'], 'String');
            }
            if (data.hasOwnProperty('personGroupId')) {
                obj['personGroupId'] = ApiClient.convertToType(data['personGroupId'], 'String');
            }
            if (data.hasOwnProperty('personId')) {
                obj['personId'] = ApiClient.convertToType(data['personId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VerifyFaceToPersonRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VerifyFaceToPersonRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of VerifyFaceToPersonRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['faceId'] && !(typeof data['faceId'] === 'string' || data['faceId'] instanceof String)) {
            throw new Error("Expected the field `faceId` to be a primitive type in the JSON string but got " + data['faceId']);
        }
        // ensure the json data is a string
        if (data['largePersonGroupId'] && !(typeof data['largePersonGroupId'] === 'string' || data['largePersonGroupId'] instanceof String)) {
            throw new Error("Expected the field `largePersonGroupId` to be a primitive type in the JSON string but got " + data['largePersonGroupId']);
        }
        // ensure the json data is a string
        if (data['personGroupId'] && !(typeof data['personGroupId'] === 'string' || data['personGroupId'] instanceof String)) {
            throw new Error("Expected the field `personGroupId` to be a primitive type in the JSON string but got " + data['personGroupId']);
        }
        // ensure the json data is a string
        if (data['personId'] && !(typeof data['personId'] === 'string' || data['personId'] instanceof String)) {
            throw new Error("Expected the field `personId` to be a primitive type in the JSON string but got " + data['personId']);
        }

        return true;
    }


}

VerifyFaceToPersonRequest.RequiredProperties = ["faceId", "personId"];

/**
 * FaceId of the face, comes from Face - Detect
 * @member {String} faceId
 */
VerifyFaceToPersonRequest.prototype['faceId'] = undefined;

/**
 * Using existing largePersonGroupId and personId for fast loading a specified person. largePersonGroupId is created in LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
 * @member {String} largePersonGroupId
 */
VerifyFaceToPersonRequest.prototype['largePersonGroupId'] = undefined;

/**
 * Using existing personGroupId and personId for fast loading a specified person. personGroupId is created in PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
 * @member {String} personGroupId
 */
VerifyFaceToPersonRequest.prototype['personGroupId'] = undefined;

/**
 * Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create.
 * @member {String} personId
 */
VerifyFaceToPersonRequest.prototype['personId'] = undefined;






export default VerifyFaceToPersonRequest;

