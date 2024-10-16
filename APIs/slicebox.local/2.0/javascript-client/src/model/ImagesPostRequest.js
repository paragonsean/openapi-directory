/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ImagesPostRequest model module.
 * @module model/ImagesPostRequest
 * @version 2.0
 */
class ImagesPostRequest {
    /**
     * Constructs a new <code>ImagesPostRequest</code>.
     * @alias module:model/ImagesPostRequest
     * @param dataset {File} The dataset file
     */
    constructor(dataset) { 
        
        ImagesPostRequest.initialize(this, dataset);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, dataset) { 
        obj['dataset'] = dataset;
    }

    /**
     * Constructs a <code>ImagesPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImagesPostRequest} obj Optional instance to populate.
     * @return {module:model/ImagesPostRequest} The populated <code>ImagesPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImagesPostRequest();

            if (data.hasOwnProperty('dataset')) {
                obj['dataset'] = ApiClient.convertToType(data['dataset'], File);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImagesPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImagesPostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ImagesPostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

ImagesPostRequest.RequiredProperties = ["dataset"];

/**
 * The dataset file
 * @member {File} dataset
 */
ImagesPostRequest.prototype['dataset'] = undefined;






export default ImagesPostRequest;

