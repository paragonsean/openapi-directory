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
import PricingGet200ResponsePricingFloatingIp from './PricingGet200ResponsePricingFloatingIp';
import PricingGet200ResponsePricingFloatingIpsInner from './PricingGet200ResponsePricingFloatingIpsInner';
import PricingGet200ResponsePricingImage from './PricingGet200ResponsePricingImage';
import PricingGet200ResponsePricingLoadBalancerTypesInner from './PricingGet200ResponsePricingLoadBalancerTypesInner';
import PricingGet200ResponsePricingPrimaryIpsInner from './PricingGet200ResponsePricingPrimaryIpsInner';
import PricingGet200ResponsePricingServerBackup from './PricingGet200ResponsePricingServerBackup';
import PricingGet200ResponsePricingServerTypesInner from './PricingGet200ResponsePricingServerTypesInner';
import PricingGet200ResponsePricingTraffic from './PricingGet200ResponsePricingTraffic';
import PricingGet200ResponsePricingVolume from './PricingGet200ResponsePricingVolume';

/**
 * The PricingGet200ResponsePricing model module.
 * @module model/PricingGet200ResponsePricing
 * @version 1.0.0
 */
class PricingGet200ResponsePricing {
    /**
     * Constructs a new <code>PricingGet200ResponsePricing</code>.
     * @alias module:model/PricingGet200ResponsePricing
     * @param currency {String} Currency the returned prices are expressed in, coded according to ISO 4217
     * @param floatingIp {module:model/PricingGet200ResponsePricingFloatingIp} 
     * @param floatingIps {Array.<module:model/PricingGet200ResponsePricingFloatingIpsInner>} Costs of Floating IPs types per Location and type
     * @param image {module:model/PricingGet200ResponsePricingImage} 
     * @param loadBalancerTypes {Array.<module:model/PricingGet200ResponsePricingLoadBalancerTypesInner>} Costs of Load Balancer types per Location and type
     * @param primaryIps {Array.<module:model/PricingGet200ResponsePricingPrimaryIpsInner>} Costs of Primary IPs types per Location
     * @param serverBackup {module:model/PricingGet200ResponsePricingServerBackup} 
     * @param serverTypes {Array.<module:model/PricingGet200ResponsePricingServerTypesInner>} Costs of Server types per Location and type
     * @param traffic {module:model/PricingGet200ResponsePricingTraffic} 
     * @param vatRate {String} The VAT rate used for calculating prices with VAT
     * @param volume {module:model/PricingGet200ResponsePricingVolume} 
     */
    constructor(currency, floatingIp, floatingIps, image, loadBalancerTypes, primaryIps, serverBackup, serverTypes, traffic, vatRate, volume) { 
        
        PricingGet200ResponsePricing.initialize(this, currency, floatingIp, floatingIps, image, loadBalancerTypes, primaryIps, serverBackup, serverTypes, traffic, vatRate, volume);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, currency, floatingIp, floatingIps, image, loadBalancerTypes, primaryIps, serverBackup, serverTypes, traffic, vatRate, volume) { 
        obj['currency'] = currency;
        obj['floating_ip'] = floatingIp;
        obj['floating_ips'] = floatingIps;
        obj['image'] = image;
        obj['load_balancer_types'] = loadBalancerTypes;
        obj['primary_ips'] = primaryIps;
        obj['server_backup'] = serverBackup;
        obj['server_types'] = serverTypes;
        obj['traffic'] = traffic;
        obj['vat_rate'] = vatRate;
        obj['volume'] = volume;
    }

    /**
     * Constructs a <code>PricingGet200ResponsePricing</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PricingGet200ResponsePricing} obj Optional instance to populate.
     * @return {module:model/PricingGet200ResponsePricing} The populated <code>PricingGet200ResponsePricing</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PricingGet200ResponsePricing();

            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('floating_ip')) {
                obj['floating_ip'] = PricingGet200ResponsePricingFloatingIp.constructFromObject(data['floating_ip']);
            }
            if (data.hasOwnProperty('floating_ips')) {
                obj['floating_ips'] = ApiClient.convertToType(data['floating_ips'], [PricingGet200ResponsePricingFloatingIpsInner]);
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = PricingGet200ResponsePricingImage.constructFromObject(data['image']);
            }
            if (data.hasOwnProperty('load_balancer_types')) {
                obj['load_balancer_types'] = ApiClient.convertToType(data['load_balancer_types'], [PricingGet200ResponsePricingLoadBalancerTypesInner]);
            }
            if (data.hasOwnProperty('primary_ips')) {
                obj['primary_ips'] = ApiClient.convertToType(data['primary_ips'], [PricingGet200ResponsePricingPrimaryIpsInner]);
            }
            if (data.hasOwnProperty('server_backup')) {
                obj['server_backup'] = PricingGet200ResponsePricingServerBackup.constructFromObject(data['server_backup']);
            }
            if (data.hasOwnProperty('server_types')) {
                obj['server_types'] = ApiClient.convertToType(data['server_types'], [PricingGet200ResponsePricingServerTypesInner]);
            }
            if (data.hasOwnProperty('traffic')) {
                obj['traffic'] = PricingGet200ResponsePricingTraffic.constructFromObject(data['traffic']);
            }
            if (data.hasOwnProperty('vat_rate')) {
                obj['vat_rate'] = ApiClient.convertToType(data['vat_rate'], 'String');
            }
            if (data.hasOwnProperty('volume')) {
                obj['volume'] = PricingGet200ResponsePricingVolume.constructFromObject(data['volume']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PricingGet200ResponsePricing</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PricingGet200ResponsePricing</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PricingGet200ResponsePricing.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // validate the optional field `floating_ip`
        if (data['floating_ip']) { // data not null
          PricingGet200ResponsePricingFloatingIp.validateJSON(data['floating_ip']);
        }
        if (data['floating_ips']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['floating_ips'])) {
                throw new Error("Expected the field `floating_ips` to be an array in the JSON data but got " + data['floating_ips']);
            }
            // validate the optional field `floating_ips` (array)
            for (const item of data['floating_ips']) {
                PricingGet200ResponsePricingFloatingIpsInner.validateJSON(item);
            };
        }
        // validate the optional field `image`
        if (data['image']) { // data not null
          PricingGet200ResponsePricingImage.validateJSON(data['image']);
        }
        if (data['load_balancer_types']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['load_balancer_types'])) {
                throw new Error("Expected the field `load_balancer_types` to be an array in the JSON data but got " + data['load_balancer_types']);
            }
            // validate the optional field `load_balancer_types` (array)
            for (const item of data['load_balancer_types']) {
                PricingGet200ResponsePricingLoadBalancerTypesInner.validateJSON(item);
            };
        }
        if (data['primary_ips']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['primary_ips'])) {
                throw new Error("Expected the field `primary_ips` to be an array in the JSON data but got " + data['primary_ips']);
            }
            // validate the optional field `primary_ips` (array)
            for (const item of data['primary_ips']) {
                PricingGet200ResponsePricingPrimaryIpsInner.validateJSON(item);
            };
        }
        // validate the optional field `server_backup`
        if (data['server_backup']) { // data not null
          PricingGet200ResponsePricingServerBackup.validateJSON(data['server_backup']);
        }
        if (data['server_types']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['server_types'])) {
                throw new Error("Expected the field `server_types` to be an array in the JSON data but got " + data['server_types']);
            }
            // validate the optional field `server_types` (array)
            for (const item of data['server_types']) {
                PricingGet200ResponsePricingServerTypesInner.validateJSON(item);
            };
        }
        // validate the optional field `traffic`
        if (data['traffic']) { // data not null
          PricingGet200ResponsePricingTraffic.validateJSON(data['traffic']);
        }
        // ensure the json data is a string
        if (data['vat_rate'] && !(typeof data['vat_rate'] === 'string' || data['vat_rate'] instanceof String)) {
            throw new Error("Expected the field `vat_rate` to be a primitive type in the JSON string but got " + data['vat_rate']);
        }
        // validate the optional field `volume`
        if (data['volume']) { // data not null
          PricingGet200ResponsePricingVolume.validateJSON(data['volume']);
        }

        return true;
    }


}

PricingGet200ResponsePricing.RequiredProperties = ["currency", "floating_ip", "floating_ips", "image", "load_balancer_types", "primary_ips", "server_backup", "server_types", "traffic", "vat_rate", "volume"];

/**
 * Currency the returned prices are expressed in, coded according to ISO 4217
 * @member {String} currency
 */
PricingGet200ResponsePricing.prototype['currency'] = undefined;

/**
 * @member {module:model/PricingGet200ResponsePricingFloatingIp} floating_ip
 */
PricingGet200ResponsePricing.prototype['floating_ip'] = undefined;

/**
 * Costs of Floating IPs types per Location and type
 * @member {Array.<module:model/PricingGet200ResponsePricingFloatingIpsInner>} floating_ips
 */
PricingGet200ResponsePricing.prototype['floating_ips'] = undefined;

/**
 * @member {module:model/PricingGet200ResponsePricingImage} image
 */
PricingGet200ResponsePricing.prototype['image'] = undefined;

/**
 * Costs of Load Balancer types per Location and type
 * @member {Array.<module:model/PricingGet200ResponsePricingLoadBalancerTypesInner>} load_balancer_types
 */
PricingGet200ResponsePricing.prototype['load_balancer_types'] = undefined;

/**
 * Costs of Primary IPs types per Location
 * @member {Array.<module:model/PricingGet200ResponsePricingPrimaryIpsInner>} primary_ips
 */
PricingGet200ResponsePricing.prototype['primary_ips'] = undefined;

/**
 * @member {module:model/PricingGet200ResponsePricingServerBackup} server_backup
 */
PricingGet200ResponsePricing.prototype['server_backup'] = undefined;

/**
 * Costs of Server types per Location and type
 * @member {Array.<module:model/PricingGet200ResponsePricingServerTypesInner>} server_types
 */
PricingGet200ResponsePricing.prototype['server_types'] = undefined;

/**
 * @member {module:model/PricingGet200ResponsePricingTraffic} traffic
 */
PricingGet200ResponsePricing.prototype['traffic'] = undefined;

/**
 * The VAT rate used for calculating prices with VAT
 * @member {String} vat_rate
 */
PricingGet200ResponsePricing.prototype['vat_rate'] = undefined;

/**
 * @member {module:model/PricingGet200ResponsePricingVolume} volume
 */
PricingGet200ResponsePricing.prototype['volume'] = undefined;






export default PricingGet200ResponsePricing;

