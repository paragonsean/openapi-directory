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
import IBucketing from './IBucketing';
import IHeadAssumptions from './IHeadAssumptions';
import ModelDate from './ModelDate';
import Percent from './Percent';
import Year from './Year';

/**
 * The IAssumptions model module.
 * @module model/IAssumptions
 * @version v1
 */
class IAssumptions {
    /**
     * Constructs a new <code>IAssumptions</code>.
     * @alias module:model/IAssumptions
     */
    constructor() { 
        
        IAssumptions.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IAssumptions</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IAssumptions} obj Optional instance to populate.
     * @return {module:model/IAssumptions} The populated <code>IAssumptions</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IAssumptions();

            if (data.hasOwnProperty('anyHeadAlreadyRetired')) {
                obj['anyHeadAlreadyRetired'] = ApiClient.convertToType(data['anyHeadAlreadyRetired'], 'Boolean');
            }
            if (data.hasOwnProperty('bothRetired')) {
                obj['bothRetired'] = ApiClient.convertToType(data['bothRetired'], 'Boolean');
            }
            if (data.hasOwnProperty('bucketing')) {
                obj['bucketing'] = IBucketing.constructFromObject(data['bucketing']);
            }
            if (data.hasOwnProperty('client')) {
                obj['client'] = IHeadAssumptions.constructFromObject(data['client']);
            }
            if (data.hasOwnProperty('coClient')) {
                obj['coClient'] = IHeadAssumptions.constructFromObject(data['coClient']);
            }
            if (data.hasOwnProperty('firstToDieDate')) {
                obj['firstToDieDate'] = ModelDate.constructFromObject(data['firstToDieDate']);
            }
            if (data.hasOwnProperty('firstToDieMember')) {
                obj['firstToDieMember'] = ApiClient.convertToType(data['firstToDieMember'], 'String');
            }
            if (data.hasOwnProperty('firstToRetireDate')) {
                obj['firstToRetireDate'] = ModelDate.constructFromObject(data['firstToRetireDate']);
            }
            if (data.hasOwnProperty('inflationRate')) {
                obj['inflationRate'] = Percent.constructFromObject(data['inflationRate']);
            }
            if (data.hasOwnProperty('lastToDieDate')) {
                obj['lastToDieDate'] = ModelDate.constructFromObject(data['lastToDieDate']);
            }
            if (data.hasOwnProperty('lastToDieMember')) {
                obj['lastToDieMember'] = ApiClient.convertToType(data['lastToDieMember'], 'String');
            }
            if (data.hasOwnProperty('lastToRetireDate')) {
                obj['lastToRetireDate'] = ModelDate.constructFromObject(data['lastToRetireDate']);
            }
            if (data.hasOwnProperty('retirementYearAdjustedIfAlreadyRetired')) {
                obj['retirementYearAdjustedIfAlreadyRetired'] = Year.constructFromObject(data['retirementYearAdjustedIfAlreadyRetired']);
            }
            if (data.hasOwnProperty('splitSurplusSavingsStrategiesEnabled')) {
                obj['splitSurplusSavingsStrategiesEnabled'] = ApiClient.convertToType(data['splitSurplusSavingsStrategiesEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('taxMethod')) {
                obj['taxMethod'] = ApiClient.convertToType(data['taxMethod'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IAssumptions</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IAssumptions</code>.
     */
    static validateJSON(data) {
        // validate the optional field `bucketing`
        if (data['bucketing']) { // data not null
          IBucketing.validateJSON(data['bucketing']);
        }
        // validate the optional field `client`
        if (data['client']) { // data not null
          IHeadAssumptions.validateJSON(data['client']);
        }
        // validate the optional field `coClient`
        if (data['coClient']) { // data not null
          IHeadAssumptions.validateJSON(data['coClient']);
        }
        // validate the optional field `firstToDieDate`
        if (data['firstToDieDate']) { // data not null
          ModelDate.validateJSON(data['firstToDieDate']);
        }
        // ensure the json data is a string
        if (data['firstToDieMember'] && !(typeof data['firstToDieMember'] === 'string' || data['firstToDieMember'] instanceof String)) {
            throw new Error("Expected the field `firstToDieMember` to be a primitive type in the JSON string but got " + data['firstToDieMember']);
        }
        // validate the optional field `firstToRetireDate`
        if (data['firstToRetireDate']) { // data not null
          ModelDate.validateJSON(data['firstToRetireDate']);
        }
        // validate the optional field `inflationRate`
        if (data['inflationRate']) { // data not null
          Percent.validateJSON(data['inflationRate']);
        }
        // validate the optional field `lastToDieDate`
        if (data['lastToDieDate']) { // data not null
          ModelDate.validateJSON(data['lastToDieDate']);
        }
        // ensure the json data is a string
        if (data['lastToDieMember'] && !(typeof data['lastToDieMember'] === 'string' || data['lastToDieMember'] instanceof String)) {
            throw new Error("Expected the field `lastToDieMember` to be a primitive type in the JSON string but got " + data['lastToDieMember']);
        }
        // validate the optional field `lastToRetireDate`
        if (data['lastToRetireDate']) { // data not null
          ModelDate.validateJSON(data['lastToRetireDate']);
        }
        // validate the optional field `retirementYearAdjustedIfAlreadyRetired`
        if (data['retirementYearAdjustedIfAlreadyRetired']) { // data not null
          Year.validateJSON(data['retirementYearAdjustedIfAlreadyRetired']);
        }
        // ensure the json data is a string
        if (data['taxMethod'] && !(typeof data['taxMethod'] === 'string' || data['taxMethod'] instanceof String)) {
            throw new Error("Expected the field `taxMethod` to be a primitive type in the JSON string but got " + data['taxMethod']);
        }

        return true;
    }


}



/**
 * @member {Boolean} anyHeadAlreadyRetired
 */
IAssumptions.prototype['anyHeadAlreadyRetired'] = undefined;

/**
 * @member {Boolean} bothRetired
 */
IAssumptions.prototype['bothRetired'] = undefined;

/**
 * @member {module:model/IBucketing} bucketing
 */
IAssumptions.prototype['bucketing'] = undefined;

/**
 * @member {module:model/IHeadAssumptions} client
 */
IAssumptions.prototype['client'] = undefined;

/**
 * @member {module:model/IHeadAssumptions} coClient
 */
IAssumptions.prototype['coClient'] = undefined;

/**
 * @member {module:model/ModelDate} firstToDieDate
 */
IAssumptions.prototype['firstToDieDate'] = undefined;

/**
 * @member {module:model/IAssumptions.FirstToDieMemberEnum} firstToDieMember
 */
IAssumptions.prototype['firstToDieMember'] = undefined;

/**
 * @member {module:model/ModelDate} firstToRetireDate
 */
IAssumptions.prototype['firstToRetireDate'] = undefined;

/**
 * @member {module:model/Percent} inflationRate
 */
IAssumptions.prototype['inflationRate'] = undefined;

/**
 * @member {module:model/ModelDate} lastToDieDate
 */
IAssumptions.prototype['lastToDieDate'] = undefined;

/**
 * @member {module:model/IAssumptions.LastToDieMemberEnum} lastToDieMember
 */
IAssumptions.prototype['lastToDieMember'] = undefined;

/**
 * @member {module:model/ModelDate} lastToRetireDate
 */
IAssumptions.prototype['lastToRetireDate'] = undefined;

/**
 * @member {module:model/Year} retirementYearAdjustedIfAlreadyRetired
 */
IAssumptions.prototype['retirementYearAdjustedIfAlreadyRetired'] = undefined;

/**
 * @member {Boolean} splitSurplusSavingsStrategiesEnabled
 */
IAssumptions.prototype['splitSurplusSavingsStrategiesEnabled'] = undefined;

/**
 * @member {module:model/IAssumptions.TaxMethodEnum} taxMethod
 */
IAssumptions.prototype['taxMethod'] = undefined;





/**
 * Allowed values for the <code>firstToDieMember</code> property.
 * @enum {String}
 * @readonly
 */
IAssumptions['FirstToDieMemberEnum'] = {

    /**
     * value: "Client"
     * @const
     */
    "Client": "Client",

    /**
     * value: "CoClient"
     * @const
     */
    "CoClient": "CoClient"
};


/**
 * Allowed values for the <code>lastToDieMember</code> property.
 * @enum {String}
 * @readonly
 */
IAssumptions['LastToDieMemberEnum'] = {

    /**
     * value: "Client"
     * @const
     */
    "Client": "Client",

    /**
     * value: "CoClient"
     * @const
     */
    "CoClient": "CoClient"
};


/**
 * Allowed values for the <code>taxMethod</code> property.
 * @enum {String}
 * @readonly
 */
IAssumptions['TaxMethodEnum'] = {

    /**
     * value: "Average"
     * @const
     */
    "Average": "Average",

    /**
     * value: "Simplified"
     * @const
     */
    "Simplified": "Simplified",

    /**
     * value: "Detailed"
     * @const
     */
    "Detailed": "Detailed"
};



export default IAssumptions;

