# openapi-java-client

Hetzner Cloud API
- API version: 1.0.0
  - Build date: 2024-10-12T12:42:41.028370-04:00[America/New_York]
  - Generator version: 7.9.0

This is the official API documentation for the Public Hetzner Cloud.

## Introduction

The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.

As an alternative to working directly with our API you may also consider to use:
* Our CLI program [hcloud](https://github.com/hetznercloud/cli)
* Our [library for Go](https://github.com/hetznercloud/hcloud-go)
* Our [library for Python](https://github.com/hetznercloud/hcloud-python)

Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).

If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following:
* The type of integration you would like to develop
* Link to the GitHub repo you will use for the Project
* Link to some other Open Source work you have already done (if you have done so)

## Getting Started
To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is `jEheVytlAoFl7F8MqUQ7jAo2hOXASztX`.

You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.haxx.se/).

Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like `servers` inside the example response. A response can also contain a `meta` object with information like [Pagination](https://docs.hetzner.cloud/#overview-pagination).

**Example Request**
```bash
curl -H \"Authorization: Bearer jEheVytlAoFl7F8MqUQ7jAo2hOXASztX\" \\
    https://api.hetzner.cloud/v1/servers
```

**Example Response**
```json
{
    \"servers\": [],
    \"meta\": {
        \"pagination\": {
            \"page\": 1,
            \"per_page\": 25,
            \"previous_page\": null,
            \"next_page\": null,
            \"last_page\": 1,
            \"total_entries\": 0
        }
    }
}
```

## Authentication
All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the `Authorization` HTTP header.

To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token.

**Example Authorization header**
```html
Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj
```

## Errors
Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.

The error response contains the following keys:

| Keys      | Meaning                                                               |
|-----------|-----------------------------------------------------------------------|
| `code`    | Short string indicating the type of error (machine-parsable)          |
| `message` | Textual description on what has gone wrong                            |
| `details` | An object providing for details on the error (schema depends on code) |

**Example response**
```json
{
  \"error\": {
    \"code\": \"invalid_input\",
    \"message\": \"invalid input in field 'broken_field': is too long\",
    \"details\": {
      \"fields\": [
        {
          \"name\": \"broken_field\",
          \"messages\": [\"is too long\"]
        }
      ]
    }
  }
}
```

### Error Codes

| Code                      | Description                                                                      |
|---------------------------|----------------------------------------------------------------------------------|
| `forbidden`               | Insufficient permissions for this request                                        |
| `invalid_input`           | Error while parsing or processing the input                                      |
| `json_error`              | Invalid JSON input in your request                                               |
| `locked`                  | The item you are trying to access is locked (there is already an Action running) |
| `not_found`               | Entity not found                                                                 |
| `rate_limit_exceeded`     | Error when sending too many requests                                             |
| `resource_limit_exceeded` | Error when exceeding the maximum quantity of a resource for an account           |
| `resource_unavailable`    | The requested resource is currently unavailable                                  |
| `service_error`           | Error within a service                                                           |
| `uniqueness_error`        | One or more of the objects fields must be unique                                 |
| `protected`               | The Action you are trying to start is protected for this resource                |
| `maintenance`             | Cannot perform operation due to maintenance                                      |
| `conflict`                | The resource has changed during the request, please retry                        |
| `unsupported_error`       | The corresponding resource does not support the Action                           |
| `token_readonly`          | The token is only allowed to perform GET requests                                |
| `unavailable`             | A service or product is currently not available                                  |

**invalid_input**
```json
{
  \"error\": {
    \"code\": \"invalid_input\",
    \"message\": \"invalid input in field 'broken_field': is too long\",
    \"details\": {
      \"fields\": [
        {
          \"name\": \"broken_field\",
          \"messages\": [\"is too long\"]
        }
      ]
    }
  }
}
```

**uniqueness_error**
```json
{
  \"error\": {
    \"code\": \"uniqueness_error\",
    \"message\": \"SSH key with the same fingerprint already exists\",
    \"details\": {
      \"fields\": [
        {
          \"name\": \"public_key\"
        }
      ]
    }
  }
}
```

**resource_limit_exceeded**
```json
{
  \"error\": {
    \"code\": \"resource_limit_exceeded\",
    \"message\": \"project limit exceeded\",
    \"details\": {
      \"limits\": [
        {
          \"name\": \"project_limit\"
        }
      ]
    }
  }
}
```

## Labels
Labels are `key/value` pairs that can be attached to all resources.

Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).

Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.

The `hetzner.cloud/` prefix is reserved and cannot be used.

**Example Labels**
```json
{
  \"labels\": {
    \"environment\":\"development\",
    \"service\":\"backend\",
    \"example.com/my\":\"label\",
    \"just-a-key\":\"\"
  }
}
```

## Label Selector
For resources with labels, you can filter resources by their labels using the label selector query language.

| Expression           | Meaning                                                             |
|----------------------|---------------------------------------------------------------------|
| `k==v` / `k=v`       | Value of key `k` does equal value `v`                               |
| `k!=v`               | Value of key `k` does not equal value `v`                           |
| `k`                  | Key `k` is present                                                  |
| `!k`                 | Key `k` is not present                                              |
| `k in (v1,v2,v3)`    | Value of key `k` is `v1`, `v2`, or `v3`                             |
| `k notin (v1,v2,v3)` | Value of key `k` is neither `v1`, nor `v2`, nor `v3`                |
| `k1==v,!k2`          | Value of key `k1` is `v` and key `k2` is not present                |

### Examples
* Returns all resources that have a `env=production` label and that don't have a `type=database` label:

  `env=production,type!=database`
* Returns all resources that have a `env=testing` or `env=staging` label:

    `env in (testing,staging)`
* Returns all resources that don't have a `type` label:

    `!type`

## Pagination
Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:

* A `page` parameter specifies the page to fetch. The number of the first page is 1.
* A `per_page` parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.

Responses contain a `Link` header with pagination information.

Additionally, if the response body is JSON and the root object is an object, that object has a `pagination` object inside the `meta` object with pagination information:

**Example Pagination**
```json
{
    \"servers\": [...],
    \"meta\": {
        \"pagination\": {
            \"page\": 2,
            \"per_page\": 25,
            \"previous_page\": 1,
            \"next_page\": 3,
            \"last_page\": 4,
            \"total_entries\": 100
        }
    }
}
```

The keys `previous_page`, `next_page`, `last_page`, and `total_entries` may be `null` when on the first page, last page, or when the total number of entries is unknown.

**Example Pagination Link header**
```bash
Link: <https://api.hetzner.cloud/v1/actions?page=2&per_page=5>; rel=\"prev\",
      <https://api.hetzner.cloud/v1/actions?page=4&per_page=5>; rel=\"next\",
      <https://api.hetzner.cloud/v1/actions?page=6&per_page=5>; rel=\"last\"
```

Line breaks have been added for display purposes only and responses may only contain some of the above `rel` values.

## Rate Limiting
All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a `429 Too Many Requests` error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.

* The `RateLimit-Limit` header contains the total number of requests you can perform per hour.
* The `RateLimit-Remaining` header contains the number of requests remaining in the current rate limit time frame.
* The `RateLimit-Reset` header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.

The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.

## Server Metadata
Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:

| Data              | Format | Contents                                                     |
|-------------------|--------|--------------------------------------------------------------|
| hostname          | text   | Name of the Server as set in the api                         |
| instance-id       | number | ID of the server                                             |
| public-ipv4       | text   | Primary public IPv4 address                                  |
| private-networks  | yaml   | Details about the private networks the Server is attached to |
| availability-zone | text   | Name of the availability zone that Server runs in            |
| region            | text   | Network zone, e.g. eu-central                                |

**Example: Summary**
```bash
$ curl http://169.254.169.254/hetzner/v1/metadata
```

```yaml
availability-zone: hel1-dc2
hostname: my-server
instance-id: 42
public-ipv4: 1.2.3.4
region: eu-central
```

**Example: Hostname**
```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/hostname
my-server
```

**Example: Instance ID**
```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/instance-id
42
```

**Example: Public IPv4**
```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4
1.2.3.4
```

**Example: Private Networks**
```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/private-networks
```

```json
- ip: 10.0.0.2
  alias_ips: [10.0.0.3, 10.0.0.4]
  interface_num: 1
  mac_address: 86:00:00:2a:7d:e0
  network_id: 1234
  network_name: nw-test1
  network: 10.0.0.0/8
  subnet: 10.0.0.0/24
  gateway: 10.0.0.1
- ip: 192.168.0.2
  alias_ips: []
  interface_num: 2
  mac_address: 86:00:00:2a:7d:e1
  network_id: 4321
  network_name: nw-test2
  network: 192.168.0.0/16
  subnet: 192.168.0.0/24
  gateway: 192.168.0.1
```

**Example: Availability Zone**
```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone
hel1-dc2
```

**Example: Region**
```bash
$ curl http://169.254.169.254/hetzner/v1/metadata/region
eu-central
```

## Sorting
Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the `sort` query string parameter. You can sort by multiple fields. You can set the sort direction by appending `:asc` or `:desc` to the field name. By default, ascending sorting is used.

**Example: Sorting**
```bash
https://api.hetzner.cloud/v1/actions?sort=status
https://api.hetzner.cloud/v1/actions?sort=status:asc
https://api.hetzner.cloud/v1/actions?sort=status:desc
https://api.hetzner.cloud/v1/actions?sort=status:asc&sort=command:desc
```



*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    Integer id = 56; // Integer | Can be used multiple times, the response will contain only Actions with specified IDs
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      ActionsResponse result = apiInstance.actionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.hetzner.cloud/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActionsApi* | [**actionsGet**](docs/ActionsApi.md#actionsGet) | **GET** /actions | Get all Actions
*ActionsApi* | [**actionsIdGet**](docs/ActionsApi.md#actionsIdGet) | **GET** /actions/{id} | Get an Action
*CertificateActionsApi* | [**certificatesIdActionsActionIdGet**](docs/CertificateActionsApi.md#certificatesIdActionsActionIdGet) | **GET** /certificates/{id}/actions/{action_id} | Get an Action for a Certificate
*CertificateActionsApi* | [**certificatesIdActionsGet**](docs/CertificateActionsApi.md#certificatesIdActionsGet) | **GET** /certificates/{id}/actions | Get all Actions for a Certificate
*CertificateActionsApi* | [**certificatesIdActionsRetryPost**](docs/CertificateActionsApi.md#certificatesIdActionsRetryPost) | **POST** /certificates/{id}/actions/retry | Retry Issuance or Renewal
*CertificatesApi* | [**certificatesGet**](docs/CertificatesApi.md#certificatesGet) | **GET** /certificates | Get all Certificates
*CertificatesApi* | [**certificatesIdDelete**](docs/CertificatesApi.md#certificatesIdDelete) | **DELETE** /certificates/{id} | Delete a Certificate
*CertificatesApi* | [**certificatesIdGet**](docs/CertificatesApi.md#certificatesIdGet) | **GET** /certificates/{id} | Get a Certificate
*CertificatesApi* | [**certificatesIdPut**](docs/CertificatesApi.md#certificatesIdPut) | **PUT** /certificates/{id} | Update a Certificate
*CertificatesApi* | [**certificatesPost**](docs/CertificatesApi.md#certificatesPost) | **POST** /certificates | Create a Certificate
*DatacentersApi* | [**datacentersGet**](docs/DatacentersApi.md#datacentersGet) | **GET** /datacenters | Get all Datacenters
*DatacentersApi* | [**datacentersIdGet**](docs/DatacentersApi.md#datacentersIdGet) | **GET** /datacenters/{id} | Get a Datacenter
*FirewallActionsApi* | [**firewallsIdActionsActionIdGet**](docs/FirewallActionsApi.md#firewallsIdActionsActionIdGet) | **GET** /firewalls/{id}/actions/{action_id} | Get an Action for a Firewall
*FirewallActionsApi* | [**firewallsIdActionsApplyToResourcesPost**](docs/FirewallActionsApi.md#firewallsIdActionsApplyToResourcesPost) | **POST** /firewalls/{id}/actions/apply_to_resources | Apply to Resources
*FirewallActionsApi* | [**firewallsIdActionsGet**](docs/FirewallActionsApi.md#firewallsIdActionsGet) | **GET** /firewalls/{id}/actions | Get all Actions for a Firewall
*FirewallActionsApi* | [**firewallsIdActionsRemoveFromResourcesPost**](docs/FirewallActionsApi.md#firewallsIdActionsRemoveFromResourcesPost) | **POST** /firewalls/{id}/actions/remove_from_resources | Remove from Resources
*FirewallActionsApi* | [**firewallsIdActionsSetRulesPost**](docs/FirewallActionsApi.md#firewallsIdActionsSetRulesPost) | **POST** /firewalls/{id}/actions/set_rules | Set Rules
*FirewallsApi* | [**firewallsGet**](docs/FirewallsApi.md#firewallsGet) | **GET** /firewalls | Get all Firewalls
*FirewallsApi* | [**firewallsIdDelete**](docs/FirewallsApi.md#firewallsIdDelete) | **DELETE** /firewalls/{id} | Delete a Firewall
*FirewallsApi* | [**firewallsIdGet**](docs/FirewallsApi.md#firewallsIdGet) | **GET** /firewalls/{id} | Get a Firewall
*FirewallsApi* | [**firewallsIdPut**](docs/FirewallsApi.md#firewallsIdPut) | **PUT** /firewalls/{id} | Update a Firewall
*FirewallsApi* | [**firewallsPost**](docs/FirewallsApi.md#firewallsPost) | **POST** /firewalls | Create a Firewall
*FloatingIpActionsApi* | [**floatingIpsIdActionsActionIdGet**](docs/FloatingIpActionsApi.md#floatingIpsIdActionsActionIdGet) | **GET** /floating_ips/{id}/actions/{action_id} | Get an Action for a Floating IP
*FloatingIpActionsApi* | [**floatingIpsIdActionsAssignPost**](docs/FloatingIpActionsApi.md#floatingIpsIdActionsAssignPost) | **POST** /floating_ips/{id}/actions/assign | Assign a Floating IP to a Server
*FloatingIpActionsApi* | [**floatingIpsIdActionsChangeDnsPtrPost**](docs/FloatingIpActionsApi.md#floatingIpsIdActionsChangeDnsPtrPost) | **POST** /floating_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Floating IP
*FloatingIpActionsApi* | [**floatingIpsIdActionsChangeProtectionPost**](docs/FloatingIpActionsApi.md#floatingIpsIdActionsChangeProtectionPost) | **POST** /floating_ips/{id}/actions/change_protection | Change Floating IP Protection
*FloatingIpActionsApi* | [**floatingIpsIdActionsGet**](docs/FloatingIpActionsApi.md#floatingIpsIdActionsGet) | **GET** /floating_ips/{id}/actions | Get all Actions for a Floating IP
*FloatingIpActionsApi* | [**floatingIpsIdActionsUnassignPost**](docs/FloatingIpActionsApi.md#floatingIpsIdActionsUnassignPost) | **POST** /floating_ips/{id}/actions/unassign | Unassign a Floating IP
*FloatingIpsApi* | [**floatingIpsGet**](docs/FloatingIpsApi.md#floatingIpsGet) | **GET** /floating_ips | Get all Floating IPs
*FloatingIpsApi* | [**floatingIpsIdDelete**](docs/FloatingIpsApi.md#floatingIpsIdDelete) | **DELETE** /floating_ips/{id} | Delete a Floating IP
*FloatingIpsApi* | [**floatingIpsIdGet**](docs/FloatingIpsApi.md#floatingIpsIdGet) | **GET** /floating_ips/{id} | Get a Floating IP
*FloatingIpsApi* | [**floatingIpsIdPut**](docs/FloatingIpsApi.md#floatingIpsIdPut) | **PUT** /floating_ips/{id} | Update a Floating IP
*FloatingIpsApi* | [**floatingIpsPost**](docs/FloatingIpsApi.md#floatingIpsPost) | **POST** /floating_ips | Create a Floating IP
*ImageActionsApi* | [**imagesIdActionsActionIdGet**](docs/ImageActionsApi.md#imagesIdActionsActionIdGet) | **GET** /images/{id}/actions/{action_id} | Get an Action for an Image
*ImageActionsApi* | [**imagesIdActionsChangeProtectionPost**](docs/ImageActionsApi.md#imagesIdActionsChangeProtectionPost) | **POST** /images/{id}/actions/change_protection | Change Image Protection
*ImageActionsApi* | [**imagesIdActionsGet**](docs/ImageActionsApi.md#imagesIdActionsGet) | **GET** /images/{id}/actions | Get all Actions for an Image
*ImagesApi* | [**imagesGet**](docs/ImagesApi.md#imagesGet) | **GET** /images | Get all Images
*ImagesApi* | [**imagesIdDelete**](docs/ImagesApi.md#imagesIdDelete) | **DELETE** /images/{id} | Delete an Image
*ImagesApi* | [**imagesIdGet**](docs/ImagesApi.md#imagesIdGet) | **GET** /images/{id} | Get an Image
*ImagesApi* | [**imagesIdPut**](docs/ImagesApi.md#imagesIdPut) | **PUT** /images/{id} | Update an Image
*IsosApi* | [**isosGet**](docs/IsosApi.md#isosGet) | **GET** /isos | Get all ISOs
*IsosApi* | [**isosIdGet**](docs/IsosApi.md#isosIdGet) | **GET** /isos/{id} | Get an ISO
*LoadBalancerActionsApi* | [**loadBalancersIdActionsActionIdGet**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsActionIdGet) | **GET** /load_balancers/{id}/actions/{action_id} | Get an Action for a Load Balancer
*LoadBalancerActionsApi* | [**loadBalancersIdActionsAddServicePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsAddServicePost) | **POST** /load_balancers/{id}/actions/add_service | Add Service
*LoadBalancerActionsApi* | [**loadBalancersIdActionsAddTargetPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsAddTargetPost) | **POST** /load_balancers/{id}/actions/add_target | Add Target
*LoadBalancerActionsApi* | [**loadBalancersIdActionsAttachToNetworkPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsAttachToNetworkPost) | **POST** /load_balancers/{id}/actions/attach_to_network | Attach a Load Balancer to a Network
*LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeAlgorithmPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeAlgorithmPost) | **POST** /load_balancers/{id}/actions/change_algorithm | Change Algorithm
*LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeDnsPtrPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeDnsPtrPost) | **POST** /load_balancers/{id}/actions/change_dns_ptr | Change reverse DNS entry for this Load Balancer
*LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeProtectionPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeProtectionPost) | **POST** /load_balancers/{id}/actions/change_protection | Change Load Balancer Protection
*LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeTypePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeTypePost) | **POST** /load_balancers/{id}/actions/change_type | Change the Type of a Load Balancer
*LoadBalancerActionsApi* | [**loadBalancersIdActionsDeleteServicePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsDeleteServicePost) | **POST** /load_balancers/{id}/actions/delete_service | Delete Service
*LoadBalancerActionsApi* | [**loadBalancersIdActionsDetachFromNetworkPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsDetachFromNetworkPost) | **POST** /load_balancers/{id}/actions/detach_from_network | Detach a Load Balancer from a Network
*LoadBalancerActionsApi* | [**loadBalancersIdActionsDisablePublicInterfacePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsDisablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/disable_public_interface | Disable the public interface of a Load Balancer
*LoadBalancerActionsApi* | [**loadBalancersIdActionsEnablePublicInterfacePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsEnablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/enable_public_interface | Enable the public interface of a Load Balancer
*LoadBalancerActionsApi* | [**loadBalancersIdActionsGet**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsGet) | **GET** /load_balancers/{id}/actions | Get all Actions for a Load Balancer
*LoadBalancerActionsApi* | [**loadBalancersIdActionsRemoveTargetPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsRemoveTargetPost) | **POST** /load_balancers/{id}/actions/remove_target | Remove Target
*LoadBalancerActionsApi* | [**loadBalancersIdActionsUpdateServicePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsUpdateServicePost) | **POST** /load_balancers/{id}/actions/update_service | Update Service
*LoadBalancerTypesApi* | [**loadBalancerTypesGet**](docs/LoadBalancerTypesApi.md#loadBalancerTypesGet) | **GET** /load_balancer_types | Get all Load Balancer Types
*LoadBalancerTypesApi* | [**loadBalancerTypesIdGet**](docs/LoadBalancerTypesApi.md#loadBalancerTypesIdGet) | **GET** /load_balancer_types/{id} | Get a Load Balancer Type
*LoadBalancersApi* | [**loadBalancersGet**](docs/LoadBalancersApi.md#loadBalancersGet) | **GET** /load_balancers | Get all Load Balancers
*LoadBalancersApi* | [**loadBalancersIdDelete**](docs/LoadBalancersApi.md#loadBalancersIdDelete) | **DELETE** /load_balancers/{id} | Delete a Load Balancer
*LoadBalancersApi* | [**loadBalancersIdGet**](docs/LoadBalancersApi.md#loadBalancersIdGet) | **GET** /load_balancers/{id} | Get a Load Balancer
*LoadBalancersApi* | [**loadBalancersIdMetricsGet**](docs/LoadBalancersApi.md#loadBalancersIdMetricsGet) | **GET** /load_balancers/{id}/metrics | Get Metrics for a LoadBalancer
*LoadBalancersApi* | [**loadBalancersIdPut**](docs/LoadBalancersApi.md#loadBalancersIdPut) | **PUT** /load_balancers/{id} | Update a Load Balancer
*LoadBalancersApi* | [**loadBalancersPost**](docs/LoadBalancersApi.md#loadBalancersPost) | **POST** /load_balancers | Create a Load Balancer
*LocationsApi* | [**locationsGet**](docs/LocationsApi.md#locationsGet) | **GET** /locations | Get all Locations
*LocationsApi* | [**locationsIdGet**](docs/LocationsApi.md#locationsIdGet) | **GET** /locations/{id} | Get a Location
*NetworkActionsApi* | [**networksIdActionsActionIdGet**](docs/NetworkActionsApi.md#networksIdActionsActionIdGet) | **GET** /networks/{id}/actions/{action_id} | Get an Action for a Network
*NetworkActionsApi* | [**networksIdActionsAddRoutePost**](docs/NetworkActionsApi.md#networksIdActionsAddRoutePost) | **POST** /networks/{id}/actions/add_route | Add a route to a Network
*NetworkActionsApi* | [**networksIdActionsAddSubnetPost**](docs/NetworkActionsApi.md#networksIdActionsAddSubnetPost) | **POST** /networks/{id}/actions/add_subnet | Add a subnet to a Network
*NetworkActionsApi* | [**networksIdActionsChangeIpRangePost**](docs/NetworkActionsApi.md#networksIdActionsChangeIpRangePost) | **POST** /networks/{id}/actions/change_ip_range | Change IP range of a Network
*NetworkActionsApi* | [**networksIdActionsChangeProtectionPost**](docs/NetworkActionsApi.md#networksIdActionsChangeProtectionPost) | **POST** /networks/{id}/actions/change_protection | Change Network Protection
*NetworkActionsApi* | [**networksIdActionsDeleteRoutePost**](docs/NetworkActionsApi.md#networksIdActionsDeleteRoutePost) | **POST** /networks/{id}/actions/delete_route | Delete a route from a Network
*NetworkActionsApi* | [**networksIdActionsDeleteSubnetPost**](docs/NetworkActionsApi.md#networksIdActionsDeleteSubnetPost) | **POST** /networks/{id}/actions/delete_subnet | Delete a subnet from a Network
*NetworkActionsApi* | [**networksIdActionsGet**](docs/NetworkActionsApi.md#networksIdActionsGet) | **GET** /networks/{id}/actions | Get all Actions for a Network
*NetworksApi* | [**networksGet**](docs/NetworksApi.md#networksGet) | **GET** /networks | Get all Networks
*NetworksApi* | [**networksIdDelete**](docs/NetworksApi.md#networksIdDelete) | **DELETE** /networks/{id} | Delete a Network
*NetworksApi* | [**networksIdGet**](docs/NetworksApi.md#networksIdGet) | **GET** /networks/{id} | Get a Network
*NetworksApi* | [**networksIdPut**](docs/NetworksApi.md#networksIdPut) | **PUT** /networks/{id} | Update a Network
*NetworksApi* | [**networksPost**](docs/NetworksApi.md#networksPost) | **POST** /networks | Create a Network
*PlacementGroupsApi* | [**placementGroupsGet**](docs/PlacementGroupsApi.md#placementGroupsGet) | **GET** /placement_groups | Get all PlacementGroups
*PlacementGroupsApi* | [**placementGroupsIdDelete**](docs/PlacementGroupsApi.md#placementGroupsIdDelete) | **DELETE** /placement_groups/{id} | Delete a PlacementGroup
*PlacementGroupsApi* | [**placementGroupsIdGet**](docs/PlacementGroupsApi.md#placementGroupsIdGet) | **GET** /placement_groups/{id} | Get a PlacementGroup
*PlacementGroupsApi* | [**placementGroupsIdPut**](docs/PlacementGroupsApi.md#placementGroupsIdPut) | **PUT** /placement_groups/{id} | Update a PlacementGroup
*PlacementGroupsApi* | [**placementGroupsPost**](docs/PlacementGroupsApi.md#placementGroupsPost) | **POST** /placement_groups | Create a PlacementGroup
*PricingApi* | [**pricingGet**](docs/PricingApi.md#pricingGet) | **GET** /pricing | Get all prices
*PrimaryIpActionsApi* | [**primaryIpsIdActionsAssignPost**](docs/PrimaryIpActionsApi.md#primaryIpsIdActionsAssignPost) | **POST** /primary_ips/{id}/actions/assign | Assign a Primary IP to a resource
*PrimaryIpActionsApi* | [**primaryIpsIdActionsChangeDnsPtrPost**](docs/PrimaryIpActionsApi.md#primaryIpsIdActionsChangeDnsPtrPost) | **POST** /primary_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Primary IP
*PrimaryIpActionsApi* | [**primaryIpsIdActionsChangeProtectionPost**](docs/PrimaryIpActionsApi.md#primaryIpsIdActionsChangeProtectionPost) | **POST** /primary_ips/{id}/actions/change_protection | Change Primary IP Protection
*PrimaryIpActionsApi* | [**primaryIpsIdActionsUnassignPost**](docs/PrimaryIpActionsApi.md#primaryIpsIdActionsUnassignPost) | **POST** /primary_ips/{id}/actions/unassign | Unassign a Primary IP from a resource
*PrimaryIpsApi* | [**primaryIpsGet**](docs/PrimaryIpsApi.md#primaryIpsGet) | **GET** /primary_ips | Get all Primary IPs
*PrimaryIpsApi* | [**primaryIpsIdDelete**](docs/PrimaryIpsApi.md#primaryIpsIdDelete) | **DELETE** /primary_ips/{id} | Delete a Primary IP
*PrimaryIpsApi* | [**primaryIpsIdGet**](docs/PrimaryIpsApi.md#primaryIpsIdGet) | **GET** /primary_ips/{id} | Get a Primary IP
*PrimaryIpsApi* | [**primaryIpsIdPut**](docs/PrimaryIpsApi.md#primaryIpsIdPut) | **PUT** /primary_ips/{id} | Update a Primary IP
*PrimaryIpsApi* | [**primaryIpsPost**](docs/PrimaryIpsApi.md#primaryIpsPost) | **POST** /primary_ips | Create a Primary IP
*ServerActionsApi* | [**serversIdActionsActionIdGet**](docs/ServerActionsApi.md#serversIdActionsActionIdGet) | **GET** /servers/{id}/actions/{action_id} | Get an Action for a Server
*ServerActionsApi* | [**serversIdActionsAddToPlacementGroupPost**](docs/ServerActionsApi.md#serversIdActionsAddToPlacementGroupPost) | **POST** /servers/{id}/actions/add_to_placement_group | Add a Server to a Placement Group
*ServerActionsApi* | [**serversIdActionsAttachIsoPost**](docs/ServerActionsApi.md#serversIdActionsAttachIsoPost) | **POST** /servers/{id}/actions/attach_iso | Attach an ISO to a Server
*ServerActionsApi* | [**serversIdActionsAttachToNetworkPost**](docs/ServerActionsApi.md#serversIdActionsAttachToNetworkPost) | **POST** /servers/{id}/actions/attach_to_network | Attach a Server to a Network
*ServerActionsApi* | [**serversIdActionsChangeAliasIpsPost**](docs/ServerActionsApi.md#serversIdActionsChangeAliasIpsPost) | **POST** /servers/{id}/actions/change_alias_ips | Change alias IPs of a Network
*ServerActionsApi* | [**serversIdActionsChangeDnsPtrPost**](docs/ServerActionsApi.md#serversIdActionsChangeDnsPtrPost) | **POST** /servers/{id}/actions/change_dns_ptr | Change reverse DNS entry for this Server
*ServerActionsApi* | [**serversIdActionsChangeProtectionPost**](docs/ServerActionsApi.md#serversIdActionsChangeProtectionPost) | **POST** /servers/{id}/actions/change_protection | Change Server Protection
*ServerActionsApi* | [**serversIdActionsChangeTypePost**](docs/ServerActionsApi.md#serversIdActionsChangeTypePost) | **POST** /servers/{id}/actions/change_type | Change the Type of a Server
*ServerActionsApi* | [**serversIdActionsCreateImagePost**](docs/ServerActionsApi.md#serversIdActionsCreateImagePost) | **POST** /servers/{id}/actions/create_image | Create Image from a Server
*ServerActionsApi* | [**serversIdActionsDetachFromNetworkPost**](docs/ServerActionsApi.md#serversIdActionsDetachFromNetworkPost) | **POST** /servers/{id}/actions/detach_from_network | Detach a Server from a Network
*ServerActionsApi* | [**serversIdActionsDetachIsoPost**](docs/ServerActionsApi.md#serversIdActionsDetachIsoPost) | **POST** /servers/{id}/actions/detach_iso | Detach an ISO from a Server
*ServerActionsApi* | [**serversIdActionsDisableBackupPost**](docs/ServerActionsApi.md#serversIdActionsDisableBackupPost) | **POST** /servers/{id}/actions/disable_backup | Disable Backups for a Server
*ServerActionsApi* | [**serversIdActionsDisableRescuePost**](docs/ServerActionsApi.md#serversIdActionsDisableRescuePost) | **POST** /servers/{id}/actions/disable_rescue | Disable Rescue Mode for a Server
*ServerActionsApi* | [**serversIdActionsEnableBackupPost**](docs/ServerActionsApi.md#serversIdActionsEnableBackupPost) | **POST** /servers/{id}/actions/enable_backup | Enable and Configure Backups for a Server
*ServerActionsApi* | [**serversIdActionsEnableRescuePost**](docs/ServerActionsApi.md#serversIdActionsEnableRescuePost) | **POST** /servers/{id}/actions/enable_rescue | Enable Rescue Mode for a Server
*ServerActionsApi* | [**serversIdActionsGet**](docs/ServerActionsApi.md#serversIdActionsGet) | **GET** /servers/{id}/actions | Get all Actions for a Server
*ServerActionsApi* | [**serversIdActionsPoweroffPost**](docs/ServerActionsApi.md#serversIdActionsPoweroffPost) | **POST** /servers/{id}/actions/poweroff | Power off a Server
*ServerActionsApi* | [**serversIdActionsPoweronPost**](docs/ServerActionsApi.md#serversIdActionsPoweronPost) | **POST** /servers/{id}/actions/poweron | Power on a Server
*ServerActionsApi* | [**serversIdActionsRebootPost**](docs/ServerActionsApi.md#serversIdActionsRebootPost) | **POST** /servers/{id}/actions/reboot | Soft-reboot a Server
*ServerActionsApi* | [**serversIdActionsRebuildPost**](docs/ServerActionsApi.md#serversIdActionsRebuildPost) | **POST** /servers/{id}/actions/rebuild | Rebuild a Server from an Image
*ServerActionsApi* | [**serversIdActionsRemoveFromPlacementGroupPost**](docs/ServerActionsApi.md#serversIdActionsRemoveFromPlacementGroupPost) | **POST** /servers/{id}/actions/remove_from_placement_group | Remove from Placement Group
*ServerActionsApi* | [**serversIdActionsRequestConsolePost**](docs/ServerActionsApi.md#serversIdActionsRequestConsolePost) | **POST** /servers/{id}/actions/request_console | Request Console for a Server
*ServerActionsApi* | [**serversIdActionsResetPasswordPost**](docs/ServerActionsApi.md#serversIdActionsResetPasswordPost) | **POST** /servers/{id}/actions/reset_password | Reset root Password of a Server
*ServerActionsApi* | [**serversIdActionsResetPost**](docs/ServerActionsApi.md#serversIdActionsResetPost) | **POST** /servers/{id}/actions/reset | Reset a Server
*ServerActionsApi* | [**serversIdActionsShutdownPost**](docs/ServerActionsApi.md#serversIdActionsShutdownPost) | **POST** /servers/{id}/actions/shutdown | Shutdown a Server
*ServerTypesApi* | [**serverTypesGet**](docs/ServerTypesApi.md#serverTypesGet) | **GET** /server_types | Get all Server Types
*ServerTypesApi* | [**serverTypesIdGet**](docs/ServerTypesApi.md#serverTypesIdGet) | **GET** /server_types/{id} | Get a Server Type
*ServersApi* | [**serversGet**](docs/ServersApi.md#serversGet) | **GET** /servers | Get all Servers
*ServersApi* | [**serversIdDelete**](docs/ServersApi.md#serversIdDelete) | **DELETE** /servers/{id} | Delete a Server
*ServersApi* | [**serversIdGet**](docs/ServersApi.md#serversIdGet) | **GET** /servers/{id} | Get a Server
*ServersApi* | [**serversIdMetricsGet**](docs/ServersApi.md#serversIdMetricsGet) | **GET** /servers/{id}/metrics | Get Metrics for a Server
*ServersApi* | [**serversIdPut**](docs/ServersApi.md#serversIdPut) | **PUT** /servers/{id} | Update a Server
*ServersApi* | [**serversPost**](docs/ServersApi.md#serversPost) | **POST** /servers | Create a Server
*SshKeysApi* | [**sshKeysGet**](docs/SshKeysApi.md#sshKeysGet) | **GET** /ssh_keys | Get all SSH keys
*SshKeysApi* | [**sshKeysIdDelete**](docs/SshKeysApi.md#sshKeysIdDelete) | **DELETE** /ssh_keys/{id} | Delete an SSH key
*SshKeysApi* | [**sshKeysIdGet**](docs/SshKeysApi.md#sshKeysIdGet) | **GET** /ssh_keys/{id} | Get a SSH key
*SshKeysApi* | [**sshKeysIdPut**](docs/SshKeysApi.md#sshKeysIdPut) | **PUT** /ssh_keys/{id} | Update an SSH key
*SshKeysApi* | [**sshKeysPost**](docs/SshKeysApi.md#sshKeysPost) | **POST** /ssh_keys | Create an SSH key
*VolumeActionsApi* | [**volumesIdActionsActionIdGet**](docs/VolumeActionsApi.md#volumesIdActionsActionIdGet) | **GET** /volumes/{id}/actions/{action_id} | Get an Action for a Volume
*VolumeActionsApi* | [**volumesIdActionsAttachPost**](docs/VolumeActionsApi.md#volumesIdActionsAttachPost) | **POST** /volumes/{id}/actions/attach | Attach Volume to a Server
*VolumeActionsApi* | [**volumesIdActionsChangeProtectionPost**](docs/VolumeActionsApi.md#volumesIdActionsChangeProtectionPost) | **POST** /volumes/{id}/actions/change_protection | Change Volume Protection
*VolumeActionsApi* | [**volumesIdActionsDetachPost**](docs/VolumeActionsApi.md#volumesIdActionsDetachPost) | **POST** /volumes/{id}/actions/detach | Detach Volume
*VolumeActionsApi* | [**volumesIdActionsGet**](docs/VolumeActionsApi.md#volumesIdActionsGet) | **GET** /volumes/{id}/actions | Get all Actions for a Volume
*VolumeActionsApi* | [**volumesIdActionsResizePost**](docs/VolumeActionsApi.md#volumesIdActionsResizePost) | **POST** /volumes/{id}/actions/resize | Resize Volume
*VolumesApi* | [**volumesGet**](docs/VolumesApi.md#volumesGet) | **GET** /volumes | Get all Volumes
*VolumesApi* | [**volumesIdDelete**](docs/VolumesApi.md#volumesIdDelete) | **DELETE** /volumes/{id} | Delete a Volume
*VolumesApi* | [**volumesIdGet**](docs/VolumesApi.md#volumesIdGet) | **GET** /volumes/{id} | Get a Volume
*VolumesApi* | [**volumesIdPut**](docs/VolumesApi.md#volumesIdPut) | **PUT** /volumes/{id} | Update a Volume
*VolumesApi* | [**volumesPost**](docs/VolumesApi.md#volumesPost) | **POST** /volumes | Create a Volume


## Documentation for Models

 - [Action](docs/Action.md)
 - [ActionError](docs/ActionError.md)
 - [ActionResourcesInner](docs/ActionResourcesInner.md)
 - [ActionResponse](docs/ActionResponse.md)
 - [ActionsResponse](docs/ActionsResponse.md)
 - [ActionsResponseMeta](docs/ActionsResponseMeta.md)
 - [ActionsResponseMetaPagination](docs/ActionsResponseMetaPagination.md)
 - [AddDeleteRouteRequest](docs/AddDeleteRouteRequest.md)
 - [AddSubnetRequest](docs/AddSubnetRequest.md)
 - [AddTargetRequest](docs/AddTargetRequest.md)
 - [AddTargetRequestLabelSelector](docs/AddTargetRequestLabelSelector.md)
 - [AddTargetRequestServer](docs/AddTargetRequestServer.md)
 - [AddToPlacementGroupRequest](docs/AddToPlacementGroupRequest.md)
 - [ApplyToResourcesRequest](docs/ApplyToResourcesRequest.md)
 - [AssignFloatingIPRequest](docs/AssignFloatingIPRequest.md)
 - [AssignPrimaryIPRequest](docs/AssignPrimaryIPRequest.md)
 - [AttachToNetworkRequest](docs/AttachToNetworkRequest.md)
 - [AttachVolumeRequest](docs/AttachVolumeRequest.md)
 - [Certificate](docs/Certificate.md)
 - [CertificateResponse](docs/CertificateResponse.md)
 - [CertificateStatus](docs/CertificateStatus.md)
 - [CertificateStatusError](docs/CertificateStatusError.md)
 - [CertificateUsedByInner](docs/CertificateUsedByInner.md)
 - [CertificatesResponse](docs/CertificatesResponse.md)
 - [ChangeDNSPTRRequest](docs/ChangeDNSPTRRequest.md)
 - [ChangeIPRangeRequest](docs/ChangeIPRangeRequest.md)
 - [ChangeLoadbalancerDnsPtrRequest](docs/ChangeLoadbalancerDnsPtrRequest.md)
 - [ChangeProtectionRequest](docs/ChangeProtectionRequest.md)
 - [ChangeProtectionRequest1](docs/ChangeProtectionRequest1.md)
 - [ChangeProtectionRequest2](docs/ChangeProtectionRequest2.md)
 - [ChangeTypeRequest](docs/ChangeTypeRequest.md)
 - [CreateCertificateRequest](docs/CreateCertificateRequest.md)
 - [CreateCertificateResponse](docs/CreateCertificateResponse.md)
 - [CreateFirewallRequest](docs/CreateFirewallRequest.md)
 - [CreateFirewallRequestApplyToInner](docs/CreateFirewallRequestApplyToInner.md)
 - [CreateFirewallRequestApplyToInnerLabelSelector](docs/CreateFirewallRequestApplyToInnerLabelSelector.md)
 - [CreateFirewallRequestApplyToInnerServer](docs/CreateFirewallRequestApplyToInnerServer.md)
 - [CreateFirewallResponse](docs/CreateFirewallResponse.md)
 - [CreateFloatingIPRequest](docs/CreateFloatingIPRequest.md)
 - [CreateImageRequest](docs/CreateImageRequest.md)
 - [CreateLoadBalancerRequest](docs/CreateLoadBalancerRequest.md)
 - [CreateLoadBalancerRequestLabels](docs/CreateLoadBalancerRequestLabels.md)
 - [CreateNetworkRequest](docs/CreateNetworkRequest.md)
 - [CreateNetworkRequestSubnetsInner](docs/CreateNetworkRequestSubnetsInner.md)
 - [CreatePlacementGroupRequest](docs/CreatePlacementGroupRequest.md)
 - [CreatePlacementGroupResponse](docs/CreatePlacementGroupResponse.md)
 - [CreatePrimaryIPRequest](docs/CreatePrimaryIPRequest.md)
 - [CreatePrimaryIPResponse](docs/CreatePrimaryIPResponse.md)
 - [CreateServerRequest](docs/CreateServerRequest.md)
 - [CreateServerRequestFirewallsInner](docs/CreateServerRequestFirewallsInner.md)
 - [CreateServerRequestPublicNet](docs/CreateServerRequestPublicNet.md)
 - [CreateServerResponse](docs/CreateServerResponse.md)
 - [CreateVolumeRequest](docs/CreateVolumeRequest.md)
 - [DatacentersGet200Response](docs/DatacentersGet200Response.md)
 - [DatacentersGet200ResponseDatacentersInner](docs/DatacentersGet200ResponseDatacentersInner.md)
 - [DatacentersGet200ResponseDatacentersInnerLocation](docs/DatacentersGet200ResponseDatacentersInnerLocation.md)
 - [DatacentersGet200ResponseDatacentersInnerServerTypes](docs/DatacentersGet200ResponseDatacentersInnerServerTypes.md)
 - [DatacentersIdGet200Response](docs/DatacentersIdGet200Response.md)
 - [DeleteSubnetRequest](docs/DeleteSubnetRequest.md)
 - [DetachFromNetworkRequest](docs/DetachFromNetworkRequest.md)
 - [Firewall](docs/Firewall.md)
 - [FirewallAppliedToInner](docs/FirewallAppliedToInner.md)
 - [FirewallAppliedToInnerAppliedToResourcesInner](docs/FirewallAppliedToInnerAppliedToResourcesInner.md)
 - [FirewallAppliedToInnerAppliedToResourcesInnerServer](docs/FirewallAppliedToInnerAppliedToResourcesInnerServer.md)
 - [FirewallAppliedToInnerLabelSelector](docs/FirewallAppliedToInnerLabelSelector.md)
 - [FirewallApplyToResources](docs/FirewallApplyToResources.md)
 - [FirewallApplyToResourcesLabelSelector](docs/FirewallApplyToResourcesLabelSelector.md)
 - [FirewallApplyToResourcesServer](docs/FirewallApplyToResourcesServer.md)
 - [FirewallRemoveFromResources](docs/FirewallRemoveFromResources.md)
 - [FirewallResponse](docs/FirewallResponse.md)
 - [FirewallsResponse](docs/FirewallsResponse.md)
 - [FloatingIpsGet200Response](docs/FloatingIpsGet200Response.md)
 - [FloatingIpsGet200ResponseFloatingIpsInner](docs/FloatingIpsGet200ResponseFloatingIpsInner.md)
 - [FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner](docs/FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner.md)
 - [FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation](docs/FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation.md)
 - [FloatingIpsGet200ResponseFloatingIpsInnerProtection](docs/FloatingIpsGet200ResponseFloatingIpsInnerProtection.md)
 - [FloatingIpsIdActionsGet200Response](docs/FloatingIpsIdActionsGet200Response.md)
 - [FloatingIpsIdGet200Response](docs/FloatingIpsIdGet200Response.md)
 - [FloatingIpsPost201Response](docs/FloatingIpsPost201Response.md)
 - [ImagesGet200Response](docs/ImagesGet200Response.md)
 - [ImagesGet200ResponseImagesInner](docs/ImagesGet200ResponseImagesInner.md)
 - [ImagesGet200ResponseImagesInnerCreatedFrom](docs/ImagesGet200ResponseImagesInnerCreatedFrom.md)
 - [ImagesIdActionsChangeProtectionPostRequest](docs/ImagesIdActionsChangeProtectionPostRequest.md)
 - [ImagesIdGet200Response](docs/ImagesIdGet200Response.md)
 - [IsosGet200Response](docs/IsosGet200Response.md)
 - [IsosGet200ResponseIsosInner](docs/IsosGet200ResponseIsosInner.md)
 - [IsosIdGet200Response](docs/IsosIdGet200Response.md)
 - [LoadBalancerAlgorithm](docs/LoadBalancerAlgorithm.md)
 - [LoadBalancerService](docs/LoadBalancerService.md)
 - [LoadBalancerServiceHTTP](docs/LoadBalancerServiceHTTP.md)
 - [LoadBalancerServiceHealthCheck](docs/LoadBalancerServiceHealthCheck.md)
 - [LoadBalancerServiceHealthCheckHttp](docs/LoadBalancerServiceHealthCheckHttp.md)
 - [LoadBalancerTarget](docs/LoadBalancerTarget.md)
 - [LoadBalancerTargetHealthStatusInner](docs/LoadBalancerTargetHealthStatusInner.md)
 - [LoadBalancerTargetIP](docs/LoadBalancerTargetIP.md)
 - [LoadBalancerTargetLabelSelector](docs/LoadBalancerTargetLabelSelector.md)
 - [LoadBalancerTargetServer](docs/LoadBalancerTargetServer.md)
 - [LoadBalancerTargetTarget](docs/LoadBalancerTargetTarget.md)
 - [LoadBalancerTypesGet200Response](docs/LoadBalancerTypesGet200Response.md)
 - [LoadBalancerTypesGet200ResponseLoadBalancerTypesInner](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInner.md)
 - [LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner.md)
 - [LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly.md)
 - [LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly.md)
 - [LoadBalancerTypesIdGet200Response](docs/LoadBalancerTypesIdGet200Response.md)
 - [LoadBalancersGet200Response](docs/LoadBalancersGet200Response.md)
 - [LoadBalancersGet200ResponseLoadBalancersInner](docs/LoadBalancersGet200ResponseLoadBalancersInner.md)
 - [LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm](docs/LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm.md)
 - [LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner](docs/LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner.md)
 - [LoadBalancersGet200ResponseLoadBalancersInnerPublicNet](docs/LoadBalancersGet200ResponseLoadBalancersInnerPublicNet.md)
 - [LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4](docs/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4.md)
 - [LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6](docs/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6.md)
 - [LoadBalancersIdActionsAttachToNetworkPostRequest](docs/LoadBalancersIdActionsAttachToNetworkPostRequest.md)
 - [LoadBalancersIdActionsChangeAlgorithmPostRequest](docs/LoadBalancersIdActionsChangeAlgorithmPostRequest.md)
 - [LoadBalancersIdActionsChangeProtectionPostRequest](docs/LoadBalancersIdActionsChangeProtectionPostRequest.md)
 - [LoadBalancersIdActionsDeleteServicePostRequest](docs/LoadBalancersIdActionsDeleteServicePostRequest.md)
 - [LoadBalancersIdActionsDetachFromNetworkPostRequest](docs/LoadBalancersIdActionsDetachFromNetworkPostRequest.md)
 - [LoadBalancersIdGet200Response](docs/LoadBalancersIdGet200Response.md)
 - [LoadBalancersIdMetricsGet200Response](docs/LoadBalancersIdMetricsGet200Response.md)
 - [LoadBalancersIdMetricsGet200ResponseMetrics](docs/LoadBalancersIdMetricsGet200ResponseMetrics.md)
 - [LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue](docs/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue.md)
 - [LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner](docs/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner.md)
 - [LoadBalancersIdPutRequest](docs/LoadBalancersIdPutRequest.md)
 - [LoadBalancersPost201Response](docs/LoadBalancersPost201Response.md)
 - [LocationsGet200Response](docs/LocationsGet200Response.md)
 - [LocationsIdGet200Response](docs/LocationsIdGet200Response.md)
 - [NetworksGet200Response](docs/NetworksGet200Response.md)
 - [NetworksGet200ResponseNetworksInner](docs/NetworksGet200ResponseNetworksInner.md)
 - [NetworksGet200ResponseNetworksInnerProtection](docs/NetworksGet200ResponseNetworksInnerProtection.md)
 - [NetworksGet200ResponseNetworksInnerRoutesInner](docs/NetworksGet200ResponseNetworksInnerRoutesInner.md)
 - [NetworksGet200ResponseNetworksInnerSubnetsInner](docs/NetworksGet200ResponseNetworksInnerSubnetsInner.md)
 - [NetworksPost201Response](docs/NetworksPost201Response.md)
 - [NullableAction](docs/NullableAction.md)
 - [PlacementGroup](docs/PlacementGroup.md)
 - [PlacementGroupNullable](docs/PlacementGroupNullable.md)
 - [PlacementGroupResponse](docs/PlacementGroupResponse.md)
 - [PlacementGroupsResponse](docs/PlacementGroupsResponse.md)
 - [PricingGet200Response](docs/PricingGet200Response.md)
 - [PricingGet200ResponsePricing](docs/PricingGet200ResponsePricing.md)
 - [PricingGet200ResponsePricingFloatingIp](docs/PricingGet200ResponsePricingFloatingIp.md)
 - [PricingGet200ResponsePricingFloatingIpPriceMonthly](docs/PricingGet200ResponsePricingFloatingIpPriceMonthly.md)
 - [PricingGet200ResponsePricingFloatingIpsInner](docs/PricingGet200ResponsePricingFloatingIpsInner.md)
 - [PricingGet200ResponsePricingFloatingIpsInnerPricesInner](docs/PricingGet200ResponsePricingFloatingIpsInnerPricesInner.md)
 - [PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly.md)
 - [PricingGet200ResponsePricingImage](docs/PricingGet200ResponsePricingImage.md)
 - [PricingGet200ResponsePricingLoadBalancerTypesInner](docs/PricingGet200ResponsePricingLoadBalancerTypesInner.md)
 - [PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner](docs/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner.md)
 - [PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly](docs/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly.md)
 - [PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly.md)
 - [PricingGet200ResponsePricingPrimaryIpsInner](docs/PricingGet200ResponsePricingPrimaryIpsInner.md)
 - [PricingGet200ResponsePricingPrimaryIpsInnerPricesInner](docs/PricingGet200ResponsePricingPrimaryIpsInnerPricesInner.md)
 - [PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly](docs/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly.md)
 - [PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly.md)
 - [PricingGet200ResponsePricingServerBackup](docs/PricingGet200ResponsePricingServerBackup.md)
 - [PricingGet200ResponsePricingServerTypesInner](docs/PricingGet200ResponsePricingServerTypesInner.md)
 - [PricingGet200ResponsePricingServerTypesInnerPricesInner](docs/PricingGet200ResponsePricingServerTypesInnerPricesInner.md)
 - [PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly](docs/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly.md)
 - [PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly.md)
 - [PricingGet200ResponsePricingTraffic](docs/PricingGet200ResponsePricingTraffic.md)
 - [PricingGet200ResponsePricingVolume](docs/PricingGet200ResponsePricingVolume.md)
 - [PrimaryIP](docs/PrimaryIP.md)
 - [PrimaryIPDatacenter](docs/PrimaryIPDatacenter.md)
 - [PrimaryIPDnsPtrInner](docs/PrimaryIPDnsPtrInner.md)
 - [PrimaryIPResponse](docs/PrimaryIPResponse.md)
 - [PrimaryIPsResponse](docs/PrimaryIPsResponse.md)
 - [RebuildServerRequest](docs/RebuildServerRequest.md)
 - [RemoveFromResourcesRequest](docs/RemoveFromResourcesRequest.md)
 - [RemoveTargetRequest](docs/RemoveTargetRequest.md)
 - [Rule](docs/Rule.md)
 - [ServerPublicNetFirewall](docs/ServerPublicNetFirewall.md)
 - [ServerTypesGet200Response](docs/ServerTypesGet200Response.md)
 - [ServerTypesGet200ResponseServerTypesInner](docs/ServerTypesGet200ResponseServerTypesInner.md)
 - [ServerTypesIdGet200Response](docs/ServerTypesIdGet200Response.md)
 - [ServersGet200Response](docs/ServersGet200Response.md)
 - [ServersGet200ResponseServersInner](docs/ServersGet200ResponseServersInner.md)
 - [ServersGet200ResponseServersInnerDatacenter](docs/ServersGet200ResponseServersInnerDatacenter.md)
 - [ServersGet200ResponseServersInnerImage](docs/ServersGet200ResponseServersInnerImage.md)
 - [ServersGet200ResponseServersInnerIso](docs/ServersGet200ResponseServersInnerIso.md)
 - [ServersGet200ResponseServersInnerPrivateNetInner](docs/ServersGet200ResponseServersInnerPrivateNetInner.md)
 - [ServersGet200ResponseServersInnerProtection](docs/ServersGet200ResponseServersInnerProtection.md)
 - [ServersGet200ResponseServersInnerPublicNet](docs/ServersGet200ResponseServersInnerPublicNet.md)
 - [ServersGet200ResponseServersInnerPublicNetIpv4](docs/ServersGet200ResponseServersInnerPublicNetIpv4.md)
 - [ServersGet200ResponseServersInnerPublicNetIpv6](docs/ServersGet200ResponseServersInnerPublicNetIpv6.md)
 - [ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner](docs/ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner.md)
 - [ServersGet200ResponseServersInnerServerType](docs/ServersGet200ResponseServersInnerServerType.md)
 - [ServersIdActionsAttachIsoPostRequest](docs/ServersIdActionsAttachIsoPostRequest.md)
 - [ServersIdActionsChangeAliasIpsPostRequest](docs/ServersIdActionsChangeAliasIpsPostRequest.md)
 - [ServersIdActionsChangeDnsPtrPostRequest](docs/ServersIdActionsChangeDnsPtrPostRequest.md)
 - [ServersIdActionsChangeProtectionPostRequest](docs/ServersIdActionsChangeProtectionPostRequest.md)
 - [ServersIdActionsChangeTypePostRequest](docs/ServersIdActionsChangeTypePostRequest.md)
 - [ServersIdActionsCreateImagePost201Response](docs/ServersIdActionsCreateImagePost201Response.md)
 - [ServersIdActionsEnableRescuePost201Response](docs/ServersIdActionsEnableRescuePost201Response.md)
 - [ServersIdActionsEnableRescuePostRequest](docs/ServersIdActionsEnableRescuePostRequest.md)
 - [ServersIdActionsRebuildPost201Response](docs/ServersIdActionsRebuildPost201Response.md)
 - [ServersIdActionsRequestConsolePost201Response](docs/ServersIdActionsRequestConsolePost201Response.md)
 - [ServersIdDelete200Response](docs/ServersIdDelete200Response.md)
 - [ServersIdGet200Response](docs/ServersIdGet200Response.md)
 - [SetRulesRequest](docs/SetRulesRequest.md)
 - [SshKeysGet200Response](docs/SshKeysGet200Response.md)
 - [SshKeysGet200ResponseSshKeysInner](docs/SshKeysGet200ResponseSshKeysInner.md)
 - [SshKeysIdPutRequest](docs/SshKeysIdPutRequest.md)
 - [SshKeysPost201Response](docs/SshKeysPost201Response.md)
 - [SshKeysPostRequest](docs/SshKeysPostRequest.md)
 - [UpdateCertificateRequest](docs/UpdateCertificateRequest.md)
 - [UpdateFirewallRequest](docs/UpdateFirewallRequest.md)
 - [UpdateFloatingIPRequest](docs/UpdateFloatingIPRequest.md)
 - [UpdateImageRequest](docs/UpdateImageRequest.md)
 - [UpdateNetworkRequest](docs/UpdateNetworkRequest.md)
 - [UpdateNetworkRequestLabels](docs/UpdateNetworkRequestLabels.md)
 - [UpdatePlacementGroupRequest](docs/UpdatePlacementGroupRequest.md)
 - [UpdatePrimaryIPRequest](docs/UpdatePrimaryIPRequest.md)
 - [UpdateServerRequest](docs/UpdateServerRequest.md)
 - [UpdateVolumeRequest](docs/UpdateVolumeRequest.md)
 - [VolumesGet200Response](docs/VolumesGet200Response.md)
 - [VolumesGet200ResponseVolumesInner](docs/VolumesGet200ResponseVolumesInner.md)
 - [VolumesGet200ResponseVolumesInnerLocation](docs/VolumesGet200ResponseVolumesInnerLocation.md)
 - [VolumesIdActionsChangeProtectionPostRequest](docs/VolumesIdActionsChangeProtectionPostRequest.md)
 - [VolumesIdActionsResizePostRequest](docs/VolumesIdActionsResizePostRequest.md)
 - [VolumesIdGet200Response](docs/VolumesIdGet200Response.md)
 - [VolumesPost201Response](docs/VolumesPost201Response.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



