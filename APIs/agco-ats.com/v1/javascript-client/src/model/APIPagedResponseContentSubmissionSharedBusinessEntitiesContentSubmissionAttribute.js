/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import APIPagedResponseMetadata from './APIPagedResponseMetadata';
import ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute from './ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute';

/**
 * The APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute model module.
 * @module model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
 * @version v1
 */
class APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute {
    /**
     * Constructs a new <code>APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute</code>.
     * A response containing a page of results and metadata concerning the results
     * @alias module:model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute
     * @param entities {Array.<module:model/ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute>} 
     * @param metadata {module:model/APIPagedResponseMetadata} 
     */
    constructor(entities, metadata) { 
        
        APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.initialize(this, entities, metadata);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, entities, metadata) { 
        obj['Entities'] = entities;
        obj['Metadata'] = metadata;
    }

    /**
     * Constructs a <code>APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute} obj Optional instance to populate.
     * @return {module:model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute} The populated <code>APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute();

            if (data.hasOwnProperty('Entities')) {
                obj['Entities'] = ApiClient.convertToType(data['Entities'], [ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute]);
            }
            if (data.hasOwnProperty('Metadata')) {
                obj['Metadata'] = APIPagedResponseMetadata.constructFromObject(data['Metadata']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['Entities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Entities'])) {
                throw new Error("Expected the field `Entities` to be an array in the JSON data but got " + data['Entities']);
            }
            // validate the optional field `Entities` (array)
            for (const item of data['Entities']) {
                ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.validateJSON(item);
            };
        }
        // validate the optional field `Metadata`
        if (data['Metadata']) { // data not null
          APIPagedResponseMetadata.validateJSON(data['Metadata']);
        }

        return true;
    }


}

APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.RequiredProperties = ["Entities", "Metadata"];

/**
 * @member {Array.<module:model/ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute>} Entities
 */
APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.prototype['Entities'] = undefined;

/**
 * @member {module:model/APIPagedResponseMetadata} Metadata
 */
APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.prototype['Metadata'] = undefined;






export default APIPagedResponseContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute;

