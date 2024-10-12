/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PredictionTag from './PredictionTag';

/**
 * The Prediction model module.
 * @module model/Prediction
 * @version 1.2
 */
class Prediction {
    /**
     * Constructs a new <code>Prediction</code>.
     * result of an image classification request
     * @alias module:model/Prediction
     */
    constructor() { 
        
        Prediction.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Prediction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Prediction} obj Optional instance to populate.
     * @return {module:model/Prediction} The populated <code>Prediction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Prediction();

            if (data.hasOwnProperty('Created')) {
                obj['Created'] = ApiClient.convertToType(data['Created'], 'Date');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'String');
            }
            if (data.hasOwnProperty('ImageUri')) {
                obj['ImageUri'] = ApiClient.convertToType(data['ImageUri'], 'String');
            }
            if (data.hasOwnProperty('Iteration')) {
                obj['Iteration'] = ApiClient.convertToType(data['Iteration'], 'String');
            }
            if (data.hasOwnProperty('Predictions')) {
                obj['Predictions'] = ApiClient.convertToType(data['Predictions'], [PredictionTag]);
            }
            if (data.hasOwnProperty('Project')) {
                obj['Project'] = ApiClient.convertToType(data['Project'], 'String');
            }
            if (data.hasOwnProperty('ThumbnailUri')) {
                obj['ThumbnailUri'] = ApiClient.convertToType(data['ThumbnailUri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Prediction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Prediction</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Id'] && !(typeof data['Id'] === 'string' || data['Id'] instanceof String)) {
            throw new Error("Expected the field `Id` to be a primitive type in the JSON string but got " + data['Id']);
        }
        // ensure the json data is a string
        if (data['ImageUri'] && !(typeof data['ImageUri'] === 'string' || data['ImageUri'] instanceof String)) {
            throw new Error("Expected the field `ImageUri` to be a primitive type in the JSON string but got " + data['ImageUri']);
        }
        // ensure the json data is a string
        if (data['Iteration'] && !(typeof data['Iteration'] === 'string' || data['Iteration'] instanceof String)) {
            throw new Error("Expected the field `Iteration` to be a primitive type in the JSON string but got " + data['Iteration']);
        }
        if (data['Predictions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Predictions'])) {
                throw new Error("Expected the field `Predictions` to be an array in the JSON data but got " + data['Predictions']);
            }
            // validate the optional field `Predictions` (array)
            for (const item of data['Predictions']) {
                PredictionTag.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Project'] && !(typeof data['Project'] === 'string' || data['Project'] instanceof String)) {
            throw new Error("Expected the field `Project` to be a primitive type in the JSON string but got " + data['Project']);
        }
        // ensure the json data is a string
        if (data['ThumbnailUri'] && !(typeof data['ThumbnailUri'] === 'string' || data['ThumbnailUri'] instanceof String)) {
            throw new Error("Expected the field `ThumbnailUri` to be a primitive type in the JSON string but got " + data['ThumbnailUri']);
        }

        return true;
    }


}



/**
 * @member {Date} Created
 */
Prediction.prototype['Created'] = undefined;

/**
 * @member {String} Id
 */
Prediction.prototype['Id'] = undefined;

/**
 * @member {String} ImageUri
 */
Prediction.prototype['ImageUri'] = undefined;

/**
 * @member {String} Iteration
 */
Prediction.prototype['Iteration'] = undefined;

/**
 * @member {Array.<module:model/PredictionTag>} Predictions
 */
Prediction.prototype['Predictions'] = undefined;

/**
 * @member {String} Project
 */
Prediction.prototype['Project'] = undefined;

/**
 * @member {String} ThumbnailUri
 */
Prediction.prototype['ThumbnailUri'] = undefined;






export default Prediction;

