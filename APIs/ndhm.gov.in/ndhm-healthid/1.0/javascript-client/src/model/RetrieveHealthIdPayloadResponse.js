/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The RetrieveHealthIdPayloadResponse model module.
 * @module model/RetrieveHealthIdPayloadResponse
 * @version 1.0
 */
class RetrieveHealthIdPayloadResponse {
    /**
     * Constructs a new <code>RetrieveHealthIdPayloadResponse</code>.
     * @alias module:model/RetrieveHealthIdPayloadResponse
     */
    constructor() { 
        
        RetrieveHealthIdPayloadResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RetrieveHealthIdPayloadResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RetrieveHealthIdPayloadResponse} obj Optional instance to populate.
     * @return {module:model/RetrieveHealthIdPayloadResponse} The populated <code>RetrieveHealthIdPayloadResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RetrieveHealthIdPayloadResponse();

            if (data.hasOwnProperty('healthId')) {
                obj['healthId'] = ApiClient.convertToType(data['healthId'], 'String');
            }
            if (data.hasOwnProperty('healthIdNumber')) {
                obj['healthIdNumber'] = ApiClient.convertToType(data['healthIdNumber'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RetrieveHealthIdPayloadResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RetrieveHealthIdPayloadResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['healthId'] && !(typeof data['healthId'] === 'string' || data['healthId'] instanceof String)) {
            throw new Error("Expected the field `healthId` to be a primitive type in the JSON string but got " + data['healthId']);
        }
        // ensure the json data is a string
        if (data['healthIdNumber'] && !(typeof data['healthIdNumber'] === 'string' || data['healthIdNumber'] instanceof String)) {
            throw new Error("Expected the field `healthIdNumber` to be a primitive type in the JSON string but got " + data['healthIdNumber']);
        }

        return true;
    }


}



/**
 * @member {String} healthId
 */
RetrieveHealthIdPayloadResponse.prototype['healthId'] = undefined;

/**
 * @member {String} healthIdNumber
 */
RetrieveHealthIdPayloadResponse.prototype['healthIdNumber'] = undefined;






export default RetrieveHealthIdPayloadResponse;

