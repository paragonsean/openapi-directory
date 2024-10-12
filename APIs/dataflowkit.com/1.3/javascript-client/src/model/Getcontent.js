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
 * The Getcontent model module.
 * @module model/Getcontent
 * @version 1.3
 */
class Getcontent {
    /**
     * Constructs a new <code>Getcontent</code>.
     * Sometimes it is necessary to retrieve the HTML content of a web page multiple times in a single request. This action is for that.
     * @alias module:model/Getcontent
     */
    constructor() { 
        
        Getcontent.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Getcontent</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Getcontent} obj Optional instance to populate.
     * @return {module:model/Getcontent} The populated <code>Getcontent</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Getcontent();

            if (data.hasOwnProperty('skipLastIteration')) {
                obj['skipLastIteration'] = ApiClient.convertToType(data['skipLastIteration'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Getcontent</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Getcontent</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * It is only used for loop actions only. Skips the last iteration.
 * @member {Boolean} skipLastIteration
 */
Getcontent.prototype['skipLastIteration'] = undefined;






export default Getcontent;

