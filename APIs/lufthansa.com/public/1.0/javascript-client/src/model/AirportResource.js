/**
 * LH Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import AirportResourceAirports from './AirportResourceAirports';
import AirportResourceMeta from './AirportResourceMeta';

/**
 * The AirportResource model module.
 * @module model/AirportResource
 * @version 1.0
 */
class AirportResource {
    /**
     * Constructs a new <code>AirportResource</code>.
     * Root element of airport response.
     * @alias module:model/AirportResource
     */
    constructor() { 
        
        AirportResource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AirportResource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AirportResource} obj Optional instance to populate.
     * @return {module:model/AirportResource} The populated <code>AirportResource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AirportResource();

            if (data.hasOwnProperty('Airports')) {
                obj['Airports'] = AirportResourceAirports.constructFromObject(data['Airports']);
            }
            if (data.hasOwnProperty('Meta')) {
                obj['Meta'] = AirportResourceMeta.constructFromObject(data['Meta']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AirportResource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AirportResource</code>.
     */
    static validateJSON(data) {
        // validate the optional field `Airports`
        if (data['Airports']) { // data not null
          AirportResourceAirports.validateJSON(data['Airports']);
        }
        // validate the optional field `Meta`
        if (data['Meta']) { // data not null
          AirportResourceMeta.validateJSON(data['Meta']);
        }

        return true;
    }


}



/**
 * @member {module:model/AirportResourceAirports} Airports
 */
AirportResource.prototype['Airports'] = undefined;

/**
 * @member {module:model/AirportResourceMeta} Meta
 */
AirportResource.prototype['Meta'] = undefined;






export default AirportResource;

