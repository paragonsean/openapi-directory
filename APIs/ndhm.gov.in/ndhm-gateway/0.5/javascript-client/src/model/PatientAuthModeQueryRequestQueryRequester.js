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

/**
 * The PatientAuthModeQueryRequestQueryRequester model module.
 * @module model/PatientAuthModeQueryRequestQueryRequester
 * @version 0.5
 */
class PatientAuthModeQueryRequestQueryRequester {
    /**
     * Constructs a new <code>PatientAuthModeQueryRequestQueryRequester</code>.
     * @alias module:model/PatientAuthModeQueryRequestQueryRequester
     * @param id {String} 
     * @param type {module:model/PatientAuthModeQueryRequestQueryRequester.TypeEnum} 
     */
    constructor(id, type) { 
        
        PatientAuthModeQueryRequestQueryRequester.initialize(this, id, type);
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
     * Constructs a <code>PatientAuthModeQueryRequestQueryRequester</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientAuthModeQueryRequestQueryRequester} obj Optional instance to populate.
     * @return {module:model/PatientAuthModeQueryRequestQueryRequester} The populated <code>PatientAuthModeQueryRequestQueryRequester</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientAuthModeQueryRequestQueryRequester();

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
     * Validates the JSON data with respect to <code>PatientAuthModeQueryRequestQueryRequester</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientAuthModeQueryRequestQueryRequester</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientAuthModeQueryRequestQueryRequester.RequiredProperties) {
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

PatientAuthModeQueryRequestQueryRequester.RequiredProperties = ["id", "type"];

/**
 * @member {String} id
 */
PatientAuthModeQueryRequestQueryRequester.prototype['id'] = undefined;

/**
 * @member {module:model/PatientAuthModeQueryRequestQueryRequester.TypeEnum} type
 */
PatientAuthModeQueryRequestQueryRequester.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
PatientAuthModeQueryRequestQueryRequester['TypeEnum'] = {

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



export default PatientAuthModeQueryRequestQueryRequester;

