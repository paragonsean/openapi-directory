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
import CustomerAttributes from './CustomerAttributes';

/**
 * The UpdateCustomerResponse model module.
 * @module model/UpdateCustomerResponse
 * @version 4.42.3
 */
class UpdateCustomerResponse {
    /**
     * Constructs a new <code>UpdateCustomerResponse</code>.
     * Customer information
     * @alias module:model/UpdateCustomerResponse
     * @param companyName {String} Company name
     * @param customerContractType {module:model/UpdateCustomerResponse.CustomerContractTypeEnum} Customer type
     * @param customerUuid {String} &#128640; Since v4.21.0  Customer UUID
     * @param id {Number} Unique identifier for the customer
     * @param lockStatus {Boolean} &#128679; Deprecated since v4.7.0  Customer lock status:  * `false` - unlocked  * `true` - locked    Please use `isLocked` instead.  All users of this customer will be blocked and can not login anymore.
     * @param quotaMax {Number} Maximal disc space which can be allocated by customer in bytes. -1 for unlimited
     * @param userMax {Number} Maximal number of users
     */
    constructor(companyName, customerContractType, customerUuid, id, lockStatus, quotaMax, userMax) { 
        
        UpdateCustomerResponse.initialize(this, companyName, customerContractType, customerUuid, id, lockStatus, quotaMax, userMax);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, companyName, customerContractType, customerUuid, id, lockStatus, quotaMax, userMax) { 
        obj['companyName'] = companyName;
        obj['customerContractType'] = customerContractType;
        obj['customerUuid'] = customerUuid;
        obj['id'] = id;
        obj['isLocked'] = false;
        obj['lockStatus'] = lockStatus || false;
        obj['quotaMax'] = quotaMax;
        obj['userMax'] = userMax;
    }

    /**
     * Constructs a <code>UpdateCustomerResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateCustomerResponse} obj Optional instance to populate.
     * @return {module:model/UpdateCustomerResponse} The populated <code>UpdateCustomerResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateCustomerResponse();

            if (data.hasOwnProperty('activationCode')) {
                obj['activationCode'] = ApiClient.convertToType(data['activationCode'], 'String');
            }
            if (data.hasOwnProperty('companyName')) {
                obj['companyName'] = ApiClient.convertToType(data['companyName'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('customerAttributes')) {
                obj['customerAttributes'] = CustomerAttributes.constructFromObject(data['customerAttributes']);
            }
            if (data.hasOwnProperty('customerContractType')) {
                obj['customerContractType'] = ApiClient.convertToType(data['customerContractType'], 'String');
            }
            if (data.hasOwnProperty('customerUuid')) {
                obj['customerUuid'] = ApiClient.convertToType(data['customerUuid'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('isLocked')) {
                obj['isLocked'] = ApiClient.convertToType(data['isLocked'], 'Boolean');
            }
            if (data.hasOwnProperty('lockStatus')) {
                obj['lockStatus'] = ApiClient.convertToType(data['lockStatus'], 'Boolean');
            }
            if (data.hasOwnProperty('providerCustomerId')) {
                obj['providerCustomerId'] = ApiClient.convertToType(data['providerCustomerId'], 'String');
            }
            if (data.hasOwnProperty('quotaMax')) {
                obj['quotaMax'] = ApiClient.convertToType(data['quotaMax'], 'Number');
            }
            if (data.hasOwnProperty('trialDays')) {
                obj['trialDays'] = ApiClient.convertToType(data['trialDays'], 'Number');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('userMax')) {
                obj['userMax'] = ApiClient.convertToType(data['userMax'], 'Number');
            }
            if (data.hasOwnProperty('webhooksMax')) {
                obj['webhooksMax'] = ApiClient.convertToType(data['webhooksMax'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateCustomerResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateCustomerResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateCustomerResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['activationCode'] && !(typeof data['activationCode'] === 'string' || data['activationCode'] instanceof String)) {
            throw new Error("Expected the field `activationCode` to be a primitive type in the JSON string but got " + data['activationCode']);
        }
        // ensure the json data is a string
        if (data['companyName'] && !(typeof data['companyName'] === 'string' || data['companyName'] instanceof String)) {
            throw new Error("Expected the field `companyName` to be a primitive type in the JSON string but got " + data['companyName']);
        }
        // validate the optional field `customerAttributes`
        if (data['customerAttributes']) { // data not null
          CustomerAttributes.validateJSON(data['customerAttributes']);
        }
        // ensure the json data is a string
        if (data['customerContractType'] && !(typeof data['customerContractType'] === 'string' || data['customerContractType'] instanceof String)) {
            throw new Error("Expected the field `customerContractType` to be a primitive type in the JSON string but got " + data['customerContractType']);
        }
        // ensure the json data is a string
        if (data['customerUuid'] && !(typeof data['customerUuid'] === 'string' || data['customerUuid'] instanceof String)) {
            throw new Error("Expected the field `customerUuid` to be a primitive type in the JSON string but got " + data['customerUuid']);
        }
        // ensure the json data is a string
        if (data['providerCustomerId'] && !(typeof data['providerCustomerId'] === 'string' || data['providerCustomerId'] instanceof String)) {
            throw new Error("Expected the field `providerCustomerId` to be a primitive type in the JSON string but got " + data['providerCustomerId']);
        }

        return true;
    }


}

UpdateCustomerResponse.RequiredProperties = ["companyName", "customerContractType", "customerUuid", "id", "lockStatus", "quotaMax", "userMax"];

/**
 * &#128679; Deprecated since v4.8.0  Customer activation code string:  * valid only for types `free` and `demo`  * for `pay` customers it is empty
 * @member {String} activationCode
 */
UpdateCustomerResponse.prototype['activationCode'] = undefined;

/**
 * Company name
 * @member {String} companyName
 */
UpdateCustomerResponse.prototype['companyName'] = undefined;

/**
 * Creation date
 * @member {Date} createdAt
 */
UpdateCustomerResponse.prototype['createdAt'] = undefined;

/**
 * @member {module:model/CustomerAttributes} customerAttributes
 */
UpdateCustomerResponse.prototype['customerAttributes'] = undefined;

/**
 * Customer type
 * @member {module:model/UpdateCustomerResponse.CustomerContractTypeEnum} customerContractType
 */
UpdateCustomerResponse.prototype['customerContractType'] = undefined;

/**
 * &#128640; Since v4.21.0  Customer UUID
 * @member {String} customerUuid
 */
UpdateCustomerResponse.prototype['customerUuid'] = undefined;

/**
 * Unique identifier for the customer
 * @member {Number} id
 */
UpdateCustomerResponse.prototype['id'] = undefined;

/**
 * Customer is locked:  * `false` - unlocked  * `true` - locked    All users of this customer will be blocked and can not login anymore.
 * @member {Boolean} isLocked
 * @default false
 */
UpdateCustomerResponse.prototype['isLocked'] = false;

/**
 * &#128679; Deprecated since v4.7.0  Customer lock status:  * `false` - unlocked  * `true` - locked    Please use `isLocked` instead.  All users of this customer will be blocked and can not login anymore.
 * @member {Boolean} lockStatus
 * @default false
 */
UpdateCustomerResponse.prototype['lockStatus'] = false;

/**
 * Provider customer ID
 * @member {String} providerCustomerId
 */
UpdateCustomerResponse.prototype['providerCustomerId'] = undefined;

/**
 * Maximal disc space which can be allocated by customer in bytes. -1 for unlimited
 * @member {Number} quotaMax
 */
UpdateCustomerResponse.prototype['quotaMax'] = undefined;

/**
 * Number of days left for trial period (relevant only for type `demo`)  (not used)
 * @member {Number} trialDays
 */
UpdateCustomerResponse.prototype['trialDays'] = undefined;

/**
 * Modification date
 * @member {Date} updatedAt
 */
UpdateCustomerResponse.prototype['updatedAt'] = undefined;

/**
 * Maximal number of users
 * @member {Number} userMax
 */
UpdateCustomerResponse.prototype['userMax'] = undefined;

/**
 * &#128640; Since v4.19.0  Maximal number of webhooks
 * @member {Number} webhooksMax
 */
UpdateCustomerResponse.prototype['webhooksMax'] = undefined;





/**
 * Allowed values for the <code>customerContractType</code> property.
 * @enum {String}
 * @readonly
 */
UpdateCustomerResponse['CustomerContractTypeEnum'] = {

    /**
     * value: "demo"
     * @const
     */
    "demo": "demo",

    /**
     * value: "free"
     * @const
     */
    "free": "free",

    /**
     * value: "pay"
     * @const
     */
    "pay": "pay"
};



export default UpdateCustomerResponse;

