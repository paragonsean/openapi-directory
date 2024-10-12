/*
 * Hetzner Cloud API
 * This is the official API documentation for the Public Hetzner Cloud.  ## Introduction  The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.  As an alternative to working directly with our API you may also consider to use: * Our CLI program [hcloud](https://github.com/hetznercloud/cli) * Our [library for Go](https://github.com/hetznercloud/hcloud-go) * Our [library for Python](https://github.com/hetznercloud/hcloud-python)  Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).  If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following: * The type of integration you would like to develop * Link to the GitHub repo you will use for the Project * Link to some other Open Source work you have already done (if you have done so)  ## Getting Started To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is `jEheVytlAoFl7F8MqUQ7jAo2hOXASztX`.  You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.haxx.se/).  Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like `servers` inside the example response. A response can also contain a `meta` object with information like [Pagination](https://docs.hetzner.cloud/#overview-pagination).  **Example Request** ```bash curl -H \"Authorization: Bearer jEheVytlAoFl7F8MqUQ7jAo2hOXASztX\" \\     https://api.hetzner.cloud/v1/servers ```  **Example Response** ```json {     \"servers\": [],     \"meta\": {         \"pagination\": {             \"page\": 1,             \"per_page\": 25,             \"previous_page\": null,             \"next_page\": null,             \"last_page\": 1,             \"total_entries\": 0         }     } } ```  ## Authentication All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the `Authorization` HTTP header.  To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token.  **Example Authorization header** ```html Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj ```  ## Errors Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.  The error response contains the following keys:  | Keys      | Meaning                                                               | |-----------|-----------------------------------------------------------------------| | `code`    | Short string indicating the type of error (machine-parsable)          | | `message` | Textual description on what has gone wrong                            | | `details` | An object providing for details on the error (schema depends on code) |  **Example response** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  ### Error Codes  | Code                      | Description                                                                      | |---------------------------|----------------------------------------------------------------------------------| | `forbidden`               | Insufficient permissions for this request                                        | | `invalid_input`           | Error while parsing or processing the input                                      | | `json_error`              | Invalid JSON input in your request                                               | | `locked`                  | The item you are trying to access is locked (there is already an Action running) | | `not_found`               | Entity not found                                                                 | | `rate_limit_exceeded`     | Error when sending too many requests                                             | | `resource_limit_exceeded` | Error when exceeding the maximum quantity of a resource for an account           | | `resource_unavailable`    | The requested resource is currently unavailable                                  | | `service_error`           | Error within a service                                                           | | `uniqueness_error`        | One or more of the objects fields must be unique                                 | | `protected`               | The Action you are trying to start is protected for this resource                | | `maintenance`             | Cannot perform operation due to maintenance                                      | | `conflict`                | The resource has changed during the request, please retry                        | | `unsupported_error`       | The corresponding resource does not support the Action                           | | `token_readonly`          | The token is only allowed to perform GET requests                                | | `unavailable`             | A service or product is currently not available                                  |  **invalid_input** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  **uniqueness_error** ```json {   \"error\": {     \"code\": \"uniqueness_error\",     \"message\": \"SSH key with the same fingerprint already exists\",     \"details\": {       \"fields\": [         {           \"name\": \"public_key\"         }       ]     }   } } ```  **resource_limit_exceeded** ```json {   \"error\": {     \"code\": \"resource_limit_exceeded\",     \"message\": \"project limit exceeded\",     \"details\": {       \"limits\": [         {           \"name\": \"project_limit\"         }       ]     }   } } ```  ## Labels Labels are `key/value` pairs that can be attached to all resources.  Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).  Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.  The `hetzner.cloud/` prefix is reserved and cannot be used.  **Example Labels** ```json {   \"labels\": {     \"environment\":\"development\",     \"service\":\"backend\",     \"example.com/my\":\"label\",     \"just-a-key\":\"\"   } } ```  ## Label Selector For resources with labels, you can filter resources by their labels using the label selector query language.  | Expression           | Meaning                                                             | |----------------------|---------------------------------------------------------------------| | `k==v` / `k=v`       | Value of key `k` does equal value `v`                               | | `k!=v`               | Value of key `k` does not equal value `v`                           | | `k`                  | Key `k` is present                                                  | | `!k`                 | Key `k` is not present                                              | | `k in (v1,v2,v3)`    | Value of key `k` is `v1`, `v2`, or `v3`                             | | `k notin (v1,v2,v3)` | Value of key `k` is neither `v1`, nor `v2`, nor `v3`                | | `k1==v,!k2`          | Value of key `k1` is `v` and key `k2` is not present                |  ### Examples * Returns all resources that have a `env=production` label and that don't have a `type=database` label:    `env=production,type!=database` * Returns all resources that have a `env=testing` or `env=staging` label:      `env in (testing,staging)` * Returns all resources that don't have a `type` label:      `!type`  ## Pagination Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:  * A `page` parameter specifies the page to fetch. The number of the first page is 1. * A `per_page` parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.  Responses contain a `Link` header with pagination information.  Additionally, if the response body is JSON and the root object is an object, that object has a `pagination` object inside the `meta` object with pagination information:  **Example Pagination** ```json {     \"servers\": [...],     \"meta\": {         \"pagination\": {             \"page\": 2,             \"per_page\": 25,             \"previous_page\": 1,             \"next_page\": 3,             \"last_page\": 4,             \"total_entries\": 100         }     } } ```  The keys `previous_page`, `next_page`, `last_page`, and `total_entries` may be `null` when on the first page, last page, or when the total number of entries is unknown.  **Example Pagination Link header** ```bash Link: <https://api.hetzner.cloud/v1/actions?page=2&per_page=5>; rel=\"prev\",       <https://api.hetzner.cloud/v1/actions?page=4&per_page=5>; rel=\"next\",       <https://api.hetzner.cloud/v1/actions?page=6&per_page=5>; rel=\"last\" ```  Line breaks have been added for display purposes only and responses may only contain some of the above `rel` values.  ## Rate Limiting All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a `429 Too Many Requests` error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.  * The `RateLimit-Limit` header contains the total number of requests you can perform per hour. * The `RateLimit-Remaining` header contains the number of requests remaining in the current rate limit time frame. * The `RateLimit-Reset` header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.  The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.  ## Server Metadata Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:  | Data              | Format | Contents                                                     | |-------------------|--------|--------------------------------------------------------------| | hostname          | text   | Name of the Server as set in the api                         | | instance-id       | number | ID of the server                                             | | public-ipv4       | text   | Primary public IPv4 address                                  | | private-networks  | yaml   | Details about the private networks the Server is attached to | | availability-zone | text   | Name of the availability zone that Server runs in            | | region            | text   | Network zone, e.g. eu-central                                |  **Example: Summary** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata ```  ```yaml availability-zone: hel1-dc2 hostname: my-server instance-id: 42 public-ipv4: 1.2.3.4 region: eu-central ```  **Example: Hostname** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/hostname my-server ```  **Example: Instance ID** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/instance-id 42 ```  **Example: Public IPv4** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4 1.2.3.4 ```  **Example: Private Networks** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/private-networks ```  ```json - ip: 10.0.0.2   alias_ips: [10.0.0.3, 10.0.0.4]   interface_num: 1   mac_address: 86:00:00:2a:7d:e0   network_id: 1234   network_name: nw-test1   network: 10.0.0.0/8   subnet: 10.0.0.0/24   gateway: 10.0.0.1 - ip: 192.168.0.2   alias_ips: []   interface_num: 2   mac_address: 86:00:00:2a:7d:e1   network_id: 4321   network_name: nw-test2   network: 192.168.0.0/16   subnet: 192.168.0.0/24   gateway: 192.168.0.1 ```  **Example: Availability Zone** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone hel1-dc2 ```  **Example: Region** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/region eu-central ```  ## Sorting Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the `sort` query string parameter. You can sort by multiple fields. You can set the sort direction by appending `:asc` or `:desc` to the field name. By default, ascending sorting is used.  **Example: Sorting** ```bash https://api.hetzner.cloud/v1/actions?sort=status https://api.hetzner.cloud/v1/actions?sort=status:asc https://api.hetzner.cloud/v1/actions?sort=status:desc https://api.hetzner.cloud/v1/actions?sort=status:asc&sort=command:desc ``` 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ActionResponse;
import org.openapitools.client.model.ActionsResponse;
import org.openapitools.client.model.AddTargetRequest;
import org.openapitools.client.model.ChangeLoadbalancerDnsPtrRequest;
import org.openapitools.client.model.ChangeTypeRequest;
import org.openapitools.client.model.LoadBalancerService;
import org.openapitools.client.model.LoadBalancersIdActionsAttachToNetworkPostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsChangeAlgorithmPostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsChangeProtectionPostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsDeleteServicePostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsDetachFromNetworkPostRequest;
import org.openapitools.client.model.RemoveTargetRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LoadBalancerActionsApi
 */
@Disabled
public class LoadBalancerActionsApiTest {

    private final LoadBalancerActionsApi api = new LoadBalancerActionsApi();

    /**
     * Get an Action for a Load Balancer
     *
     * Returns a specific Action for a Load Balancer.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsActionIdGetTest() throws ApiException {
        Integer id = null;
        Integer actionId = null;
        ActionResponse response = api.loadBalancersIdActionsActionIdGet(id, actionId);
        // TODO: test validations
    }

    /**
     * Add Service
     *
     * Adds a service to a Load Balancer.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsAddServicePostTest() throws ApiException {
        Integer id = null;
        LoadBalancerService loadBalancerService = null;
        ActionResponse response = api.loadBalancersIdActionsAddServicePost(id, loadBalancerService);
        // TODO: test validations
    }

    /**
     * Add Target
     *
     * Adds a target to a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP you are trying to add as a target is not owned by the Project owner                            | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsAddTargetPostTest() throws ApiException {
        Integer id = null;
        AddTargetRequest addTargetRequest = null;
        ActionResponse response = api.loadBalancersIdActionsAddTargetPost(id, addTargetRequest);
        // TODO: test validations
    }

    /**
     * Attach a Load Balancer to a Network
     *
     * Attach a Load Balancer to a Network.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;load_balancer_already_attached&#x60; | The Load Balancer is already attached to a network                    | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Load Balancer within the network | 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsAttachToNetworkPostTest() throws ApiException {
        Integer id = null;
        LoadBalancersIdActionsAttachToNetworkPostRequest loadBalancersIdActionsAttachToNetworkPostRequest = null;
        ActionResponse response = api.loadBalancersIdActionsAttachToNetworkPost(id, loadBalancersIdActionsAttachToNetworkPostRequest);
        // TODO: test validations
    }

    /**
     * Change Algorithm
     *
     * Change the algorithm that determines to which target new requests are sent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsChangeAlgorithmPostTest() throws ApiException {
        Integer id = null;
        LoadBalancersIdActionsChangeAlgorithmPostRequest loadBalancersIdActionsChangeAlgorithmPostRequest = null;
        ActionResponse response = api.loadBalancersIdActionsChangeAlgorithmPost(id, loadBalancersIdActionsChangeAlgorithmPostRequest);
        // TODO: test validations
    }

    /**
     * Change reverse DNS entry for this Load Balancer
     *
     * Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.  Floating IPs assigned to the Server are not affected by this. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsChangeDnsPtrPostTest() throws ApiException {
        Integer id = null;
        ChangeLoadbalancerDnsPtrRequest changeLoadbalancerDnsPtrRequest = null;
        ActionResponse response = api.loadBalancersIdActionsChangeDnsPtrPost(id, changeLoadbalancerDnsPtrRequest);
        // TODO: test validations
    }

    /**
     * Change Load Balancer Protection
     *
     * Changes the protection configuration of a Load Balancer.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsChangeProtectionPostTest() throws ApiException {
        Integer id = null;
        LoadBalancersIdActionsChangeProtectionPostRequest loadBalancersIdActionsChangeProtectionPostRequest = null;
        ActionResponse response = api.loadBalancersIdActionsChangeProtectionPost(id, loadBalancersIdActionsChangeProtectionPostRequest);
        // TODO: test validations
    }

    /**
     * Change the Type of a Load Balancer
     *
     * Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.  **Call specific error codes**  | Code                         | Description                                                     | |------------------------------|-----------------------------------------------------------------| | &#x60;invalid_load_balancer_type&#x60; | The Load Balancer type does not fit for the given Load Balancer | 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsChangeTypePostTest() throws ApiException {
        Integer id = null;
        ChangeTypeRequest changeTypeRequest = null;
        ActionResponse response = api.loadBalancersIdActionsChangeTypePost(id, changeTypeRequest);
        // TODO: test validations
    }

    /**
     * Delete Service
     *
     * Delete a service of a Load Balancer.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsDeleteServicePostTest() throws ApiException {
        Integer id = null;
        LoadBalancersIdActionsDeleteServicePostRequest loadBalancersIdActionsDeleteServicePostRequest = null;
        ActionResponse response = api.loadBalancersIdActionsDeleteServicePost(id, loadBalancersIdActionsDeleteServicePostRequest);
        // TODO: test validations
    }

    /**
     * Detach a Load Balancer from a Network
     *
     * Detaches a Load Balancer from a network.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsDetachFromNetworkPostTest() throws ApiException {
        Integer id = null;
        LoadBalancersIdActionsDetachFromNetworkPostRequest loadBalancersIdActionsDetachFromNetworkPostRequest = null;
        ActionResponse response = api.loadBalancersIdActionsDetachFromNetworkPost(id, loadBalancersIdActionsDetachFromNetworkPostRequest);
        // TODO: test validations
    }

    /**
     * Disable the public interface of a Load Balancer
     *
     * Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.  #### Call specific error codes  | Code                                      | Description                                                                    | |-------------------------------------------|--------------------------------------------------------------------------------| | &#x60;load_balancer_not_attached_to_network&#x60;   |  The Load Balancer is not attached to a network                                | | &#x60;targets_without_use_private_ip&#x60;          | The Load Balancer has targets that use the public IP instead of the private IP | 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsDisablePublicInterfacePostTest() throws ApiException {
        Integer id = null;
        ActionResponse response = api.loadBalancersIdActionsDisablePublicInterfacePost(id);
        // TODO: test validations
    }

    /**
     * Enable the public interface of a Load Balancer
     *
     * Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsEnablePublicInterfacePostTest() throws ApiException {
        Integer id = null;
        ActionResponse response = api.loadBalancersIdActionsEnablePublicInterfacePost(id);
        // TODO: test validations
    }

    /**
     * Get all Actions for a Load Balancer
     *
     * Returns all Action objects for a Load Balancer. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsGetTest() throws ApiException {
        Integer id = null;
        String sort = null;
        String status = null;
        ActionsResponse response = api.loadBalancersIdActionsGet(id, sort, status);
        // TODO: test validations
    }

    /**
     * Remove Target
     *
     * Removes a target from a Load Balancer.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsRemoveTargetPostTest() throws ApiException {
        Integer id = null;
        RemoveTargetRequest removeTargetRequest = null;
        ActionResponse response = api.loadBalancersIdActionsRemoveTargetPost(id, removeTargetRequest);
        // TODO: test validations
    }

    /**
     * Update Service
     *
     * Updates a Load Balancer Service.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void loadBalancersIdActionsUpdateServicePostTest() throws ApiException {
        Integer id = null;
        LoadBalancerService loadBalancerService = null;
        ActionResponse response = api.loadBalancersIdActionsUpdateServicePost(id, loadBalancerService);
        // TODO: test validations
    }

}
