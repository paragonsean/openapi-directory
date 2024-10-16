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
import BranchConfigurationsGet200ResponseAllOfArtifactVersioning from './BranchConfigurationsGet200ResponseAllOfArtifactVersioning';
import BranchConfigurationsGet200ResponseAllOfToolsets from './BranchConfigurationsGet200ResponseAllOfToolsets';

/**
 * The BranchConfigurationWithId model module.
 * @module model/BranchConfigurationWithId
 * @version v0.1
 */
class BranchConfigurationWithId {
    /**
     * Constructs a new <code>BranchConfigurationWithId</code>.
     * @alias module:model/BranchConfigurationWithId
     * @param id {Number} 
     */
    constructor(id) { 
        
        BranchConfigurationWithId.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>BranchConfigurationWithId</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BranchConfigurationWithId} obj Optional instance to populate.
     * @return {module:model/BranchConfigurationWithId} The populated <code>BranchConfigurationWithId</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BranchConfigurationWithId();

            if (data.hasOwnProperty('artifactVersioning')) {
                obj['artifactVersioning'] = BranchConfigurationsGet200ResponseAllOfArtifactVersioning.constructFromObject(data['artifactVersioning']);
            }
            if (data.hasOwnProperty('badgeIsEnabled')) {
                obj['badgeIsEnabled'] = ApiClient.convertToType(data['badgeIsEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('cloneFromBranch')) {
                obj['cloneFromBranch'] = ApiClient.convertToType(data['cloneFromBranch'], 'String');
            }
            if (data.hasOwnProperty('signed')) {
                obj['signed'] = ApiClient.convertToType(data['signed'], 'Boolean');
            }
            if (data.hasOwnProperty('testsEnabled')) {
                obj['testsEnabled'] = ApiClient.convertToType(data['testsEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('toolsets')) {
                obj['toolsets'] = BranchConfigurationsGet200ResponseAllOfToolsets.constructFromObject(data['toolsets']);
            }
            if (data.hasOwnProperty('trigger')) {
                obj['trigger'] = ApiClient.convertToType(data['trigger'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BranchConfigurationWithId</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BranchConfigurationWithId</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BranchConfigurationWithId.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `artifactVersioning`
        if (data['artifactVersioning']) { // data not null
          BranchConfigurationsGet200ResponseAllOfArtifactVersioning.validateJSON(data['artifactVersioning']);
        }
        // ensure the json data is a string
        if (data['cloneFromBranch'] && !(typeof data['cloneFromBranch'] === 'string' || data['cloneFromBranch'] instanceof String)) {
            throw new Error("Expected the field `cloneFromBranch` to be a primitive type in the JSON string but got " + data['cloneFromBranch']);
        }
        // validate the optional field `toolsets`
        if (data['toolsets']) { // data not null
          BranchConfigurationsGet200ResponseAllOfToolsets.validateJSON(data['toolsets']);
        }
        // ensure the json data is a string
        if (data['trigger'] && !(typeof data['trigger'] === 'string' || data['trigger'] instanceof String)) {
            throw new Error("Expected the field `trigger` to be a primitive type in the JSON string but got " + data['trigger']);
        }

        return true;
    }


}

BranchConfigurationWithId.RequiredProperties = ["id"];

/**
 * @member {module:model/BranchConfigurationsGet200ResponseAllOfArtifactVersioning} artifactVersioning
 */
BranchConfigurationWithId.prototype['artifactVersioning'] = undefined;

/**
 * @member {Boolean} badgeIsEnabled
 */
BranchConfigurationWithId.prototype['badgeIsEnabled'] = undefined;

/**
 * A configured branch name to clone from. If provided, all other parameters will be ignored. Only supported in POST requests.
 * @member {String} cloneFromBranch
 */
BranchConfigurationWithId.prototype['cloneFromBranch'] = undefined;

/**
 * @member {Boolean} signed
 */
BranchConfigurationWithId.prototype['signed'] = undefined;

/**
 * @member {Boolean} testsEnabled
 */
BranchConfigurationWithId.prototype['testsEnabled'] = undefined;

/**
 * @member {module:model/BranchConfigurationsGet200ResponseAllOfToolsets} toolsets
 */
BranchConfigurationWithId.prototype['toolsets'] = undefined;

/**
 * @member {module:model/BranchConfigurationWithId.TriggerEnum} trigger
 */
BranchConfigurationWithId.prototype['trigger'] = undefined;

/**
 * @member {Number} id
 */
BranchConfigurationWithId.prototype['id'] = undefined;





/**
 * Allowed values for the <code>trigger</code> property.
 * @enum {String}
 * @readonly
 */
BranchConfigurationWithId['TriggerEnum'] = {

    /**
     * value: "continous"
     * @const
     */
    "continous": "continous",

    /**
     * value: "continuous"
     * @const
     */
    "continuous": "continuous",

    /**
     * value: "manual"
     * @const
     */
    "manual": "manual"
};



export default BranchConfigurationWithId;

