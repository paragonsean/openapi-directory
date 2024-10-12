/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PointPointDailyStatsTemperatureData model module.
 * @module model/PointPointDailyStatsTemperatureData
 * @version v1
 */
class PointPointDailyStatsTemperatureData {
    /**
     * Constructs a new <code>PointPointDailyStatsTemperatureData</code>.
     * @alias module:model/PointPointDailyStatsTemperatureData
     */
    constructor() { 
        
        PointPointDailyStatsTemperatureData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PointPointDailyStatsTemperatureData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PointPointDailyStatsTemperatureData} obj Optional instance to populate.
     * @return {module:model/PointPointDailyStatsTemperatureData} The populated <code>PointPointDailyStatsTemperatureData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PointPointDailyStatsTemperatureData();

            if (data.hasOwnProperty('avg')) {
                obj['avg'] = ApiClient.convertToType(data['avg'], 'Number');
            }
            if (data.hasOwnProperty('avg_max')) {
                obj['avg_max'] = ApiClient.convertToType(data['avg_max'], 'Number');
            }
            if (data.hasOwnProperty('avg_min')) {
                obj['avg_min'] = ApiClient.convertToType(data['avg_min'], 'Number');
            }
            if (data.hasOwnProperty('record_max')) {
                obj['record_max'] = ApiClient.convertToType(data['record_max'], 'Number');
            }
            if (data.hasOwnProperty('record_min')) {
                obj['record_min'] = ApiClient.convertToType(data['record_min'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PointPointDailyStatsTemperatureData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PointPointDailyStatsTemperatureData</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Long-term temperature average. Units: metric = °C, us = °F, uk = °C, ca = °C
 * @member {Number} avg
 */
PointPointDailyStatsTemperatureData.prototype['avg'] = undefined;

/**
 * Long-term daily maximum temperature average. Units: metric = °C, us = °F, uk = °C, ca = °C
 * @member {Number} avg_max
 */
PointPointDailyStatsTemperatureData.prototype['avg_max'] = undefined;

/**
 * Long-term daily minimum temperature average. Units: metric = °C, us = °F, uk = °C, ca = °C
 * @member {Number} avg_min
 */
PointPointDailyStatsTemperatureData.prototype['avg_min'] = undefined;

/**
 * Historical daily maximum. Units: metric = °C, us = °F, uk = °C, ca = °C
 * @member {Number} record_max
 */
PointPointDailyStatsTemperatureData.prototype['record_max'] = undefined;

/**
 * Historical daily minimum temperature. Units: metric = °C, us = °F, uk = °C, ca = °C
 * @member {Number} record_min
 */
PointPointDailyStatsTemperatureData.prototype['record_min'] = undefined;






export default PointPointDailyStatsTemperatureData;

