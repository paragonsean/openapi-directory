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
import FaceAttributes from './FaceAttributes';
import FaceLandmarks from './FaceLandmarks';
import FaceRectangle from './FaceRectangle';
import RecognitionModel from './RecognitionModel';

/**
 * The DetectedFace model module.
 * @module model/DetectedFace
 * @version 1.0
 */
class DetectedFace {
    /**
     * Constructs a new <code>DetectedFace</code>.
     * Detected Face object.
     * @alias module:model/DetectedFace
     * @param faceRectangle {module:model/FaceRectangle} 
     */
    constructor(faceRectangle) { 
        
        DetectedFace.initialize(this, faceRectangle);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, faceRectangle) { 
        obj['faceRectangle'] = faceRectangle;
    }

    /**
     * Constructs a <code>DetectedFace</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DetectedFace} obj Optional instance to populate.
     * @return {module:model/DetectedFace} The populated <code>DetectedFace</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DetectedFace();

            if (data.hasOwnProperty('faceAttributes')) {
                obj['faceAttributes'] = FaceAttributes.constructFromObject(data['faceAttributes']);
            }
            if (data.hasOwnProperty('faceId')) {
                obj['faceId'] = ApiClient.convertToType(data['faceId'], 'String');
            }
            if (data.hasOwnProperty('faceLandmarks')) {
                obj['faceLandmarks'] = FaceLandmarks.constructFromObject(data['faceLandmarks']);
            }
            if (data.hasOwnProperty('faceRectangle')) {
                obj['faceRectangle'] = FaceRectangle.constructFromObject(data['faceRectangle']);
            }
            if (data.hasOwnProperty('recognitionModel')) {
                obj['recognitionModel'] = RecognitionModel.constructFromObject(data['recognitionModel']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DetectedFace</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DetectedFace</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DetectedFace.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `faceAttributes`
        if (data['faceAttributes']) { // data not null
          FaceAttributes.validateJSON(data['faceAttributes']);
        }
        // ensure the json data is a string
        if (data['faceId'] && !(typeof data['faceId'] === 'string' || data['faceId'] instanceof String)) {
            throw new Error("Expected the field `faceId` to be a primitive type in the JSON string but got " + data['faceId']);
        }
        // validate the optional field `faceLandmarks`
        if (data['faceLandmarks']) { // data not null
          FaceLandmarks.validateJSON(data['faceLandmarks']);
        }
        // validate the optional field `faceRectangle`
        if (data['faceRectangle']) { // data not null
          FaceRectangle.validateJSON(data['faceRectangle']);
        }

        return true;
    }


}

DetectedFace.RequiredProperties = ["faceRectangle"];

/**
 * @member {module:model/FaceAttributes} faceAttributes
 */
DetectedFace.prototype['faceAttributes'] = undefined;

/**
 * @member {String} faceId
 */
DetectedFace.prototype['faceId'] = undefined;

/**
 * @member {module:model/FaceLandmarks} faceLandmarks
 */
DetectedFace.prototype['faceLandmarks'] = undefined;

/**
 * @member {module:model/FaceRectangle} faceRectangle
 */
DetectedFace.prototype['faceRectangle'] = undefined;

/**
 * @member {module:model/RecognitionModel} recognitionModel
 */
DetectedFace.prototype['recognitionModel'] = undefined;






export default DetectedFace;

