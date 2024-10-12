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


import ApiClient from './ApiClient';
import Action from './model/Action';
import ActionError from './model/ActionError';
import ActionResourcesInner from './model/ActionResourcesInner';
import ActionResponse from './model/ActionResponse';
import ActionsResponse from './model/ActionsResponse';
import ActionsResponseMeta from './model/ActionsResponseMeta';
import ActionsResponseMetaPagination from './model/ActionsResponseMetaPagination';
import AddDeleteRouteRequest from './model/AddDeleteRouteRequest';
import AddSubnetRequest from './model/AddSubnetRequest';
import AddTargetRequest from './model/AddTargetRequest';
import AddTargetRequestLabelSelector from './model/AddTargetRequestLabelSelector';
import AddTargetRequestServer from './model/AddTargetRequestServer';
import AddToPlacementGroupRequest from './model/AddToPlacementGroupRequest';
import ApplyToResourcesRequest from './model/ApplyToResourcesRequest';
import AssignFloatingIPRequest from './model/AssignFloatingIPRequest';
import AssignPrimaryIPRequest from './model/AssignPrimaryIPRequest';
import AttachToNetworkRequest from './model/AttachToNetworkRequest';
import AttachVolumeRequest from './model/AttachVolumeRequest';
import Certificate from './model/Certificate';
import CertificateResponse from './model/CertificateResponse';
import CertificateStatus from './model/CertificateStatus';
import CertificateStatusError from './model/CertificateStatusError';
import CertificateUsedByInner from './model/CertificateUsedByInner';
import CertificatesResponse from './model/CertificatesResponse';
import ChangeDNSPTRRequest from './model/ChangeDNSPTRRequest';
import ChangeIPRangeRequest from './model/ChangeIPRangeRequest';
import ChangeLoadbalancerDnsPtrRequest from './model/ChangeLoadbalancerDnsPtrRequest';
import ChangeProtectionRequest from './model/ChangeProtectionRequest';
import ChangeProtectionRequest1 from './model/ChangeProtectionRequest1';
import ChangeProtectionRequest2 from './model/ChangeProtectionRequest2';
import ChangeTypeRequest from './model/ChangeTypeRequest';
import CreateCertificateRequest from './model/CreateCertificateRequest';
import CreateCertificateResponse from './model/CreateCertificateResponse';
import CreateFirewallRequest from './model/CreateFirewallRequest';
import CreateFirewallRequestApplyToInner from './model/CreateFirewallRequestApplyToInner';
import CreateFirewallRequestApplyToInnerLabelSelector from './model/CreateFirewallRequestApplyToInnerLabelSelector';
import CreateFirewallRequestApplyToInnerServer from './model/CreateFirewallRequestApplyToInnerServer';
import CreateFirewallResponse from './model/CreateFirewallResponse';
import CreateFloatingIPRequest from './model/CreateFloatingIPRequest';
import CreateImageRequest from './model/CreateImageRequest';
import CreateLoadBalancerRequest from './model/CreateLoadBalancerRequest';
import CreateLoadBalancerRequestLabels from './model/CreateLoadBalancerRequestLabels';
import CreateNetworkRequest from './model/CreateNetworkRequest';
import CreateNetworkRequestSubnetsInner from './model/CreateNetworkRequestSubnetsInner';
import CreatePlacementGroupRequest from './model/CreatePlacementGroupRequest';
import CreatePlacementGroupResponse from './model/CreatePlacementGroupResponse';
import CreatePrimaryIPRequest from './model/CreatePrimaryIPRequest';
import CreatePrimaryIPResponse from './model/CreatePrimaryIPResponse';
import CreateServerRequest from './model/CreateServerRequest';
import CreateServerRequestFirewallsInner from './model/CreateServerRequestFirewallsInner';
import CreateServerRequestPublicNet from './model/CreateServerRequestPublicNet';
import CreateServerResponse from './model/CreateServerResponse';
import CreateVolumeRequest from './model/CreateVolumeRequest';
import DatacentersGet200Response from './model/DatacentersGet200Response';
import DatacentersGet200ResponseDatacentersInner from './model/DatacentersGet200ResponseDatacentersInner';
import DatacentersGet200ResponseDatacentersInnerLocation from './model/DatacentersGet200ResponseDatacentersInnerLocation';
import DatacentersGet200ResponseDatacentersInnerServerTypes from './model/DatacentersGet200ResponseDatacentersInnerServerTypes';
import DatacentersIdGet200Response from './model/DatacentersIdGet200Response';
import DeleteSubnetRequest from './model/DeleteSubnetRequest';
import DetachFromNetworkRequest from './model/DetachFromNetworkRequest';
import Firewall from './model/Firewall';
import FirewallAppliedToInner from './model/FirewallAppliedToInner';
import FirewallAppliedToInnerAppliedToResourcesInner from './model/FirewallAppliedToInnerAppliedToResourcesInner';
import FirewallAppliedToInnerAppliedToResourcesInnerServer from './model/FirewallAppliedToInnerAppliedToResourcesInnerServer';
import FirewallAppliedToInnerLabelSelector from './model/FirewallAppliedToInnerLabelSelector';
import FirewallApplyToResources from './model/FirewallApplyToResources';
import FirewallApplyToResourcesLabelSelector from './model/FirewallApplyToResourcesLabelSelector';
import FirewallApplyToResourcesServer from './model/FirewallApplyToResourcesServer';
import FirewallRemoveFromResources from './model/FirewallRemoveFromResources';
import FirewallResponse from './model/FirewallResponse';
import FirewallsResponse from './model/FirewallsResponse';
import FloatingIpsGet200Response from './model/FloatingIpsGet200Response';
import FloatingIpsGet200ResponseFloatingIpsInner from './model/FloatingIpsGet200ResponseFloatingIpsInner';
import FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner from './model/FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner';
import FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation from './model/FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation';
import FloatingIpsGet200ResponseFloatingIpsInnerProtection from './model/FloatingIpsGet200ResponseFloatingIpsInnerProtection';
import FloatingIpsIdActionsGet200Response from './model/FloatingIpsIdActionsGet200Response';
import FloatingIpsIdGet200Response from './model/FloatingIpsIdGet200Response';
import FloatingIpsPost201Response from './model/FloatingIpsPost201Response';
import ImagesGet200Response from './model/ImagesGet200Response';
import ImagesGet200ResponseImagesInner from './model/ImagesGet200ResponseImagesInner';
import ImagesGet200ResponseImagesInnerCreatedFrom from './model/ImagesGet200ResponseImagesInnerCreatedFrom';
import ImagesIdActionsChangeProtectionPostRequest from './model/ImagesIdActionsChangeProtectionPostRequest';
import ImagesIdGet200Response from './model/ImagesIdGet200Response';
import IsosGet200Response from './model/IsosGet200Response';
import IsosGet200ResponseIsosInner from './model/IsosGet200ResponseIsosInner';
import IsosIdGet200Response from './model/IsosIdGet200Response';
import LoadBalancerAlgorithm from './model/LoadBalancerAlgorithm';
import LoadBalancerService from './model/LoadBalancerService';
import LoadBalancerServiceHTTP from './model/LoadBalancerServiceHTTP';
import LoadBalancerServiceHealthCheck from './model/LoadBalancerServiceHealthCheck';
import LoadBalancerServiceHealthCheckHttp from './model/LoadBalancerServiceHealthCheckHttp';
import LoadBalancerTarget from './model/LoadBalancerTarget';
import LoadBalancerTargetHealthStatusInner from './model/LoadBalancerTargetHealthStatusInner';
import LoadBalancerTargetIP from './model/LoadBalancerTargetIP';
import LoadBalancerTargetLabelSelector from './model/LoadBalancerTargetLabelSelector';
import LoadBalancerTargetServer from './model/LoadBalancerTargetServer';
import LoadBalancerTargetTarget from './model/LoadBalancerTargetTarget';
import LoadBalancerTypesGet200Response from './model/LoadBalancerTypesGet200Response';
import LoadBalancerTypesGet200ResponseLoadBalancerTypesInner from './model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInner';
import LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner from './model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner';
import LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly from './model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly';
import LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly from './model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly';
import LoadBalancerTypesIdGet200Response from './model/LoadBalancerTypesIdGet200Response';
import LoadBalancersGet200Response from './model/LoadBalancersGet200Response';
import LoadBalancersGet200ResponseLoadBalancersInner from './model/LoadBalancersGet200ResponseLoadBalancersInner';
import LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm from './model/LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm';
import LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner from './model/LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner';
import LoadBalancersGet200ResponseLoadBalancersInnerPublicNet from './model/LoadBalancersGet200ResponseLoadBalancersInnerPublicNet';
import LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4 from './model/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4';
import LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6 from './model/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6';
import LoadBalancersIdActionsAttachToNetworkPostRequest from './model/LoadBalancersIdActionsAttachToNetworkPostRequest';
import LoadBalancersIdActionsChangeAlgorithmPostRequest from './model/LoadBalancersIdActionsChangeAlgorithmPostRequest';
import LoadBalancersIdActionsChangeProtectionPostRequest from './model/LoadBalancersIdActionsChangeProtectionPostRequest';
import LoadBalancersIdActionsDeleteServicePostRequest from './model/LoadBalancersIdActionsDeleteServicePostRequest';
import LoadBalancersIdActionsDetachFromNetworkPostRequest from './model/LoadBalancersIdActionsDetachFromNetworkPostRequest';
import LoadBalancersIdGet200Response from './model/LoadBalancersIdGet200Response';
import LoadBalancersIdMetricsGet200Response from './model/LoadBalancersIdMetricsGet200Response';
import LoadBalancersIdMetricsGet200ResponseMetrics from './model/LoadBalancersIdMetricsGet200ResponseMetrics';
import LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue from './model/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue';
import LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner from './model/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner';
import LoadBalancersIdPutRequest from './model/LoadBalancersIdPutRequest';
import LoadBalancersPost201Response from './model/LoadBalancersPost201Response';
import LocationsGet200Response from './model/LocationsGet200Response';
import LocationsIdGet200Response from './model/LocationsIdGet200Response';
import NetworksGet200Response from './model/NetworksGet200Response';
import NetworksGet200ResponseNetworksInner from './model/NetworksGet200ResponseNetworksInner';
import NetworksGet200ResponseNetworksInnerProtection from './model/NetworksGet200ResponseNetworksInnerProtection';
import NetworksGet200ResponseNetworksInnerRoutesInner from './model/NetworksGet200ResponseNetworksInnerRoutesInner';
import NetworksGet200ResponseNetworksInnerSubnetsInner from './model/NetworksGet200ResponseNetworksInnerSubnetsInner';
import NetworksPost201Response from './model/NetworksPost201Response';
import NullableAction from './model/NullableAction';
import PlacementGroup from './model/PlacementGroup';
import PlacementGroupNullable from './model/PlacementGroupNullable';
import PlacementGroupResponse from './model/PlacementGroupResponse';
import PlacementGroupsResponse from './model/PlacementGroupsResponse';
import PricingGet200Response from './model/PricingGet200Response';
import PricingGet200ResponsePricing from './model/PricingGet200ResponsePricing';
import PricingGet200ResponsePricingFloatingIp from './model/PricingGet200ResponsePricingFloatingIp';
import PricingGet200ResponsePricingFloatingIpPriceMonthly from './model/PricingGet200ResponsePricingFloatingIpPriceMonthly';
import PricingGet200ResponsePricingFloatingIpsInner from './model/PricingGet200ResponsePricingFloatingIpsInner';
import PricingGet200ResponsePricingFloatingIpsInnerPricesInner from './model/PricingGet200ResponsePricingFloatingIpsInnerPricesInner';
import PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly from './model/PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly';
import PricingGet200ResponsePricingImage from './model/PricingGet200ResponsePricingImage';
import PricingGet200ResponsePricingLoadBalancerTypesInner from './model/PricingGet200ResponsePricingLoadBalancerTypesInner';
import PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner from './model/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner';
import PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly from './model/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly';
import PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly from './model/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly';
import PricingGet200ResponsePricingPrimaryIpsInner from './model/PricingGet200ResponsePricingPrimaryIpsInner';
import PricingGet200ResponsePricingPrimaryIpsInnerPricesInner from './model/PricingGet200ResponsePricingPrimaryIpsInnerPricesInner';
import PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly from './model/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly';
import PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly from './model/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly';
import PricingGet200ResponsePricingServerBackup from './model/PricingGet200ResponsePricingServerBackup';
import PricingGet200ResponsePricingServerTypesInner from './model/PricingGet200ResponsePricingServerTypesInner';
import PricingGet200ResponsePricingServerTypesInnerPricesInner from './model/PricingGet200ResponsePricingServerTypesInnerPricesInner';
import PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly from './model/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly';
import PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly from './model/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly';
import PricingGet200ResponsePricingTraffic from './model/PricingGet200ResponsePricingTraffic';
import PricingGet200ResponsePricingVolume from './model/PricingGet200ResponsePricingVolume';
import PrimaryIP from './model/PrimaryIP';
import PrimaryIPDatacenter from './model/PrimaryIPDatacenter';
import PrimaryIPDnsPtrInner from './model/PrimaryIPDnsPtrInner';
import PrimaryIPResponse from './model/PrimaryIPResponse';
import PrimaryIPsResponse from './model/PrimaryIPsResponse';
import RebuildServerRequest from './model/RebuildServerRequest';
import RemoveFromResourcesRequest from './model/RemoveFromResourcesRequest';
import RemoveTargetRequest from './model/RemoveTargetRequest';
import Rule from './model/Rule';
import ServerPublicNetFirewall from './model/ServerPublicNetFirewall';
import ServerTypesGet200Response from './model/ServerTypesGet200Response';
import ServerTypesGet200ResponseServerTypesInner from './model/ServerTypesGet200ResponseServerTypesInner';
import ServerTypesIdGet200Response from './model/ServerTypesIdGet200Response';
import ServersGet200Response from './model/ServersGet200Response';
import ServersGet200ResponseServersInner from './model/ServersGet200ResponseServersInner';
import ServersGet200ResponseServersInnerDatacenter from './model/ServersGet200ResponseServersInnerDatacenter';
import ServersGet200ResponseServersInnerImage from './model/ServersGet200ResponseServersInnerImage';
import ServersGet200ResponseServersInnerIso from './model/ServersGet200ResponseServersInnerIso';
import ServersGet200ResponseServersInnerPrivateNetInner from './model/ServersGet200ResponseServersInnerPrivateNetInner';
import ServersGet200ResponseServersInnerProtection from './model/ServersGet200ResponseServersInnerProtection';
import ServersGet200ResponseServersInnerPublicNet from './model/ServersGet200ResponseServersInnerPublicNet';
import ServersGet200ResponseServersInnerPublicNetIpv4 from './model/ServersGet200ResponseServersInnerPublicNetIpv4';
import ServersGet200ResponseServersInnerPublicNetIpv6 from './model/ServersGet200ResponseServersInnerPublicNetIpv6';
import ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner from './model/ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner';
import ServersGet200ResponseServersInnerServerType from './model/ServersGet200ResponseServersInnerServerType';
import ServersIdActionsAttachIsoPostRequest from './model/ServersIdActionsAttachIsoPostRequest';
import ServersIdActionsChangeAliasIpsPostRequest from './model/ServersIdActionsChangeAliasIpsPostRequest';
import ServersIdActionsChangeDnsPtrPostRequest from './model/ServersIdActionsChangeDnsPtrPostRequest';
import ServersIdActionsChangeProtectionPostRequest from './model/ServersIdActionsChangeProtectionPostRequest';
import ServersIdActionsChangeTypePostRequest from './model/ServersIdActionsChangeTypePostRequest';
import ServersIdActionsCreateImagePost201Response from './model/ServersIdActionsCreateImagePost201Response';
import ServersIdActionsEnableRescuePost201Response from './model/ServersIdActionsEnableRescuePost201Response';
import ServersIdActionsEnableRescuePostRequest from './model/ServersIdActionsEnableRescuePostRequest';
import ServersIdActionsRebuildPost201Response from './model/ServersIdActionsRebuildPost201Response';
import ServersIdActionsRequestConsolePost201Response from './model/ServersIdActionsRequestConsolePost201Response';
import ServersIdDelete200Response from './model/ServersIdDelete200Response';
import ServersIdGet200Response from './model/ServersIdGet200Response';
import SetRulesRequest from './model/SetRulesRequest';
import SshKeysGet200Response from './model/SshKeysGet200Response';
import SshKeysGet200ResponseSshKeysInner from './model/SshKeysGet200ResponseSshKeysInner';
import SshKeysIdPutRequest from './model/SshKeysIdPutRequest';
import SshKeysPost201Response from './model/SshKeysPost201Response';
import SshKeysPostRequest from './model/SshKeysPostRequest';
import UpdateCertificateRequest from './model/UpdateCertificateRequest';
import UpdateFirewallRequest from './model/UpdateFirewallRequest';
import UpdateFloatingIPRequest from './model/UpdateFloatingIPRequest';
import UpdateImageRequest from './model/UpdateImageRequest';
import UpdateNetworkRequest from './model/UpdateNetworkRequest';
import UpdateNetworkRequestLabels from './model/UpdateNetworkRequestLabels';
import UpdatePlacementGroupRequest from './model/UpdatePlacementGroupRequest';
import UpdatePrimaryIPRequest from './model/UpdatePrimaryIPRequest';
import UpdateServerRequest from './model/UpdateServerRequest';
import UpdateVolumeRequest from './model/UpdateVolumeRequest';
import VolumesGet200Response from './model/VolumesGet200Response';
import VolumesGet200ResponseVolumesInner from './model/VolumesGet200ResponseVolumesInner';
import VolumesGet200ResponseVolumesInnerLocation from './model/VolumesGet200ResponseVolumesInnerLocation';
import VolumesIdActionsChangeProtectionPostRequest from './model/VolumesIdActionsChangeProtectionPostRequest';
import VolumesIdActionsResizePostRequest from './model/VolumesIdActionsResizePostRequest';
import VolumesIdGet200Response from './model/VolumesIdGet200Response';
import VolumesPost201Response from './model/VolumesPost201Response';
import ActionsApi from './api/ActionsApi';
import CertificateActionsApi from './api/CertificateActionsApi';
import CertificatesApi from './api/CertificatesApi';
import DatacentersApi from './api/DatacentersApi';
import FirewallActionsApi from './api/FirewallActionsApi';
import FirewallsApi from './api/FirewallsApi';
import FloatingIPActionsApi from './api/FloatingIPActionsApi';
import FloatingIPsApi from './api/FloatingIPsApi';
import ISOsApi from './api/ISOsApi';
import ImageActionsApi from './api/ImageActionsApi';
import ImagesApi from './api/ImagesApi';
import LoadBalancerActionsApi from './api/LoadBalancerActionsApi';
import LoadBalancerTypesApi from './api/LoadBalancerTypesApi';
import LoadBalancersApi from './api/LoadBalancersApi';
import LocationsApi from './api/LocationsApi';
import NetworkActionsApi from './api/NetworkActionsApi';
import NetworksApi from './api/NetworksApi';
import PlacementGroupsApi from './api/PlacementGroupsApi';
import PricingApi from './api/PricingApi';
import PrimaryIPActionsApi from './api/PrimaryIPActionsApi';
import PrimaryIPsApi from './api/PrimaryIPsApi';
import SSHKeysApi from './api/SSHKeysApi';
import ServerActionsApi from './api/ServerActionsApi';
import ServerTypesApi from './api/ServerTypesApi';
import ServersApi from './api/ServersApi';
import VolumeActionsApi from './api/VolumeActionsApi';
import VolumesApi from './api/VolumesApi';


/**
* This is the official API documentation for the Public Hetzner Cloud.  ## Introduction  The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.  As an alternative to working directly with our API you may also consider to use: * Our CLI program [hcloud](https://github.com/hetznercloud/cli) * Our [library for Go](https://github.com/hetznercloud/hcloud-go) * Our [library for Python](https://github.com/hetznercloud/hcloud-python)  Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).  If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following: * The type of integration you would like to develop * Link to the GitHub repo you will use for the Project * Link to some other Open Source work you have already done (if you have done so)  ## Getting Started To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to &#x60;Security&#x60; → &#x60;API Tokens&#x60;, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is &#x60;jEheVytlAoFl7F8MqUQ7jAo2hOXASztX&#x60;.  You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.haxx.se/).  Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like &#x60;servers&#x60; inside the example response. A response can also contain a &#x60;meta&#x60; object with information like [Pagination](https://docs.hetzner.cloud/#overview-pagination).  **Example Request** &#x60;&#x60;&#x60;bash curl -H \&quot;Authorization: Bearer jEheVytlAoFl7F8MqUQ7jAo2hOXASztX\&quot; \\     https://api.hetzner.cloud/v1/servers &#x60;&#x60;&#x60;  **Example Response** &#x60;&#x60;&#x60;json {     \&quot;servers\&quot;: [],     \&quot;meta\&quot;: {         \&quot;pagination\&quot;: {             \&quot;page\&quot;: 1,             \&quot;per_page\&quot;: 25,             \&quot;previous_page\&quot;: null,             \&quot;next_page\&quot;: null,             \&quot;last_page\&quot;: 1,             \&quot;total_entries\&quot;: 0         }     } } &#x60;&#x60;&#x60;  ## Authentication All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the &#x60;Authorization&#x60; HTTP header.  To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to &#x60;Security&#x60; → &#x60;API Tokens&#x60;, and generate a new token.  **Example Authorization header** &#x60;&#x60;&#x60;html Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj &#x60;&#x60;&#x60;  ## Errors Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.  The error response contains the following keys:  | Keys      | Meaning                                                               | |-----------|-----------------------------------------------------------------------| | &#x60;code&#x60;    | Short string indicating the type of error (machine-parsable)          | | &#x60;message&#x60; | Textual description on what has gone wrong                            | | &#x60;details&#x60; | An object providing for details on the error (schema depends on code) |  **Example response** &#x60;&#x60;&#x60;json {   \&quot;error\&quot;: {     \&quot;code\&quot;: \&quot;invalid_input\&quot;,     \&quot;message\&quot;: \&quot;invalid input in field &#39;broken_field&#39;: is too long\&quot;,     \&quot;details\&quot;: {       \&quot;fields\&quot;: [         {           \&quot;name\&quot;: \&quot;broken_field\&quot;,           \&quot;messages\&quot;: [\&quot;is too long\&quot;]         }       ]     }   } } &#x60;&#x60;&#x60;  ### Error Codes  | Code                      | Description                                                                      | |---------------------------|----------------------------------------------------------------------------------| | &#x60;forbidden&#x60;               | Insufficient permissions for this request                                        | | &#x60;invalid_input&#x60;           | Error while parsing or processing the input                                      | | &#x60;json_error&#x60;              | Invalid JSON input in your request                                               | | &#x60;locked&#x60;                  | The item you are trying to access is locked (there is already an Action running) | | &#x60;not_found&#x60;               | Entity not found                                                                 | | &#x60;rate_limit_exceeded&#x60;     | Error when sending too many requests                                             | | &#x60;resource_limit_exceeded&#x60; | Error when exceeding the maximum quantity of a resource for an account           | | &#x60;resource_unavailable&#x60;    | The requested resource is currently unavailable                                  | | &#x60;service_error&#x60;           | Error within a service                                                           | | &#x60;uniqueness_error&#x60;        | One or more of the objects fields must be unique                                 | | &#x60;protected&#x60;               | The Action you are trying to start is protected for this resource                | | &#x60;maintenance&#x60;             | Cannot perform operation due to maintenance                                      | | &#x60;conflict&#x60;                | The resource has changed during the request, please retry                        | | &#x60;unsupported_error&#x60;       | The corresponding resource does not support the Action                           | | &#x60;token_readonly&#x60;          | The token is only allowed to perform GET requests                                | | &#x60;unavailable&#x60;             | A service or product is currently not available                                  |  **invalid_input** &#x60;&#x60;&#x60;json {   \&quot;error\&quot;: {     \&quot;code\&quot;: \&quot;invalid_input\&quot;,     \&quot;message\&quot;: \&quot;invalid input in field &#39;broken_field&#39;: is too long\&quot;,     \&quot;details\&quot;: {       \&quot;fields\&quot;: [         {           \&quot;name\&quot;: \&quot;broken_field\&quot;,           \&quot;messages\&quot;: [\&quot;is too long\&quot;]         }       ]     }   } } &#x60;&#x60;&#x60;  **uniqueness_error** &#x60;&#x60;&#x60;json {   \&quot;error\&quot;: {     \&quot;code\&quot;: \&quot;uniqueness_error\&quot;,     \&quot;message\&quot;: \&quot;SSH key with the same fingerprint already exists\&quot;,     \&quot;details\&quot;: {       \&quot;fields\&quot;: [         {           \&quot;name\&quot;: \&quot;public_key\&quot;         }       ]     }   } } &#x60;&#x60;&#x60;  **resource_limit_exceeded** &#x60;&#x60;&#x60;json {   \&quot;error\&quot;: {     \&quot;code\&quot;: \&quot;resource_limit_exceeded\&quot;,     \&quot;message\&quot;: \&quot;project limit exceeded\&quot;,     \&quot;details\&quot;: {       \&quot;limits\&quot;: [         {           \&quot;name\&quot;: \&quot;project_limit\&quot;         }       ]     }   } } &#x60;&#x60;&#x60;  ## Labels Labels are &#x60;key/value&#x60; pairs that can be attached to all resources.  Valid label keys have two segments: an optional prefix and name, separated by a slash (&#x60;/&#x60;). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (&#x60;[a-z0-9A-Z]&#x60;) with dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;), dots (&#x60;.&#x60;), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (&#x60;.&#x60;), not longer than 253 characters in total, followed by a slash (&#x60;/&#x60;).  Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (&#x60;[a-z0-9A-Z]&#x60;) with dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;), dots (&#x60;.&#x60;), and alphanumerics between.  The &#x60;hetzner.cloud/&#x60; prefix is reserved and cannot be used.  **Example Labels** &#x60;&#x60;&#x60;json {   \&quot;labels\&quot;: {     \&quot;environment\&quot;:\&quot;development\&quot;,     \&quot;service\&quot;:\&quot;backend\&quot;,     \&quot;example.com/my\&quot;:\&quot;label\&quot;,     \&quot;just-a-key\&quot;:\&quot;\&quot;   } } &#x60;&#x60;&#x60;  ## Label Selector For resources with labels, you can filter resources by their labels using the label selector query language.  | Expression           | Meaning                                                             | |----------------------|---------------------------------------------------------------------| | &#x60;k&#x3D;&#x3D;v&#x60; / &#x60;k&#x3D;v&#x60;       | Value of key &#x60;k&#x60; does equal value &#x60;v&#x60;                               | | &#x60;k!&#x3D;v&#x60;               | Value of key &#x60;k&#x60; does not equal value &#x60;v&#x60;                           | | &#x60;k&#x60;                  | Key &#x60;k&#x60; is present                                                  | | &#x60;!k&#x60;                 | Key &#x60;k&#x60; is not present                                              | | &#x60;k in (v1,v2,v3)&#x60;    | Value of key &#x60;k&#x60; is &#x60;v1&#x60;, &#x60;v2&#x60;, or &#x60;v3&#x60;                             | | &#x60;k notin (v1,v2,v3)&#x60; | Value of key &#x60;k&#x60; is neither &#x60;v1&#x60;, nor &#x60;v2&#x60;, nor &#x60;v3&#x60;                | | &#x60;k1&#x3D;&#x3D;v,!k2&#x60;          | Value of key &#x60;k1&#x60; is &#x60;v&#x60; and key &#x60;k2&#x60; is not present                |  ### Examples * Returns all resources that have a &#x60;env&#x3D;production&#x60; label and that don&#39;t have a &#x60;type&#x3D;database&#x60; label:    &#x60;env&#x3D;production,type!&#x3D;database&#x60; * Returns all resources that have a &#x60;env&#x3D;testing&#x60; or &#x60;env&#x3D;staging&#x60; label:      &#x60;env in (testing,staging)&#x60; * Returns all resources that don&#39;t have a &#x60;type&#x60; label:      &#x60;!type&#x60;  ## Pagination Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:  * A &#x60;page&#x60; parameter specifies the page to fetch. The number of the first page is 1. * A &#x60;per_page&#x60; parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.  Responses contain a &#x60;Link&#x60; header with pagination information.  Additionally, if the response body is JSON and the root object is an object, that object has a &#x60;pagination&#x60; object inside the &#x60;meta&#x60; object with pagination information:  **Example Pagination** &#x60;&#x60;&#x60;json {     \&quot;servers\&quot;: [...],     \&quot;meta\&quot;: {         \&quot;pagination\&quot;: {             \&quot;page\&quot;: 2,             \&quot;per_page\&quot;: 25,             \&quot;previous_page\&quot;: 1,             \&quot;next_page\&quot;: 3,             \&quot;last_page\&quot;: 4,             \&quot;total_entries\&quot;: 100         }     } } &#x60;&#x60;&#x60;  The keys &#x60;previous_page&#x60;, &#x60;next_page&#x60;, &#x60;last_page&#x60;, and &#x60;total_entries&#x60; may be &#x60;null&#x60; when on the first page, last page, or when the total number of entries is unknown.  **Example Pagination Link header** &#x60;&#x60;&#x60;bash Link: &lt;https://api.hetzner.cloud/v1/actions?page&#x3D;2&amp;per_page&#x3D;5&gt;; rel&#x3D;\&quot;prev\&quot;,       &lt;https://api.hetzner.cloud/v1/actions?page&#x3D;4&amp;per_page&#x3D;5&gt;; rel&#x3D;\&quot;next\&quot;,       &lt;https://api.hetzner.cloud/v1/actions?page&#x3D;6&amp;per_page&#x3D;5&gt;; rel&#x3D;\&quot;last\&quot; &#x60;&#x60;&#x60;  Line breaks have been added for display purposes only and responses may only contain some of the above &#x60;rel&#x60; values.  ## Rate Limiting All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a &#x60;429 Too Many Requests&#x60; error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.  * The &#x60;RateLimit-Limit&#x60; header contains the total number of requests you can perform per hour. * The &#x60;RateLimit-Remaining&#x60; header contains the number of requests remaining in the current rate limit time frame. * The &#x60;RateLimit-Reset&#x60; header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.  The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.  ## Server Metadata Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:  | Data              | Format | Contents                                                     | |-------------------|--------|--------------------------------------------------------------| | hostname          | text   | Name of the Server as set in the api                         | | instance-id       | number | ID of the server                                             | | public-ipv4       | text   | Primary public IPv4 address                                  | | private-networks  | yaml   | Details about the private networks the Server is attached to | | availability-zone | text   | Name of the availability zone that Server runs in            | | region            | text   | Network zone, e.g. eu-central                                |  **Example: Summary** &#x60;&#x60;&#x60;bash $ curl http://169.254.169.254/hetzner/v1/metadata &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;yaml availability-zone: hel1-dc2 hostname: my-server instance-id: 42 public-ipv4: 1.2.3.4 region: eu-central &#x60;&#x60;&#x60;  **Example: Hostname** &#x60;&#x60;&#x60;bash $ curl http://169.254.169.254/hetzner/v1/metadata/hostname my-server &#x60;&#x60;&#x60;  **Example: Instance ID** &#x60;&#x60;&#x60;bash $ curl http://169.254.169.254/hetzner/v1/metadata/instance-id 42 &#x60;&#x60;&#x60;  **Example: Public IPv4** &#x60;&#x60;&#x60;bash $ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4 1.2.3.4 &#x60;&#x60;&#x60;  **Example: Private Networks** &#x60;&#x60;&#x60;bash $ curl http://169.254.169.254/hetzner/v1/metadata/private-networks &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;json - ip: 10.0.0.2   alias_ips: [10.0.0.3, 10.0.0.4]   interface_num: 1   mac_address: 86:00:00:2a:7d:e0   network_id: 1234   network_name: nw-test1   network: 10.0.0.0/8   subnet: 10.0.0.0/24   gateway: 10.0.0.1 - ip: 192.168.0.2   alias_ips: []   interface_num: 2   mac_address: 86:00:00:2a:7d:e1   network_id: 4321   network_name: nw-test2   network: 192.168.0.0/16   subnet: 192.168.0.0/24   gateway: 192.168.0.1 &#x60;&#x60;&#x60;  **Example: Availability Zone** &#x60;&#x60;&#x60;bash $ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone hel1-dc2 &#x60;&#x60;&#x60;  **Example: Region** &#x60;&#x60;&#x60;bash $ curl http://169.254.169.254/hetzner/v1/metadata/region eu-central &#x60;&#x60;&#x60;  ## Sorting Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the &#x60;sort&#x60; query string parameter. You can sort by multiple fields. You can set the sort direction by appending &#x60;:asc&#x60; or &#x60;:desc&#x60; to the field name. By default, ascending sorting is used.  **Example: Sorting** &#x60;&#x60;&#x60;bash https://api.hetzner.cloud/v1/actions?sort&#x3D;status https://api.hetzner.cloud/v1/actions?sort&#x3D;status:asc https://api.hetzner.cloud/v1/actions?sort&#x3D;status:desc https://api.hetzner.cloud/v1/actions?sort&#x3D;status:asc&amp;sort&#x3D;command:desc &#x60;&#x60;&#x60; .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var HetznerCloudApi = require('index'); // See note below*.
* var xxxSvc = new HetznerCloudApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new HetznerCloudApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new HetznerCloudApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new HetznerCloudApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Action model constructor.
     * @property {module:model/Action}
     */
    Action,

    /**
     * The ActionError model constructor.
     * @property {module:model/ActionError}
     */
    ActionError,

    /**
     * The ActionResourcesInner model constructor.
     * @property {module:model/ActionResourcesInner}
     */
    ActionResourcesInner,

    /**
     * The ActionResponse model constructor.
     * @property {module:model/ActionResponse}
     */
    ActionResponse,

    /**
     * The ActionsResponse model constructor.
     * @property {module:model/ActionsResponse}
     */
    ActionsResponse,

    /**
     * The ActionsResponseMeta model constructor.
     * @property {module:model/ActionsResponseMeta}
     */
    ActionsResponseMeta,

    /**
     * The ActionsResponseMetaPagination model constructor.
     * @property {module:model/ActionsResponseMetaPagination}
     */
    ActionsResponseMetaPagination,

    /**
     * The AddDeleteRouteRequest model constructor.
     * @property {module:model/AddDeleteRouteRequest}
     */
    AddDeleteRouteRequest,

    /**
     * The AddSubnetRequest model constructor.
     * @property {module:model/AddSubnetRequest}
     */
    AddSubnetRequest,

    /**
     * The AddTargetRequest model constructor.
     * @property {module:model/AddTargetRequest}
     */
    AddTargetRequest,

    /**
     * The AddTargetRequestLabelSelector model constructor.
     * @property {module:model/AddTargetRequestLabelSelector}
     */
    AddTargetRequestLabelSelector,

    /**
     * The AddTargetRequestServer model constructor.
     * @property {module:model/AddTargetRequestServer}
     */
    AddTargetRequestServer,

    /**
     * The AddToPlacementGroupRequest model constructor.
     * @property {module:model/AddToPlacementGroupRequest}
     */
    AddToPlacementGroupRequest,

    /**
     * The ApplyToResourcesRequest model constructor.
     * @property {module:model/ApplyToResourcesRequest}
     */
    ApplyToResourcesRequest,

    /**
     * The AssignFloatingIPRequest model constructor.
     * @property {module:model/AssignFloatingIPRequest}
     */
    AssignFloatingIPRequest,

    /**
     * The AssignPrimaryIPRequest model constructor.
     * @property {module:model/AssignPrimaryIPRequest}
     */
    AssignPrimaryIPRequest,

    /**
     * The AttachToNetworkRequest model constructor.
     * @property {module:model/AttachToNetworkRequest}
     */
    AttachToNetworkRequest,

    /**
     * The AttachVolumeRequest model constructor.
     * @property {module:model/AttachVolumeRequest}
     */
    AttachVolumeRequest,

    /**
     * The Certificate model constructor.
     * @property {module:model/Certificate}
     */
    Certificate,

    /**
     * The CertificateResponse model constructor.
     * @property {module:model/CertificateResponse}
     */
    CertificateResponse,

    /**
     * The CertificateStatus model constructor.
     * @property {module:model/CertificateStatus}
     */
    CertificateStatus,

    /**
     * The CertificateStatusError model constructor.
     * @property {module:model/CertificateStatusError}
     */
    CertificateStatusError,

    /**
     * The CertificateUsedByInner model constructor.
     * @property {module:model/CertificateUsedByInner}
     */
    CertificateUsedByInner,

    /**
     * The CertificatesResponse model constructor.
     * @property {module:model/CertificatesResponse}
     */
    CertificatesResponse,

    /**
     * The ChangeDNSPTRRequest model constructor.
     * @property {module:model/ChangeDNSPTRRequest}
     */
    ChangeDNSPTRRequest,

    /**
     * The ChangeIPRangeRequest model constructor.
     * @property {module:model/ChangeIPRangeRequest}
     */
    ChangeIPRangeRequest,

    /**
     * The ChangeLoadbalancerDnsPtrRequest model constructor.
     * @property {module:model/ChangeLoadbalancerDnsPtrRequest}
     */
    ChangeLoadbalancerDnsPtrRequest,

    /**
     * The ChangeProtectionRequest model constructor.
     * @property {module:model/ChangeProtectionRequest}
     */
    ChangeProtectionRequest,

    /**
     * The ChangeProtectionRequest1 model constructor.
     * @property {module:model/ChangeProtectionRequest1}
     */
    ChangeProtectionRequest1,

    /**
     * The ChangeProtectionRequest2 model constructor.
     * @property {module:model/ChangeProtectionRequest2}
     */
    ChangeProtectionRequest2,

    /**
     * The ChangeTypeRequest model constructor.
     * @property {module:model/ChangeTypeRequest}
     */
    ChangeTypeRequest,

    /**
     * The CreateCertificateRequest model constructor.
     * @property {module:model/CreateCertificateRequest}
     */
    CreateCertificateRequest,

    /**
     * The CreateCertificateResponse model constructor.
     * @property {module:model/CreateCertificateResponse}
     */
    CreateCertificateResponse,

    /**
     * The CreateFirewallRequest model constructor.
     * @property {module:model/CreateFirewallRequest}
     */
    CreateFirewallRequest,

    /**
     * The CreateFirewallRequestApplyToInner model constructor.
     * @property {module:model/CreateFirewallRequestApplyToInner}
     */
    CreateFirewallRequestApplyToInner,

    /**
     * The CreateFirewallRequestApplyToInnerLabelSelector model constructor.
     * @property {module:model/CreateFirewallRequestApplyToInnerLabelSelector}
     */
    CreateFirewallRequestApplyToInnerLabelSelector,

    /**
     * The CreateFirewallRequestApplyToInnerServer model constructor.
     * @property {module:model/CreateFirewallRequestApplyToInnerServer}
     */
    CreateFirewallRequestApplyToInnerServer,

    /**
     * The CreateFirewallResponse model constructor.
     * @property {module:model/CreateFirewallResponse}
     */
    CreateFirewallResponse,

    /**
     * The CreateFloatingIPRequest model constructor.
     * @property {module:model/CreateFloatingIPRequest}
     */
    CreateFloatingIPRequest,

    /**
     * The CreateImageRequest model constructor.
     * @property {module:model/CreateImageRequest}
     */
    CreateImageRequest,

    /**
     * The CreateLoadBalancerRequest model constructor.
     * @property {module:model/CreateLoadBalancerRequest}
     */
    CreateLoadBalancerRequest,

    /**
     * The CreateLoadBalancerRequestLabels model constructor.
     * @property {module:model/CreateLoadBalancerRequestLabels}
     */
    CreateLoadBalancerRequestLabels,

    /**
     * The CreateNetworkRequest model constructor.
     * @property {module:model/CreateNetworkRequest}
     */
    CreateNetworkRequest,

    /**
     * The CreateNetworkRequestSubnetsInner model constructor.
     * @property {module:model/CreateNetworkRequestSubnetsInner}
     */
    CreateNetworkRequestSubnetsInner,

    /**
     * The CreatePlacementGroupRequest model constructor.
     * @property {module:model/CreatePlacementGroupRequest}
     */
    CreatePlacementGroupRequest,

    /**
     * The CreatePlacementGroupResponse model constructor.
     * @property {module:model/CreatePlacementGroupResponse}
     */
    CreatePlacementGroupResponse,

    /**
     * The CreatePrimaryIPRequest model constructor.
     * @property {module:model/CreatePrimaryIPRequest}
     */
    CreatePrimaryIPRequest,

    /**
     * The CreatePrimaryIPResponse model constructor.
     * @property {module:model/CreatePrimaryIPResponse}
     */
    CreatePrimaryIPResponse,

    /**
     * The CreateServerRequest model constructor.
     * @property {module:model/CreateServerRequest}
     */
    CreateServerRequest,

    /**
     * The CreateServerRequestFirewallsInner model constructor.
     * @property {module:model/CreateServerRequestFirewallsInner}
     */
    CreateServerRequestFirewallsInner,

    /**
     * The CreateServerRequestPublicNet model constructor.
     * @property {module:model/CreateServerRequestPublicNet}
     */
    CreateServerRequestPublicNet,

    /**
     * The CreateServerResponse model constructor.
     * @property {module:model/CreateServerResponse}
     */
    CreateServerResponse,

    /**
     * The CreateVolumeRequest model constructor.
     * @property {module:model/CreateVolumeRequest}
     */
    CreateVolumeRequest,

    /**
     * The DatacentersGet200Response model constructor.
     * @property {module:model/DatacentersGet200Response}
     */
    DatacentersGet200Response,

    /**
     * The DatacentersGet200ResponseDatacentersInner model constructor.
     * @property {module:model/DatacentersGet200ResponseDatacentersInner}
     */
    DatacentersGet200ResponseDatacentersInner,

    /**
     * The DatacentersGet200ResponseDatacentersInnerLocation model constructor.
     * @property {module:model/DatacentersGet200ResponseDatacentersInnerLocation}
     */
    DatacentersGet200ResponseDatacentersInnerLocation,

    /**
     * The DatacentersGet200ResponseDatacentersInnerServerTypes model constructor.
     * @property {module:model/DatacentersGet200ResponseDatacentersInnerServerTypes}
     */
    DatacentersGet200ResponseDatacentersInnerServerTypes,

    /**
     * The DatacentersIdGet200Response model constructor.
     * @property {module:model/DatacentersIdGet200Response}
     */
    DatacentersIdGet200Response,

    /**
     * The DeleteSubnetRequest model constructor.
     * @property {module:model/DeleteSubnetRequest}
     */
    DeleteSubnetRequest,

    /**
     * The DetachFromNetworkRequest model constructor.
     * @property {module:model/DetachFromNetworkRequest}
     */
    DetachFromNetworkRequest,

    /**
     * The Firewall model constructor.
     * @property {module:model/Firewall}
     */
    Firewall,

    /**
     * The FirewallAppliedToInner model constructor.
     * @property {module:model/FirewallAppliedToInner}
     */
    FirewallAppliedToInner,

    /**
     * The FirewallAppliedToInnerAppliedToResourcesInner model constructor.
     * @property {module:model/FirewallAppliedToInnerAppliedToResourcesInner}
     */
    FirewallAppliedToInnerAppliedToResourcesInner,

    /**
     * The FirewallAppliedToInnerAppliedToResourcesInnerServer model constructor.
     * @property {module:model/FirewallAppliedToInnerAppliedToResourcesInnerServer}
     */
    FirewallAppliedToInnerAppliedToResourcesInnerServer,

    /**
     * The FirewallAppliedToInnerLabelSelector model constructor.
     * @property {module:model/FirewallAppliedToInnerLabelSelector}
     */
    FirewallAppliedToInnerLabelSelector,

    /**
     * The FirewallApplyToResources model constructor.
     * @property {module:model/FirewallApplyToResources}
     */
    FirewallApplyToResources,

    /**
     * The FirewallApplyToResourcesLabelSelector model constructor.
     * @property {module:model/FirewallApplyToResourcesLabelSelector}
     */
    FirewallApplyToResourcesLabelSelector,

    /**
     * The FirewallApplyToResourcesServer model constructor.
     * @property {module:model/FirewallApplyToResourcesServer}
     */
    FirewallApplyToResourcesServer,

    /**
     * The FirewallRemoveFromResources model constructor.
     * @property {module:model/FirewallRemoveFromResources}
     */
    FirewallRemoveFromResources,

    /**
     * The FirewallResponse model constructor.
     * @property {module:model/FirewallResponse}
     */
    FirewallResponse,

    /**
     * The FirewallsResponse model constructor.
     * @property {module:model/FirewallsResponse}
     */
    FirewallsResponse,

    /**
     * The FloatingIpsGet200Response model constructor.
     * @property {module:model/FloatingIpsGet200Response}
     */
    FloatingIpsGet200Response,

    /**
     * The FloatingIpsGet200ResponseFloatingIpsInner model constructor.
     * @property {module:model/FloatingIpsGet200ResponseFloatingIpsInner}
     */
    FloatingIpsGet200ResponseFloatingIpsInner,

    /**
     * The FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner model constructor.
     * @property {module:model/FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner}
     */
    FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner,

    /**
     * The FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation model constructor.
     * @property {module:model/FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation}
     */
    FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation,

    /**
     * The FloatingIpsGet200ResponseFloatingIpsInnerProtection model constructor.
     * @property {module:model/FloatingIpsGet200ResponseFloatingIpsInnerProtection}
     */
    FloatingIpsGet200ResponseFloatingIpsInnerProtection,

    /**
     * The FloatingIpsIdActionsGet200Response model constructor.
     * @property {module:model/FloatingIpsIdActionsGet200Response}
     */
    FloatingIpsIdActionsGet200Response,

    /**
     * The FloatingIpsIdGet200Response model constructor.
     * @property {module:model/FloatingIpsIdGet200Response}
     */
    FloatingIpsIdGet200Response,

    /**
     * The FloatingIpsPost201Response model constructor.
     * @property {module:model/FloatingIpsPost201Response}
     */
    FloatingIpsPost201Response,

    /**
     * The ImagesGet200Response model constructor.
     * @property {module:model/ImagesGet200Response}
     */
    ImagesGet200Response,

    /**
     * The ImagesGet200ResponseImagesInner model constructor.
     * @property {module:model/ImagesGet200ResponseImagesInner}
     */
    ImagesGet200ResponseImagesInner,

    /**
     * The ImagesGet200ResponseImagesInnerCreatedFrom model constructor.
     * @property {module:model/ImagesGet200ResponseImagesInnerCreatedFrom}
     */
    ImagesGet200ResponseImagesInnerCreatedFrom,

    /**
     * The ImagesIdActionsChangeProtectionPostRequest model constructor.
     * @property {module:model/ImagesIdActionsChangeProtectionPostRequest}
     */
    ImagesIdActionsChangeProtectionPostRequest,

    /**
     * The ImagesIdGet200Response model constructor.
     * @property {module:model/ImagesIdGet200Response}
     */
    ImagesIdGet200Response,

    /**
     * The IsosGet200Response model constructor.
     * @property {module:model/IsosGet200Response}
     */
    IsosGet200Response,

    /**
     * The IsosGet200ResponseIsosInner model constructor.
     * @property {module:model/IsosGet200ResponseIsosInner}
     */
    IsosGet200ResponseIsosInner,

    /**
     * The IsosIdGet200Response model constructor.
     * @property {module:model/IsosIdGet200Response}
     */
    IsosIdGet200Response,

    /**
     * The LoadBalancerAlgorithm model constructor.
     * @property {module:model/LoadBalancerAlgorithm}
     */
    LoadBalancerAlgorithm,

    /**
     * The LoadBalancerService model constructor.
     * @property {module:model/LoadBalancerService}
     */
    LoadBalancerService,

    /**
     * The LoadBalancerServiceHTTP model constructor.
     * @property {module:model/LoadBalancerServiceHTTP}
     */
    LoadBalancerServiceHTTP,

    /**
     * The LoadBalancerServiceHealthCheck model constructor.
     * @property {module:model/LoadBalancerServiceHealthCheck}
     */
    LoadBalancerServiceHealthCheck,

    /**
     * The LoadBalancerServiceHealthCheckHttp model constructor.
     * @property {module:model/LoadBalancerServiceHealthCheckHttp}
     */
    LoadBalancerServiceHealthCheckHttp,

    /**
     * The LoadBalancerTarget model constructor.
     * @property {module:model/LoadBalancerTarget}
     */
    LoadBalancerTarget,

    /**
     * The LoadBalancerTargetHealthStatusInner model constructor.
     * @property {module:model/LoadBalancerTargetHealthStatusInner}
     */
    LoadBalancerTargetHealthStatusInner,

    /**
     * The LoadBalancerTargetIP model constructor.
     * @property {module:model/LoadBalancerTargetIP}
     */
    LoadBalancerTargetIP,

    /**
     * The LoadBalancerTargetLabelSelector model constructor.
     * @property {module:model/LoadBalancerTargetLabelSelector}
     */
    LoadBalancerTargetLabelSelector,

    /**
     * The LoadBalancerTargetServer model constructor.
     * @property {module:model/LoadBalancerTargetServer}
     */
    LoadBalancerTargetServer,

    /**
     * The LoadBalancerTargetTarget model constructor.
     * @property {module:model/LoadBalancerTargetTarget}
     */
    LoadBalancerTargetTarget,

    /**
     * The LoadBalancerTypesGet200Response model constructor.
     * @property {module:model/LoadBalancerTypesGet200Response}
     */
    LoadBalancerTypesGet200Response,

    /**
     * The LoadBalancerTypesGet200ResponseLoadBalancerTypesInner model constructor.
     * @property {module:model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInner}
     */
    LoadBalancerTypesGet200ResponseLoadBalancerTypesInner,

    /**
     * The LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner model constructor.
     * @property {module:model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner}
     */
    LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner,

    /**
     * The LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly model constructor.
     * @property {module:model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly}
     */
    LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly,

    /**
     * The LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly model constructor.
     * @property {module:model/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly}
     */
    LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly,

    /**
     * The LoadBalancerTypesIdGet200Response model constructor.
     * @property {module:model/LoadBalancerTypesIdGet200Response}
     */
    LoadBalancerTypesIdGet200Response,

    /**
     * The LoadBalancersGet200Response model constructor.
     * @property {module:model/LoadBalancersGet200Response}
     */
    LoadBalancersGet200Response,

    /**
     * The LoadBalancersGet200ResponseLoadBalancersInner model constructor.
     * @property {module:model/LoadBalancersGet200ResponseLoadBalancersInner}
     */
    LoadBalancersGet200ResponseLoadBalancersInner,

    /**
     * The LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm model constructor.
     * @property {module:model/LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm}
     */
    LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm,

    /**
     * The LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner model constructor.
     * @property {module:model/LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner}
     */
    LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner,

    /**
     * The LoadBalancersGet200ResponseLoadBalancersInnerPublicNet model constructor.
     * @property {module:model/LoadBalancersGet200ResponseLoadBalancersInnerPublicNet}
     */
    LoadBalancersGet200ResponseLoadBalancersInnerPublicNet,

    /**
     * The LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4 model constructor.
     * @property {module:model/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4}
     */
    LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4,

    /**
     * The LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6 model constructor.
     * @property {module:model/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6}
     */
    LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6,

    /**
     * The LoadBalancersIdActionsAttachToNetworkPostRequest model constructor.
     * @property {module:model/LoadBalancersIdActionsAttachToNetworkPostRequest}
     */
    LoadBalancersIdActionsAttachToNetworkPostRequest,

    /**
     * The LoadBalancersIdActionsChangeAlgorithmPostRequest model constructor.
     * @property {module:model/LoadBalancersIdActionsChangeAlgorithmPostRequest}
     */
    LoadBalancersIdActionsChangeAlgorithmPostRequest,

    /**
     * The LoadBalancersIdActionsChangeProtectionPostRequest model constructor.
     * @property {module:model/LoadBalancersIdActionsChangeProtectionPostRequest}
     */
    LoadBalancersIdActionsChangeProtectionPostRequest,

    /**
     * The LoadBalancersIdActionsDeleteServicePostRequest model constructor.
     * @property {module:model/LoadBalancersIdActionsDeleteServicePostRequest}
     */
    LoadBalancersIdActionsDeleteServicePostRequest,

    /**
     * The LoadBalancersIdActionsDetachFromNetworkPostRequest model constructor.
     * @property {module:model/LoadBalancersIdActionsDetachFromNetworkPostRequest}
     */
    LoadBalancersIdActionsDetachFromNetworkPostRequest,

    /**
     * The LoadBalancersIdGet200Response model constructor.
     * @property {module:model/LoadBalancersIdGet200Response}
     */
    LoadBalancersIdGet200Response,

    /**
     * The LoadBalancersIdMetricsGet200Response model constructor.
     * @property {module:model/LoadBalancersIdMetricsGet200Response}
     */
    LoadBalancersIdMetricsGet200Response,

    /**
     * The LoadBalancersIdMetricsGet200ResponseMetrics model constructor.
     * @property {module:model/LoadBalancersIdMetricsGet200ResponseMetrics}
     */
    LoadBalancersIdMetricsGet200ResponseMetrics,

    /**
     * The LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue model constructor.
     * @property {module:model/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue}
     */
    LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue,

    /**
     * The LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner model constructor.
     * @property {module:model/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner}
     */
    LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner,

    /**
     * The LoadBalancersIdPutRequest model constructor.
     * @property {module:model/LoadBalancersIdPutRequest}
     */
    LoadBalancersIdPutRequest,

    /**
     * The LoadBalancersPost201Response model constructor.
     * @property {module:model/LoadBalancersPost201Response}
     */
    LoadBalancersPost201Response,

    /**
     * The LocationsGet200Response model constructor.
     * @property {module:model/LocationsGet200Response}
     */
    LocationsGet200Response,

    /**
     * The LocationsIdGet200Response model constructor.
     * @property {module:model/LocationsIdGet200Response}
     */
    LocationsIdGet200Response,

    /**
     * The NetworksGet200Response model constructor.
     * @property {module:model/NetworksGet200Response}
     */
    NetworksGet200Response,

    /**
     * The NetworksGet200ResponseNetworksInner model constructor.
     * @property {module:model/NetworksGet200ResponseNetworksInner}
     */
    NetworksGet200ResponseNetworksInner,

    /**
     * The NetworksGet200ResponseNetworksInnerProtection model constructor.
     * @property {module:model/NetworksGet200ResponseNetworksInnerProtection}
     */
    NetworksGet200ResponseNetworksInnerProtection,

    /**
     * The NetworksGet200ResponseNetworksInnerRoutesInner model constructor.
     * @property {module:model/NetworksGet200ResponseNetworksInnerRoutesInner}
     */
    NetworksGet200ResponseNetworksInnerRoutesInner,

    /**
     * The NetworksGet200ResponseNetworksInnerSubnetsInner model constructor.
     * @property {module:model/NetworksGet200ResponseNetworksInnerSubnetsInner}
     */
    NetworksGet200ResponseNetworksInnerSubnetsInner,

    /**
     * The NetworksPost201Response model constructor.
     * @property {module:model/NetworksPost201Response}
     */
    NetworksPost201Response,

    /**
     * The NullableAction model constructor.
     * @property {module:model/NullableAction}
     */
    NullableAction,

    /**
     * The PlacementGroup model constructor.
     * @property {module:model/PlacementGroup}
     */
    PlacementGroup,

    /**
     * The PlacementGroupNullable model constructor.
     * @property {module:model/PlacementGroupNullable}
     */
    PlacementGroupNullable,

    /**
     * The PlacementGroupResponse model constructor.
     * @property {module:model/PlacementGroupResponse}
     */
    PlacementGroupResponse,

    /**
     * The PlacementGroupsResponse model constructor.
     * @property {module:model/PlacementGroupsResponse}
     */
    PlacementGroupsResponse,

    /**
     * The PricingGet200Response model constructor.
     * @property {module:model/PricingGet200Response}
     */
    PricingGet200Response,

    /**
     * The PricingGet200ResponsePricing model constructor.
     * @property {module:model/PricingGet200ResponsePricing}
     */
    PricingGet200ResponsePricing,

    /**
     * The PricingGet200ResponsePricingFloatingIp model constructor.
     * @property {module:model/PricingGet200ResponsePricingFloatingIp}
     */
    PricingGet200ResponsePricingFloatingIp,

    /**
     * The PricingGet200ResponsePricingFloatingIpPriceMonthly model constructor.
     * @property {module:model/PricingGet200ResponsePricingFloatingIpPriceMonthly}
     */
    PricingGet200ResponsePricingFloatingIpPriceMonthly,

    /**
     * The PricingGet200ResponsePricingFloatingIpsInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingFloatingIpsInner}
     */
    PricingGet200ResponsePricingFloatingIpsInner,

    /**
     * The PricingGet200ResponsePricingFloatingIpsInnerPricesInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingFloatingIpsInnerPricesInner}
     */
    PricingGet200ResponsePricingFloatingIpsInnerPricesInner,

    /**
     * The PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly model constructor.
     * @property {module:model/PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly}
     */
    PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly,

    /**
     * The PricingGet200ResponsePricingImage model constructor.
     * @property {module:model/PricingGet200ResponsePricingImage}
     */
    PricingGet200ResponsePricingImage,

    /**
     * The PricingGet200ResponsePricingLoadBalancerTypesInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingLoadBalancerTypesInner}
     */
    PricingGet200ResponsePricingLoadBalancerTypesInner,

    /**
     * The PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner}
     */
    PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner,

    /**
     * The PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly model constructor.
     * @property {module:model/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly}
     */
    PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly,

    /**
     * The PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly model constructor.
     * @property {module:model/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly}
     */
    PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly,

    /**
     * The PricingGet200ResponsePricingPrimaryIpsInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingPrimaryIpsInner}
     */
    PricingGet200ResponsePricingPrimaryIpsInner,

    /**
     * The PricingGet200ResponsePricingPrimaryIpsInnerPricesInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingPrimaryIpsInnerPricesInner}
     */
    PricingGet200ResponsePricingPrimaryIpsInnerPricesInner,

    /**
     * The PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly model constructor.
     * @property {module:model/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly}
     */
    PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly,

    /**
     * The PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly model constructor.
     * @property {module:model/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly}
     */
    PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly,

    /**
     * The PricingGet200ResponsePricingServerBackup model constructor.
     * @property {module:model/PricingGet200ResponsePricingServerBackup}
     */
    PricingGet200ResponsePricingServerBackup,

    /**
     * The PricingGet200ResponsePricingServerTypesInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingServerTypesInner}
     */
    PricingGet200ResponsePricingServerTypesInner,

    /**
     * The PricingGet200ResponsePricingServerTypesInnerPricesInner model constructor.
     * @property {module:model/PricingGet200ResponsePricingServerTypesInnerPricesInner}
     */
    PricingGet200ResponsePricingServerTypesInnerPricesInner,

    /**
     * The PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly model constructor.
     * @property {module:model/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly}
     */
    PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly,

    /**
     * The PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly model constructor.
     * @property {module:model/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly}
     */
    PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly,

    /**
     * The PricingGet200ResponsePricingTraffic model constructor.
     * @property {module:model/PricingGet200ResponsePricingTraffic}
     */
    PricingGet200ResponsePricingTraffic,

    /**
     * The PricingGet200ResponsePricingVolume model constructor.
     * @property {module:model/PricingGet200ResponsePricingVolume}
     */
    PricingGet200ResponsePricingVolume,

    /**
     * The PrimaryIP model constructor.
     * @property {module:model/PrimaryIP}
     */
    PrimaryIP,

    /**
     * The PrimaryIPDatacenter model constructor.
     * @property {module:model/PrimaryIPDatacenter}
     */
    PrimaryIPDatacenter,

    /**
     * The PrimaryIPDnsPtrInner model constructor.
     * @property {module:model/PrimaryIPDnsPtrInner}
     */
    PrimaryIPDnsPtrInner,

    /**
     * The PrimaryIPResponse model constructor.
     * @property {module:model/PrimaryIPResponse}
     */
    PrimaryIPResponse,

    /**
     * The PrimaryIPsResponse model constructor.
     * @property {module:model/PrimaryIPsResponse}
     */
    PrimaryIPsResponse,

    /**
     * The RebuildServerRequest model constructor.
     * @property {module:model/RebuildServerRequest}
     */
    RebuildServerRequest,

    /**
     * The RemoveFromResourcesRequest model constructor.
     * @property {module:model/RemoveFromResourcesRequest}
     */
    RemoveFromResourcesRequest,

    /**
     * The RemoveTargetRequest model constructor.
     * @property {module:model/RemoveTargetRequest}
     */
    RemoveTargetRequest,

    /**
     * The Rule model constructor.
     * @property {module:model/Rule}
     */
    Rule,

    /**
     * The ServerPublicNetFirewall model constructor.
     * @property {module:model/ServerPublicNetFirewall}
     */
    ServerPublicNetFirewall,

    /**
     * The ServerTypesGet200Response model constructor.
     * @property {module:model/ServerTypesGet200Response}
     */
    ServerTypesGet200Response,

    /**
     * The ServerTypesGet200ResponseServerTypesInner model constructor.
     * @property {module:model/ServerTypesGet200ResponseServerTypesInner}
     */
    ServerTypesGet200ResponseServerTypesInner,

    /**
     * The ServerTypesIdGet200Response model constructor.
     * @property {module:model/ServerTypesIdGet200Response}
     */
    ServerTypesIdGet200Response,

    /**
     * The ServersGet200Response model constructor.
     * @property {module:model/ServersGet200Response}
     */
    ServersGet200Response,

    /**
     * The ServersGet200ResponseServersInner model constructor.
     * @property {module:model/ServersGet200ResponseServersInner}
     */
    ServersGet200ResponseServersInner,

    /**
     * The ServersGet200ResponseServersInnerDatacenter model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerDatacenter}
     */
    ServersGet200ResponseServersInnerDatacenter,

    /**
     * The ServersGet200ResponseServersInnerImage model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerImage}
     */
    ServersGet200ResponseServersInnerImage,

    /**
     * The ServersGet200ResponseServersInnerIso model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerIso}
     */
    ServersGet200ResponseServersInnerIso,

    /**
     * The ServersGet200ResponseServersInnerPrivateNetInner model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerPrivateNetInner}
     */
    ServersGet200ResponseServersInnerPrivateNetInner,

    /**
     * The ServersGet200ResponseServersInnerProtection model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerProtection}
     */
    ServersGet200ResponseServersInnerProtection,

    /**
     * The ServersGet200ResponseServersInnerPublicNet model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerPublicNet}
     */
    ServersGet200ResponseServersInnerPublicNet,

    /**
     * The ServersGet200ResponseServersInnerPublicNetIpv4 model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerPublicNetIpv4}
     */
    ServersGet200ResponseServersInnerPublicNetIpv4,

    /**
     * The ServersGet200ResponseServersInnerPublicNetIpv6 model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerPublicNetIpv6}
     */
    ServersGet200ResponseServersInnerPublicNetIpv6,

    /**
     * The ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner}
     */
    ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner,

    /**
     * The ServersGet200ResponseServersInnerServerType model constructor.
     * @property {module:model/ServersGet200ResponseServersInnerServerType}
     */
    ServersGet200ResponseServersInnerServerType,

    /**
     * The ServersIdActionsAttachIsoPostRequest model constructor.
     * @property {module:model/ServersIdActionsAttachIsoPostRequest}
     */
    ServersIdActionsAttachIsoPostRequest,

    /**
     * The ServersIdActionsChangeAliasIpsPostRequest model constructor.
     * @property {module:model/ServersIdActionsChangeAliasIpsPostRequest}
     */
    ServersIdActionsChangeAliasIpsPostRequest,

    /**
     * The ServersIdActionsChangeDnsPtrPostRequest model constructor.
     * @property {module:model/ServersIdActionsChangeDnsPtrPostRequest}
     */
    ServersIdActionsChangeDnsPtrPostRequest,

    /**
     * The ServersIdActionsChangeProtectionPostRequest model constructor.
     * @property {module:model/ServersIdActionsChangeProtectionPostRequest}
     */
    ServersIdActionsChangeProtectionPostRequest,

    /**
     * The ServersIdActionsChangeTypePostRequest model constructor.
     * @property {module:model/ServersIdActionsChangeTypePostRequest}
     */
    ServersIdActionsChangeTypePostRequest,

    /**
     * The ServersIdActionsCreateImagePost201Response model constructor.
     * @property {module:model/ServersIdActionsCreateImagePost201Response}
     */
    ServersIdActionsCreateImagePost201Response,

    /**
     * The ServersIdActionsEnableRescuePost201Response model constructor.
     * @property {module:model/ServersIdActionsEnableRescuePost201Response}
     */
    ServersIdActionsEnableRescuePost201Response,

    /**
     * The ServersIdActionsEnableRescuePostRequest model constructor.
     * @property {module:model/ServersIdActionsEnableRescuePostRequest}
     */
    ServersIdActionsEnableRescuePostRequest,

    /**
     * The ServersIdActionsRebuildPost201Response model constructor.
     * @property {module:model/ServersIdActionsRebuildPost201Response}
     */
    ServersIdActionsRebuildPost201Response,

    /**
     * The ServersIdActionsRequestConsolePost201Response model constructor.
     * @property {module:model/ServersIdActionsRequestConsolePost201Response}
     */
    ServersIdActionsRequestConsolePost201Response,

    /**
     * The ServersIdDelete200Response model constructor.
     * @property {module:model/ServersIdDelete200Response}
     */
    ServersIdDelete200Response,

    /**
     * The ServersIdGet200Response model constructor.
     * @property {module:model/ServersIdGet200Response}
     */
    ServersIdGet200Response,

    /**
     * The SetRulesRequest model constructor.
     * @property {module:model/SetRulesRequest}
     */
    SetRulesRequest,

    /**
     * The SshKeysGet200Response model constructor.
     * @property {module:model/SshKeysGet200Response}
     */
    SshKeysGet200Response,

    /**
     * The SshKeysGet200ResponseSshKeysInner model constructor.
     * @property {module:model/SshKeysGet200ResponseSshKeysInner}
     */
    SshKeysGet200ResponseSshKeysInner,

    /**
     * The SshKeysIdPutRequest model constructor.
     * @property {module:model/SshKeysIdPutRequest}
     */
    SshKeysIdPutRequest,

    /**
     * The SshKeysPost201Response model constructor.
     * @property {module:model/SshKeysPost201Response}
     */
    SshKeysPost201Response,

    /**
     * The SshKeysPostRequest model constructor.
     * @property {module:model/SshKeysPostRequest}
     */
    SshKeysPostRequest,

    /**
     * The UpdateCertificateRequest model constructor.
     * @property {module:model/UpdateCertificateRequest}
     */
    UpdateCertificateRequest,

    /**
     * The UpdateFirewallRequest model constructor.
     * @property {module:model/UpdateFirewallRequest}
     */
    UpdateFirewallRequest,

    /**
     * The UpdateFloatingIPRequest model constructor.
     * @property {module:model/UpdateFloatingIPRequest}
     */
    UpdateFloatingIPRequest,

    /**
     * The UpdateImageRequest model constructor.
     * @property {module:model/UpdateImageRequest}
     */
    UpdateImageRequest,

    /**
     * The UpdateNetworkRequest model constructor.
     * @property {module:model/UpdateNetworkRequest}
     */
    UpdateNetworkRequest,

    /**
     * The UpdateNetworkRequestLabels model constructor.
     * @property {module:model/UpdateNetworkRequestLabels}
     */
    UpdateNetworkRequestLabels,

    /**
     * The UpdatePlacementGroupRequest model constructor.
     * @property {module:model/UpdatePlacementGroupRequest}
     */
    UpdatePlacementGroupRequest,

    /**
     * The UpdatePrimaryIPRequest model constructor.
     * @property {module:model/UpdatePrimaryIPRequest}
     */
    UpdatePrimaryIPRequest,

    /**
     * The UpdateServerRequest model constructor.
     * @property {module:model/UpdateServerRequest}
     */
    UpdateServerRequest,

    /**
     * The UpdateVolumeRequest model constructor.
     * @property {module:model/UpdateVolumeRequest}
     */
    UpdateVolumeRequest,

    /**
     * The VolumesGet200Response model constructor.
     * @property {module:model/VolumesGet200Response}
     */
    VolumesGet200Response,

    /**
     * The VolumesGet200ResponseVolumesInner model constructor.
     * @property {module:model/VolumesGet200ResponseVolumesInner}
     */
    VolumesGet200ResponseVolumesInner,

    /**
     * The VolumesGet200ResponseVolumesInnerLocation model constructor.
     * @property {module:model/VolumesGet200ResponseVolumesInnerLocation}
     */
    VolumesGet200ResponseVolumesInnerLocation,

    /**
     * The VolumesIdActionsChangeProtectionPostRequest model constructor.
     * @property {module:model/VolumesIdActionsChangeProtectionPostRequest}
     */
    VolumesIdActionsChangeProtectionPostRequest,

    /**
     * The VolumesIdActionsResizePostRequest model constructor.
     * @property {module:model/VolumesIdActionsResizePostRequest}
     */
    VolumesIdActionsResizePostRequest,

    /**
     * The VolumesIdGet200Response model constructor.
     * @property {module:model/VolumesIdGet200Response}
     */
    VolumesIdGet200Response,

    /**
     * The VolumesPost201Response model constructor.
     * @property {module:model/VolumesPost201Response}
     */
    VolumesPost201Response,

    /**
    * The ActionsApi service constructor.
    * @property {module:api/ActionsApi}
    */
    ActionsApi,

    /**
    * The CertificateActionsApi service constructor.
    * @property {module:api/CertificateActionsApi}
    */
    CertificateActionsApi,

    /**
    * The CertificatesApi service constructor.
    * @property {module:api/CertificatesApi}
    */
    CertificatesApi,

    /**
    * The DatacentersApi service constructor.
    * @property {module:api/DatacentersApi}
    */
    DatacentersApi,

    /**
    * The FirewallActionsApi service constructor.
    * @property {module:api/FirewallActionsApi}
    */
    FirewallActionsApi,

    /**
    * The FirewallsApi service constructor.
    * @property {module:api/FirewallsApi}
    */
    FirewallsApi,

    /**
    * The FloatingIPActionsApi service constructor.
    * @property {module:api/FloatingIPActionsApi}
    */
    FloatingIPActionsApi,

    /**
    * The FloatingIPsApi service constructor.
    * @property {module:api/FloatingIPsApi}
    */
    FloatingIPsApi,

    /**
    * The ISOsApi service constructor.
    * @property {module:api/ISOsApi}
    */
    ISOsApi,

    /**
    * The ImageActionsApi service constructor.
    * @property {module:api/ImageActionsApi}
    */
    ImageActionsApi,

    /**
    * The ImagesApi service constructor.
    * @property {module:api/ImagesApi}
    */
    ImagesApi,

    /**
    * The LoadBalancerActionsApi service constructor.
    * @property {module:api/LoadBalancerActionsApi}
    */
    LoadBalancerActionsApi,

    /**
    * The LoadBalancerTypesApi service constructor.
    * @property {module:api/LoadBalancerTypesApi}
    */
    LoadBalancerTypesApi,

    /**
    * The LoadBalancersApi service constructor.
    * @property {module:api/LoadBalancersApi}
    */
    LoadBalancersApi,

    /**
    * The LocationsApi service constructor.
    * @property {module:api/LocationsApi}
    */
    LocationsApi,

    /**
    * The NetworkActionsApi service constructor.
    * @property {module:api/NetworkActionsApi}
    */
    NetworkActionsApi,

    /**
    * The NetworksApi service constructor.
    * @property {module:api/NetworksApi}
    */
    NetworksApi,

    /**
    * The PlacementGroupsApi service constructor.
    * @property {module:api/PlacementGroupsApi}
    */
    PlacementGroupsApi,

    /**
    * The PricingApi service constructor.
    * @property {module:api/PricingApi}
    */
    PricingApi,

    /**
    * The PrimaryIPActionsApi service constructor.
    * @property {module:api/PrimaryIPActionsApi}
    */
    PrimaryIPActionsApi,

    /**
    * The PrimaryIPsApi service constructor.
    * @property {module:api/PrimaryIPsApi}
    */
    PrimaryIPsApi,

    /**
    * The SSHKeysApi service constructor.
    * @property {module:api/SSHKeysApi}
    */
    SSHKeysApi,

    /**
    * The ServerActionsApi service constructor.
    * @property {module:api/ServerActionsApi}
    */
    ServerActionsApi,

    /**
    * The ServerTypesApi service constructor.
    * @property {module:api/ServerTypesApi}
    */
    ServerTypesApi,

    /**
    * The ServersApi service constructor.
    * @property {module:api/ServersApi}
    */
    ServersApi,

    /**
    * The VolumeActionsApi service constructor.
    * @property {module:api/VolumeActionsApi}
    */
    VolumeActionsApi,

    /**
    * The VolumesApi service constructor.
    * @property {module:api/VolumesApi}
    */
    VolumesApi
};
