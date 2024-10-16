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
import Currency from './Currency';

/**
 * The ITaxes model module.
 * @module model/ITaxes
 * @version v1
 */
class ITaxes {
    /**
     * Constructs a new <code>ITaxes</code>.
     * @alias module:model/ITaxes
     */
    constructor() { 
        
        ITaxes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ITaxes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ITaxes} obj Optional instance to populate.
     * @return {module:model/ITaxes} The populated <code>ITaxes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ITaxes();

            if (data.hasOwnProperty('estate')) {
                obj['estate'] = Currency.constructFromObject(data['estate']);
            }
            if (data.hasOwnProperty('federalIncome')) {
                obj['federalIncome'] = Currency.constructFromObject(data['federalIncome']);
            }
            if (data.hasOwnProperty('giftAndGenerationSkippingTransfer')) {
                obj['giftAndGenerationSkippingTransfer'] = Currency.constructFromObject(data['giftAndGenerationSkippingTransfer']);
            }
            if (data.hasOwnProperty('medicare')) {
                obj['medicare'] = Currency.constructFromObject(data['medicare']);
            }
            if (data.hasOwnProperty('pensionEarlyDistributionPenalty')) {
                obj['pensionEarlyDistributionPenalty'] = Currency.constructFromObject(data['pensionEarlyDistributionPenalty']);
            }
            if (data.hasOwnProperty('pensionPenaltyOnExcessDistributions')) {
                obj['pensionPenaltyOnExcessDistributions'] = Currency.constructFromObject(data['pensionPenaltyOnExcessDistributions']);
            }
            if (data.hasOwnProperty('refundableCredits')) {
                obj['refundableCredits'] = Currency.constructFromObject(data['refundableCredits']);
            }
            if (data.hasOwnProperty('socialSecurityEmployer')) {
                obj['socialSecurityEmployer'] = Currency.constructFromObject(data['socialSecurityEmployer']);
            }
            if (data.hasOwnProperty('socialSecuritySelfEmployed')) {
                obj['socialSecuritySelfEmployed'] = Currency.constructFromObject(data['socialSecuritySelfEmployed']);
            }
            if (data.hasOwnProperty('stateIncome')) {
                obj['stateIncome'] = Currency.constructFromObject(data['stateIncome']);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = Currency.constructFromObject(data['total']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ITaxes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ITaxes</code>.
     */
    static validateJSON(data) {
        // validate the optional field `estate`
        if (data['estate']) { // data not null
          Currency.validateJSON(data['estate']);
        }
        // validate the optional field `federalIncome`
        if (data['federalIncome']) { // data not null
          Currency.validateJSON(data['federalIncome']);
        }
        // validate the optional field `giftAndGenerationSkippingTransfer`
        if (data['giftAndGenerationSkippingTransfer']) { // data not null
          Currency.validateJSON(data['giftAndGenerationSkippingTransfer']);
        }
        // validate the optional field `medicare`
        if (data['medicare']) { // data not null
          Currency.validateJSON(data['medicare']);
        }
        // validate the optional field `pensionEarlyDistributionPenalty`
        if (data['pensionEarlyDistributionPenalty']) { // data not null
          Currency.validateJSON(data['pensionEarlyDistributionPenalty']);
        }
        // validate the optional field `pensionPenaltyOnExcessDistributions`
        if (data['pensionPenaltyOnExcessDistributions']) { // data not null
          Currency.validateJSON(data['pensionPenaltyOnExcessDistributions']);
        }
        // validate the optional field `refundableCredits`
        if (data['refundableCredits']) { // data not null
          Currency.validateJSON(data['refundableCredits']);
        }
        // validate the optional field `socialSecurityEmployer`
        if (data['socialSecurityEmployer']) { // data not null
          Currency.validateJSON(data['socialSecurityEmployer']);
        }
        // validate the optional field `socialSecuritySelfEmployed`
        if (data['socialSecuritySelfEmployed']) { // data not null
          Currency.validateJSON(data['socialSecuritySelfEmployed']);
        }
        // validate the optional field `stateIncome`
        if (data['stateIncome']) { // data not null
          Currency.validateJSON(data['stateIncome']);
        }
        // validate the optional field `total`
        if (data['total']) { // data not null
          Currency.validateJSON(data['total']);
        }

        return true;
    }


}



/**
 * @member {module:model/Currency} estate
 */
ITaxes.prototype['estate'] = undefined;

/**
 * @member {module:model/Currency} federalIncome
 */
ITaxes.prototype['federalIncome'] = undefined;

/**
 * @member {module:model/Currency} giftAndGenerationSkippingTransfer
 */
ITaxes.prototype['giftAndGenerationSkippingTransfer'] = undefined;

/**
 * @member {module:model/Currency} medicare
 */
ITaxes.prototype['medicare'] = undefined;

/**
 * @member {module:model/Currency} pensionEarlyDistributionPenalty
 */
ITaxes.prototype['pensionEarlyDistributionPenalty'] = undefined;

/**
 * @member {module:model/Currency} pensionPenaltyOnExcessDistributions
 */
ITaxes.prototype['pensionPenaltyOnExcessDistributions'] = undefined;

/**
 * @member {module:model/Currency} refundableCredits
 */
ITaxes.prototype['refundableCredits'] = undefined;

/**
 * @member {module:model/Currency} socialSecurityEmployer
 */
ITaxes.prototype['socialSecurityEmployer'] = undefined;

/**
 * @member {module:model/Currency} socialSecuritySelfEmployed
 */
ITaxes.prototype['socialSecuritySelfEmployed'] = undefined;

/**
 * @member {module:model/Currency} stateIncome
 */
ITaxes.prototype['stateIncome'] = undefined;

/**
 * @member {module:model/Currency} total
 */
ITaxes.prototype['total'] = undefined;






export default ITaxes;

