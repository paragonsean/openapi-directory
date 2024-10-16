/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import SpellCheckResponseTokensInner from './SpellCheckResponseTokensInner';

/**
 * The SpellCheckResponse model module.
 * @module model/SpellCheckResponse
 * @version 2.0
 */
class SpellCheckResponse {
    /**
     * Constructs a new <code>SpellCheckResponse</code>.
     * @alias module:model/SpellCheckResponse
     * @param correctedTextHtml {String} The corrected text for the entire search term (multiple words/tokens), where misspelled tokens are replaced with the correct texts and html tags <b><i>
     * @param tokens {Array.<module:model/SpellCheckResponseTokensInner>} The word in the text query string that is not spelled correctly
     */
    constructor(correctedTextHtml, tokens) { 
        
        SpellCheckResponse.initialize(this, correctedTextHtml, tokens);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, correctedTextHtml, tokens) { 
        obj['corrected_text_html'] = correctedTextHtml;
        obj['tokens'] = tokens;
    }

    /**
     * Constructs a <code>SpellCheckResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SpellCheckResponse} obj Optional instance to populate.
     * @return {module:model/SpellCheckResponse} The populated <code>SpellCheckResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SpellCheckResponse();

            if (data.hasOwnProperty('corrected_text_html')) {
                obj['corrected_text_html'] = ApiClient.convertToType(data['corrected_text_html'], 'String');
            }
            if (data.hasOwnProperty('tokens')) {
                obj['tokens'] = ApiClient.convertToType(data['tokens'], [SpellCheckResponseTokensInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SpellCheckResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SpellCheckResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SpellCheckResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['corrected_text_html'] && !(typeof data['corrected_text_html'] === 'string' || data['corrected_text_html'] instanceof String)) {
            throw new Error("Expected the field `corrected_text_html` to be a primitive type in the JSON string but got " + data['corrected_text_html']);
        }
        if (data['tokens']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tokens'])) {
                throw new Error("Expected the field `tokens` to be an array in the JSON data but got " + data['tokens']);
            }
            // validate the optional field `tokens` (array)
            for (const item of data['tokens']) {
                SpellCheckResponseTokensInner.validateJSON(item);
            };
        }

        return true;
    }


}

SpellCheckResponse.RequiredProperties = ["corrected_text_html", "tokens"];

/**
 * The corrected text for the entire search term (multiple words/tokens), where misspelled tokens are replaced with the correct texts and html tags <b><i>
 * @member {String} corrected_text_html
 */
SpellCheckResponse.prototype['corrected_text_html'] = undefined;

/**
 * The word in the text query string that is not spelled correctly
 * @member {Array.<module:model/SpellCheckResponseTokensInner>} tokens
 */
SpellCheckResponse.prototype['tokens'] = undefined;






export default SpellCheckResponse;

