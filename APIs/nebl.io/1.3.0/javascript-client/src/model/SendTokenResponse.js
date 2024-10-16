/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The SendTokenResponse model module.
 * @module model/SendTokenResponse
 * @version 1.3.0
 */
class SendTokenResponse {
    /**
     * Constructs a new <code>SendTokenResponse</code>.
     * @alias module:model/SendTokenResponse
     */
    constructor() { 
        
        SendTokenResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SendTokenResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SendTokenResponse} obj Optional instance to populate.
     * @return {module:model/SendTokenResponse} The populated <code>SendTokenResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SendTokenResponse();

            if (data.hasOwnProperty('multisigOutputs')) {
                obj['multisigOutputs'] = ApiClient.convertToType(data['multisigOutputs'], ['Number']);
            }
            if (data.hasOwnProperty('ntp1OutputIndexes')) {
                obj['ntp1OutputIndexes'] = ApiClient.convertToType(data['ntp1OutputIndexes'], ['Number']);
            }
            if (data.hasOwnProperty('txHex')) {
                obj['txHex'] = ApiClient.convertToType(data['txHex'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SendTokenResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SendTokenResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['multisigOutputs'])) {
            throw new Error("Expected the field `multisigOutputs` to be an array in the JSON data but got " + data['multisigOutputs']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['ntp1OutputIndexes'])) {
            throw new Error("Expected the field `ntp1OutputIndexes` to be an array in the JSON data but got " + data['ntp1OutputIndexes']);
        }
        // ensure the json data is a string
        if (data['txHex'] && !(typeof data['txHex'] === 'string' || data['txHex'] instanceof String)) {
            throw new Error("Expected the field `txHex` to be a primitive type in the JSON string but got " + data['txHex']);
        }

        return true;
    }


}



/**
 * Array of indexes of multisig outputs
 * @member {Array.<Number>} multisigOutputs
 */
SendTokenResponse.prototype['multisigOutputs'] = undefined;

/**
 * Array of indexes transfering NTP1 tokens
 * @member {Array.<Number>} ntp1OutputIndexes
 */
SendTokenResponse.prototype['ntp1OutputIndexes'] = undefined;

/**
 * Unsigned, raw transaction hex of the transaction to send the token
 * @member {String} txHex
 */
SendTokenResponse.prototype['txHex'] = undefined;






export default SendTokenResponse;

