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
 * The ApiTokenClaim model module.
 * @module model/ApiTokenClaim
 * @version v0.1
 */
class ApiTokenClaim {
    /**
     * Constructs a new <code>ApiTokenClaim</code>.
     * @alias module:model/ApiTokenClaim
     */
    constructor() { 
        
        ApiTokenClaim.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiTokenClaim</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiTokenClaim} obj Optional instance to populate.
     * @return {module:model/ApiTokenClaim} The populated <code>ApiTokenClaim</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiTokenClaim();

            if (data.hasOwnProperty('claim_type')) {
                obj['claim_type'] = ApiClient.convertToType(data['claim_type'], 'String');
            }
            if (data.hasOwnProperty('claim_value')) {
                obj['claim_value'] = ApiClient.convertToType(data['claim_value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiTokenClaim</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiTokenClaim</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['claim_type'] && !(typeof data['claim_type'] === 'string' || data['claim_type'] instanceof String)) {
            throw new Error("Expected the field `claim_type` to be a primitive type in the JSON string but got " + data['claim_type']);
        }
        // ensure the json data is a string
        if (data['claim_value'] && !(typeof data['claim_value'] === 'string' || data['claim_value'] instanceof String)) {
            throw new Error("Expected the field `claim_value` to be a primitive type in the JSON string but got " + data['claim_value']);
        }

        return true;
    }


}



/**
 * @member {module:model/ApiTokenClaim.ClaimTypeEnum} claim_type
 */
ApiTokenClaim.prototype['claim_type'] = undefined;

/**
 * @member {String} claim_value
 */
ApiTokenClaim.prototype['claim_value'] = undefined;





/**
 * Allowed values for the <code>claim_type</code> property.
 * @enum {String}
 * @readonly
 */
ApiTokenClaim['ClaimTypeEnum'] = {

    /**
     * value: "user_email"
     * @const
     */
    "user_email": "user_email",

    /**
     * value: "user_origin"
     * @const
     */
    "user_origin": "user_origin",

    /**
     * value: "app_owner_name"
     * @const
     */
    "app_owner_name": "app_owner_name",

    /**
     * value: "app_name"
     * @const
     */
    "app_name": "app_name",

    /**
     * value: "app_origin"
     * @const
     */
    "app_origin": "app_origin",

    /**
     * value: "app_os"
     * @const
     */
    "app_os": "app_os",

    /**
     * value: "app_platform"
     * @const
     */
    "app_platform": "app_platform",

    /**
     * value: "app_secret"
     * @const
     */
    "app_secret": "app_secret"
};



export default ApiTokenClaim;

