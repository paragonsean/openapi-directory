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
import GetOrganizationSensorReadingsHistory200ResponseInnerBattery from './GetOrganizationSensorReadingsHistory200ResponseInnerBattery';
import GetOrganizationSensorReadingsHistory200ResponseInnerButton from './GetOrganizationSensorReadingsHistory200ResponseInnerButton';
import GetOrganizationSensorReadingsHistory200ResponseInnerDoor from './GetOrganizationSensorReadingsHistory200ResponseInnerDoor';
import GetOrganizationSensorReadingsHistory200ResponseInnerHumidity from './GetOrganizationSensorReadingsHistory200ResponseInnerHumidity';
import GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality from './GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality';
import GetOrganizationSensorReadingsHistory200ResponseInnerNoise from './GetOrganizationSensorReadingsHistory200ResponseInnerNoise';
import GetOrganizationSensorReadingsHistory200ResponseInnerPm25 from './GetOrganizationSensorReadingsHistory200ResponseInnerPm25';
import GetOrganizationSensorReadingsHistory200ResponseInnerTemperature from './GetOrganizationSensorReadingsHistory200ResponseInnerTemperature';
import GetOrganizationSensorReadingsHistory200ResponseInnerTvoc from './GetOrganizationSensorReadingsHistory200ResponseInnerTvoc';
import GetOrganizationSensorReadingsHistory200ResponseInnerWater from './GetOrganizationSensorReadingsHistory200ResponseInnerWater';

/**
 * The GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner model module.
 * @module model/GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner
 * @version 1.32.0
 */
class GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner {
    /**
     * Constructs a new <code>GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner</code>.
     * @alias module:model/GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner
     */
    constructor() { 
        
        GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner} obj Optional instance to populate.
     * @return {module:model/GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner} The populated <code>GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner();

            if (data.hasOwnProperty('battery')) {
                obj['battery'] = GetOrganizationSensorReadingsHistory200ResponseInnerBattery.constructFromObject(data['battery']);
            }
            if (data.hasOwnProperty('button')) {
                obj['button'] = GetOrganizationSensorReadingsHistory200ResponseInnerButton.constructFromObject(data['button']);
            }
            if (data.hasOwnProperty('door')) {
                obj['door'] = GetOrganizationSensorReadingsHistory200ResponseInnerDoor.constructFromObject(data['door']);
            }
            if (data.hasOwnProperty('humidity')) {
                obj['humidity'] = GetOrganizationSensorReadingsHistory200ResponseInnerHumidity.constructFromObject(data['humidity']);
            }
            if (data.hasOwnProperty('indoorAirQuality')) {
                obj['indoorAirQuality'] = GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality.constructFromObject(data['indoorAirQuality']);
            }
            if (data.hasOwnProperty('metric')) {
                obj['metric'] = ApiClient.convertToType(data['metric'], 'String');
            }
            if (data.hasOwnProperty('noise')) {
                obj['noise'] = GetOrganizationSensorReadingsHistory200ResponseInnerNoise.constructFromObject(data['noise']);
            }
            if (data.hasOwnProperty('pm25')) {
                obj['pm25'] = GetOrganizationSensorReadingsHistory200ResponseInnerPm25.constructFromObject(data['pm25']);
            }
            if (data.hasOwnProperty('temperature')) {
                obj['temperature'] = GetOrganizationSensorReadingsHistory200ResponseInnerTemperature.constructFromObject(data['temperature']);
            }
            if (data.hasOwnProperty('ts')) {
                obj['ts'] = ApiClient.convertToType(data['ts'], 'String');
            }
            if (data.hasOwnProperty('tvoc')) {
                obj['tvoc'] = GetOrganizationSensorReadingsHistory200ResponseInnerTvoc.constructFromObject(data['tvoc']);
            }
            if (data.hasOwnProperty('water')) {
                obj['water'] = GetOrganizationSensorReadingsHistory200ResponseInnerWater.constructFromObject(data['water']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `battery`
        if (data['battery']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerBattery.validateJSON(data['battery']);
        }
        // validate the optional field `button`
        if (data['button']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerButton.validateJSON(data['button']);
        }
        // validate the optional field `door`
        if (data['door']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerDoor.validateJSON(data['door']);
        }
        // validate the optional field `humidity`
        if (data['humidity']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerHumidity.validateJSON(data['humidity']);
        }
        // validate the optional field `indoorAirQuality`
        if (data['indoorAirQuality']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality.validateJSON(data['indoorAirQuality']);
        }
        // ensure the json data is a string
        if (data['metric'] && !(typeof data['metric'] === 'string' || data['metric'] instanceof String)) {
            throw new Error("Expected the field `metric` to be a primitive type in the JSON string but got " + data['metric']);
        }
        // validate the optional field `noise`
        if (data['noise']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerNoise.validateJSON(data['noise']);
        }
        // validate the optional field `pm25`
        if (data['pm25']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerPm25.validateJSON(data['pm25']);
        }
        // validate the optional field `temperature`
        if (data['temperature']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerTemperature.validateJSON(data['temperature']);
        }
        // ensure the json data is a string
        if (data['ts'] && !(typeof data['ts'] === 'string' || data['ts'] instanceof String)) {
            throw new Error("Expected the field `ts` to be a primitive type in the JSON string but got " + data['ts']);
        }
        // validate the optional field `tvoc`
        if (data['tvoc']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerTvoc.validateJSON(data['tvoc']);
        }
        // validate the optional field `water`
        if (data['water']) { // data not null
          GetOrganizationSensorReadingsHistory200ResponseInnerWater.validateJSON(data['water']);
        }

        return true;
    }


}



/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerBattery} battery
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['battery'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerButton} button
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['button'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerDoor} door
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['door'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerHumidity} humidity
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['humidity'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality} indoorAirQuality
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['indoorAirQuality'] = undefined;

/**
 * Type of sensor reading.
 * @member {module:model/GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.MetricEnum} metric
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['metric'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerNoise} noise
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['noise'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerPm25} pm25
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['pm25'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerTemperature} temperature
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['temperature'] = undefined;

/**
 * Time at which the reading occurred, in ISO8601 format.
 * @member {String} ts
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['ts'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerTvoc} tvoc
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['tvoc'] = undefined;

/**
 * @member {module:model/GetOrganizationSensorReadingsHistory200ResponseInnerWater} water
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.prototype['water'] = undefined;





/**
 * Allowed values for the <code>metric</code> property.
 * @enum {String}
 * @readonly
 */
GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner['MetricEnum'] = {

    /**
     * value: "battery"
     * @const
     */
    "battery": "battery",

    /**
     * value: "button"
     * @const
     */
    "button": "button",

    /**
     * value: "door"
     * @const
     */
    "door": "door",

    /**
     * value: "humidity"
     * @const
     */
    "humidity": "humidity",

    /**
     * value: "indoorAirQuality"
     * @const
     */
    "indoorAirQuality": "indoorAirQuality",

    /**
     * value: "noise"
     * @const
     */
    "noise": "noise",

    /**
     * value: "pm25"
     * @const
     */
    "pm25": "pm25",

    /**
     * value: "temperature"
     * @const
     */
    "temperature": "temperature",

    /**
     * value: "tvoc"
     * @const
     */
    "tvoc": "tvoc",

    /**
     * value: "water"
     * @const
     */
    "water": "water"
};



export default GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner;

