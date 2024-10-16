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

/**
 * The AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments model module.
 * @module model/AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments
 * @version v1
 */
class AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments {
    /**
     * Constructs a new <code>AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments</code>.
     * @alias module:model/AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments
     */
    constructor() { 
        
        AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments} obj Optional instance to populate.
     * @return {module:model/AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments} The populated <code>AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments();

            if (data.hasOwnProperty('clientRetirementAge')) {
                obj['clientRetirementAge'] = ApiClient.convertToType(data['clientRetirementAge'], 'Number');
            }
            if (data.hasOwnProperty('coClientRetirementAge')) {
                obj['coClientRetirementAge'] = ApiClient.convertToType(data['coClientRetirementAge'], 'Number');
            }
            if (data.hasOwnProperty('discretionaryExpenseCoverage')) {
                obj['discretionaryExpenseCoverage'] = ApiClient.convertToType(data['discretionaryExpenseCoverage'], 'Number');
            }
            if (data.hasOwnProperty('fixedExpenseCoverage')) {
                obj['fixedExpenseCoverage'] = ApiClient.convertToType(data['fixedExpenseCoverage'], 'Number');
            }
            if (data.hasOwnProperty('lumpSumContribution')) {
                obj['lumpSumContribution'] = ApiClient.convertToType(data['lumpSumContribution'], 'Number');
            }
            if (data.hasOwnProperty('lumpSumDate')) {
                obj['lumpSumDate'] = ApiClient.convertToType(data['lumpSumDate'], 'Date');
            }
            if (data.hasOwnProperty('monthlySavingsContribution')) {
                obj['monthlySavingsContribution'] = ApiClient.convertToType(data['monthlySavingsContribution'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Number} clientRetirementAge
 */
AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.prototype['clientRetirementAge'] = undefined;

/**
 * @member {Number} coClientRetirementAge
 */
AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.prototype['coClientRetirementAge'] = undefined;

/**
 * @member {Number} discretionaryExpenseCoverage
 */
AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.prototype['discretionaryExpenseCoverage'] = undefined;

/**
 * @member {Number} fixedExpenseCoverage
 */
AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.prototype['fixedExpenseCoverage'] = undefined;

/**
 * @member {Number} lumpSumContribution
 */
AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.prototype['lumpSumContribution'] = undefined;

/**
 * @member {Date} lumpSumDate
 */
AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.prototype['lumpSumDate'] = undefined;

/**
 * @member {Number} monthlySavingsContribution
 */
AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.prototype['monthlySavingsContribution'] = undefined;






export default AdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments;

