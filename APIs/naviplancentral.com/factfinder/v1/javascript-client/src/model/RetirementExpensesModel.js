/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
import RetirementExpenseWithIdModel from './RetirementExpenseWithIdModel';

/**
 * The RetirementExpensesModel model module.
 * @module model/RetirementExpensesModel
 * @version v1
 */
class RetirementExpensesModel {
    /**
     * Constructs a new <code>RetirementExpensesModel</code>.
     * @alias module:model/RetirementExpensesModel
     */
    constructor() { 
        
        RetirementExpensesModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RetirementExpensesModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RetirementExpensesModel} obj Optional instance to populate.
     * @return {module:model/RetirementExpensesModel} The populated <code>RetirementExpensesModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RetirementExpensesModel();

            if (data.hasOwnProperty('retirementExpenses')) {
                obj['retirementExpenses'] = ApiClient.convertToType(data['retirementExpenses'], [RetirementExpenseWithIdModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RetirementExpensesModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RetirementExpensesModel</code>.
     */
    static validateJSON(data) {
        if (data['retirementExpenses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['retirementExpenses'])) {
                throw new Error("Expected the field `retirementExpenses` to be an array in the JSON data but got " + data['retirementExpenses']);
            }
            // validate the optional field `retirementExpenses` (array)
            for (const item of data['retirementExpenses']) {
                RetirementExpenseWithIdModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/RetirementExpenseWithIdModel>} retirementExpenses
 */
RetirementExpensesModel.prototype['retirementExpenses'] = undefined;






export default RetirementExpensesModel;

