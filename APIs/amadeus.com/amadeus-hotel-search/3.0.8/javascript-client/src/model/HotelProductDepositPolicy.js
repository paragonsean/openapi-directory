/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import HotelProductPaymentPolicy from './HotelProductPaymentPolicy';
import QualifiedFreeText from './QualifiedFreeText';

/**
 * The HotelProductDepositPolicy model module.
 * @module model/HotelProductDepositPolicy
 * @version 3.0.8
 */
class HotelProductDepositPolicy {
    /**
     * Constructs a new <code>HotelProductDepositPolicy</code>.
     * the deposit/prepay policy information applicable to the offer. It includes accepted payments, deadline and the amount due
     * @alias module:model/HotelProductDepositPolicy
     */
    constructor() { 
        
        HotelProductDepositPolicy.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HotelProductDepositPolicy</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HotelProductDepositPolicy} obj Optional instance to populate.
     * @return {module:model/HotelProductDepositPolicy} The populated <code>HotelProductDepositPolicy</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HotelProductDepositPolicy();

            if (data.hasOwnProperty('acceptedPayments')) {
                obj['acceptedPayments'] = HotelProductPaymentPolicy.constructFromObject(data['acceptedPayments']);
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'String');
            }
            if (data.hasOwnProperty('deadline')) {
                obj['deadline'] = ApiClient.convertToType(data['deadline'], 'Date');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = QualifiedFreeText.constructFromObject(data['description']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HotelProductDepositPolicy</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HotelProductDepositPolicy</code>.
     */
    static validateJSON(data) {
        // validate the optional field `acceptedPayments`
        if (data['acceptedPayments']) { // data not null
          HotelProductPaymentPolicy.validateJSON(data['acceptedPayments']);
        }
        // ensure the json data is a string
        if (data['amount'] && !(typeof data['amount'] === 'string' || data['amount'] instanceof String)) {
            throw new Error("Expected the field `amount` to be a primitive type in the JSON string but got " + data['amount']);
        }
        // validate the optional field `description`
        if (data['description']) { // data not null
          QualifiedFreeText.validateJSON(data['description']);
        }

        return true;
    }


}



/**
 * @member {module:model/HotelProductPaymentPolicy} acceptedPayments
 */
HotelProductDepositPolicy.prototype['acceptedPayments'] = undefined;

/**
 * Deposit-Prepay amount
 * @member {String} amount
 */
HotelProductDepositPolicy.prototype['amount'] = undefined;

/**
 * The date and time of the deadline in ISO 8601[https://www.w3.org/TR/NOTE-datetime].   Example: 2010-08-14T13:00:00  Please note that this value is expressed in the hotels local time zone
 * @member {Date} deadline
 */
HotelProductDepositPolicy.prototype['deadline'] = undefined;

/**
 * @member {module:model/QualifiedFreeText} description
 */
HotelProductDepositPolicy.prototype['description'] = undefined;






export default HotelProductDepositPolicy;

