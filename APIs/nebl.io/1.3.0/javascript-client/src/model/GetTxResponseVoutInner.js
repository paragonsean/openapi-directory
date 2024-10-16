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
import GetTransactionInfoResponseVinInnerPreviousOutput from './GetTransactionInfoResponseVinInnerPreviousOutput';

/**
 * The GetTxResponseVoutInner model module.
 * @module model/GetTxResponseVoutInner
 * @version 1.3.0
 */
class GetTxResponseVoutInner {
    /**
     * Constructs a new <code>GetTxResponseVoutInner</code>.
     * @alias module:model/GetTxResponseVoutInner
     */
    constructor() { 
        
        GetTxResponseVoutInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetTxResponseVoutInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetTxResponseVoutInner} obj Optional instance to populate.
     * @return {module:model/GetTxResponseVoutInner} The populated <code>GetTxResponseVoutInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetTxResponseVoutInner();

            if (data.hasOwnProperty('blockheight')) {
                obj['blockheight'] = ApiClient.convertToType(data['blockheight'], 'Number');
            }
            if (data.hasOwnProperty('n')) {
                obj['n'] = ApiClient.convertToType(data['n'], 'Number');
            }
            if (data.hasOwnProperty('scriptPubKey')) {
                obj['scriptPubKey'] = GetTransactionInfoResponseVinInnerPreviousOutput.constructFromObject(data['scriptPubKey']);
            }
            if (data.hasOwnProperty('used')) {
                obj['used'] = ApiClient.convertToType(data['used'], 'Boolean');
            }
            if (data.hasOwnProperty('usedBlockheight')) {
                obj['usedBlockheight'] = ApiClient.convertToType(data['usedBlockheight'], 'Number');
            }
            if (data.hasOwnProperty('usedTxid')) {
                obj['usedTxid'] = ApiClient.convertToType(data['usedTxid'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetTxResponseVoutInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetTxResponseVoutInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `scriptPubKey`
        if (data['scriptPubKey']) { // data not null
          GetTransactionInfoResponseVinInnerPreviousOutput.validateJSON(data['scriptPubKey']);
        }
        // ensure the json data is a string
        if (data['usedTxid'] && !(typeof data['usedTxid'] === 'string' || data['usedTxid'] instanceof String)) {
            throw new Error("Expected the field `usedTxid` to be a primitive type in the JSON string but got " + data['usedTxid']);
        }

        return true;
    }


}



/**
 * Blockheight of this transaction
 * @member {Number} blockheight
 */
GetTxResponseVoutInner.prototype['blockheight'] = undefined;

/**
 * Output index
 * @member {Number} n
 */
GetTxResponseVoutInner.prototype['n'] = undefined;

/**
 * @member {module:model/GetTransactionInfoResponseVinInnerPreviousOutput} scriptPubKey
 */
GetTxResponseVoutInner.prototype['scriptPubKey'] = undefined;

/**
 * Whether this output has now been used
 * @member {Boolean} used
 */
GetTxResponseVoutInner.prototype['used'] = undefined;

/**
 * Blockheight this output was used in
 * @member {Number} usedBlockheight
 */
GetTxResponseVoutInner.prototype['usedBlockheight'] = undefined;

/**
 * TXID this output was used in
 * @member {String} usedTxid
 */
GetTxResponseVoutInner.prototype['usedTxid'] = undefined;

/**
 * Value of the output in NEBL
 * @member {Number} value
 */
GetTxResponseVoutInner.prototype['value'] = undefined;






export default GetTxResponseVoutInner;

