/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CreditCardBrand from './CreditCardBrand';
import CreditCardCommon from './CreditCardCommon';

/**
 * The CreditCard model module.
 * @module model/CreditCard
 * @version 1.9.0
 */
class CreditCard {
    /**
     * Constructs a new <code>CreditCard</code>.
     * credit card
     * @alias module:model/CreditCard
     * @implements module:model/CreditCardCommon
     */
    constructor() { 
        CreditCardCommon.initialize(this);
        CreditCard.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreditCard</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreditCard} obj Optional instance to populate.
     * @return {module:model/CreditCard} The populated <code>CreditCard</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreditCard();
            CreditCardCommon.constructFromObject(data, obj);

            if (data.hasOwnProperty('brand')) {
                obj['brand'] = CreditCardBrand.constructFromObject(data['brand']);
            }
            if (data.hasOwnProperty('expiryDate')) {
                obj['expiryDate'] = ApiClient.convertToType(data['expiryDate'], 'String');
            }
            if (data.hasOwnProperty('holder')) {
                obj['holder'] = ApiClient.convertToType(data['holder'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
            if (data.hasOwnProperty('flightOfferIds')) {
                obj['flightOfferIds'] = ApiClient.convertToType(data['flightOfferIds'], ['String']);
            }
            if (data.hasOwnProperty('securityCode')) {
                obj['securityCode'] = ApiClient.convertToType(data['securityCode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreditCard</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreditCard</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['expiryDate'] && !(typeof data['expiryDate'] === 'string' || data['expiryDate'] instanceof String)) {
            throw new Error("Expected the field `expiryDate` to be a primitive type in the JSON string but got " + data['expiryDate']);
        }
        // ensure the json data is a string
        if (data['holder'] && !(typeof data['holder'] === 'string' || data['holder'] instanceof String)) {
            throw new Error("Expected the field `holder` to be a primitive type in the JSON string but got " + data['holder']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['flightOfferIds'])) {
            throw new Error("Expected the field `flightOfferIds` to be an array in the JSON data but got " + data['flightOfferIds']);
        }
        // ensure the json data is a string
        if (data['securityCode'] && !(typeof data['securityCode'] === 'string' || data['securityCode'] instanceof String)) {
            throw new Error("Expected the field `securityCode` to be a primitive type in the JSON string but got " + data['securityCode']);
        }

        return true;
    }


}



/**
 * @member {module:model/CreditCardBrand} brand
 */
CreditCard.prototype['brand'] = undefined;

/**
 * credit card expiration date following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (YYYY-MM format, e.g. 2012-08)
 * @member {String} expiryDate
 */
CreditCard.prototype['expiryDate'] = undefined;

/**
 * card holder as on the card
 * @member {String} holder
 */
CreditCard.prototype['holder'] = undefined;

/**
 * card number
 * @member {String} number
 */
CreditCard.prototype['number'] = undefined;

/**
 * Id of the concern flightOffers
 * @member {Array.<String>} flightOfferIds
 */
CreditCard.prototype['flightOfferIds'] = undefined;

/**
 * card security code
 * @member {String} securityCode
 */
CreditCard.prototype['securityCode'] = undefined;


// Implement CreditCardCommon interface:
/**
 * @member {module:model/CreditCardBrand} brand
 */
CreditCardCommon.prototype['brand'] = undefined;
/**
 * credit card expiration date following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (YYYY-MM format, e.g. 2012-08)
 * @member {String} expiryDate
 */
CreditCardCommon.prototype['expiryDate'] = undefined;
/**
 * card holder as on the card
 * @member {String} holder
 */
CreditCardCommon.prototype['holder'] = undefined;
/**
 * card number
 * @member {String} number
 */
CreditCardCommon.prototype['number'] = undefined;




export default CreditCard;

