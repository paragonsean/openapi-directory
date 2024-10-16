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
 * The AnalyticsSessionDurationsDistribution200ResponseDistributionInner model module.
 * @module model/AnalyticsSessionDurationsDistribution200ResponseDistributionInner
 * @version v0.1
 */
class AnalyticsSessionDurationsDistribution200ResponseDistributionInner {
    /**
     * Constructs a new <code>AnalyticsSessionDurationsDistribution200ResponseDistributionInner</code>.
     * @alias module:model/AnalyticsSessionDurationsDistribution200ResponseDistributionInner
     */
    constructor() { 
        
        AnalyticsSessionDurationsDistribution200ResponseDistributionInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalyticsSessionDurationsDistribution200ResponseDistributionInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalyticsSessionDurationsDistribution200ResponseDistributionInner} obj Optional instance to populate.
     * @return {module:model/AnalyticsSessionDurationsDistribution200ResponseDistributionInner} The populated <code>AnalyticsSessionDurationsDistribution200ResponseDistributionInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalyticsSessionDurationsDistribution200ResponseDistributionInner();

            if (data.hasOwnProperty('bucket')) {
                obj['bucket'] = ApiClient.convertToType(data['bucket'], 'String');
            }
            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnalyticsSessionDurationsDistribution200ResponseDistributionInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnalyticsSessionDurationsDistribution200ResponseDistributionInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['bucket'] && !(typeof data['bucket'] === 'string' || data['bucket'] instanceof String)) {
            throw new Error("Expected the field `bucket` to be a primitive type in the JSON string but got " + data['bucket']);
        }

        return true;
    }


}



/**
 * The bucket name.
 * @member {String} bucket
 */
AnalyticsSessionDurationsDistribution200ResponseDistributionInner.prototype['bucket'] = undefined;

/**
 * The count of sessions in current bucket.
 * @member {Number} count
 */
AnalyticsSessionDurationsDistribution200ResponseDistributionInner.prototype['count'] = undefined;






export default AnalyticsSessionDurationsDistribution200ResponseDistributionInner;

