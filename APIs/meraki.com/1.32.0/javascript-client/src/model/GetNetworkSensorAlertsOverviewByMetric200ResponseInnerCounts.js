/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCountsNoise from './GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCountsNoise';

/**
 * The GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts model module.
 * @module model/GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts
 * @version 1.32.0
 */
class GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts {
    /**
     * Constructs a new <code>GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts</code>.
     * Counts of sensor alerts over the timespan, by reading metric
     * @alias module:model/GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts
     */
    constructor() { 
        
        GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts} obj Optional instance to populate.
     * @return {module:model/GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts} The populated <code>GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts();

            if (data.hasOwnProperty('door')) {
                obj['door'] = ApiClient.convertToType(data['door'], 'Number');
            }
            if (data.hasOwnProperty('humidity')) {
                obj['humidity'] = ApiClient.convertToType(data['humidity'], 'Number');
            }
            if (data.hasOwnProperty('indoorAirQuality')) {
                obj['indoorAirQuality'] = ApiClient.convertToType(data['indoorAirQuality'], 'Number');
            }
            if (data.hasOwnProperty('noise')) {
                obj['noise'] = GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCountsNoise.constructFromObject(data['noise']);
            }
            if (data.hasOwnProperty('pm25')) {
                obj['pm25'] = ApiClient.convertToType(data['pm25'], 'Number');
            }
            if (data.hasOwnProperty('temperature')) {
                obj['temperature'] = ApiClient.convertToType(data['temperature'], 'Number');
            }
            if (data.hasOwnProperty('tvoc')) {
                obj['tvoc'] = ApiClient.convertToType(data['tvoc'], 'Number');
            }
            if (data.hasOwnProperty('water')) {
                obj['water'] = ApiClient.convertToType(data['water'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts</code>.
     */
    static validateJSON(data) {
        // validate the optional field `noise`
        if (data['noise']) { // data not null
          GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCountsNoise.validateJSON(data['noise']);
        }

        return true;
    }


}



/**
 * Number of sensor alerts that occurred due to an open door
 * @member {Number} door
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['door'] = undefined;

/**
 * Number of sensor alerts that occurred due to humidity readings
 * @member {Number} humidity
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['humidity'] = undefined;

/**
 * Number of sensor alerts that occurred due to indoor air quality readings
 * @member {Number} indoorAirQuality
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['indoorAirQuality'] = undefined;

/**
 * @member {module:model/GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCountsNoise} noise
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['noise'] = undefined;

/**
 * Number of sensor alerts that occurred due to PM2.5 readings
 * @member {Number} pm25
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['pm25'] = undefined;

/**
 * Number of sensor alerts that occurred due to temperature readings
 * @member {Number} temperature
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['temperature'] = undefined;

/**
 * Number of sensor alerts that occurred due to TVOC readings
 * @member {Number} tvoc
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['tvoc'] = undefined;

/**
 * Number of sensor alerts that occurred due to the presence of water
 * @member {Number} water
 */
GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts.prototype['water'] = undefined;






export default GetNetworkSensorAlertsOverviewByMetric200ResponseInnerCounts;

