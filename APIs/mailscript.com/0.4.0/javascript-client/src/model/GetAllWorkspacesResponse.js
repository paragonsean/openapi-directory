/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GetAllWorkspacesResponseListInner from './GetAllWorkspacesResponseListInner';

/**
 * The GetAllWorkspacesResponse model module.
 * @module model/GetAllWorkspacesResponse
 * @version 0.4.0
 */
class GetAllWorkspacesResponse {
    /**
     * Constructs a new <code>GetAllWorkspacesResponse</code>.
     * @alias module:model/GetAllWorkspacesResponse
     * @param list {Array.<module:model/GetAllWorkspacesResponseListInner>} 
     */
    constructor(list) { 
        
        GetAllWorkspacesResponse.initialize(this, list);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, list) { 
        obj['list'] = list;
    }

    /**
     * Constructs a <code>GetAllWorkspacesResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetAllWorkspacesResponse} obj Optional instance to populate.
     * @return {module:model/GetAllWorkspacesResponse} The populated <code>GetAllWorkspacesResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetAllWorkspacesResponse();

            if (data.hasOwnProperty('list')) {
                obj['list'] = ApiClient.convertToType(data['list'], [GetAllWorkspacesResponseListInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetAllWorkspacesResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetAllWorkspacesResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetAllWorkspacesResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['list']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['list'])) {
                throw new Error("Expected the field `list` to be an array in the JSON data but got " + data['list']);
            }
            // validate the optional field `list` (array)
            for (const item of data['list']) {
                GetAllWorkspacesResponseListInner.validateJSON(item);
            };
        }

        return true;
    }


}

GetAllWorkspacesResponse.RequiredProperties = ["list"];

/**
 * @member {Array.<module:model/GetAllWorkspacesResponseListInner>} list
 */
GetAllWorkspacesResponse.prototype['list'] = undefined;






export default GetAllWorkspacesResponse;

