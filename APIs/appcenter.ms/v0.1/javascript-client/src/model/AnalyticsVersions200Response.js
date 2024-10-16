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
import AnalyticsVersions200ResponseVersionsInner from './AnalyticsVersions200ResponseVersionsInner';

/**
 * The AnalyticsVersions200Response model module.
 * @module model/AnalyticsVersions200Response
 * @version v0.1
 */
class AnalyticsVersions200Response {
    /**
     * Constructs a new <code>AnalyticsVersions200Response</code>.
     * @alias module:model/AnalyticsVersions200Response
     */
    constructor() { 
        
        AnalyticsVersions200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalyticsVersions200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalyticsVersions200Response} obj Optional instance to populate.
     * @return {module:model/AnalyticsVersions200Response} The populated <code>AnalyticsVersions200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalyticsVersions200Response();

            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('versions')) {
                obj['versions'] = ApiClient.convertToType(data['versions'], [AnalyticsVersions200ResponseVersionsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnalyticsVersions200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnalyticsVersions200Response</code>.
     */
    static validateJSON(data) {
        if (data['versions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['versions'])) {
                throw new Error("Expected the field `versions` to be an array in the JSON data but got " + data['versions']);
            }
            // validate the optional field `versions` (array)
            for (const item of data['versions']) {
                AnalyticsVersions200ResponseVersionsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The total count of versions.
 * @member {Number} total
 */
AnalyticsVersions200Response.prototype['total'] = undefined;

/**
 * List of version count.
 * @member {Array.<module:model/AnalyticsVersions200ResponseVersionsInner>} versions
 */
AnalyticsVersions200Response.prototype['versions'] = undefined;






export default AnalyticsVersions200Response;

