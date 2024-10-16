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
import CurrencyWithDate from './CurrencyWithDate';
import FormattedLifestyleType from './FormattedLifestyleType';
import ModelDate from './ModelDate';
import Percent from './Percent';

/**
 * The ILifestyleAsset model module.
 * @module model/ILifestyleAsset
 * @version v1
 */
class ILifestyleAsset {
    /**
     * Constructs a new <code>ILifestyleAsset</code>.
     * @alias module:model/ILifestyleAsset
     */
    constructor() { 
        
        ILifestyleAsset.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ILifestyleAsset</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ILifestyleAsset} obj Optional instance to populate.
     * @return {module:model/ILifestyleAsset} The populated <code>ILifestyleAsset</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ILifestyleAsset();

            if (data.hasOwnProperty('afterTaxProceedsAccountName')) {
                obj['afterTaxProceedsAccountName'] = ApiClient.convertToType(data['afterTaxProceedsAccountName'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('futureValueProjectedGrossSaleValue')) {
                obj['futureValueProjectedGrossSaleValue'] = Currency.constructFromObject(data['futureValueProjectedGrossSaleValue']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('isMajorPurchaseGoal')) {
                obj['isMajorPurchaseGoal'] = ApiClient.convertToType(data['isMajorPurchaseGoal'], 'Boolean');
            }
            if (data.hasOwnProperty('marketValueAsOf')) {
                obj['marketValueAsOf'] = CurrencyWithDate.constructFromObject(data['marketValueAsOf']);
            }
            if (data.hasOwnProperty('owner')) {
                obj['owner'] = ApiClient.convertToType(data['owner'], 'String');
            }
            if (data.hasOwnProperty('preTaxGrowthRate')) {
                obj['preTaxGrowthRate'] = Percent.constructFromObject(data['preTaxGrowthRate']);
            }
            if (data.hasOwnProperty('presentValueProjectedGrossSaleValue')) {
                obj['presentValueProjectedGrossSaleValue'] = Currency.constructFromObject(data['presentValueProjectedGrossSaleValue']);
            }
            if (data.hasOwnProperty('projectedSaleDate')) {
                obj['projectedSaleDate'] = ModelDate.constructFromObject(data['projectedSaleDate']);
            }
            if (data.hasOwnProperty('purchaseAmount')) {
                obj['purchaseAmount'] = Currency.constructFromObject(data['purchaseAmount']);
            }
            if (data.hasOwnProperty('purchaseDate')) {
                obj['purchaseDate'] = ModelDate.constructFromObject(data['purchaseDate']);
            }
            if (data.hasOwnProperty('sellingCostPercent')) {
                obj['sellingCostPercent'] = Percent.constructFromObject(data['sellingCostPercent']);
            }
            if (data.hasOwnProperty('standardDeviation')) {
                obj['standardDeviation'] = Percent.constructFromObject(data['standardDeviation']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = FormattedLifestyleType.constructFromObject(data['type']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ILifestyleAsset</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ILifestyleAsset</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['afterTaxProceedsAccountName'] && !(typeof data['afterTaxProceedsAccountName'] === 'string' || data['afterTaxProceedsAccountName'] instanceof String)) {
            throw new Error("Expected the field `afterTaxProceedsAccountName` to be a primitive type in the JSON string but got " + data['afterTaxProceedsAccountName']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // validate the optional field `futureValueProjectedGrossSaleValue`
        if (data['futureValueProjectedGrossSaleValue']) { // data not null
          Currency.validateJSON(data['futureValueProjectedGrossSaleValue']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `marketValueAsOf`
        if (data['marketValueAsOf']) { // data not null
          CurrencyWithDate.validateJSON(data['marketValueAsOf']);
        }
        // ensure the json data is a string
        if (data['owner'] && !(typeof data['owner'] === 'string' || data['owner'] instanceof String)) {
            throw new Error("Expected the field `owner` to be a primitive type in the JSON string but got " + data['owner']);
        }
        // validate the optional field `preTaxGrowthRate`
        if (data['preTaxGrowthRate']) { // data not null
          Percent.validateJSON(data['preTaxGrowthRate']);
        }
        // validate the optional field `presentValueProjectedGrossSaleValue`
        if (data['presentValueProjectedGrossSaleValue']) { // data not null
          Currency.validateJSON(data['presentValueProjectedGrossSaleValue']);
        }
        // validate the optional field `projectedSaleDate`
        if (data['projectedSaleDate']) { // data not null
          ModelDate.validateJSON(data['projectedSaleDate']);
        }
        // validate the optional field `purchaseAmount`
        if (data['purchaseAmount']) { // data not null
          Currency.validateJSON(data['purchaseAmount']);
        }
        // validate the optional field `purchaseDate`
        if (data['purchaseDate']) { // data not null
          ModelDate.validateJSON(data['purchaseDate']);
        }
        // validate the optional field `sellingCostPercent`
        if (data['sellingCostPercent']) { // data not null
          Percent.validateJSON(data['sellingCostPercent']);
        }
        // validate the optional field `standardDeviation`
        if (data['standardDeviation']) { // data not null
          Percent.validateJSON(data['standardDeviation']);
        }
        // validate the optional field `type`
        if (data['type']) { // data not null
          FormattedLifestyleType.validateJSON(data['type']);
        }

        return true;
    }


}



/**
 * @member {String} afterTaxProceedsAccountName
 */
ILifestyleAsset.prototype['afterTaxProceedsAccountName'] = undefined;

/**
 * @member {String} description
 */
ILifestyleAsset.prototype['description'] = undefined;

/**
 * @member {module:model/Currency} futureValueProjectedGrossSaleValue
 */
ILifestyleAsset.prototype['futureValueProjectedGrossSaleValue'] = undefined;

/**
 * @member {String} id
 */
ILifestyleAsset.prototype['id'] = undefined;

/**
 * @member {Boolean} isMajorPurchaseGoal
 */
ILifestyleAsset.prototype['isMajorPurchaseGoal'] = undefined;

/**
 * @member {module:model/CurrencyWithDate} marketValueAsOf
 */
ILifestyleAsset.prototype['marketValueAsOf'] = undefined;

/**
 * @member {module:model/ILifestyleAsset.OwnerEnum} owner
 */
ILifestyleAsset.prototype['owner'] = undefined;

/**
 * @member {module:model/Percent} preTaxGrowthRate
 */
ILifestyleAsset.prototype['preTaxGrowthRate'] = undefined;

/**
 * @member {module:model/Currency} presentValueProjectedGrossSaleValue
 */
ILifestyleAsset.prototype['presentValueProjectedGrossSaleValue'] = undefined;

/**
 * @member {module:model/ModelDate} projectedSaleDate
 */
ILifestyleAsset.prototype['projectedSaleDate'] = undefined;

/**
 * @member {module:model/Currency} purchaseAmount
 */
ILifestyleAsset.prototype['purchaseAmount'] = undefined;

/**
 * @member {module:model/ModelDate} purchaseDate
 */
ILifestyleAsset.prototype['purchaseDate'] = undefined;

/**
 * @member {module:model/Percent} sellingCostPercent
 */
ILifestyleAsset.prototype['sellingCostPercent'] = undefined;

/**
 * @member {module:model/Percent} standardDeviation
 */
ILifestyleAsset.prototype['standardDeviation'] = undefined;

/**
 * @member {module:model/FormattedLifestyleType} type
 */
ILifestyleAsset.prototype['type'] = undefined;





/**
 * Allowed values for the <code>owner</code> property.
 * @enum {String}
 * @readonly
 */
ILifestyleAsset['OwnerEnum'] = {

    /**
     * value: "All"
     * @const
     */
    "All": "All",

    /**
     * value: "Head1"
     * @const
     */
    "Head1": "Head1",

    /**
     * value: "Head2"
     * @const
     */
    "Head2": "Head2",

    /**
     * value: "NonHead1"
     * @const
     */
    "NonHead1": "NonHead1",

    /**
     * value: "NonHead2"
     * @const
     */
    "NonHead2": "NonHead2",

    /**
     * value: "NonHead3"
     * @const
     */
    "NonHead3": "NonHead3",

    /**
     * value: "NonHead4"
     * @const
     */
    "NonHead4": "NonHead4",

    /**
     * value: "NonHead5"
     * @const
     */
    "NonHead5": "NonHead5",

    /**
     * value: "NonHead6"
     * @const
     */
    "NonHead6": "NonHead6",

    /**
     * value: "NonHead7"
     * @const
     */
    "NonHead7": "NonHead7",

    /**
     * value: "NonHead8"
     * @const
     */
    "NonHead8": "NonHead8",

    /**
     * value: "NonHead9"
     * @const
     */
    "NonHead9": "NonHead9",

    /**
     * value: "CommunityProperty"
     * @const
     */
    "CommunityProperty": "CommunityProperty",

    /**
     * value: "Joint"
     * @const
     */
    "Joint": "Joint",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other",

    /**
     * value: "AllDependents"
     * @const
     */
    "AllDependents": "AllDependents",

    /**
     * value: "AllFamilyMembers"
     * @const
     */
    "AllFamilyMembers": "AllFamilyMembers",

    /**
     * value: "Corporation"
     * @const
     */
    "Corporation": "Corporation"
};



export default ILifestyleAsset;

