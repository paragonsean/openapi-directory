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
import GetNFTMetaV2200ResponseContractInfo from './GetNFTMetaV2200ResponseContractInfo';

/**
 * The GetNFTMetaV2200Response model module.
 * @module model/GetNFTMetaV2200Response
 * @version 2.0
 */
class GetNFTMetaV2200Response {
    /**
     * Constructs a new <code>GetNFTMetaV2200Response</code>.
     * @alias module:model/GetNFTMetaV2200Response
     */
    constructor() { 
        
        GetNFTMetaV2200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNFTMetaV2200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNFTMetaV2200Response} obj Optional instance to populate.
     * @return {module:model/GetNFTMetaV2200Response} The populated <code>GetNFTMetaV2200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNFTMetaV2200Response();

            if (data.hasOwnProperty('contractInfo')) {
                obj['contractInfo'] = GetNFTMetaV2200ResponseContractInfo.constructFromObject(data['contractInfo']);
            }
            if (data.hasOwnProperty('tokenId')) {
                obj['tokenId'] = ApiClient.convertToType(data['tokenId'], 'String');
            }
            if (data.hasOwnProperty('uri')) {
                obj['uri'] = ApiClient.convertToType(data['uri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNFTMetaV2200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNFTMetaV2200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `contractInfo`
        if (data['contractInfo']) { // data not null
          GetNFTMetaV2200ResponseContractInfo.validateJSON(data['contractInfo']);
        }
        // ensure the json data is a string
        if (data['tokenId'] && !(typeof data['tokenId'] === 'string' || data['tokenId'] instanceof String)) {
            throw new Error("Expected the field `tokenId` to be a primitive type in the JSON string but got " + data['tokenId']);
        }
        // ensure the json data is a string
        if (data['uri'] && !(typeof data['uri'] === 'string' || data['uri'] instanceof String)) {
            throw new Error("Expected the field `uri` to be a primitive type in the JSON string but got " + data['uri']);
        }

        return true;
    }


}



/**
 * @member {module:model/GetNFTMetaV2200ResponseContractInfo} contractInfo
 */
GetNFTMetaV2200Response.prototype['contractInfo'] = undefined;

/**
 * @member {String} tokenId
 */
GetNFTMetaV2200Response.prototype['tokenId'] = undefined;

/**
 * @member {String} uri
 */
GetNFTMetaV2200Response.prototype['uri'] = undefined;






export default GetNFTMetaV2200Response;

