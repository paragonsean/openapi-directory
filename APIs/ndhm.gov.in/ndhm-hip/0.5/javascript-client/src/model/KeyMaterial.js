/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import KeyObject from './KeyObject';

/**
 * The KeyMaterial model module.
 * @module model/KeyMaterial
 * @version 0.5
 */
class KeyMaterial {
    /**
     * Constructs a new <code>KeyMaterial</code>.
     * @alias module:model/KeyMaterial
     * @param cryptoAlg {String} 
     * @param curve {String} 
     * @param dhPublicKey {module:model/KeyObject} 
     * @param nonce {String} 
     */
    constructor(cryptoAlg, curve, dhPublicKey, nonce) { 
        
        KeyMaterial.initialize(this, cryptoAlg, curve, dhPublicKey, nonce);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, cryptoAlg, curve, dhPublicKey, nonce) { 
        obj['cryptoAlg'] = cryptoAlg;
        obj['curve'] = curve;
        obj['dhPublicKey'] = dhPublicKey;
        obj['nonce'] = nonce;
    }

    /**
     * Constructs a <code>KeyMaterial</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/KeyMaterial} obj Optional instance to populate.
     * @return {module:model/KeyMaterial} The populated <code>KeyMaterial</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new KeyMaterial();

            if (data.hasOwnProperty('cryptoAlg')) {
                obj['cryptoAlg'] = ApiClient.convertToType(data['cryptoAlg'], 'String');
            }
            if (data.hasOwnProperty('curve')) {
                obj['curve'] = ApiClient.convertToType(data['curve'], 'String');
            }
            if (data.hasOwnProperty('dhPublicKey')) {
                obj['dhPublicKey'] = KeyObject.constructFromObject(data['dhPublicKey']);
            }
            if (data.hasOwnProperty('nonce')) {
                obj['nonce'] = ApiClient.convertToType(data['nonce'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>KeyMaterial</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>KeyMaterial</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of KeyMaterial.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['cryptoAlg'] && !(typeof data['cryptoAlg'] === 'string' || data['cryptoAlg'] instanceof String)) {
            throw new Error("Expected the field `cryptoAlg` to be a primitive type in the JSON string but got " + data['cryptoAlg']);
        }
        // ensure the json data is a string
        if (data['curve'] && !(typeof data['curve'] === 'string' || data['curve'] instanceof String)) {
            throw new Error("Expected the field `curve` to be a primitive type in the JSON string but got " + data['curve']);
        }
        // validate the optional field `dhPublicKey`
        if (data['dhPublicKey']) { // data not null
          KeyObject.validateJSON(data['dhPublicKey']);
        }
        // ensure the json data is a string
        if (data['nonce'] && !(typeof data['nonce'] === 'string' || data['nonce'] instanceof String)) {
            throw new Error("Expected the field `nonce` to be a primitive type in the JSON string but got " + data['nonce']);
        }

        return true;
    }


}

KeyMaterial.RequiredProperties = ["cryptoAlg", "curve", "dhPublicKey", "nonce"];

/**
 * @member {String} cryptoAlg
 */
KeyMaterial.prototype['cryptoAlg'] = undefined;

/**
 * @member {String} curve
 */
KeyMaterial.prototype['curve'] = undefined;

/**
 * @member {module:model/KeyObject} dhPublicKey
 */
KeyMaterial.prototype['dhPublicKey'] = undefined;

/**
 * @member {String} nonce
 */
KeyMaterial.prototype['nonce'] = undefined;






export default KeyMaterial;

