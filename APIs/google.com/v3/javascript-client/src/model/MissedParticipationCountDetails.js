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
import NoPriceCountDetails from './NoPriceCountDetails';
import PriceMissingCountDetails from './PriceMissingCountDetails';
import PriceProblemCountDetails from './PriceProblemCountDetails';
import PriceUnavailableCountDetails from './PriceUnavailableCountDetails';

/**
 * The MissedParticipationCountDetails model module.
 * @module model/MissedParticipationCountDetails
 * @version v3
 */
class MissedParticipationCountDetails {
    /**
     * Constructs a new <code>MissedParticipationCountDetails</code>.
     * Missed participation count broken down by reason.
     * @alias module:model/MissedParticipationCountDetails
     */
    constructor() { 
        
        MissedParticipationCountDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MissedParticipationCountDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MissedParticipationCountDetails} obj Optional instance to populate.
     * @return {module:model/MissedParticipationCountDetails} The populated <code>MissedParticipationCountDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MissedParticipationCountDetails();

            if (data.hasOwnProperty('hotelSuspendedCount')) {
                obj['hotelSuspendedCount'] = ApiClient.convertToType(data['hotelSuspendedCount'], 'String');
            }
            if (data.hasOwnProperty('noAvailabilityCount')) {
                obj['noAvailabilityCount'] = ApiClient.convertToType(data['noAvailabilityCount'], 'String');
            }
            if (data.hasOwnProperty('noLandingPageCount')) {
                obj['noLandingPageCount'] = ApiClient.convertToType(data['noLandingPageCount'], 'String');
            }
            if (data.hasOwnProperty('noPriceCount')) {
                obj['noPriceCount'] = ApiClient.convertToType(data['noPriceCount'], 'String');
            }
            if (data.hasOwnProperty('noPriceCountDetails')) {
                obj['noPriceCountDetails'] = NoPriceCountDetails.constructFromObject(data['noPriceCountDetails']);
            }
            if (data.hasOwnProperty('noTaxBreakdownCount')) {
                obj['noTaxBreakdownCount'] = ApiClient.convertToType(data['noTaxBreakdownCount'], 'String');
            }
            if (data.hasOwnProperty('otherReasonCount')) {
                obj['otherReasonCount'] = ApiClient.convertToType(data['otherReasonCount'], 'String');
            }
            if (data.hasOwnProperty('priceMissingCount')) {
                obj['priceMissingCount'] = ApiClient.convertToType(data['priceMissingCount'], 'String');
            }
            if (data.hasOwnProperty('priceMissingCountDetails')) {
                obj['priceMissingCountDetails'] = PriceMissingCountDetails.constructFromObject(data['priceMissingCountDetails']);
            }
            if (data.hasOwnProperty('priceProblemCount')) {
                obj['priceProblemCount'] = ApiClient.convertToType(data['priceProblemCount'], 'String');
            }
            if (data.hasOwnProperty('priceProblemCountDetails')) {
                obj['priceProblemCountDetails'] = PriceProblemCountDetails.constructFromObject(data['priceProblemCountDetails']);
            }
            if (data.hasOwnProperty('priceUnavailableCount')) {
                obj['priceUnavailableCount'] = ApiClient.convertToType(data['priceUnavailableCount'], 'String');
            }
            if (data.hasOwnProperty('priceUnavailableCountDetails')) {
                obj['priceUnavailableCountDetails'] = PriceUnavailableCountDetails.constructFromObject(data['priceUnavailableCountDetails']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MissedParticipationCountDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MissedParticipationCountDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['hotelSuspendedCount'] && !(typeof data['hotelSuspendedCount'] === 'string' || data['hotelSuspendedCount'] instanceof String)) {
            throw new Error("Expected the field `hotelSuspendedCount` to be a primitive type in the JSON string but got " + data['hotelSuspendedCount']);
        }
        // ensure the json data is a string
        if (data['noAvailabilityCount'] && !(typeof data['noAvailabilityCount'] === 'string' || data['noAvailabilityCount'] instanceof String)) {
            throw new Error("Expected the field `noAvailabilityCount` to be a primitive type in the JSON string but got " + data['noAvailabilityCount']);
        }
        // ensure the json data is a string
        if (data['noLandingPageCount'] && !(typeof data['noLandingPageCount'] === 'string' || data['noLandingPageCount'] instanceof String)) {
            throw new Error("Expected the field `noLandingPageCount` to be a primitive type in the JSON string but got " + data['noLandingPageCount']);
        }
        // ensure the json data is a string
        if (data['noPriceCount'] && !(typeof data['noPriceCount'] === 'string' || data['noPriceCount'] instanceof String)) {
            throw new Error("Expected the field `noPriceCount` to be a primitive type in the JSON string but got " + data['noPriceCount']);
        }
        // validate the optional field `noPriceCountDetails`
        if (data['noPriceCountDetails']) { // data not null
          NoPriceCountDetails.validateJSON(data['noPriceCountDetails']);
        }
        // ensure the json data is a string
        if (data['noTaxBreakdownCount'] && !(typeof data['noTaxBreakdownCount'] === 'string' || data['noTaxBreakdownCount'] instanceof String)) {
            throw new Error("Expected the field `noTaxBreakdownCount` to be a primitive type in the JSON string but got " + data['noTaxBreakdownCount']);
        }
        // ensure the json data is a string
        if (data['otherReasonCount'] && !(typeof data['otherReasonCount'] === 'string' || data['otherReasonCount'] instanceof String)) {
            throw new Error("Expected the field `otherReasonCount` to be a primitive type in the JSON string but got " + data['otherReasonCount']);
        }
        // ensure the json data is a string
        if (data['priceMissingCount'] && !(typeof data['priceMissingCount'] === 'string' || data['priceMissingCount'] instanceof String)) {
            throw new Error("Expected the field `priceMissingCount` to be a primitive type in the JSON string but got " + data['priceMissingCount']);
        }
        // validate the optional field `priceMissingCountDetails`
        if (data['priceMissingCountDetails']) { // data not null
          PriceMissingCountDetails.validateJSON(data['priceMissingCountDetails']);
        }
        // ensure the json data is a string
        if (data['priceProblemCount'] && !(typeof data['priceProblemCount'] === 'string' || data['priceProblemCount'] instanceof String)) {
            throw new Error("Expected the field `priceProblemCount` to be a primitive type in the JSON string but got " + data['priceProblemCount']);
        }
        // validate the optional field `priceProblemCountDetails`
        if (data['priceProblemCountDetails']) { // data not null
          PriceProblemCountDetails.validateJSON(data['priceProblemCountDetails']);
        }
        // ensure the json data is a string
        if (data['priceUnavailableCount'] && !(typeof data['priceUnavailableCount'] === 'string' || data['priceUnavailableCount'] instanceof String)) {
            throw new Error("Expected the field `priceUnavailableCount` to be a primitive type in the JSON string but got " + data['priceUnavailableCount']);
        }
        // validate the optional field `priceUnavailableCountDetails`
        if (data['priceUnavailableCountDetails']) { // data not null
          PriceUnavailableCountDetails.validateJSON(data['priceUnavailableCountDetails']);
        }

        return true;
    }


}



/**
 * The total number of missed participations due to one or more of your hotels being suspended due to price accuracy violations.
 * @member {String} hotelSuspendedCount
 */
MissedParticipationCountDetails.prototype['hotelSuspendedCount'] = undefined;

/**
 * The total number of missed participation due to the hotel/itinerary combination being unavailable, or the traveler was ineligible for the rates. To participate in these auctions, you may need to provide more pricing information.
 * @member {String} noAvailabilityCount
 */
MissedParticipationCountDetails.prototype['noAvailabilityCount'] = undefined;

/**
 * No landing page matched the user.
 * @member {String} noLandingPageCount
 */
MissedParticipationCountDetails.prototype['noLandingPageCount'] = undefined;

/**
 * The total number of missed participations due to a price not being offered for the requested itinerary.
 * @member {String} noPriceCount
 */
MissedParticipationCountDetails.prototype['noPriceCount'] = undefined;

/**
 * @member {module:model/NoPriceCountDetails} noPriceCountDetails
 */
MissedParticipationCountDetails.prototype['noPriceCountDetails'] = undefined;

/**
 * The total number of missed participation due to one or more of your hotels not specifying taxes and fees separately.
 * @member {String} noTaxBreakdownCount
 */
MissedParticipationCountDetails.prototype['noTaxBreakdownCount'] = undefined;

/**
 * Hotel did not participate for an unknown reason.
 * @member {String} otherReasonCount
 */
MissedParticipationCountDetails.prototype['otherReasonCount'] = undefined;

/**
 * The total number of missed participations due to either a price not being present in Google's cache or failing to successfully respond to live pricing. Comprised of the following: * Bandwidth depleted * Cache rate missing * Itinerary blocked * Live pricing not set up * Live pricing timeout * Live pricing error
 * @member {String} priceMissingCount
 */
MissedParticipationCountDetails.prototype['priceMissingCount'] = undefined;

/**
 * @member {module:model/PriceMissingCountDetails} priceMissingCountDetails
 */
MissedParticipationCountDetails.prototype['priceMissingCountDetails'] = undefined;

/**
 * The total number of missed participation due to an issue with the accuracy of the price provided for the itinerary. Comprised of the following: * Hotel suspended * Price unusually high * Price unusually low * Taxes and feeds missing
 * @member {String} priceProblemCount
 */
MissedParticipationCountDetails.prototype['priceProblemCount'] = undefined;

/**
 * @member {module:model/PriceProblemCountDetails} priceProblemCountDetails
 */
MissedParticipationCountDetails.prototype['priceProblemCountDetails'] = undefined;

/**
 * The total number of missed participation due to price listed as unavailable (-1) for the requested itinerary. Comprised of the following: * Price unavailable * Participation not likely * Other
 * @member {String} priceUnavailableCount
 */
MissedParticipationCountDetails.prototype['priceUnavailableCount'] = undefined;

/**
 * @member {module:model/PriceUnavailableCountDetails} priceUnavailableCountDetails
 */
MissedParticipationCountDetails.prototype['priceUnavailableCountDetails'] = undefined;






export default MissedParticipationCountDetails;

