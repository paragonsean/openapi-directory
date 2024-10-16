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

/**
 * The GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity model module.
 * @module model/GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity
 * @version 1.32.0
 */
class GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity {
    /**
     * Constructs a new <code>GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity</code>.
     * Humidity threshold. One of &#39;relativePercentage&#39; or &#39;quality&#39; must be provided.
     * @alias module:model/GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity
     */
    constructor() { 
        
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity} obj Optional instance to populate.
     * @return {module:model/GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity} The populated <code>GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity();

            if (data.hasOwnProperty('quality')) {
                obj['quality'] = ApiClient.convertToType(data['quality'], 'String');
            }
            if (data.hasOwnProperty('relativePercentage')) {
                obj['relativePercentage'] = ApiClient.convertToType(data['relativePercentage'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['quality'] && !(typeof data['quality'] === 'string' || data['quality'] instanceof String)) {
            throw new Error("Expected the field `quality` to be a primitive type in the JSON string but got " + data['quality']);
        }

        return true;
    }


}



/**
 * Alerting threshold as a qualitative humidity level.
 * @member {module:model/GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity.QualityEnum} quality
 */
GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity.prototype['quality'] = undefined;

/**
 * Alerting threshold in %RH.
 * @member {Number} relativePercentage
 */
GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity.prototype['relativePercentage'] = undefined;





/**
 * Allowed values for the <code>quality</code> property.
 * @enum {String}
 * @readonly
 */
GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity['QualityEnum'] = {

    /**
     * value: "fair"
     * @const
     */
    "fair": "fair",

    /**
     * value: "good"
     * @const
     */
    "good": "good",

    /**
     * value: "inadequate"
     * @const
     */
    "inadequate": "inadequate",

    /**
     * value: "poor"
     * @const
     */
    "poor": "poor"
};



export default GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity;

