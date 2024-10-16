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
import Action from './Action';
import InitialCookie from './InitialCookie';

/**
 * The Fetchrequest model module.
 * @module model/Fetchrequest
 * @version 1.3
 */
class Fetchrequest {
    /**
     * Constructs a new <code>Fetchrequest</code>.
     * @alias module:model/Fetchrequest
     * @param type {module:model/Fetchrequest.TypeEnum} If set to `base`, the Base fetcher is used for downloading web page content. Use `chrome` for fetching content with a Headless chrome browser. If omitted `base` fetcher is used by default.
     * @param url {String} Specify URL to download.
     */
    constructor(type, url) { 
        
        Fetchrequest.initialize(this, type, url);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type, url) { 
        obj['output'] = 'buffer';
        obj['type'] = type;
        obj['url'] = url;
    }

    /**
     * Constructs a <code>Fetchrequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Fetchrequest} obj Optional instance to populate.
     * @return {module:model/Fetchrequest} The populated <code>Fetchrequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Fetchrequest();

            if (data.hasOwnProperty('actions')) {
                obj['actions'] = ApiClient.convertToType(data['actions'], [Action]);
            }
            if (data.hasOwnProperty('ignoreHTTPStatusErrCodes')) {
                obj['ignoreHTTPStatusErrCodes'] = ApiClient.convertToType(data['ignoreHTTPStatusErrCodes'], 'Boolean');
            }
            if (data.hasOwnProperty('initialCookies')) {
                obj['initialCookies'] = ApiClient.convertToType(data['initialCookies'], [InitialCookie]);
            }
            if (data.hasOwnProperty('output')) {
                obj['output'] = ApiClient.convertToType(data['output'], 'String');
            }
            if (data.hasOwnProperty('proxy')) {
                obj['proxy'] = ApiClient.convertToType(data['proxy'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
            if (data.hasOwnProperty('waitDelay')) {
                obj['waitDelay'] = ApiClient.convertToType(data['waitDelay'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Fetchrequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Fetchrequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Fetchrequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['actions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['actions'])) {
                throw new Error("Expected the field `actions` to be an array in the JSON data but got " + data['actions']);
            }
            // validate the optional field `actions` (array)
            for (const item of data['actions']) {
                Action.validateJSON(item);
            };
        }
        if (data['initialCookies']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['initialCookies'])) {
                throw new Error("Expected the field `initialCookies` to be an array in the JSON data but got " + data['initialCookies']);
            }
            // validate the optional field `initialCookies` (array)
            for (const item of data['initialCookies']) {
                InitialCookie.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['output'] && !(typeof data['output'] === 'string' || data['output'] instanceof String)) {
            throw new Error("Expected the field `output` to be a primitive type in the JSON string but got " + data['output']);
        }
        // ensure the json data is a string
        if (data['proxy'] && !(typeof data['proxy'] === 'string' || data['proxy'] instanceof String)) {
            throw new Error("Expected the field `proxy` to be a primitive type in the JSON string but got " + data['proxy']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}

Fetchrequest.RequiredProperties = ["type", "url"];

/**
 * Use actions to automate manual workflows while rendering web pages. They simulate real-world human interaction with pages. _(Chrome fetcher type only)_
 * @member {Array.<module:model/Action>} actions
 */
Fetchrequest.prototype['actions'] = undefined;

/**
 * The HTTP 200 OK success status response code indicates that the request has succeeded. Sometimes a server returns normal HTML content even with an erroneous Non-200 HTTP response status code. The IgnoreHTTPStatusCode option is useful when you need to force the return of HTML content. Defaults to \"false.\"
 * @member {Boolean} ignoreHTTPStatusErrCodes
 */
Fetchrequest.prototype['ignoreHTTPStatusErrCodes'] = undefined;

/**
 * The \"Initial Cookies\" option is useful for crawling websites that require a login. The simplest solution to get an array of cookies for specific websites is to use a web browser \"EditThisCookie\" extension. Copy a cookie array with \"EditThisCookie\" and paste it into the \"Initial cookie\" field.
 * @member {Array.<module:model/InitialCookie>} initialCookies
 */
Fetchrequest.prototype['initialCookies'] = undefined;

/**
 * If set to _file_, the content of downloaded HTML is uploaded to Dataflow Kit Storage first. Then the link to this file is returned. Overwise, downloaded content is returned in the response body.
 * @member {module:model/Fetchrequest.OutputEnum} output
 * @default 'buffer'
 */
Fetchrequest.prototype['output'] = 'buffer';

/**
 * Specify proxy by adding [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to `country-` value to send requests through a proxy in the specified country. Use `country-any` to use random geo-targets.
 * @member {String} proxy
 */
Fetchrequest.prototype['proxy'] = undefined;

/**
 * If set to `base`, the Base fetcher is used for downloading web page content. Use `chrome` for fetching content with a Headless chrome browser. If omitted `base` fetcher is used by default.
 * @member {module:model/Fetchrequest.TypeEnum} type
 */
Fetchrequest.prototype['type'] = undefined;

/**
 * Specify URL to download.
 * @member {String} url
 */
Fetchrequest.prototype['url'] = undefined;

/**
 * Specify a wait delay (in seconds). This may be useful if certain elements of the web site need to be rendered after the initial page load. _(Chrome fetcher type only)_
 * @member {Number} waitDelay
 */
Fetchrequest.prototype['waitDelay'] = undefined;





/**
 * Allowed values for the <code>output</code> property.
 * @enum {String}
 * @readonly
 */
Fetchrequest['OutputEnum'] = {

    /**
     * value: "buffer"
     * @const
     */
    "buffer": "buffer",

    /**
     * value: "file"
     * @const
     */
    "file": "file"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Fetchrequest['TypeEnum'] = {

    /**
     * value: "base"
     * @const
     */
    "base": "base",

    /**
     * value: "chrome"
     * @const
     */
    "chrome": "chrome"
};



export default Fetchrequest;

