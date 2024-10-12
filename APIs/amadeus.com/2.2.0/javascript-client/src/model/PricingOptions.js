/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PricingOptions model module.
 * @module model/PricingOptions
 * @version 2.2.0
 */
class PricingOptions {
    /**
     * Constructs a new <code>PricingOptions</code>.
     * @alias module:model/PricingOptions
     */
    constructor() { 
        
        PricingOptions.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PricingOptions</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PricingOptions} obj Optional instance to populate.
     * @return {module:model/PricingOptions} The populated <code>PricingOptions</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PricingOptions();

            if (data.hasOwnProperty('fareType')) {
                obj['fareType'] = ApiClient.convertToType(data['fareType'], ['String']);
            }
            if (data.hasOwnProperty('includedCheckedBagsOnly')) {
                obj['includedCheckedBagsOnly'] = ApiClient.convertToType(data['includedCheckedBagsOnly'], 'Boolean');
            }
            if (data.hasOwnProperty('noPenaltyFare')) {
                obj['noPenaltyFare'] = ApiClient.convertToType(data['noPenaltyFare'], 'Boolean');
            }
            if (data.hasOwnProperty('noRestrictionFare')) {
                obj['noRestrictionFare'] = ApiClient.convertToType(data['noRestrictionFare'], 'Boolean');
            }
            if (data.hasOwnProperty('refundableFare')) {
                obj['refundableFare'] = ApiClient.convertToType(data['refundableFare'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PricingOptions</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PricingOptions</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['fareType'])) {
            throw new Error("Expected the field `fareType` to be an array in the JSON data but got " + data['fareType']);
        }

        return true;
    }


}



/**
 * type of fare of the flight-offer
 * @member {Array.<module:model/PricingOptions.FareTypeEnum>} fareType
 */
PricingOptions.prototype['fareType'] = undefined;

/**
 * If true, returns the flight-offers with included checked bags only
 * @member {Boolean} includedCheckedBagsOnly
 */
PricingOptions.prototype['includedCheckedBagsOnly'] = undefined;

/**
 * If true, returns the flight-offers with no penalty fares only
 * @member {Boolean} noPenaltyFare
 */
PricingOptions.prototype['noPenaltyFare'] = undefined;

/**
 * If true, returns the flight-offers with no restriction fares only
 * @member {Boolean} noRestrictionFare
 */
PricingOptions.prototype['noRestrictionFare'] = undefined;

/**
 * If true, returns the flight-offers with refundable fares only
 * @member {Boolean} refundableFare
 */
PricingOptions.prototype['refundableFare'] = undefined;





/**
 * Allowed values for the <code>fareType</code> property.
 * @enum {String}
 * @readonly
 */
PricingOptions['FareTypeEnum'] = {

    /**
     * value: "PUBLISHED"
     * @const
     */
    "PUBLISHED": "PUBLISHED",

    /**
     * value: "NEGOTIATED"
     * @const
     */
    "NEGOTIATED": "NEGOTIATED",

    /**
     * value: "CORPORATE"
     * @const
     */
    "CORPORATE": "CORPORATE"
};



export default PricingOptions;

