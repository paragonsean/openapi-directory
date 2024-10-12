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
import GetAddressInfoResponseUtxosInner from './GetAddressInfoResponseUtxosInner';

/**
 * The GetAddressInfoResponse model module.
 * @module model/GetAddressInfoResponse
 * @version 1.3.0
 */
class GetAddressInfoResponse {
    /**
     * Constructs a new <code>GetAddressInfoResponse</code>.
     * @alias module:model/GetAddressInfoResponse
     */
    constructor() { 
        
        GetAddressInfoResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetAddressInfoResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetAddressInfoResponse} obj Optional instance to populate.
     * @return {module:model/GetAddressInfoResponse} The populated <code>GetAddressInfoResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetAddressInfoResponse();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
            if (data.hasOwnProperty('utxos')) {
                obj['utxos'] = ApiClient.convertToType(data['utxos'], [GetAddressInfoResponseUtxosInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetAddressInfoResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetAddressInfoResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['address'] && !(typeof data['address'] === 'string' || data['address'] instanceof String)) {
            throw new Error("Expected the field `address` to be a primitive type in the JSON string but got " + data['address']);
        }
        if (data['utxos']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['utxos'])) {
                throw new Error("Expected the field `utxos` to be an array in the JSON data but got " + data['utxos']);
            }
            // validate the optional field `utxos` (array)
            for (const item of data['utxos']) {
                GetAddressInfoResponseUtxosInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The Neblio Address
 * @member {String} address
 */
GetAddressInfoResponse.prototype['address'] = undefined;

/**
 * Array of UTXOs held at this address.
 * @member {Array.<module:model/GetAddressInfoResponseUtxosInner>} utxos
 */
GetAddressInfoResponse.prototype['utxos'] = undefined;






export default GetAddressInfoResponse;

