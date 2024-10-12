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
 * The DoubleClick model module.
 * @module model/DoubleClick
 * @version 1.3
 */
class DoubleClick {
    /**
     * Constructs a new <code>DoubleClick</code>.
     * Double clicks on a target element (such as a link, button, checkbox, or radio button) with specified CSS Selector.
     * @alias module:model/DoubleClick
     */
    constructor() { 
        
        DoubleClick.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DoubleClick</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DoubleClick} obj Optional instance to populate.
     * @return {module:model/DoubleClick} The populated <code>DoubleClick</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DoubleClick();

            if (data.hasOwnProperty('ignoreIfNotPresent')) {
                obj['ignoreIfNotPresent'] = ApiClient.convertToType(data['ignoreIfNotPresent'], 'Boolean');
            }
            if (data.hasOwnProperty('selector')) {
                obj['selector'] = ApiClient.convertToType(data['selector'], 'String');
            }
            if (data.hasOwnProperty('skipLastIteration')) {
                obj['skipLastIteration'] = ApiClient.convertToType(data['skipLastIteration'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DoubleClick</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DoubleClick</code>.
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
 * This optional parameter is useful when the target element occasionally may not be present in the DOM.
 * @member {Boolean} ignoreIfNotPresent
 */
DoubleClick.prototype['ignoreIfNotPresent'] = undefined;

/**
 * Must be a valid CSS Selector
 * @member {String} selector
 */
DoubleClick.prototype['selector'] = undefined;

/**
 * It is only used for click action inside a loop only. Skips the last iteration.
 * @member {Boolean} skipLastIteration
 */
DoubleClick.prototype['skipLastIteration'] = undefined;






export default DoubleClick;

