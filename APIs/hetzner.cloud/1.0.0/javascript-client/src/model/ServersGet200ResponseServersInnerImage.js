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
import FloatingIpsGet200ResponseFloatingIpsInnerProtection from './FloatingIpsGet200ResponseFloatingIpsInnerProtection';
import ImagesGet200ResponseImagesInnerCreatedFrom from './ImagesGet200ResponseImagesInnerCreatedFrom';

/**
 * The ServersGet200ResponseServersInnerImage model module.
 * @module model/ServersGet200ResponseServersInnerImage
 * @version 1.0.0
 */
class ServersGet200ResponseServersInnerImage {
    /**
     * Constructs a new <code>ServersGet200ResponseServersInnerImage</code>.
     * @alias module:model/ServersGet200ResponseServersInnerImage
     * @param boundTo {Number} ID of Server the Image is bound to. Only set for Images of type `backup`.
     * @param created {String} Point in time when the Resource was created (in ISO-8601 format)
     * @param createdFrom {module:model/ImagesGet200ResponseImagesInnerCreatedFrom} 
     * @param deleted {String} Point in time where the Image was deleted (in ISO-8601 format)
     * @param deprecated {String} Point in time when the Image is considered to be deprecated (in ISO-8601 format)
     * @param description {String} Description of the Image
     * @param diskSize {Number} Size of the disk contained in the Image in GB
     * @param id {Number} ID of the Resource
     * @param imageSize {Number} Size of the Image file in our storage in GB. For snapshot Images this is the value relevant for calculating costs for the Image.
     * @param labels {Object.<String, String>} User-defined labels (key-value pairs)
     * @param name {String} Unique identifier of the Image. This value is only set for system Images.
     * @param osFlavor {module:model/ServersGet200ResponseServersInnerImage.OsFlavorEnum} Flavor of operating system contained in the Image
     * @param osVersion {String} Operating system version
     * @param protection {module:model/FloatingIpsGet200ResponseFloatingIpsInnerProtection} 
     * @param status {module:model/ServersGet200ResponseServersInnerImage.StatusEnum} Whether the Image can be used or if it's still being created or unavailable
     * @param type {module:model/ServersGet200ResponseServersInnerImage.TypeEnum} Type of the Image
     */
    constructor(boundTo, created, createdFrom, deleted, deprecated, description, diskSize, id, imageSize, labels, name, osFlavor, osVersion, protection, status, type) { 
        
        ServersGet200ResponseServersInnerImage.initialize(this, boundTo, created, createdFrom, deleted, deprecated, description, diskSize, id, imageSize, labels, name, osFlavor, osVersion, protection, status, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, boundTo, created, createdFrom, deleted, deprecated, description, diskSize, id, imageSize, labels, name, osFlavor, osVersion, protection, status, type) { 
        obj['bound_to'] = boundTo;
        obj['created'] = created;
        obj['created_from'] = createdFrom;
        obj['deleted'] = deleted;
        obj['deprecated'] = deprecated;
        obj['description'] = description;
        obj['disk_size'] = diskSize;
        obj['id'] = id;
        obj['image_size'] = imageSize;
        obj['labels'] = labels;
        obj['name'] = name;
        obj['os_flavor'] = osFlavor;
        obj['os_version'] = osVersion;
        obj['protection'] = protection;
        obj['status'] = status;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>ServersGet200ResponseServersInnerImage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServersGet200ResponseServersInnerImage} obj Optional instance to populate.
     * @return {module:model/ServersGet200ResponseServersInnerImage} The populated <code>ServersGet200ResponseServersInnerImage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServersGet200ResponseServersInnerImage();

            if (data.hasOwnProperty('bound_to')) {
                obj['bound_to'] = ApiClient.convertToType(data['bound_to'], 'Number');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'String');
            }
            if (data.hasOwnProperty('created_from')) {
                obj['created_from'] = ImagesGet200ResponseImagesInnerCreatedFrom.constructFromObject(data['created_from']);
            }
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'String');
            }
            if (data.hasOwnProperty('deprecated')) {
                obj['deprecated'] = ApiClient.convertToType(data['deprecated'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('disk_size')) {
                obj['disk_size'] = ApiClient.convertToType(data['disk_size'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('image_size')) {
                obj['image_size'] = ApiClient.convertToType(data['image_size'], 'Number');
            }
            if (data.hasOwnProperty('labels')) {
                obj['labels'] = ApiClient.convertToType(data['labels'], {'String': 'String'});
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('os_flavor')) {
                obj['os_flavor'] = ApiClient.convertToType(data['os_flavor'], 'String');
            }
            if (data.hasOwnProperty('os_version')) {
                obj['os_version'] = ApiClient.convertToType(data['os_version'], 'String');
            }
            if (data.hasOwnProperty('protection')) {
                obj['protection'] = FloatingIpsGet200ResponseFloatingIpsInnerProtection.constructFromObject(data['protection']);
            }
            if (data.hasOwnProperty('rapid_deploy')) {
                obj['rapid_deploy'] = ApiClient.convertToType(data['rapid_deploy'], 'Boolean');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServersGet200ResponseServersInnerImage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServersGet200ResponseServersInnerImage</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ServersGet200ResponseServersInnerImage.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['created'] && !(typeof data['created'] === 'string' || data['created'] instanceof String)) {
            throw new Error("Expected the field `created` to be a primitive type in the JSON string but got " + data['created']);
        }
        // validate the optional field `created_from`
        if (data['created_from']) { // data not null
          ImagesGet200ResponseImagesInnerCreatedFrom.validateJSON(data['created_from']);
        }
        // ensure the json data is a string
        if (data['deleted'] && !(typeof data['deleted'] === 'string' || data['deleted'] instanceof String)) {
            throw new Error("Expected the field `deleted` to be a primitive type in the JSON string but got " + data['deleted']);
        }
        // ensure the json data is a string
        if (data['deprecated'] && !(typeof data['deprecated'] === 'string' || data['deprecated'] instanceof String)) {
            throw new Error("Expected the field `deprecated` to be a primitive type in the JSON string but got " + data['deprecated']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['os_flavor'] && !(typeof data['os_flavor'] === 'string' || data['os_flavor'] instanceof String)) {
            throw new Error("Expected the field `os_flavor` to be a primitive type in the JSON string but got " + data['os_flavor']);
        }
        // ensure the json data is a string
        if (data['os_version'] && !(typeof data['os_version'] === 'string' || data['os_version'] instanceof String)) {
            throw new Error("Expected the field `os_version` to be a primitive type in the JSON string but got " + data['os_version']);
        }
        // validate the optional field `protection`
        if (data['protection']) { // data not null
          FloatingIpsGet200ResponseFloatingIpsInnerProtection.validateJSON(data['protection']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

ServersGet200ResponseServersInnerImage.RequiredProperties = ["bound_to", "created", "created_from", "deleted", "deprecated", "description", "disk_size", "id", "image_size", "labels", "name", "os_flavor", "os_version", "protection", "status", "type"];

/**
 * ID of Server the Image is bound to. Only set for Images of type `backup`.
 * @member {Number} bound_to
 */
ServersGet200ResponseServersInnerImage.prototype['bound_to'] = undefined;

/**
 * Point in time when the Resource was created (in ISO-8601 format)
 * @member {String} created
 */
ServersGet200ResponseServersInnerImage.prototype['created'] = undefined;

/**
 * @member {module:model/ImagesGet200ResponseImagesInnerCreatedFrom} created_from
 */
ServersGet200ResponseServersInnerImage.prototype['created_from'] = undefined;

/**
 * Point in time where the Image was deleted (in ISO-8601 format)
 * @member {String} deleted
 */
ServersGet200ResponseServersInnerImage.prototype['deleted'] = undefined;

/**
 * Point in time when the Image is considered to be deprecated (in ISO-8601 format)
 * @member {String} deprecated
 */
ServersGet200ResponseServersInnerImage.prototype['deprecated'] = undefined;

/**
 * Description of the Image
 * @member {String} description
 */
ServersGet200ResponseServersInnerImage.prototype['description'] = undefined;

/**
 * Size of the disk contained in the Image in GB
 * @member {Number} disk_size
 */
ServersGet200ResponseServersInnerImage.prototype['disk_size'] = undefined;

/**
 * ID of the Resource
 * @member {Number} id
 */
ServersGet200ResponseServersInnerImage.prototype['id'] = undefined;

/**
 * Size of the Image file in our storage in GB. For snapshot Images this is the value relevant for calculating costs for the Image.
 * @member {Number} image_size
 */
ServersGet200ResponseServersInnerImage.prototype['image_size'] = undefined;

/**
 * User-defined labels (key-value pairs)
 * @member {Object.<String, String>} labels
 */
ServersGet200ResponseServersInnerImage.prototype['labels'] = undefined;

/**
 * Unique identifier of the Image. This value is only set for system Images.
 * @member {String} name
 */
ServersGet200ResponseServersInnerImage.prototype['name'] = undefined;

/**
 * Flavor of operating system contained in the Image
 * @member {module:model/ServersGet200ResponseServersInnerImage.OsFlavorEnum} os_flavor
 */
ServersGet200ResponseServersInnerImage.prototype['os_flavor'] = undefined;

/**
 * Operating system version
 * @member {String} os_version
 */
ServersGet200ResponseServersInnerImage.prototype['os_version'] = undefined;

/**
 * @member {module:model/FloatingIpsGet200ResponseFloatingIpsInnerProtection} protection
 */
ServersGet200ResponseServersInnerImage.prototype['protection'] = undefined;

/**
 * Indicates that rapid deploy of the Image is available
 * @member {Boolean} rapid_deploy
 */
ServersGet200ResponseServersInnerImage.prototype['rapid_deploy'] = undefined;

/**
 * Whether the Image can be used or if it's still being created or unavailable
 * @member {module:model/ServersGet200ResponseServersInnerImage.StatusEnum} status
 */
ServersGet200ResponseServersInnerImage.prototype['status'] = undefined;

/**
 * Type of the Image
 * @member {module:model/ServersGet200ResponseServersInnerImage.TypeEnum} type
 */
ServersGet200ResponseServersInnerImage.prototype['type'] = undefined;





/**
 * Allowed values for the <code>os_flavor</code> property.
 * @enum {String}
 * @readonly
 */
ServersGet200ResponseServersInnerImage['OsFlavorEnum'] = {

    /**
     * value: "ubuntu"
     * @const
     */
    "ubuntu": "ubuntu",

    /**
     * value: "centos"
     * @const
     */
    "centos": "centos",

    /**
     * value: "debian"
     * @const
     */
    "debian": "debian",

    /**
     * value: "fedora"
     * @const
     */
    "fedora": "fedora",

    /**
     * value: "unknown"
     * @const
     */
    "unknown": "unknown"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
ServersGet200ResponseServersInnerImage['StatusEnum'] = {

    /**
     * value: "available"
     * @const
     */
    "available": "available",

    /**
     * value: "creating"
     * @const
     */
    "creating": "creating",

    /**
     * value: "unavailable"
     * @const
     */
    "unavailable": "unavailable"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
ServersGet200ResponseServersInnerImage['TypeEnum'] = {

    /**
     * value: "system"
     * @const
     */
    "system": "system",

    /**
     * value: "app"
     * @const
     */
    "app": "app",

    /**
     * value: "snapshot"
     * @const
     */
    "snapshot": "snapshot",

    /**
     * value: "backup"
     * @const
     */
    "backup": "backup",

    /**
     * value: "temporary"
     * @const
     */
    "temporary": "temporary"
};



export default ServersGet200ResponseServersInnerImage;

