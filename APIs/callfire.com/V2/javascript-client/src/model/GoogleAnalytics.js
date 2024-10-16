/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GoogleAnalytics model module.
 * @module model/GoogleAnalytics
 * @version V2
 */
class GoogleAnalytics {
    /**
     * Constructs a new <code>GoogleAnalytics</code>.
     * Google Analytics for Call Tracking
     * @alias module:model/GoogleAnalytics
     */
    constructor() { 
        
        GoogleAnalytics.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GoogleAnalytics</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GoogleAnalytics} obj Optional instance to populate.
     * @return {module:model/GoogleAnalytics} The populated <code>GoogleAnalytics</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GoogleAnalytics();

            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], 'String');
            }
            if (data.hasOwnProperty('domain')) {
                obj['domain'] = ApiClient.convertToType(data['domain'], 'String');
            }
            if (data.hasOwnProperty('googleAccountId')) {
                obj['googleAccountId'] = ApiClient.convertToType(data['googleAccountId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GoogleAnalytics</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GoogleAnalytics</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['category'] && !(typeof data['category'] === 'string' || data['category'] instanceof String)) {
            throw new Error("Expected the field `category` to be a primitive type in the JSON string but got " + data['category']);
        }
        // ensure the json data is a string
        if (data['domain'] && !(typeof data['domain'] === 'string' || data['domain'] instanceof String)) {
            throw new Error("Expected the field `domain` to be a primitive type in the JSON string but got " + data['domain']);
        }
        // ensure the json data is a string
        if (data['googleAccountId'] && !(typeof data['googleAccountId'] === 'string' || data['googleAccountId'] instanceof String)) {
            throw new Error("Expected the field `googleAccountId` to be a primitive type in the JSON string but got " + data['googleAccountId']);
        }

        return true;
    }


}



/**
 * A category to group. For example: Sales or Support
 * @member {String} category
 */
GoogleAnalytics.prototype['category'] = undefined;

/**
 * A domain name for analytics
 * @member {String} domain
 */
GoogleAnalytics.prototype['domain'] = undefined;

/**
 * An id of a Google account, example: UA-XXXXX-2X
 * @member {String} googleAccountId
 */
GoogleAnalytics.prototype['googleAccountId'] = undefined;






export default GoogleAnalytics;

