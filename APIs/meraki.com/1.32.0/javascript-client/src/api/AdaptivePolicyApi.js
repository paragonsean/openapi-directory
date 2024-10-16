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
import CreateOrganizationAdaptivePolicyAclRequest from '../model/CreateOrganizationAdaptivePolicyAclRequest';
import CreateOrganizationAdaptivePolicyGroupRequest from '../model/CreateOrganizationAdaptivePolicyGroupRequest';
import CreateOrganizationAdaptivePolicyPolicyRequest from '../model/CreateOrganizationAdaptivePolicyPolicyRequest';
import GetOrganizationAdaptivePolicyOverview200Response from '../model/GetOrganizationAdaptivePolicyOverview200Response';
import UpdateOrganizationAdaptivePolicyAclRequest from '../model/UpdateOrganizationAdaptivePolicyAclRequest';
import UpdateOrganizationAdaptivePolicyGroupRequest from '../model/UpdateOrganizationAdaptivePolicyGroupRequest';
import UpdateOrganizationAdaptivePolicyPolicyRequest from '../model/UpdateOrganizationAdaptivePolicyPolicyRequest';
import UpdateOrganizationAdaptivePolicySettingsRequest from '../model/UpdateOrganizationAdaptivePolicySettingsRequest';

/**
* AdaptivePolicy service.
* @module api/AdaptivePolicyApi
* @version 1.32.0
*/
export default class AdaptivePolicyApi {

    /**
    * Constructs a new AdaptivePolicyApi. 
    * @alias module:api/AdaptivePolicyApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createOrganizationAdaptivePolicyAcl_1 operation.
     * @callback module:api/AdaptivePolicyApi~createOrganizationAdaptivePolicyAcl_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates new adaptive policy ACL
     * Creates new adaptive policy ACL
     * @param {String} organizationId 
     * @param {module:model/CreateOrganizationAdaptivePolicyAclRequest} createOrganizationAdaptivePolicyAclRequest 
     * @param {module:api/AdaptivePolicyApi~createOrganizationAdaptivePolicyAcl_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createOrganizationAdaptivePolicyAcl_1(organizationId, createOrganizationAdaptivePolicyAclRequest, callback) {
      let postBody = createOrganizationAdaptivePolicyAclRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling createOrganizationAdaptivePolicyAcl_1");
      }
      // verify the required parameter 'createOrganizationAdaptivePolicyAclRequest' is set
      if (createOrganizationAdaptivePolicyAclRequest === undefined || createOrganizationAdaptivePolicyAclRequest === null) {
        throw new Error("Missing the required parameter 'createOrganizationAdaptivePolicyAclRequest' when calling createOrganizationAdaptivePolicyAcl_1");
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
        '/organizations/{organizationId}/adaptivePolicy/acls', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createOrganizationAdaptivePolicyGroup_1 operation.
     * @callback module:api/AdaptivePolicyApi~createOrganizationAdaptivePolicyGroup_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new adaptive policy group
     * Creates a new adaptive policy group
     * @param {String} organizationId 
     * @param {module:model/CreateOrganizationAdaptivePolicyGroupRequest} createOrganizationAdaptivePolicyGroupRequest 
     * @param {module:api/AdaptivePolicyApi~createOrganizationAdaptivePolicyGroup_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createOrganizationAdaptivePolicyGroup_1(organizationId, createOrganizationAdaptivePolicyGroupRequest, callback) {
      let postBody = createOrganizationAdaptivePolicyGroupRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling createOrganizationAdaptivePolicyGroup_1");
      }
      // verify the required parameter 'createOrganizationAdaptivePolicyGroupRequest' is set
      if (createOrganizationAdaptivePolicyGroupRequest === undefined || createOrganizationAdaptivePolicyGroupRequest === null) {
        throw new Error("Missing the required parameter 'createOrganizationAdaptivePolicyGroupRequest' when calling createOrganizationAdaptivePolicyGroup_1");
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
     * Callback function to receive the result of the createOrganizationAdaptivePolicyPolicy_1 operation.
     * @callback module:api/AdaptivePolicyApi~createOrganizationAdaptivePolicyPolicy_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add an Adaptive Policy
     * Add an Adaptive Policy
     * @param {String} organizationId 
     * @param {module:model/CreateOrganizationAdaptivePolicyPolicyRequest} createOrganizationAdaptivePolicyPolicyRequest 
     * @param {module:api/AdaptivePolicyApi~createOrganizationAdaptivePolicyPolicy_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createOrganizationAdaptivePolicyPolicy_1(organizationId, createOrganizationAdaptivePolicyPolicyRequest, callback) {
      let postBody = createOrganizationAdaptivePolicyPolicyRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling createOrganizationAdaptivePolicyPolicy_1");
      }
      // verify the required parameter 'createOrganizationAdaptivePolicyPolicyRequest' is set
      if (createOrganizationAdaptivePolicyPolicyRequest === undefined || createOrganizationAdaptivePolicyPolicyRequest === null) {
        throw new Error("Missing the required parameter 'createOrganizationAdaptivePolicyPolicyRequest' when calling createOrganizationAdaptivePolicyPolicy_1");
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
        '/organizations/{organizationId}/adaptivePolicy/policies', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganizationAdaptivePolicyAcl_1 operation.
     * @callback module:api/AdaptivePolicyApi~deleteOrganizationAdaptivePolicyAcl_1Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified adaptive policy ACL
     * Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.
     * @param {String} organizationId 
     * @param {String} aclId 
     * @param {module:api/AdaptivePolicyApi~deleteOrganizationAdaptivePolicyAcl_1Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationAdaptivePolicyAcl_1(organizationId, aclId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling deleteOrganizationAdaptivePolicyAcl_1");
      }
      // verify the required parameter 'aclId' is set
      if (aclId === undefined || aclId === null) {
        throw new Error("Missing the required parameter 'aclId' when calling deleteOrganizationAdaptivePolicyAcl_1");
      }

      let pathParams = {
        'organizationId': organizationId,
        'aclId': aclId
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
        '/organizations/{organizationId}/adaptivePolicy/acls/{aclId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganizationAdaptivePolicyGroup_1 operation.
     * @callback module:api/AdaptivePolicyApi~deleteOrganizationAdaptivePolicyGroup_1Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified adaptive policy group and any associated policies and references
     * Deletes the specified adaptive policy group and any associated policies and references
     * @param {String} organizationId 
     * @param {String} id 
     * @param {module:api/AdaptivePolicyApi~deleteOrganizationAdaptivePolicyGroup_1Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationAdaptivePolicyGroup_1(organizationId, id, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling deleteOrganizationAdaptivePolicyGroup_1");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteOrganizationAdaptivePolicyGroup_1");
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
     * Callback function to receive the result of the deleteOrganizationAdaptivePolicyPolicy_1 operation.
     * @callback module:api/AdaptivePolicyApi~deleteOrganizationAdaptivePolicyPolicy_1Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an Adaptive Policy
     * Delete an Adaptive Policy
     * @param {String} organizationId 
     * @param {String} id 
     * @param {module:api/AdaptivePolicyApi~deleteOrganizationAdaptivePolicyPolicy_1Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationAdaptivePolicyPolicy_1(organizationId, id, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling deleteOrganizationAdaptivePolicyPolicy_1");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling deleteOrganizationAdaptivePolicyPolicy_1");
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
        '/organizations/{organizationId}/adaptivePolicy/policies/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicyAcl_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyAcl_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the adaptive policy ACL information
     * Returns the adaptive policy ACL information
     * @param {String} organizationId 
     * @param {String} aclId 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyAcl_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationAdaptivePolicyAcl_1(organizationId, aclId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyAcl_1");
      }
      // verify the required parameter 'aclId' is set
      if (aclId === undefined || aclId === null) {
        throw new Error("Missing the required parameter 'aclId' when calling getOrganizationAdaptivePolicyAcl_1");
      }

      let pathParams = {
        'organizationId': organizationId,
        'aclId': aclId
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
        '/organizations/{organizationId}/adaptivePolicy/acls/{aclId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicyAcls_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyAcls_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List adaptive policy ACLs in a organization
     * List adaptive policy ACLs in a organization
     * @param {String} organizationId 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyAcls_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationAdaptivePolicyAcls_1(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyAcls_1");
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
        '/organizations/{organizationId}/adaptivePolicy/acls', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicyGroup_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyGroup_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns an adaptive policy group
     * Returns an adaptive policy group
     * @param {String} organizationId 
     * @param {String} id 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyGroup_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationAdaptivePolicyGroup_1(organizationId, id, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyGroup_1");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getOrganizationAdaptivePolicyGroup_1");
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
     * Callback function to receive the result of the getOrganizationAdaptivePolicyGroups_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyGroups_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List adaptive policy groups in a organization
     * List adaptive policy groups in a organization
     * @param {String} organizationId 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyGroups_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationAdaptivePolicyGroups_1(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyGroups_1");
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
     * Callback function to receive the result of the getOrganizationAdaptivePolicyOverview_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyOverview_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetOrganizationAdaptivePolicyOverview200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns adaptive policy aggregate statistics for an organization
     * Returns adaptive policy aggregate statistics for an organization
     * @param {String} organizationId 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyOverview_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetOrganizationAdaptivePolicyOverview200Response}
     */
    getOrganizationAdaptivePolicyOverview_1(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyOverview_1");
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
      let returnType = GetOrganizationAdaptivePolicyOverview200Response;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/adaptivePolicy/overview', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicyPolicies_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyPolicies_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List adaptive policies in an organization
     * List adaptive policies in an organization
     * @param {String} organizationId 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyPolicies_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationAdaptivePolicyPolicies_1(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyPolicies_1");
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
        '/organizations/{organizationId}/adaptivePolicy/policies', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicyPolicy_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyPolicy_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return an adaptive policy
     * Return an adaptive policy
     * @param {String} organizationId 
     * @param {String} id 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicyPolicy_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationAdaptivePolicyPolicy_1(organizationId, id, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicyPolicy_1");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling getOrganizationAdaptivePolicyPolicy_1");
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
        '/organizations/{organizationId}/adaptivePolicy/policies/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationAdaptivePolicySettings_1 operation.
     * @callback module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicySettings_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns global adaptive policy settings in an organization
     * Returns global adaptive policy settings in an organization
     * @param {String} organizationId 
     * @param {module:api/AdaptivePolicyApi~getOrganizationAdaptivePolicySettings_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationAdaptivePolicySettings_1(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationAdaptivePolicySettings_1");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/adaptivePolicy/settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationAdaptivePolicyAcl_1 operation.
     * @callback module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicyAcl_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates an adaptive policy ACL
     * Updates an adaptive policy ACL
     * @param {String} organizationId 
     * @param {String} aclId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateOrganizationAdaptivePolicyAclRequest} [updateOrganizationAdaptivePolicyAclRequest] 
     * @param {module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicyAcl_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateOrganizationAdaptivePolicyAcl_1(organizationId, aclId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationAdaptivePolicyAclRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationAdaptivePolicyAcl_1");
      }
      // verify the required parameter 'aclId' is set
      if (aclId === undefined || aclId === null) {
        throw new Error("Missing the required parameter 'aclId' when calling updateOrganizationAdaptivePolicyAcl_1");
      }

      let pathParams = {
        'organizationId': organizationId,
        'aclId': aclId
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
        '/organizations/{organizationId}/adaptivePolicy/acls/{aclId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationAdaptivePolicyGroup_1 operation.
     * @callback module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicyGroup_1Callback
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
     * @param {module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicyGroup_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateOrganizationAdaptivePolicyGroup_1(organizationId, id, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationAdaptivePolicyGroupRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationAdaptivePolicyGroup_1");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateOrganizationAdaptivePolicyGroup_1");
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
     * Callback function to receive the result of the updateOrganizationAdaptivePolicyPolicy_1 operation.
     * @callback module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicyPolicy_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an Adaptive Policy
     * Update an Adaptive Policy
     * @param {String} organizationId 
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateOrganizationAdaptivePolicyPolicyRequest} [updateOrganizationAdaptivePolicyPolicyRequest] 
     * @param {module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicyPolicy_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateOrganizationAdaptivePolicyPolicy_1(organizationId, id, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationAdaptivePolicyPolicyRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationAdaptivePolicyPolicy_1");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling updateOrganizationAdaptivePolicyPolicy_1");
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
        '/organizations/{organizationId}/adaptivePolicy/policies/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationAdaptivePolicySettings_1 operation.
     * @callback module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicySettings_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update global adaptive policy settings
     * Update global adaptive policy settings
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateOrganizationAdaptivePolicySettingsRequest} [updateOrganizationAdaptivePolicySettingsRequest] 
     * @param {module:api/AdaptivePolicyApi~updateOrganizationAdaptivePolicySettings_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateOrganizationAdaptivePolicySettings_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationAdaptivePolicySettingsRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationAdaptivePolicySettings_1");
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
        '/organizations/{organizationId}/adaptivePolicy/settings', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
