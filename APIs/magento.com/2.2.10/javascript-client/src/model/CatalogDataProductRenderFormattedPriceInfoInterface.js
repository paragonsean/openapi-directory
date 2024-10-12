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
 * The CatalogDataProductRenderFormattedPriceInfoInterface model module.
 * @module model/CatalogDataProductRenderFormattedPriceInfoInterface
 * @version 2.2.10
 */
class CatalogDataProductRenderFormattedPriceInfoInterface {
    /**
     * Constructs a new <code>CatalogDataProductRenderFormattedPriceInfoInterface</code>.
     * Formatted Price interface. Aggregate formatted html with price representations. E.g.: &lt;span class&#x3D;\&quot;price\&quot;&gt;$9.00&lt;/span&gt; Consider currency, rounding and html
     * @alias module:model/CatalogDataProductRenderFormattedPriceInfoInterface
     * @param finalPrice {String} Html with final price
     * @param maxPrice {String} Max price of a product
     * @param maxRegularPrice {String} Max regular price
     * @param minimalPrice {String} The minimal price of the product or variation
     * @param minimalRegularPrice {String} Minimal regular price
     * @param regularPrice {String} Price - is price of product without discounts and special price with taxes and fixed product tax
     * @param specialPrice {String} Special price
     */
    constructor(finalPrice, maxPrice, maxRegularPrice, minimalPrice, minimalRegularPrice, regularPrice, specialPrice) { 
        
        CatalogDataProductRenderFormattedPriceInfoInterface.initialize(this, finalPrice, maxPrice, maxRegularPrice, minimalPrice, minimalRegularPrice, regularPrice, specialPrice);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, finalPrice, maxPrice, maxRegularPrice, minimalPrice, minimalRegularPrice, regularPrice, specialPrice) { 
        obj['final_price'] = finalPrice;
        obj['max_price'] = maxPrice;
        obj['max_regular_price'] = maxRegularPrice;
        obj['minimal_price'] = minimalPrice;
        obj['minimal_regular_price'] = minimalRegularPrice;
        obj['regular_price'] = regularPrice;
        obj['special_price'] = specialPrice;
    }

    /**
     * Constructs a <code>CatalogDataProductRenderFormattedPriceInfoInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogDataProductRenderFormattedPriceInfoInterface} obj Optional instance to populate.
     * @return {module:model/CatalogDataProductRenderFormattedPriceInfoInterface} The populated <code>CatalogDataProductRenderFormattedPriceInfoInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogDataProductRenderFormattedPriceInfoInterface();

            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('final_price')) {
                obj['final_price'] = ApiClient.convertToType(data['final_price'], 'String');
            }
            if (data.hasOwnProperty('max_price')) {
                obj['max_price'] = ApiClient.convertToType(data['max_price'], 'String');
            }
            if (data.hasOwnProperty('max_regular_price')) {
                obj['max_regular_price'] = ApiClient.convertToType(data['max_regular_price'], 'String');
            }
            if (data.hasOwnProperty('minimal_price')) {
                obj['minimal_price'] = ApiClient.convertToType(data['minimal_price'], 'String');
            }
            if (data.hasOwnProperty('minimal_regular_price')) {
                obj['minimal_regular_price'] = ApiClient.convertToType(data['minimal_regular_price'], 'String');
            }
            if (data.hasOwnProperty('regular_price')) {
                obj['regular_price'] = ApiClient.convertToType(data['regular_price'], 'String');
            }
            if (data.hasOwnProperty('special_price')) {
                obj['special_price'] = ApiClient.convertToType(data['special_price'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogDataProductRenderFormattedPriceInfoInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogDataProductRenderFormattedPriceInfoInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CatalogDataProductRenderFormattedPriceInfoInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['final_price'] && !(typeof data['final_price'] === 'string' || data['final_price'] instanceof String)) {
            throw new Error("Expected the field `final_price` to be a primitive type in the JSON string but got " + data['final_price']);
        }
        // ensure the json data is a string
        if (data['max_price'] && !(typeof data['max_price'] === 'string' || data['max_price'] instanceof String)) {
            throw new Error("Expected the field `max_price` to be a primitive type in the JSON string but got " + data['max_price']);
        }
        // ensure the json data is a string
        if (data['max_regular_price'] && !(typeof data['max_regular_price'] === 'string' || data['max_regular_price'] instanceof String)) {
            throw new Error("Expected the field `max_regular_price` to be a primitive type in the JSON string but got " + data['max_regular_price']);
        }
        // ensure the json data is a string
        if (data['minimal_price'] && !(typeof data['minimal_price'] === 'string' || data['minimal_price'] instanceof String)) {
            throw new Error("Expected the field `minimal_price` to be a primitive type in the JSON string but got " + data['minimal_price']);
        }
        // ensure the json data is a string
        if (data['minimal_regular_price'] && !(typeof data['minimal_regular_price'] === 'string' || data['minimal_regular_price'] instanceof String)) {
            throw new Error("Expected the field `minimal_regular_price` to be a primitive type in the JSON string but got " + data['minimal_regular_price']);
        }
        // ensure the json data is a string
        if (data['regular_price'] && !(typeof data['regular_price'] === 'string' || data['regular_price'] instanceof String)) {
            throw new Error("Expected the field `regular_price` to be a primitive type in the JSON string but got " + data['regular_price']);
        }
        // ensure the json data is a string
        if (data['special_price'] && !(typeof data['special_price'] === 'string' || data['special_price'] instanceof String)) {
            throw new Error("Expected the field `special_price` to be a primitive type in the JSON string but got " + data['special_price']);
        }

        return true;
    }


}

CatalogDataProductRenderFormattedPriceInfoInterface.RequiredProperties = ["final_price", "max_price", "max_regular_price", "minimal_price", "minimal_regular_price", "regular_price", "special_price"];

/**
 * ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductRender\\FormattedPriceInfoInterface
 * @member {Object} extension_attributes
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['extension_attributes'] = undefined;

/**
 * Html with final price
 * @member {String} final_price
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['final_price'] = undefined;

/**
 * Max price of a product
 * @member {String} max_price
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['max_price'] = undefined;

/**
 * Max regular price
 * @member {String} max_regular_price
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['max_regular_price'] = undefined;

/**
 * The minimal price of the product or variation
 * @member {String} minimal_price
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['minimal_price'] = undefined;

/**
 * Minimal regular price
 * @member {String} minimal_regular_price
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['minimal_regular_price'] = undefined;

/**
 * Price - is price of product without discounts and special price with taxes and fixed product tax
 * @member {String} regular_price
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['regular_price'] = undefined;

/**
 * Special price
 * @member {String} special_price
 */
CatalogDataProductRenderFormattedPriceInfoInterface.prototype['special_price'] = undefined;






export default CatalogDataProductRenderFormattedPriceInfoInterface;

