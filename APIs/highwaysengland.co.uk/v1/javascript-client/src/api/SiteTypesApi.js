/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import SiteTypeLayer from '../model/SiteTypeLayer';
import SiteTypeResponse from '../model/SiteTypeResponse';

/**
* SiteTypes service.
* @module api/SiteTypesApi
* @version v1
*/
export default class SiteTypesApi {

    /**
    * Constructs a new SiteTypesApi. 
    * @alias module:api/SiteTypesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the siteTypesGetSitesForPublicFacingAPI operation.
     * @callback module:api/SiteTypesApi~siteTypesGetSitesForPublicFacingAPICallback
     * @param {String} error Error message, if any.
     * @param {module:model/SiteTypeLayer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the layer metadata for the LayerId specified.
     * @param {Number} siteTypeId 1 = MIDAS, 2 = TAME, 3 = TMU, 4 = TRADS Legacy
     * @param {String} version 
     * @param {module:api/SiteTypesApi~siteTypesGetSitesForPublicFacingAPICallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SiteTypeLayer}
     */
    siteTypesGetSitesForPublicFacingAPI(siteTypeId, version, callback) {
      let postBody = null;
      // verify the required parameter 'siteTypeId' is set
      if (siteTypeId === undefined || siteTypeId === null) {
        throw new Error("Missing the required parameter 'siteTypeId' when calling siteTypesGetSitesForPublicFacingAPI");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling siteTypesGetSitesForPublicFacingAPI");
      }

      let pathParams = {
        'siteType_Id': siteTypeId,
        'version': version
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SiteTypeLayer;
      return this.apiClient.callApi(
        '/v{version}/sitetypes/{siteType_Id}/sites', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the siteTypesIndex operation.
     * @callback module:api/SiteTypesApi~siteTypesIndexCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SiteTypeResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return list of site types
     * @param {String} version 
     * @param {module:api/SiteTypesApi~siteTypesIndexCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SiteTypeResponse}
     */
    siteTypesIndex(version, callback) {
      let postBody = null;
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling siteTypesIndex");
      }

      let pathParams = {
        'version': version
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SiteTypeResponse;
      return this.apiClient.callApi(
        '/v{version}/sitetypes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
