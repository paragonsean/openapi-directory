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
 * The ApiTokensPostRequest model module.
 * @module model/ApiTokensPostRequest
 * @version v0.1
 */
class ApiTokensPostRequest {
    /**
     * Constructs a new <code>ApiTokensPostRequest</code>.
     * @alias module:model/ApiTokensPostRequest
     */
    constructor() { 
        
        ApiTokensPostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiTokensPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiTokensPostRequest} obj Optional instance to populate.
     * @return {module:model/ApiTokensPostRequest} The populated <code>ApiTokensPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiTokensPostRequest();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('encrypted_token')) {
                obj['encrypted_token'] = ApiClient.convertToType(data['encrypted_token'], 'String');
            }
            if (data.hasOwnProperty('scope')) {
                obj['scope'] = ApiClient.convertToType(data['scope'], ['String']);
            }
            if (data.hasOwnProperty('token_hash')) {
                obj['token_hash'] = ApiClient.convertToType(data['token_hash'], 'String');
            }
            if (data.hasOwnProperty('token_type')) {
                obj['token_type'] = ApiClient.convertToType(data['token_type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiTokensPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiTokensPostRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['encrypted_token'] && !(typeof data['encrypted_token'] === 'string' || data['encrypted_token'] instanceof String)) {
            throw new Error("Expected the field `encrypted_token` to be a primitive type in the JSON string but got " + data['encrypted_token']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['scope'])) {
            throw new Error("Expected the field `scope` to be an array in the JSON data but got " + data['scope']);
        }
        // ensure the json data is a string
        if (data['token_hash'] && !(typeof data['token_hash'] === 'string' || data['token_hash'] instanceof String)) {
            throw new Error("Expected the field `token_hash` to be a primitive type in the JSON string but got " + data['token_hash']);
        }
        // ensure the json data is a string
        if (data['token_type'] && !(typeof data['token_type'] === 'string' || data['token_type'] instanceof String)) {
            throw new Error("Expected the field `token_type` to be a primitive type in the JSON string but got " + data['token_type']);
        }

        return true;
    }


}



/**
 * The description of the token
 * @member {String} description
 */
ApiTokensPostRequest.prototype['description'] = undefined;

/**
 * An encrypted value of the token.
 * @member {String} encrypted_token
 */
ApiTokensPostRequest.prototype['encrypted_token'] = undefined;

/**
 * The scope for this token. An array of supported roles.
 * @member {Array.<module:model/ApiTokensPostRequest.ScopeEnum>} scope
 */
ApiTokensPostRequest.prototype['scope'] = undefined;

/**
 * The hashed value of api token
 * @member {String} token_hash
 */
ApiTokensPostRequest.prototype['token_hash'] = undefined;

/**
 * The token's type. public:managed by the user; in_app_update:special token for in-app update scenario; buid:dedicated for CI usage for now; session:for CLI session management; tester_app: used for tester mobile app; default is \"public\".'
 * @member {module:model/ApiTokensPostRequest.TokenTypeEnum} token_type
 */
ApiTokensPostRequest.prototype['token_type'] = undefined;





/**
 * Allowed values for the <code>scope</code> property.
 * @enum {String}
 * @readonly
 */
ApiTokensPostRequest['ScopeEnum'] = {

    /**
     * value: "all"
     * @const
     */
    "all": "all",

    /**
     * value: "in_app_update"
     * @const
     */
    "in_app_update": "in_app_update",

    /**
     * value: "viewer"
     * @const
     */
    "viewer": "viewer"
};


/**
 * Allowed values for the <code>token_type</code> property.
 * @enum {String}
 * @readonly
 */
ApiTokensPostRequest['TokenTypeEnum'] = {

    /**
     * value: "public"
     * @const
     */
    "public": "public",

    /**
     * value: "in_app_update"
     * @const
     */
    "in_app_update": "in_app_update",

    /**
     * value: "build"
     * @const
     */
    "build": "build",

    /**
     * value: "session"
     * @const
     */
    "session": "session",

    /**
     * value: "tester_app"
     * @const
     */
    "tester_app": "tester_app"
};



export default ApiTokensPostRequest;

