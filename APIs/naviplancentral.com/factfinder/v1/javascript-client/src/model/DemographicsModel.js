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
import FamilyHeadModel from './FamilyHeadModel';

/**
 * The DemographicsModel model module.
 * @module model/DemographicsModel
 * @version v1
 */
class DemographicsModel {
    /**
     * Constructs a new <code>DemographicsModel</code>.
     * @alias module:model/DemographicsModel
     * @param city {String} 
     * @param factFinderId {Number} 
     * @param head1 {module:model/FamilyHeadModel} 
     * @param jointAnalysis {Boolean} 
     * @param state {Number} 
     */
    constructor(city, factFinderId, head1, jointAnalysis, state) { 
        
        DemographicsModel.initialize(this, city, factFinderId, head1, jointAnalysis, state);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, city, factFinderId, head1, jointAnalysis, state) { 
        obj['city'] = city;
        obj['factFinderId'] = factFinderId;
        obj['head1'] = head1;
        obj['jointAnalysis'] = jointAnalysis;
        obj['state'] = state;
    }

    /**
     * Constructs a <code>DemographicsModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DemographicsModel} obj Optional instance to populate.
     * @return {module:model/DemographicsModel} The populated <code>DemographicsModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DemographicsModel();

            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('externalDestinationId')) {
                obj['externalDestinationId'] = ApiClient.convertToType(data['externalDestinationId'], 'String');
            }
            if (data.hasOwnProperty('externalSourceId')) {
                obj['externalSourceId'] = ApiClient.convertToType(data['externalSourceId'], 'String');
            }
            if (data.hasOwnProperty('factFinderId')) {
                obj['factFinderId'] = ApiClient.convertToType(data['factFinderId'], 'Number');
            }
            if (data.hasOwnProperty('head1')) {
                obj['head1'] = FamilyHeadModel.constructFromObject(data['head1']);
            }
            if (data.hasOwnProperty('head2')) {
                obj['head2'] = FamilyHeadModel.constructFromObject(data['head2']);
            }
            if (data.hasOwnProperty('jointAnalysis')) {
                obj['jointAnalysis'] = ApiClient.convertToType(data['jointAnalysis'], 'Boolean');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DemographicsModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DemographicsModel</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DemographicsModel.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['externalDestinationId'] && !(typeof data['externalDestinationId'] === 'string' || data['externalDestinationId'] instanceof String)) {
            throw new Error("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got " + data['externalDestinationId']);
        }
        // ensure the json data is a string
        if (data['externalSourceId'] && !(typeof data['externalSourceId'] === 'string' || data['externalSourceId'] instanceof String)) {
            throw new Error("Expected the field `externalSourceId` to be a primitive type in the JSON string but got " + data['externalSourceId']);
        }
        // validate the optional field `head1`
        if (data['head1']) { // data not null
          FamilyHeadModel.validateJSON(data['head1']);
        }
        // validate the optional field `head2`
        if (data['head2']) { // data not null
          FamilyHeadModel.validateJSON(data['head2']);
        }

        return true;
    }


}

DemographicsModel.RequiredProperties = ["city", "factFinderId", "head1", "jointAnalysis", "state"];

/**
 * @member {String} city
 */
DemographicsModel.prototype['city'] = undefined;

/**
 * @member {String} externalDestinationId
 */
DemographicsModel.prototype['externalDestinationId'] = undefined;

/**
 * @member {String} externalSourceId
 */
DemographicsModel.prototype['externalSourceId'] = undefined;

/**
 * @member {Number} factFinderId
 */
DemographicsModel.prototype['factFinderId'] = undefined;

/**
 * @member {module:model/FamilyHeadModel} head1
 */
DemographicsModel.prototype['head1'] = undefined;

/**
 * @member {module:model/FamilyHeadModel} head2
 */
DemographicsModel.prototype['head2'] = undefined;

/**
 * @member {Boolean} jointAnalysis
 */
DemographicsModel.prototype['jointAnalysis'] = undefined;

/**
 * @member {Number} state
 */
DemographicsModel.prototype['state'] = undefined;






export default DemographicsModel;

