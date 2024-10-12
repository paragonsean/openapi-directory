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
import SharedCatalogDataSharedCatalogInterface from './SharedCatalogDataSharedCatalogInterface';

/**
 * The SharedCatalogSharedCatalogRepositoryV1SavePostRequest model module.
 * @module model/SharedCatalogSharedCatalogRepositoryV1SavePostRequest
 * @version 2.2.10
 */
class SharedCatalogSharedCatalogRepositoryV1SavePostRequest {
    /**
     * Constructs a new <code>SharedCatalogSharedCatalogRepositoryV1SavePostRequest</code>.
     * @alias module:model/SharedCatalogSharedCatalogRepositoryV1SavePostRequest
     * @param sharedCatalog {module:model/SharedCatalogDataSharedCatalogInterface} 
     */
    constructor(sharedCatalog) { 
        
        SharedCatalogSharedCatalogRepositoryV1SavePostRequest.initialize(this, sharedCatalog);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, sharedCatalog) { 
        obj['sharedCatalog'] = sharedCatalog;
    }

    /**
     * Constructs a <code>SharedCatalogSharedCatalogRepositoryV1SavePostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SharedCatalogSharedCatalogRepositoryV1SavePostRequest} obj Optional instance to populate.
     * @return {module:model/SharedCatalogSharedCatalogRepositoryV1SavePostRequest} The populated <code>SharedCatalogSharedCatalogRepositoryV1SavePostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SharedCatalogSharedCatalogRepositoryV1SavePostRequest();

            if (data.hasOwnProperty('sharedCatalog')) {
                obj['sharedCatalog'] = SharedCatalogDataSharedCatalogInterface.constructFromObject(data['sharedCatalog']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SharedCatalogSharedCatalogRepositoryV1SavePostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SharedCatalogSharedCatalogRepositoryV1SavePostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SharedCatalogSharedCatalogRepositoryV1SavePostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `sharedCatalog`
        if (data['sharedCatalog']) { // data not null
          SharedCatalogDataSharedCatalogInterface.validateJSON(data['sharedCatalog']);
        }

        return true;
    }


}

SharedCatalogSharedCatalogRepositoryV1SavePostRequest.RequiredProperties = ["sharedCatalog"];

/**
 * @member {module:model/SharedCatalogDataSharedCatalogInterface} sharedCatalog
 */
SharedCatalogSharedCatalogRepositoryV1SavePostRequest.prototype['sharedCatalog'] = undefined;






export default SharedCatalogSharedCatalogRepositoryV1SavePostRequest;

