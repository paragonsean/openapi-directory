/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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
import EFTBankDto from './EFTBankDto';
import OwnerOpeningBalanceDto from './OwnerOpeningBalanceDto';
import OwnerOpeningBalanceInPeriodsDto from './OwnerOpeningBalanceInPeriodsDto';

/**
 * The CustomerDto model module.
 * @module model/CustomerDto
 * @version v1
 */
class CustomerDto {
    /**
     * Constructs a new <code>CustomerDto</code>.
     * @alias module:model/CustomerDto
     */
    constructor() { 
        
        CustomerDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CustomerDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CustomerDto} obj Optional instance to populate.
     * @return {module:model/CustomerDto} The populated <code>CustomerDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CustomerDto();

            if (data.hasOwnProperty('accountName')) {
                obj['accountName'] = ApiClient.convertToType(data['accountName'], 'String');
            }
            if (data.hasOwnProperty('accountNumber')) {
                obj['accountNumber'] = ApiClient.convertToType(data['accountNumber'], 'String');
            }
            if (data.hasOwnProperty('additionalEmails')) {
                obj['additionalEmails'] = ApiClient.convertToType(data['additionalEmails'], ['String']);
            }
            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], ['String']);
            }
            if (data.hasOwnProperty('authCode')) {
                obj['authCode'] = ApiClient.convertToType(data['authCode'], 'String');
            }
            if (data.hasOwnProperty('bank')) {
                obj['bank'] = EFTBankDto.constructFromObject(data['bank']);
            }
            if (data.hasOwnProperty('businessIdentifierCode')) {
                obj['businessIdentifierCode'] = ApiClient.convertToType(data['businessIdentifierCode'], 'String');
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('contact')) {
                obj['contact'] = ApiClient.convertToType(data['contact'], 'String');
            }
            if (data.hasOwnProperty('delivery')) {
                obj['delivery'] = ApiClient.convertToType(data['delivery'], ['String']);
            }
            if (data.hasOwnProperty('eFTReference')) {
                obj['eFTReference'] = ApiClient.convertToType(data['eFTReference'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('fax')) {
                obj['fax'] = ApiClient.convertToType(data['fax'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('internationalBankAccountNumber')) {
                obj['internationalBankAccountNumber'] = ApiClient.convertToType(data['internationalBankAccountNumber'], 'String');
            }
            if (data.hasOwnProperty('ledgerBalance')) {
                obj['ledgerBalance'] = ApiClient.convertToType(data['ledgerBalance'], 'Number');
            }
            if (data.hasOwnProperty('mobile')) {
                obj['mobile'] = ApiClient.convertToType(data['mobile'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('openingBalance')) {
                obj['openingBalance'] = OwnerOpeningBalanceInPeriodsDto.constructFromObject(data['openingBalance']);
            }
            if (data.hasOwnProperty('openingBalances')) {
                obj['openingBalances'] = ApiClient.convertToType(data['openingBalances'], [OwnerOpeningBalanceDto]);
            }
            if (data.hasOwnProperty('ourCode')) {
                obj['ourCode'] = ApiClient.convertToType(data['ourCode'], 'String');
            }
            if (data.hasOwnProperty('ownerTypeId')) {
                obj['ownerTypeId'] = ApiClient.convertToType(data['ownerTypeId'], 'Number');
            }
            if (data.hasOwnProperty('phone')) {
                obj['phone'] = ApiClient.convertToType(data['phone'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Blob');
            }
            if (data.hasOwnProperty('vatAnalysisTypeId')) {
                obj['vatAnalysisTypeId'] = ApiClient.convertToType(data['vatAnalysisTypeId'], 'Number');
            }
            if (data.hasOwnProperty('vatReg')) {
                obj['vatReg'] = ApiClient.convertToType(data['vatReg'], 'String');
            }
            if (data.hasOwnProperty('vatType')) {
                obj['vatType'] = ApiClient.convertToType(data['vatType'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CustomerDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CustomerDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['accountName'] && !(typeof data['accountName'] === 'string' || data['accountName'] instanceof String)) {
            throw new Error("Expected the field `accountName` to be a primitive type in the JSON string but got " + data['accountName']);
        }
        // ensure the json data is a string
        if (data['accountNumber'] && !(typeof data['accountNumber'] === 'string' || data['accountNumber'] instanceof String)) {
            throw new Error("Expected the field `accountNumber` to be a primitive type in the JSON string but got " + data['accountNumber']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['additionalEmails'])) {
            throw new Error("Expected the field `additionalEmails` to be an array in the JSON data but got " + data['additionalEmails']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['address'])) {
            throw new Error("Expected the field `address` to be an array in the JSON data but got " + data['address']);
        }
        // ensure the json data is a string
        if (data['authCode'] && !(typeof data['authCode'] === 'string' || data['authCode'] instanceof String)) {
            throw new Error("Expected the field `authCode` to be a primitive type in the JSON string but got " + data['authCode']);
        }
        // validate the optional field `bank`
        if (data['bank']) { // data not null
          EFTBankDto.validateJSON(data['bank']);
        }
        // ensure the json data is a string
        if (data['businessIdentifierCode'] && !(typeof data['businessIdentifierCode'] === 'string' || data['businessIdentifierCode'] instanceof String)) {
            throw new Error("Expected the field `businessIdentifierCode` to be a primitive type in the JSON string but got " + data['businessIdentifierCode']);
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['contact'] && !(typeof data['contact'] === 'string' || data['contact'] instanceof String)) {
            throw new Error("Expected the field `contact` to be a primitive type in the JSON string but got " + data['contact']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['delivery'])) {
            throw new Error("Expected the field `delivery` to be an array in the JSON data but got " + data['delivery']);
        }
        // ensure the json data is a string
        if (data['eFTReference'] && !(typeof data['eFTReference'] === 'string' || data['eFTReference'] instanceof String)) {
            throw new Error("Expected the field `eFTReference` to be a primitive type in the JSON string but got " + data['eFTReference']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['fax'] && !(typeof data['fax'] === 'string' || data['fax'] instanceof String)) {
            throw new Error("Expected the field `fax` to be a primitive type in the JSON string but got " + data['fax']);
        }
        // ensure the json data is a string
        if (data['internationalBankAccountNumber'] && !(typeof data['internationalBankAccountNumber'] === 'string' || data['internationalBankAccountNumber'] instanceof String)) {
            throw new Error("Expected the field `internationalBankAccountNumber` to be a primitive type in the JSON string but got " + data['internationalBankAccountNumber']);
        }
        // ensure the json data is a string
        if (data['mobile'] && !(typeof data['mobile'] === 'string' || data['mobile'] instanceof String)) {
            throw new Error("Expected the field `mobile` to be a primitive type in the JSON string but got " + data['mobile']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `openingBalance`
        if (data['openingBalance']) { // data not null
          OwnerOpeningBalanceInPeriodsDto.validateJSON(data['openingBalance']);
        }
        if (data['openingBalances']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['openingBalances'])) {
                throw new Error("Expected the field `openingBalances` to be an array in the JSON data but got " + data['openingBalances']);
            }
            // validate the optional field `openingBalances` (array)
            for (const item of data['openingBalances']) {
                OwnerOpeningBalanceDto.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['ourCode'] && !(typeof data['ourCode'] === 'string' || data['ourCode'] instanceof String)) {
            throw new Error("Expected the field `ourCode` to be a primitive type in the JSON string but got " + data['ourCode']);
        }
        // ensure the json data is a string
        if (data['phone'] && !(typeof data['phone'] === 'string' || data['phone'] instanceof String)) {
            throw new Error("Expected the field `phone` to be a primitive type in the JSON string but got " + data['phone']);
        }
        // ensure the json data is a string
        if (data['vatReg'] && !(typeof data['vatReg'] === 'string' || data['vatReg'] instanceof String)) {
            throw new Error("Expected the field `vatReg` to be a primitive type in the JSON string but got " + data['vatReg']);
        }

        return true;
    }


}



/**
 * @member {String} accountName
 */
CustomerDto.prototype['accountName'] = undefined;

/**
 * @member {String} accountNumber
 */
CustomerDto.prototype['accountNumber'] = undefined;

/**
 * @member {Array.<String>} additionalEmails
 */
CustomerDto.prototype['additionalEmails'] = undefined;

/**
 * @member {Array.<String>} address
 */
CustomerDto.prototype['address'] = undefined;

/**
 * @member {String} authCode
 */
CustomerDto.prototype['authCode'] = undefined;

/**
 * @member {module:model/EFTBankDto} bank
 */
CustomerDto.prototype['bank'] = undefined;

/**
 * @member {String} businessIdentifierCode
 */
CustomerDto.prototype['businessIdentifierCode'] = undefined;

/**
 * @member {String} code
 */
CustomerDto.prototype['code'] = undefined;

/**
 * @member {String} contact
 */
CustomerDto.prototype['contact'] = undefined;

/**
 * @member {Array.<String>} delivery
 */
CustomerDto.prototype['delivery'] = undefined;

/**
 * @member {String} eFTReference
 */
CustomerDto.prototype['eFTReference'] = undefined;

/**
 * @member {String} email
 */
CustomerDto.prototype['email'] = undefined;

/**
 * @member {String} fax
 */
CustomerDto.prototype['fax'] = undefined;

/**
 * @member {Number} id
 */
CustomerDto.prototype['id'] = undefined;

/**
 * @member {String} internationalBankAccountNumber
 */
CustomerDto.prototype['internationalBankAccountNumber'] = undefined;

/**
 * @member {Number} ledgerBalance
 */
CustomerDto.prototype['ledgerBalance'] = undefined;

/**
 * @member {String} mobile
 */
CustomerDto.prototype['mobile'] = undefined;

/**
 * @member {String} name
 */
CustomerDto.prototype['name'] = undefined;

/**
 * @member {module:model/OwnerOpeningBalanceInPeriodsDto} openingBalance
 */
CustomerDto.prototype['openingBalance'] = undefined;

/**
 * @member {Array.<module:model/OwnerOpeningBalanceDto>} openingBalances
 */
CustomerDto.prototype['openingBalances'] = undefined;

/**
 * @member {String} ourCode
 */
CustomerDto.prototype['ourCode'] = undefined;

/**
 * @member {Number} ownerTypeId
 */
CustomerDto.prototype['ownerTypeId'] = undefined;

/**
 * @member {String} phone
 */
CustomerDto.prototype['phone'] = undefined;

/**
 * @member {Blob} timestamp
 */
CustomerDto.prototype['timestamp'] = undefined;

/**
 * @member {Number} vatAnalysisTypeId
 */
CustomerDto.prototype['vatAnalysisTypeId'] = undefined;

/**
 * @member {String} vatReg
 */
CustomerDto.prototype['vatReg'] = undefined;

/**
 * @member {Number} vatType
 */
CustomerDto.prototype['vatType'] = undefined;






export default CustomerDto;

