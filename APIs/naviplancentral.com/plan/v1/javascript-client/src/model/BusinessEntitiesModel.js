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
import IBusinessEntity from './IBusinessEntity';
import ObjectLink from './ObjectLink';

/**
 * The BusinessEntitiesModel model module.
 * @module model/BusinessEntitiesModel
 * @version v1
 */
class BusinessEntitiesModel {
    /**
     * Constructs a new <code>BusinessEntitiesModel</code>.
     * @alias module:model/BusinessEntitiesModel
     */
    constructor() { 
        
        BusinessEntitiesModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BusinessEntitiesModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BusinessEntitiesModel} obj Optional instance to populate.
     * @return {module:model/BusinessEntitiesModel} The populated <code>BusinessEntitiesModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BusinessEntitiesModel();

            if (data.hasOwnProperty('businessEntities')) {
                obj['businessEntities'] = ApiClient.convertToType(data['businessEntities'], [IBusinessEntity]);
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = ApiClient.convertToType(data['links'], [ObjectLink]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BusinessEntitiesModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BusinessEntitiesModel</code>.
     */
    static validateJSON(data) {
        if (data['businessEntities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['businessEntities'])) {
                throw new Error("Expected the field `businessEntities` to be an array in the JSON data but got " + data['businessEntities']);
            }
            // validate the optional field `businessEntities` (array)
            for (const item of data['businessEntities']) {
                IBusinessEntity.validateJSON(item);
            };
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
 * @member {Array.<module:model/IBusinessEntity>} businessEntities
 */
BusinessEntitiesModel.prototype['businessEntities'] = undefined;

/**
 * @member {Array.<module:model/ObjectLink>} links
 */
BusinessEntitiesModel.prototype['links'] = undefined;






export default BusinessEntitiesModel;

