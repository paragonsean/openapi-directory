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
 * The GetEstimateFeeV2200Response model module.
 * @module model/GetEstimateFeeV2200Response
 * @version 2.0
 */
class GetEstimateFeeV2200Response {
    /**
     * Constructs a new <code>GetEstimateFeeV2200Response</code>.
     * @alias module:model/GetEstimateFeeV2200Response
     */
    constructor() { 
        
        GetEstimateFeeV2200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetEstimateFeeV2200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetEstimateFeeV2200Response} obj Optional instance to populate.
     * @return {module:model/GetEstimateFeeV2200Response} The populated <code>GetEstimateFeeV2200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetEstimateFeeV2200Response();

            if (data.hasOwnProperty('result')) {
                obj['result'] = ApiClient.convertToType(data['result'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetEstimateFeeV2200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetEstimateFeeV2200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['result'] && !(typeof data['result'] === 'string' || data['result'] instanceof String)) {
            throw new Error("Expected the field `result` to be a primitive type in the JSON string but got " + data['result']);
        }

        return true;
    }


}



/**
 * @member {String} result
 */
GetEstimateFeeV2200Response.prototype['result'] = undefined;






export default GetEstimateFeeV2200Response;

