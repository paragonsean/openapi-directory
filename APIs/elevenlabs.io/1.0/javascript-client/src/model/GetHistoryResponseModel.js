/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import HistoryItemResponseModel from './HistoryItemResponseModel';

/**
 * The GetHistoryResponseModel model module.
 * @module model/GetHistoryResponseModel
 * @version 1.0
 */
class GetHistoryResponseModel {
    /**
     * Constructs a new <code>GetHistoryResponseModel</code>.
     * @alias module:model/GetHistoryResponseModel
     * @param history {Array.<module:model/HistoryItemResponseModel>} 
     */
    constructor(history) { 
        
        GetHistoryResponseModel.initialize(this, history);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, history) { 
        obj['history'] = history;
    }

    /**
     * Constructs a <code>GetHistoryResponseModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetHistoryResponseModel} obj Optional instance to populate.
     * @return {module:model/GetHistoryResponseModel} The populated <code>GetHistoryResponseModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetHistoryResponseModel();

            if (data.hasOwnProperty('history')) {
                obj['history'] = ApiClient.convertToType(data['history'], [HistoryItemResponseModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetHistoryResponseModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetHistoryResponseModel</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetHistoryResponseModel.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['history']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['history'])) {
                throw new Error("Expected the field `history` to be an array in the JSON data but got " + data['history']);
            }
            // validate the optional field `history` (array)
            for (const item of data['history']) {
                HistoryItemResponseModel.validateJSON(item);
            };
        }

        return true;
    }


}

GetHistoryResponseModel.RequiredProperties = ["history"];

/**
 * @member {Array.<module:model/HistoryItemResponseModel>} history
 */
GetHistoryResponseModel.prototype['history'] = undefined;






export default GetHistoryResponseModel;

