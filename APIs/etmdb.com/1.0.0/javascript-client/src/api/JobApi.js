/**
 * EtMDB REST API v1
 * The Ethiopian Movie Database
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Job service.
* @module api/JobApi
* @version 1.0.0
*/
export default class JobApi {

    /**
    * Constructs a new JobApi. 
    * @alias module:api/JobApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the jobSearchRead operation.
     * @callback module:api/JobApi~jobSearchReadCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return job details search result
     * Return job details search result  ### Response Class (Status 200)  * __{job_title}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date
     * @param {String} jobTitle 
     * @param {module:api/JobApi~jobSearchReadCallback} callback The callback function, accepting three arguments: error, data, response
     */
    jobSearchRead(jobTitle, callback) {
      let postBody = null;
      // verify the required parameter 'jobTitle' is set
      if (jobTitle === undefined || jobTitle === null) {
        throw new Error("Missing the required parameter 'jobTitle' when calling jobSearchRead");
      }

      let pathParams = {
        'job_title': jobTitle
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/job/search/{job_title}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the jobSearchallRead operation.
     * @callback module:api/JobApi~jobSearchallReadCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return job details search result
     * Return job details search result  ### Response Class (Status 200)  * __{company_name}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date
     * @param {String} companyName 
     * @param {module:api/JobApi~jobSearchallReadCallback} callback The callback function, accepting three arguments: error, data, response
     */
    jobSearchallRead(companyName, callback) {
      let postBody = null;
      // verify the required parameter 'companyName' is set
      if (companyName === undefined || companyName === null) {
        throw new Error("Missing the required parameter 'companyName' when calling jobSearchallRead");
      }

      let pathParams = {
        'company_name': companyName
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/job/searchall/{company_name}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
