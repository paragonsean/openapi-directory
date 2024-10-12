/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PasswordCredentials from './PasswordCredentials';
import SwitchDataSourceRequest from './SwitchDataSourceRequest';

/**
 * The JuniperSwitchDataSourceRequest model module.
 * @module model/JuniperSwitchDataSourceRequest
 * @version 1.0.0
 */
class JuniperSwitchDataSourceRequest {
    /**
     * Constructs a new <code>JuniperSwitchDataSourceRequest</code>.
     * @alias module:model/JuniperSwitchDataSourceRequest
     * @implements module:model/SwitchDataSourceRequest
     * @param nickname {String} 
     * @param proxyId {String} proxy vm which should register this vcenter
     */
    constructor(nickname, proxyId) { 
        SwitchDataSourceRequest.initialize(this, nickname, proxyId);
        JuniperSwitchDataSourceRequest.initialize(this, nickname, proxyId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, nickname, proxyId) { 
        obj['enabled'] = true;
        obj['nickname'] = nickname;
        obj['proxy_id'] = proxyId;
    }

    /**
     * Constructs a <code>JuniperSwitchDataSourceRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/JuniperSwitchDataSourceRequest} obj Optional instance to populate.
     * @return {module:model/JuniperSwitchDataSourceRequest} The populated <code>JuniperSwitchDataSourceRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new JuniperSwitchDataSourceRequest();
            SwitchDataSourceRequest.constructFromObject(data, obj);

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('fqdn')) {
                obj['fqdn'] = ApiClient.convertToType(data['fqdn'], 'String');
            }
            if (data.hasOwnProperty('ip')) {
                obj['ip'] = ApiClient.convertToType(data['ip'], 'String');
            }
            if (data.hasOwnProperty('nickname')) {
                obj['nickname'] = ApiClient.convertToType(data['nickname'], 'String');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('proxy_id')) {
                obj['proxy_id'] = ApiClient.convertToType(data['proxy_id'], 'String');
            }
            if (data.hasOwnProperty('credentials')) {
                obj['credentials'] = PasswordCredentials.constructFromObject(data['credentials']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>JuniperSwitchDataSourceRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>JuniperSwitchDataSourceRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of JuniperSwitchDataSourceRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['fqdn'] && !(typeof data['fqdn'] === 'string' || data['fqdn'] instanceof String)) {
            throw new Error("Expected the field `fqdn` to be a primitive type in the JSON string but got " + data['fqdn']);
        }
        // ensure the json data is a string
        if (data['ip'] && !(typeof data['ip'] === 'string' || data['ip'] instanceof String)) {
            throw new Error("Expected the field `ip` to be a primitive type in the JSON string but got " + data['ip']);
        }
        // ensure the json data is a string
        if (data['nickname'] && !(typeof data['nickname'] === 'string' || data['nickname'] instanceof String)) {
            throw new Error("Expected the field `nickname` to be a primitive type in the JSON string but got " + data['nickname']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['proxy_id'] && !(typeof data['proxy_id'] === 'string' || data['proxy_id'] instanceof String)) {
            throw new Error("Expected the field `proxy_id` to be a primitive type in the JSON string but got " + data['proxy_id']);
        }
        // validate the optional field `credentials`
        if (data['credentials']) { // data not null
          PasswordCredentials.validateJSON(data['credentials']);
        }

        return true;
    }


}

JuniperSwitchDataSourceRequest.RequiredProperties = ["nickname", "proxy_id"];

/**
 * @member {Boolean} enabled
 * @default true
 */
JuniperSwitchDataSourceRequest.prototype['enabled'] = true;

/**
 * @member {String} fqdn
 */
JuniperSwitchDataSourceRequest.prototype['fqdn'] = undefined;

/**
 * @member {String} ip
 */
JuniperSwitchDataSourceRequest.prototype['ip'] = undefined;

/**
 * @member {String} nickname
 */
JuniperSwitchDataSourceRequest.prototype['nickname'] = undefined;

/**
 * @member {String} notes
 */
JuniperSwitchDataSourceRequest.prototype['notes'] = undefined;

/**
 * proxy vm which should register this vcenter
 * @member {String} proxy_id
 */
JuniperSwitchDataSourceRequest.prototype['proxy_id'] = undefined;

/**
 * @member {module:model/PasswordCredentials} credentials
 */
JuniperSwitchDataSourceRequest.prototype['credentials'] = undefined;


// Implement SwitchDataSourceRequest interface:
/**
 * @member {Boolean} enabled
 * @default true
 */
SwitchDataSourceRequest.prototype['enabled'] = true;
/**
 * @member {String} fqdn
 */
SwitchDataSourceRequest.prototype['fqdn'] = undefined;
/**
 * @member {String} ip
 */
SwitchDataSourceRequest.prototype['ip'] = undefined;
/**
 * @member {String} nickname
 */
SwitchDataSourceRequest.prototype['nickname'] = undefined;
/**
 * @member {String} notes
 */
SwitchDataSourceRequest.prototype['notes'] = undefined;
/**
 * proxy vm which should register this vcenter
 * @member {String} proxy_id
 */
SwitchDataSourceRequest.prototype['proxy_id'] = undefined;
/**
 * @member {module:model/PasswordCredentials} credentials
 */
SwitchDataSourceRequest.prototype['credentials'] = undefined;




export default JuniperSwitchDataSourceRequest;

