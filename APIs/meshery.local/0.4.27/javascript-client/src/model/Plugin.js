/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PluginConfig from './PluginConfig';
import PluginSettings from './PluginSettings';

/**
 * The Plugin model module.
 * @module model/Plugin
 * @version 0.4.27
 */
class Plugin {
    /**
     * Constructs a new <code>Plugin</code>.
     * Plugin A plugin for the Engine API
     * @alias module:model/Plugin
     * @param config {module:model/PluginConfig} 
     * @param enabled {Boolean} True if the plugin is running. False if the plugin is not running, only installed.
     * @param name {String} name
     * @param settings {module:model/PluginSettings} 
     */
    constructor(config, enabled, name, settings) { 
        
        Plugin.initialize(this, config, enabled, name, settings);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, config, enabled, name, settings) { 
        obj['Config'] = config;
        obj['Enabled'] = enabled;
        obj['Name'] = name;
        obj['Settings'] = settings;
    }

    /**
     * Constructs a <code>Plugin</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Plugin} obj Optional instance to populate.
     * @return {module:model/Plugin} The populated <code>Plugin</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Plugin();

            if (data.hasOwnProperty('Config')) {
                obj['Config'] = PluginConfig.constructFromObject(data['Config']);
            }
            if (data.hasOwnProperty('Enabled')) {
                obj['Enabled'] = ApiClient.convertToType(data['Enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('PluginReference')) {
                obj['PluginReference'] = ApiClient.convertToType(data['PluginReference'], 'String');
            }
            if (data.hasOwnProperty('Settings')) {
                obj['Settings'] = PluginSettings.constructFromObject(data['Settings']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Plugin</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Plugin</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Plugin.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `Config`
        if (data['Config']) { // data not null
          PluginConfig.validateJSON(data['Config']);
        }
        // ensure the json data is a string
        if (data['Id'] && !(typeof data['Id'] === 'string' || data['Id'] instanceof String)) {
            throw new Error("Expected the field `Id` to be a primitive type in the JSON string but got " + data['Id']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['PluginReference'] && !(typeof data['PluginReference'] === 'string' || data['PluginReference'] instanceof String)) {
            throw new Error("Expected the field `PluginReference` to be a primitive type in the JSON string but got " + data['PluginReference']);
        }
        // validate the optional field `Settings`
        if (data['Settings']) { // data not null
          PluginSettings.validateJSON(data['Settings']);
        }

        return true;
    }


}

Plugin.RequiredProperties = ["Config", "Enabled", "Name", "Settings"];

/**
 * @member {module:model/PluginConfig} Config
 */
Plugin.prototype['Config'] = undefined;

/**
 * True if the plugin is running. False if the plugin is not running, only installed.
 * @member {Boolean} Enabled
 */
Plugin.prototype['Enabled'] = undefined;

/**
 * Id
 * @member {String} Id
 */
Plugin.prototype['Id'] = undefined;

/**
 * name
 * @member {String} Name
 */
Plugin.prototype['Name'] = undefined;

/**
 * plugin remote reference used to push/pull the plugin
 * @member {String} PluginReference
 */
Plugin.prototype['PluginReference'] = undefined;

/**
 * @member {module:model/PluginSettings} Settings
 */
Plugin.prototype['Settings'] = undefined;






export default Plugin;

