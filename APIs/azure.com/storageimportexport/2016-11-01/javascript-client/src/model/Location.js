/**
 * StorageImportExport
 * The Storage Import/Export Resource Provider API.
 *
 * The version of the OpenAPI document: 2016-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import LocationProperties from './LocationProperties';

/**
 * The Location model module.
 * @module model/Location
 * @version 2016-11-01
 */
class Location {
    /**
     * Constructs a new <code>Location</code>.
     * Provides information about an Azure data center location.
     * @alias module:model/Location
     */
    constructor() { 
        
        Location.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Location</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Location} obj Optional instance to populate.
     * @return {module:model/Location} The populated <code>Location</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Location();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = LocationProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Location</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Location</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          LocationProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * Specifies the resource identifier of the location. 
 * @member {String} id
 */
Location.prototype['id'] = undefined;

/**
 * Specifies the name of the location. Use List Locations to get all supported locations. 
 * @member {String} name
 */
Location.prototype['name'] = undefined;

/**
 * @member {module:model/LocationProperties} properties
 */
Location.prototype['properties'] = undefined;

/**
 * Specifies the type of the location. 
 * @member {String} type
 */
Location.prototype['type'] = undefined;






export default Location;

