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
 * The PointPointHourlyPrecipitationData model module.
 * @module model/PointPointHourlyPrecipitationData
 * @version v1
 */
class PointPointHourlyPrecipitationData {
    /**
     * Constructs a new <code>PointPointHourlyPrecipitationData</code>.
     * @alias module:model/PointPointHourlyPrecipitationData
     */
    constructor() { 
        
        PointPointHourlyPrecipitationData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PointPointHourlyPrecipitationData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PointPointHourlyPrecipitationData} obj Optional instance to populate.
     * @return {module:model/PointPointHourlyPrecipitationData} The populated <code>PointPointHourlyPrecipitationData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PointPointHourlyPrecipitationData();

            if (data.hasOwnProperty('convective')) {
                obj['convective'] = ApiClient.convertToType(data['convective'], 'Number');
            }
            if (data.hasOwnProperty('rainspot')) {
                obj['rainspot'] = ApiClient.convertToType(data['rainspot'], File);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], File);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PointPointHourlyPrecipitationData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PointPointHourlyPrecipitationData</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Total precipitation amount accumulated since last hour. Units: metric = mm/h, us = inches per hour, uk = mm/h, ca = mm/h
 * @member {Number} convective
 */
PointPointHourlyPrecipitationData.prototype['convective'] = undefined;

/**
 * Precipitation in the surrounding of queried location. The data is 7x7 ASCII art string, queried location being in the center. Character `#` means there is precipitation, `.` means no precipitation. The distance between neighboring cells is 0.25°. Unit: rainspot
 * @member {File} rainspot
 */
PointPointHourlyPrecipitationData.prototype['rainspot'] = undefined;

/**
 * Total precipitation amount accumulated since last hour. Units: metric = mm/h, us = inches per hour, uk = mm/h, ca = mm/h
 * @member {Number} total
 */
PointPointHourlyPrecipitationData.prototype['total'] = undefined;

/**
 * Precipitation type, may be one of:  * `none`, it there is no precipitation * `rain` * `snow` * `rain_snow` * `ice pellets` * `frozen rain`  Unit: precipitation type
 * @member {File} type
 */
PointPointHourlyPrecipitationData.prototype['type'] = undefined;






export default PointPointHourlyPrecipitationData;

