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
import SettingValueModelHaljsonEmbeddedConfig from './SettingValueModelHaljsonEmbeddedConfig';
import SettingValueModelHaljsonEmbeddedEnvironment from './SettingValueModelHaljsonEmbeddedEnvironment';
import SettingValueModelHaljsonEmbeddedIntegrationLinksInner from './SettingValueModelHaljsonEmbeddedIntegrationLinksInner';
import SettingValueModelHaljsonEmbeddedSetting from './SettingValueModelHaljsonEmbeddedSetting';
import SettingValueModelHaljsonEmbeddedSettingTagsInner from './SettingValueModelHaljsonEmbeddedSettingTagsInner';

/**
 * The SettingValueModelHaljsonEmbedded model module.
 * @module model/SettingValueModelHaljsonEmbedded
 * @version v1
 */
class SettingValueModelHaljsonEmbedded {
    /**
     * Constructs a new <code>SettingValueModelHaljsonEmbedded</code>.
     * @alias module:model/SettingValueModelHaljsonEmbedded
     */
    constructor() { 
        
        SettingValueModelHaljsonEmbedded.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SettingValueModelHaljsonEmbedded</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SettingValueModelHaljsonEmbedded} obj Optional instance to populate.
     * @return {module:model/SettingValueModelHaljsonEmbedded} The populated <code>SettingValueModelHaljsonEmbedded</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SettingValueModelHaljsonEmbedded();

            if (data.hasOwnProperty('config')) {
                obj['config'] = SettingValueModelHaljsonEmbeddedConfig.constructFromObject(data['config']);
            }
            if (data.hasOwnProperty('environment')) {
                obj['environment'] = SettingValueModelHaljsonEmbeddedEnvironment.constructFromObject(data['environment']);
            }
            if (data.hasOwnProperty('integrationLinks')) {
                obj['integrationLinks'] = ApiClient.convertToType(data['integrationLinks'], [SettingValueModelHaljsonEmbeddedIntegrationLinksInner]);
            }
            if (data.hasOwnProperty('setting')) {
                obj['setting'] = SettingValueModelHaljsonEmbeddedSetting.constructFromObject(data['setting']);
            }
            if (data.hasOwnProperty('settingTags')) {
                obj['settingTags'] = ApiClient.convertToType(data['settingTags'], [SettingValueModelHaljsonEmbeddedSettingTagsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SettingValueModelHaljsonEmbedded</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SettingValueModelHaljsonEmbedded</code>.
     */
    static validateJSON(data) {
        // validate the optional field `config`
        if (data['config']) { // data not null
          SettingValueModelHaljsonEmbeddedConfig.validateJSON(data['config']);
        }
        // validate the optional field `environment`
        if (data['environment']) { // data not null
          SettingValueModelHaljsonEmbeddedEnvironment.validateJSON(data['environment']);
        }
        if (data['integrationLinks']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['integrationLinks'])) {
                throw new Error("Expected the field `integrationLinks` to be an array in the JSON data but got " + data['integrationLinks']);
            }
            // validate the optional field `integrationLinks` (array)
            for (const item of data['integrationLinks']) {
                SettingValueModelHaljsonEmbeddedIntegrationLinksInner.validateJSON(item);
            };
        }
        // validate the optional field `setting`
        if (data['setting']) { // data not null
          SettingValueModelHaljsonEmbeddedSetting.validateJSON(data['setting']);
        }
        if (data['settingTags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['settingTags'])) {
                throw new Error("Expected the field `settingTags` to be an array in the JSON data but got " + data['settingTags']);
            }
            // validate the optional field `settingTags` (array)
            for (const item of data['settingTags']) {
                SettingValueModelHaljsonEmbeddedSettingTagsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/SettingValueModelHaljsonEmbeddedConfig} config
 */
SettingValueModelHaljsonEmbedded.prototype['config'] = undefined;

/**
 * @member {module:model/SettingValueModelHaljsonEmbeddedEnvironment} environment
 */
SettingValueModelHaljsonEmbedded.prototype['environment'] = undefined;

/**
 * @member {Array.<module:model/SettingValueModelHaljsonEmbeddedIntegrationLinksInner>} integrationLinks
 */
SettingValueModelHaljsonEmbedded.prototype['integrationLinks'] = undefined;

/**
 * @member {module:model/SettingValueModelHaljsonEmbeddedSetting} setting
 */
SettingValueModelHaljsonEmbedded.prototype['setting'] = undefined;

/**
 * @member {Array.<module:model/SettingValueModelHaljsonEmbeddedSettingTagsInner>} settingTags
 */
SettingValueModelHaljsonEmbedded.prototype['settingTags'] = undefined;






export default SettingValueModelHaljsonEmbedded;

