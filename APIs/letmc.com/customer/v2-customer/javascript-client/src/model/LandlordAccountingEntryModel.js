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

/**
 * The LandlordAccountingEntryModel model module.
 * @module model/LandlordAccountingEntryModel
 * @version v2-customer
 */
class LandlordAccountingEntryModel {
    /**
     * Constructs a new <code>LandlordAccountingEntryModel</code>.
     * Landlord Accounting - Finance Entry
     * @alias module:model/LandlordAccountingEntryModel
     */
    constructor() { 
        
        LandlordAccountingEntryModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LandlordAccountingEntryModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LandlordAccountingEntryModel} obj Optional instance to populate.
     * @return {module:model/LandlordAccountingEntryModel} The populated <code>LandlordAccountingEntryModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LandlordAccountingEntryModel();

            if (data.hasOwnProperty('Amount')) {
                obj['Amount'] = ApiClient.convertToType(data['Amount'], 'Number');
            }
            if (data.hasOwnProperty('Date')) {
                obj['Date'] = ApiClient.convertToType(data['Date'], 'Date');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('TransactionNumber')) {
                obj['TransactionNumber'] = ApiClient.convertToType(data['TransactionNumber'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LandlordAccountingEntryModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LandlordAccountingEntryModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }

        return true;
    }


}



/**
 * Amount
 * @member {Number} Amount
 */
LandlordAccountingEntryModel.prototype['Amount'] = undefined;

/**
 * Payment Date
 * @member {Date} Date
 */
LandlordAccountingEntryModel.prototype['Date'] = undefined;

/**
 * Description.
 * @member {String} Description
 */
LandlordAccountingEntryModel.prototype['Description'] = undefined;

/**
 * Transaction Number
 * @member {Number} TransactionNumber
 */
LandlordAccountingEntryModel.prototype['TransactionNumber'] = undefined;






export default LandlordAccountingEntryModel;

