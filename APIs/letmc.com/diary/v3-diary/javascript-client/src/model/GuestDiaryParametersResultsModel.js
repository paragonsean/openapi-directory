/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BaseHypermediaLink from './BaseHypermediaLink';
import GuestDiaryParametersModel from './GuestDiaryParametersModel';

/**
 * The GuestDiaryParametersResultsModel model module.
 * @module model/GuestDiaryParametersResultsModel
 * @version v3-diary
 */
class GuestDiaryParametersResultsModel {
    /**
     * Constructs a new <code>GuestDiaryParametersResultsModel</code>.
     * Contacts Person Model Results:-
     * @alias module:model/GuestDiaryParametersResultsModel
     */
    constructor() { 
        
        GuestDiaryParametersResultsModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GuestDiaryParametersResultsModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GuestDiaryParametersResultsModel} obj Optional instance to populate.
     * @return {module:model/GuestDiaryParametersResultsModel} The populated <code>GuestDiaryParametersResultsModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GuestDiaryParametersResultsModel();

            if (data.hasOwnProperty('Count')) {
                obj['Count'] = ApiClient.convertToType(data['Count'], 'Number');
            }
            if (data.hasOwnProperty('Data')) {
                obj['Data'] = ApiClient.convertToType(data['Data'], [GuestDiaryParametersModel]);
            }
            if (data.hasOwnProperty('Links')) {
                obj['Links'] = ApiClient.convertToType(data['Links'], [BaseHypermediaLink]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GuestDiaryParametersResultsModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GuestDiaryParametersResultsModel</code>.
     */
    static validateJSON(data) {
        if (data['Data']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Data'])) {
                throw new Error("Expected the field `Data` to be an array in the JSON data but got " + data['Data']);
            }
            // validate the optional field `Data` (array)
            for (const item of data['Data']) {
                GuestDiaryParametersModel.validateJSON(item);
            };
        }
        if (data['Links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Links'])) {
                throw new Error("Expected the field `Links` to be an array in the JSON data but got " + data['Links']);
            }
            // validate the optional field `Links` (array)
            for (const item of data['Links']) {
                BaseHypermediaLink.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Results count:-
 * @member {Number} Count
 */
GuestDiaryParametersResultsModel.prototype['Count'] = undefined;

/**
 * Results data:-
 * @member {Array.<module:model/GuestDiaryParametersModel>} Data
 */
GuestDiaryParametersResultsModel.prototype['Data'] = undefined;

/**
 * Results links:-
 * @member {Array.<module:model/BaseHypermediaLink>} Links
 */
GuestDiaryParametersResultsModel.prototype['Links'] = undefined;






export default GuestDiaryParametersResultsModel;

