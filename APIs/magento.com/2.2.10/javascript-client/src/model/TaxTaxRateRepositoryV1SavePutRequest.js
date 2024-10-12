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
import TaxDataTaxRateInterface from './TaxDataTaxRateInterface';

/**
 * The TaxTaxRateRepositoryV1SavePutRequest model module.
 * @module model/TaxTaxRateRepositoryV1SavePutRequest
 * @version 2.2.10
 */
class TaxTaxRateRepositoryV1SavePutRequest {
    /**
     * Constructs a new <code>TaxTaxRateRepositoryV1SavePutRequest</code>.
     * @alias module:model/TaxTaxRateRepositoryV1SavePutRequest
     * @param taxRate {module:model/TaxDataTaxRateInterface} 
     */
    constructor(taxRate) { 
        
        TaxTaxRateRepositoryV1SavePutRequest.initialize(this, taxRate);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, taxRate) { 
        obj['taxRate'] = taxRate;
    }

    /**
     * Constructs a <code>TaxTaxRateRepositoryV1SavePutRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TaxTaxRateRepositoryV1SavePutRequest} obj Optional instance to populate.
     * @return {module:model/TaxTaxRateRepositoryV1SavePutRequest} The populated <code>TaxTaxRateRepositoryV1SavePutRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TaxTaxRateRepositoryV1SavePutRequest();

            if (data.hasOwnProperty('taxRate')) {
                obj['taxRate'] = TaxDataTaxRateInterface.constructFromObject(data['taxRate']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TaxTaxRateRepositoryV1SavePutRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TaxTaxRateRepositoryV1SavePutRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TaxTaxRateRepositoryV1SavePutRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `taxRate`
        if (data['taxRate']) { // data not null
          TaxDataTaxRateInterface.validateJSON(data['taxRate']);
        }

        return true;
    }


}

TaxTaxRateRepositoryV1SavePutRequest.RequiredProperties = ["taxRate"];

/**
 * @member {module:model/TaxDataTaxRateInterface} taxRate
 */
TaxTaxRateRepositoryV1SavePutRequest.prototype['taxRate'] = undefined;






export default TaxTaxRateRepositoryV1SavePutRequest;

