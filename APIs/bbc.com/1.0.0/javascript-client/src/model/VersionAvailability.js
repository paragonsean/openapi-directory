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
import VersionAvailabilityAvailability from './VersionAvailabilityAvailability';

/**
 * The VersionAvailability model module.
 * @module model/VersionAvailability
 * @version 1.0.0
 */
class VersionAvailability {
    /**
     * Constructs a new <code>VersionAvailability</code>.
     * @alias module:model/VersionAvailability
     * @param availability {module:model/VersionAvailabilityAvailability} 
     */
    constructor(availability) { 
        
        VersionAvailability.initialize(this, availability);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, availability) { 
        obj['availability'] = availability;
    }

    /**
     * Constructs a <code>VersionAvailability</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VersionAvailability} obj Optional instance to populate.
     * @return {module:model/VersionAvailability} The populated <code>VersionAvailability</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VersionAvailability();

            if (data.hasOwnProperty('availability')) {
                obj['availability'] = VersionAvailabilityAvailability.constructFromObject(data['availability']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VersionAvailability</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VersionAvailability</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of VersionAvailability.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `availability`
        if (data['availability']) { // data not null
          VersionAvailabilityAvailability.validateJSON(data['availability']);
        }

        return true;
    }


}

VersionAvailability.RequiredProperties = ["availability"];

/**
 * @member {module:model/VersionAvailabilityAvailability} availability
 */
VersionAvailability.prototype['availability'] = undefined;






export default VersionAvailability;

