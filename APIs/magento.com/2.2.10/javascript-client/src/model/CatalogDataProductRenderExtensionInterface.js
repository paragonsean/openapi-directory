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
import CatalogDataProductRenderButtonInterface from './CatalogDataProductRenderButtonInterface';

/**
 * The CatalogDataProductRenderExtensionInterface model module.
 * @module model/CatalogDataProductRenderExtensionInterface
 * @version 2.2.10
 */
class CatalogDataProductRenderExtensionInterface {
    /**
     * Constructs a new <code>CatalogDataProductRenderExtensionInterface</code>.
     * ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductRenderInterface
     * @alias module:model/CatalogDataProductRenderExtensionInterface
     */
    constructor() { 
        
        CatalogDataProductRenderExtensionInterface.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CatalogDataProductRenderExtensionInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogDataProductRenderExtensionInterface} obj Optional instance to populate.
     * @return {module:model/CatalogDataProductRenderExtensionInterface} The populated <code>CatalogDataProductRenderExtensionInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogDataProductRenderExtensionInterface();

            if (data.hasOwnProperty('review_html')) {
                obj['review_html'] = ApiClient.convertToType(data['review_html'], 'String');
            }
            if (data.hasOwnProperty('wishlist_button')) {
                obj['wishlist_button'] = CatalogDataProductRenderButtonInterface.constructFromObject(data['wishlist_button']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogDataProductRenderExtensionInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogDataProductRenderExtensionInterface</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['review_html'] && !(typeof data['review_html'] === 'string' || data['review_html'] instanceof String)) {
            throw new Error("Expected the field `review_html` to be a primitive type in the JSON string but got " + data['review_html']);
        }
        // validate the optional field `wishlist_button`
        if (data['wishlist_button']) { // data not null
          CatalogDataProductRenderButtonInterface.validateJSON(data['wishlist_button']);
        }

        return true;
    }


}



/**
 * @member {String} review_html
 */
CatalogDataProductRenderExtensionInterface.prototype['review_html'] = undefined;

/**
 * @member {module:model/CatalogDataProductRenderButtonInterface} wishlist_button
 */
CatalogDataProductRenderExtensionInterface.prototype['wishlist_button'] = undefined;






export default CatalogDataProductRenderExtensionInterface;

