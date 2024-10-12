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
import CatalogDataProductWebsiteLinkInterface from './CatalogDataProductWebsiteLinkInterface';

/**
 * The CatalogProductWebsiteLinkRepositoryV1SavePutRequest model module.
 * @module model/CatalogProductWebsiteLinkRepositoryV1SavePutRequest
 * @version 2.2.10
 */
class CatalogProductWebsiteLinkRepositoryV1SavePutRequest {
    /**
     * Constructs a new <code>CatalogProductWebsiteLinkRepositoryV1SavePutRequest</code>.
     * @alias module:model/CatalogProductWebsiteLinkRepositoryV1SavePutRequest
     * @param productWebsiteLink {module:model/CatalogDataProductWebsiteLinkInterface} 
     */
    constructor(productWebsiteLink) { 
        
        CatalogProductWebsiteLinkRepositoryV1SavePutRequest.initialize(this, productWebsiteLink);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, productWebsiteLink) { 
        obj['productWebsiteLink'] = productWebsiteLink;
    }

    /**
     * Constructs a <code>CatalogProductWebsiteLinkRepositoryV1SavePutRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogProductWebsiteLinkRepositoryV1SavePutRequest} obj Optional instance to populate.
     * @return {module:model/CatalogProductWebsiteLinkRepositoryV1SavePutRequest} The populated <code>CatalogProductWebsiteLinkRepositoryV1SavePutRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogProductWebsiteLinkRepositoryV1SavePutRequest();

            if (data.hasOwnProperty('productWebsiteLink')) {
                obj['productWebsiteLink'] = CatalogDataProductWebsiteLinkInterface.constructFromObject(data['productWebsiteLink']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogProductWebsiteLinkRepositoryV1SavePutRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogProductWebsiteLinkRepositoryV1SavePutRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CatalogProductWebsiteLinkRepositoryV1SavePutRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `productWebsiteLink`
        if (data['productWebsiteLink']) { // data not null
          CatalogDataProductWebsiteLinkInterface.validateJSON(data['productWebsiteLink']);
        }

        return true;
    }


}

CatalogProductWebsiteLinkRepositoryV1SavePutRequest.RequiredProperties = ["productWebsiteLink"];

/**
 * @member {module:model/CatalogDataProductWebsiteLinkInterface} productWebsiteLink
 */
CatalogProductWebsiteLinkRepositoryV1SavePutRequest.prototype['productWebsiteLink'] = undefined;






export default CatalogProductWebsiteLinkRepositoryV1SavePutRequest;

