/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PriceUnavailableCountDetails model module.
 * @module model/PriceUnavailableCountDetails
 * @version v3
 */
class PriceUnavailableCountDetails {
    /**
     * Constructs a new <code>PriceUnavailableCountDetails</code>.
     * The reasons that contributed to the price unavailable count and the total count for each reason.
     * @alias module:model/PriceUnavailableCountDetails
     */
    constructor() { 
        
        PriceUnavailableCountDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PriceUnavailableCountDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PriceUnavailableCountDetails} obj Optional instance to populate.
     * @return {module:model/PriceUnavailableCountDetails} The populated <code>PriceUnavailableCountDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PriceUnavailableCountDetails();

            if (data.hasOwnProperty('participationNotLikelyCount')) {
                obj['participationNotLikelyCount'] = ApiClient.convertToType(data['participationNotLikelyCount'], 'String');
            }
            if (data.hasOwnProperty('priceUnavailableCount')) {
                obj['priceUnavailableCount'] = ApiClient.convertToType(data['priceUnavailableCount'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PriceUnavailableCountDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PriceUnavailableCountDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['participationNotLikelyCount'] && !(typeof data['participationNotLikelyCount'] === 'string' || data['participationNotLikelyCount'] instanceof String)) {
            throw new Error("Expected the field `participationNotLikelyCount` to be a primitive type in the JSON string but got " + data['participationNotLikelyCount']);
        }
        // ensure the json data is a string
        if (data['priceUnavailableCount'] && !(typeof data['priceUnavailableCount'] === 'string' || data['priceUnavailableCount'] instanceof String)) {
            throw new Error("Expected the field `priceUnavailableCount` to be a primitive type in the JSON string but got " + data['priceUnavailableCount']);
        }

        return true;
    }


}



/**
 * No price was cached for this itinerary, and no live query was done because your server usually tells us the hotel is unavailable or sold out.
 * @member {String} participationNotLikelyCount
 */
PriceUnavailableCountDetails.prototype['participationNotLikelyCount'] = undefined;

/**
 * Hotel did not participate because it wasn't available for the itinerary dates.
 * @member {String} priceUnavailableCount
 */
PriceUnavailableCountDetails.prototype['priceUnavailableCount'] = undefined;






export default PriceUnavailableCountDetails;

