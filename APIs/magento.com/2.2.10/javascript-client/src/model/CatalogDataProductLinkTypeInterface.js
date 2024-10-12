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
 * The CatalogDataProductLinkTypeInterface model module.
 * @module model/CatalogDataProductLinkTypeInterface
 * @version 2.2.10
 */
class CatalogDataProductLinkTypeInterface {
    /**
     * Constructs a new <code>CatalogDataProductLinkTypeInterface</code>.
     * 
     * @alias module:model/CatalogDataProductLinkTypeInterface
     * @param code {Number} Link type code
     * @param name {String} Link type name
     */
    constructor(code, name) { 
        
        CatalogDataProductLinkTypeInterface.initialize(this, code, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, code, name) { 
        obj['code'] = code;
        obj['name'] = name;
    }

    /**
     * Constructs a <code>CatalogDataProductLinkTypeInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogDataProductLinkTypeInterface} obj Optional instance to populate.
     * @return {module:model/CatalogDataProductLinkTypeInterface} The populated <code>CatalogDataProductLinkTypeInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogDataProductLinkTypeInterface();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'Number');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogDataProductLinkTypeInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogDataProductLinkTypeInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CatalogDataProductLinkTypeInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

CatalogDataProductLinkTypeInterface.RequiredProperties = ["code", "name"];

/**
 * Link type code
 * @member {Number} code
 */
CatalogDataProductLinkTypeInterface.prototype['code'] = undefined;

/**
 * ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductLinkTypeInterface
 * @member {Object} extension_attributes
 */
CatalogDataProductLinkTypeInterface.prototype['extension_attributes'] = undefined;

/**
 * Link type name
 * @member {String} name
 */
CatalogDataProductLinkTypeInterface.prototype['name'] = undefined;






export default CatalogDataProductLinkTypeInterface;

