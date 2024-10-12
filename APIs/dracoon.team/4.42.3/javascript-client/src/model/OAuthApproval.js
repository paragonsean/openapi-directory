/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OAuthApproval model module.
 * @module model/OAuthApproval
 * @version 4.42.3
 */
class OAuthApproval {
    /**
     * Constructs a new <code>OAuthApproval</code>.
     * OAuth client approval information
     * @alias module:model/OAuthApproval
     * @param clientId {String} ID of the OAuth client
     * @param clientName {String} Name, which is shown at the client configuration and authorization.
     */
    constructor(clientId, clientName) { 
        
        OAuthApproval.initialize(this, clientId, clientName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, clientId, clientName) { 
        obj['clientId'] = clientId;
        obj['clientName'] = clientName;
    }

    /**
     * Constructs a <code>OAuthApproval</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OAuthApproval} obj Optional instance to populate.
     * @return {module:model/OAuthApproval} The populated <code>OAuthApproval</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OAuthApproval();

            if (data.hasOwnProperty('clientId')) {
                obj['clientId'] = ApiClient.convertToType(data['clientId'], 'String');
            }
            if (data.hasOwnProperty('clientName')) {
                obj['clientName'] = ApiClient.convertToType(data['clientName'], 'String');
            }
            if (data.hasOwnProperty('expiresAt')) {
                obj['expiresAt'] = ApiClient.convertToType(data['expiresAt'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OAuthApproval</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OAuthApproval</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OAuthApproval.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['clientId'] && !(typeof data['clientId'] === 'string' || data['clientId'] instanceof String)) {
            throw new Error("Expected the field `clientId` to be a primitive type in the JSON string but got " + data['clientId']);
        }
        // ensure the json data is a string
        if (data['clientName'] && !(typeof data['clientName'] === 'string' || data['clientName'] instanceof String)) {
            throw new Error("Expected the field `clientName` to be a primitive type in the JSON string but got " + data['clientName']);
        }

        return true;
    }


}

OAuthApproval.RequiredProperties = ["clientId", "clientName"];

/**
 * ID of the OAuth client
 * @member {String} clientId
 */
OAuthApproval.prototype['clientId'] = undefined;

/**
 * Name, which is shown at the client configuration and authorization.
 * @member {String} clientName
 */
OAuthApproval.prototype['clientName'] = undefined;

/**
 * Expiration date of the approval
 * @member {Date} expiresAt
 */
OAuthApproval.prototype['expiresAt'] = undefined;






export default OAuthApproval;

