/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
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
import Identifier from './Identifier';
import PatientAddress from './PatientAddress';
import PatientGender from './PatientGender';

/**
 * The PatientDemographicResponse model module.
 * @module model/PatientDemographicResponse
 * @version 0.5
 */
class PatientDemographicResponse {
    /**
     * Constructs a new <code>PatientDemographicResponse</code>.
     * @alias module:model/PatientDemographicResponse
     * @param gender {module:model/PatientGender} 
     * @param id {String} PHR Identifier of patient at consent manager
     * @param name {String} 
     * @param yearOfBirth {Number} 
     */
    constructor(gender, id, name, yearOfBirth) { 
        
        PatientDemographicResponse.initialize(this, gender, id, name, yearOfBirth);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, gender, id, name, yearOfBirth) { 
        obj['gender'] = gender;
        obj['id'] = id;
        obj['name'] = name;
        obj['yearOfBirth'] = yearOfBirth;
    }

    /**
     * Constructs a <code>PatientDemographicResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientDemographicResponse} obj Optional instance to populate.
     * @return {module:model/PatientDemographicResponse} The populated <code>PatientDemographicResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientDemographicResponse();

            if (data.hasOwnProperty('address')) {
                obj['address'] = PatientAddress.constructFromObject(data['address']);
            }
            if (data.hasOwnProperty('gender')) {
                obj['gender'] = PatientGender.constructFromObject(data['gender']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('identifiers')) {
                obj['identifiers'] = ApiClient.convertToType(data['identifiers'], [Identifier]);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('yearOfBirth')) {
                obj['yearOfBirth'] = ApiClient.convertToType(data['yearOfBirth'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientDemographicResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientDemographicResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientDemographicResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `address`
        if (data['address']) { // data not null
          PatientAddress.validateJSON(data['address']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        if (data['identifiers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['identifiers'])) {
                throw new Error("Expected the field `identifiers` to be an array in the JSON data but got " + data['identifiers']);
            }
            // validate the optional field `identifiers` (array)
            for (const item of data['identifiers']) {
                Identifier.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

PatientDemographicResponse.RequiredProperties = ["gender", "id", "name", "yearOfBirth"];

/**
 * @member {module:model/PatientAddress} address
 */
PatientDemographicResponse.prototype['address'] = undefined;

/**
 * @member {module:model/PatientGender} gender
 */
PatientDemographicResponse.prototype['gender'] = undefined;

/**
 * PHR Identifier of patient at consent manager
 * @member {String} id
 */
PatientDemographicResponse.prototype['id'] = undefined;

/**
 * @member {Array.<module:model/Identifier>} identifiers
 */
PatientDemographicResponse.prototype['identifiers'] = undefined;

/**
 * @member {String} name
 */
PatientDemographicResponse.prototype['name'] = undefined;

/**
 * @member {Number} yearOfBirth
 */
PatientDemographicResponse.prototype['yearOfBirth'] = undefined;






export default PatientDemographicResponse;

