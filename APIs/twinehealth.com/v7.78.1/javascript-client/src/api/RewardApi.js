/**
 * Fitbit Plus API
 * # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \"yaml\" file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. <!-- ReDoc-Inject: <security-definitions> -->  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user's identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters `page[size]` and `page[number]` to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a `links` object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=1`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=2`, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters `page[limit]` and `page[after]` to specify the max number of entries returned and identify where to begin the next page. Add `page[limit]` to the parameters to use cursor-based paging. The response will include a `links` object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[limit]=50`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, you will not see a duplicate entry when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[limit]=50&page[after]=<cursor>`.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against `meta.count`. Set `page[size]` or `page[limit]` to 0 to get only the count.  It is not valid to mix the two strategies. 
 *
 * The version of the OpenAPI document: v7.78.1
 * Contact: apiteam@twinehealth.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CreateOrUpdateErrorResponse from '../model/CreateOrUpdateErrorResponse';
import CreateRewardRequest from '../model/CreateRewardRequest';
import CreateRewardResponse from '../model/CreateRewardResponse';
import FetchErrorResponse from '../model/FetchErrorResponse';
import FetchRewardResponse from '../model/FetchRewardResponse';
import FetchRewardsResponse from '../model/FetchRewardsResponse';

/**
* Reward service.
* @module api/RewardApi
* @version v7.78.1
*/
export default class RewardApi {

    /**
    * Constructs a new RewardApi. 
    * @alias module:api/RewardApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createReward operation.
     * @callback module:api/RewardApi~createRewardCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRewardResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a reward
     * Create a reward for a patient.
     * @param {module:model/CreateRewardRequest} createRewardRequest 
     * @param {module:api/RewardApi~createRewardCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRewardResponse}
     */
    createReward(createRewardRequest, callback) {
      let postBody = createRewardRequest;
      // verify the required parameter 'createRewardRequest' is set
      if (createRewardRequest === undefined || createRewardRequest === null) {
        throw new Error("Missing the required parameter 'createRewardRequest' when calling createReward");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/vnd.api+json'];
      let accepts = ['application/vnd.api+json'];
      let returnType = CreateRewardResponse;
      return this.apiClient.callApi(
        '/reward', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchReward operation.
     * @callback module:api/RewardApi~fetchRewardCallback
     * @param {String} error Error message, if any.
     * @param {module:model/FetchRewardResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a reward
     * Get a reward record by id.
     * @param {String} id Reward identifier
     * @param {module:api/RewardApi~fetchRewardCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/FetchRewardResponse}
     */
    fetchReward(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling fetchReward");
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
      let contentTypes = [];
      let accepts = ['application/vnd.api+json'];
      let returnType = FetchRewardResponse;
      return this.apiClient.callApi(
        '/reward/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchRewards operation.
     * @callback module:api/RewardApi~fetchRewardsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/FetchRewardsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List rewards
     * Get a list of rewards matching the specified filters.
     * @param {Object} opts Optional parameters
     * @param {String} [filterPatient] Patient identifier. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
     * @param {String} [filterRewardProgramActivation] Reward program activation identifier
     * @param {String} [filterThread] Thread identifier
     * @param {String} [filterGroups] Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
     * @param {String} [filterOrganization] Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
     * @param {module:api/RewardApi~fetchRewardsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/FetchRewardsResponse}
     */
    fetchRewards(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filter[patient]': opts['filterPatient'],
        'filter[reward_program_activation]': opts['filterRewardProgramActivation'],
        'filter[thread]': opts['filterThread'],
        'filter[groups]': opts['filterGroups'],
        'filter[organization]': opts['filterOrganization']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/vnd.api+json'];
      let returnType = FetchRewardsResponse;
      return this.apiClient.callApi(
        '/reward', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
