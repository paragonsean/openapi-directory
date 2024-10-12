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
 * The CatalogDataProductLinkExtensionInterface model module.
 * @module model/CatalogDataProductLinkExtensionInterface
 * @version 2.2.10
 */
class CatalogDataProductLinkExtensionInterface {
    /**
     * Constructs a new <code>CatalogDataProductLinkExtensionInterface</code>.
     * ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductLinkInterface
     * @alias module:model/CatalogDataProductLinkExtensionInterface
     */
    constructor() { 
        
        CatalogDataProductLinkExtensionInterface.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CatalogDataProductLinkExtensionInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogDataProductLinkExtensionInterface} obj Optional instance to populate.
     * @return {module:model/CatalogDataProductLinkExtensionInterface} The populated <code>CatalogDataProductLinkExtensionInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogDataProductLinkExtensionInterface();

            if (data.hasOwnProperty('qty')) {
                obj['qty'] = ApiClient.convertToType(data['qty'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogDataProductLinkExtensionInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogDataProductLinkExtensionInterface</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Number} qty
 */
CatalogDataProductLinkExtensionInterface.prototype['qty'] = undefined;






export default CatalogDataProductLinkExtensionInterface;

