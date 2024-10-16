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
 * The GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage model module.
 * @module model/GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage
 * @version 1.32.0
 */
class GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage {
    /**
     * Constructs a new <code>GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage</code>.
     * Date usage of the SSID, in megabytes
     * @alias module:model/GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage
     */
    constructor() { 
        
        GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage} obj Optional instance to populate.
     * @return {module:model/GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage} The populated <code>GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage();

            if (data.hasOwnProperty('downstream')) {
                obj['downstream'] = ApiClient.convertToType(data['downstream'], 'Number');
            }
            if (data.hasOwnProperty('percentage')) {
                obj['percentage'] = ApiClient.convertToType(data['percentage'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('upstream')) {
                obj['upstream'] = ApiClient.convertToType(data['upstream'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Downstream usage of the SSID
 * @member {Number} downstream
 */
GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage.prototype['downstream'] = undefined;

/**
 * Percentage usage of the SSID
 * @member {Number} percentage
 */
GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage.prototype['percentage'] = undefined;

/**
 * Total usage of the SSID
 * @member {Number} total
 */
GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage.prototype['total'] = undefined;

/**
 * Upstream usage of the SSID
 * @member {Number} upstream
 */
GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage.prototype['upstream'] = undefined;






export default GetOrganizationSummaryTopSsidsByUsage200ResponseInnerUsage;

