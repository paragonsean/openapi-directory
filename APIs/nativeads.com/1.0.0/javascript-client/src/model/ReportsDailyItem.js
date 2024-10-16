/**
 * Native Ads Publisher API
 * This is a Native Ads Publisher API it provides same functionality as Native Ads Publisher Account GUI. 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ReportsDailyItem model module.
 * @module model/ReportsDailyItem
 * @version 1.0.0
 */
class ReportsDailyItem {
    /**
     * Constructs a new <code>ReportsDailyItem</code>.
     * @alias module:model/ReportsDailyItem
     */
    constructor() { 
        
        ReportsDailyItem.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ReportsDailyItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReportsDailyItem} obj Optional instance to populate.
     * @return {module:model/ReportsDailyItem} The populated <code>ReportsDailyItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReportsDailyItem();

            if (data.hasOwnProperty('clicks')) {
                obj['clicks'] = ApiClient.convertToType(data['clicks'], 'String');
            }
            if (data.hasOwnProperty('cpc')) {
                obj['cpc'] = ApiClient.convertToType(data['cpc'], 'String');
            }
            if (data.hasOwnProperty('ctr')) {
                obj['ctr'] = ApiClient.convertToType(data['ctr'], 'String');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
            if (data.hasOwnProperty('earnings')) {
                obj['earnings'] = ApiClient.convertToType(data['earnings'], 'String');
            }
            if (data.hasOwnProperty('impressions')) {
                obj['impressions'] = ApiClient.convertToType(data['impressions'], 'String');
            }
            if (data.hasOwnProperty('net_ecpm')) {
                obj['net_ecpm'] = ApiClient.convertToType(data['net_ecpm'], 'String');
            }
            if (data.hasOwnProperty('rpm')) {
                obj['rpm'] = ApiClient.convertToType(data['rpm'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ReportsDailyItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReportsDailyItem</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['clicks'] && !(typeof data['clicks'] === 'string' || data['clicks'] instanceof String)) {
            throw new Error("Expected the field `clicks` to be a primitive type in the JSON string but got " + data['clicks']);
        }
        // ensure the json data is a string
        if (data['cpc'] && !(typeof data['cpc'] === 'string' || data['cpc'] instanceof String)) {
            throw new Error("Expected the field `cpc` to be a primitive type in the JSON string but got " + data['cpc']);
        }
        // ensure the json data is a string
        if (data['ctr'] && !(typeof data['ctr'] === 'string' || data['ctr'] instanceof String)) {
            throw new Error("Expected the field `ctr` to be a primitive type in the JSON string but got " + data['ctr']);
        }
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }
        // ensure the json data is a string
        if (data['earnings'] && !(typeof data['earnings'] === 'string' || data['earnings'] instanceof String)) {
            throw new Error("Expected the field `earnings` to be a primitive type in the JSON string but got " + data['earnings']);
        }
        // ensure the json data is a string
        if (data['impressions'] && !(typeof data['impressions'] === 'string' || data['impressions'] instanceof String)) {
            throw new Error("Expected the field `impressions` to be a primitive type in the JSON string but got " + data['impressions']);
        }
        // ensure the json data is a string
        if (data['net_ecpm'] && !(typeof data['net_ecpm'] === 'string' || data['net_ecpm'] instanceof String)) {
            throw new Error("Expected the field `net_ecpm` to be a primitive type in the JSON string but got " + data['net_ecpm']);
        }
        // ensure the json data is a string
        if (data['rpm'] && !(typeof data['rpm'] === 'string' || data['rpm'] instanceof String)) {
            throw new Error("Expected the field `rpm` to be a primitive type in the JSON string but got " + data['rpm']);
        }

        return true;
    }


}



/**
 * @member {String} clicks
 */
ReportsDailyItem.prototype['clicks'] = undefined;

/**
 * @member {String} cpc
 */
ReportsDailyItem.prototype['cpc'] = undefined;

/**
 * @member {String} ctr
 */
ReportsDailyItem.prototype['ctr'] = undefined;

/**
 * @member {String} date
 */
ReportsDailyItem.prototype['date'] = undefined;

/**
 * @member {String} earnings
 */
ReportsDailyItem.prototype['earnings'] = undefined;

/**
 * @member {String} impressions
 */
ReportsDailyItem.prototype['impressions'] = undefined;

/**
 * @member {String} net_ecpm
 */
ReportsDailyItem.prototype['net_ecpm'] = undefined;

/**
 * @member {String} rpm
 */
ReportsDailyItem.prototype['rpm'] = undefined;






export default ReportsDailyItem;

