/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The MoneyObject model module.
 * @module model/MoneyObject
 * @version v1
 */
class MoneyObject {
    /**
     * Constructs a new <code>MoneyObject</code>.
     * Provides information about a value of money. 
     * @alias module:model/MoneyObject
     * @param currencyCode {String} The ISO 4217 currency code. 
     * @param value {String} The amount of money, formatted as a string in the relevant currency. For example, for an Australian dollar value of $10.56, this field will be `\"10.56\"`. The currency symbol is not included in the string. 
     * @param valueInBaseUnits {Number} The amount of money in the smallest denomination for the currency, as a 64-bit integer.  For example, for an Australian dollar value of $10.56, this field will be `1056`. 
     */
    constructor(currencyCode, value, valueInBaseUnits) { 
        
        MoneyObject.initialize(this, currencyCode, value, valueInBaseUnits);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, currencyCode, value, valueInBaseUnits) { 
        obj['currencyCode'] = currencyCode;
        obj['value'] = value;
        obj['valueInBaseUnits'] = valueInBaseUnits;
    }

    /**
     * Constructs a <code>MoneyObject</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MoneyObject} obj Optional instance to populate.
     * @return {module:model/MoneyObject} The populated <code>MoneyObject</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MoneyObject();

            if (data.hasOwnProperty('currencyCode')) {
                obj['currencyCode'] = ApiClient.convertToType(data['currencyCode'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
            if (data.hasOwnProperty('valueInBaseUnits')) {
                obj['valueInBaseUnits'] = ApiClient.convertToType(data['valueInBaseUnits'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MoneyObject</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MoneyObject</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of MoneyObject.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['currencyCode'] && !(typeof data['currencyCode'] === 'string' || data['currencyCode'] instanceof String)) {
            throw new Error("Expected the field `currencyCode` to be a primitive type in the JSON string but got " + data['currencyCode']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}

MoneyObject.RequiredProperties = ["currencyCode", "value", "valueInBaseUnits"];

/**
 * The ISO 4217 currency code. 
 * @member {String} currencyCode
 */
MoneyObject.prototype['currencyCode'] = undefined;

/**
 * The amount of money, formatted as a string in the relevant currency. For example, for an Australian dollar value of $10.56, this field will be `\"10.56\"`. The currency symbol is not included in the string. 
 * @member {String} value
 */
MoneyObject.prototype['value'] = undefined;

/**
 * The amount of money in the smallest denomination for the currency, as a 64-bit integer.  For example, for an Australian dollar value of $10.56, this field will be `1056`. 
 * @member {Number} valueInBaseUnits
 */
MoneyObject.prototype['valueInBaseUnits'] = undefined;






export default MoneyObject;

