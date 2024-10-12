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
import ConfigModelHaljsonEmbedded from './ConfigModelHaljsonEmbedded';
import EnvironmentModelHaljsonLinks from './EnvironmentModelHaljsonLinks';

/**
 * The TagModelHaljson model module.
 * @module model/TagModelHaljson
 * @version v1
 */
class TagModelHaljson {
    /**
     * Constructs a new <code>TagModelHaljson</code>.
     * @alias module:model/TagModelHaljson
     */
    constructor() { 
        
        TagModelHaljson.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TagModelHaljson</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TagModelHaljson} obj Optional instance to populate.
     * @return {module:model/TagModelHaljson} The populated <code>TagModelHaljson</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TagModelHaljson();

            if (data.hasOwnProperty('_embedded')) {
                obj['_embedded'] = ConfigModelHaljsonEmbedded.constructFromObject(data['_embedded']);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = EnvironmentModelHaljsonLinks.constructFromObject(data['_links']);
            }
            if (data.hasOwnProperty('color')) {
                obj['color'] = ApiClient.convertToType(data['color'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('tagId')) {
                obj['tagId'] = ApiClient.convertToType(data['tagId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TagModelHaljson</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TagModelHaljson</code>.
     */
    static validateJSON(data) {
        // validate the optional field `_embedded`
        if (data['_embedded']) { // data not null
          ConfigModelHaljsonEmbedded.validateJSON(data['_embedded']);
        }
        // validate the optional field `_links`
        if (data['_links']) { // data not null
          EnvironmentModelHaljsonLinks.validateJSON(data['_links']);
        }
        // ensure the json data is a string
        if (data['color'] && !(typeof data['color'] === 'string' || data['color'] instanceof String)) {
            throw new Error("Expected the field `color` to be a primitive type in the JSON string but got " + data['color']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {module:model/ConfigModelHaljsonEmbedded} _embedded
 */
TagModelHaljson.prototype['_embedded'] = undefined;

/**
 * @member {module:model/EnvironmentModelHaljsonLinks} _links
 */
TagModelHaljson.prototype['_links'] = undefined;

/**
 * @member {String} color
 */
TagModelHaljson.prototype['color'] = undefined;

/**
 * @member {String} name
 */
TagModelHaljson.prototype['name'] = undefined;

/**
 * @member {Number} tagId
 */
TagModelHaljson.prototype['tagId'] = undefined;






export default TagModelHaljson;

