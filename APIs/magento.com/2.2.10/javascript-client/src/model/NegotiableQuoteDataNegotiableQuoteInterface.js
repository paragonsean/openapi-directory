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
 * The NegotiableQuoteDataNegotiableQuoteInterface model module.
 * @module model/NegotiableQuoteDataNegotiableQuoteInterface
 * @version 2.2.10
 */
class NegotiableQuoteDataNegotiableQuoteInterface {
    /**
     * Constructs a new <code>NegotiableQuoteDataNegotiableQuoteInterface</code>.
     * Interface NegotiableQuoteInterface
     * @alias module:model/NegotiableQuoteDataNegotiableQuoteInterface
     * @param appliedRuleIds {String} Quote rules.
     * @param creatorId {Number} Quote creator id.
     * @param creatorType {Number} Quote creator type.
     * @param deletedSku {String} Deleted products sku.
     * @param emailNotificationStatus {Number} Email notification status.
     * @param expirationPeriod {String} Expiration period.
     * @param hasUnconfirmedChanges {Boolean} Has unconfirmed changes.
     * @param isAddressDraft {Boolean} Is address draft.
     * @param isCustomerPriceChanged {Boolean} Customer price changes.
     * @param isRegularQuote {Boolean} Is regular quote.
     * @param isShippingTaxChanged {Boolean} Shipping tax changes.
     * @param negotiatedPriceType {Number} Negotiated price type.
     * @param negotiatedPriceValue {Number} Negotiated price value.
     * @param notifications {Number} Quote notifications.
     * @param quoteId {Number} Negotiable quote ID.
     * @param quoteName {String} Negotiable quote name.
     * @param shippingPrice {Number} Proposed shipping price.
     * @param status {String} Negotiable quote status.
     */
    constructor(appliedRuleIds, creatorId, creatorType, deletedSku, emailNotificationStatus, expirationPeriod, hasUnconfirmedChanges, isAddressDraft, isCustomerPriceChanged, isRegularQuote, isShippingTaxChanged, negotiatedPriceType, negotiatedPriceValue, notifications, quoteId, quoteName, shippingPrice, status) { 
        
        NegotiableQuoteDataNegotiableQuoteInterface.initialize(this, appliedRuleIds, creatorId, creatorType, deletedSku, emailNotificationStatus, expirationPeriod, hasUnconfirmedChanges, isAddressDraft, isCustomerPriceChanged, isRegularQuote, isShippingTaxChanged, negotiatedPriceType, negotiatedPriceValue, notifications, quoteId, quoteName, shippingPrice, status);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, appliedRuleIds, creatorId, creatorType, deletedSku, emailNotificationStatus, expirationPeriod, hasUnconfirmedChanges, isAddressDraft, isCustomerPriceChanged, isRegularQuote, isShippingTaxChanged, negotiatedPriceType, negotiatedPriceValue, notifications, quoteId, quoteName, shippingPrice, status) { 
        obj['applied_rule_ids'] = appliedRuleIds;
        obj['creator_id'] = creatorId;
        obj['creator_type'] = creatorType;
        obj['deleted_sku'] = deletedSku;
        obj['email_notification_status'] = emailNotificationStatus;
        obj['expiration_period'] = expirationPeriod;
        obj['has_unconfirmed_changes'] = hasUnconfirmedChanges;
        obj['is_address_draft'] = isAddressDraft;
        obj['is_customer_price_changed'] = isCustomerPriceChanged;
        obj['is_regular_quote'] = isRegularQuote;
        obj['is_shipping_tax_changed'] = isShippingTaxChanged;
        obj['negotiated_price_type'] = negotiatedPriceType;
        obj['negotiated_price_value'] = negotiatedPriceValue;
        obj['notifications'] = notifications;
        obj['quote_id'] = quoteId;
        obj['quote_name'] = quoteName;
        obj['shipping_price'] = shippingPrice;
        obj['status'] = status;
    }

    /**
     * Constructs a <code>NegotiableQuoteDataNegotiableQuoteInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NegotiableQuoteDataNegotiableQuoteInterface} obj Optional instance to populate.
     * @return {module:model/NegotiableQuoteDataNegotiableQuoteInterface} The populated <code>NegotiableQuoteDataNegotiableQuoteInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NegotiableQuoteDataNegotiableQuoteInterface();

            if (data.hasOwnProperty('applied_rule_ids')) {
                obj['applied_rule_ids'] = ApiClient.convertToType(data['applied_rule_ids'], 'String');
            }
            if (data.hasOwnProperty('base_negotiated_total_price')) {
                obj['base_negotiated_total_price'] = ApiClient.convertToType(data['base_negotiated_total_price'], 'Number');
            }
            if (data.hasOwnProperty('base_original_total_price')) {
                obj['base_original_total_price'] = ApiClient.convertToType(data['base_original_total_price'], 'Number');
            }
            if (data.hasOwnProperty('creator_id')) {
                obj['creator_id'] = ApiClient.convertToType(data['creator_id'], 'Number');
            }
            if (data.hasOwnProperty('creator_type')) {
                obj['creator_type'] = ApiClient.convertToType(data['creator_type'], 'Number');
            }
            if (data.hasOwnProperty('deleted_sku')) {
                obj['deleted_sku'] = ApiClient.convertToType(data['deleted_sku'], 'String');
            }
            if (data.hasOwnProperty('email_notification_status')) {
                obj['email_notification_status'] = ApiClient.convertToType(data['email_notification_status'], 'Number');
            }
            if (data.hasOwnProperty('expiration_period')) {
                obj['expiration_period'] = ApiClient.convertToType(data['expiration_period'], 'String');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('has_unconfirmed_changes')) {
                obj['has_unconfirmed_changes'] = ApiClient.convertToType(data['has_unconfirmed_changes'], 'Boolean');
            }
            if (data.hasOwnProperty('is_address_draft')) {
                obj['is_address_draft'] = ApiClient.convertToType(data['is_address_draft'], 'Boolean');
            }
            if (data.hasOwnProperty('is_customer_price_changed')) {
                obj['is_customer_price_changed'] = ApiClient.convertToType(data['is_customer_price_changed'], 'Boolean');
            }
            if (data.hasOwnProperty('is_regular_quote')) {
                obj['is_regular_quote'] = ApiClient.convertToType(data['is_regular_quote'], 'Boolean');
            }
            if (data.hasOwnProperty('is_shipping_tax_changed')) {
                obj['is_shipping_tax_changed'] = ApiClient.convertToType(data['is_shipping_tax_changed'], 'Boolean');
            }
            if (data.hasOwnProperty('negotiated_price_type')) {
                obj['negotiated_price_type'] = ApiClient.convertToType(data['negotiated_price_type'], 'Number');
            }
            if (data.hasOwnProperty('negotiated_price_value')) {
                obj['negotiated_price_value'] = ApiClient.convertToType(data['negotiated_price_value'], 'Number');
            }
            if (data.hasOwnProperty('negotiated_total_price')) {
                obj['negotiated_total_price'] = ApiClient.convertToType(data['negotiated_total_price'], 'Number');
            }
            if (data.hasOwnProperty('notifications')) {
                obj['notifications'] = ApiClient.convertToType(data['notifications'], 'Number');
            }
            if (data.hasOwnProperty('original_total_price')) {
                obj['original_total_price'] = ApiClient.convertToType(data['original_total_price'], 'Number');
            }
            if (data.hasOwnProperty('quote_id')) {
                obj['quote_id'] = ApiClient.convertToType(data['quote_id'], 'Number');
            }
            if (data.hasOwnProperty('quote_name')) {
                obj['quote_name'] = ApiClient.convertToType(data['quote_name'], 'String');
            }
            if (data.hasOwnProperty('shipping_price')) {
                obj['shipping_price'] = ApiClient.convertToType(data['shipping_price'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NegotiableQuoteDataNegotiableQuoteInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NegotiableQuoteDataNegotiableQuoteInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NegotiableQuoteDataNegotiableQuoteInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['applied_rule_ids'] && !(typeof data['applied_rule_ids'] === 'string' || data['applied_rule_ids'] instanceof String)) {
            throw new Error("Expected the field `applied_rule_ids` to be a primitive type in the JSON string but got " + data['applied_rule_ids']);
        }
        // ensure the json data is a string
        if (data['deleted_sku'] && !(typeof data['deleted_sku'] === 'string' || data['deleted_sku'] instanceof String)) {
            throw new Error("Expected the field `deleted_sku` to be a primitive type in the JSON string but got " + data['deleted_sku']);
        }
        // ensure the json data is a string
        if (data['expiration_period'] && !(typeof data['expiration_period'] === 'string' || data['expiration_period'] instanceof String)) {
            throw new Error("Expected the field `expiration_period` to be a primitive type in the JSON string but got " + data['expiration_period']);
        }
        // ensure the json data is a string
        if (data['quote_name'] && !(typeof data['quote_name'] === 'string' || data['quote_name'] instanceof String)) {
            throw new Error("Expected the field `quote_name` to be a primitive type in the JSON string but got " + data['quote_name']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

NegotiableQuoteDataNegotiableQuoteInterface.RequiredProperties = ["applied_rule_ids", "creator_id", "creator_type", "deleted_sku", "email_notification_status", "expiration_period", "has_unconfirmed_changes", "is_address_draft", "is_customer_price_changed", "is_regular_quote", "is_shipping_tax_changed", "negotiated_price_type", "negotiated_price_value", "notifications", "quote_id", "quote_name", "shipping_price", "status"];

/**
 * Quote rules.
 * @member {String} applied_rule_ids
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['applied_rule_ids'] = undefined;

/**
 * Quote negotiated total price in base currency.
 * @member {Number} base_negotiated_total_price
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['base_negotiated_total_price'] = undefined;

/**
 * Quote original total price in base currency.
 * @member {Number} base_original_total_price
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['base_original_total_price'] = undefined;

/**
 * Quote creator id.
 * @member {Number} creator_id
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['creator_id'] = undefined;

/**
 * Quote creator type.
 * @member {Number} creator_type
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['creator_type'] = undefined;

/**
 * Deleted products sku.
 * @member {String} deleted_sku
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['deleted_sku'] = undefined;

/**
 * Email notification status.
 * @member {Number} email_notification_status
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['email_notification_status'] = undefined;

/**
 * Expiration period.
 * @member {String} expiration_period
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['expiration_period'] = undefined;

/**
 * ExtensionInterface class for @see \\Magento\\NegotiableQuote\\Api\\Data\\NegotiableQuoteInterface
 * @member {Object} extension_attributes
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['extension_attributes'] = undefined;

/**
 * Has unconfirmed changes.
 * @member {Boolean} has_unconfirmed_changes
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['has_unconfirmed_changes'] = undefined;

/**
 * Is address draft.
 * @member {Boolean} is_address_draft
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['is_address_draft'] = undefined;

/**
 * Customer price changes.
 * @member {Boolean} is_customer_price_changed
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['is_customer_price_changed'] = undefined;

/**
 * Is regular quote.
 * @member {Boolean} is_regular_quote
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['is_regular_quote'] = undefined;

/**
 * Shipping tax changes.
 * @member {Boolean} is_shipping_tax_changed
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['is_shipping_tax_changed'] = undefined;

/**
 * Negotiated price type.
 * @member {Number} negotiated_price_type
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['negotiated_price_type'] = undefined;

/**
 * Negotiated price value.
 * @member {Number} negotiated_price_value
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['negotiated_price_value'] = undefined;

/**
 * Quote negotiated total price.
 * @member {Number} negotiated_total_price
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['negotiated_total_price'] = undefined;

/**
 * Quote notifications.
 * @member {Number} notifications
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['notifications'] = undefined;

/**
 * Quote original total price.
 * @member {Number} original_total_price
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['original_total_price'] = undefined;

/**
 * Negotiable quote ID.
 * @member {Number} quote_id
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['quote_id'] = undefined;

/**
 * Negotiable quote name.
 * @member {String} quote_name
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['quote_name'] = undefined;

/**
 * Proposed shipping price.
 * @member {Number} shipping_price
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['shipping_price'] = undefined;

/**
 * Negotiable quote status.
 * @member {String} status
 */
NegotiableQuoteDataNegotiableQuoteInterface.prototype['status'] = undefined;






export default NegotiableQuoteDataNegotiableQuoteInterface;

