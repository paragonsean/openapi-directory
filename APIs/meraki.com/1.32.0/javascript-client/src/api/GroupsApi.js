/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CreateNetworkFirmwareUpgradesStagedGroupRequest from '../model/CreateNetworkFirmwareUpgradesStagedGroupRequest';
import CreateOrganizationAdaptivePolicyGroupRequest from '../model/CreateOrganizationAdaptivePolicyGroupRequest';
import CreateOrganizationPolicyObjectsGroupRequest from '../model/CreateOrganizationPolicyObjectsGroupRequest';
import GetNetworkFirmwareUpgradesStagedGroups200ResponseInner from '../model/GetNetworkFirmwareUpgradesStagedGroups200ResponseInner';
import UpdateOrganizationAdaptivePolicyGroupRequest from '../model/UpdateOrganizationAdaptivePolicyGroupRequest';
import UpdateOrganizationPolicyObjectsGroupRequest from '../model/UpdateOrganizationPolicyObjectsGroupRequest';

/**
* Groups service.
* @module api/GroupsApi
* @version 1.32.0
*/
export default class GroupsApi {

    /**
    * Constructs a new GroupsApi. 
    * @alias module:api/GroupsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createNetworkFirmwareUpgradesStagedGroup_3 operation.
     * @callback module:api/GroupsApi~createNetworkFirmwareUpgradesStagedGroup_3Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a Staged Upgrade Group for a network
     * Create a Staged Upgrade Group for a network
     * @param {String} networkId 
     * @param {module:model/CreateNetworkFirmwareUpgradesStagedGroupRequest} createNetworkFirmwareUpgradesStagedGroupRequest 
     * @param {module:api/GroupsApi~createNetworkFirmwareUpgradesStagedGroup_3Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createNetworkFirmwareUpgradesStagedGroup_3(networkId, createNetworkFirmwareUpgradesStagedGroupRequest, callback) {
      let postBody = createNetworkFirmwareUpgradesStagedGroupRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkFirmwareUpgradesStagedGroup_3");
      }
      // verify the required parameter 'createNetworkFirmwareUpgradesStagedGroupRequest' is set
      if (createNetworkFirmwareUpgradesStagedGroupRequest === undefined || createNetworkFirmwareUpgradesStagedGroupRequest === null) {
        throw new Error("Missing the required parameter 'createNetworkFirmwareUpgradesStagedGroupRequest' when calling createNetworkFirmwareUpgradesStagedGroup_3");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/firmwareUpgrades/staged/groups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createOrganizationAdaptivePolicyGroup_2 operation.
     * @callback module:api/GroupsApi~createOrganizationAdaptivePolicyGroup_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new adaptive policy group
     * Creates a new adaptive policy group
     * @param {String} organizationId 
     * @param {module:model/CreateOrganizationAdaptivePolicyGroupRequest} createOrganizationAdaptivePolicyGroupRequest 
     * @param {module:api/GroupsApi~createOrganizationAdaptivePolicyGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createOrganizationAdaptivePolicyGroup_2(organizationId, createOrganizationAdaptivePolicyGroupRequest, callback) {
      let postBody = createOrganizationAdaptivePolicyGroupRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling createOrganizationAdaptivePolicyGroup_2");
      }
      // verify the required parameter 'createOrganizationAdaptivePolicyGroupRequest' is set
      if (createOrganizationAdaptivePolicyGroupRequest === undefined || createOrganizationAdaptivePolicyGroupRequest === null) {
        throw new Error("Missing the required parameter 'createOrganizationAdaptivePolicyGroupRequest' when calling createOrganizationAdaptivePolicyGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/adaptivePolicy/groups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createOrganizationPolicyObjectsGroup_2 operation.
     * @callback module:api/GroupsApi~createOrganizationPolicyObjectsGroup_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new Policy Object Group.
     * Creates a new Policy Object Group.
     * @param {String} organizationId 
     * @param {module:model/CreateOrganizationPolicyObjectsGroupRequest} createOrganizationPolicyObjectsGroupRequest 
     * @param {module:api/GroupsApi~createOrganizationPolicyObjectsGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createOrganizationPolicyObjectsGroup_2(organizationId, createOrganizationPolicyObjectsGroupRequest, callback) {
      let postBody = createOrganizationPolicyObjectsGroupRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling createOrganizationPolicyObjectsGroup_2");
      }
      // verify the required parameter 'createOrganizationPolicyObjectsGroupRequest' is set
      if (createOrganizationPolicyObjectsGroupRequest === undefined || createOrganizationPolicyObjectsGroupRequest === null) {
        throw new Error("Missing the required parameter 'createOrganizationPolicyObjectsGroupRequest' when calling createOrganizationPolicyObjectsGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/policyObjects/groups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetworkFirmwareUpgradesStagedGroup_3 operation.
     * @callback module:api/GroupsApi~deleteNetworkFirmwareUpgradesStagedGroup_3Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Staged Upgrade Group
     * Delete a Staged Upgrade Group
     * @param {String} networkId 
     * @param {String} groupId 
     * @param {module:api/GroupsApi~deleteNetworkFirmwareUpgradesStagedGroup_3Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling deleteNetworkFirmwareUpgradesStagedGroup_3");
      }
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling deleteNetworkFirmwareUpgradesStagedGroup_3");
      }

      let pathParams = {
        'networkId': networkId,
        'groupId': groupId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganizationAdaptivePolicyGroup_2 operation.
     * @callback module:api/GroupsApi~deleteOrganizationAdaptivePolicyGroup_2Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified adaptive policy group and any associated policies and references
     * Deletes the specified adaptive policy group and any associated policies and references
     * @param {String} organizationId 
     * @param {String} id 
     * @param {module:api/GroupsApi~deleteOrganizationAdaptivePolicyGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationAdaptivePolicyGroup_2(organizationId, id, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling deleteOrganizationAdaptivePolicyGroup_2");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteOrganizationAdaptivePolicyGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/adaptivePolicy/groups/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganizationPolicyObjectsGroup_2 operation.
     * @callback module:api/GroupsApi~deleteOrganizationPolicyObjectsGroup_2Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a Policy Object Group.
     * Deletes a Policy Object Group.
     * @param {String} organizationId 
     * @param {String} policyObjectGroupId 
     * @param {module:api/GroupsApi~deleteOrganizationPolicyObjectsGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling deleteOrganizationPolicyObjectsGroup_2");
      }
      // verify the required parameter 'policyObjectGroupId' is set
      if (policyObjectGroupId === undefined || policyObjectGroupId === null) {
        throw new Error("Missing the required parameter 'policyObjectGroupId' when calling deleteOrganizationPolicyObjectsGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'policyObjectGroupId': policyObjectGroupId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkFirmwareUpgradesStagedGroup_3 operation.
     * @callback module:api/GroupsApi~getNetworkFirmwareUpgradesStagedGroup_3Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkFirmwareUpgradesStagedGroups200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a Staged Upgrade Group from a network
     * Get a Staged Upgrade Group from a network
     * @param {String} networkId 
     * @param {String} groupId 
     * @param {module:api/GroupsApi~getNetworkFirmwareUpgradesStagedGroup_3Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkFirmwareUpgradesStagedGroups200ResponseInner}
     */
    getNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkFirmwareUpgradesStagedGroup_3");
      }
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling getNetworkFirmwareUpgradesStagedGroup_3");
      }

      let pathParams = {
        'networkId': networkId,
        'groupId': groupId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetNetworkFirmwareUpgradesStagedGroups200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkFirmwareUpgradesStagedGroups_3 operation.
     * @callback module:api/GroupsApi~getNetworkFirmwareUpgradesStagedGroups_3Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetNetworkFirmwareUpgradesStagedGroups200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List of Staged Upgrade Groups in a network
     * List of Staged Upgrade Groups in a network
     * @param {String} networkId 
     * @param {module:api/GroupsApi~getNetworkFirmwareUpgradesStagedGroups_3Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetNetworkFirmwareUpgradesStagedGroups200ResponseInner>}
     */
    getNetworkFirmwareUpgradesStagedGroups_3(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkFirmwareUpgradesStagedGroups_3");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetNetworkFirmwareUpgradesStagedGroups200ResponseInner];
      return this.apiClient.callApi(
        '/networks/{networkId}/firmwareUpgrades/staged/groups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicyGroup_2 operation.
     * @callback module:api/GroupsApi~getOrganizationAdaptivePolicyGroup_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns an adaptive policy group
     * Returns an adaptive policy group
     * @param {String} organizationId 
     * @param {String} id 
     * @param {module:api/GroupsApi~getOrganizationAdaptivePolicyGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationAdaptivePolicyGroup_2(organizationId, id, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyGroup_2");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getOrganizationAdaptivePolicyGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/adaptivePolicy/groups/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicyGroups_2 operation.
     * @callback module:api/GroupsApi~getOrganizationAdaptivePolicyGroups_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List adaptive policy groups in a organization
     * List adaptive policy groups in a organization
     * @param {String} organizationId 
     * @param {module:api/GroupsApi~getOrganizationAdaptivePolicyGroups_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationAdaptivePolicyGroups_2(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyGroups_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/adaptivePolicy/groups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationPolicyObjectsGroup_2 operation.
     * @callback module:api/GroupsApi~getOrganizationPolicyObjectsGroup_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Shows details of a Policy Object Group.
     * Shows details of a Policy Object Group.
     * @param {String} organizationId 
     * @param {String} policyObjectGroupId 
     * @param {module:api/GroupsApi~getOrganizationPolicyObjectsGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationPolicyObjectsGroup_2");
      }
      // verify the required parameter 'policyObjectGroupId' is set
      if (policyObjectGroupId === undefined || policyObjectGroupId === null) {
        throw new Error("Missing the required parameter 'policyObjectGroupId' when calling getOrganizationPolicyObjectsGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'policyObjectGroupId': policyObjectGroupId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationPolicyObjectsGroups_2 operation.
     * @callback module:api/GroupsApi~getOrganizationPolicyObjectsGroups_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists Policy Object Groups belonging to the organization.
     * Lists Policy Object Groups belonging to the organization.
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {module:api/GroupsApi~getOrganizationPolicyObjectsGroups_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationPolicyObjectsGroups_2(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationPolicyObjectsGroups_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        'perPage': opts['perPage'],
        'startingAfter': opts['startingAfter'],
        'endingBefore': opts['endingBefore']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/policyObjects/groups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkFirmwareUpgradesStagedGroup_3 operation.
     * @callback module:api/GroupsApi~updateNetworkFirmwareUpgradesStagedGroup_3Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Staged Upgrade Group for a network
     * Update a Staged Upgrade Group for a network
     * @param {String} networkId 
     * @param {String} groupId 
     * @param {module:model/CreateNetworkFirmwareUpgradesStagedGroupRequest} createNetworkFirmwareUpgradesStagedGroupRequest 
     * @param {module:api/GroupsApi~updateNetworkFirmwareUpgradesStagedGroup_3Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest, callback) {
      let postBody = createNetworkFirmwareUpgradesStagedGroupRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkFirmwareUpgradesStagedGroup_3");
      }
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling updateNetworkFirmwareUpgradesStagedGroup_3");
      }
      // verify the required parameter 'createNetworkFirmwareUpgradesStagedGroupRequest' is set
      if (createNetworkFirmwareUpgradesStagedGroupRequest === undefined || createNetworkFirmwareUpgradesStagedGroupRequest === null) {
        throw new Error("Missing the required parameter 'createNetworkFirmwareUpgradesStagedGroupRequest' when calling updateNetworkFirmwareUpgradesStagedGroup_3");
      }

      let pathParams = {
        'networkId': networkId,
        'groupId': groupId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationAdaptivePolicyGroup_2 operation.
     * @callback module:api/GroupsApi~updateOrganizationAdaptivePolicyGroup_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates an adaptive policy group
     * Updates an adaptive policy group. If updating \"Infrastructure\", only the SGT is allowed. Cannot update \"Unknown\".
     * @param {String} organizationId 
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateOrganizationAdaptivePolicyGroupRequest} [updateOrganizationAdaptivePolicyGroupRequest] 
     * @param {module:api/GroupsApi~updateOrganizationAdaptivePolicyGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateOrganizationAdaptivePolicyGroup_2(organizationId, id, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationAdaptivePolicyGroupRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationAdaptivePolicyGroup_2");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateOrganizationAdaptivePolicyGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/adaptivePolicy/groups/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationPolicyObjectsGroup_2 operation.
     * @callback module:api/GroupsApi~updateOrganizationPolicyObjectsGroup_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates a Policy Object Group.
     * Updates a Policy Object Group.
     * @param {String} organizationId 
     * @param {String} policyObjectGroupId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateOrganizationPolicyObjectsGroupRequest} [updateOrganizationPolicyObjectsGroupRequest] 
     * @param {module:api/GroupsApi~updateOrganizationPolicyObjectsGroup_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationPolicyObjectsGroupRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationPolicyObjectsGroup_2");
      }
      // verify the required parameter 'policyObjectGroupId' is set
      if (policyObjectGroupId === undefined || policyObjectGroupId === null) {
        throw new Error("Missing the required parameter 'policyObjectGroupId' when calling updateOrganizationPolicyObjectsGroup_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'policyObjectGroupId': policyObjectGroupId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
