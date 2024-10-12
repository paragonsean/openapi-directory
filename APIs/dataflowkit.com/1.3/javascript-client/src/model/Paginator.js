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
 * The Paginator model module.
 * @module model/Paginator
 * @version 1.3
 */
class Paginator {
    /**
     * Constructs a new <code>Paginator</code>.
     * Specify _Next link_ paginator on pages containing a link pointing to the next page. The next page link is extracted from a document by querying href attribute of a given element&#39;s CSS selector.
     * @alias module:model/Paginator
     */
    constructor() { 
        
        Paginator.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Paginator</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Paginator} obj Optional instance to populate.
     * @return {module:model/Paginator} The populated <code>Paginator</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Paginator();

            if (data.hasOwnProperty('nextPageSelector')) {
                obj['nextPageSelector'] = ApiClient.convertToType(data['nextPageSelector'], 'String');
            }
            if (data.hasOwnProperty('pageNum')) {
                obj['pageNum'] = ApiClient.convertToType(data['pageNum'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Paginator</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Paginator</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nextPageSelector'] && !(typeof data['nextPageSelector'] === 'string' || data['nextPageSelector'] instanceof String)) {
            throw new Error("Expected the field `nextPageSelector` to be a primitive type in the JSON string but got " + data['nextPageSelector']);
        }

        return true;
    }


}



/**
 * @member {String} nextPageSelector
 */
Paginator.prototype['nextPageSelector'] = undefined;

/**
 * @member {Number} pageNum
 */
Paginator.prototype['pageNum'] = undefined;






export default Paginator;

