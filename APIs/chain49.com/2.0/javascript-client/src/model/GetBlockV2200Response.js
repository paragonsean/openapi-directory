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
import GetBlockV2200ResponseTxsInner from './GetBlockV2200ResponseTxsInner';

/**
 * The GetBlockV2200Response model module.
 * @module model/GetBlockV2200Response
 * @version 2.0
 */
class GetBlockV2200Response {
    /**
     * Constructs a new <code>GetBlockV2200Response</code>.
     * @alias module:model/GetBlockV2200Response
     */
    constructor() { 
        
        GetBlockV2200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetBlockV2200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetBlockV2200Response} obj Optional instance to populate.
     * @return {module:model/GetBlockV2200Response} The populated <code>GetBlockV2200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetBlockV2200Response();

            if (data.hasOwnProperty('bits')) {
                obj['bits'] = ApiClient.convertToType(data['bits'], 'String');
            }
            if (data.hasOwnProperty('confirmations')) {
                obj['confirmations'] = ApiClient.convertToType(data['confirmations'], 'Number');
            }
            if (data.hasOwnProperty('difficulty')) {
                obj['difficulty'] = ApiClient.convertToType(data['difficulty'], 'String');
            }
            if (data.hasOwnProperty('hash')) {
                obj['hash'] = ApiClient.convertToType(data['hash'], 'String');
            }
            if (data.hasOwnProperty('height')) {
                obj['height'] = ApiClient.convertToType(data['height'], 'Number');
            }
            if (data.hasOwnProperty('itemsOnPage')) {
                obj['itemsOnPage'] = ApiClient.convertToType(data['itemsOnPage'], 'Number');
            }
            if (data.hasOwnProperty('merkleRoot')) {
                obj['merkleRoot'] = ApiClient.convertToType(data['merkleRoot'], 'String');
            }
            if (data.hasOwnProperty('nextBlockHash')) {
                obj['nextBlockHash'] = ApiClient.convertToType(data['nextBlockHash'], 'String');
            }
            if (data.hasOwnProperty('nonce')) {
                obj['nonce'] = ApiClient.convertToType(data['nonce'], 'String');
            }
            if (data.hasOwnProperty('page')) {
                obj['page'] = ApiClient.convertToType(data['page'], 'Number');
            }
            if (data.hasOwnProperty('previousBlockHash')) {
                obj['previousBlockHash'] = ApiClient.convertToType(data['previousBlockHash'], 'String');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'Number');
            }
            if (data.hasOwnProperty('time')) {
                obj['time'] = ApiClient.convertToType(data['time'], 'Number');
            }
            if (data.hasOwnProperty('totalPages')) {
                obj['totalPages'] = ApiClient.convertToType(data['totalPages'], 'Number');
            }
            if (data.hasOwnProperty('txCount')) {
                obj['txCount'] = ApiClient.convertToType(data['txCount'], 'Number');
            }
            if (data.hasOwnProperty('txs')) {
                obj['txs'] = ApiClient.convertToType(data['txs'], [GetBlockV2200ResponseTxsInner]);
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetBlockV2200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetBlockV2200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['bits'] && !(typeof data['bits'] === 'string' || data['bits'] instanceof String)) {
            throw new Error("Expected the field `bits` to be a primitive type in the JSON string but got " + data['bits']);
        }
        // ensure the json data is a string
        if (data['difficulty'] && !(typeof data['difficulty'] === 'string' || data['difficulty'] instanceof String)) {
            throw new Error("Expected the field `difficulty` to be a primitive type in the JSON string but got " + data['difficulty']);
        }
        // ensure the json data is a string
        if (data['hash'] && !(typeof data['hash'] === 'string' || data['hash'] instanceof String)) {
            throw new Error("Expected the field `hash` to be a primitive type in the JSON string but got " + data['hash']);
        }
        // ensure the json data is a string
        if (data['merkleRoot'] && !(typeof data['merkleRoot'] === 'string' || data['merkleRoot'] instanceof String)) {
            throw new Error("Expected the field `merkleRoot` to be a primitive type in the JSON string but got " + data['merkleRoot']);
        }
        // ensure the json data is a string
        if (data['nextBlockHash'] && !(typeof data['nextBlockHash'] === 'string' || data['nextBlockHash'] instanceof String)) {
            throw new Error("Expected the field `nextBlockHash` to be a primitive type in the JSON string but got " + data['nextBlockHash']);
        }
        // ensure the json data is a string
        if (data['nonce'] && !(typeof data['nonce'] === 'string' || data['nonce'] instanceof String)) {
            throw new Error("Expected the field `nonce` to be a primitive type in the JSON string but got " + data['nonce']);
        }
        // ensure the json data is a string
        if (data['previousBlockHash'] && !(typeof data['previousBlockHash'] === 'string' || data['previousBlockHash'] instanceof String)) {
            throw new Error("Expected the field `previousBlockHash` to be a primitive type in the JSON string but got " + data['previousBlockHash']);
        }
        if (data['txs']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['txs'])) {
                throw new Error("Expected the field `txs` to be an array in the JSON data but got " + data['txs']);
            }
            // validate the optional field `txs` (array)
            for (const item of data['txs']) {
                GetBlockV2200ResponseTxsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} bits
 */
GetBlockV2200Response.prototype['bits'] = undefined;

/**
 * @member {Number} confirmations
 */
GetBlockV2200Response.prototype['confirmations'] = undefined;

/**
 * @member {String} difficulty
 */
GetBlockV2200Response.prototype['difficulty'] = undefined;

/**
 * @member {String} hash
 */
GetBlockV2200Response.prototype['hash'] = undefined;

/**
 * @member {Number} height
 */
GetBlockV2200Response.prototype['height'] = undefined;

/**
 * @member {Number} itemsOnPage
 */
GetBlockV2200Response.prototype['itemsOnPage'] = undefined;

/**
 * @member {String} merkleRoot
 */
GetBlockV2200Response.prototype['merkleRoot'] = undefined;

/**
 * @member {String} nextBlockHash
 */
GetBlockV2200Response.prototype['nextBlockHash'] = undefined;

/**
 * @member {String} nonce
 */
GetBlockV2200Response.prototype['nonce'] = undefined;

/**
 * @member {Number} page
 */
GetBlockV2200Response.prototype['page'] = undefined;

/**
 * @member {String} previousBlockHash
 */
GetBlockV2200Response.prototype['previousBlockHash'] = undefined;

/**
 * @member {Number} size
 */
GetBlockV2200Response.prototype['size'] = undefined;

/**
 * @member {Number} time
 */
GetBlockV2200Response.prototype['time'] = undefined;

/**
 * @member {Number} totalPages
 */
GetBlockV2200Response.prototype['totalPages'] = undefined;

/**
 * @member {Number} txCount
 */
GetBlockV2200Response.prototype['txCount'] = undefined;

/**
 * @member {Array.<module:model/GetBlockV2200ResponseTxsInner>} txs
 */
GetBlockV2200Response.prototype['txs'] = undefined;

/**
 * @member {Number} version
 */
GetBlockV2200Response.prototype['version'] = undefined;






export default GetBlockV2200Response;

