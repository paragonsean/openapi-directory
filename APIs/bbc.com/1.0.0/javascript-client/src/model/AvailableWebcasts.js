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
import AvailableVersionsElement from './AvailableVersionsElement';

/**
 * The AvailableWebcasts model module.
 * @module model/AvailableWebcasts
 * @version 1.0.0
 */
class AvailableWebcasts {
    /**
     * Constructs a new <code>AvailableWebcasts</code>.
     * @alias module:model/AvailableWebcasts
     * @param available {Number} 
     * @param availableVersionsElement {module:model/AvailableVersionsElement} 
     */
    constructor(available, availableVersionsElement) { 
        
        AvailableWebcasts.initialize(this, available, availableVersionsElement);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, available, availableVersionsElement) { 
        obj['available'] = available;
        obj['available_versions_element'] = availableVersionsElement;
    }

    /**
     * Constructs a <code>AvailableWebcasts</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvailableWebcasts} obj Optional instance to populate.
     * @return {module:model/AvailableWebcasts} The populated <code>AvailableWebcasts</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvailableWebcasts();

            if (data.hasOwnProperty('available')) {
                obj['available'] = ApiClient.convertToType(data['available'], 'Number');
            }
            if (data.hasOwnProperty('available_versions_element')) {
                obj['available_versions_element'] = AvailableVersionsElement.constructFromObject(data['available_versions_element']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvailableWebcasts</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvailableWebcasts</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AvailableWebcasts.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `available_versions_element`
        if (data['available_versions_element']) { // data not null
          AvailableVersionsElement.validateJSON(data['available_versions_element']);
        }

        return true;
    }


}

AvailableWebcasts.RequiredProperties = ["available", "available_versions_element"];

/**
 * @member {Number} available
 */
AvailableWebcasts.prototype['available'] = undefined;

/**
 * @member {module:model/AvailableVersionsElement} available_versions_element
 */
AvailableWebcasts.prototype['available_versions_element'] = undefined;






export default AvailableWebcasts;

