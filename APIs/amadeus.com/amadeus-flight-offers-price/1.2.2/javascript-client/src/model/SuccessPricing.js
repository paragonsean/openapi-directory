/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Dictionaries from './Dictionaries';
import FlightOfferPricingOut from './FlightOfferPricingOut';
import IncludedResourcesMap from './IncludedResourcesMap';
import Issue from './Issue';

/**
 * The SuccessPricing model module.
 * @module model/SuccessPricing
 * @version 1.2.2
 */
class SuccessPricing {
    /**
     * Constructs a new <code>SuccessPricing</code>.
     * @alias module:model/SuccessPricing
     * @param data {module:model/FlightOfferPricingOut} 
     */
    constructor(data) { 
        
        SuccessPricing.initialize(this, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data) { 
        obj['data'] = data;
    }

    /**
     * Constructs a <code>SuccessPricing</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SuccessPricing} obj Optional instance to populate.
     * @return {module:model/SuccessPricing} The populated <code>SuccessPricing</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SuccessPricing();

            if (data.hasOwnProperty('data')) {
                obj['data'] = FlightOfferPricingOut.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('dictionaries')) {
                obj['dictionaries'] = Dictionaries.constructFromObject(data['dictionaries']);
            }
            if (data.hasOwnProperty('included')) {
                obj['included'] = IncludedResourcesMap.constructFromObject(data['included']);
            }
            if (data.hasOwnProperty('warnings')) {
                obj['warnings'] = ApiClient.convertToType(data['warnings'], [Issue]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SuccessPricing</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SuccessPricing</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SuccessPricing.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          FlightOfferPricingOut.validateJSON(data['data']);
        }
        // validate the optional field `dictionaries`
        if (data['dictionaries']) { // data not null
          Dictionaries.validateJSON(data['dictionaries']);
        }
        // validate the optional field `included`
        if (data['included']) { // data not null
          IncludedResourcesMap.validateJSON(data['included']);
        }
        if (data['warnings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['warnings'])) {
                throw new Error("Expected the field `warnings` to be an array in the JSON data but got " + data['warnings']);
            }
            // validate the optional field `warnings` (array)
            for (const item of data['warnings']) {
                Issue.validateJSON(item);
            };
        }

        return true;
    }


}

SuccessPricing.RequiredProperties = ["data"];

/**
 * @member {module:model/FlightOfferPricingOut} data
 */
SuccessPricing.prototype['data'] = undefined;

/**
 * @member {module:model/Dictionaries} dictionaries
 */
SuccessPricing.prototype['dictionaries'] = undefined;

/**
 * @member {module:model/IncludedResourcesMap} included
 */
SuccessPricing.prototype['included'] = undefined;

/**
 * @member {Array.<module:model/Issue>} warnings
 */
SuccessPricing.prototype['warnings'] = undefined;






export default SuccessPricing;

