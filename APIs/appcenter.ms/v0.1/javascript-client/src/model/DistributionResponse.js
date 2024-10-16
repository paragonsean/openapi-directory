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
 * The DistributionResponse model module.
 * @module model/DistributionResponse
 * @version v0.1
 */
class DistributionResponse {
    /**
     * Constructs a new <code>DistributionResponse</code>.
     * @alias module:model/DistributionResponse
     */
    constructor() { 
        
        DistributionResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DistributionResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DistributionResponse} obj Optional instance to populate.
     * @return {module:model/DistributionResponse} The populated <code>DistributionResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DistributionResponse();

            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('upload_id')) {
                obj['upload_id'] = ApiClient.convertToType(data['upload_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DistributionResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DistributionResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['upload_id'] && !(typeof data['upload_id'] === 'string' || data['upload_id'] instanceof String)) {
            throw new Error("Expected the field `upload_id` to be a primitive type in the JSON string but got " + data['upload_id']);
        }

        return true;
    }


}



/**
 * Status of the Request
 * @member {String} status
 */
DistributionResponse.prototype['status'] = undefined;

/**
 * A unique ID of the upload
 * @member {String} upload_id
 */
DistributionResponse.prototype['upload_id'] = undefined;






export default DistributionResponse;

