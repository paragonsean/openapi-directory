/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AuthorizationCodesSharedModelsAuthorizationContactInformation model module.
 * @module model/AuthorizationCodesSharedModelsAuthorizationContactInformation
 * @version v1
 */
class AuthorizationCodesSharedModelsAuthorizationContactInformation {
    /**
     * Constructs a new <code>AuthorizationCodesSharedModelsAuthorizationContactInformation</code>.
     * @alias module:model/AuthorizationCodesSharedModelsAuthorizationContactInformation
     * @param authorizationCodeID {Number} AuthorizationCode ID that the contact information ties into.
     * @param contact {String} Name of contact requesting an authorization code. Minimum length of 3 characters.
     * @param dealerCode {String} Dealer code that relates to the dealership. Minimum length of 3 characters.
     * @param dealership {String} Name of dealership. Minimum length of 3 characters.
     * @param phone {String} Phone number of contact.
     */
    constructor(authorizationCodeID, contact, dealerCode, dealership, phone) { 
        
        AuthorizationCodesSharedModelsAuthorizationContactInformation.initialize(this, authorizationCodeID, contact, dealerCode, dealership, phone);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, authorizationCodeID, contact, dealerCode, dealership, phone) { 
        obj['AuthorizationCodeID'] = authorizationCodeID;
        obj['Contact'] = contact;
        obj['DealerCode'] = dealerCode;
        obj['Dealership'] = dealership;
        obj['Phone'] = phone;
    }

    /**
     * Constructs a <code>AuthorizationCodesSharedModelsAuthorizationContactInformation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AuthorizationCodesSharedModelsAuthorizationContactInformation} obj Optional instance to populate.
     * @return {module:model/AuthorizationCodesSharedModelsAuthorizationContactInformation} The populated <code>AuthorizationCodesSharedModelsAuthorizationContactInformation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AuthorizationCodesSharedModelsAuthorizationContactInformation();

            if (data.hasOwnProperty('AuthorizationCodeID')) {
                obj['AuthorizationCodeID'] = ApiClient.convertToType(data['AuthorizationCodeID'], 'Number');
            }
            if (data.hasOwnProperty('Code')) {
                obj['Code'] = ApiClient.convertToType(data['Code'], 'String');
            }
            if (data.hasOwnProperty('Contact')) {
                obj['Contact'] = ApiClient.convertToType(data['Contact'], 'String');
            }
            if (data.hasOwnProperty('CreatedBy')) {
                obj['CreatedBy'] = ApiClient.convertToType(data['CreatedBy'], 'String');
            }
            if (data.hasOwnProperty('CreatedDate')) {
                obj['CreatedDate'] = ApiClient.convertToType(data['CreatedDate'], 'Date');
            }
            if (data.hasOwnProperty('DealerCode')) {
                obj['DealerCode'] = ApiClient.convertToType(data['DealerCode'], 'String');
            }
            if (data.hasOwnProperty('Dealership')) {
                obj['Dealership'] = ApiClient.convertToType(data['Dealership'], 'String');
            }
            if (data.hasOwnProperty('DefinitionName')) {
                obj['DefinitionName'] = ApiClient.convertToType(data['DefinitionName'], 'String');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('ID')) {
                obj['ID'] = ApiClient.convertToType(data['ID'], 'Number');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('Phone')) {
                obj['Phone'] = ApiClient.convertToType(data['Phone'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AuthorizationCodesSharedModelsAuthorizationContactInformation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AuthorizationCodesSharedModelsAuthorizationContactInformation</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AuthorizationCodesSharedModelsAuthorizationContactInformation.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['Code'] && !(typeof data['Code'] === 'string' || data['Code'] instanceof String)) {
            throw new Error("Expected the field `Code` to be a primitive type in the JSON string but got " + data['Code']);
        }
        // ensure the json data is a string
        if (data['Contact'] && !(typeof data['Contact'] === 'string' || data['Contact'] instanceof String)) {
            throw new Error("Expected the field `Contact` to be a primitive type in the JSON string but got " + data['Contact']);
        }
        // ensure the json data is a string
        if (data['CreatedBy'] && !(typeof data['CreatedBy'] === 'string' || data['CreatedBy'] instanceof String)) {
            throw new Error("Expected the field `CreatedBy` to be a primitive type in the JSON string but got " + data['CreatedBy']);
        }
        // ensure the json data is a string
        if (data['DealerCode'] && !(typeof data['DealerCode'] === 'string' || data['DealerCode'] instanceof String)) {
            throw new Error("Expected the field `DealerCode` to be a primitive type in the JSON string but got " + data['DealerCode']);
        }
        // ensure the json data is a string
        if (data['Dealership'] && !(typeof data['Dealership'] === 'string' || data['Dealership'] instanceof String)) {
            throw new Error("Expected the field `Dealership` to be a primitive type in the JSON string but got " + data['Dealership']);
        }
        // ensure the json data is a string
        if (data['DefinitionName'] && !(typeof data['DefinitionName'] === 'string' || data['DefinitionName'] instanceof String)) {
            throw new Error("Expected the field `DefinitionName` to be a primitive type in the JSON string but got " + data['DefinitionName']);
        }
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['Phone'] && !(typeof data['Phone'] === 'string' || data['Phone'] instanceof String)) {
            throw new Error("Expected the field `Phone` to be a primitive type in the JSON string but got " + data['Phone']);
        }

        return true;
    }


}

AuthorizationCodesSharedModelsAuthorizationContactInformation.RequiredProperties = ["AuthorizationCodeID", "Contact", "DealerCode", "Dealership", "Phone"];

/**
 * AuthorizationCode ID that the contact information ties into.
 * @member {Number} AuthorizationCodeID
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['AuthorizationCodeID'] = undefined;

/**
 * The authorization code. Read Only.
 * @member {String} Code
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['Code'] = undefined;

/**
 * Name of contact requesting an authorization code. Minimum length of 3 characters.
 * @member {String} Contact
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['Contact'] = undefined;

/**
 * The name of the user that created this code. Read Only.
 * @member {String} CreatedBy
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['CreatedBy'] = undefined;

/**
 * The date the authorization code was created.
 * @member {Date} CreatedDate
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['CreatedDate'] = undefined;

/**
 * Dealer code that relates to the dealership. Minimum length of 3 characters.
 * @member {String} DealerCode
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['DealerCode'] = undefined;

/**
 * Name of dealership. Minimum length of 3 characters.
 * @member {String} Dealership
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['Dealership'] = undefined;

/**
 * The name of the definition used for generating this authorization code. Read Only.
 * @member {String} DefinitionName
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['DefinitionName'] = undefined;

/**
 * Email of contact.
 * @member {String} Email
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['Email'] = undefined;

/**
 * ID of authorizationContactInformation
 * @member {Number} ID
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['ID'] = undefined;

/**
 * Optional notes used for internal use.
 * @member {String} Notes
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['Notes'] = undefined;

/**
 * Phone number of contact.
 * @member {String} Phone
 */
AuthorizationCodesSharedModelsAuthorizationContactInformation.prototype['Phone'] = undefined;






export default AuthorizationCodesSharedModelsAuthorizationContactInformation;

