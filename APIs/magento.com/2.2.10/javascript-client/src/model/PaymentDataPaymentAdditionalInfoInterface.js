/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PaymentDataPaymentAdditionalInfoInterface model module.
 * @module model/PaymentDataPaymentAdditionalInfoInterface
 * @version 2.2.10
 */
class PaymentDataPaymentAdditionalInfoInterface {
    /**
     * Constructs a new <code>PaymentDataPaymentAdditionalInfoInterface</code>.
     * Payment additional info interface.
     * @alias module:model/PaymentDataPaymentAdditionalInfoInterface
     * @param key {String} Object key
     * @param value {String} Object value
     */
    constructor(key, value) { 
        
        PaymentDataPaymentAdditionalInfoInterface.initialize(this, key, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, key, value) { 
        obj['key'] = key;
        obj['value'] = value;
    }

    /**
     * Constructs a <code>PaymentDataPaymentAdditionalInfoInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaymentDataPaymentAdditionalInfoInterface} obj Optional instance to populate.
     * @return {module:model/PaymentDataPaymentAdditionalInfoInterface} The populated <code>PaymentDataPaymentAdditionalInfoInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PaymentDataPaymentAdditionalInfoInterface();

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
     * Validates the JSON data with respect to <code>PaymentDataPaymentAdditionalInfoInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PaymentDataPaymentAdditionalInfoInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PaymentDataPaymentAdditionalInfoInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
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

PaymentDataPaymentAdditionalInfoInterface.RequiredProperties = ["key", "value"];

/**
 * Object key
 * @member {String} key
 */
PaymentDataPaymentAdditionalInfoInterface.prototype['key'] = undefined;

/**
 * Object value
 * @member {String} value
 */
PaymentDataPaymentAdditionalInfoInterface.prototype['value'] = undefined;






export default PaymentDataPaymentAdditionalInfoInterface;

