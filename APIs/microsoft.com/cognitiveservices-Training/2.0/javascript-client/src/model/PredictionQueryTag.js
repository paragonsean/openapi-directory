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

/**
 * The PredictionQueryTag model module.
 * @module model/PredictionQueryTag
 * @version 2.0
 */
class PredictionQueryTag {
    /**
     * Constructs a new <code>PredictionQueryTag</code>.
     * @alias module:model/PredictionQueryTag
     */
    constructor() { 
        
        PredictionQueryTag.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PredictionQueryTag</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PredictionQueryTag} obj Optional instance to populate.
     * @return {module:model/PredictionQueryTag} The populated <code>PredictionQueryTag</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PredictionQueryTag();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('maxThreshold')) {
                obj['maxThreshold'] = ApiClient.convertToType(data['maxThreshold'], 'Number');
            }
            if (data.hasOwnProperty('minThreshold')) {
                obj['minThreshold'] = ApiClient.convertToType(data['minThreshold'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PredictionQueryTag</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PredictionQueryTag</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * @member {String} id
 */
PredictionQueryTag.prototype['id'] = undefined;

/**
 * @member {Number} maxThreshold
 */
PredictionQueryTag.prototype['maxThreshold'] = undefined;

/**
 * @member {Number} minThreshold
 */
PredictionQueryTag.prototype['minThreshold'] = undefined;






export default PredictionQueryTag;

