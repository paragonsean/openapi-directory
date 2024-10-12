/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import EndpointGetAutocompletesData from './EndpointGetAutocompletesData';

/**
 * The EndpointGetAutocompletes model module.
 * @module model/EndpointGetAutocompletes
 * @version 4
 */
class EndpointGetAutocompletes {
    /**
     * Constructs a new <code>EndpointGetAutocompletes</code>.
     * @alias module:model/EndpointGetAutocompletes
     */
    constructor() { 
        
        EndpointGetAutocompletes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointGetAutocompletes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointGetAutocompletes} obj Optional instance to populate.
     * @return {module:model/EndpointGetAutocompletes} The populated <code>EndpointGetAutocompletes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointGetAutocompletes();

            if (data.hasOwnProperty('data')) {
                obj['data'] = EndpointGetAutocompletesData.constructFromObject(data['data']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointGetAutocompletes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointGetAutocompletes</code>.
     */
    static validateJSON(data) {
        // validate the optional field `data`
        if (data['data']) { // data not null
          EndpointGetAutocompletesData.validateJSON(data['data']);
        }

        return true;
    }


}



/**
 * @member {module:model/EndpointGetAutocompletesData} data
 */
EndpointGetAutocompletes.prototype['data'] = undefined;






export default EndpointGetAutocompletes;

