/**
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Submit model module.
 * @module model/Submit
 * @version 1.3
 */
class Submit {
    /**
     * Constructs a new <code>Submit</code>.
     * Submit the specified form. This action is useful for forms without explicit submit buttons, such as single-input Search forms.
     * @alias module:model/Submit
     */
    constructor() { 
        
        Submit.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Submit</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Submit} obj Optional instance to populate.
     * @return {module:model/Submit} The populated <code>Submit</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Submit();

            if (data.hasOwnProperty('selector')) {
                obj['selector'] = ApiClient.convertToType(data['selector'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Submit</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Submit</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['selector'] && !(typeof data['selector'] === 'string' || data['selector'] instanceof String)) {
            throw new Error("Expected the field `selector` to be a primitive type in the JSON string but got " + data['selector']);
        }

        return true;
    }


}



/**
 * Must be an any valid CSS Selector inside the parent form to submit.
 * @member {String} selector
 */
Submit.prototype['selector'] = undefined;






export default Submit;

