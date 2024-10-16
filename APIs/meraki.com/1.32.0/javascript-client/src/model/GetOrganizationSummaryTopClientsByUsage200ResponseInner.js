/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork from './GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork';
import GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage from './GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage';

/**
 * The GetOrganizationSummaryTopClientsByUsage200ResponseInner model module.
 * @module model/GetOrganizationSummaryTopClientsByUsage200ResponseInner
 * @version 1.32.0
 */
class GetOrganizationSummaryTopClientsByUsage200ResponseInner {
    /**
     * Constructs a new <code>GetOrganizationSummaryTopClientsByUsage200ResponseInner</code>.
     * @alias module:model/GetOrganizationSummaryTopClientsByUsage200ResponseInner
     */
    constructor() { 
        
        GetOrganizationSummaryTopClientsByUsage200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationSummaryTopClientsByUsage200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationSummaryTopClientsByUsage200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetOrganizationSummaryTopClientsByUsage200ResponseInner} The populated <code>GetOrganizationSummaryTopClientsByUsage200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationSummaryTopClientsByUsage200ResponseInner();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('mac')) {
                obj['mac'] = ApiClient.convertToType(data['mac'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('network')) {
                obj['network'] = GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.constructFromObject(data['network']);
            }
            if (data.hasOwnProperty('usage')) {
                obj['usage'] = GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.constructFromObject(data['usage']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationSummaryTopClientsByUsage200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationSummaryTopClientsByUsage200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['mac'] && !(typeof data['mac'] === 'string' || data['mac'] instanceof String)) {
            throw new Error("Expected the field `mac` to be a primitive type in the JSON string but got " + data['mac']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `network`
        if (data['network']) { // data not null
          GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.validateJSON(data['network']);
        }
        // validate the optional field `usage`
        if (data['usage']) { // data not null
          GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage.validateJSON(data['usage']);
        }

        return true;
    }


}



/**
 * ID of client
 * @member {String} id
 */
GetOrganizationSummaryTopClientsByUsage200ResponseInner.prototype['id'] = undefined;

/**
 * MAC address of client
 * @member {String} mac
 */
GetOrganizationSummaryTopClientsByUsage200ResponseInner.prototype['mac'] = undefined;

/**
 * Name of client
 * @member {String} name
 */
GetOrganizationSummaryTopClientsByUsage200ResponseInner.prototype['name'] = undefined;

/**
 * @member {module:model/GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork} network
 */
GetOrganizationSummaryTopClientsByUsage200ResponseInner.prototype['network'] = undefined;

/**
 * @member {module:model/GetOrganizationSummaryTopClientsByUsage200ResponseInnerUsage} usage
 */
GetOrganizationSummaryTopClientsByUsage200ResponseInner.prototype['usage'] = undefined;






export default GetOrganizationSummaryTopClientsByUsage200ResponseInner;

