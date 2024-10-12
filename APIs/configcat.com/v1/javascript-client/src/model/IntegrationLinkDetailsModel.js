/**
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IntegrationLinkDetail from './IntegrationLinkDetail';

/**
 * The IntegrationLinkDetailsModel model module.
 * @module model/IntegrationLinkDetailsModel
 * @version v1
 */
class IntegrationLinkDetailsModel {
    /**
     * Constructs a new <code>IntegrationLinkDetailsModel</code>.
     * @alias module:model/IntegrationLinkDetailsModel
     */
    constructor() { 
        
        IntegrationLinkDetailsModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IntegrationLinkDetailsModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IntegrationLinkDetailsModel} obj Optional instance to populate.
     * @return {module:model/IntegrationLinkDetailsModel} The populated <code>IntegrationLinkDetailsModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IntegrationLinkDetailsModel();

            if (data.hasOwnProperty('allIntegrationLinkCount')) {
                obj['allIntegrationLinkCount'] = ApiClient.convertToType(data['allIntegrationLinkCount'], 'Number');
            }
            if (data.hasOwnProperty('details')) {
                obj['details'] = ApiClient.convertToType(data['details'], [IntegrationLinkDetail]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IntegrationLinkDetailsModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IntegrationLinkDetailsModel</code>.
     */
    static validateJSON(data) {
        if (data['details']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['details'])) {
                throw new Error("Expected the field `details` to be an array in the JSON data but got " + data['details']);
            }
            // validate the optional field `details` (array)
            for (const item of data['details']) {
                IntegrationLinkDetail.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} allIntegrationLinkCount
 */
IntegrationLinkDetailsModel.prototype['allIntegrationLinkCount'] = undefined;

/**
 * @member {Array.<module:model/IntegrationLinkDetail>} details
 */
IntegrationLinkDetailsModel.prototype['details'] = undefined;






export default IntegrationLinkDetailsModel;

