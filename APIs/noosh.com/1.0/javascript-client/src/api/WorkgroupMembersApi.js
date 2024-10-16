/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import HTTPStatusVO from '../model/HTTPStatusVO';
import UserDetailsExpandVO from '../model/UserDetailsExpandVO';
import WorkgroupMembersListVO from '../model/WorkgroupMembersListVO';

/**
* WorkgroupMembers service.
* @module api/WorkgroupMembersApi
* @version 1.0
*/
export default class WorkgroupMembersApi {

    /**
    * Constructs a new WorkgroupMembersApi. 
    * @alias module:api/WorkgroupMembersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getWorkgroupMemberInfo operation.
     * @callback module:api/WorkgroupMembersApi~getWorkgroupMemberInfoCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserDetailsExpandVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Workgroup Member Info
     * Workgroup Member Info
     * @param {String} workgroupId 
     * @param {String} userId 
     * @param {module:api/WorkgroupMembersApi~getWorkgroupMemberInfoCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserDetailsExpandVO}
     */
    getWorkgroupMemberInfo(workgroupId, userId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getWorkgroupMemberInfo");
      }
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling getWorkgroupMemberInfo");
      }

      let pathParams = {
        'workgroup_id': workgroupId,
        'user_id': userId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*', 'application/json', 'application/x-json-smile', 'application/x-yaml', 'application/xml', 'text/csv', 'text/x-yaml', 'text/xml'];
      let returnType = UserDetailsExpandVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/workgroupMembers/{user_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getWorkgroupMemberList operation.
     * @callback module:api/WorkgroupMembersApi~getWorkgroupMemberListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/WorkgroupMembersListVO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the workgroup members
     * List the workgroup members
     * @param {String} workgroupId 
     * @param {module:api/WorkgroupMembersApi~getWorkgroupMemberListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/WorkgroupMembersListVO}
     */
    getWorkgroupMemberList(workgroupId, callback) {
      let postBody = null;
      // verify the required parameter 'workgroupId' is set
      if (workgroupId === undefined || workgroupId === null) {
        throw new Error("Missing the required parameter 'workgroupId' when calling getWorkgroupMemberList");
      }

      let pathParams = {
        'workgroup_id': workgroupId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*', 'application/json', 'application/x-json-smile', 'application/x-yaml', 'application/xml', 'text/csv', 'text/x-yaml', 'text/xml'];
      let returnType = WorkgroupMembersListVO;
      return this.apiClient.callApi(
        '/v1/workgroups/{workgroup_id}/workgroupMembers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
