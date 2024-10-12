/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Prediction from './Prediction';
import PredictionQueryToken from './PredictionQueryToken';

/**
 * The PredictionQuery model module.
 * @module model/PredictionQuery
 * @version 1.2
 */
class PredictionQuery {
    /**
     * Constructs a new <code>PredictionQuery</code>.
     * @alias module:model/PredictionQuery
     */
    constructor() { 
        
        PredictionQuery.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PredictionQuery</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PredictionQuery} obj Optional instance to populate.
     * @return {module:model/PredictionQuery} The populated <code>PredictionQuery</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PredictionQuery();

            if (data.hasOwnProperty('Results')) {
                obj['Results'] = ApiClient.convertToType(data['Results'], [Prediction]);
            }
            if (data.hasOwnProperty('Token')) {
                obj['Token'] = PredictionQueryToken.constructFromObject(data['Token']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PredictionQuery</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PredictionQuery</code>.
     */
    static validateJSON(data) {
        if (data['Results']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Results'])) {
                throw new Error("Expected the field `Results` to be an array in the JSON data but got " + data['Results']);
            }
            // validate the optional field `Results` (array)
            for (const item of data['Results']) {
                Prediction.validateJSON(item);
            };
        }
        // validate the optional field `Token`
        if (data['Token']) { // data not null
          PredictionQueryToken.validateJSON(data['Token']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Prediction>} Results
 */
PredictionQuery.prototype['Results'] = undefined;

/**
 * @member {module:model/PredictionQueryToken} Token
 */
PredictionQuery.prototype['Token'] = undefined;






export default PredictionQuery;

