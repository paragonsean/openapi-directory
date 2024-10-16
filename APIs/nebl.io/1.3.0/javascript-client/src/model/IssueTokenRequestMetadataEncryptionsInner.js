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
 * The IssueTokenRequestMetadataEncryptionsInner model module.
 * @module model/IssueTokenRequestMetadataEncryptionsInner
 * @version 1.3.0
 */
class IssueTokenRequestMetadataEncryptionsInner {
    /**
     * Constructs a new <code>IssueTokenRequestMetadataEncryptionsInner</code>.
     * @alias module:model/IssueTokenRequestMetadataEncryptionsInner
     */
    constructor() { 
        
        IssueTokenRequestMetadataEncryptionsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IssueTokenRequestMetadataEncryptionsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IssueTokenRequestMetadataEncryptionsInner} obj Optional instance to populate.
     * @return {module:model/IssueTokenRequestMetadataEncryptionsInner} The populated <code>IssueTokenRequestMetadataEncryptionsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IssueTokenRequestMetadataEncryptionsInner();

            if (data.hasOwnProperty('format')) {
                obj['format'] = ApiClient.convertToType(data['format'], 'String');
            }
            if (data.hasOwnProperty('key')) {
                obj['key'] = ApiClient.convertToType(data['key'], 'String');
            }
            if (data.hasOwnProperty('pubkey')) {
                obj['pubkey'] = ApiClient.convertToType(data['pubkey'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IssueTokenRequestMetadataEncryptionsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IssueTokenRequestMetadataEncryptionsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['format'] && !(typeof data['format'] === 'string' || data['format'] instanceof String)) {
            throw new Error("Expected the field `format` to be a primitive type in the JSON string but got " + data['format']);
        }
        // ensure the json data is a string
        if (data['key'] && !(typeof data['key'] === 'string' || data['key'] instanceof String)) {
            throw new Error("Expected the field `key` to be a primitive type in the JSON string but got " + data['key']);
        }
        // ensure the json data is a string
        if (data['pubkey'] && !(typeof data['pubkey'] === 'string' || data['pubkey'] instanceof String)) {
            throw new Error("Expected the field `pubkey` to be a primitive type in the JSON string but got " + data['pubkey']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * key format (pem or der)
 * @member {String} format
 */
IssueTokenRequestMetadataEncryptionsInner.prototype['format'] = undefined;

/**
 * userData key to encrypt
 * @member {String} key
 */
IssueTokenRequestMetadataEncryptionsInner.prototype['key'] = undefined;

/**
 * RSA public key used for encryption
 * @member {String} pubkey
 */
IssueTokenRequestMetadataEncryptionsInner.prototype['pubkey'] = undefined;

/**
 * pkcs1 or pkcs8
 * @member {String} type
 */
IssueTokenRequestMetadataEncryptionsInner.prototype['type'] = undefined;






export default IssueTokenRequestMetadataEncryptionsInner;

