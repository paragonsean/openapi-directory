/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
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
import TagPathTag from './TagPathTag';

/**
 * The AnonymizationKeyValue model module.
 * @module model/AnonymizationKeyValue
 * @version 2.0
 */
class AnonymizationKeyValue {
    /**
     * Constructs a new <code>AnonymizationKeyValue</code>.
     * @alias module:model/AnonymizationKeyValue
     */
    constructor() { 
        
        AnonymizationKeyValue.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnonymizationKeyValue</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnonymizationKeyValue} obj Optional instance to populate.
     * @return {module:model/AnonymizationKeyValue} The populated <code>AnonymizationKeyValue</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnonymizationKeyValue();

            if (data.hasOwnProperty('anonymizationKeyId')) {
                obj['anonymizationKeyId'] = ApiClient.convertToType(data['anonymizationKeyId'], 'Number');
            }
            if (data.hasOwnProperty('anonymizedValue')) {
                obj['anonymizedValue'] = ApiClient.convertToType(data['anonymizedValue'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('tagPath')) {
                obj['tagPath'] = TagPathTag.constructFromObject(data['tagPath']);
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnonymizationKeyValue</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnonymizationKeyValue</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['anonymizedValue'] && !(typeof data['anonymizedValue'] === 'string' || data['anonymizedValue'] instanceof String)) {
            throw new Error("Expected the field `anonymizedValue` to be a primitive type in the JSON string but got " + data['anonymizedValue']);
        }
        // validate the optional field `tagPath`
        if (data['tagPath']) { // data not null
          TagPathTag.validateJSON(data['tagPath']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * @member {Number} anonymizationKeyId
 */
AnonymizationKeyValue.prototype['anonymizationKeyId'] = undefined;

/**
 * @member {String} anonymizedValue
 */
AnonymizationKeyValue.prototype['anonymizedValue'] = undefined;

/**
 * @member {Number} id
 */
AnonymizationKeyValue.prototype['id'] = undefined;

/**
 * @member {module:model/TagPathTag} tagPath
 */
AnonymizationKeyValue.prototype['tagPath'] = undefined;

/**
 * @member {String} value
 */
AnonymizationKeyValue.prototype['value'] = undefined;






export default AnonymizationKeyValue;

