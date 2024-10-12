/**
 * Currencytick API Documentation
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Healthcheck400Response model module.
 * @module model/Healthcheck400Response
 * @version 1.0.0
 */
class Healthcheck400Response {
    /**
     * Constructs a new <code>Healthcheck400Response</code>.
     * @alias module:model/Healthcheck400Response
     */
    constructor() { 
        
        Healthcheck400Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Healthcheck400Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Healthcheck400Response} obj Optional instance to populate.
     * @return {module:model/Healthcheck400Response} The populated <code>Healthcheck400Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Healthcheck400Response();

            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Healthcheck400Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Healthcheck400Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * The status of this API (`up` or `down`).
 * @member {String} status
 */
Healthcheck400Response.prototype['status'] = undefined;






export default Healthcheck400Response;

