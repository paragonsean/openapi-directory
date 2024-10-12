/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ConversationsConversationIdOfferPostRequestShippingPrice model module.
 * @module model/ConversationsConversationIdOfferPostRequestShippingPrice
 * @version 3.0
 */
class ConversationsConversationIdOfferPostRequestShippingPrice {
    /**
     * Constructs a new <code>ConversationsConversationIdOfferPostRequestShippingPrice</code>.
     * Shipping price (sellers only)
     * @alias module:model/ConversationsConversationIdOfferPostRequestShippingPrice
     * @param amount {String} The amount of money being expressed, as a POSIX-compliant decimal number
     * @param currency {module:model/ConversationsConversationIdOfferPostRequestShippingPrice.CurrencyEnum} The currency the money will be expressed in
     */
    constructor(amount, currency) { 
        
        ConversationsConversationIdOfferPostRequestShippingPrice.initialize(this, amount, currency);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, amount, currency) { 
        obj['amount'] = amount;
        obj['currency'] = currency;
    }

    /**
     * Constructs a <code>ConversationsConversationIdOfferPostRequestShippingPrice</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConversationsConversationIdOfferPostRequestShippingPrice} obj Optional instance to populate.
     * @return {module:model/ConversationsConversationIdOfferPostRequestShippingPrice} The populated <code>ConversationsConversationIdOfferPostRequestShippingPrice</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConversationsConversationIdOfferPostRequestShippingPrice();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConversationsConversationIdOfferPostRequestShippingPrice</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConversationsConversationIdOfferPostRequestShippingPrice</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConversationsConversationIdOfferPostRequestShippingPrice.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['amount'] && !(typeof data['amount'] === 'string' || data['amount'] instanceof String)) {
            throw new Error("Expected the field `amount` to be a primitive type in the JSON string but got " + data['amount']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }

        return true;
    }


}

ConversationsConversationIdOfferPostRequestShippingPrice.RequiredProperties = ["amount", "currency"];

/**
 * The amount of money being expressed, as a POSIX-compliant decimal number
 * @member {String} amount
 */
ConversationsConversationIdOfferPostRequestShippingPrice.prototype['amount'] = undefined;

/**
 * The currency the money will be expressed in
 * @member {module:model/ConversationsConversationIdOfferPostRequestShippingPrice.CurrencyEnum} currency
 */
ConversationsConversationIdOfferPostRequestShippingPrice.prototype['currency'] = undefined;





/**
 * Allowed values for the <code>currency</code> property.
 * @enum {String}
 * @readonly
 */
ConversationsConversationIdOfferPostRequestShippingPrice['CurrencyEnum'] = {

    /**
     * value: "USD"
     * @const
     */
    "USD": "USD",

    /**
     * value: "CAD"
     * @const
     */
    "CAD": "CAD",

    /**
     * value: "EUR"
     * @const
     */
    "EUR": "EUR",

    /**
     * value: "GBP"
     * @const
     */
    "GBP": "GBP",

    /**
     * value: "AUD"
     * @const
     */
    "AUD": "AUD",

    /**
     * value: "JPY"
     * @const
     */
    "JPY": "JPY",

    /**
     * value: "NZD"
     * @const
     */
    "NZD": "NZD",

    /**
     * value: "MXN"
     * @const
     */
    "MXN": "MXN"
};



export default ConversationsConversationIdOfferPostRequestShippingPrice;

