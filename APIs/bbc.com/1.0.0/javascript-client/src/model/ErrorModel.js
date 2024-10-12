/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ErrorModelFault from './ErrorModelFault';

/**
 * The ErrorModel model module.
 * @module model/ErrorModel
 * @version 1.0.0
 */
class ErrorModel {
    /**
     * Constructs a new <code>ErrorModel</code>.
     * @alias module:model/ErrorModel
     */
    constructor() { 
        
        ErrorModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ErrorModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ErrorModel} obj Optional instance to populate.
     * @return {module:model/ErrorModel} The populated <code>ErrorModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ErrorModel();

            if (data.hasOwnProperty('fault')) {
                obj['fault'] = ErrorModelFault.constructFromObject(data['fault']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ErrorModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ErrorModel</code>.
     */
    static validateJSON(data) {
        // validate the optional field `fault`
        if (data['fault']) { // data not null
          ErrorModelFault.validateJSON(data['fault']);
        }

        return true;
    }


}



/**
 * @member {module:model/ErrorModelFault} fault
 */
ErrorModel.prototype['fault'] = undefined;






export default ErrorModel;

