/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AdditionalServiceType from './AdditionalServiceType';

/**
 * The AdditionalService model module.
 * @module model/AdditionalService
 * @version 1.9.0
 */
class AdditionalService {
    /**
     * Constructs a new <code>AdditionalService</code>.
     * @alias module:model/AdditionalService
     */
    constructor() { 
        
        AdditionalService.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AdditionalService</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AdditionalService} obj Optional instance to populate.
     * @return {module:model/AdditionalService} The populated <code>AdditionalService</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AdditionalService();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = AdditionalServiceType.constructFromObject(data['type']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AdditionalService</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AdditionalService</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['amount'] && !(typeof data['amount'] === 'string' || data['amount'] instanceof String)) {
            throw new Error("Expected the field `amount` to be a primitive type in the JSON string but got " + data['amount']);
        }

        return true;
    }


}



/**
 * @member {String} amount
 */
AdditionalService.prototype['amount'] = undefined;

/**
 * @member {module:model/AdditionalServiceType} type
 */
AdditionalService.prototype['type'] = undefined;






export default AdditionalService;

