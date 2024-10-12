/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import StorageRequiredFields from './StorageRequiredFields';
import TaxRequiredFields from './TaxRequiredFields';
import Transaction from './Transaction';

/**
 * The UnconfirmTransactionOut model module.
 * @module model/UnconfirmTransactionOut
 * @version 1
 */
class UnconfirmTransactionOut {
    /**
     * Constructs a new <code>UnconfirmTransactionOut</code>.
     * @alias module:model/UnconfirmTransactionOut
     */
    constructor() { 
        
        UnconfirmTransactionOut.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UnconfirmTransactionOut</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UnconfirmTransactionOut} obj Optional instance to populate.
     * @return {module:model/UnconfirmTransactionOut} The populated <code>UnconfirmTransactionOut</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UnconfirmTransactionOut();

            if (data.hasOwnProperty('storage_required_fields')) {
                obj['storage_required_fields'] = ApiClient.convertToType(data['storage_required_fields'], [StorageRequiredFields]);
            }
            if (data.hasOwnProperty('tax_required_fields')) {
                obj['tax_required_fields'] = ApiClient.convertToType(data['tax_required_fields'], [TaxRequiredFields]);
            }
            if (data.hasOwnProperty('transaction')) {
                obj['transaction'] = Transaction.constructFromObject(data['transaction']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UnconfirmTransactionOut</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UnconfirmTransactionOut</code>.
     */
    static validateJSON(data) {
        if (data['storage_required_fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['storage_required_fields'])) {
                throw new Error("Expected the field `storage_required_fields` to be an array in the JSON data but got " + data['storage_required_fields']);
            }
            // validate the optional field `storage_required_fields` (array)
            for (const item of data['storage_required_fields']) {
                StorageRequiredFields.validateJSON(item);
            };
        }
        if (data['tax_required_fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tax_required_fields'])) {
                throw new Error("Expected the field `tax_required_fields` to be an array in the JSON data but got " + data['tax_required_fields']);
            }
            // validate the optional field `tax_required_fields` (array)
            for (const item of data['tax_required_fields']) {
                TaxRequiredFields.validateJSON(item);
            };
        }
        // validate the optional field `transaction`
        if (data['transaction']) { // data not null
          Transaction.validateJSON(data['transaction']);
        }

        return true;
    }


}



/**
 * Fields required for transaction storage (can be added later - it's up to merchant software). Depends on the region/transaction type.
 * @member {Array.<module:model/StorageRequiredFields>} storage_required_fields
 */
UnconfirmTransactionOut.prototype['storage_required_fields'] = undefined;

/**
 * Fields required for tax calculation. Depends on the region/transaction type.
 * @member {Array.<module:model/TaxRequiredFields>} tax_required_fields
 */
UnconfirmTransactionOut.prototype['tax_required_fields'] = undefined;

/**
 * @member {module:model/Transaction} transaction
 */
UnconfirmTransactionOut.prototype['transaction'] = undefined;






export default UnconfirmTransactionOut;

