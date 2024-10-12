/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DeleteNodesRequest model module.
 * @module model/DeleteNodesRequest
 * @version 4.42.3
 */
class DeleteNodesRequest {
    /**
     * Constructs a new <code>DeleteNodesRequest</code>.
     * Request model for deleting nodes
     * @alias module:model/DeleteNodesRequest
     * @param nodeIds {Array.<Number>} List of node IDs
     */
    constructor(nodeIds) { 
        
        DeleteNodesRequest.initialize(this, nodeIds);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, nodeIds) { 
        obj['nodeIds'] = nodeIds;
    }

    /**
     * Constructs a <code>DeleteNodesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeleteNodesRequest} obj Optional instance to populate.
     * @return {module:model/DeleteNodesRequest} The populated <code>DeleteNodesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeleteNodesRequest();

            if (data.hasOwnProperty('nodeIds')) {
                obj['nodeIds'] = ApiClient.convertToType(data['nodeIds'], ['Number']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeleteNodesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeleteNodesRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeleteNodesRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['nodeIds'])) {
            throw new Error("Expected the field `nodeIds` to be an array in the JSON data but got " + data['nodeIds']);
        }

        return true;
    }


}

DeleteNodesRequest.RequiredProperties = ["nodeIds"];

/**
 * List of node IDs
 * @member {Array.<Number>} nodeIds
 */
DeleteNodesRequest.prototype['nodeIds'] = undefined;






export default DeleteNodesRequest;

