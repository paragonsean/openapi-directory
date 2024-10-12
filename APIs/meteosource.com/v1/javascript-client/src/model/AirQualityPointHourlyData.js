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
 * The AirQualityPointHourlyData model module.
 * @module model/AirQualityPointHourlyData
 * @version v1
 */
class AirQualityPointHourlyData {
    /**
     * Constructs a new <code>AirQualityPointHourlyData</code>.
     * @alias module:model/AirQualityPointHourlyData
     */
    constructor() { 
        
        AirQualityPointHourlyData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AirQualityPointHourlyData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AirQualityPointHourlyData} obj Optional instance to populate.
     * @return {module:model/AirQualityPointHourlyData} The populated <code>AirQualityPointHourlyData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AirQualityPointHourlyData();

            if (data.hasOwnProperty('aerosol_550')) {
                obj['aerosol_550'] = ApiClient.convertToType(data['aerosol_550'], 'Number');
            }
            if (data.hasOwnProperty('air_quality')) {
                obj['air_quality'] = ApiClient.convertToType(data['air_quality'], 'Number');
            }
            if (data.hasOwnProperty('co_surface')) {
                obj['co_surface'] = ApiClient.convertToType(data['co_surface'], 'Number');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'Date');
            }
            if (data.hasOwnProperty('dust_550nm')) {
                obj['dust_550nm'] = ApiClient.convertToType(data['dust_550nm'], 'Number');
            }
            if (data.hasOwnProperty('dust_mixing_ratio_05')) {
                obj['dust_mixing_ratio_05'] = ApiClient.convertToType(data['dust_mixing_ratio_05'], 'Number');
            }
            if (data.hasOwnProperty('no2_surface')) {
                obj['no2_surface'] = ApiClient.convertToType(data['no2_surface'], 'Number');
            }
            if (data.hasOwnProperty('no_surface')) {
                obj['no_surface'] = ApiClient.convertToType(data['no_surface'], 'Number');
            }
            if (data.hasOwnProperty('ozone_surface')) {
                obj['ozone_surface'] = ApiClient.convertToType(data['ozone_surface'], 'Number');
            }
            if (data.hasOwnProperty('ozone_total')) {
                obj['ozone_total'] = ApiClient.convertToType(data['ozone_total'], 'Number');
            }
            if (data.hasOwnProperty('pm10')) {
                obj['pm10'] = ApiClient.convertToType(data['pm10'], 'Number');
            }
            if (data.hasOwnProperty('pm25')) {
                obj['pm25'] = ApiClient.convertToType(data['pm25'], 'Number');
            }
            if (data.hasOwnProperty('so2_surface')) {
                obj['so2_surface'] = ApiClient.convertToType(data['so2_surface'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AirQualityPointHourlyData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AirQualityPointHourlyData</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Total aerosol optical depth at 550 nm. Unit: dimensionless
 * @member {Number} aerosol_550
 */
AirQualityPointHourlyData.prototype['aerosol_550'] = undefined;

/**
 * Air quality index. The following values can appear:  * 1 - Very good * 2 - Good * 3 - Medium * 4 - Poor * 5 - Very poor * 6 - Extremely poor  Unit: index
 * @member {Number} air_quality
 */
AirQualityPointHourlyData.prototype['air_quality'] = undefined;

/**
 * Carbon monoxide at surface level. Unit: µg/m3
 * @member {Number} co_surface
 */
AirQualityPointHourlyData.prototype['co_surface'] = undefined;

/**
 * Datetime in YYYY-MM-DDTHH:MM:SS format.
 * @member {Date} date
 */
AirQualityPointHourlyData.prototype['date'] = undefined;

/**
 * Dust aerosol optical depth at 550 nm. Unit: dimensionless
 * @member {Number} dust_550nm
 */
AirQualityPointHourlyData.prototype['dust_550nm'] = undefined;

/**
 * Dust aerosol (0.55 - 0.9 µm) mixing ratio. Unit: kg/kg
 * @member {Number} dust_mixing_ratio_05
 */
AirQualityPointHourlyData.prototype['dust_mixing_ratio_05'] = undefined;

/**
 * Nitrogen dioxide at surface level. Unit: µg/m3
 * @member {Number} no2_surface
 */
AirQualityPointHourlyData.prototype['no2_surface'] = undefined;

/**
 * Nitrogen monoxide at surface level. Unit: µg/m3
 * @member {Number} no_surface
 */
AirQualityPointHourlyData.prototype['no_surface'] = undefined;

/**
 * Ozone. Unit: µg/m3
 * @member {Number} ozone_surface
 */
AirQualityPointHourlyData.prototype['ozone_surface'] = undefined;

/**
 * Total column ozone. Unit: Dobson
 * @member {Number} ozone_total
 */
AirQualityPointHourlyData.prototype['ozone_total'] = undefined;

/**
 * Particulate matter d < 10 µm (PM10). Unit: µg/m3
 * @member {Number} pm10
 */
AirQualityPointHourlyData.prototype['pm10'] = undefined;

/**
 * Particulate matter d < 2.5 µm (PM2.5). Unit: µg/m3
 * @member {Number} pm25
 */
AirQualityPointHourlyData.prototype['pm25'] = undefined;

/**
 * Sulphur dioxide at surface level. Unit: µg/m3
 * @member {Number} so2_surface
 */
AirQualityPointHourlyData.prototype['so2_surface'] = undefined;






export default AirQualityPointHourlyData;

