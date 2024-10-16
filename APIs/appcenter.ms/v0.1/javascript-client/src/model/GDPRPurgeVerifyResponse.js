/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GDPRPurgeVerifyResponse model module.
 * @module model/GDPRPurgeVerifyResponse
 * @version v0.1
 */
class GDPRPurgeVerifyResponse {
    /**
     * Constructs a new <code>GDPRPurgeVerifyResponse</code>.
     * @alias module:model/GDPRPurgeVerifyResponse
     * @param success {Boolean} indicate whether GDPR purge operation succeeds or not
     */
    constructor(success) { 
        
        GDPRPurgeVerifyResponse.initialize(this, success);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, success) { 
        obj['success'] = success;
    }

    /**
     * Constructs a <code>GDPRPurgeVerifyResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GDPRPurgeVerifyResponse} obj Optional instance to populate.
     * @return {module:model/GDPRPurgeVerifyResponse} The populated <code>GDPRPurgeVerifyResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GDPRPurgeVerifyResponse();

            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GDPRPurgeVerifyResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GDPRPurgeVerifyResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GDPRPurgeVerifyResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

GDPRPurgeVerifyResponse.RequiredProperties = ["success"];

/**
 * indicate whether GDPR purge operation succeeds or not
 * @member {Boolean} success
 */
GDPRPurgeVerifyResponse.prototype['success'] = undefined;






export default GDPRPurgeVerifyResponse;

