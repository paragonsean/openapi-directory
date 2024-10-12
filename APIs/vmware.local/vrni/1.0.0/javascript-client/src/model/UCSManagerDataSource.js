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
import DataSourceType from './DataSourceType';
import PasswordCredentials from './PasswordCredentials';
import SwitchDataSource from './SwitchDataSource';

/**
 * The UCSManagerDataSource model module.
 * @module model/UCSManagerDataSource
 * @version 1.0.0
 */
class UCSManagerDataSource {
    /**
     * Constructs a new <code>UCSManagerDataSource</code>.
     * @alias module:model/UCSManagerDataSource
     * @extends module:model/SwitchDataSource
     * @implements module:model/SwitchDataSource
     */
    constructor() { 
        SwitchDataSource.initialize(this);
        UCSManagerDataSource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UCSManagerDataSource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UCSManagerDataSource} obj Optional instance to populate.
     * @return {module:model/UCSManagerDataSource} The populated <code>UCSManagerDataSource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UCSManagerDataSource();
            SwitchDataSource.constructFromObject(data, obj);
            SwitchDataSource.constructFromObject(data, obj);

        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UCSManagerDataSource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UCSManagerDataSource</code>.
     */
    static validateJSON(data) {

        return true;
    }


}




// Implement SwitchDataSource interface:
/**
 * @member {Boolean} enabled
 * @default true
 */
SwitchDataSource.prototype['enabled'] = true;
/**
 * @member {String} entity_id
 */
SwitchDataSource.prototype['entity_id'] = undefined;
/**
 * @member {module:model/DataSourceType} entity_type
 */
SwitchDataSource.prototype['entity_type'] = undefined;
/**
 * @member {String} fqdn
 */
SwitchDataSource.prototype['fqdn'] = undefined;
/**
 * @member {String} ip
 */
SwitchDataSource.prototype['ip'] = undefined;
/**
 * @member {String} nickname
 */
SwitchDataSource.prototype['nickname'] = undefined;
/**
 * @member {String} notes
 */
SwitchDataSource.prototype['notes'] = undefined;
/**
 * proxy vm which should register this vcenter
 * @member {String} proxy_id
 */
SwitchDataSource.prototype['proxy_id'] = undefined;
/**
 * @member {module:model/PasswordCredentials} credentials
 */
SwitchDataSource.prototype['credentials'] = undefined;




export default UCSManagerDataSource;

