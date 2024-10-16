/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GetXpubV2200ResponseTokensInner model module.
 * @module model/GetXpubV2200ResponseTokensInner
 * @version 2.0
 */
class GetXpubV2200ResponseTokensInner {
    /**
     * Constructs a new <code>GetXpubV2200ResponseTokensInner</code>.
     * @alias module:model/GetXpubV2200ResponseTokensInner
     */
    constructor() { 
        
        GetXpubV2200ResponseTokensInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetXpubV2200ResponseTokensInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetXpubV2200ResponseTokensInner} obj Optional instance to populate.
     * @return {module:model/GetXpubV2200ResponseTokensInner} The populated <code>GetXpubV2200ResponseTokensInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetXpubV2200ResponseTokensInner();

            if (data.hasOwnProperty('balance')) {
                obj['balance'] = ApiClient.convertToType(data['balance'], 'String');
            }
            if (data.hasOwnProperty('decimals')) {
                obj['decimals'] = ApiClient.convertToType(data['decimals'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('totalReceived')) {
                obj['totalReceived'] = ApiClient.convertToType(data['totalReceived'], 'String');
            }
            if (data.hasOwnProperty('totalSent')) {
                obj['totalSent'] = ApiClient.convertToType(data['totalSent'], 'String');
            }
            if (data.hasOwnProperty('transfers')) {
                obj['transfers'] = ApiClient.convertToType(data['transfers'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetXpubV2200ResponseTokensInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetXpubV2200ResponseTokensInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['balance'] && !(typeof data['balance'] === 'string' || data['balance'] instanceof String)) {
            throw new Error("Expected the field `balance` to be a primitive type in the JSON string but got " + data['balance']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }
        // ensure the json data is a string
        if (data['totalReceived'] && !(typeof data['totalReceived'] === 'string' || data['totalReceived'] instanceof String)) {
            throw new Error("Expected the field `totalReceived` to be a primitive type in the JSON string but got " + data['totalReceived']);
        }
        // ensure the json data is a string
        if (data['totalSent'] && !(typeof data['totalSent'] === 'string' || data['totalSent'] instanceof String)) {
            throw new Error("Expected the field `totalSent` to be a primitive type in the JSON string but got " + data['totalSent']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {String} balance
 */
GetXpubV2200ResponseTokensInner.prototype['balance'] = undefined;

/**
 * @member {Number} decimals
 */
GetXpubV2200ResponseTokensInner.prototype['decimals'] = undefined;

/**
 * @member {String} name
 */
GetXpubV2200ResponseTokensInner.prototype['name'] = undefined;

/**
 * @member {String} path
 */
GetXpubV2200ResponseTokensInner.prototype['path'] = undefined;

/**
 * @member {String} totalReceived
 */
GetXpubV2200ResponseTokensInner.prototype['totalReceived'] = undefined;

/**
 * @member {String} totalSent
 */
GetXpubV2200ResponseTokensInner.prototype['totalSent'] = undefined;

/**
 * @member {Number} transfers
 */
GetXpubV2200ResponseTokensInner.prototype['transfers'] = undefined;

/**
 * @member {String} type
 */
GetXpubV2200ResponseTokensInner.prototype['type'] = undefined;






export default GetXpubV2200ResponseTokensInner;

