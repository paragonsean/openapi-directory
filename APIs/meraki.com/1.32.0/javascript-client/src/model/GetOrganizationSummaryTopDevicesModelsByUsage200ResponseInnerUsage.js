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

/**
 * The GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage model module.
 * @module model/GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage
 * @version 1.32.0
 */
class GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage {
    /**
     * Constructs a new <code>GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage</code>.
     * Usage info in megabytes
     * @alias module:model/GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage
     */
    constructor() { 
        
        GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage} obj Optional instance to populate.
     * @return {module:model/GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage} The populated <code>GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage();

            if (data.hasOwnProperty('average')) {
                obj['average'] = ApiClient.convertToType(data['average'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Average usage in megabytes
 * @member {Number} average
 */
GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.prototype['average'] = undefined;

/**
 * Total usage in megabytes
 * @member {Number} total
 */
GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.prototype['total'] = undefined;






export default GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage;

