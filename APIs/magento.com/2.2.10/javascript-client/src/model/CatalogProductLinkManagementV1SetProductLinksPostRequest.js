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
import CatalogDataProductLinkInterface from './CatalogDataProductLinkInterface';

/**
 * The CatalogProductLinkManagementV1SetProductLinksPostRequest model module.
 * @module model/CatalogProductLinkManagementV1SetProductLinksPostRequest
 * @version 2.2.10
 */
class CatalogProductLinkManagementV1SetProductLinksPostRequest {
    /**
     * Constructs a new <code>CatalogProductLinkManagementV1SetProductLinksPostRequest</code>.
     * @alias module:model/CatalogProductLinkManagementV1SetProductLinksPostRequest
     * @param items {Array.<module:model/CatalogDataProductLinkInterface>} 
     */
    constructor(items) { 
        
        CatalogProductLinkManagementV1SetProductLinksPostRequest.initialize(this, items);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, items) { 
        obj['items'] = items;
    }

    /**
     * Constructs a <code>CatalogProductLinkManagementV1SetProductLinksPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogProductLinkManagementV1SetProductLinksPostRequest} obj Optional instance to populate.
     * @return {module:model/CatalogProductLinkManagementV1SetProductLinksPostRequest} The populated <code>CatalogProductLinkManagementV1SetProductLinksPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogProductLinkManagementV1SetProductLinksPostRequest();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [CatalogDataProductLinkInterface]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogProductLinkManagementV1SetProductLinksPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogProductLinkManagementV1SetProductLinksPostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CatalogProductLinkManagementV1SetProductLinksPostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                CatalogDataProductLinkInterface.validateJSON(item);
            };
        }

        return true;
    }


}

CatalogProductLinkManagementV1SetProductLinksPostRequest.RequiredProperties = ["items"];

/**
 * @member {Array.<module:model/CatalogDataProductLinkInterface>} items
 */
CatalogProductLinkManagementV1SetProductLinksPostRequest.prototype['items'] = undefined;






export default CatalogProductLinkManagementV1SetProductLinksPostRequest;

