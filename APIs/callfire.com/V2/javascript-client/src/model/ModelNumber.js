/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Region from './Region';

/**
 * The ModelNumber model module.
 * @module model/ModelNumber
 * @version V2
 */
class ModelNumber {
    /**
     * Constructs a new <code>ModelNumber</code>.
     * ~
     * @alias module:model/ModelNumber
     */
    constructor() { 
        
        ModelNumber.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ModelNumber</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ModelNumber} obj Optional instance to populate.
     * @return {module:model/ModelNumber} The populated <code>ModelNumber</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ModelNumber();

            if (data.hasOwnProperty('nationalFormat')) {
                obj['nationalFormat'] = ApiClient.convertToType(data['nationalFormat'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
            if (data.hasOwnProperty('region')) {
                obj['region'] = Region.constructFromObject(data['region']);
            }
            if (data.hasOwnProperty('sendEmailOnCreate')) {
                obj['sendEmailOnCreate'] = ApiClient.convertToType(data['sendEmailOnCreate'], 'Boolean');
            }
            if (data.hasOwnProperty('tollFree')) {
                obj['tollFree'] = ApiClient.convertToType(data['tollFree'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ModelNumber</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ModelNumber</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nationalFormat'] && !(typeof data['nationalFormat'] === 'string' || data['nationalFormat'] instanceof String)) {
            throw new Error("Expected the field `nationalFormat` to be a primitive type in the JSON string but got " + data['nationalFormat']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }
        // validate the optional field `region`
        if (data['region']) { // data not null
          Region.validateJSON(data['region']);
        }

        return true;
    }


}



/**
 * ~
 * @member {String} nationalFormat
 */
ModelNumber.prototype['nationalFormat'] = undefined;

/**
 * ~
 * @member {String} number
 */
ModelNumber.prototype['number'] = undefined;

/**
 * @member {module:model/Region} region
 */
ModelNumber.prototype['region'] = undefined;

/**
 * ~
 * @member {Boolean} sendEmailOnCreate
 */
ModelNumber.prototype['sendEmailOnCreate'] = undefined;

/**
 * ~
 * @member {Boolean} tollFree
 */
ModelNumber.prototype['tollFree'] = undefined;






export default ModelNumber;

