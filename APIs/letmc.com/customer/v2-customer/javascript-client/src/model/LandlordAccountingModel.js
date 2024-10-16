/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import LandlordAccountingEntryModel from './LandlordAccountingEntryModel';
import LandlordAccountingInvoiceModel from './LandlordAccountingInvoiceModel';

/**
 * The LandlordAccountingModel model module.
 * @module model/LandlordAccountingModel
 * @version v2-customer
 */
class LandlordAccountingModel {
    /**
     * Constructs a new <code>LandlordAccountingModel</code>.
     * Landlord Accounting
     * @alias module:model/LandlordAccountingModel
     */
    constructor() { 
        
        LandlordAccountingModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LandlordAccountingModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LandlordAccountingModel} obj Optional instance to populate.
     * @return {module:model/LandlordAccountingModel} The populated <code>LandlordAccountingModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LandlordAccountingModel();

            if (data.hasOwnProperty('AccountBalance')) {
                obj['AccountBalance'] = ApiClient.convertToType(data['AccountBalance'], 'Number');
            }
            if (data.hasOwnProperty('LastPayment')) {
                obj['LastPayment'] = ApiClient.convertToType(data['LastPayment'], 'Date');
            }
            if (data.hasOwnProperty('PaymentHistory')) {
                obj['PaymentHistory'] = ApiClient.convertToType(data['PaymentHistory'], [LandlordAccountingEntryModel]);
            }
            if (data.hasOwnProperty('Statements')) {
                obj['Statements'] = ApiClient.convertToType(data['Statements'], [LandlordAccountingInvoiceModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LandlordAccountingModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LandlordAccountingModel</code>.
     */
    static validateJSON(data) {
        if (data['PaymentHistory']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['PaymentHistory'])) {
                throw new Error("Expected the field `PaymentHistory` to be an array in the JSON data but got " + data['PaymentHistory']);
            }
            // validate the optional field `PaymentHistory` (array)
            for (const item of data['PaymentHistory']) {
                LandlordAccountingEntryModel.validateJSON(item);
            };
        }
        if (data['Statements']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Statements'])) {
                throw new Error("Expected the field `Statements` to be an array in the JSON data but got " + data['Statements']);
            }
            // validate the optional field `Statements` (array)
            for (const item of data['Statements']) {
                LandlordAccountingInvoiceModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Account Balance
 * @member {Number} AccountBalance
 */
LandlordAccountingModel.prototype['AccountBalance'] = undefined;

/**
 * Last Payment Made
 * @member {Date} LastPayment
 */
LandlordAccountingModel.prototype['LastPayment'] = undefined;

/**
 * Payment History
 * @member {Array.<module:model/LandlordAccountingEntryModel>} PaymentHistory
 */
LandlordAccountingModel.prototype['PaymentHistory'] = undefined;

/**
 * Statements
 * @member {Array.<module:model/LandlordAccountingInvoiceModel>} Statements
 */
LandlordAccountingModel.prototype['Statements'] = undefined;






export default LandlordAccountingModel;

