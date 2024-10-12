/**
 * Hetzner Cloud API
 * This is the official API documentation for the Public Hetzner Cloud.  ## Introduction  The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.  As an alternative to working directly with our API you may also consider to use: * Our CLI program [hcloud](https://github.com/hetznercloud/cli) * Our [library for Go](https://github.com/hetznercloud/hcloud-go) * Our [library for Python](https://github.com/hetznercloud/hcloud-python)  Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).  If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following: * The type of integration you would like to develop * Link to the GitHub repo you will use for the Project * Link to some other Open Source work you have already done (if you have done so)  ## Getting Started To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is `jEheVytlAoFl7F8MqUQ7jAo2hOXASztX`.  You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.haxx.se/).  Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like `servers` inside the example response. A response can also contain a `meta` object with information like [Pagination](https://docs.hetzner.cloud/#overview-pagination).  **Example Request** ```bash curl -H \"Authorization: Bearer jEheVytlAoFl7F8MqUQ7jAo2hOXASztX\" \\     https://api.hetzner.cloud/v1/servers ```  **Example Response** ```json {     \"servers\": [],     \"meta\": {         \"pagination\": {             \"page\": 1,             \"per_page\": 25,             \"previous_page\": null,             \"next_page\": null,             \"last_page\": 1,             \"total_entries\": 0         }     } } ```  ## Authentication All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the `Authorization` HTTP header.  To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token.  **Example Authorization header** ```html Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj ```  ## Errors Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.  The error response contains the following keys:  | Keys      | Meaning                                                               | |-----------|-----------------------------------------------------------------------| | `code`    | Short string indicating the type of error (machine-parsable)          | | `message` | Textual description on what has gone wrong                            | | `details` | An object providing for details on the error (schema depends on code) |  **Example response** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  ### Error Codes  | Code                      | Description                                                                      | |---------------------------|----------------------------------------------------------------------------------| | `forbidden`               | Insufficient permissions for this request                                        | | `invalid_input`           | Error while parsing or processing the input                                      | | `json_error`              | Invalid JSON input in your request                                               | | `locked`                  | The item you are trying to access is locked (there is already an Action running) | | `not_found`               | Entity not found                                                                 | | `rate_limit_exceeded`     | Error when sending too many requests                                             | | `resource_limit_exceeded` | Error when exceeding the maximum quantity of a resource for an account           | | `resource_unavailable`    | The requested resource is currently unavailable                                  | | `service_error`           | Error within a service                                                           | | `uniqueness_error`        | One or more of the objects fields must be unique                                 | | `protected`               | The Action you are trying to start is protected for this resource                | | `maintenance`             | Cannot perform operation due to maintenance                                      | | `conflict`                | The resource has changed during the request, please retry                        | | `unsupported_error`       | The corresponding resource does not support the Action                           | | `token_readonly`          | The token is only allowed to perform GET requests                                | | `unavailable`             | A service or product is currently not available                                  |  **invalid_input** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  **uniqueness_error** ```json {   \"error\": {     \"code\": \"uniqueness_error\",     \"message\": \"SSH key with the same fingerprint already exists\",     \"details\": {       \"fields\": [         {           \"name\": \"public_key\"         }       ]     }   } } ```  **resource_limit_exceeded** ```json {   \"error\": {     \"code\": \"resource_limit_exceeded\",     \"message\": \"project limit exceeded\",     \"details\": {       \"limits\": [         {           \"name\": \"project_limit\"         }       ]     }   } } ```  ## Labels Labels are `key/value` pairs that can be attached to all resources.  Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).  Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.  The `hetzner.cloud/` prefix is reserved and cannot be used.  **Example Labels** ```json {   \"labels\": {     \"environment\":\"development\",     \"service\":\"backend\",     \"example.com/my\":\"label\",     \"just-a-key\":\"\"   } } ```  ## Label Selector For resources with labels, you can filter resources by their labels using the label selector query language.  | Expression           | Meaning                                                             | |----------------------|---------------------------------------------------------------------| | `k==v` / `k=v`       | Value of key `k` does equal value `v`                               | | `k!=v`               | Value of key `k` does not equal value `v`                           | | `k`                  | Key `k` is present                                                  | | `!k`                 | Key `k` is not present                                              | | `k in (v1,v2,v3)`    | Value of key `k` is `v1`, `v2`, or `v3`                             | | `k notin (v1,v2,v3)` | Value of key `k` is neither `v1`, nor `v2`, nor `v3`                | | `k1==v,!k2`          | Value of key `k1` is `v` and key `k2` is not present                |  ### Examples * Returns all resources that have a `env=production` label and that don't have a `type=database` label:    `env=production,type!=database` * Returns all resources that have a `env=testing` or `env=staging` label:      `env in (testing,staging)` * Returns all resources that don't have a `type` label:      `!type`  ## Pagination Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:  * A `page` parameter specifies the page to fetch. The number of the first page is 1. * A `per_page` parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.  Responses contain a `Link` header with pagination information.  Additionally, if the response body is JSON and the root object is an object, that object has a `pagination` object inside the `meta` object with pagination information:  **Example Pagination** ```json {     \"servers\": [...],     \"meta\": {         \"pagination\": {             \"page\": 2,             \"per_page\": 25,             \"previous_page\": 1,             \"next_page\": 3,             \"last_page\": 4,             \"total_entries\": 100         }     } } ```  The keys `previous_page`, `next_page`, `last_page`, and `total_entries` may be `null` when on the first page, last page, or when the total number of entries is unknown.  **Example Pagination Link header** ```bash Link: <https://api.hetzner.cloud/v1/actions?page=2&per_page=5>; rel=\"prev\",       <https://api.hetzner.cloud/v1/actions?page=4&per_page=5>; rel=\"next\",       <https://api.hetzner.cloud/v1/actions?page=6&per_page=5>; rel=\"last\" ```  Line breaks have been added for display purposes only and responses may only contain some of the above `rel` values.  ## Rate Limiting All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a `429 Too Many Requests` error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.  * The `RateLimit-Limit` header contains the total number of requests you can perform per hour. * The `RateLimit-Remaining` header contains the number of requests remaining in the current rate limit time frame. * The `RateLimit-Reset` header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.  The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.  ## Server Metadata Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:  | Data              | Format | Contents                                                     | |-------------------|--------|--------------------------------------------------------------| | hostname          | text   | Name of the Server as set in the api                         | | instance-id       | number | ID of the server                                             | | public-ipv4       | text   | Primary public IPv4 address                                  | | private-networks  | yaml   | Details about the private networks the Server is attached to | | availability-zone | text   | Name of the availability zone that Server runs in            | | region            | text   | Network zone, e.g. eu-central                                |  **Example: Summary** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata ```  ```yaml availability-zone: hel1-dc2 hostname: my-server instance-id: 42 public-ipv4: 1.2.3.4 region: eu-central ```  **Example: Hostname** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/hostname my-server ```  **Example: Instance ID** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/instance-id 42 ```  **Example: Public IPv4** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4 1.2.3.4 ```  **Example: Private Networks** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/private-networks ```  ```json - ip: 10.0.0.2   alias_ips: [10.0.0.3, 10.0.0.4]   interface_num: 1   mac_address: 86:00:00:2a:7d:e0   network_id: 1234   network_name: nw-test1   network: 10.0.0.0/8   subnet: 10.0.0.0/24   gateway: 10.0.0.1 - ip: 192.168.0.2   alias_ips: []   interface_num: 2   mac_address: 86:00:00:2a:7d:e1   network_id: 4321   network_name: nw-test2   network: 192.168.0.0/16   subnet: 192.168.0.0/24   gateway: 192.168.0.1 ```  **Example: Availability Zone** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone hel1-dc2 ```  **Example: Region** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/region eu-central ```  ## Sorting Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the `sort` query string parameter. You can sort by multiple fields. You can set the sort direction by appending `:asc` or `:desc` to the field name. By default, ascending sorting is used.  **Example: Sorting** ```bash https://api.hetzner.cloud/v1/actions?sort=status https://api.hetzner.cloud/v1/actions?sort=status:asc https://api.hetzner.cloud/v1/actions?sort=status:desc https://api.hetzner.cloud/v1/actions?sort=status:asc&sort=command:desc ``` 
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
import ActionResponse from '../model/ActionResponse';
import ActionsResponse from '../model/ActionsResponse';
import AddToPlacementGroupRequest from '../model/AddToPlacementGroupRequest';
import AttachToNetworkRequest from '../model/AttachToNetworkRequest';
import CreateImageRequest from '../model/CreateImageRequest';
import DetachFromNetworkRequest from '../model/DetachFromNetworkRequest';
import RebuildServerRequest from '../model/RebuildServerRequest';
import ServersIdActionsAttachIsoPostRequest from '../model/ServersIdActionsAttachIsoPostRequest';
import ServersIdActionsChangeAliasIpsPostRequest from '../model/ServersIdActionsChangeAliasIpsPostRequest';
import ServersIdActionsChangeDnsPtrPostRequest from '../model/ServersIdActionsChangeDnsPtrPostRequest';
import ServersIdActionsChangeProtectionPostRequest from '../model/ServersIdActionsChangeProtectionPostRequest';
import ServersIdActionsChangeTypePostRequest from '../model/ServersIdActionsChangeTypePostRequest';
import ServersIdActionsCreateImagePost201Response from '../model/ServersIdActionsCreateImagePost201Response';
import ServersIdActionsEnableRescuePost201Response from '../model/ServersIdActionsEnableRescuePost201Response';
import ServersIdActionsEnableRescuePostRequest from '../model/ServersIdActionsEnableRescuePostRequest';
import ServersIdActionsRebuildPost201Response from '../model/ServersIdActionsRebuildPost201Response';
import ServersIdActionsRequestConsolePost201Response from '../model/ServersIdActionsRequestConsolePost201Response';

/**
* ServerActions service.
* @module api/ServerActionsApi
* @version 1.0.0
*/
export default class ServerActionsApi {

    /**
    * Constructs a new ServerActionsApi. 
    * @alias module:api/ServerActionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the serversIdActionsActionIdGet operation.
     * @callback module:api/ServerActionsApi~serversIdActionsActionIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get an Action for a Server
     * Returns a specific Action object for a Server.
     * @param {Number} id ID of the Server
     * @param {Number} actionId ID of the Action
     * @param {module:api/ServerActionsApi~serversIdActionsActionIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsActionIdGet(id, actionId, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsActionIdGet");
      }
      // verify the required parameter 'actionId' is set
      if (actionId === undefined || actionId === null) {
        throw new Error("Missing the required parameter 'actionId' when calling serversIdActionsActionIdGet");
      }

      let pathParams = {
        'id': id,
        'action_id': actionId
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
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/{action_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsAddToPlacementGroupPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsAddToPlacementGroupPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a Server to a Placement Group
     * Adds a Server to a Placement Group.  Server must be powered off for this command to succeed.  #### Call specific error codes  | Code                          | Description                                                          | |-------------------------------|----------------------------------------------------------------------| | `server_not_stopped`          | The action requires a stopped server                                 | 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/AddToPlacementGroupRequest} [addToPlacementGroupRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsAddToPlacementGroupPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsAddToPlacementGroupPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['addToPlacementGroupRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsAddToPlacementGroupPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/add_to_placement_group', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsAttachIsoPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsAttachIsoPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Attach an ISO to a Server
     * Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already attached ISO will automatically be detached before the new ISO is attached.  Servers with attached ISOs have a modified boot order: They will try to boot from the ISO first before falling back to hard disk. 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/ServersIdActionsAttachIsoPostRequest} [serversIdActionsAttachIsoPostRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsAttachIsoPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsAttachIsoPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['serversIdActionsAttachIsoPostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsAttachIsoPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/attach_iso', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsAttachToNetworkPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsAttachToNetworkPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Attach a Server to a Network
     * Attaches a Server to a network. This will complement the fixed public Server interface by adding an additional ethernet interface to the Server which is connected to the specified network.  The Server will get an IP auto assigned from a subnet of type `server` in the same `network_zone`.  Using the `alias_ips` attribute you can also define one or more additional IPs to the Servers. Please note that you will have to configure these IPs by hand on your Server since only the primary IP will be given out by DHCP.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | `server_already_attached`        | The server is already attached to the network                         | | `ip_not_available`               | The provided Network IP is not available                              | | `no_subnet_available`            | No Subnet or IP is available for the Server within the network        | | `networks_overlap`               | The network IP range overlaps with one of the server networks         | 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/AttachToNetworkRequest} [attachToNetworkRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsAttachToNetworkPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsAttachToNetworkPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['attachToNetworkRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsAttachToNetworkPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/attach_to_network', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsChangeAliasIpsPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsChangeAliasIpsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change alias IPs of a Network
     * Changes the alias IPs of an already attached Network. Note that the existing aliases for the specified Network will be replaced with these provided in the request body. So if you want to add an alias IP, you have to provide the existing ones from the Network plus the new alias IP in the request body.
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/ServersIdActionsChangeAliasIpsPostRequest} [serversIdActionsChangeAliasIpsPostRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsChangeAliasIpsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsChangeAliasIpsPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['serversIdActionsChangeAliasIpsPostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsChangeAliasIpsPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/change_alias_ips', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsChangeDnsPtrPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsChangeDnsPtrPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change reverse DNS entry for this Server
     * Changes the hostname that will appear when getting the hostname belonging to the primary IPs (IPv4 and IPv6) of this Server.  Floating IPs assigned to the Server are not affected by this. 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/ServersIdActionsChangeDnsPtrPostRequest} [serversIdActionsChangeDnsPtrPostRequest] Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.
     * @param {module:api/ServerActionsApi~serversIdActionsChangeDnsPtrPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsChangeDnsPtrPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['serversIdActionsChangeDnsPtrPostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsChangeDnsPtrPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/change_dns_ptr', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsChangeProtectionPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsChangeProtectionPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change Server Protection
     * Changes the protection configuration of the Server.
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/ServersIdActionsChangeProtectionPostRequest} [serversIdActionsChangeProtectionPostRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsChangeProtectionPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsChangeProtectionPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['serversIdActionsChangeProtectionPostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsChangeProtectionPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/change_protection', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsChangeTypePost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsChangeTypePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change the Type of a Server
     * Changes the type (Cores, RAM and disk sizes) of a Server.  Server must be powered off for this command to succeed.  This copies the content of its disk, and starts it again.  You can only migrate to Server types with the same `storage_type` and equal or bigger disks. Shrinking disks is not possible as it might destroy data.  If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to downgrade the Server type, set `upgrade_disk` to `false`.  #### Call specific error codes  | Code                          | Description                                                          | |-------------------------------|----------------------------------------------------------------------| | `invalid_server_type`         | The server type does not fit for the given server or is deprecated   | | `server_not_stopped`          | The action requires a stopped server                                 | 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/ServersIdActionsChangeTypePostRequest} [serversIdActionsChangeTypePostRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsChangeTypePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsChangeTypePost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['serversIdActionsChangeTypePostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsChangeTypePost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/change_type', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsCreateImagePost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsCreateImagePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServersIdActionsCreateImagePost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create Image from a Server
     * Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates a snapshot of the current state of the disk and copies it into an Image. If the Server is currently running you must make sure that its disk content is consistent. Otherwise, the created Image may not be readable.  To make sure disk content is consistent, we recommend to shut down the Server prior to creating an Image.  You can either create a `backup` Image that is bound to the Server and therefore will be deleted when the Server is deleted, or you can create an `snapshot` Image which is completely independent of the Server it was created from and will survive Server deletion. Backup Images are only available when the backup option is enabled for the Server. Snapshot Images are billed on a per GB basis. 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateImageRequest} [createImageRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsCreateImagePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServersIdActionsCreateImagePost201Response}
     */
    serversIdActionsCreateImagePost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['createImageRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsCreateImagePost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ServersIdActionsCreateImagePost201Response;
      return this.apiClient.callApi(
        '/servers/{id}/actions/create_image', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsDetachFromNetworkPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsDetachFromNetworkPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Detach a Server from a Network
     * Detaches a Server from a network. The interface for this network will vanish.
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/DetachFromNetworkRequest} [detachFromNetworkRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsDetachFromNetworkPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsDetachFromNetworkPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['detachFromNetworkRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsDetachFromNetworkPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/detach_from_network', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsDetachIsoPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsDetachIsoPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Detach an ISO from a Server
     * Detaches an ISO from a Server. In case no ISO Image is attached to the Server, the status of the returned Action is immediately set to `success`
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsDetachIsoPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsDetachIsoPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsDetachIsoPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/detach_iso', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsDisableBackupPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsDisableBackupPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disable Backups for a Server
     * Disables the automatic backup option and deletes all existing Backups for a Server. No more additional charges for backups will be made.  Caution: This immediately removes all existing backups for the Server! 
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsDisableBackupPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsDisableBackupPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsDisableBackupPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/disable_backup', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsDisableRescuePost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsDisableRescuePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disable Rescue Mode for a Server
     * Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on next reboot.  Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.  Disabling rescue mode will not reboot your Server — you will have to do this yourself. 
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsDisableRescuePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsDisableRescuePost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsDisableRescuePost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/disable_rescue', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsEnableBackupPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsEnableBackupPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Enable and Configure Backups for a Server
     * Enables and configures the automatic daily backup option for the Server. Enabling automatic backups will increase the price of the Server by 20%. In return, you will get seven slots where Images of type backup can be stored.  Backups are automatically created daily. 
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsEnableBackupPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsEnableBackupPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsEnableBackupPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/enable_backup', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsEnableRescuePost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsEnableRescuePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServersIdActionsEnableRescuePost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Enable Rescue Mode for a Server
     * Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue mode boots it will start a special minimal Linux distribution designed for repair and reinstall.  In case a Server cannot boot on its own you can use this to access a Server’s disks.  Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.  Enabling rescue mode will not [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server — you will have to do this yourself. 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/ServersIdActionsEnableRescuePostRequest} [serversIdActionsEnableRescuePostRequest] 
     * @param {module:api/ServerActionsApi~serversIdActionsEnableRescuePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServersIdActionsEnableRescuePost201Response}
     */
    serversIdActionsEnableRescuePost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['serversIdActionsEnableRescuePostRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsEnableRescuePost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ServersIdActionsEnableRescuePost201Response;
      return this.apiClient.callApi(
        '/servers/{id}/actions/enable_rescue', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsGet operation.
     * @callback module:api/ServerActionsApi~serversIdActionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get all Actions for a Server
     * Returns all Action objects for a Server. You can `sort` the results by using the sort URI parameter, and filter them with the `status` parameter.
     * @param {Number} id ID of the Resource
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [sort] Can be used multiple times.
     * @param {module:model/String} [status] Can be used multiple times, the response will contain only Actions with specified statuses
     * @param {module:api/ServerActionsApi~serversIdActionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionsResponse}
     */
    serversIdActionsGet(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'sort': opts['sort'],
        'status': opts['status']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ActionsResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsPoweroffPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsPoweroffPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Power off a Server
     * Cuts power to the Server. This forcefully stops it without giving the Server operating system time to gracefully stop. May lead to data loss, equivalent to pulling the power cord. Power off should only be used when shutdown does not work.
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsPoweroffPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsPoweroffPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsPoweroffPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/poweroff', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsPoweronPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsPoweronPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Power on a Server
     * Starts a Server by turning its power on.
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsPoweronPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsPoweronPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsPoweronPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/poweron', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsRebootPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsRebootPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Soft-reboot a Server
     * Reboots a Server gracefully by sending an ACPI request. The Server operating system must support ACPI and react to the request, otherwise the Server will not reboot.
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsRebootPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsRebootPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsRebootPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/reboot', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsRebuildPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsRebuildPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServersIdActionsRebuildPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Rebuild a Server from an Image
     * Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying all data** on the target Server  The Image can either be one you have created earlier (`backup` or `snapshot` Image) or it can be a completely fresh `system` Image provided by us. You can get a list of all available Images with `GET /images`.  Your Server will automatically be powered off before the rebuild command executes. 
     * @param {Number} id ID of the Server
     * @param {Object} opts Optional parameters
     * @param {module:model/RebuildServerRequest} [rebuildServerRequest] To select which Image to rebuild from you can either pass an ID or a name as the `image` argument. Passing a name only works for `system` Images since the other Image types do not have a name set.
     * @param {module:api/ServerActionsApi~serversIdActionsRebuildPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServersIdActionsRebuildPost201Response}
     */
    serversIdActionsRebuildPost(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['rebuildServerRequest'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsRebuildPost");
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ServersIdActionsRebuildPost201Response;
      return this.apiClient.callApi(
        '/servers/{id}/actions/rebuild', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsRemoveFromPlacementGroupPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsRemoveFromPlacementGroupPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove from Placement Group
     * Removes a Server from a Placement Group. 
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsRemoveFromPlacementGroupPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsRemoveFromPlacementGroupPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsRemoveFromPlacementGroupPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/remove_from_placement_group', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsRequestConsolePost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsRequestConsolePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServersIdActionsRequestConsolePost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request Console for a Server
     * Requests credentials for remote access via VNC over websocket to keyboard, monitor, and mouse for a Server. The provided URL is valid for 1 minute, after this period a new url needs to be created to connect to the Server. How long the connection is open after the initial connect is not subject to this timeout.
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsRequestConsolePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServersIdActionsRequestConsolePost201Response}
     */
    serversIdActionsRequestConsolePost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsRequestConsolePost");
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
      let accepts = ['application/json'];
      let returnType = ServersIdActionsRequestConsolePost201Response;
      return this.apiClient.callApi(
        '/servers/{id}/actions/request_console', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsResetPasswordPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsResetPasswordPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServersIdActionsEnableRescuePost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reset root Password of a Server
     * Resets the root password. Only works for Linux systems that are running the qemu guest agent. Server must be powered on (status `running`) in order for this operation to succeed.  This will generate a new password for this Server and return it.  If this does not succeed you can use the rescue system to netboot the Server and manually change your Server password by hand. 
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsResetPasswordPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServersIdActionsEnableRescuePost201Response}
     */
    serversIdActionsResetPasswordPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsResetPasswordPost");
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
      let accepts = ['application/json'];
      let returnType = ServersIdActionsEnableRescuePost201Response;
      return this.apiClient.callApi(
        '/servers/{id}/actions/reset_password', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsResetPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsResetPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Reset a Server
     * Cuts power to a Server and starts it again. This forcefully stops it without giving the Server operating system time to gracefully stop. This may lead to data loss, it’s equivalent to pulling the power cord and plugging it in again. Reset should only be used when reboot does not work.
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsResetPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsResetPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsResetPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/reset', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the serversIdActionsShutdownPost operation.
     * @callback module:api/ServerActionsApi~serversIdActionsShutdownPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Shutdown a Server
     * Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating system must support ACPI and react to the request, otherwise the Server will not shut down.
     * @param {Number} id ID of the Server
     * @param {module:api/ServerActionsApi~serversIdActionsShutdownPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActionResponse}
     */
    serversIdActionsShutdownPost(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling serversIdActionsShutdownPost");
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
      let accepts = ['application/json'];
      let returnType = ActionResponse;
      return this.apiClient.callApi(
        '/servers/{id}/actions/shutdown', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
