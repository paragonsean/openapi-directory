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
import ObjectLink from './ObjectLink';

/**
 * The DisabilityInsurancePolicyWithIdModel model module.
 * @module model/DisabilityInsurancePolicyWithIdModel
 * @version v1
 */
class DisabilityInsurancePolicyWithIdModel {
    /**
     * Constructs a new <code>DisabilityInsurancePolicyWithIdModel</code>.
     * @alias module:model/DisabilityInsurancePolicyWithIdModel
     */
    constructor() { 
        
        DisabilityInsurancePolicyWithIdModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DisabilityInsurancePolicyWithIdModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DisabilityInsurancePolicyWithIdModel} obj Optional instance to populate.
     * @return {module:model/DisabilityInsurancePolicyWithIdModel} The populated <code>DisabilityInsurancePolicyWithIdModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DisabilityInsurancePolicyWithIdModel();

            if (data.hasOwnProperty('benefit')) {
                obj['benefit'] = ApiClient.convertToType(data['benefit'], 'Number');
            }
            if (data.hasOwnProperty('benefitFrequency')) {
                obj['benefitFrequency'] = ApiClient.convertToType(data['benefitFrequency'], 'Number');
            }
            if (data.hasOwnProperty('benefitType')) {
                obj['benefitType'] = ApiClient.convertToType(data['benefitType'], 'String');
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
            if (data.hasOwnProperty('insurancePolicyId')) {
                obj['insurancePolicyId'] = ApiClient.convertToType(data['insurancePolicyId'], 'Number');
            }
            if (data.hasOwnProperty('insured')) {
                obj['insured'] = ApiClient.convertToType(data['insured'], 'String');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = ApiClient.convertToType(data['links'], [ObjectLink]);
            }
            if (data.hasOwnProperty('policyType')) {
                obj['policyType'] = ApiClient.convertToType(data['policyType'], 'Number');
            }
            if (data.hasOwnProperty('premium')) {
                obj['premium'] = ApiClient.convertToType(data['premium'], 'Number');
            }
            if (data.hasOwnProperty('premiumFrequency')) {
                obj['premiumFrequency'] = ApiClient.convertToType(data['premiumFrequency'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DisabilityInsurancePolicyWithIdModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DisabilityInsurancePolicyWithIdModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['benefitType'] && !(typeof data['benefitType'] === 'string' || data['benefitType'] instanceof String)) {
            throw new Error("Expected the field `benefitType` to be a primitive type in the JSON string but got " + data['benefitType']);
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

        return true;
    }


}



/**
 * @member {Number} benefit
 */
DisabilityInsurancePolicyWithIdModel.prototype['benefit'] = undefined;

/**
 * @member {Number} benefitFrequency
 */
DisabilityInsurancePolicyWithIdModel.prototype['benefitFrequency'] = undefined;

/**
 * @member {module:model/DisabilityInsurancePolicyWithIdModel.BenefitTypeEnum} benefitType
 */
DisabilityInsurancePolicyWithIdModel.prototype['benefitType'] = undefined;

/**
 * @member {String} description
 */
DisabilityInsurancePolicyWithIdModel.prototype['description'] = undefined;

/**
 * @member {String} externalDestinationId
 */
DisabilityInsurancePolicyWithIdModel.prototype['externalDestinationId'] = undefined;

/**
 * @member {Number} factFinderId
 */
DisabilityInsurancePolicyWithIdModel.prototype['factFinderId'] = undefined;

/**
 * @member {Number} insurancePolicyId
 */
DisabilityInsurancePolicyWithIdModel.prototype['insurancePolicyId'] = undefined;

/**
 * @member {module:model/DisabilityInsurancePolicyWithIdModel.InsuredEnum} insured
 */
DisabilityInsurancePolicyWithIdModel.prototype['insured'] = undefined;

/**
 * @member {Array.<module:model/ObjectLink>} links
 */
DisabilityInsurancePolicyWithIdModel.prototype['links'] = undefined;

/**
 * @member {Number} policyType
 */
DisabilityInsurancePolicyWithIdModel.prototype['policyType'] = undefined;

/**
 * @member {Number} premium
 */
DisabilityInsurancePolicyWithIdModel.prototype['premium'] = undefined;

/**
 * @member {Number} premiumFrequency
 */
DisabilityInsurancePolicyWithIdModel.prototype['premiumFrequency'] = undefined;





/**
 * Allowed values for the <code>benefitType</code> property.
 * @enum {String}
 * @readonly
 */
DisabilityInsurancePolicyWithIdModel['BenefitTypeEnum'] = {

    /**
     * value: "Dollar"
     * @const
     */
    "Dollar": "Dollar",

    /**
     * value: "Percent"
     * @const
     */
    "Percent": "Percent"
};


/**
 * Allowed values for the <code>insured</code> property.
 * @enum {String}
 * @readonly
 */
DisabilityInsurancePolicyWithIdModel['InsuredEnum'] = {

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



export default DisabilityInsurancePolicyWithIdModel;

