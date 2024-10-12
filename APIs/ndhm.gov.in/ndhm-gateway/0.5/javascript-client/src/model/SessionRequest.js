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
 * The SessionRequest model module.
 * @module model/SessionRequest
 * @version 0.5
 */
class SessionRequest {
    /**
     * Constructs a new <code>SessionRequest</code>.
     * @alias module:model/SessionRequest
     * @param clientId {String} 
     * @param clientSecret {String} 
     * @param grantType {module:model/SessionRequest.GrantTypeEnum} 
     */
    constructor(clientId, clientSecret, grantType) { 
        
        SessionRequest.initialize(this, clientId, clientSecret, grantType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, clientId, clientSecret, grantType) { 
        obj['clientId'] = clientId;
        obj['clientSecret'] = clientSecret;
        obj['grantType'] = grantType;
    }

    /**
     * Constructs a <code>SessionRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SessionRequest} obj Optional instance to populate.
     * @return {module:model/SessionRequest} The populated <code>SessionRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SessionRequest();

            if (data.hasOwnProperty('clientId')) {
                obj['clientId'] = ApiClient.convertToType(data['clientId'], 'String');
            }
            if (data.hasOwnProperty('clientSecret')) {
                obj['clientSecret'] = ApiClient.convertToType(data['clientSecret'], 'String');
            }
            if (data.hasOwnProperty('grantType')) {
                obj['grantType'] = ApiClient.convertToType(data['grantType'], 'String');
            }
            if (data.hasOwnProperty('refreshToken')) {
                obj['refreshToken'] = ApiClient.convertToType(data['refreshToken'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SessionRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SessionRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SessionRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['clientId'] && !(typeof data['clientId'] === 'string' || data['clientId'] instanceof String)) {
            throw new Error("Expected the field `clientId` to be a primitive type in the JSON string but got " + data['clientId']);
        }
        // ensure the json data is a string
        if (data['clientSecret'] && !(typeof data['clientSecret'] === 'string' || data['clientSecret'] instanceof String)) {
            throw new Error("Expected the field `clientSecret` to be a primitive type in the JSON string but got " + data['clientSecret']);
        }
        // ensure the json data is a string
        if (data['grantType'] && !(typeof data['grantType'] === 'string' || data['grantType'] instanceof String)) {
            throw new Error("Expected the field `grantType` to be a primitive type in the JSON string but got " + data['grantType']);
        }
        // ensure the json data is a string
        if (data['refreshToken'] && !(typeof data['refreshToken'] === 'string' || data['refreshToken'] instanceof String)) {
            throw new Error("Expected the field `refreshToken` to be a primitive type in the JSON string but got " + data['refreshToken']);
        }

        return true;
    }


}

SessionRequest.RequiredProperties = ["clientId", "clientSecret", "grantType"];

/**
 * @member {String} clientId
 */
SessionRequest.prototype['clientId'] = undefined;

/**
 * @member {String} clientSecret
 */
SessionRequest.prototype['clientSecret'] = undefined;

/**
 * @member {module:model/SessionRequest.GrantTypeEnum} grantType
 */
SessionRequest.prototype['grantType'] = undefined;

/**
 * @member {String} refreshToken
 */
SessionRequest.prototype['refreshToken'] = undefined;





/**
 * Allowed values for the <code>grantType</code> property.
 * @enum {String}
 * @readonly
 */
SessionRequest['GrantTypeEnum'] = {

    /**
     * value: "client_credentials"
     * @const
     */
    "client_credentials": "client_credentials",

    /**
     * value: "refresh_token"
     * @const
     */
    "refresh_token": "refresh_token"
};



export default SessionRequest;

