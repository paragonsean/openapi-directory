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
 * The ShareProfileAcknowledgement model module.
 * @module model/ShareProfileAcknowledgement
 * @version 0.5
 */
class ShareProfileAcknowledgement {
    /**
     * Constructs a new <code>ShareProfileAcknowledgement</code>.
     * @alias module:model/ShareProfileAcknowledgement
     * @param healthId {String} 
     * @param status {module:model/ShareProfileAcknowledgement.StatusEnum} 
     */
    constructor(healthId, status) { 
        
        ShareProfileAcknowledgement.initialize(this, healthId, status);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, healthId, status) { 
        obj['healthId'] = healthId;
        obj['status'] = status;
    }

    /**
     * Constructs a <code>ShareProfileAcknowledgement</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ShareProfileAcknowledgement} obj Optional instance to populate.
     * @return {module:model/ShareProfileAcknowledgement} The populated <code>ShareProfileAcknowledgement</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ShareProfileAcknowledgement();

            if (data.hasOwnProperty('healthId')) {
                obj['healthId'] = ApiClient.convertToType(data['healthId'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ShareProfileAcknowledgement</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ShareProfileAcknowledgement</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ShareProfileAcknowledgement.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['healthId'] && !(typeof data['healthId'] === 'string' || data['healthId'] instanceof String)) {
            throw new Error("Expected the field `healthId` to be a primitive type in the JSON string but got " + data['healthId']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

ShareProfileAcknowledgement.RequiredProperties = ["healthId", "status"];

/**
 * @member {String} healthId
 */
ShareProfileAcknowledgement.prototype['healthId'] = undefined;

/**
 * @member {module:model/ShareProfileAcknowledgement.StatusEnum} status
 */
ShareProfileAcknowledgement.prototype['status'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
ShareProfileAcknowledgement['StatusEnum'] = {

    /**
     * value: "SUCCESS"
     * @const
     */
    "SUCCESS": "SUCCESS",

    /**
     * value: "FAILURE"
     * @const
     */
    "FAILURE": "FAILURE"
};



export default ShareProfileAcknowledgement;

