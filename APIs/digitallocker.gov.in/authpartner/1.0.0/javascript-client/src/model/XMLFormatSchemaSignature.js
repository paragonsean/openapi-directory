/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import XMLFormatSchemaSignatureKeyInfo from './XMLFormatSchemaSignatureKeyInfo';

/**
 * The XMLFormatSchemaSignature model module.
 * @module model/XMLFormatSchemaSignature
 * @version 1.0.0
 */
class XMLFormatSchemaSignature {
    /**
     * Constructs a new <code>XMLFormatSchemaSignature</code>.
     * @alias module:model/XMLFormatSchemaSignature
     * @param keyInfo {module:model/XMLFormatSchemaSignatureKeyInfo} 
     */
    constructor(keyInfo) { 
        
        XMLFormatSchemaSignature.initialize(this, keyInfo);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, keyInfo) { 
        obj['KeyInfo'] = keyInfo;
    }

    /**
     * Constructs a <code>XMLFormatSchemaSignature</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/XMLFormatSchemaSignature} obj Optional instance to populate.
     * @return {module:model/XMLFormatSchemaSignature} The populated <code>XMLFormatSchemaSignature</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new XMLFormatSchemaSignature();

            if (data.hasOwnProperty('KeyInfo')) {
                obj['KeyInfo'] = XMLFormatSchemaSignatureKeyInfo.constructFromObject(data['KeyInfo']);
            }
            if (data.hasOwnProperty('SignatureValue')) {
                obj['SignatureValue'] = ApiClient.convertToType(data['SignatureValue'], Object);
            }
            if (data.hasOwnProperty('SignedInfo')) {
                obj['SignedInfo'] = ApiClient.convertToType(data['SignedInfo'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>XMLFormatSchemaSignature</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>XMLFormatSchemaSignature</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of XMLFormatSchemaSignature.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `KeyInfo`
        if (data['KeyInfo']) { // data not null
          XMLFormatSchemaSignatureKeyInfo.validateJSON(data['KeyInfo']);
        }

        return true;
    }


}

XMLFormatSchemaSignature.RequiredProperties = ["KeyInfo"];

/**
 * @member {module:model/XMLFormatSchemaSignatureKeyInfo} KeyInfo
 */
XMLFormatSchemaSignature.prototype['KeyInfo'] = undefined;

/**
 * @member {Object} SignatureValue
 */
XMLFormatSchemaSignature.prototype['SignatureValue'] = undefined;

/**
 * @member {Object} SignedInfo
 */
XMLFormatSchemaSignature.prototype['SignedInfo'] = undefined;






export default XMLFormatSchemaSignature;

