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
import BundleDataOptionInterface from './BundleDataOptionInterface';
import CatalogDataCategoryLinkInterface from './CatalogDataCategoryLinkInterface';
import CatalogInventoryDataStockItemInterface from './CatalogInventoryDataStockItemInterface';
import ConfigurableProductDataOptionInterface from './ConfigurableProductDataOptionInterface';
import DownloadableDataLinkInterface from './DownloadableDataLinkInterface';
import DownloadableDataSampleInterface from './DownloadableDataSampleInterface';
import GiftCardDataGiftcardAmountInterface from './GiftCardDataGiftcardAmountInterface';

/**
 * The CatalogDataProductExtensionInterface model module.
 * @module model/CatalogDataProductExtensionInterface
 * @version 2.2.10
 */
class CatalogDataProductExtensionInterface {
    /**
     * Constructs a new <code>CatalogDataProductExtensionInterface</code>.
     * ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductInterface
     * @alias module:model/CatalogDataProductExtensionInterface
     */
    constructor() { 
        
        CatalogDataProductExtensionInterface.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CatalogDataProductExtensionInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogDataProductExtensionInterface} obj Optional instance to populate.
     * @return {module:model/CatalogDataProductExtensionInterface} The populated <code>CatalogDataProductExtensionInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogDataProductExtensionInterface();

            if (data.hasOwnProperty('bundle_product_options')) {
                obj['bundle_product_options'] = ApiClient.convertToType(data['bundle_product_options'], [BundleDataOptionInterface]);
            }
            if (data.hasOwnProperty('category_links')) {
                obj['category_links'] = ApiClient.convertToType(data['category_links'], [CatalogDataCategoryLinkInterface]);
            }
            if (data.hasOwnProperty('configurable_product_links')) {
                obj['configurable_product_links'] = ApiClient.convertToType(data['configurable_product_links'], ['Number']);
            }
            if (data.hasOwnProperty('configurable_product_options')) {
                obj['configurable_product_options'] = ApiClient.convertToType(data['configurable_product_options'], [ConfigurableProductDataOptionInterface]);
            }
            if (data.hasOwnProperty('downloadable_product_links')) {
                obj['downloadable_product_links'] = ApiClient.convertToType(data['downloadable_product_links'], [DownloadableDataLinkInterface]);
            }
            if (data.hasOwnProperty('downloadable_product_samples')) {
                obj['downloadable_product_samples'] = ApiClient.convertToType(data['downloadable_product_samples'], [DownloadableDataSampleInterface]);
            }
            if (data.hasOwnProperty('giftcard_amounts')) {
                obj['giftcard_amounts'] = ApiClient.convertToType(data['giftcard_amounts'], [GiftCardDataGiftcardAmountInterface]);
            }
            if (data.hasOwnProperty('stock_item')) {
                obj['stock_item'] = CatalogInventoryDataStockItemInterface.constructFromObject(data['stock_item']);
            }
            if (data.hasOwnProperty('website_ids')) {
                obj['website_ids'] = ApiClient.convertToType(data['website_ids'], ['Number']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogDataProductExtensionInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogDataProductExtensionInterface</code>.
     */
    static validateJSON(data) {
        if (data['bundle_product_options']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['bundle_product_options'])) {
                throw new Error("Expected the field `bundle_product_options` to be an array in the JSON data but got " + data['bundle_product_options']);
            }
            // validate the optional field `bundle_product_options` (array)
            for (const item of data['bundle_product_options']) {
                BundleDataOptionInterface.validateJSON(item);
            };
        }
        if (data['category_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['category_links'])) {
                throw new Error("Expected the field `category_links` to be an array in the JSON data but got " + data['category_links']);
            }
            // validate the optional field `category_links` (array)
            for (const item of data['category_links']) {
                CatalogDataCategoryLinkInterface.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['configurable_product_links'])) {
            throw new Error("Expected the field `configurable_product_links` to be an array in the JSON data but got " + data['configurable_product_links']);
        }
        if (data['configurable_product_options']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['configurable_product_options'])) {
                throw new Error("Expected the field `configurable_product_options` to be an array in the JSON data but got " + data['configurable_product_options']);
            }
            // validate the optional field `configurable_product_options` (array)
            for (const item of data['configurable_product_options']) {
                ConfigurableProductDataOptionInterface.validateJSON(item);
            };
        }
        if (data['downloadable_product_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['downloadable_product_links'])) {
                throw new Error("Expected the field `downloadable_product_links` to be an array in the JSON data but got " + data['downloadable_product_links']);
            }
            // validate the optional field `downloadable_product_links` (array)
            for (const item of data['downloadable_product_links']) {
                DownloadableDataLinkInterface.validateJSON(item);
            };
        }
        if (data['downloadable_product_samples']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['downloadable_product_samples'])) {
                throw new Error("Expected the field `downloadable_product_samples` to be an array in the JSON data but got " + data['downloadable_product_samples']);
            }
            // validate the optional field `downloadable_product_samples` (array)
            for (const item of data['downloadable_product_samples']) {
                DownloadableDataSampleInterface.validateJSON(item);
            };
        }
        if (data['giftcard_amounts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['giftcard_amounts'])) {
                throw new Error("Expected the field `giftcard_amounts` to be an array in the JSON data but got " + data['giftcard_amounts']);
            }
            // validate the optional field `giftcard_amounts` (array)
            for (const item of data['giftcard_amounts']) {
                GiftCardDataGiftcardAmountInterface.validateJSON(item);
            };
        }
        // validate the optional field `stock_item`
        if (data['stock_item']) { // data not null
          CatalogInventoryDataStockItemInterface.validateJSON(data['stock_item']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['website_ids'])) {
            throw new Error("Expected the field `website_ids` to be an array in the JSON data but got " + data['website_ids']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/BundleDataOptionInterface>} bundle_product_options
 */
CatalogDataProductExtensionInterface.prototype['bundle_product_options'] = undefined;

/**
 * @member {Array.<module:model/CatalogDataCategoryLinkInterface>} category_links
 */
CatalogDataProductExtensionInterface.prototype['category_links'] = undefined;

/**
 * @member {Array.<Number>} configurable_product_links
 */
CatalogDataProductExtensionInterface.prototype['configurable_product_links'] = undefined;

/**
 * @member {Array.<module:model/ConfigurableProductDataOptionInterface>} configurable_product_options
 */
CatalogDataProductExtensionInterface.prototype['configurable_product_options'] = undefined;

/**
 * @member {Array.<module:model/DownloadableDataLinkInterface>} downloadable_product_links
 */
CatalogDataProductExtensionInterface.prototype['downloadable_product_links'] = undefined;

/**
 * @member {Array.<module:model/DownloadableDataSampleInterface>} downloadable_product_samples
 */
CatalogDataProductExtensionInterface.prototype['downloadable_product_samples'] = undefined;

/**
 * @member {Array.<module:model/GiftCardDataGiftcardAmountInterface>} giftcard_amounts
 */
CatalogDataProductExtensionInterface.prototype['giftcard_amounts'] = undefined;

/**
 * @member {module:model/CatalogInventoryDataStockItemInterface} stock_item
 */
CatalogDataProductExtensionInterface.prototype['stock_item'] = undefined;

/**
 * @member {Array.<Number>} website_ids
 */
CatalogDataProductExtensionInterface.prototype['website_ids'] = undefined;






export default CatalogDataProductExtensionInterface;

