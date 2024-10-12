/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
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

/**
 * The HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner model module.
 * @module model/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner
 * @version 0.5
 */
class HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner {
    /**
     * Constructs a new <code>HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner</code>.
     * @alias module:model/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner
     * @param careContextReference {String} 
     * @param hiStatus {module:model/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.HiStatusEnum} 
     */
    constructor(careContextReference, hiStatus) { 
        
        HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.initialize(this, careContextReference, hiStatus);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, careContextReference, hiStatus) { 
        obj['careContextReference'] = careContextReference;
        obj['hiStatus'] = hiStatus;
    }

    /**
     * Constructs a <code>HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner} obj Optional instance to populate.
     * @return {module:model/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner} The populated <code>HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner();

            if (data.hasOwnProperty('careContextReference')) {
                obj['careContextReference'] = ApiClient.convertToType(data['careContextReference'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('hiStatus')) {
                obj['hiStatus'] = ApiClient.convertToType(data['hiStatus'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['careContextReference'] && !(typeof data['careContextReference'] === 'string' || data['careContextReference'] instanceof String)) {
            throw new Error("Expected the field `careContextReference` to be a primitive type in the JSON string but got " + data['careContextReference']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['hiStatus'] && !(typeof data['hiStatus'] === 'string' || data['hiStatus'] instanceof String)) {
            throw new Error("Expected the field `hiStatus` to be a primitive type in the JSON string but got " + data['hiStatus']);
        }

        return true;
    }


}

HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.RequiredProperties = ["careContextReference", "hiStatus"];

/**
 * @member {String} careContextReference
 */
HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.prototype['careContextReference'] = undefined;

/**
 * @member {String} description
 */
HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.prototype['description'] = undefined;

/**
 * @member {module:model/HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.HiStatusEnum} hiStatus
 */
HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner.prototype['hiStatus'] = undefined;





/**
 * Allowed values for the <code>hiStatus</code> property.
 * @enum {String}
 * @readonly
 */
HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner['HiStatusEnum'] = {

    /**
     * value: "DELIVERED"
     * @const
     */
    "DELIVERED": "DELIVERED",

    /**
     * value: "OK"
     * @const
     */
    "OK": "OK",

    /**
     * value: "ERRORED"
     * @const
     */
    "ERRORED": "ERRORED"
};



export default HealthInformationNotificationNotificationStatusNotificationStatusResponsesInner;

