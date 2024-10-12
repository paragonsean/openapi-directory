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
import EnvironmentModelHaljsonLinks from './EnvironmentModelHaljsonLinks';
import RolloutPercentageItemModel from './RolloutPercentageItemModel';
import RolloutRuleModel from './RolloutRuleModel';
import SettingValueModelHaljsonEmbedded from './SettingValueModelHaljsonEmbedded';

/**
 * The SettingValueModelHaljson model module.
 * @module model/SettingValueModelHaljson
 * @version v1
 */
class SettingValueModelHaljson {
    /**
     * Constructs a new <code>SettingValueModelHaljson</code>.
     * @alias module:model/SettingValueModelHaljson
     */
    constructor() { 
        
        SettingValueModelHaljson.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SettingValueModelHaljson</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SettingValueModelHaljson} obj Optional instance to populate.
     * @return {module:model/SettingValueModelHaljson} The populated <code>SettingValueModelHaljson</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SettingValueModelHaljson();

            if (data.hasOwnProperty('_embedded')) {
                obj['_embedded'] = SettingValueModelHaljsonEmbedded.constructFromObject(data['_embedded']);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = EnvironmentModelHaljsonLinks.constructFromObject(data['_links']);
            }
            if (data.hasOwnProperty('lastUpdaterUserEmail')) {
                obj['lastUpdaterUserEmail'] = ApiClient.convertToType(data['lastUpdaterUserEmail'], 'String');
            }
            if (data.hasOwnProperty('lastUpdaterUserFullName')) {
                obj['lastUpdaterUserFullName'] = ApiClient.convertToType(data['lastUpdaterUserFullName'], 'String');
            }
            if (data.hasOwnProperty('readOnly')) {
                obj['readOnly'] = ApiClient.convertToType(data['readOnly'], 'Boolean');
            }
            if (data.hasOwnProperty('rolloutPercentageItems')) {
                obj['rolloutPercentageItems'] = ApiClient.convertToType(data['rolloutPercentageItems'], [RolloutPercentageItemModel]);
            }
            if (data.hasOwnProperty('rolloutRules')) {
                obj['rolloutRules'] = ApiClient.convertToType(data['rolloutRules'], [RolloutRuleModel]);
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SettingValueModelHaljson</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SettingValueModelHaljson</code>.
     */
    static validateJSON(data) {
        // validate the optional field `_embedded`
        if (data['_embedded']) { // data not null
          SettingValueModelHaljsonEmbedded.validateJSON(data['_embedded']);
        }
        // validate the optional field `_links`
        if (data['_links']) { // data not null
          EnvironmentModelHaljsonLinks.validateJSON(data['_links']);
        }
        // ensure the json data is a string
        if (data['lastUpdaterUserEmail'] && !(typeof data['lastUpdaterUserEmail'] === 'string' || data['lastUpdaterUserEmail'] instanceof String)) {
            throw new Error("Expected the field `lastUpdaterUserEmail` to be a primitive type in the JSON string but got " + data['lastUpdaterUserEmail']);
        }
        // ensure the json data is a string
        if (data['lastUpdaterUserFullName'] && !(typeof data['lastUpdaterUserFullName'] === 'string' || data['lastUpdaterUserFullName'] instanceof String)) {
            throw new Error("Expected the field `lastUpdaterUserFullName` to be a primitive type in the JSON string but got " + data['lastUpdaterUserFullName']);
        }
        if (data['rolloutPercentageItems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['rolloutPercentageItems'])) {
                throw new Error("Expected the field `rolloutPercentageItems` to be an array in the JSON data but got " + data['rolloutPercentageItems']);
            }
            // validate the optional field `rolloutPercentageItems` (array)
            for (const item of data['rolloutPercentageItems']) {
                RolloutPercentageItemModel.validateJSON(item);
            };
        }
        if (data['rolloutRules']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['rolloutRules'])) {
                throw new Error("Expected the field `rolloutRules` to be an array in the JSON data but got " + data['rolloutRules']);
            }
            // validate the optional field `rolloutRules` (array)
            for (const item of data['rolloutRules']) {
                RolloutRuleModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/SettingValueModelHaljsonEmbedded} _embedded
 */
SettingValueModelHaljson.prototype['_embedded'] = undefined;

/**
 * @member {module:model/EnvironmentModelHaljsonLinks} _links
 */
SettingValueModelHaljson.prototype['_links'] = undefined;

/**
 * @member {String} lastUpdaterUserEmail
 */
SettingValueModelHaljson.prototype['lastUpdaterUserEmail'] = undefined;

/**
 * @member {String} lastUpdaterUserFullName
 */
SettingValueModelHaljson.prototype['lastUpdaterUserFullName'] = undefined;

/**
 * @member {Boolean} readOnly
 */
SettingValueModelHaljson.prototype['readOnly'] = undefined;

/**
 * The percentage rule collection.
 * @member {Array.<module:model/RolloutPercentageItemModel>} rolloutPercentageItems
 */
SettingValueModelHaljson.prototype['rolloutPercentageItems'] = undefined;

/**
 * The targeting rule collection.
 * @member {Array.<module:model/RolloutRuleModel>} rolloutRules
 */
SettingValueModelHaljson.prototype['rolloutRules'] = undefined;

/**
 * @member {Date} updatedAt
 */
SettingValueModelHaljson.prototype['updatedAt'] = undefined;

/**
 * The value to serve. It must respect the setting type.
 * @member {Object} value
 */
SettingValueModelHaljson.prototype['value'] = undefined;






export default SettingValueModelHaljson;

