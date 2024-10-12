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
 * The SalesDataInvoiceItemCreationInterface model module.
 * @module model/SalesDataInvoiceItemCreationInterface
 * @version 2.2.10
 */
class SalesDataInvoiceItemCreationInterface {
    /**
     * Constructs a new <code>SalesDataInvoiceItemCreationInterface</code>.
     * Input argument for invoice creation Interface InvoiceItemCreationInterface
     * @alias module:model/SalesDataInvoiceItemCreationInterface
     * @param orderItemId {Number} Order item ID.
     * @param qty {Number} Quantity.
     */
    constructor(orderItemId, qty) { 
        
        SalesDataInvoiceItemCreationInterface.initialize(this, orderItemId, qty);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, orderItemId, qty) { 
        obj['order_item_id'] = orderItemId;
        obj['qty'] = qty;
    }

    /**
     * Constructs a <code>SalesDataInvoiceItemCreationInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesDataInvoiceItemCreationInterface} obj Optional instance to populate.
     * @return {module:model/SalesDataInvoiceItemCreationInterface} The populated <code>SalesDataInvoiceItemCreationInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesDataInvoiceItemCreationInterface();

            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('order_item_id')) {
                obj['order_item_id'] = ApiClient.convertToType(data['order_item_id'], 'Number');
            }
            if (data.hasOwnProperty('qty')) {
                obj['qty'] = ApiClient.convertToType(data['qty'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SalesDataInvoiceItemCreationInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesDataInvoiceItemCreationInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SalesDataInvoiceItemCreationInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

SalesDataInvoiceItemCreationInterface.RequiredProperties = ["order_item_id", "qty"];

/**
 * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\InvoiceItemCreationInterface
 * @member {Object} extension_attributes
 */
SalesDataInvoiceItemCreationInterface.prototype['extension_attributes'] = undefined;

/**
 * Order item ID.
 * @member {Number} order_item_id
 */
SalesDataInvoiceItemCreationInterface.prototype['order_item_id'] = undefined;

/**
 * Quantity.
 * @member {Number} qty
 */
SalesDataInvoiceItemCreationInterface.prototype['qty'] = undefined;






export default SalesDataInvoiceItemCreationInterface;

