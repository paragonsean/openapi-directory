/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The EaadharXamlSchemaKycResUidDataPoi model module.
 * @module model/EaadharXamlSchemaKycResUidDataPoi
 * @version 1.0.0
 */
class EaadharXamlSchemaKycResUidDataPoi {
    /**
     * Constructs a new <code>EaadharXamlSchemaKycResUidDataPoi</code>.
     * @alias module:model/EaadharXamlSchemaKycResUidDataPoi
     * @param dob {String} 
     * @param gender {String} 
     * @param name {String} 
     */
    constructor(dob, gender, name) { 
        
        EaadharXamlSchemaKycResUidDataPoi.initialize(this, dob, gender, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, dob, gender, name) { 
        obj['dob'] = dob;
        obj['gender'] = gender;
        obj['name'] = name;
    }

    /**
     * Constructs a <code>EaadharXamlSchemaKycResUidDataPoi</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EaadharXamlSchemaKycResUidDataPoi} obj Optional instance to populate.
     * @return {module:model/EaadharXamlSchemaKycResUidDataPoi} The populated <code>EaadharXamlSchemaKycResUidDataPoi</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EaadharXamlSchemaKycResUidDataPoi();

            if (data.hasOwnProperty('dob')) {
                obj['dob'] = ApiClient.convertToType(data['dob'], 'String');
            }
            if (data.hasOwnProperty('gender')) {
                obj['gender'] = ApiClient.convertToType(data['gender'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EaadharXamlSchemaKycResUidDataPoi</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EaadharXamlSchemaKycResUidDataPoi</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EaadharXamlSchemaKycResUidDataPoi.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['dob'] && !(typeof data['dob'] === 'string' || data['dob'] instanceof String)) {
            throw new Error("Expected the field `dob` to be a primitive type in the JSON string but got " + data['dob']);
        }
        // ensure the json data is a string
        if (data['gender'] && !(typeof data['gender'] === 'string' || data['gender'] instanceof String)) {
            throw new Error("Expected the field `gender` to be a primitive type in the JSON string but got " + data['gender']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

EaadharXamlSchemaKycResUidDataPoi.RequiredProperties = ["dob", "gender", "name"];

/**
 * @member {String} dob
 */
EaadharXamlSchemaKycResUidDataPoi.prototype['dob'] = undefined;

/**
 * @member {String} gender
 */
EaadharXamlSchemaKycResUidDataPoi.prototype['gender'] = undefined;

/**
 * @member {String} name
 */
EaadharXamlSchemaKycResUidDataPoi.prototype['name'] = undefined;






export default EaadharXamlSchemaKycResUidDataPoi;

