/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
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
 * The PatientAuthRequester model module.
 * @module model/PatientAuthRequester
 * @version 0.5
 */
class PatientAuthRequester {
    /**
     * Constructs a new <code>PatientAuthRequester</code>.
     * identification of requester
     * @alias module:model/PatientAuthRequester
     * @param id {String} 
     * @param type {module:model/PatientAuthRequester.TypeEnum} 
     */
    constructor(id, type) { 
        
        PatientAuthRequester.initialize(this, id, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, type) { 
        obj['id'] = id;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>PatientAuthRequester</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientAuthRequester} obj Optional instance to populate.
     * @return {module:model/PatientAuthRequester} The populated <code>PatientAuthRequester</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientAuthRequester();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientAuthRequester</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientAuthRequester</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientAuthRequester.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

PatientAuthRequester.RequiredProperties = ["id", "type"];

/**
 * @member {String} id
 */
PatientAuthRequester.prototype['id'] = undefined;

/**
 * @member {module:model/PatientAuthRequester.TypeEnum} type
 */
PatientAuthRequester.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
PatientAuthRequester['TypeEnum'] = {

    /**
     * value: "HIP"
     * @const
     */
    "HIP": "HIP",

    /**
     * value: "HIU"
     * @const
     */
    "HIU": "HIU"
};



export default PatientAuthRequester;

