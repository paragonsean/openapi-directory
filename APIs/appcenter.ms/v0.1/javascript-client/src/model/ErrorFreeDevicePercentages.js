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
import ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner from './ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner';

/**
 * The ErrorFreeDevicePercentages model module.
 * @module model/ErrorFreeDevicePercentages
 * @version v0.1
 */
class ErrorFreeDevicePercentages {
    /**
     * Constructs a new <code>ErrorFreeDevicePercentages</code>.
     * @alias module:model/ErrorFreeDevicePercentages
     */
    constructor() { 
        
        ErrorFreeDevicePercentages.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ErrorFreeDevicePercentages</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ErrorFreeDevicePercentages} obj Optional instance to populate.
     * @return {module:model/ErrorFreeDevicePercentages} The populated <code>ErrorFreeDevicePercentages</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ErrorFreeDevicePercentages();

            if (data.hasOwnProperty('averagePercentage')) {
                obj['averagePercentage'] = ApiClient.convertToType(data['averagePercentage'], 'Number');
            }
            if (data.hasOwnProperty('dailyPercentages')) {
                obj['dailyPercentages'] = ApiClient.convertToType(data['dailyPercentages'], [ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ErrorFreeDevicePercentages</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ErrorFreeDevicePercentages</code>.
     */
    static validateJSON(data) {
        if (data['dailyPercentages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['dailyPercentages'])) {
                throw new Error("Expected the field `dailyPercentages` to be an array in the JSON data but got " + data['dailyPercentages']);
            }
            // validate the optional field `dailyPercentages` (array)
            for (const item of data['dailyPercentages']) {
                ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Average percentage
 * @member {Number} averagePercentage
 */
ErrorFreeDevicePercentages.prototype['averagePercentage'] = undefined;

/**
 * The error-free percentage per day.
 * @member {Array.<module:model/ErrorsGroupErrorFreeDevicePercentages200ResponseDailyPercentagesInner>} dailyPercentages
 */
ErrorFreeDevicePercentages.prototype['dailyPercentages'] = undefined;






export default ErrorFreeDevicePercentages;

