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
import AnalyticsDeviceCounts200ResponseDailyInner from './AnalyticsDeviceCounts200ResponseDailyInner';

/**
 * The AnalyticsCrashCounts200Response model module.
 * @module model/AnalyticsCrashCounts200Response
 * @version v0.1
 */
class AnalyticsCrashCounts200Response {
    /**
     * Constructs a new <code>AnalyticsCrashCounts200Response</code>.
     * @alias module:model/AnalyticsCrashCounts200Response
     */
    constructor() { 
        
        AnalyticsCrashCounts200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalyticsCrashCounts200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalyticsCrashCounts200Response} obj Optional instance to populate.
     * @return {module:model/AnalyticsCrashCounts200Response} The populated <code>AnalyticsCrashCounts200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalyticsCrashCounts200Response();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('crashes')) {
                obj['crashes'] = ApiClient.convertToType(data['crashes'], [AnalyticsDeviceCounts200ResponseDailyInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnalyticsCrashCounts200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnalyticsCrashCounts200Response</code>.
     */
    static validateJSON(data) {
        if (data['crashes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['crashes'])) {
                throw new Error("Expected the field `crashes` to be an array in the JSON data but got " + data['crashes']);
            }
            // validate the optional field `crashes` (array)
            for (const item of data['crashes']) {
                AnalyticsDeviceCounts200ResponseDailyInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Total crash count.
 * @member {Number} count
 */
AnalyticsCrashCounts200Response.prototype['count'] = undefined;

/**
 * The total crash count for day.
 * @member {Array.<module:model/AnalyticsDeviceCounts200ResponseDailyInner>} crashes
 */
AnalyticsCrashCounts200Response.prototype['crashes'] = undefined;






export default AnalyticsCrashCounts200Response;

