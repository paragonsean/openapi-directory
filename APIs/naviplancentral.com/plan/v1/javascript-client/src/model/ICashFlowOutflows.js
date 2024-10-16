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
import ICashFlowCategory from './ICashFlowCategory';

/**
 * The ICashFlowOutflows model module.
 * @module model/ICashFlowOutflows
 * @version v1
 */
class ICashFlowOutflows {
    /**
     * Constructs a new <code>ICashFlowOutflows</code>.
     * @alias module:model/ICashFlowOutflows
     */
    constructor() { 
        
        ICashFlowOutflows.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ICashFlowOutflows</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ICashFlowOutflows} obj Optional instance to populate.
     * @return {module:model/ICashFlowOutflows} The populated <code>ICashFlowOutflows</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ICashFlowOutflows();

            if (data.hasOwnProperty('contributions')) {
                obj['contributions'] = Currency.constructFromObject(data['contributions']);
            }
            if (data.hasOwnProperty('educationExpenses')) {
                obj['educationExpenses'] = ICashFlowCategory.constructFromObject(data['educationExpenses']);
            }
            if (data.hasOwnProperty('employerExpenses')) {
                obj['employerExpenses'] = ICashFlowCategory.constructFromObject(data['employerExpenses']);
            }
            if (data.hasOwnProperty('employmentBusinessExpenses')) {
                obj['employmentBusinessExpenses'] = ICashFlowCategory.constructFromObject(data['employmentBusinessExpenses']);
            }
            if (data.hasOwnProperty('investmentExpenses')) {
                obj['investmentExpenses'] = ICashFlowCategory.constructFromObject(data['investmentExpenses']);
            }
            if (data.hasOwnProperty('lifestyleExpenses')) {
                obj['lifestyleExpenses'] = ICashFlowCategory.constructFromObject(data['lifestyleExpenses']);
            }
            if (data.hasOwnProperty('lifestyleExpensesDiscretionary')) {
                obj['lifestyleExpensesDiscretionary'] = ICashFlowCategory.constructFromObject(data['lifestyleExpensesDiscretionary']);
            }
            if (data.hasOwnProperty('lifestyleExpensesFixed')) {
                obj['lifestyleExpensesFixed'] = ICashFlowCategory.constructFromObject(data['lifestyleExpensesFixed']);
            }
            if (data.hasOwnProperty('lockedInContributions')) {
                obj['lockedInContributions'] = Currency.constructFromObject(data['lockedInContributions']);
            }
            if (data.hasOwnProperty('medicalExpenses')) {
                obj['medicalExpenses'] = ICashFlowCategory.constructFromObject(data['medicalExpenses']);
            }
            if (data.hasOwnProperty('miscellaneousExpenses')) {
                obj['miscellaneousExpenses'] = ICashFlowCategory.constructFromObject(data['miscellaneousExpenses']);
            }
            if (data.hasOwnProperty('miscellaneousExpensesDiscretionary')) {
                obj['miscellaneousExpensesDiscretionary'] = ICashFlowCategory.constructFromObject(data['miscellaneousExpensesDiscretionary']);
            }
            if (data.hasOwnProperty('miscellaneousExpensesFixed')) {
                obj['miscellaneousExpensesFixed'] = ICashFlowCategory.constructFromObject(data['miscellaneousExpensesFixed']);
            }
            if (data.hasOwnProperty('nonQualifiedContributions')) {
                obj['nonQualifiedContributions'] = ICashFlowCategory.constructFromObject(data['nonQualifiedContributions']);
            }
            if (data.hasOwnProperty('nonQualifiedReinvestments')) {
                obj['nonQualifiedReinvestments'] = ICashFlowCategory.constructFromObject(data['nonQualifiedReinvestments']);
            }
            if (data.hasOwnProperty('privateCorporationOutflows')) {
                obj['privateCorporationOutflows'] = ICashFlowCategory.constructFromObject(data['privateCorporationOutflows']);
            }
            if (data.hasOwnProperty('qualifiedContributions')) {
                obj['qualifiedContributions'] = ICashFlowCategory.constructFromObject(data['qualifiedContributions']);
            }
            if (data.hasOwnProperty('rothContributions')) {
                obj['rothContributions'] = Currency.constructFromObject(data['rothContributions']);
            }
            if (data.hasOwnProperty('surplusOutflows')) {
                obj['surplusOutflows'] = ICashFlowCategory.constructFromObject(data['surplusOutflows']);
            }
            if (data.hasOwnProperty('surplusSavings')) {
                obj['surplusSavings'] = Currency.constructFromObject(data['surplusSavings']);
            }
            if (data.hasOwnProperty('tfsaContributions')) {
                obj['tfsaContributions'] = Currency.constructFromObject(data['tfsaContributions']);
            }
            if (data.hasOwnProperty('totalNeeds')) {
                obj['totalNeeds'] = Currency.constructFromObject(data['totalNeeds']);
            }
            if (data.hasOwnProperty('totalWithTaxes')) {
                obj['totalWithTaxes'] = Currency.constructFromObject(data['totalWithTaxes']);
            }
            if (data.hasOwnProperty('totalWithoutTaxes')) {
                obj['totalWithoutTaxes'] = Currency.constructFromObject(data['totalWithoutTaxes']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ICashFlowOutflows</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ICashFlowOutflows</code>.
     */
    static validateJSON(data) {
        // validate the optional field `contributions`
        if (data['contributions']) { // data not null
          Currency.validateJSON(data['contributions']);
        }
        // validate the optional field `educationExpenses`
        if (data['educationExpenses']) { // data not null
          ICashFlowCategory.validateJSON(data['educationExpenses']);
        }
        // validate the optional field `employerExpenses`
        if (data['employerExpenses']) { // data not null
          ICashFlowCategory.validateJSON(data['employerExpenses']);
        }
        // validate the optional field `employmentBusinessExpenses`
        if (data['employmentBusinessExpenses']) { // data not null
          ICashFlowCategory.validateJSON(data['employmentBusinessExpenses']);
        }
        // validate the optional field `investmentExpenses`
        if (data['investmentExpenses']) { // data not null
          ICashFlowCategory.validateJSON(data['investmentExpenses']);
        }
        // validate the optional field `lifestyleExpenses`
        if (data['lifestyleExpenses']) { // data not null
          ICashFlowCategory.validateJSON(data['lifestyleExpenses']);
        }
        // validate the optional field `lifestyleExpensesDiscretionary`
        if (data['lifestyleExpensesDiscretionary']) { // data not null
          ICashFlowCategory.validateJSON(data['lifestyleExpensesDiscretionary']);
        }
        // validate the optional field `lifestyleExpensesFixed`
        if (data['lifestyleExpensesFixed']) { // data not null
          ICashFlowCategory.validateJSON(data['lifestyleExpensesFixed']);
        }
        // validate the optional field `lockedInContributions`
        if (data['lockedInContributions']) { // data not null
          Currency.validateJSON(data['lockedInContributions']);
        }
        // validate the optional field `medicalExpenses`
        if (data['medicalExpenses']) { // data not null
          ICashFlowCategory.validateJSON(data['medicalExpenses']);
        }
        // validate the optional field `miscellaneousExpenses`
        if (data['miscellaneousExpenses']) { // data not null
          ICashFlowCategory.validateJSON(data['miscellaneousExpenses']);
        }
        // validate the optional field `miscellaneousExpensesDiscretionary`
        if (data['miscellaneousExpensesDiscretionary']) { // data not null
          ICashFlowCategory.validateJSON(data['miscellaneousExpensesDiscretionary']);
        }
        // validate the optional field `miscellaneousExpensesFixed`
        if (data['miscellaneousExpensesFixed']) { // data not null
          ICashFlowCategory.validateJSON(data['miscellaneousExpensesFixed']);
        }
        // validate the optional field `nonQualifiedContributions`
        if (data['nonQualifiedContributions']) { // data not null
          ICashFlowCategory.validateJSON(data['nonQualifiedContributions']);
        }
        // validate the optional field `nonQualifiedReinvestments`
        if (data['nonQualifiedReinvestments']) { // data not null
          ICashFlowCategory.validateJSON(data['nonQualifiedReinvestments']);
        }
        // validate the optional field `privateCorporationOutflows`
        if (data['privateCorporationOutflows']) { // data not null
          ICashFlowCategory.validateJSON(data['privateCorporationOutflows']);
        }
        // validate the optional field `qualifiedContributions`
        if (data['qualifiedContributions']) { // data not null
          ICashFlowCategory.validateJSON(data['qualifiedContributions']);
        }
        // validate the optional field `rothContributions`
        if (data['rothContributions']) { // data not null
          Currency.validateJSON(data['rothContributions']);
        }
        // validate the optional field `surplusOutflows`
        if (data['surplusOutflows']) { // data not null
          ICashFlowCategory.validateJSON(data['surplusOutflows']);
        }
        // validate the optional field `surplusSavings`
        if (data['surplusSavings']) { // data not null
          Currency.validateJSON(data['surplusSavings']);
        }
        // validate the optional field `tfsaContributions`
        if (data['tfsaContributions']) { // data not null
          Currency.validateJSON(data['tfsaContributions']);
        }
        // validate the optional field `totalNeeds`
        if (data['totalNeeds']) { // data not null
          Currency.validateJSON(data['totalNeeds']);
        }
        // validate the optional field `totalWithTaxes`
        if (data['totalWithTaxes']) { // data not null
          Currency.validateJSON(data['totalWithTaxes']);
        }
        // validate the optional field `totalWithoutTaxes`
        if (data['totalWithoutTaxes']) { // data not null
          Currency.validateJSON(data['totalWithoutTaxes']);
        }

        return true;
    }


}



/**
 * @member {module:model/Currency} contributions
 */
ICashFlowOutflows.prototype['contributions'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} educationExpenses
 */
ICashFlowOutflows.prototype['educationExpenses'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} employerExpenses
 */
ICashFlowOutflows.prototype['employerExpenses'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} employmentBusinessExpenses
 */
ICashFlowOutflows.prototype['employmentBusinessExpenses'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} investmentExpenses
 */
ICashFlowOutflows.prototype['investmentExpenses'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} lifestyleExpenses
 */
ICashFlowOutflows.prototype['lifestyleExpenses'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} lifestyleExpensesDiscretionary
 */
ICashFlowOutflows.prototype['lifestyleExpensesDiscretionary'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} lifestyleExpensesFixed
 */
ICashFlowOutflows.prototype['lifestyleExpensesFixed'] = undefined;

/**
 * @member {module:model/Currency} lockedInContributions
 */
ICashFlowOutflows.prototype['lockedInContributions'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} medicalExpenses
 */
ICashFlowOutflows.prototype['medicalExpenses'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} miscellaneousExpenses
 */
ICashFlowOutflows.prototype['miscellaneousExpenses'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} miscellaneousExpensesDiscretionary
 */
ICashFlowOutflows.prototype['miscellaneousExpensesDiscretionary'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} miscellaneousExpensesFixed
 */
ICashFlowOutflows.prototype['miscellaneousExpensesFixed'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} nonQualifiedContributions
 */
ICashFlowOutflows.prototype['nonQualifiedContributions'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} nonQualifiedReinvestments
 */
ICashFlowOutflows.prototype['nonQualifiedReinvestments'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} privateCorporationOutflows
 */
ICashFlowOutflows.prototype['privateCorporationOutflows'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} qualifiedContributions
 */
ICashFlowOutflows.prototype['qualifiedContributions'] = undefined;

/**
 * @member {module:model/Currency} rothContributions
 */
ICashFlowOutflows.prototype['rothContributions'] = undefined;

/**
 * @member {module:model/ICashFlowCategory} surplusOutflows
 */
ICashFlowOutflows.prototype['surplusOutflows'] = undefined;

/**
 * @member {module:model/Currency} surplusSavings
 */
ICashFlowOutflows.prototype['surplusSavings'] = undefined;

/**
 * @member {module:model/Currency} tfsaContributions
 */
ICashFlowOutflows.prototype['tfsaContributions'] = undefined;

/**
 * @member {module:model/Currency} totalNeeds
 */
ICashFlowOutflows.prototype['totalNeeds'] = undefined;

/**
 * @member {module:model/Currency} totalWithTaxes
 */
ICashFlowOutflows.prototype['totalWithTaxes'] = undefined;

/**
 * @member {module:model/Currency} totalWithoutTaxes
 */
ICashFlowOutflows.prototype['totalWithoutTaxes'] = undefined;






export default ICashFlowOutflows;

