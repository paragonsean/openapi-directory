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


import ApiClient from "../ApiClient";
import JsonPatch from '../model/JsonPatch';
import SettingValueModel from '../model/SettingValueModel';
import SettingValueModelHaljson from '../model/SettingValueModelHaljson';
import UpdateSettingValueModel from '../model/UpdateSettingValueModel';

/**
* FeatureFlagSettingValuesUsingSDKKey service.
* @module api/FeatureFlagSettingValuesUsingSDKKeyApi
* @version v1
*/
export default class FeatureFlagSettingValuesUsingSDKKeyApi {

    /**
    * Constructs a new FeatureFlagSettingValuesUsingSDKKeyApi. 
    * @alias module:api/FeatureFlagSettingValuesUsingSDKKeyApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getSettingValueBySdkkey operation.
     * @callback module:api/FeatureFlagSettingValuesUsingSDKKeyApi~getSettingValueBySdkkeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SettingValueModelHaljson} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get value
     * This endpoint returns the value of a Feature Flag or Setting  in a specified Environment identified by the <a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://app.configcat.com/sdkkey\">SDK key</a> passed in the `X-CONFIGCAT-SDKKEY` header.  The most important attributes in the response are the `value`, `rolloutRules` and `percentageRules`. The `value` represents what the clients will get when the evaluation requests of our SDKs  are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.  The `rolloutRules` and `percentageRules` attributes are representing the current  Targeting and Percentage Rules configuration of the actual Feature Flag or Setting  in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/advanced/targeting/).
     * @param {String} settingKeyOrId The key or id of the Setting.
     * @param {Object} opts Optional parameters
     * @param {String} [X_CONFIGCAT_SDKKEY] The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
     * @param {module:api/FeatureFlagSettingValuesUsingSDKKeyApi~getSettingValueBySdkkeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SettingValueModelHaljson}
     */
    getSettingValueBySdkkey(settingKeyOrId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'settingKeyOrId' is set
      if (settingKeyOrId === undefined || settingKeyOrId === null) {
        throw new Error("Missing the required parameter 'settingKeyOrId' when calling getSettingValueBySdkkey");
      }

      let pathParams = {
        'settingKeyOrId': settingKeyOrId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-CONFIGCAT-SDKKEY': opts['X_CONFIGCAT_SDKKEY']
      };
      let formParams = {
      };

      let authNames = ['Basic'];
      let contentTypes = [];
      let accepts = ['application/hal+json', 'application/json'];
      let returnType = SettingValueModelHaljson;
      return this.apiClient.callApi(
        '/v1/settings/{settingKeyOrId}/value', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the replaceSettingValueBySdkkey operation.
     * @callback module:api/FeatureFlagSettingValuesUsingSDKKeyApi~replaceSettingValueBySdkkeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SettingValueModelHaljson} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Replace value
     * This endpoint replaces the value of a Feature Flag or Setting  in a specified Environment identified by the <a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://app.configcat.com/sdkkey\">SDK key</a> passed in the `X-CONFIGCAT-SDKKEY` header.  Only the `value`, `rolloutRules` and `percentageRules` attributes are modifiable by this endpoint.  **Important:** As this endpoint is doing a complete replace, it's important to set every other attribute that you don't  want to change to its original state. Not listing one means that it will reset.  For example: We have the following resource. ``` {  \"rolloutPercentageItems\": [   {    \"percentage\": 30,    \"value\": true   },   {    \"percentage\": 70,    \"value\": false   }  ],  \"rolloutRules\": [],  \"value\": false } ``` If we send a replace request body as below: ``` {  \"value\": true } ``` Then besides that the default served value is set to `true`, all the Percentage Rules are deleted.  So we get a response like this: ``` {  \"rolloutPercentageItems\": [],  \"rolloutRules\": [],  \"value\": true } ```
     * @param {String} settingKeyOrId The key or id of the Setting.
     * @param {module:model/UpdateSettingValueModel} updateSettingValueModel 
     * @param {Object} opts Optional parameters
     * @param {String} [reason] The reason note for the Audit Log if the Product's \"Config changes require a reason\" preference is turned on.
     * @param {String} [X_CONFIGCAT_SDKKEY] The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
     * @param {module:api/FeatureFlagSettingValuesUsingSDKKeyApi~replaceSettingValueBySdkkeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SettingValueModelHaljson}
     */
    replaceSettingValueBySdkkey(settingKeyOrId, updateSettingValueModel, opts, callback) {
      opts = opts || {};
      let postBody = updateSettingValueModel;
      // verify the required parameter 'settingKeyOrId' is set
      if (settingKeyOrId === undefined || settingKeyOrId === null) {
        throw new Error("Missing the required parameter 'settingKeyOrId' when calling replaceSettingValueBySdkkey");
      }
      // verify the required parameter 'updateSettingValueModel' is set
      if (updateSettingValueModel === undefined || updateSettingValueModel === null) {
        throw new Error("Missing the required parameter 'updateSettingValueModel' when calling replaceSettingValueBySdkkey");
      }

      let pathParams = {
        'settingKeyOrId': settingKeyOrId
      };
      let queryParams = {
        'reason': opts['reason']
      };
      let headerParams = {
        'X-CONFIGCAT-SDKKEY': opts['X_CONFIGCAT_SDKKEY']
      };
      let formParams = {
      };

      let authNames = ['Basic'];
      let contentTypes = ['application/*+json', 'application/json', 'text/json'];
      let accepts = ['application/hal+json', 'application/json'];
      let returnType = SettingValueModelHaljson;
      return this.apiClient.callApi(
        '/v1/settings/{settingKeyOrId}/value', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateSettingValueBySdkkey operation.
     * @callback module:api/FeatureFlagSettingValuesUsingSDKKeyApi~updateSettingValueBySdkkeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SettingValueModelHaljson} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update value
     * This endpoint updates the value of a Feature Flag or Setting  with a collection of [JSON Patch](http://jsonpatch.com) operations in a specified Environment identified by the <a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://app.configcat.com/sdkkey\">SDK key</a> passed in the `X-CONFIGCAT-SDKKEY` header.  Only the `value`, `rolloutRules` and `percentageRules` attributes are modifiable by this endpoint.  The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don't want to change. It supports collection reordering, so it also  can be used for reordering the targeting rules of a Feature Flag or Setting.  For example: We have the following resource. ``` {  \"rolloutPercentageItems\": [   {    \"percentage\": 30,    \"value\": true   },   {    \"percentage\": 70,    \"value\": false   }  ],  \"rolloutRules\": [],  \"value\": false } ``` If we send an update request body as below: ``` [  {   \"op\": \"replace\",   \"path\": \"/value\",   \"value\": true  } ] ``` Only the default served value is going to be set to `true` and all the Percentage Rules are remaining unchanged. So we get a response like this: ``` {  \"rolloutPercentageItems\": [   {    \"percentage\": 30,    \"value\": true   },   {    \"percentage\": 70,    \"value\": false   }  ],  \"rolloutRules\": [],  \"value\": true } ```
     * @param {String} settingKeyOrId The key or id of the Setting.
     * @param {module:model/JsonPatch} jsonPatch 
     * @param {Object} opts Optional parameters
     * @param {String} [reason] The reason note for the Audit Log if the Product's \"Config changes require a reason\" preference is turned on.
     * @param {String} [X_CONFIGCAT_SDKKEY] The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
     * @param {module:api/FeatureFlagSettingValuesUsingSDKKeyApi~updateSettingValueBySdkkeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SettingValueModelHaljson}
     */
    updateSettingValueBySdkkey(settingKeyOrId, jsonPatch, opts, callback) {
      opts = opts || {};
      let postBody = jsonPatch;
      // verify the required parameter 'settingKeyOrId' is set
      if (settingKeyOrId === undefined || settingKeyOrId === null) {
        throw new Error("Missing the required parameter 'settingKeyOrId' when calling updateSettingValueBySdkkey");
      }
      // verify the required parameter 'jsonPatch' is set
      if (jsonPatch === undefined || jsonPatch === null) {
        throw new Error("Missing the required parameter 'jsonPatch' when calling updateSettingValueBySdkkey");
      }

      let pathParams = {
        'settingKeyOrId': settingKeyOrId
      };
      let queryParams = {
        'reason': opts['reason']
      };
      let headerParams = {
        'X-CONFIGCAT-SDKKEY': opts['X_CONFIGCAT_SDKKEY']
      };
      let formParams = {
      };

      let authNames = ['Basic'];
      let contentTypes = ['application/*+json', 'application/json', 'text/json'];
      let accepts = ['application/hal+json', 'application/json'];
      let returnType = SettingValueModelHaljson;
      return this.apiClient.callApi(
        '/v1/settings/{settingKeyOrId}/value', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
