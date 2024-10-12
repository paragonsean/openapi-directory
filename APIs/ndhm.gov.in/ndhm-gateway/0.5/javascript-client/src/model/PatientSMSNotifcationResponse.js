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
import Error from './Error';
import RequestReference from './RequestReference';

/**
 * The PatientSMSNotifcationResponse model module.
 * @module model/PatientSMSNotifcationResponse
 * @version 0.5
 */
class PatientSMSNotifcationResponse {
    /**
     * Constructs a new <code>PatientSMSNotifcationResponse</code>.
     * @alias module:model/PatientSMSNotifcationResponse
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param resp {module:model/RequestReference} 
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     */
    constructor(requestId, resp, timestamp) { 
        
        PatientSMSNotifcationResponse.initialize(this, requestId, resp, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, requestId, resp, timestamp) { 
        obj['requestId'] = requestId;
        obj['resp'] = resp;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>PatientSMSNotifcationResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientSMSNotifcationResponse} obj Optional instance to populate.
     * @return {module:model/PatientSMSNotifcationResponse} The populated <code>PatientSMSNotifcationResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientSMSNotifcationResponse();

            if (data.hasOwnProperty('error')) {
                obj['error'] = Error.constructFromObject(data['error']);
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('resp')) {
                obj['resp'] = RequestReference.constructFromObject(data['resp']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientSMSNotifcationResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientSMSNotifcationResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientSMSNotifcationResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `error`
        if (data['error']) { // data not null
          Error.validateJSON(data['error']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }
        // validate the optional field `resp`
        if (data['resp']) { // data not null
          RequestReference.validateJSON(data['resp']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

PatientSMSNotifcationResponse.RequiredProperties = ["requestId", "resp", "timestamp"];

/**
 * @member {module:model/Error} error
 */
PatientSMSNotifcationResponse.prototype['error'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
PatientSMSNotifcationResponse.prototype['requestId'] = undefined;

/**
 * @member {module:model/RequestReference} resp
 */
PatientSMSNotifcationResponse.prototype['resp'] = undefined;

/**
 * @member {module:model/PatientSMSNotifcationResponse.StatusEnum} status
 */
PatientSMSNotifcationResponse.prototype['status'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
PatientSMSNotifcationResponse.prototype['timestamp'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
PatientSMSNotifcationResponse['StatusEnum'] = {

    /**
     * value: "ACKNOWLEDGED"
     * @const
     */
    "ACKNOWLEDGED": "ACKNOWLEDGED",

    /**
     * value: "ERRORED"
     * @const
     */
    "ERRORED": "ERRORED"
};



export default PatientSMSNotifcationResponse;

