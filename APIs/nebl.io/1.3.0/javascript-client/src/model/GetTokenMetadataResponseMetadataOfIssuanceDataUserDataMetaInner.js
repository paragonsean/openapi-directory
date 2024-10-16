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
 * The GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner model module.
 * @module model/GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner
 * @version 1.3.0
 */
class GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner {
    /**
     * Constructs a new <code>GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner</code>.
     * @alias module:model/GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner
     */
    constructor() { 
        
        GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner} obj Optional instance to populate.
     * @return {module:model/GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner} The populated <code>GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner();

            if (data.hasOwnProperty('key')) {
                obj['key'] = ApiClient.convertToType(data['key'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['key'] && !(typeof data['key'] === 'string' || data['key'] instanceof String)) {
            throw new Error("Expected the field `key` to be a primitive type in the JSON string but got " + data['key']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * @member {String} key
 */
GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner.prototype['key'] = undefined;

/**
 * @member {String} value
 */
GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner.prototype['value'] = undefined;






export default GetTokenMetadataResponseMetadataOfIssuanceDataUserDataMetaInner;

