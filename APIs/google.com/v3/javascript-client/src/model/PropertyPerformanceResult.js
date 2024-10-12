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
import ModelDate from './ModelDate';

/**
 * The PropertyPerformanceResult model module.
 * @module model/PropertyPerformanceResult
 * @version v3
 */
class PropertyPerformanceResult {
    /**
     * Constructs a new <code>PropertyPerformanceResult</code>.
     * Represents a result from querying for the property performance report for an account.
     * @alias module:model/PropertyPerformanceResult
     */
    constructor() { 
        
        PropertyPerformanceResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PropertyPerformanceResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PropertyPerformanceResult} obj Optional instance to populate.
     * @return {module:model/PropertyPerformanceResult} The populated <code>PropertyPerformanceResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PropertyPerformanceResult();

            if (data.hasOwnProperty('adsClickCount')) {
                obj['adsClickCount'] = ApiClient.convertToType(data['adsClickCount'], 'String');
            }
            if (data.hasOwnProperty('adsClickthroughRate')) {
                obj['adsClickthroughRate'] = ApiClient.convertToType(data['adsClickthroughRate'], 'Number');
            }
            if (data.hasOwnProperty('adsImpressionCount')) {
                obj['adsImpressionCount'] = ApiClient.convertToType(data['adsImpressionCount'], 'String');
            }
            if (data.hasOwnProperty('advanceBookingWindow')) {
                obj['advanceBookingWindow'] = ApiClient.convertToType(data['advanceBookingWindow'], 'String');
            }
            if (data.hasOwnProperty('brand')) {
                obj['brand'] = ApiClient.convertToType(data['brand'], 'String');
            }
            if (data.hasOwnProperty('clickCount')) {
                obj['clickCount'] = ApiClient.convertToType(data['clickCount'], 'String');
            }
            if (data.hasOwnProperty('clickthroughRate')) {
                obj['clickthroughRate'] = ApiClient.convertToType(data['clickthroughRate'], 'Number');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ModelDate.constructFromObject(data['date']);
            }
            if (data.hasOwnProperty('deviceType')) {
                obj['deviceType'] = ApiClient.convertToType(data['deviceType'], 'String');
            }
            if (data.hasOwnProperty('highIntentUsers')) {
                obj['highIntentUsers'] = ApiClient.convertToType(data['highIntentUsers'], 'Boolean');
            }
            if (data.hasOwnProperty('impressionCount')) {
                obj['impressionCount'] = ApiClient.convertToType(data['impressionCount'], 'String');
            }
            if (data.hasOwnProperty('lengthOfStay')) {
                obj['lengthOfStay'] = ApiClient.convertToType(data['lengthOfStay'], 'String');
            }
            if (data.hasOwnProperty('occupancy')) {
                obj['occupancy'] = ApiClient.convertToType(data['occupancy'], 'String');
            }
            if (data.hasOwnProperty('partnerPropertyDisplayName')) {
                obj['partnerPropertyDisplayName'] = ApiClient.convertToType(data['partnerPropertyDisplayName'], 'String');
            }
            if (data.hasOwnProperty('partnerPropertyId')) {
                obj['partnerPropertyId'] = ApiClient.convertToType(data['partnerPropertyId'], 'String');
            }
            if (data.hasOwnProperty('propertyRegionCode')) {
                obj['propertyRegionCode'] = ApiClient.convertToType(data['propertyRegionCode'], 'String');
            }
            if (data.hasOwnProperty('userRegionCode')) {
                obj['userRegionCode'] = ApiClient.convertToType(data['userRegionCode'], 'String');
            }
            if (data.hasOwnProperty('vrWebsiteButtonClicks')) {
                obj['vrWebsiteButtonClicks'] = ApiClient.convertToType(data['vrWebsiteButtonClicks'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PropertyPerformanceResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PropertyPerformanceResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['adsClickCount'] && !(typeof data['adsClickCount'] === 'string' || data['adsClickCount'] instanceof String)) {
            throw new Error("Expected the field `adsClickCount` to be a primitive type in the JSON string but got " + data['adsClickCount']);
        }
        // ensure the json data is a string
        if (data['adsImpressionCount'] && !(typeof data['adsImpressionCount'] === 'string' || data['adsImpressionCount'] instanceof String)) {
            throw new Error("Expected the field `adsImpressionCount` to be a primitive type in the JSON string but got " + data['adsImpressionCount']);
        }
        // ensure the json data is a string
        if (data['advanceBookingWindow'] && !(typeof data['advanceBookingWindow'] === 'string' || data['advanceBookingWindow'] instanceof String)) {
            throw new Error("Expected the field `advanceBookingWindow` to be a primitive type in the JSON string but got " + data['advanceBookingWindow']);
        }
        // ensure the json data is a string
        if (data['brand'] && !(typeof data['brand'] === 'string' || data['brand'] instanceof String)) {
            throw new Error("Expected the field `brand` to be a primitive type in the JSON string but got " + data['brand']);
        }
        // ensure the json data is a string
        if (data['clickCount'] && !(typeof data['clickCount'] === 'string' || data['clickCount'] instanceof String)) {
            throw new Error("Expected the field `clickCount` to be a primitive type in the JSON string but got " + data['clickCount']);
        }
        // validate the optional field `date`
        if (data['date']) { // data not null
          ModelDate.validateJSON(data['date']);
        }
        // ensure the json data is a string
        if (data['deviceType'] && !(typeof data['deviceType'] === 'string' || data['deviceType'] instanceof String)) {
            throw new Error("Expected the field `deviceType` to be a primitive type in the JSON string but got " + data['deviceType']);
        }
        // ensure the json data is a string
        if (data['impressionCount'] && !(typeof data['impressionCount'] === 'string' || data['impressionCount'] instanceof String)) {
            throw new Error("Expected the field `impressionCount` to be a primitive type in the JSON string but got " + data['impressionCount']);
        }
        // ensure the json data is a string
        if (data['lengthOfStay'] && !(typeof data['lengthOfStay'] === 'string' || data['lengthOfStay'] instanceof String)) {
            throw new Error("Expected the field `lengthOfStay` to be a primitive type in the JSON string but got " + data['lengthOfStay']);
        }
        // ensure the json data is a string
        if (data['occupancy'] && !(typeof data['occupancy'] === 'string' || data['occupancy'] instanceof String)) {
            throw new Error("Expected the field `occupancy` to be a primitive type in the JSON string but got " + data['occupancy']);
        }
        // ensure the json data is a string
        if (data['partnerPropertyDisplayName'] && !(typeof data['partnerPropertyDisplayName'] === 'string' || data['partnerPropertyDisplayName'] instanceof String)) {
            throw new Error("Expected the field `partnerPropertyDisplayName` to be a primitive type in the JSON string but got " + data['partnerPropertyDisplayName']);
        }
        // ensure the json data is a string
        if (data['partnerPropertyId'] && !(typeof data['partnerPropertyId'] === 'string' || data['partnerPropertyId'] instanceof String)) {
            throw new Error("Expected the field `partnerPropertyId` to be a primitive type in the JSON string but got " + data['partnerPropertyId']);
        }
        // ensure the json data is a string
        if (data['propertyRegionCode'] && !(typeof data['propertyRegionCode'] === 'string' || data['propertyRegionCode'] instanceof String)) {
            throw new Error("Expected the field `propertyRegionCode` to be a primitive type in the JSON string but got " + data['propertyRegionCode']);
        }
        // ensure the json data is a string
        if (data['userRegionCode'] && !(typeof data['userRegionCode'] === 'string' || data['userRegionCode'] instanceof String)) {
            throw new Error("Expected the field `userRegionCode` to be a primitive type in the JSON string but got " + data['userRegionCode']);
        }
        // ensure the json data is a string
        if (data['vrWebsiteButtonClicks'] && !(typeof data['vrWebsiteButtonClicks'] === 'string' || data['vrWebsiteButtonClicks'] instanceof String)) {
            throw new Error("Expected the field `vrWebsiteButtonClicks` to be a primitive type in the JSON string but got " + data['vrWebsiteButtonClicks']);
        }

        return true;
    }


}



/**
 * The total number of ad clicks that were recorded for this result.
 * @member {String} adsClickCount
 */
PropertyPerformanceResult.prototype['adsClickCount'] = undefined;

/**
 * Equal to `ads_click_count` divided by `ads_impression_count`.
 * @member {Number} adsClickthroughRate
 */
PropertyPerformanceResult.prototype['adsClickthroughRate'] = undefined;

/**
 * The total number of ad impressions that were recorded for this result.
 * @member {String} adsImpressionCount
 */
PropertyPerformanceResult.prototype['adsImpressionCount'] = undefined;

/**
 * Difference in days between query date and check-in date in property's local timezone. Only present if `advanceBookingWindow` is specified in `aggregateBy` in the request.
 * @member {module:model/PropertyPerformanceResult.AdvanceBookingWindowEnum} advanceBookingWindow
 */
PropertyPerformanceResult.prototype['advanceBookingWindow'] = undefined;

/**
 * Partner-specified brand for the property. Only present if `brand` is specified in `aggregateBy` in the request.
 * @member {String} brand
 */
PropertyPerformanceResult.prototype['brand'] = undefined;

/**
 * The total number of free booking link clicks that were recorded for this result.
 * @member {String} clickCount
 */
PropertyPerformanceResult.prototype['clickCount'] = undefined;

/**
 * Equal to `click_count` divided by `impression_count`.
 * @member {Number} clickthroughRate
 */
PropertyPerformanceResult.prototype['clickthroughRate'] = undefined;

/**
 * @member {module:model/ModelDate} date
 */
PropertyPerformanceResult.prototype['date'] = undefined;

/**
 * The user’s device type. Only present if `deviceType` is specified in `aggregateBy` in the request.
 * @member {module:model/PropertyPerformanceResult.DeviceTypeEnum} deviceType
 */
PropertyPerformanceResult.prototype['deviceType'] = undefined;

/**
 * Whether the user’s query indicated a strong interest in booking. Only present if `highIntentUsers` is specified in `aggregateBy` in the request.
 * @member {Boolean} highIntentUsers
 */
PropertyPerformanceResult.prototype['highIntentUsers'] = undefined;

/**
 * The total number of free booking link impressions that were recorded for this result. This value is rounded to preserve user privacy.
 * @member {String} impressionCount
 */
PropertyPerformanceResult.prototype['impressionCount'] = undefined;

/**
 * Number of nights between check-in and check-out dates specified by user. Only present if `lengthOfStay` is specified in `aggregateBy` in the request.
 * @member {module:model/PropertyPerformanceResult.LengthOfStayEnum} lengthOfStay
 */
PropertyPerformanceResult.prototype['lengthOfStay'] = undefined;

/**
 * Requested number of people staying at the property. Only present if `partnerPropertyId` is specified in `aggregateBy` in the request.
 * @member {module:model/PropertyPerformanceResult.OccupancyEnum} occupancy
 */
PropertyPerformanceResult.prototype['occupancy'] = undefined;

/**
 * Partner's property name. Only present if `partnerPropertyDisplayName` is specified in `aggregateBy` in the request.
 * @member {String} partnerPropertyDisplayName
 */
PropertyPerformanceResult.prototype['partnerPropertyDisplayName'] = undefined;

/**
 * Partner's property ID. Only present if `partnerPropertyId` is specified in `aggregateBy` in the request.
 * @member {String} partnerPropertyId
 */
PropertyPerformanceResult.prototype['partnerPropertyId'] = undefined;

/**
 * ISO 3116 region code of the country/region of the property. Only present if `propertyRegionCode` is specified in `aggregateBy` in the request
 * @member {String} propertyRegionCode
 */
PropertyPerformanceResult.prototype['propertyRegionCode'] = undefined;

/**
 * ISO 3116 region code of the country/region of the user. Only present if `userRegionCode` is specified in `aggregateBy` in the request
 * @member {String} userRegionCode
 */
PropertyPerformanceResult.prototype['userRegionCode'] = undefined;

/**
 * The total number of clicks on the \"Website\" button on Google for vacation rentals.
 * @member {String} vrWebsiteButtonClicks
 */
PropertyPerformanceResult.prototype['vrWebsiteButtonClicks'] = undefined;





/**
 * Allowed values for the <code>advanceBookingWindow</code> property.
 * @enum {String}
 * @readonly
 */
PropertyPerformanceResult['AdvanceBookingWindowEnum'] = {

    /**
     * value: "ADVANCE_BOOKING_WINDOW_UNSPECIFIED"
     * @const
     */
    "UNSPECIFIED": "ADVANCE_BOOKING_WINDOW_UNSPECIFIED",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_SAME_DAY"
     * @const
     */
    "SAME_DAY": "ADVANCE_BOOKING_WINDOW_SAME_DAY",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_NEXT_DAY"
     * @const
     */
    "NEXT_DAY": "ADVANCE_BOOKING_WINDOW_NEXT_DAY",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_2_TO_7"
     * @const
     */
    "DAYS_2_TO_7": "ADVANCE_BOOKING_WINDOW_DAYS_2_TO_7",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_8_TO_14"
     * @const
     */
    "DAYS_8_TO_14": "ADVANCE_BOOKING_WINDOW_DAYS_8_TO_14",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_15_TO_30"
     * @const
     */
    "DAYS_15_TO_30": "ADVANCE_BOOKING_WINDOW_DAYS_15_TO_30",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_31_TO_60"
     * @const
     */
    "DAYS_31_TO_60": "ADVANCE_BOOKING_WINDOW_DAYS_31_TO_60",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90"
     * @const
     */
    "DAYS_61_TO_90": "ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_91_TO_120"
     * @const
     */
    "DAYS_91_TO_120": "ADVANCE_BOOKING_WINDOW_DAYS_91_TO_120",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_121_TO_150"
     * @const
     */
    "DAYS_121_TO_150": "ADVANCE_BOOKING_WINDOW_DAYS_121_TO_150",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_151_TO_180"
     * @const
     */
    "DAYS_151_TO_180": "ADVANCE_BOOKING_WINDOW_DAYS_151_TO_180",

    /**
     * value: "ADVANCE_BOOKING_WINDOW_DAYS_OVER_180"
     * @const
     */
    "DAYS_OVER_180": "ADVANCE_BOOKING_WINDOW_DAYS_OVER_180"
};


/**
 * Allowed values for the <code>deviceType</code> property.
 * @enum {String}
 * @readonly
 */
PropertyPerformanceResult['DeviceTypeEnum'] = {

    /**
     * value: "DEVICE_UNSPECIFIED"
     * @const
     */
    "DEVICE_UNSPECIFIED": "DEVICE_UNSPECIFIED",

    /**
     * value: "DEVICE_UNKNOWN"
     * @const
     */
    "DEVICE_UNKNOWN": "DEVICE_UNKNOWN",

    /**
     * value: "DESKTOP"
     * @const
     */
    "DESKTOP": "DESKTOP",

    /**
     * value: "MOBILE"
     * @const
     */
    "MOBILE": "MOBILE",

    /**
     * value: "TABLET"
     * @const
     */
    "TABLET": "TABLET"
};


/**
 * Allowed values for the <code>lengthOfStay</code> property.
 * @enum {String}
 * @readonly
 */
PropertyPerformanceResult['LengthOfStayEnum'] = {

    /**
     * value: "LENGTH_OF_STAY_UNSPECIFIED"
     * @const
     */
    "UNSPECIFIED": "LENGTH_OF_STAY_UNSPECIFIED",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_1"
     * @const
     */
    "NIGHTS_1": "LENGTH_OF_STAY_NIGHTS_1",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_2"
     * @const
     */
    "NIGHTS_2": "LENGTH_OF_STAY_NIGHTS_2",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_3"
     * @const
     */
    "NIGHTS_3": "LENGTH_OF_STAY_NIGHTS_3",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_4_TO_7"
     * @const
     */
    "NIGHTS_4_TO_7": "LENGTH_OF_STAY_NIGHTS_4_TO_7",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_8_TO_14"
     * @const
     */
    "NIGHTS_8_TO_14": "LENGTH_OF_STAY_NIGHTS_8_TO_14",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_15_TO_21"
     * @const
     */
    "NIGHTS_15_TO_21": "LENGTH_OF_STAY_NIGHTS_15_TO_21",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_22_TO_30"
     * @const
     */
    "NIGHTS_22_TO_30": "LENGTH_OF_STAY_NIGHTS_22_TO_30",

    /**
     * value: "LENGTH_OF_STAY_NIGHTS_OVER_30"
     * @const
     */
    "NIGHTS_OVER_30": "LENGTH_OF_STAY_NIGHTS_OVER_30"
};


/**
 * Allowed values for the <code>occupancy</code> property.
 * @enum {String}
 * @readonly
 */
PropertyPerformanceResult['OccupancyEnum'] = {

    /**
     * value: "OCCUPANCY_UNSPECIFIED"
     * @const
     */
    "UNSPECIFIED": "OCCUPANCY_UNSPECIFIED",

    /**
     * value: "OCCUPANCY_1"
     * @const
     */
    "1": "OCCUPANCY_1",

    /**
     * value: "OCCUPANCY_2"
     * @const
     */
    "2": "OCCUPANCY_2",

    /**
     * value: "OCCUPANCY_3"
     * @const
     */
    "3": "OCCUPANCY_3",

    /**
     * value: "OCCUPANCY_4"
     * @const
     */
    "4": "OCCUPANCY_4",

    /**
     * value: "OCCUPANCY_OVER_4"
     * @const
     */
    "OVER_4": "OCCUPANCY_OVER_4"
};



export default PropertyPerformanceResult;

