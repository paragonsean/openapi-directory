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
 * The BranchConfigurationRevisionChangedBy model module.
 * @module model/BranchConfigurationRevisionChangedBy
 * @version v0.1
 */
class BranchConfigurationRevisionChangedBy {
    /**
     * Constructs a new <code>BranchConfigurationRevisionChangedBy</code>.
     * user who made a change in branch configuration
     * @alias module:model/BranchConfigurationRevisionChangedBy
     */
    constructor() { 
        
        BranchConfigurationRevisionChangedBy.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BranchConfigurationRevisionChangedBy</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BranchConfigurationRevisionChangedBy} obj Optional instance to populate.
     * @return {module:model/BranchConfigurationRevisionChangedBy} The populated <code>BranchConfigurationRevisionChangedBy</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BranchConfigurationRevisionChangedBy();

            if (data.hasOwnProperty('displayName')) {
                obj['displayName'] = ApiClient.convertToType(data['displayName'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BranchConfigurationRevisionChangedBy</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BranchConfigurationRevisionChangedBy</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['displayName'] && !(typeof data['displayName'] === 'string' || data['displayName'] instanceof String)) {
            throw new Error("Expected the field `displayName` to be a primitive type in the JSON string but got " + data['displayName']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}



/**
 * @member {String} displayName
 */
BranchConfigurationRevisionChangedBy.prototype['displayName'] = undefined;

/**
 * @member {String} url
 */
BranchConfigurationRevisionChangedBy.prototype['url'] = undefined;






export default BranchConfigurationRevisionChangedBy;

