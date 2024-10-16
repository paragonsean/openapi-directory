/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner model module.
 * @module model/ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner
 * @version v0.1
 */
class ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner {
    /**
     * Constructs a new <code>ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner</code>.
     * @alias module:model/ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner
     */
    constructor() { 
        
        ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner} obj Optional instance to populate.
     * @return {module:model/ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner} The populated <code>ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner();

            if (data.hasOwnProperty('datetime')) {
                obj['datetime'] = ApiClient.convertToType(data['datetime'], 'String');
            }
            if (data.hasOwnProperty('percentage')) {
                obj['percentage'] = ApiClient.convertToType(data['percentage'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['datetime'] && !(typeof data['datetime'] === 'string' || data['datetime'] instanceof String)) {
            throw new Error("Expected the field `datetime` to be a primitive type in the JSON string but got " + data['datetime']);
        }

        return true;
    }


}



/**
 * the ISO 8601 datetime
 * @member {String} datetime
 */
ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner.prototype['datetime'] = undefined;

/**
 * percentage of the object
 * @member {Number} percentage
 */
ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner.prototype['percentage'] = undefined;






export default ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner;

