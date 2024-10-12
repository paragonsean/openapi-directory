/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CompanyCreditDataCreditBalanceOptionsInterface from './CompanyCreditDataCreditBalanceOptionsInterface';

/**
 * The CompanyCreditCreditBalanceManagementV1DecreasePostRequest model module.
 * @module model/CompanyCreditCreditBalanceManagementV1DecreasePostRequest
 * @version 2.2.10
 */
class CompanyCreditCreditBalanceManagementV1DecreasePostRequest {
    /**
     * Constructs a new <code>CompanyCreditCreditBalanceManagementV1DecreasePostRequest</code>.
     * @alias module:model/CompanyCreditCreditBalanceManagementV1DecreasePostRequest
     * @param currency {String} 
     * @param operationType {Number} 
     * @param value {Number} 
     */
    constructor(currency, operationType, value) { 
        
        CompanyCreditCreditBalanceManagementV1DecreasePostRequest.initialize(this, currency, operationType, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, currency, operationType, value) { 
        obj['currency'] = currency;
        obj['operationType'] = operationType;
        obj['value'] = value;
    }

    /**
     * Constructs a <code>CompanyCreditCreditBalanceManagementV1DecreasePostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CompanyCreditCreditBalanceManagementV1DecreasePostRequest} obj Optional instance to populate.
     * @return {module:model/CompanyCreditCreditBalanceManagementV1DecreasePostRequest} The populated <code>CompanyCreditCreditBalanceManagementV1DecreasePostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CompanyCreditCreditBalanceManagementV1DecreasePostRequest();

            if (data.hasOwnProperty('comment')) {
                obj['comment'] = ApiClient.convertToType(data['comment'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('operationType')) {
                obj['operationType'] = ApiClient.convertToType(data['operationType'], 'Number');
            }
            if (data.hasOwnProperty('options')) {
                obj['options'] = CompanyCreditDataCreditBalanceOptionsInterface.constructFromObject(data['options']);
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CompanyCreditCreditBalanceManagementV1DecreasePostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CompanyCreditCreditBalanceManagementV1DecreasePostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CompanyCreditCreditBalanceManagementV1DecreasePostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['comment'] && !(typeof data['comment'] === 'string' || data['comment'] instanceof String)) {
            throw new Error("Expected the field `comment` to be a primitive type in the JSON string but got " + data['comment']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // validate the optional field `options`
        if (data['options']) { // data not null
          CompanyCreditDataCreditBalanceOptionsInterface.validateJSON(data['options']);
        }

        return true;
    }


}

CompanyCreditCreditBalanceManagementV1DecreasePostRequest.RequiredProperties = ["currency", "operationType", "value"];

/**
 * [optional]
 * @member {String} comment
 */
CompanyCreditCreditBalanceManagementV1DecreasePostRequest.prototype['comment'] = undefined;

/**
 * @member {String} currency
 */
CompanyCreditCreditBalanceManagementV1DecreasePostRequest.prototype['currency'] = undefined;

/**
 * @member {Number} operationType
 */
CompanyCreditCreditBalanceManagementV1DecreasePostRequest.prototype['operationType'] = undefined;

/**
 * @member {module:model/CompanyCreditDataCreditBalanceOptionsInterface} options
 */
CompanyCreditCreditBalanceManagementV1DecreasePostRequest.prototype['options'] = undefined;

/**
 * @member {Number} value
 */
CompanyCreditCreditBalanceManagementV1DecreasePostRequest.prototype['value'] = undefined;






export default CompanyCreditCreditBalanceManagementV1DecreasePostRequest;

