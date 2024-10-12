/**
 * Flight Order Management
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
import BaggageAllowance from './BaggageAllowance';
import ServiceName from './ServiceName';

/**
 * The AdditionalServicesRequest model module.
 * @module model/AdditionalServicesRequest
 * @version 1.9.0
 */
class AdditionalServicesRequest {
    /**
     * Constructs a new <code>AdditionalServicesRequest</code>.
     * @alias module:model/AdditionalServicesRequest
     */
    constructor() { 
        
        AdditionalServicesRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AdditionalServicesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AdditionalServicesRequest} obj Optional instance to populate.
     * @return {module:model/AdditionalServicesRequest} The populated <code>AdditionalServicesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AdditionalServicesRequest();

            if (data.hasOwnProperty('chargeableCheckedBags')) {
                obj['chargeableCheckedBags'] = BaggageAllowance.constructFromObject(data['chargeableCheckedBags']);
            }
            if (data.hasOwnProperty('chargeableSeatNumber')) {
                obj['chargeableSeatNumber'] = ApiClient.convertToType(data['chargeableSeatNumber'], 'String');
            }
            if (data.hasOwnProperty('otherServices')) {
                obj['otherServices'] = ApiClient.convertToType(data['otherServices'], [ServiceName]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AdditionalServicesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AdditionalServicesRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `chargeableCheckedBags`
        if (data['chargeableCheckedBags']) { // data not null
          BaggageAllowance.validateJSON(data['chargeableCheckedBags']);
        }
        // ensure the json data is a string
        if (data['chargeableSeatNumber'] && !(typeof data['chargeableSeatNumber'] === 'string' || data['chargeableSeatNumber'] instanceof String)) {
            throw new Error("Expected the field `chargeableSeatNumber` to be a primitive type in the JSON string but got " + data['chargeableSeatNumber']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['otherServices'])) {
            throw new Error("Expected the field `otherServices` to be an array in the JSON data but got " + data['otherServices']);
        }

        return true;
    }


}



/**
 * @member {module:model/BaggageAllowance} chargeableCheckedBags
 */
AdditionalServicesRequest.prototype['chargeableCheckedBags'] = undefined;

/**
 * seat number
 * @member {String} chargeableSeatNumber
 */
AdditionalServicesRequest.prototype['chargeableSeatNumber'] = undefined;

/**
 * Other services to add
 * @member {Array.<module:model/ServiceName>} otherServices
 */
AdditionalServicesRequest.prototype['otherServices'] = undefined;






export default AdditionalServicesRequest;

