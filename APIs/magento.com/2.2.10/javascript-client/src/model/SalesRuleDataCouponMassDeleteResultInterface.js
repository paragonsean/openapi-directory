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
 * The SalesRuleDataCouponMassDeleteResultInterface model module.
 * @module model/SalesRuleDataCouponMassDeleteResultInterface
 * @version 2.2.10
 */
class SalesRuleDataCouponMassDeleteResultInterface {
    /**
     * Constructs a new <code>SalesRuleDataCouponMassDeleteResultInterface</code>.
     * Coupon mass delete results interface.
     * @alias module:model/SalesRuleDataCouponMassDeleteResultInterface
     * @param failedItems {Array.<String>} List of failed items.
     * @param missingItems {Array.<String>} List of missing items.
     */
    constructor(failedItems, missingItems) { 
        
        SalesRuleDataCouponMassDeleteResultInterface.initialize(this, failedItems, missingItems);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, failedItems, missingItems) { 
        obj['failed_items'] = failedItems;
        obj['missing_items'] = missingItems;
    }

    /**
     * Constructs a <code>SalesRuleDataCouponMassDeleteResultInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesRuleDataCouponMassDeleteResultInterface} obj Optional instance to populate.
     * @return {module:model/SalesRuleDataCouponMassDeleteResultInterface} The populated <code>SalesRuleDataCouponMassDeleteResultInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesRuleDataCouponMassDeleteResultInterface();

            if (data.hasOwnProperty('failed_items')) {
                obj['failed_items'] = ApiClient.convertToType(data['failed_items'], ['String']);
            }
            if (data.hasOwnProperty('missing_items')) {
                obj['missing_items'] = ApiClient.convertToType(data['missing_items'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SalesRuleDataCouponMassDeleteResultInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesRuleDataCouponMassDeleteResultInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SalesRuleDataCouponMassDeleteResultInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['failed_items'])) {
            throw new Error("Expected the field `failed_items` to be an array in the JSON data but got " + data['failed_items']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['missing_items'])) {
            throw new Error("Expected the field `missing_items` to be an array in the JSON data but got " + data['missing_items']);
        }

        return true;
    }


}

SalesRuleDataCouponMassDeleteResultInterface.RequiredProperties = ["failed_items", "missing_items"];

/**
 * List of failed items.
 * @member {Array.<String>} failed_items
 */
SalesRuleDataCouponMassDeleteResultInterface.prototype['failed_items'] = undefined;

/**
 * List of missing items.
 * @member {Array.<String>} missing_items
 */
SalesRuleDataCouponMassDeleteResultInterface.prototype['missing_items'] = undefined;






export default SalesRuleDataCouponMassDeleteResultInterface;

