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
import GetNetworkAlertsHistory200ResponseInnerDestinations from './GetNetworkAlertsHistory200ResponseInnerDestinations';
import GetNetworkAlertsHistory200ResponseInnerDevice from './GetNetworkAlertsHistory200ResponseInnerDevice';

/**
 * The GetNetworkAlertsHistory200ResponseInner model module.
 * @module model/GetNetworkAlertsHistory200ResponseInner
 * @version 1.32.0
 */
class GetNetworkAlertsHistory200ResponseInner {
    /**
     * Constructs a new <code>GetNetworkAlertsHistory200ResponseInner</code>.
     * @alias module:model/GetNetworkAlertsHistory200ResponseInner
     */
    constructor() { 
        
        GetNetworkAlertsHistory200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkAlertsHistory200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkAlertsHistory200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkAlertsHistory200ResponseInner} The populated <code>GetNetworkAlertsHistory200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkAlertsHistory200ResponseInner();

            if (data.hasOwnProperty('alertData')) {
                obj['alertData'] = ApiClient.convertToType(data['alertData'], Object);
            }
            if (data.hasOwnProperty('alertType')) {
                obj['alertType'] = ApiClient.convertToType(data['alertType'], 'String');
            }
            if (data.hasOwnProperty('alertTypeId')) {
                obj['alertTypeId'] = ApiClient.convertToType(data['alertTypeId'], 'String');
            }
            if (data.hasOwnProperty('destinations')) {
                obj['destinations'] = GetNetworkAlertsHistory200ResponseInnerDestinations.constructFromObject(data['destinations']);
            }
            if (data.hasOwnProperty('device')) {
                obj['device'] = GetNetworkAlertsHistory200ResponseInnerDevice.constructFromObject(data['device']);
            }
            if (data.hasOwnProperty('occurredAt')) {
                obj['occurredAt'] = ApiClient.convertToType(data['occurredAt'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkAlertsHistory200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkAlertsHistory200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['alertType'] && !(typeof data['alertType'] === 'string' || data['alertType'] instanceof String)) {
            throw new Error("Expected the field `alertType` to be a primitive type in the JSON string but got " + data['alertType']);
        }
        // ensure the json data is a string
        if (data['alertTypeId'] && !(typeof data['alertTypeId'] === 'string' || data['alertTypeId'] instanceof String)) {
            throw new Error("Expected the field `alertTypeId` to be a primitive type in the JSON string but got " + data['alertTypeId']);
        }
        // validate the optional field `destinations`
        if (data['destinations']) { // data not null
          GetNetworkAlertsHistory200ResponseInnerDestinations.validateJSON(data['destinations']);
        }
        // validate the optional field `device`
        if (data['device']) { // data not null
          GetNetworkAlertsHistory200ResponseInnerDevice.validateJSON(data['device']);
        }
        // ensure the json data is a string
        if (data['occurredAt'] && !(typeof data['occurredAt'] === 'string' || data['occurredAt'] instanceof String)) {
            throw new Error("Expected the field `occurredAt` to be a primitive type in the JSON string but got " + data['occurredAt']);
        }

        return true;
    }


}



/**
 * relevant data about the event that caused the alert
 * @member {Object} alertData
 */
GetNetworkAlertsHistory200ResponseInner.prototype['alertData'] = undefined;

/**
 * user friendly alert type
 * @member {String} alertType
 */
GetNetworkAlertsHistory200ResponseInner.prototype['alertType'] = undefined;

/**
 * type of alert
 * @member {String} alertTypeId
 */
GetNetworkAlertsHistory200ResponseInner.prototype['alertTypeId'] = undefined;

/**
 * @member {module:model/GetNetworkAlertsHistory200ResponseInnerDestinations} destinations
 */
GetNetworkAlertsHistory200ResponseInner.prototype['destinations'] = undefined;

/**
 * @member {module:model/GetNetworkAlertsHistory200ResponseInnerDevice} device
 */
GetNetworkAlertsHistory200ResponseInner.prototype['device'] = undefined;

/**
 * time when the event occurred
 * @member {String} occurredAt
 */
GetNetworkAlertsHistory200ResponseInner.prototype['occurredAt'] = undefined;






export default GetNetworkAlertsHistory200ResponseInner;

