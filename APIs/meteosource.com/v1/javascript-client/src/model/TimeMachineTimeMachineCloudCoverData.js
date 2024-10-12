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
 * The TimeMachineTimeMachineCloudCoverData model module.
 * @module model/TimeMachineTimeMachineCloudCoverData
 * @version v1
 */
class TimeMachineTimeMachineCloudCoverData {
    /**
     * Constructs a new <code>TimeMachineTimeMachineCloudCoverData</code>.
     * @alias module:model/TimeMachineTimeMachineCloudCoverData
     */
    constructor() { 
        
        TimeMachineTimeMachineCloudCoverData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TimeMachineTimeMachineCloudCoverData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TimeMachineTimeMachineCloudCoverData} obj Optional instance to populate.
     * @return {module:model/TimeMachineTimeMachineCloudCoverData} The populated <code>TimeMachineTimeMachineCloudCoverData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TimeMachineTimeMachineCloudCoverData();

            if (data.hasOwnProperty('high')) {
                obj['high'] = ApiClient.convertToType(data['high'], 'Number');
            }
            if (data.hasOwnProperty('low')) {
                obj['low'] = ApiClient.convertToType(data['low'], 'Number');
            }
            if (data.hasOwnProperty('middle')) {
                obj['middle'] = ApiClient.convertToType(data['middle'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TimeMachineTimeMachineCloudCoverData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TimeMachineTimeMachineCloudCoverData</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Percentage of sky covered by high clouds. Unit: %
 * @member {Number} high
 */
TimeMachineTimeMachineCloudCoverData.prototype['high'] = undefined;

/**
 * Percentage of sky covered by low clouds. Unit: %
 * @member {Number} low
 */
TimeMachineTimeMachineCloudCoverData.prototype['low'] = undefined;

/**
 * Percentage of sky covered by middle clouds. Unit: %
 * @member {Number} middle
 */
TimeMachineTimeMachineCloudCoverData.prototype['middle'] = undefined;

/**
 * Percentage of sky covered by clouds. Unit: %
 * @member {Number} total
 */
TimeMachineTimeMachineCloudCoverData.prototype['total'] = undefined;






export default TimeMachineTimeMachineCloudCoverData;

