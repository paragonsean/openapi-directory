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
import LifeInsurancePolicySubaccountWithIdModel from './LifeInsurancePolicySubaccountWithIdModel';
import ObjectLink from './ObjectLink';

/**
 * The LifeInsurancePolicyWithSubEntitiesModel model module.
 * @module model/LifeInsurancePolicyWithSubEntitiesModel
 * @version v1
 */
class LifeInsurancePolicyWithSubEntitiesModel {
    /**
     * Constructs a new <code>LifeInsurancePolicyWithSubEntitiesModel</code>.
     * @alias module:model/LifeInsurancePolicyWithSubEntitiesModel
     */
    constructor() { 
        
        LifeInsurancePolicyWithSubEntitiesModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LifeInsurancePolicyWithSubEntitiesModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LifeInsurancePolicyWithSubEntitiesModel} obj Optional instance to populate.
     * @return {module:model/LifeInsurancePolicyWithSubEntitiesModel} The populated <code>LifeInsurancePolicyWithSubEntitiesModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LifeInsurancePolicyWithSubEntitiesModel();

            if (data.hasOwnProperty('beneficiary')) {
                obj['beneficiary'] = ApiClient.convertToType(data['beneficiary'], 'String');
            }
            if (data.hasOwnProperty('beneficiaryDependentId')) {
                obj['beneficiaryDependentId'] = ApiClient.convertToType(data['beneficiaryDependentId'], 'Number');
            }
            if (data.hasOwnProperty('benefit')) {
                obj['benefit'] = ApiClient.convertToType(data['benefit'], 'Number');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('externalDestinationId')) {
                obj['externalDestinationId'] = ApiClient.convertToType(data['externalDestinationId'], 'String');
            }
            if (data.hasOwnProperty('factFinderId')) {
                obj['factFinderId'] = ApiClient.convertToType(data['factFinderId'], 'Number');
            }
            if (data.hasOwnProperty('frequency')) {
                obj['frequency'] = ApiClient.convertToType(data['frequency'], 'Number');
            }
            if (data.hasOwnProperty('generalAccountMarketValue')) {
                obj['generalAccountMarketValue'] = ApiClient.convertToType(data['generalAccountMarketValue'], 'Number');
            }
            if (data.hasOwnProperty('insurancePolicyId')) {
                obj['insurancePolicyId'] = ApiClient.convertToType(data['insurancePolicyId'], 'Number');
            }
            if (data.hasOwnProperty('insured')) {
                obj['insured'] = ApiClient.convertToType(data['insured'], 'String');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = ApiClient.convertToType(data['links'], [ObjectLink]);
            }
            if (data.hasOwnProperty('payer')) {
                obj['payer'] = ApiClient.convertToType(data['payer'], 'String');
            }
            if (data.hasOwnProperty('policyType')) {
                obj['policyType'] = ApiClient.convertToType(data['policyType'], 'Number');
            }
            if (data.hasOwnProperty('premium')) {
                obj['premium'] = ApiClient.convertToType(data['premium'], 'Number');
            }
            if (data.hasOwnProperty('subaccounts')) {
                obj['subaccounts'] = ApiClient.convertToType(data['subaccounts'], [LifeInsurancePolicySubaccountWithIdModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LifeInsurancePolicyWithSubEntitiesModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LifeInsurancePolicyWithSubEntitiesModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['beneficiary'] && !(typeof data['beneficiary'] === 'string' || data['beneficiary'] instanceof String)) {
            throw new Error("Expected the field `beneficiary` to be a primitive type in the JSON string but got " + data['beneficiary']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['externalDestinationId'] && !(typeof data['externalDestinationId'] === 'string' || data['externalDestinationId'] instanceof String)) {
            throw new Error("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got " + data['externalDestinationId']);
        }
        // ensure the json data is a string
        if (data['insured'] && !(typeof data['insured'] === 'string' || data['insured'] instanceof String)) {
            throw new Error("Expected the field `insured` to be a primitive type in the JSON string but got " + data['insured']);
        }
        if (data['links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['links'])) {
                throw new Error("Expected the field `links` to be an array in the JSON data but got " + data['links']);
            }
            // validate the optional field `links` (array)
            for (const item of data['links']) {
                ObjectLink.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['payer'] && !(typeof data['payer'] === 'string' || data['payer'] instanceof String)) {
            throw new Error("Expected the field `payer` to be a primitive type in the JSON string but got " + data['payer']);
        }
        if (data['subaccounts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['subaccounts'])) {
                throw new Error("Expected the field `subaccounts` to be an array in the JSON data but got " + data['subaccounts']);
            }
            // validate the optional field `subaccounts` (array)
            for (const item of data['subaccounts']) {
                LifeInsurancePolicySubaccountWithIdModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/LifeInsurancePolicyWithSubEntitiesModel.BeneficiaryEnum} beneficiary
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['beneficiary'] = undefined;

/**
 * @member {Number} beneficiaryDependentId
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['beneficiaryDependentId'] = undefined;

/**
 * @member {Number} benefit
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['benefit'] = undefined;

/**
 * @member {String} description
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['description'] = undefined;

/**
 * @member {String} externalDestinationId
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['externalDestinationId'] = undefined;

/**
 * @member {Number} factFinderId
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['factFinderId'] = undefined;

/**
 * @member {Number} frequency
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['frequency'] = undefined;

/**
 * @member {Number} generalAccountMarketValue
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['generalAccountMarketValue'] = undefined;

/**
 * @member {Number} insurancePolicyId
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['insurancePolicyId'] = undefined;

/**
 * @member {module:model/LifeInsurancePolicyWithSubEntitiesModel.InsuredEnum} insured
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['insured'] = undefined;

/**
 * @member {Array.<module:model/ObjectLink>} links
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['links'] = undefined;

/**
 * @member {module:model/LifeInsurancePolicyWithSubEntitiesModel.PayerEnum} payer
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['payer'] = undefined;

/**
 * @member {Number} policyType
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['policyType'] = undefined;

/**
 * @member {Number} premium
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['premium'] = undefined;

/**
 * @member {Array.<module:model/LifeInsurancePolicySubaccountWithIdModel>} subaccounts
 */
LifeInsurancePolicyWithSubEntitiesModel.prototype['subaccounts'] = undefined;





/**
 * Allowed values for the <code>beneficiary</code> property.
 * @enum {String}
 * @readonly
 */
LifeInsurancePolicyWithSubEntitiesModel['BeneficiaryEnum'] = {

    /**
     * value: "Client"
     * @const
     */
    "Client": "Client",

    /**
     * value: "CoClient"
     * @const
     */
    "CoClient": "CoClient",

    /**
     * value: "Dependent"
     * @const
     */
    "Dependent": "Dependent",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other"
};


/**
 * Allowed values for the <code>insured</code> property.
 * @enum {String}
 * @readonly
 */
LifeInsurancePolicyWithSubEntitiesModel['InsuredEnum'] = {

    /**
     * value: "Client"
     * @const
     */
    "Client": "Client",

    /**
     * value: "CoClient"
     * @const
     */
    "CoClient": "CoClient",

    /**
     * value: "FirstToDie"
     * @const
     */
    "FirstToDie": "FirstToDie",

    /**
     * value: "SecondToDie"
     * @const
     */
    "SecondToDie": "SecondToDie",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other"
};


/**
 * Allowed values for the <code>payer</code> property.
 * @enum {String}
 * @readonly
 */
LifeInsurancePolicyWithSubEntitiesModel['PayerEnum'] = {

    /**
     * value: "Client"
     * @const
     */
    "Client": "Client",

    /**
     * value: "CoClient"
     * @const
     */
    "CoClient": "CoClient",

    /**
     * value: "Joint"
     * @const
     */
    "Joint": "Joint",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other"
};



export default LifeInsurancePolicyWithSubEntitiesModel;

