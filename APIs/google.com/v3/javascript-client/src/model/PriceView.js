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
import HotelPricePerItinerary from './HotelPricePerItinerary';

/**
 * The PriceView model module.
 * @module model/PriceView
 * @version v3
 */
class PriceView {
    /**
     * Constructs a new <code>PriceView</code>.
     * A price view. Covers the Prices functionality in pre-v3.0 API versions.
     * @alias module:model/PriceView
     */
    constructor() { 
        
        PriceView.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PriceView</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PriceView} obj Optional instance to populate.
     * @return {module:model/PriceView} The populated <code>PriceView</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PriceView();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('perItineraryPrices')) {
                obj['perItineraryPrices'] = ApiClient.convertToType(data['perItineraryPrices'], [HotelPricePerItinerary]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PriceView</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PriceView</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['perItineraryPrices']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['perItineraryPrices'])) {
                throw new Error("Expected the field `perItineraryPrices` to be an array in the JSON data but got " + data['perItineraryPrices']);
            }
            // validate the optional field `perItineraryPrices` (array)
            for (const item of data['perItineraryPrices']) {
                HotelPricePerItinerary.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Resource name in the format `accounts/{account_id}/priceViews/{partner_hotel_id}`.
 * @member {String} name
 */
PriceView.prototype['name'] = undefined;

/**
 * Price for each itinerary.
 * @member {Array.<module:model/HotelPricePerItinerary>} perItineraryPrices
 */
PriceView.prototype['perItineraryPrices'] = undefined;






export default PriceView;

