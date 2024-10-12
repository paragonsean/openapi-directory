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
import EnvironmentAccessType from './EnvironmentAccessType';

/**
 * The EnvironmentAccessModel model module.
 * @module model/EnvironmentAccessModel
 * @version v1
 */
class EnvironmentAccessModel {
    /**
     * Constructs a new <code>EnvironmentAccessModel</code>.
     * @alias module:model/EnvironmentAccessModel
     */
    constructor() { 
        
        EnvironmentAccessModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EnvironmentAccessModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EnvironmentAccessModel} obj Optional instance to populate.
     * @return {module:model/EnvironmentAccessModel} The populated <code>EnvironmentAccessModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EnvironmentAccessModel();

            if (data.hasOwnProperty('color')) {
                obj['color'] = ApiClient.convertToType(data['color'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('environmentAccessType')) {
                obj['environmentAccessType'] = EnvironmentAccessType.constructFromObject(data['environmentAccessType']);
            }
            if (data.hasOwnProperty('environmentId')) {
                obj['environmentId'] = ApiClient.convertToType(data['environmentId'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('order')) {
                obj['order'] = ApiClient.convertToType(data['order'], 'Number');
            }
            if (data.hasOwnProperty('reasonRequired')) {
                obj['reasonRequired'] = ApiClient.convertToType(data['reasonRequired'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EnvironmentAccessModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EnvironmentAccessModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['color'] && !(typeof data['color'] === 'string' || data['color'] instanceof String)) {
            throw new Error("Expected the field `color` to be a primitive type in the JSON string but got " + data['color']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['environmentId'] && !(typeof data['environmentId'] === 'string' || data['environmentId'] instanceof String)) {
            throw new Error("Expected the field `environmentId` to be a primitive type in the JSON string but got " + data['environmentId']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {String} color
 */
EnvironmentAccessModel.prototype['color'] = undefined;

/**
 * @member {String} description
 */
EnvironmentAccessModel.prototype['description'] = undefined;

/**
 * @member {module:model/EnvironmentAccessType} environmentAccessType
 */
EnvironmentAccessModel.prototype['environmentAccessType'] = undefined;

/**
 * @member {String} environmentId
 */
EnvironmentAccessModel.prototype['environmentId'] = undefined;

/**
 * @member {String} name
 */
EnvironmentAccessModel.prototype['name'] = undefined;

/**
 * @member {Number} order
 */
EnvironmentAccessModel.prototype['order'] = undefined;

/**
 * @member {Boolean} reasonRequired
 */
EnvironmentAccessModel.prototype['reasonRequired'] = undefined;






export default EnvironmentAccessModel;

