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
import CodeReferenceRequest from '../model/CodeReferenceRequest';
import DeleteRepositoryReportsRequest from '../model/DeleteRepositoryReportsRequest';

/**
* CodeReferences service.
* @module api/CodeReferencesApi
* @version v1
*/
export default class CodeReferencesApi {

    /**
    * Constructs a new CodeReferencesApi. 
    * @alias module:api/CodeReferencesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v1CodeReferencesDeleteReportsPost operation.
     * @callback module:api/CodeReferencesApi~v1CodeReferencesDeleteReportsPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/DeleteRepositoryReportsRequest} deleteRepositoryReportsRequest 
     * @param {module:api/CodeReferencesApi~v1CodeReferencesDeleteReportsPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    v1CodeReferencesDeleteReportsPost(deleteRepositoryReportsRequest, callback) {
      let postBody = deleteRepositoryReportsRequest;
      // verify the required parameter 'deleteRepositoryReportsRequest' is set
      if (deleteRepositoryReportsRequest === undefined || deleteRepositoryReportsRequest === null) {
        throw new Error("Missing the required parameter 'deleteRepositoryReportsRequest' when calling v1CodeReferencesDeleteReportsPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Basic'];
      let contentTypes = ['application/*+json', 'application/json', 'text/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/v1/code-references/delete-reports', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v1CodeReferencesPost operation.
     * @callback module:api/CodeReferencesApi~v1CodeReferencesPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/CodeReferenceRequest} codeReferenceRequest 
     * @param {module:api/CodeReferencesApi~v1CodeReferencesPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    v1CodeReferencesPost(codeReferenceRequest, callback) {
      let postBody = codeReferenceRequest;
      // verify the required parameter 'codeReferenceRequest' is set
      if (codeReferenceRequest === undefined || codeReferenceRequest === null) {
        throw new Error("Missing the required parameter 'codeReferenceRequest' when calling v1CodeReferencesPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Basic'];
      let contentTypes = ['application/*+json', 'application/json', 'text/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/v1/code-references', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
