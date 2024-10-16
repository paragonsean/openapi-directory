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
 * The RetirementGoalModel model module.
 * @module model/RetirementGoalModel
 * @version v1
 */
class RetirementGoalModel {
    /**
     * Constructs a new <code>RetirementGoalModel</code>.
     * @alias module:model/RetirementGoalModel
     * @param factFinderId {Number} 
     */
    constructor(factFinderId) { 
        
        RetirementGoalModel.initialize(this, factFinderId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, factFinderId) { 
        obj['factFinderId'] = factFinderId;
    }

    /**
     * Constructs a <code>RetirementGoalModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RetirementGoalModel} obj Optional instance to populate.
     * @return {module:model/RetirementGoalModel} The populated <code>RetirementGoalModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RetirementGoalModel();

            if (data.hasOwnProperty('externalDestinationId')) {
                obj['externalDestinationId'] = ApiClient.convertToType(data['externalDestinationId'], 'String');
            }
            if (data.hasOwnProperty('factFinderId')) {
                obj['factFinderId'] = ApiClient.convertToType(data['factFinderId'], 'Number');
            }
            if (data.hasOwnProperty('head1RetirementDate')) {
                obj['head1RetirementDate'] = ApiClient.convertToType(data['head1RetirementDate'], 'Date');
            }
            if (data.hasOwnProperty('head2RetirementDate')) {
                obj['head2RetirementDate'] = ApiClient.convertToType(data['head2RetirementDate'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RetirementGoalModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RetirementGoalModel</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RetirementGoalModel.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['externalDestinationId'] && !(typeof data['externalDestinationId'] === 'string' || data['externalDestinationId'] instanceof String)) {
            throw new Error("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got " + data['externalDestinationId']);
        }

        return true;
    }


}

RetirementGoalModel.RequiredProperties = ["factFinderId"];

/**
 * @member {String} externalDestinationId
 */
RetirementGoalModel.prototype['externalDestinationId'] = undefined;

/**
 * @member {Number} factFinderId
 */
RetirementGoalModel.prototype['factFinderId'] = undefined;

/**
 * @member {Date} head1RetirementDate
 */
RetirementGoalModel.prototype['head1RetirementDate'] = undefined;

/**
 * @member {Date} head2RetirementDate
 */
RetirementGoalModel.prototype['head2RetirementDate'] = undefined;






export default RetirementGoalModel;

