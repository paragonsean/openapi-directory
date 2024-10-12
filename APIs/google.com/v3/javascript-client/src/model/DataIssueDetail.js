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
 * The DataIssueDetail model module.
 * @module model/DataIssueDetail
 * @version v3
 */
class DataIssueDetail {
    /**
     * Constructs a new <code>DataIssueDetail</code>.
     * Details on a data issue in the listing.
     * @alias module:model/DataIssueDetail
     */
    constructor() { 
        
        DataIssueDetail.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DataIssueDetail</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DataIssueDetail} obj Optional instance to populate.
     * @return {module:model/DataIssueDetail} The populated <code>DataIssueDetail</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DataIssueDetail();

            if (data.hasOwnProperty('dataIssueSeverity')) {
                obj['dataIssueSeverity'] = ApiClient.convertToType(data['dataIssueSeverity'], 'String');
            }
            if (data.hasOwnProperty('dataIssueType')) {
                obj['dataIssueType'] = ApiClient.convertToType(data['dataIssueType'], 'String');
            }
            if (data.hasOwnProperty('isSelfResolving')) {
                obj['isSelfResolving'] = ApiClient.convertToType(data['isSelfResolving'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DataIssueDetail</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DataIssueDetail</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['dataIssueSeverity'] && !(typeof data['dataIssueSeverity'] === 'string' || data['dataIssueSeverity'] instanceof String)) {
            throw new Error("Expected the field `dataIssueSeverity` to be a primitive type in the JSON string but got " + data['dataIssueSeverity']);
        }
        // ensure the json data is a string
        if (data['dataIssueType'] && !(typeof data['dataIssueType'] === 'string' || data['dataIssueType'] instanceof String)) {
            throw new Error("Expected the field `dataIssueType` to be a primitive type in the JSON string but got " + data['dataIssueType']);
        }

        return true;
    }


}



/**
 * The severity of the data issue.
 * @member {module:model/DataIssueDetail.DataIssueSeverityEnum} dataIssueSeverity
 */
DataIssueDetail.prototype['dataIssueSeverity'] = undefined;

/**
 * The type of the data issue.
 * @member {module:model/DataIssueDetail.DataIssueTypeEnum} dataIssueType
 */
DataIssueDetail.prototype['dataIssueType'] = undefined;

/**
 * Whether or not the issue is self-resolving. If true, the issue is expected to resolve itself. If false or not set, action is needed to resolve the issue. Refer to documentation on the data issue’s type for further information.
 * @member {Boolean} isSelfResolving
 */
DataIssueDetail.prototype['isSelfResolving'] = undefined;





/**
 * Allowed values for the <code>dataIssueSeverity</code> property.
 * @enum {String}
 * @readonly
 */
DataIssueDetail['DataIssueSeverityEnum'] = {

    /**
     * value: "DATA_ISSUE_SEVERITY_UNSPECIFIED"
     * @const
     */
    "DATA_ISSUE_SEVERITY_UNSPECIFIED": "DATA_ISSUE_SEVERITY_UNSPECIFIED",

    /**
     * value: "ERROR"
     * @const
     */
    "ERROR": "ERROR",

    /**
     * value: "WARNING"
     * @const
     */
    "WARNING": "WARNING",

    /**
     * value: "INFO"
     * @const
     */
    "INFO": "INFO"
};


/**
 * Allowed values for the <code>dataIssueType</code> property.
 * @enum {String}
 * @readonly
 */
DataIssueDetail['DataIssueTypeEnum'] = {

    /**
     * value: "FEED_DATA_ISSUE_UNSPECIFIED"
     * @const
     */
    "FEED_DATA_ISSUE_UNSPECIFIED": "FEED_DATA_ISSUE_UNSPECIFIED",

    /**
     * value: "FEED_DATA_ISSUE_UNKNOWN"
     * @const
     */
    "FEED_DATA_ISSUE_UNKNOWN": "FEED_DATA_ISSUE_UNKNOWN",

    /**
     * value: "NO_DATA_ISSUE"
     * @const
     */
    "NO_DATA_ISSUE": "NO_DATA_ISSUE",

    /**
     * value: "DUPLICATE_ADDRESS"
     * @const
     */
    "DUPLICATE_ADDRESS": "DUPLICATE_ADDRESS",

    /**
     * value: "MISSING_PHYSICAL_STREET_ADDRESS"
     * @const
     */
    "MISSING_PHYSICAL_STREET_ADDRESS": "MISSING_PHYSICAL_STREET_ADDRESS",

    /**
     * value: "MISSING_STREET_NAME"
     * @const
     */
    "MISSING_STREET_NAME": "MISSING_STREET_NAME",

    /**
     * value: "MISSING_STREET_NUMBER"
     * @const
     */
    "MISSING_STREET_NUMBER": "MISSING_STREET_NUMBER",

    /**
     * value: "MISSING_ADDRESS"
     * @const
     */
    "MISSING_ADDRESS": "MISSING_ADDRESS",

    /**
     * value: "MISSING_COUNTRY"
     * @const
     */
    "MISSING_COUNTRY": "MISSING_COUNTRY",

    /**
     * value: "INVALID_POSTAL_CODE"
     * @const
     */
    "INVALID_POSTAL_CODE": "INVALID_POSTAL_CODE",

    /**
     * value: "INVALID_POSTAL_CODE_SUFFIX"
     * @const
     */
    "INVALID_POSTAL_CODE_SUFFIX": "INVALID_POSTAL_CODE_SUFFIX",

    /**
     * value: "UNEXPECTED_POSTAL_CODE_SUFFIX"
     * @const
     */
    "UNEXPECTED_POSTAL_CODE_SUFFIX": "UNEXPECTED_POSTAL_CODE_SUFFIX",

    /**
     * value: "UNEXPECTED_POSTAL_CODE"
     * @const
     */
    "UNEXPECTED_POSTAL_CODE": "UNEXPECTED_POSTAL_CODE",

    /**
     * value: "INVALID_AMENITIES"
     * @const
     */
    "INVALID_AMENITIES": "INVALID_AMENITIES",

    /**
     * value: "INVALID_EMAIL_ADDRESS"
     * @const
     */
    "INVALID_EMAIL_ADDRESS": "INVALID_EMAIL_ADDRESS",

    /**
     * value: "DUPLICATE_LATLONG"
     * @const
     */
    "DUPLICATE_LATLONG": "DUPLICATE_LATLONG",

    /**
     * value: "LATLONG_INCONSISTENT_WITH_ADDRESS"
     * @const
     */
    "LATLONG_INCONSISTENT_WITH_ADDRESS": "LATLONG_INCONSISTENT_WITH_ADDRESS",

    /**
     * value: "MISSING_LATLONG"
     * @const
     */
    "MISSING_LATLONG": "MISSING_LATLONG",

    /**
     * value: "COULD_NOT_GEOCODE"
     * @const
     */
    "COULD_NOT_GEOCODE": "COULD_NOT_GEOCODE",

    /**
     * value: "MISSING_HOTEL_NAME"
     * @const
     */
    "MISSING_HOTEL_NAME": "MISSING_HOTEL_NAME",

    /**
     * value: "HOTEL_NAME_EMPTY"
     * @const
     */
    "HOTEL_NAME_EMPTY": "HOTEL_NAME_EMPTY",

    /**
     * value: "INVALID_HOTEL_NAME"
     * @const
     */
    "INVALID_HOTEL_NAME": "INVALID_HOTEL_NAME",

    /**
     * value: "HOTEL_NAME_TOO_LONG"
     * @const
     */
    "HOTEL_NAME_TOO_LONG": "HOTEL_NAME_TOO_LONG",

    /**
     * value: "PARSE_ERROR_IN_XML"
     * @const
     */
    "PARSE_ERROR_IN_XML": "PARSE_ERROR_IN_XML",

    /**
     * value: "UNEXPECTED_ATTRIBUTE_IN_XML"
     * @const
     */
    "UNEXPECTED_ATTRIBUTE_IN_XML": "UNEXPECTED_ATTRIBUTE_IN_XML",

    /**
     * value: "DUPLICATE_PHONE_NUMBER"
     * @const
     */
    "DUPLICATE_PHONE_NUMBER": "DUPLICATE_PHONE_NUMBER",

    /**
     * value: "MISSING_PHONE_NUMBER"
     * @const
     */
    "MISSING_PHONE_NUMBER": "MISSING_PHONE_NUMBER",

    /**
     * value: "MISSING_VOICE_PHONE_NUMBER"
     * @const
     */
    "MISSING_VOICE_PHONE_NUMBER": "MISSING_VOICE_PHONE_NUMBER",

    /**
     * value: "INVALID_PHONE_NUMBER_FORMAT"
     * @const
     */
    "INVALID_PHONE_NUMBER_FORMAT": "INVALID_PHONE_NUMBER_FORMAT",

    /**
     * value: "INVALID_PHONE_NUMBER"
     * @const
     */
    "INVALID_PHONE_NUMBER": "INVALID_PHONE_NUMBER",

    /**
     * value: "INVALID_PHONE_NUMBER_COUNTRY_CODE"
     * @const
     */
    "INVALID_PHONE_NUMBER_COUNTRY_CODE": "INVALID_PHONE_NUMBER_COUNTRY_CODE",

    /**
     * value: "PHONE_NUMBER_TOO_LONG"
     * @const
     */
    "PHONE_NUMBER_TOO_LONG": "PHONE_NUMBER_TOO_LONG",

    /**
     * value: "PHONE_NUMBER_TOO_SHORT"
     * @const
     */
    "PHONE_NUMBER_TOO_SHORT": "PHONE_NUMBER_TOO_SHORT",

    /**
     * value: "INVALID_WEBSITE_URL"
     * @const
     */
    "INVALID_WEBSITE_URL": "INVALID_WEBSITE_URL",

    /**
     * value: "ADWORDS_ATTRIBUTE_TOO_LONG"
     * @const
     */
    "ADWORDS_ATTRIBUTE_TOO_LONG": "ADWORDS_ATTRIBUTE_TOO_LONG",

    /**
     * value: "BRAND_NOT_ALLOWED"
     * @const
     */
    "BRAND_NOT_ALLOWED": "BRAND_NOT_ALLOWED",

    /**
     * value: "FLAGGED_DUE_TO_SUSPICIOUS_METADATA"
     * @const
     */
    "FLAGGED_DUE_TO_SUSPICIOUS_METADATA": "FLAGGED_DUE_TO_SUSPICIOUS_METADATA",

    /**
     * value: "NOT_ENOUGH_IMAGES_PROVIDED"
     * @const
     */
    "NOT_ENOUGH_IMAGES_PROVIDED": "NOT_ENOUGH_IMAGES_PROVIDED",

    /**
     * value: "IMAGE_PROCESSING_IN_PROGRESS"
     * @const
     */
    "IMAGE_PROCESSING_IN_PROGRESS": "IMAGE_PROCESSING_IN_PROGRESS",

    /**
     * value: "CANNOT_FETCH_IMAGES"
     * @const
     */
    "CANNOT_FETCH_IMAGES": "CANNOT_FETCH_IMAGES",

    /**
     * value: "INCOMPATIBLE_IMAGE_SIZE_OR_LOW_QUALITY"
     * @const
     */
    "INCOMPATIBLE_IMAGE_SIZE_OR_LOW_QUALITY": "INCOMPATIBLE_IMAGE_SIZE_OR_LOW_QUALITY",

    /**
     * value: "MISSING_LANG_IN_RAW_LISTING"
     * @const
     */
    "MISSING_LANG_IN_RAW_LISTING": "MISSING_LANG_IN_RAW_LISTING",

    /**
     * value: "IS_HOTEL"
     * @const
     */
    "IS_HOTEL": "IS_HOTEL",

    /**
     * value: "MISSING_REQ_ATTR"
     * @const
     */
    "MISSING_REQ_ATTR": "MISSING_REQ_ATTR",

    /**
     * value: "MISSING_NAME"
     * @const
     */
    "MISSING_NAME": "MISSING_NAME",

    /**
     * value: "MISSING_LANG_IN_NAME"
     * @const
     */
    "MISSING_LANG_IN_NAME": "MISSING_LANG_IN_NAME",

    /**
     * value: "VR_NAME_TOO_LONG"
     * @const
     */
    "VR_NAME_TOO_LONG": "VR_NAME_TOO_LONG",

    /**
     * value: "TEST_PROPERTY"
     * @const
     */
    "TEST_PROPERTY": "TEST_PROPERTY",

    /**
     * value: "NON_VR_ACCOMMODATION_TYPE_BASED_ON_LISTING_NAME"
     * @const
     */
    "NON_VR_ACCOMMODATION_TYPE_BASED_ON_LISTING_NAME": "NON_VR_ACCOMMODATION_TYPE_BASED_ON_LISTING_NAME",

    /**
     * value: "BRAND_NAME_TOO_LONG"
     * @const
     */
    "BRAND_NAME_TOO_LONG": "BRAND_NAME_TOO_LONG",

    /**
     * value: "MISSING_BRAND_NAME"
     * @const
     */
    "MISSING_BRAND_NAME": "MISSING_BRAND_NAME",

    /**
     * value: "INVALID_REVIEW_RATING"
     * @const
     */
    "INVALID_REVIEW_RATING": "INVALID_REVIEW_RATING",

    /**
     * value: "INVALID_CHECKIN_FORMAT"
     * @const
     */
    "INVALID_CHECKIN_FORMAT": "INVALID_CHECKIN_FORMAT",

    /**
     * value: "INVALID_CHECKOUT_FORMAT"
     * @const
     */
    "INVALID_CHECKOUT_FORMAT": "INVALID_CHECKOUT_FORMAT"
};



export default DataIssueDetail;

