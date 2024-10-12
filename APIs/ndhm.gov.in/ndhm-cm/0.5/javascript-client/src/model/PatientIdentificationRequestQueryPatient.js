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
 * The PatientIdentificationRequestQueryPatient model module.
 * @module model/PatientIdentificationRequestQueryPatient
 * @version 0.5
 */
class PatientIdentificationRequestQueryPatient {
    /**
     * Constructs a new <code>PatientIdentificationRequestQueryPatient</code>.
     * @alias module:model/PatientIdentificationRequestQueryPatient
     * @param id {String} 
     */
    constructor(id) { 
        
        PatientIdentificationRequestQueryPatient.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>PatientIdentificationRequestQueryPatient</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientIdentificationRequestQueryPatient} obj Optional instance to populate.
     * @return {module:model/PatientIdentificationRequestQueryPatient} The populated <code>PatientIdentificationRequestQueryPatient</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientIdentificationRequestQueryPatient();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientIdentificationRequestQueryPatient</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientIdentificationRequestQueryPatient</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientIdentificationRequestQueryPatient.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}

PatientIdentificationRequestQueryPatient.RequiredProperties = ["id"];

/**
 * @member {String} id
 */
PatientIdentificationRequestQueryPatient.prototype['id'] = undefined;






export default PatientIdentificationRequestQueryPatient;

