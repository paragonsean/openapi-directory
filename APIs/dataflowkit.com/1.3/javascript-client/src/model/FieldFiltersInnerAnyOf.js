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
 * The FieldFiltersInnerAnyOf model module.
 * @module model/FieldFiltersInnerAnyOf
 * @version 1.3
 */
class FieldFiltersInnerAnyOf {
    /**
     * Constructs a new <code>FieldFiltersInnerAnyOf</code>.
     * @alias module:model/FieldFiltersInnerAnyOf
     */
    constructor() { 
        
        FieldFiltersInnerAnyOf.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FieldFiltersInnerAnyOf</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FieldFiltersInnerAnyOf} obj Optional instance to populate.
     * @return {module:model/FieldFiltersInnerAnyOf} The populated <code>FieldFiltersInnerAnyOf</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FieldFiltersInnerAnyOf();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FieldFiltersInnerAnyOf</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FieldFiltersInnerAnyOf</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {module:model/FieldFiltersInnerAnyOf.NameEnum} name
 */
FieldFiltersInnerAnyOf.prototype['name'] = undefined;





/**
 * Allowed values for the <code>name</code> property.
 * @enum {String}
 * @readonly
 */
FieldFiltersInnerAnyOf['NameEnum'] = {

    /**
     * value: "trim"
     * @const
     */
    "trim": "trim",

    /**
     * value: "normal"
     * @const
     */
    "normal": "normal",

    /**
     * value: "uppercase"
     * @const
     */
    "uppercase": "uppercase",

    /**
     * value: "lowercase"
     * @const
     */
    "lowercase": "lowercase",

    /**
     * value: "capitalize"
     * @const
     */
    "capitalize": "capitalize",

    /**
     * value: "concatinate"
     * @const
     */
    "concatinate": "concatinate"
};



export default FieldFiltersInnerAnyOf;

