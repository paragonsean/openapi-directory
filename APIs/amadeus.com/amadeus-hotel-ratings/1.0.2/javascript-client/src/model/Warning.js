/**
 * Hotel Ratings
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, this API in test only offers 24 hotels; 10 in London and 14 in New-York. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ErrorSource from './ErrorSource';

/**
 * The Warning model module.
 * @module model/Warning
 * @version 1.0.2
 */
class Warning {
    /**
     * Constructs a new <code>Warning</code>.
     * @alias module:model/Warning
     * @param code {Number} A machine-readable error code from the Canned Messages table, that will enable the API Consumers code to handle this type of error
     * @param title {String} An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized
     */
    constructor(code, title) { 
        
        Warning.initialize(this, code, title);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, code, title) { 
        obj['code'] = code;
        obj['title'] = title;
    }

    /**
     * Constructs a <code>Warning</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Warning} obj Optional instance to populate.
     * @return {module:model/Warning} The populated <code>Warning</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Warning();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'Number');
            }
            if (data.hasOwnProperty('detail')) {
                obj['detail'] = ApiClient.convertToType(data['detail'], 'String');
            }
            if (data.hasOwnProperty('documentation')) {
                obj['documentation'] = ApiClient.convertToType(data['documentation'], 'String');
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = ErrorSource.constructFromObject(data['source']);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Warning</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Warning</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Warning.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['detail'] && !(typeof data['detail'] === 'string' || data['detail'] instanceof String)) {
            throw new Error("Expected the field `detail` to be a primitive type in the JSON string but got " + data['detail']);
        }
        // ensure the json data is a string
        if (data['documentation'] && !(typeof data['documentation'] === 'string' || data['documentation'] instanceof String)) {
            throw new Error("Expected the field `documentation` to be a primitive type in the JSON string but got " + data['documentation']);
        }
        // validate the optional field `source`
        if (data['source']) { // data not null
          ErrorSource.validateJSON(data['source']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}

Warning.RequiredProperties = ["code", "title"];

/**
 * A machine-readable error code from the Canned Messages table, that will enable the API Consumers code to handle this type of error
 * @member {Number} code
 */
Warning.prototype['code'] = undefined;

/**
 * An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized.
 * @member {String} detail
 */
Warning.prototype['detail'] = undefined;

/**
 * A link to a web page or file with further documentation to help the API consumer resolve this error
 * @member {String} documentation
 */
Warning.prototype['documentation'] = undefined;

/**
 * @member {module:model/ErrorSource} source
 */
Warning.prototype['source'] = undefined;

/**
 * An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized
 * @member {String} title
 */
Warning.prototype['title'] = undefined;






export default Warning;

