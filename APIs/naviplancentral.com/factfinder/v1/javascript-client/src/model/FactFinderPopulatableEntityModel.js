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

/**
 * The FactFinderPopulatableEntityModel model module.
 * @module model/FactFinderPopulatableEntityModel
 * @version v1
 */
class FactFinderPopulatableEntityModel {
    /**
     * Constructs a new <code>FactFinderPopulatableEntityModel</code>.
     * @alias module:model/FactFinderPopulatableEntityModel
     * @param householdId {Number} 
     */
    constructor(householdId) { 
        
        FactFinderPopulatableEntityModel.initialize(this, householdId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, householdId) { 
        obj['householdId'] = householdId;
    }

    /**
     * Constructs a <code>FactFinderPopulatableEntityModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FactFinderPopulatableEntityModel} obj Optional instance to populate.
     * @return {module:model/FactFinderPopulatableEntityModel} The populated <code>FactFinderPopulatableEntityModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FactFinderPopulatableEntityModel();

            if (data.hasOwnProperty('householdId')) {
                obj['householdId'] = ApiClient.convertToType(data['householdId'], 'Number');
            }
            if (data.hasOwnProperty('modules')) {
                obj['modules'] = ApiClient.convertToType(data['modules'], ['String']);
            }
            if (data.hasOwnProperty('planId')) {
                obj['planId'] = ApiClient.convertToType(data['planId'], 'Number');
            }
            if (data.hasOwnProperty('planLevel')) {
                obj['planLevel'] = ApiClient.convertToType(data['planLevel'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FactFinderPopulatableEntityModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FactFinderPopulatableEntityModel</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FactFinderPopulatableEntityModel.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['modules'])) {
            throw new Error("Expected the field `modules` to be an array in the JSON data but got " + data['modules']);
        }
        // ensure the json data is a string
        if (data['planLevel'] && !(typeof data['planLevel'] === 'string' || data['planLevel'] instanceof String)) {
            throw new Error("Expected the field `planLevel` to be a primitive type in the JSON string but got " + data['planLevel']);
        }

        return true;
    }


}

FactFinderPopulatableEntityModel.RequiredProperties = ["householdId"];

/**
 * @member {Number} householdId
 */
FactFinderPopulatableEntityModel.prototype['householdId'] = undefined;

/**
 * @member {Array.<module:model/FactFinderPopulatableEntityModel.ModulesEnum>} modules
 */
FactFinderPopulatableEntityModel.prototype['modules'] = undefined;

/**
 * @member {Number} planId
 */
FactFinderPopulatableEntityModel.prototype['planId'] = undefined;

/**
 * @member {module:model/FactFinderPopulatableEntityModel.PlanLevelEnum} planLevel
 */
FactFinderPopulatableEntityModel.prototype['planLevel'] = undefined;





/**
 * Allowed values for the <code>modules</code> property.
 * @enum {String}
 * @readonly
 */
FactFinderPopulatableEntityModel['ModulesEnum'] = {

    /**
     * value: "Demographics"
     * @const
     */
    "Demographics": "Demographics",

    /**
     * value: "Assets"
     * @const
     */
    "Assets": "Assets",

    /**
     * value: "Liabilities"
     * @const
     */
    "Liabilities": "Liabilities",

    /**
     * value: "Incomes"
     * @const
     */
    "Incomes": "Incomes",

    /**
     * value: "Expenses"
     * @const
     */
    "Expenses": "Expenses",

    /**
     * value: "Insurance"
     * @const
     */
    "Insurance": "Insurance",

    /**
     * value: "Retirement"
     * @const
     */
    "Retirement": "Retirement",

    /**
     * value: "Education"
     * @const
     */
    "Education": "Education",

    /**
     * value: "MajorPurchase"
     * @const
     */
    "MajorPurchase": "MajorPurchase"
};


/**
 * Allowed values for the <code>planLevel</code> property.
 * @enum {String}
 * @readonly
 */
FactFinderPopulatableEntityModel['PlanLevelEnum'] = {

    /**
     * value: "Level2"
     * @const
     */
    "Level2": "Level2",

    /**
     * value: "Level1"
     * @const
     */
    "Level1": "Level1"
};



export default FactFinderPopulatableEntityModel;

