/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Description model module.
 * @module model/Description
 * @version 2.0.2
 */
class Description {
    /**
     * Constructs a new <code>Description</code>.
     * @alias module:model/Description
     */
    constructor() { 
        
        Description.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Description</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Description} obj Optional instance to populate.
     * @return {module:model/Description} The populated <code>Description</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Description();

            if (data.hasOwnProperty('descriptionType')) {
                obj['descriptionType'] = ApiClient.convertToType(data['descriptionType'], 'String');
            }
            if (data.hasOwnProperty('text')) {
                obj['text'] = ApiClient.convertToType(data['text'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Description</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Description</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['descriptionType'] && !(typeof data['descriptionType'] === 'string' || data['descriptionType'] instanceof String)) {
            throw new Error("Expected the field `descriptionType` to be a primitive type in the JSON string but got " + data['descriptionType']);
        }
        // ensure the json data is a string
        if (data['text'] && !(typeof data['text'] === 'string' || data['text'] instanceof String)) {
            throw new Error("Expected the field `text` to be a primitive type in the JSON string but got " + data['text']);
        }

        return true;
    }


}



/**
 * @member {String} descriptionType
 */
Description.prototype['descriptionType'] = undefined;

/**
 * @member {String} text
 */
Description.prototype['text'] = undefined;






export default Description;

