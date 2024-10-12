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
import PatientCareContextLinkPatient from './PatientCareContextLinkPatient';

/**
 * The PatientCareContextLink model module.
 * @module model/PatientCareContextLink
 * @version 0.5
 */
class PatientCareContextLink {
    /**
     * Constructs a new <code>PatientCareContextLink</code>.
     * @alias module:model/PatientCareContextLink
     * @param accessToken {String} AccessToken fetched in the user auth process for the purpose specified
     * @param patient {module:model/PatientCareContextLinkPatient} 
     */
    constructor(accessToken, patient) { 
        
        PatientCareContextLink.initialize(this, accessToken, patient);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, accessToken, patient) { 
        obj['accessToken'] = accessToken;
        obj['patient'] = patient;
    }

    /**
     * Constructs a <code>PatientCareContextLink</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientCareContextLink} obj Optional instance to populate.
     * @return {module:model/PatientCareContextLink} The populated <code>PatientCareContextLink</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientCareContextLink();

            if (data.hasOwnProperty('accessToken')) {
                obj['accessToken'] = ApiClient.convertToType(data['accessToken'], 'String');
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = PatientCareContextLinkPatient.constructFromObject(data['patient']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientCareContextLink</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientCareContextLink</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientCareContextLink.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['accessToken'] && !(typeof data['accessToken'] === 'string' || data['accessToken'] instanceof String)) {
            throw new Error("Expected the field `accessToken` to be a primitive type in the JSON string but got " + data['accessToken']);
        }
        // validate the optional field `patient`
        if (data['patient']) { // data not null
          PatientCareContextLinkPatient.validateJSON(data['patient']);
        }

        return true;
    }


}

PatientCareContextLink.RequiredProperties = ["accessToken", "patient"];

/**
 * AccessToken fetched in the user auth process for the purpose specified
 * @member {String} accessToken
 */
PatientCareContextLink.prototype['accessToken'] = undefined;

/**
 * @member {module:model/PatientCareContextLinkPatient} patient
 */
PatientCareContextLink.prototype['patient'] = undefined;






export default PatientCareContextLink;

