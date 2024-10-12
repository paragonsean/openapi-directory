/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CmsDataPageInterface from '../model/CmsDataPageInterface';
import CmsPageRepositoryV1SavePostRequest from '../model/CmsPageRepositoryV1SavePostRequest';
import ErrorResponse from '../model/ErrorResponse';

/**
* CmsPageId service.
* @module api/CmsPageIdApi
* @version 2.2.10
*/
export default class CmsPageIdApi {

    /**
    * Constructs a new CmsPageIdApi. 
    * @alias module:api/CmsPageIdApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the cmsPageRepositoryV1SavePut operation.
     * @callback module:api/CmsPageIdApi~cmsPageRepositoryV1SavePutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CmsDataPageInterface} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * cmsPage/{id}
     * Save page.
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {module:model/CmsPageRepositoryV1SavePostRequest} [cmsPageRepositoryV1SavePostRequest] 
     * @param {module:api/CmsPageIdApi~cmsPageRepositoryV1SavePutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CmsDataPageInterface}
     */
    cmsPageRepositoryV1SavePut(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['cmsPageRepositoryV1SavePostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling cmsPageRepositoryV1SavePut");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = CmsDataPageInterface;
      return this.apiClient.callApi(
        '/V1/cmsPage/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
