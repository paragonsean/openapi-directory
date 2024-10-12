/**
 * ResourceHealthMetadata API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ResourceHealthMetadata from './ResourceHealthMetadata';

/**
 * The ResourceHealthMetadataCollection model module.
 * @module model/ResourceHealthMetadataCollection
 * @version 2018-02-01
 */
class ResourceHealthMetadataCollection {
    /**
     * Constructs a new <code>ResourceHealthMetadataCollection</code>.
     * Collection of resource health metadata.
     * @alias module:model/ResourceHealthMetadataCollection
     * @param value {Array.<module:model/ResourceHealthMetadata>} Collection of resources.
     */
    constructor(value) { 
        
        ResourceHealthMetadataCollection.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>ResourceHealthMetadataCollection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResourceHealthMetadataCollection} obj Optional instance to populate.
     * @return {module:model/ResourceHealthMetadataCollection} The populated <code>ResourceHealthMetadataCollection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResourceHealthMetadataCollection();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [ResourceHealthMetadata]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResourceHealthMetadataCollection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResourceHealthMetadataCollection</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ResourceHealthMetadataCollection.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                ResourceHealthMetadata.validateJSON(item);
            };
        }

        return true;
    }


}

ResourceHealthMetadataCollection.RequiredProperties = ["value"];

/**
 * Link to next page of resources.
 * @member {String} nextLink
 */
ResourceHealthMetadataCollection.prototype['nextLink'] = undefined;

/**
 * Collection of resources.
 * @member {Array.<module:model/ResourceHealthMetadata>} value
 */
ResourceHealthMetadataCollection.prototype['value'] = undefined;






export default ResourceHealthMetadataCollection;

