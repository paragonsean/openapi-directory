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
import Fetchrequest from './Fetchrequest';
import Field from './Field';
import Paginator from './Paginator';

/**
 * The Parserequest model module.
 * @module model/Parserequest
 * @version 1.3
 */
class Parserequest {
    /**
     * Constructs a new <code>Parserequest</code>.
     * @alias module:model/Parserequest
     * @param fields {Array.<module:model/Field>} Define a  set of fields used to extract data from a web page. A Field represents a given chunk of extracted data from every block on each page. 
     * @param format {module:model/Parserequest.FormatEnum} Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format.
     * @param name {String} Collection name.
     */
    constructor(fields, format, name) { 
        
        Parserequest.initialize(this, fields, format, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, fields, format, name) { 
        obj['fields'] = fields;
        obj['format'] = format;
        obj['name'] = name;
        obj['path'] = false;
    }

    /**
     * Constructs a <code>Parserequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Parserequest} obj Optional instance to populate.
     * @return {module:model/Parserequest} The populated <code>Parserequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Parserequest();

            if (data.hasOwnProperty('commonParent')) {
                obj['commonParent'] = ApiClient.convertToType(data['commonParent'], 'String');
            }
            if (data.hasOwnProperty('fields')) {
                obj['fields'] = ApiClient.convertToType(data['fields'], [Field]);
            }
            if (data.hasOwnProperty('format')) {
                obj['format'] = ApiClient.convertToType(data['format'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('paginator')) {
                obj['paginator'] = Paginator.constructFromObject(data['paginator']);
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'Boolean');
            }
            if (data.hasOwnProperty('request')) {
                obj['request'] = Fetchrequest.constructFromObject(data['request']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Parserequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Parserequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Parserequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['commonParent'] && !(typeof data['commonParent'] === 'string' || data['commonParent'] instanceof String)) {
            throw new Error("Expected the field `commonParent` to be a primitive type in the JSON string but got " + data['commonParent']);
        }
        if (data['fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['fields'])) {
                throw new Error("Expected the field `fields` to be an array in the JSON data but got " + data['fields']);
            }
            // validate the optional field `fields` (array)
            for (const item of data['fields']) {
                Field.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['format'] && !(typeof data['format'] === 'string' || data['format'] instanceof String)) {
            throw new Error("Expected the field `format` to be a primitive type in the JSON string but got " + data['format']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `paginator`
        if (data['paginator']) { // data not null
          Paginator.validateJSON(data['paginator']);
        }
        // validate the optional field `request`
        if (data['request']) { // data not null
          Fetchrequest.validateJSON(data['request']);
        }

        return true;
    }


}

Parserequest.RequiredProperties = ["fields", "format", "name"];

/**
 * Specifies common ancestor block for a set of fields used to extract data from a web page. _(CSS Selector)_
 * @member {String} commonParent
 */
Parserequest.prototype['commonParent'] = undefined;

/**
 * Define a  set of fields used to extract data from a web page. A Field represents a given chunk of extracted data from every block on each page. 
 * @member {Array.<module:model/Field>} fields
 */
Parserequest.prototype['fields'] = undefined;

/**
 * Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format.
 * @member {module:model/Parserequest.FormatEnum} format
 */
Parserequest.prototype['format'] = undefined;

/**
 * Collection name.
 * @member {String} name
 */
Parserequest.prototype['name'] = undefined;

/**
 * @member {module:model/Paginator} paginator
 */
Parserequest.prototype['paginator'] = undefined;

/**
 * Path is a special parameter specifying navigation pages only. It collects information from detailed pages. No results from the current page return. Defaults to false.
 * @member {Boolean} path
 * @default false
 */
Parserequest.prototype['path'] = false;

/**
 * @member {module:model/Fetchrequest} request
 */
Parserequest.prototype['request'] = undefined;





/**
 * Allowed values for the <code>format</code> property.
 * @enum {String}
 * @readonly
 */
Parserequest['FormatEnum'] = {

    /**
     * value: "csv"
     * @const
     */
    "csv": "csv",

    /**
     * value: "json"
     * @const
     */
    "json": "json",

    /**
     * value: "jsonl"
     * @const
     */
    "jsonl": "jsonl",

    /**
     * value: "excel"
     * @const
     */
    "excel": "excel",

    /**
     * value: "xml"
     * @const
     */
    "xml": "xml"
};



export default Parserequest;

