/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Prediction from './Prediction';

/**
 * The ImagePrediction model module.
 * @module model/ImagePrediction
 * @version 2.0
 */
class ImagePrediction {
    /**
     * Constructs a new <code>ImagePrediction</code>.
     * @alias module:model/ImagePrediction
     */
    constructor() { 
        
        ImagePrediction.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImagePrediction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImagePrediction} obj Optional instance to populate.
     * @return {module:model/ImagePrediction} The populated <code>ImagePrediction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImagePrediction();

            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('iteration')) {
                obj['iteration'] = ApiClient.convertToType(data['iteration'], 'String');
            }
            if (data.hasOwnProperty('predictions')) {
                obj['predictions'] = ApiClient.convertToType(data['predictions'], [Prediction]);
            }
            if (data.hasOwnProperty('project')) {
                obj['project'] = ApiClient.convertToType(data['project'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImagePrediction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImagePrediction</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['iteration'] && !(typeof data['iteration'] === 'string' || data['iteration'] instanceof String)) {
            throw new Error("Expected the field `iteration` to be a primitive type in the JSON string but got " + data['iteration']);
        }
        if (data['predictions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['predictions'])) {
                throw new Error("Expected the field `predictions` to be an array in the JSON data but got " + data['predictions']);
            }
            // validate the optional field `predictions` (array)
            for (const item of data['predictions']) {
                Prediction.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['project'] && !(typeof data['project'] === 'string' || data['project'] instanceof String)) {
            throw new Error("Expected the field `project` to be a primitive type in the JSON string but got " + data['project']);
        }

        return true;
    }


}



/**
 * @member {Date} created
 */
ImagePrediction.prototype['created'] = undefined;

/**
 * @member {String} id
 */
ImagePrediction.prototype['id'] = undefined;

/**
 * @member {String} iteration
 */
ImagePrediction.prototype['iteration'] = undefined;

/**
 * @member {Array.<module:model/Prediction>} predictions
 */
ImagePrediction.prototype['predictions'] = undefined;

/**
 * @member {String} project
 */
ImagePrediction.prototype['project'] = undefined;






export default ImagePrediction;

