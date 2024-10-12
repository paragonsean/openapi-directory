/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OutputCollectionResult model module.
 * @module model/OutputCollectionResult
 * @version 2021.1.01
 */
class OutputCollectionResult {
    /**
     * Constructs a new <code>OutputCollectionResult</code>.
     * @alias module:model/OutputCollectionResult
     */
    constructor() { 
        
        OutputCollectionResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OutputCollectionResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OutputCollectionResult} obj Optional instance to populate.
     * @return {module:model/OutputCollectionResult} The populated <code>OutputCollectionResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OutputCollectionResult();

            if (data.hasOwnProperty('result')) {
                obj['result'] = ApiClient.convertToType(data['result'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OutputCollectionResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OutputCollectionResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['result'])) {
            throw new Error("Expected the field `result` to be an array in the JSON data but got " + data['result']);
        }

        return true;
    }


}



/**
 * Modified collection result
 * @member {Array.<String>} result
 */
OutputCollectionResult.prototype['result'] = undefined;






export default OutputCollectionResult;

