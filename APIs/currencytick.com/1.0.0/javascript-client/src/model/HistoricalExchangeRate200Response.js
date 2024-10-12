/**
 * Currencytick API Documentation
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HistoricalExchangeRate200Response model module.
 * @module model/HistoricalExchangeRate200Response
 * @version 1.0.0
 */
class HistoricalExchangeRate200Response {
    /**
     * Constructs a new <code>HistoricalExchangeRate200Response</code>.
     * @alias module:model/HistoricalExchangeRate200Response
     */
    constructor() { 
        
        HistoricalExchangeRate200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HistoricalExchangeRate200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HistoricalExchangeRate200Response} obj Optional instance to populate.
     * @return {module:model/HistoricalExchangeRate200Response} The populated <code>HistoricalExchangeRate200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HistoricalExchangeRate200Response();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'String');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
            if (data.hasOwnProperty('from')) {
                obj['from'] = ApiClient.convertToType(data['from'], 'String');
            }
            if (data.hasOwnProperty('rate')) {
                obj['rate'] = ApiClient.convertToType(data['rate'], 'Number');
            }
            if (data.hasOwnProperty('to')) {
                obj['to'] = ApiClient.convertToType(data['to'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HistoricalExchangeRate200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HistoricalExchangeRate200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['amount'] && !(typeof data['amount'] === 'string' || data['amount'] instanceof String)) {
            throw new Error("Expected the field `amount` to be a primitive type in the JSON string but got " + data['amount']);
        }
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }
        // ensure the json data is a string
        if (data['from'] && !(typeof data['from'] === 'string' || data['from'] instanceof String)) {
            throw new Error("Expected the field `from` to be a primitive type in the JSON string but got " + data['from']);
        }
        // ensure the json data is a string
        if (data['to'] && !(typeof data['to'] === 'string' || data['to'] instanceof String)) {
            throw new Error("Expected the field `to` to be a primitive type in the JSON string but got " + data['to']);
        }

        return true;
    }


}



/**
 * @member {String} amount
 */
HistoricalExchangeRate200Response.prototype['amount'] = undefined;

/**
 * @member {String} date
 */
HistoricalExchangeRate200Response.prototype['date'] = undefined;

/**
 * @member {String} from
 */
HistoricalExchangeRate200Response.prototype['from'] = undefined;

/**
 * @member {Number} rate
 */
HistoricalExchangeRate200Response.prototype['rate'] = undefined;

/**
 * @member {String} to
 */
HistoricalExchangeRate200Response.prototype['to'] = undefined;






export default HistoricalExchangeRate200Response;

