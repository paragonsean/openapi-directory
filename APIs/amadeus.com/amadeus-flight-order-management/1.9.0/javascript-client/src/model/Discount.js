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
import DiscountTravelerType from './DiscountTravelerType';
import DiscountType from './DiscountType';

/**
 * The Discount model module.
 * @module model/Discount
 * @version 1.9.0
 */
class Discount {
    /**
     * Constructs a new <code>Discount</code>.
     * traveler discount
     * @alias module:model/Discount
     */
    constructor() { 
        
        Discount.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Discount</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Discount} obj Optional instance to populate.
     * @return {module:model/Discount} The populated <code>Discount</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Discount();

            if (data.hasOwnProperty('cardNumber')) {
                obj['cardNumber'] = ApiClient.convertToType(data['cardNumber'], 'String');
            }
            if (data.hasOwnProperty('certificateNumber')) {
                obj['certificateNumber'] = ApiClient.convertToType(data['certificateNumber'], 'String');
            }
            if (data.hasOwnProperty('cityName')) {
                obj['cityName'] = ApiClient.convertToType(data['cityName'], 'String');
            }
            if (data.hasOwnProperty('subType')) {
                obj['subType'] = DiscountType.constructFromObject(data['subType']);
            }
            if (data.hasOwnProperty('travelerType')) {
                obj['travelerType'] = DiscountTravelerType.constructFromObject(data['travelerType']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Discount</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Discount</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['cardNumber'] && !(typeof data['cardNumber'] === 'string' || data['cardNumber'] instanceof String)) {
            throw new Error("Expected the field `cardNumber` to be a primitive type in the JSON string but got " + data['cardNumber']);
        }
        // ensure the json data is a string
        if (data['certificateNumber'] && !(typeof data['certificateNumber'] === 'string' || data['certificateNumber'] instanceof String)) {
            throw new Error("Expected the field `certificateNumber` to be a primitive type in the JSON string but got " + data['certificateNumber']);
        }
        // ensure the json data is a string
        if (data['cityName'] && !(typeof data['cityName'] === 'string' || data['cityName'] instanceof String)) {
            throw new Error("Expected the field `cityName` to be a primitive type in the JSON string but got " + data['cityName']);
        }

        return true;
    }


}



/**
 * resident card number
 * @member {String} cardNumber
 */
Discount.prototype['cardNumber'] = undefined;

/**
 * resident certificate number
 * @member {String} certificateNumber
 */
Discount.prototype['certificateNumber'] = undefined;

/**
 * city of residence
 * @member {String} cityName
 */
Discount.prototype['cityName'] = undefined;

/**
 * @member {module:model/DiscountType} subType
 */
Discount.prototype['subType'] = undefined;

/**
 * @member {module:model/DiscountTravelerType} travelerType
 */
Discount.prototype['travelerType'] = undefined;






export default Discount;

