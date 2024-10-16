/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
import ILoanRepaymentToShareholder from './ILoanRepaymentToShareholder';
import IManualDividendDistribution from './IManualDividendDistribution';
import IShareRedemption from './IShareRedemption';

/**
 * The IWithdrawals model module.
 * @module model/IWithdrawals
 * @version v1
 */
class IWithdrawals {
    /**
     * Constructs a new <code>IWithdrawals</code>.
     * @alias module:model/IWithdrawals
     */
    constructor() { 
        
        IWithdrawals.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IWithdrawals</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IWithdrawals} obj Optional instance to populate.
     * @return {module:model/IWithdrawals} The populated <code>IWithdrawals</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IWithdrawals();

            if (data.hasOwnProperty('loanRepaymentsToShareholder')) {
                obj['loanRepaymentsToShareholder'] = ApiClient.convertToType(data['loanRepaymentsToShareholder'], [ILoanRepaymentToShareholder]);
            }
            if (data.hasOwnProperty('manualDividendDistributions')) {
                obj['manualDividendDistributions'] = ApiClient.convertToType(data['manualDividendDistributions'], [IManualDividendDistribution]);
            }
            if (data.hasOwnProperty('shareRedemptions')) {
                obj['shareRedemptions'] = ApiClient.convertToType(data['shareRedemptions'], [IShareRedemption]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IWithdrawals</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IWithdrawals</code>.
     */
    static validateJSON(data) {
        if (data['loanRepaymentsToShareholder']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['loanRepaymentsToShareholder'])) {
                throw new Error("Expected the field `loanRepaymentsToShareholder` to be an array in the JSON data but got " + data['loanRepaymentsToShareholder']);
            }
            // validate the optional field `loanRepaymentsToShareholder` (array)
            for (const item of data['loanRepaymentsToShareholder']) {
                ILoanRepaymentToShareholder.validateJSON(item);
            };
        }
        if (data['manualDividendDistributions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['manualDividendDistributions'])) {
                throw new Error("Expected the field `manualDividendDistributions` to be an array in the JSON data but got " + data['manualDividendDistributions']);
            }
            // validate the optional field `manualDividendDistributions` (array)
            for (const item of data['manualDividendDistributions']) {
                IManualDividendDistribution.validateJSON(item);
            };
        }
        if (data['shareRedemptions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['shareRedemptions'])) {
                throw new Error("Expected the field `shareRedemptions` to be an array in the JSON data but got " + data['shareRedemptions']);
            }
            // validate the optional field `shareRedemptions` (array)
            for (const item of data['shareRedemptions']) {
                IShareRedemption.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ILoanRepaymentToShareholder>} loanRepaymentsToShareholder
 */
IWithdrawals.prototype['loanRepaymentsToShareholder'] = undefined;

/**
 * @member {Array.<module:model/IManualDividendDistribution>} manualDividendDistributions
 */
IWithdrawals.prototype['manualDividendDistributions'] = undefined;

/**
 * @member {Array.<module:model/IShareRedemption>} shareRedemptions
 */
IWithdrawals.prototype['shareRedemptions'] = undefined;






export default IWithdrawals;

