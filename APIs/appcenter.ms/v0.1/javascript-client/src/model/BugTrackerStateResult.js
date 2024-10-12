/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BugTrackerStateResult model module.
 * @module model/BugTrackerStateResult
 * @version v0.1
 */
class BugTrackerStateResult {
    /**
     * Constructs a new <code>BugTrackerStateResult</code>.
     * Object returned in response to getting or updating the state of a bugtracker
     * @alias module:model/BugTrackerStateResult
     */
    constructor() { 
        
        BugTrackerStateResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BugTrackerStateResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BugTrackerStateResult} obj Optional instance to populate.
     * @return {module:model/BugTrackerStateResult} The populated <code>BugTrackerStateResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BugTrackerStateResult();

            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BugTrackerStateResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BugTrackerStateResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }

        return true;
    }


}



/**
 * bugtracker state
 * @member {module:model/BugTrackerStateResult.StateEnum} state
 */
BugTrackerStateResult.prototype['state'] = undefined;





/**
 * Allowed values for the <code>state</code> property.
 * @enum {String}
 * @readonly
 */
BugTrackerStateResult['StateEnum'] = {

    /**
     * value: "enabled"
     * @const
     */
    "enabled": "enabled",

    /**
     * value: "disabled"
     * @const
     */
    "disabled": "disabled",

    /**
     * value: "unauthorized"
     * @const
     */
    "unauthorized": "unauthorized"
};



export default BugTrackerStateResult;

