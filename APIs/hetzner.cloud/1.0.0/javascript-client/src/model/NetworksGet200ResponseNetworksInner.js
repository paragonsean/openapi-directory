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

import ApiClient from '../ApiClient';
import NetworksGet200ResponseNetworksInnerProtection from './NetworksGet200ResponseNetworksInnerProtection';
import NetworksGet200ResponseNetworksInnerRoutesInner from './NetworksGet200ResponseNetworksInnerRoutesInner';
import NetworksGet200ResponseNetworksInnerSubnetsInner from './NetworksGet200ResponseNetworksInnerSubnetsInner';

/**
 * The NetworksGet200ResponseNetworksInner model module.
 * @module model/NetworksGet200ResponseNetworksInner
 * @version 1.0.0
 */
class NetworksGet200ResponseNetworksInner {
    /**
     * Constructs a new <code>NetworksGet200ResponseNetworksInner</code>.
     * @alias module:model/NetworksGet200ResponseNetworksInner
     * @param created {String} Point in time when the Network was created (in ISO-8601 format)
     * @param id {Number} ID of the Network
     * @param ipRange {String} IPv4 prefix of the whole Network
     * @param labels {Object} User-defined labels (key-value pairs)
     * @param name {String} Name of the Network
     * @param protection {module:model/NetworksGet200ResponseNetworksInnerProtection} 
     * @param routes {Array.<module:model/NetworksGet200ResponseNetworksInnerRoutesInner>} Array of routes set in this Network
     * @param servers {Array.<Number>} Array of IDs of Servers attached to this Network
     * @param subnets {Array.<module:model/NetworksGet200ResponseNetworksInnerSubnetsInner>} Array subnets allocated in this Network
     */
    constructor(created, id, ipRange, labels, name, protection, routes, servers, subnets) { 
        
        NetworksGet200ResponseNetworksInner.initialize(this, created, id, ipRange, labels, name, protection, routes, servers, subnets);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, created, id, ipRange, labels, name, protection, routes, servers, subnets) { 
        obj['created'] = created;
        obj['id'] = id;
        obj['ip_range'] = ipRange;
        obj['labels'] = labels;
        obj['name'] = name;
        obj['protection'] = protection;
        obj['routes'] = routes;
        obj['servers'] = servers;
        obj['subnets'] = subnets;
    }

    /**
     * Constructs a <code>NetworksGet200ResponseNetworksInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NetworksGet200ResponseNetworksInner} obj Optional instance to populate.
     * @return {module:model/NetworksGet200ResponseNetworksInner} The populated <code>NetworksGet200ResponseNetworksInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NetworksGet200ResponseNetworksInner();

            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('ip_range')) {
                obj['ip_range'] = ApiClient.convertToType(data['ip_range'], 'String');
            }
            if (data.hasOwnProperty('labels')) {
                obj['labels'] = ApiClient.convertToType(data['labels'], Object);
            }
            if (data.hasOwnProperty('load_balancers')) {
                obj['load_balancers'] = ApiClient.convertToType(data['load_balancers'], ['Number']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('protection')) {
                obj['protection'] = NetworksGet200ResponseNetworksInnerProtection.constructFromObject(data['protection']);
            }
            if (data.hasOwnProperty('routes')) {
                obj['routes'] = ApiClient.convertToType(data['routes'], [NetworksGet200ResponseNetworksInnerRoutesInner]);
            }
            if (data.hasOwnProperty('servers')) {
                obj['servers'] = ApiClient.convertToType(data['servers'], ['Number']);
            }
            if (data.hasOwnProperty('subnets')) {
                obj['subnets'] = ApiClient.convertToType(data['subnets'], [NetworksGet200ResponseNetworksInnerSubnetsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NetworksGet200ResponseNetworksInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NetworksGet200ResponseNetworksInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NetworksGet200ResponseNetworksInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['created'] && !(typeof data['created'] === 'string' || data['created'] instanceof String)) {
            throw new Error("Expected the field `created` to be a primitive type in the JSON string but got " + data['created']);
        }
        // ensure the json data is a string
        if (data['ip_range'] && !(typeof data['ip_range'] === 'string' || data['ip_range'] instanceof String)) {
            throw new Error("Expected the field `ip_range` to be a primitive type in the JSON string but got " + data['ip_range']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['load_balancers'])) {
            throw new Error("Expected the field `load_balancers` to be an array in the JSON data but got " + data['load_balancers']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `protection`
        if (data['protection']) { // data not null
          NetworksGet200ResponseNetworksInnerProtection.validateJSON(data['protection']);
        }
        if (data['routes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['routes'])) {
                throw new Error("Expected the field `routes` to be an array in the JSON data but got " + data['routes']);
            }
            // validate the optional field `routes` (array)
            for (const item of data['routes']) {
                NetworksGet200ResponseNetworksInnerRoutesInner.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['servers'])) {
            throw new Error("Expected the field `servers` to be an array in the JSON data but got " + data['servers']);
        }
        if (data['subnets']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['subnets'])) {
                throw new Error("Expected the field `subnets` to be an array in the JSON data but got " + data['subnets']);
            }
            // validate the optional field `subnets` (array)
            for (const item of data['subnets']) {
                NetworksGet200ResponseNetworksInnerSubnetsInner.validateJSON(item);
            };
        }

        return true;
    }


}

NetworksGet200ResponseNetworksInner.RequiredProperties = ["created", "id", "ip_range", "labels", "name", "protection", "routes", "servers", "subnets"];

/**
 * Point in time when the Network was created (in ISO-8601 format)
 * @member {String} created
 */
NetworksGet200ResponseNetworksInner.prototype['created'] = undefined;

/**
 * ID of the Network
 * @member {Number} id
 */
NetworksGet200ResponseNetworksInner.prototype['id'] = undefined;

/**
 * IPv4 prefix of the whole Network
 * @member {String} ip_range
 */
NetworksGet200ResponseNetworksInner.prototype['ip_range'] = undefined;

/**
 * User-defined labels (key-value pairs)
 * @member {Object} labels
 */
NetworksGet200ResponseNetworksInner.prototype['labels'] = undefined;

/**
 * Array of IDs of Load Balancers attached to this Network
 * @member {Array.<Number>} load_balancers
 */
NetworksGet200ResponseNetworksInner.prototype['load_balancers'] = undefined;

/**
 * Name of the Network
 * @member {String} name
 */
NetworksGet200ResponseNetworksInner.prototype['name'] = undefined;

/**
 * @member {module:model/NetworksGet200ResponseNetworksInnerProtection} protection
 */
NetworksGet200ResponseNetworksInner.prototype['protection'] = undefined;

/**
 * Array of routes set in this Network
 * @member {Array.<module:model/NetworksGet200ResponseNetworksInnerRoutesInner>} routes
 */
NetworksGet200ResponseNetworksInner.prototype['routes'] = undefined;

/**
 * Array of IDs of Servers attached to this Network
 * @member {Array.<Number>} servers
 */
NetworksGet200ResponseNetworksInner.prototype['servers'] = undefined;

/**
 * Array subnets allocated in this Network
 * @member {Array.<module:model/NetworksGet200ResponseNetworksInnerSubnetsInner>} subnets
 */
NetworksGet200ResponseNetworksInner.prototype['subnets'] = undefined;






export default NetworksGet200ResponseNetworksInner;

