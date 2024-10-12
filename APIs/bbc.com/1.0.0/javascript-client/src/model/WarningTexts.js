/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import WarningTextsWarningTextInner from './WarningTextsWarningTextInner';

/**
 * The WarningTexts model module.
 * @module model/WarningTexts
 * @version 1.0.0
 */
class WarningTexts {
    /**
     * Constructs a new <code>WarningTexts</code>.
     * @alias module:model/WarningTexts
     */
    constructor() { 
        
        WarningTexts.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WarningTexts</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WarningTexts} obj Optional instance to populate.
     * @return {module:model/WarningTexts} The populated <code>WarningTexts</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WarningTexts();

            if (data.hasOwnProperty('warning_text')) {
                obj['warning_text'] = ApiClient.convertToType(data['warning_text'], [WarningTextsWarningTextInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WarningTexts</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WarningTexts</code>.
     */
    static validateJSON(data) {
        if (data['warning_text']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['warning_text'])) {
                throw new Error("Expected the field `warning_text` to be an array in the JSON data but got " + data['warning_text']);
            }
            // validate the optional field `warning_text` (array)
            for (const item of data['warning_text']) {
                WarningTextsWarningTextInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/WarningTextsWarningTextInner>} warning_text
 */
WarningTexts.prototype['warning_text'] = undefined;






export default WarningTexts;

