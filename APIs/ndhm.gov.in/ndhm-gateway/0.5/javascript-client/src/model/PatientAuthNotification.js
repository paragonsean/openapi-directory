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
import PatientAuthNotificationAuth from './PatientAuthNotificationAuth';

/**
 * The PatientAuthNotification model module.
 * @module model/PatientAuthNotification
 * @version 0.5
 */
class PatientAuthNotification {
    /**
     * Constructs a new <code>PatientAuthNotification</code>.
     * @alias module:model/PatientAuthNotification
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     */
    constructor(requestId, timestamp) { 
        
        PatientAuthNotification.initialize(this, requestId, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, requestId, timestamp) { 
        obj['requestId'] = requestId;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>PatientAuthNotification</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientAuthNotification} obj Optional instance to populate.
     * @return {module:model/PatientAuthNotification} The populated <code>PatientAuthNotification</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientAuthNotification();

            if (data.hasOwnProperty('auth')) {
                obj['auth'] = PatientAuthNotificationAuth.constructFromObject(data['auth']);
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientAuthNotification</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientAuthNotification</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientAuthNotification.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `auth`
        if (data['auth']) { // data not null
          PatientAuthNotificationAuth.validateJSON(data['auth']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }

        return true;
    }


}

PatientAuthNotification.RequiredProperties = ["requestId", "timestamp"];

/**
 * @member {module:model/PatientAuthNotificationAuth} auth
 */
PatientAuthNotification.prototype['auth'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
PatientAuthNotification.prototype['requestId'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
PatientAuthNotification.prototype['timestamp'] = undefined;






export default PatientAuthNotification;

