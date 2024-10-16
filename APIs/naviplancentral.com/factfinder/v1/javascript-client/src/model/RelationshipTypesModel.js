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
import RelationshipTypeModel from './RelationshipTypeModel';

/**
 * The RelationshipTypesModel model module.
 * @module model/RelationshipTypesModel
 * @version v1
 */
class RelationshipTypesModel {
    /**
     * Constructs a new <code>RelationshipTypesModel</code>.
     * @alias module:model/RelationshipTypesModel
     */
    constructor() { 
        
        RelationshipTypesModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RelationshipTypesModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RelationshipTypesModel} obj Optional instance to populate.
     * @return {module:model/RelationshipTypesModel} The populated <code>RelationshipTypesModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RelationshipTypesModel();

            if (data.hasOwnProperty('relationshipTypes')) {
                obj['relationshipTypes'] = ApiClient.convertToType(data['relationshipTypes'], [RelationshipTypeModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RelationshipTypesModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RelationshipTypesModel</code>.
     */
    static validateJSON(data) {
        if (data['relationshipTypes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['relationshipTypes'])) {
                throw new Error("Expected the field `relationshipTypes` to be an array in the JSON data but got " + data['relationshipTypes']);
            }
            // validate the optional field `relationshipTypes` (array)
            for (const item of data['relationshipTypes']) {
                RelationshipTypeModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/RelationshipTypeModel>} relationshipTypes
 */
RelationshipTypesModel.prototype['relationshipTypes'] = undefined;






export default RelationshipTypesModel;

