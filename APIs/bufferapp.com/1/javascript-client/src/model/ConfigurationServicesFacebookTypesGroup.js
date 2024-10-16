/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ConfigurationServicesAppdotnetTypesProfileIcons from './ConfigurationServicesAppdotnetTypesProfileIcons';

/**
 * The ConfigurationServicesFacebookTypesGroup model module.
 * @module model/ConfigurationServicesFacebookTypesGroup
 * @version 1
 */
class ConfigurationServicesFacebookTypesGroup {
    /**
     * Constructs a new <code>ConfigurationServicesFacebookTypesGroup</code>.
     * @alias module:model/ConfigurationServicesFacebookTypesGroup
     */
    constructor() { 
        
        ConfigurationServicesFacebookTypesGroup.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ConfigurationServicesFacebookTypesGroup</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConfigurationServicesFacebookTypesGroup} obj Optional instance to populate.
     * @return {module:model/ConfigurationServicesFacebookTypesGroup} The populated <code>ConfigurationServicesFacebookTypesGroup</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConfigurationServicesFacebookTypesGroup();

            if (data.hasOwnProperty('character_limit')) {
                obj['character_limit'] = ApiClient.convertToType(data['character_limit'], 'Number');
            }
            if (data.hasOwnProperty('icons')) {
                obj['icons'] = ConfigurationServicesAppdotnetTypesProfileIcons.constructFromObject(data['icons']);
            }
            if (data.hasOwnProperty('link_attachments')) {
                obj['link_attachments'] = ApiClient.convertToType(data['link_attachments'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('schedule_limit')) {
                obj['schedule_limit'] = ApiClient.convertToType(data['schedule_limit'], 'Number');
            }
            if (data.hasOwnProperty('supported_interactions')) {
                obj['supported_interactions'] = ApiClient.convertToType(data['supported_interactions'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConfigurationServicesFacebookTypesGroup</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConfigurationServicesFacebookTypesGroup</code>.
     */
    static validateJSON(data) {
        // validate the optional field `icons`
        if (data['icons']) { // data not null
          ConfigurationServicesAppdotnetTypesProfileIcons.validateJSON(data['icons']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['supported_interactions'])) {
            throw new Error("Expected the field `supported_interactions` to be an array in the JSON data but got " + data['supported_interactions']);
        }

        return true;
    }


}



/**
 * @member {Number} character_limit
 */
ConfigurationServicesFacebookTypesGroup.prototype['character_limit'] = undefined;

/**
 * @member {module:model/ConfigurationServicesAppdotnetTypesProfileIcons} icons
 */
ConfigurationServicesFacebookTypesGroup.prototype['icons'] = undefined;

/**
 * @member {Boolean} link_attachments
 */
ConfigurationServicesFacebookTypesGroup.prototype['link_attachments'] = undefined;

/**
 * @member {String} name
 */
ConfigurationServicesFacebookTypesGroup.prototype['name'] = undefined;

/**
 * @member {Number} schedule_limit
 */
ConfigurationServicesFacebookTypesGroup.prototype['schedule_limit'] = undefined;

/**
 * @member {Array.<String>} supported_interactions
 */
ConfigurationServicesFacebookTypesGroup.prototype['supported_interactions'] = undefined;






export default ConfigurationServicesFacebookTypesGroup;

