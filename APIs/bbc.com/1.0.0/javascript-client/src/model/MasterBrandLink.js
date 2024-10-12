/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import MasterBrandLinkMasterBrand from './MasterBrandLinkMasterBrand';

/**
 * The MasterBrandLink model module.
 * @module model/MasterBrandLink
 * @version 1.0.0
 */
class MasterBrandLink {
    /**
     * Constructs a new <code>MasterBrandLink</code>.
     * @alias module:model/MasterBrandLink
     * @param masterBrand {module:model/MasterBrandLinkMasterBrand} 
     */
    constructor(masterBrand) { 
        
        MasterBrandLink.initialize(this, masterBrand);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, masterBrand) { 
        obj['master_brand'] = masterBrand;
    }

    /**
     * Constructs a <code>MasterBrandLink</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MasterBrandLink} obj Optional instance to populate.
     * @return {module:model/MasterBrandLink} The populated <code>MasterBrandLink</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MasterBrandLink();

            if (data.hasOwnProperty('master_brand')) {
                obj['master_brand'] = MasterBrandLinkMasterBrand.constructFromObject(data['master_brand']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MasterBrandLink</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MasterBrandLink</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of MasterBrandLink.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `master_brand`
        if (data['master_brand']) { // data not null
          MasterBrandLinkMasterBrand.validateJSON(data['master_brand']);
        }

        return true;
    }


}

MasterBrandLink.RequiredProperties = ["master_brand"];

/**
 * @member {module:model/MasterBrandLinkMasterBrand} master_brand
 */
MasterBrandLink.prototype['master_brand'] = undefined;






export default MasterBrandLink;

