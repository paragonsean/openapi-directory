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
import BoardType from './BoardType';
import HotelProductCommission from './HotelProductCommission';
import HotelProductGuests from './HotelProductGuests';
import HotelProductHotelPrice from './HotelProductHotelPrice';
import HotelProductPolicyDetails from './HotelProductPolicyDetails';
import HotelProductRateFamily from './HotelProductRateFamily';
import HotelProductRoomDetails from './HotelProductRoomDetails';
import QualifiedFreeText from './QualifiedFreeText';
import Type from './Type';

/**
 * The HotelOffer model module.
 * @module model/HotelOffer
 * @version 3.0.8
 */
class HotelOffer {
    /**
     * Constructs a new <code>HotelOffer</code>.
     * Hotel Offer
     * @alias module:model/HotelOffer
     * @param id {String} Unique identifier of this offer. Might be valid for a temporary period only.
     * @param price {module:model/HotelProductHotelPrice} 
     * @param rateCode {String} Special Rate - Provider Response Code (3 chars) Examples    * RAC - Rack    * BAR - Best Available Rate    * PRO - Promotional    * COR - Corporate    * GOV - Government (qualified)    * AAA - AAA (qualified)    * BNB - Bed and Breakfast    * PKG - Package    * TVL - Travel Industry    * SPC - Special Promo Rate    * WKD - Weekend    * CON - Convention    * SNR - Senior (Europe) (qualified)    * ARP - AARP - American Association of Retired People (50+) (qualified)    * SRS - Senior (qualified)    * ROR - Room Only Rate (no breakfast)    * FAM - Family    * DAY - Day rate
     * @param room {module:model/HotelProductRoomDetails} 
     */
    constructor(id, price, rateCode, room) { 
        
        HotelOffer.initialize(this, id, price, rateCode, room);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, price, rateCode, room) { 
        obj['id'] = id;
        obj['price'] = price;
        obj['rateCode'] = rateCode;
        obj['room'] = room;
    }

    /**
     * Constructs a <code>HotelOffer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HotelOffer} obj Optional instance to populate.
     * @return {module:model/HotelOffer} The populated <code>HotelOffer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HotelOffer();

            if (data.hasOwnProperty('boardType')) {
                obj['boardType'] = BoardType.constructFromObject(data['boardType']);
            }
            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], 'String');
            }
            if (data.hasOwnProperty('checkInDate')) {
                obj['checkInDate'] = ApiClient.convertToType(data['checkInDate'], 'Date');
            }
            if (data.hasOwnProperty('checkOutDate')) {
                obj['checkOutDate'] = ApiClient.convertToType(data['checkOutDate'], 'Date');
            }
            if (data.hasOwnProperty('commission')) {
                obj['commission'] = HotelProductCommission.constructFromObject(data['commission']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = QualifiedFreeText.constructFromObject(data['description']);
            }
            if (data.hasOwnProperty('guests')) {
                obj['guests'] = HotelProductGuests.constructFromObject(data['guests']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('policies')) {
                obj['policies'] = HotelProductPolicyDetails.constructFromObject(data['policies']);
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = HotelProductHotelPrice.constructFromObject(data['price']);
            }
            if (data.hasOwnProperty('rateCode')) {
                obj['rateCode'] = ApiClient.convertToType(data['rateCode'], 'String');
            }
            if (data.hasOwnProperty('rateFamilyEstimated')) {
                obj['rateFamilyEstimated'] = HotelProductRateFamily.constructFromObject(data['rateFamilyEstimated']);
            }
            if (data.hasOwnProperty('room')) {
                obj['room'] = HotelProductRoomDetails.constructFromObject(data['room']);
            }
            if (data.hasOwnProperty('roomQuantity')) {
                obj['roomQuantity'] = ApiClient.convertToType(data['roomQuantity'], 'String');
            }
            if (data.hasOwnProperty('self')) {
                obj['self'] = ApiClient.convertToType(data['self'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = Type.constructFromObject(data['type']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HotelOffer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HotelOffer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HotelOffer.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['category'] && !(typeof data['category'] === 'string' || data['category'] instanceof String)) {
            throw new Error("Expected the field `category` to be a primitive type in the JSON string but got " + data['category']);
        }
        // validate the optional field `commission`
        if (data['commission']) { // data not null
          HotelProductCommission.validateJSON(data['commission']);
        }
        // validate the optional field `description`
        if (data['description']) { // data not null
          QualifiedFreeText.validateJSON(data['description']);
        }
        // validate the optional field `guests`
        if (data['guests']) { // data not null
          HotelProductGuests.validateJSON(data['guests']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `policies`
        if (data['policies']) { // data not null
          HotelProductPolicyDetails.validateJSON(data['policies']);
        }
        // validate the optional field `price`
        if (data['price']) { // data not null
          HotelProductHotelPrice.validateJSON(data['price']);
        }
        // ensure the json data is a string
        if (data['rateCode'] && !(typeof data['rateCode'] === 'string' || data['rateCode'] instanceof String)) {
            throw new Error("Expected the field `rateCode` to be a primitive type in the JSON string but got " + data['rateCode']);
        }
        // validate the optional field `rateFamilyEstimated`
        if (data['rateFamilyEstimated']) { // data not null
          HotelProductRateFamily.validateJSON(data['rateFamilyEstimated']);
        }
        // validate the optional field `room`
        if (data['room']) { // data not null
          HotelProductRoomDetails.validateJSON(data['room']);
        }
        // ensure the json data is a string
        if (data['roomQuantity'] && !(typeof data['roomQuantity'] === 'string' || data['roomQuantity'] instanceof String)) {
            throw new Error("Expected the field `roomQuantity` to be a primitive type in the JSON string but got " + data['roomQuantity']);
        }
        // ensure the json data is a string
        if (data['self'] && !(typeof data['self'] === 'string' || data['self'] instanceof String)) {
            throw new Error("Expected the field `self` to be a primitive type in the JSON string but got " + data['self']);
        }

        return true;
    }


}

HotelOffer.RequiredProperties = ["id", "price", "rateCode", "room"];

/**
 * @member {module:model/BoardType} boardType
 */
HotelOffer.prototype['boardType'] = undefined;

/**
 * Special Rate Category Examples:   ASSOCIATION   FAMILY_PLAN
 * @member {String} category
 */
HotelOffer.prototype['category'] = undefined;

/**
 * check-in date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is today date (no dates in the past).
 * @member {Date} checkInDate
 */
HotelOffer.prototype['checkInDate'] = undefined;

/**
 * check-out date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is `checkInDate`+1.
 * @member {Date} checkOutDate
 */
HotelOffer.prototype['checkOutDate'] = undefined;

/**
 * @member {module:model/HotelProductCommission} commission
 */
HotelOffer.prototype['commission'] = undefined;

/**
 * @member {module:model/QualifiedFreeText} description
 */
HotelOffer.prototype['description'] = undefined;

/**
 * @member {module:model/HotelProductGuests} guests
 */
HotelOffer.prototype['guests'] = undefined;

/**
 * Unique identifier of this offer. Might be valid for a temporary period only.
 * @member {String} id
 */
HotelOffer.prototype['id'] = undefined;

/**
 * @member {module:model/HotelProductPolicyDetails} policies
 */
HotelOffer.prototype['policies'] = undefined;

/**
 * @member {module:model/HotelProductHotelPrice} price
 */
HotelOffer.prototype['price'] = undefined;

/**
 * Special Rate - Provider Response Code (3 chars) Examples    * RAC - Rack    * BAR - Best Available Rate    * PRO - Promotional    * COR - Corporate    * GOV - Government (qualified)    * AAA - AAA (qualified)    * BNB - Bed and Breakfast    * PKG - Package    * TVL - Travel Industry    * SPC - Special Promo Rate    * WKD - Weekend    * CON - Convention    * SNR - Senior (Europe) (qualified)    * ARP - AARP - American Association of Retired People (50+) (qualified)    * SRS - Senior (qualified)    * ROR - Room Only Rate (no breakfast)    * FAM - Family    * DAY - Day rate
 * @member {String} rateCode
 */
HotelOffer.prototype['rateCode'] = undefined;

/**
 * @member {module:model/HotelProductRateFamily} rateFamilyEstimated
 */
HotelOffer.prototype['rateFamilyEstimated'] = undefined;

/**
 * @member {module:model/HotelProductRoomDetails} room
 */
HotelOffer.prototype['room'] = undefined;

/**
 * number of rooms (1-9)
 * @member {String} roomQuantity
 */
HotelOffer.prototype['roomQuantity'] = undefined;

/**
 * A self link to the object. Use this to refresh the Offer price
 * @member {String} self
 */
HotelOffer.prototype['self'] = undefined;

/**
 * @member {module:model/Type} type
 */
HotelOffer.prototype['type'] = undefined;






export default HotelOffer;

