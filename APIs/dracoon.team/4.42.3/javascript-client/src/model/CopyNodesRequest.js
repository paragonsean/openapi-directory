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
import CopyNode from './CopyNode';

/**
 * The CopyNodesRequest model module.
 * @module model/CopyNodesRequest
 * @version 4.42.3
 */
class CopyNodesRequest {
    /**
     * Constructs a new <code>CopyNodesRequest</code>.
     * Request model for copying nodes
     * @alias module:model/CopyNodesRequest
     */
    constructor() { 
        
        CopyNodesRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['keepShareLinks'] = false;
        obj['resolutionStrategy'] = 'autorename';
    }

    /**
     * Constructs a <code>CopyNodesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CopyNodesRequest} obj Optional instance to populate.
     * @return {module:model/CopyNodesRequest} The populated <code>CopyNodesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CopyNodesRequest();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [CopyNode]);
            }
            if (data.hasOwnProperty('keepShareLinks')) {
                obj['keepShareLinks'] = ApiClient.convertToType(data['keepShareLinks'], 'Boolean');
            }
            if (data.hasOwnProperty('nodeIds')) {
                obj['nodeIds'] = ApiClient.convertToType(data['nodeIds'], ['Number']);
            }
            if (data.hasOwnProperty('resolutionStrategy')) {
                obj['resolutionStrategy'] = ApiClient.convertToType(data['resolutionStrategy'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CopyNodesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CopyNodesRequest</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                CopyNode.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['nodeIds'])) {
            throw new Error("Expected the field `nodeIds` to be an array in the JSON data but got " + data['nodeIds']);
        }
        // ensure the json data is a string
        if (data['resolutionStrategy'] && !(typeof data['resolutionStrategy'] === 'string' || data['resolutionStrategy'] instanceof String)) {
            throw new Error("Expected the field `resolutionStrategy` to be a primitive type in the JSON string but got " + data['resolutionStrategy']);
        }

        return true;
    }


}



/**
 * List of nodes to be copied
 * @member {Array.<module:model/CopyNode>} items
 */
CopyNodesRequest.prototype['items'] = undefined;

/**
 * Preserve Download Share Links and point them to the new node.
 * @member {Boolean} keepShareLinks
 * @default false
 */
CopyNodesRequest.prototype['keepShareLinks'] = false;

/**
 * &#128679; Deprecated since v4.5.0  Node IDs  Please use `items` instead.
 * @member {Array.<Number>} nodeIds
 */
CopyNodesRequest.prototype['nodeIds'] = undefined;

/**
 * Node conflict resolution strategy:  * `autorename`  * `overwrite`  * `fail`
 * @member {module:model/CopyNodesRequest.ResolutionStrategyEnum} resolutionStrategy
 * @default 'autorename'
 */
CopyNodesRequest.prototype['resolutionStrategy'] = 'autorename';





/**
 * Allowed values for the <code>resolutionStrategy</code> property.
 * @enum {String}
 * @readonly
 */
CopyNodesRequest['ResolutionStrategyEnum'] = {

    /**
     * value: "autorename"
     * @const
     */
    "autorename": "autorename",

    /**
     * value: "overwrite"
     * @const
     */
    "overwrite": "overwrite",

    /**
     * value: "fail"
     * @const
     */
    "fail": "fail"
};



export default CopyNodesRequest;

