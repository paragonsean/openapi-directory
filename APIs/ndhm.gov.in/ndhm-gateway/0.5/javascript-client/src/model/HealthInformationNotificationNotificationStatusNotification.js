/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner from './HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner';

/**
 * The HealthInformationNotificationNotificationStatusNotification model module.
 * @module model/HealthInformationNotificationNotificationStatusNotification
 * @version 0.5
 */
class HealthInformationNotificationNotificationStatusNotification {
    /**
     * Constructs a new <code>HealthInformationNotificationNotificationStatusNotification</code>.
     * @alias module:model/HealthInformationNotificationNotificationStatusNotification
     * @param hipId {String} 
     * @param sessionStatus {module:model/HealthInformationNotificationNotificationStatusNotification.SessionStatusEnum} 
     */
    constructor(hipId, sessionStatus) { 
        
        HealthInformationNotificationNotificationStatusNotification.initialize(this, hipId, sessionStatus);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, hipId, sessionStatus) { 
        obj['hipId'] = hipId;
        obj['sessionStatus'] = sessionStatus;
    }

    /**
     * Constructs a <code>HealthInformationNotificationNotificationStatusNotification</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HealthInformationNotificationNotificationStatusNotification} obj Optional instance to populate.
     * @return {module:model/HealthInformationNotificationNotificationStatusNotification} The populated <code>HealthInformationNotificationNotificationStatusNotification</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HealthInformationNotificationNotificationStatusNotification();

            if (data.hasOwnProperty('hipId')) {
                obj['hipId'] = ApiClient.convertToType(data['hipId'], 'String');
            }
            if (data.hasOwnProperty('sessionStatus')) {
                obj['sessionStatus'] = ApiClient.convertToType(data['sessionStatus'], 'String');
            }
            if (data.hasOwnProperty('statusResponses')) {
                obj['statusResponses'] = ApiClient.convertToType(data['statusResponses'], [HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HealthInformationNotificationNotificationStatusNotification</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HealthInformationNotificationNotificationStatusNotification</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HealthInformationNotificationNotificationStatusNotification.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['hipId'] && !(typeof data['hipId'] === 'string' || data['hipId'] instanceof String)) {
            throw new Error("Expected the field `hipId` to be a primitive type in the JSON string but got " + data['hipId']);
        }
        // ensure the json data is a string
        if (data['sessionStatus'] && !(typeof data['sessionStatus'] === 'string' || data['sessionStatus'] instanceof String)) {
            throw new Error("Expected the field `sessionStatus` to be a primitive type in the JSON string but got " + data['sessionStatus']);
        }
        if (data['statusResponses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['statusResponses'])) {
                throw new Error("Expected the field `statusResponses` to be an array in the JSON data but got " + data['statusResponses']);
            }
            // validate the optional field `statusResponses` (array)
            for (const item of data['statusResponses']) {
                HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.validateJSON(item);
            };
        }

        return true;
    }


}

HealthInformationNotificationNotificationStatusNotification.RequiredProperties = ["hipId", "sessionStatus"];

/**
 * @member {String} hipId
 */
HealthInformationNotificationNotificationStatusNotification.prototype['hipId'] = undefined;

/**
 * @member {module:model/HealthInformationNotificationNotificationStatusNotification.SessionStatusEnum} sessionStatus
 */
HealthInformationNotificationNotificationStatusNotification.prototype['sessionStatus'] = undefined;

/**
 * @member {Array.<module:model/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner>} statusResponses
 */
HealthInformationNotificationNotificationStatusNotification.prototype['statusResponses'] = undefined;





/**
 * Allowed values for the <code>sessionStatus</code> property.
 * @enum {String}
 * @readonly
 */
HealthInformationNotificationNotificationStatusNotification['SessionStatusEnum'] = {

    /**
     * value: "TRANSFERRED"
     * @const
     */
    "TRANSFERRED": "TRANSFERRED",

    /**
     * value: "FAILED"
     * @const
     */
    "FAILED": "FAILED"
};



export default HealthInformationNotificationNotificationStatusNotification;

