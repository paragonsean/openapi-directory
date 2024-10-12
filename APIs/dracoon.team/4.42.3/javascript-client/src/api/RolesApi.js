/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import GroupIds from '../model/GroupIds';
import RoleGroupList from '../model/RoleGroupList';
import RoleList from '../model/RoleList';
import RoleUserList from '../model/RoleUserList';
import UserIds from '../model/UserIds';

/**
* Roles service.
* @module api/RolesApi
* @version 4.42.3
*/
export default class RolesApi {

    /**
    * Constructs a new RolesApi. 
    * @alias module:api/RolesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addRoleGroups operation.
     * @callback module:api/RolesApi~addRoleGroupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RoleGroupList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Assign group(s) to the role
     * ### Description: Assign group(s) to a role.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; grant permission on desired role</span> required.  ### Postcondition: One or more groups will be added to a role.  ### Further Information: None.
     * @param {Number} roleId Role ID
     * @param {module:model/GroupIds} groupIds 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/RolesApi~addRoleGroupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RoleGroupList}
     */
    addRoleGroups(roleId, groupIds, opts, callback) {
      opts = opts || {};
      let postBody = groupIds;
      // verify the required parameter 'roleId' is set
      if (roleId === undefined || roleId === null) {
        throw new Error("Missing the required parameter 'roleId' when calling addRoleGroups");
      }
      // verify the required parameter 'groupIds' is set
      if (groupIds === undefined || groupIds === null) {
        throw new Error("Missing the required parameter 'groupIds' when calling addRoleGroups");
      }

      let pathParams = {
        'role_id': roleId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = RoleGroupList;
      return this.apiClient.callApi(
        '/v4/roles/{role_id}/groups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addRoleUsers operation.
     * @callback module:api/RolesApi~addRoleUsersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RoleUserList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Assign user(s) to the role
     * ### Description: Assign user(s) to a role.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; grant permission on desired role</span> required.  ### Postcondition: One or more users will be added to a role.  ### Further Information: None.
     * @param {Number} roleId Role ID
     * @param {module:model/UserIds} userIds 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/RolesApi~addRoleUsersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RoleUserList}
     */
    addRoleUsers(roleId, userIds, opts, callback) {
      opts = opts || {};
      let postBody = userIds;
      // verify the required parameter 'roleId' is set
      if (roleId === undefined || roleId === null) {
        throw new Error("Missing the required parameter 'roleId' when calling addRoleUsers");
      }
      // verify the required parameter 'userIds' is set
      if (userIds === undefined || userIds === null) {
        throw new Error("Missing the required parameter 'userIds' when calling addRoleUsers");
      }

      let pathParams = {
        'role_id': roleId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = RoleUserList;
      return this.apiClient.callApi(
        '/v4/roles/{role_id}/users', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestRoleGroups operation.
     * @callback module:api/RolesApi~requestRoleGroupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RoleGroupList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request groups with specific role
     * ### Description:   Get all groups with a specific role.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read groups</span> required.  ### Postcondition: List of to the role assigned groups is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: `FIELD_NAME:OPERATOR:VALUE`    <details style=\"padding-left: 10px\"> <summary style=\"cursor: pointer; outline: none\"><strong>Example</strong></summary>  `isMember:eq:false|name:cn:searchString`   Get all groups that are **NOT** a member of that role **AND** whose name contains `searchString`.  </details>  ### Filtering options: <details style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | `FIELD_NAME` | Filter Description | `OPERATOR` | Operator Description | `VALUE` | | :--- | :--- | :--- | :--- | :--- | | `isMember` | Filter the groups which are (not) member of that role | `eq` |  | <ul><li>`true`</li><li>`false`</li><li>`any`</li></ul>default: `true` | | `name` | Group name filter | `cn` | Group name contains value. | `search String` |  </details>
     * @param {Number} roleId Role ID
     * @param {Object} opts Optional parameters
     * @param {Number} [offset] Range offset
     * @param {Number} [limit] Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
     * @param {String} [filter] Filter string
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/RolesApi~requestRoleGroupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RoleGroupList}
     */
    requestRoleGroups(roleId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'roleId' is set
      if (roleId === undefined || roleId === null) {
        throw new Error("Missing the required parameter 'roleId' when calling requestRoleGroups");
      }

      let pathParams = {
        'role_id': roleId
      };
      let queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'filter': opts['filter']
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = RoleGroupList;
      return this.apiClient.callApi(
        '/v4/roles/{role_id}/groups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestRoleUsers operation.
     * @callback module:api/RolesApi~requestRoleUsersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RoleUserList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request users with specific role
     * ### Description:   Get all users with a specific role.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read users</span> required.  ### Postcondition: List of users is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: `FIELD_NAME:OPERATOR:VALUE`    <details style=\"padding-left: 10px\"> <summary style=\"cursor: pointer; outline: none\"><strong>Example</strong></summary>  `isMember:eq:false|user:cn:searchString`   Get all users that are **NOT** member of that role **AND** whose (`firstName` **OR** `lastName` **OR** `email` **OR** `username`) is like `searchString`.  </details>  ### Filtering options: <details style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | `FIELD_NAME` | Filter Description | `OPERATOR` | Operator Description | `VALUE` | | :--- | :--- | :--- | :--- | :--- | | `user` | User filter | `cn` | User contains value (`firstName` **OR** `lastName` **OR** `email` **OR** `username`). | `search String` | | `isMember` | Filter the users which are (not) member of that role | `eq` |  | <ul><li>`true`</li><li>`false`</li><li>`any`</li></ul>default: `true` |  </details>  ### Deprecated filtering options: <details style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | `FIELD_NAME` | Filter Description | `OPERATOR` | Operator Description | `VALUE` | | :--- | :--- | :--- | :--- | :--- | | <del>`displayName`</del> | User display name filter (use `user` filter) | `cn` | User display name contains value (`firstName` **OR** `lastName` **OR** `email`). | `search String` |  </details>
     * @param {Number} roleId Role ID
     * @param {Object} opts Optional parameters
     * @param {Number} [offset] Range offset
     * @param {Number} [limit] Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
     * @param {String} [filter] Filter string
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/RolesApi~requestRoleUsersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RoleUserList}
     */
    requestRoleUsers(roleId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'roleId' is set
      if (roleId === undefined || roleId === null) {
        throw new Error("Missing the required parameter 'roleId' when calling requestRoleUsers");
      }

      let pathParams = {
        'role_id': roleId
      };
      let queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'filter': opts['filter']
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = RoleUserList;
      return this.apiClient.callApi(
        '/v4/roles/{role_id}/users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestRoles operation.
     * @callback module:api/RolesApi~requestRolesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RoleList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request all roles with assigned rights
     * ### Description:   Retrieve a list of all roles with assigned rights.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read users</span> required.  ### Postcondition: List of roles with assigned rights is returned.  ### Further Information: None.
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/RolesApi~requestRolesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RoleList}
     */
    requestRoles(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = RoleList;
      return this.apiClient.callApi(
        '/v4/roles', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the revokeRoleGroups operation.
     * @callback module:api/RolesApi~revokeRoleGroupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RoleGroupList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Revoke granted role from group(s)
     * ### Description:   Revoke granted group(s) from a role.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; grant permission on desired role</span> required.   For each role, at least one non-expiring user **MUST** remain who may grant the role.  ### Postcondition: One or more groups will be removed from a role.  ### Further Information: None.
     * @param {Number} roleId Role ID
     * @param {module:model/GroupIds} groupIds 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/RolesApi~revokeRoleGroupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RoleGroupList}
     */
    revokeRoleGroups(roleId, groupIds, opts, callback) {
      opts = opts || {};
      let postBody = groupIds;
      // verify the required parameter 'roleId' is set
      if (roleId === undefined || roleId === null) {
        throw new Error("Missing the required parameter 'roleId' when calling revokeRoleGroups");
      }
      // verify the required parameter 'groupIds' is set
      if (groupIds === undefined || groupIds === null) {
        throw new Error("Missing the required parameter 'groupIds' when calling revokeRoleGroups");
      }

      let pathParams = {
        'role_id': roleId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = RoleGroupList;
      return this.apiClient.callApi(
        '/v4/roles/{role_id}/groups', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the revokeRoleUsers operation.
     * @callback module:api/RolesApi~revokeRoleUsersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/RoleUserList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Revoke granted role from user(s)
     * ### Description:   Revoke granted user(s) from a role.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; grant permission on desired role</span> required.   For each role, at least one non-expiring user **MUST** remain who may grant the role.  ### Postcondition: One or more users will be removed from a role.  ### Further Information: None.
     * @param {Number} roleId Role ID
     * @param {module:model/UserIds} userIds 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/RolesApi~revokeRoleUsersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/RoleUserList}
     */
    revokeRoleUsers(roleId, userIds, opts, callback) {
      opts = opts || {};
      let postBody = userIds;
      // verify the required parameter 'roleId' is set
      if (roleId === undefined || roleId === null) {
        throw new Error("Missing the required parameter 'roleId' when calling revokeRoleUsers");
      }
      // verify the required parameter 'userIds' is set
      if (userIds === undefined || userIds === null) {
        throw new Error("Missing the required parameter 'userIds' when calling revokeRoleUsers");
      }

      let pathParams = {
        'role_id': roleId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = RoleUserList;
      return this.apiClient.callApi(
        '/v4/roles/{role_id}/users', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
