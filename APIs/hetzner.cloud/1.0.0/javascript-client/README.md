# hetzner_cloud_api

HetznerCloudApi - JavaScript client for hetzner_cloud_api
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

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install hetzner_cloud_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your hetzner_cloud_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var HetznerCloudApi = require('hetzner_cloud_api');


var api = new HetznerCloudApi.ActionsApi()
var opts = {
  'id': 56, // {Number} Can be used multiple times, the response will contain only Actions with specified IDs
  'sort': "sort_example", // {String} Can be used multiple times.
  'status': "status_example" // {String} Can be used multiple times, the response will contain only Actions with specified statuses
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.actionsGet(opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.hetzner.cloud/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HetznerCloudApi.ActionsApi* | [**actionsGet**](docs/ActionsApi.md#actionsGet) | **GET** /actions | Get all Actions
*HetznerCloudApi.ActionsApi* | [**actionsIdGet**](docs/ActionsApi.md#actionsIdGet) | **GET** /actions/{id} | Get an Action
*HetznerCloudApi.CertificateActionsApi* | [**certificatesIdActionsActionIdGet**](docs/CertificateActionsApi.md#certificatesIdActionsActionIdGet) | **GET** /certificates/{id}/actions/{action_id} | Get an Action for a Certificate
*HetznerCloudApi.CertificateActionsApi* | [**certificatesIdActionsGet**](docs/CertificateActionsApi.md#certificatesIdActionsGet) | **GET** /certificates/{id}/actions | Get all Actions for a Certificate
*HetznerCloudApi.CertificateActionsApi* | [**certificatesIdActionsRetryPost**](docs/CertificateActionsApi.md#certificatesIdActionsRetryPost) | **POST** /certificates/{id}/actions/retry | Retry Issuance or Renewal
*HetznerCloudApi.CertificatesApi* | [**certificatesGet**](docs/CertificatesApi.md#certificatesGet) | **GET** /certificates | Get all Certificates
*HetznerCloudApi.CertificatesApi* | [**certificatesIdDelete**](docs/CertificatesApi.md#certificatesIdDelete) | **DELETE** /certificates/{id} | Delete a Certificate
*HetznerCloudApi.CertificatesApi* | [**certificatesIdGet**](docs/CertificatesApi.md#certificatesIdGet) | **GET** /certificates/{id} | Get a Certificate
*HetznerCloudApi.CertificatesApi* | [**certificatesIdPut**](docs/CertificatesApi.md#certificatesIdPut) | **PUT** /certificates/{id} | Update a Certificate
*HetznerCloudApi.CertificatesApi* | [**certificatesPost**](docs/CertificatesApi.md#certificatesPost) | **POST** /certificates | Create a Certificate
*HetznerCloudApi.DatacentersApi* | [**datacentersGet**](docs/DatacentersApi.md#datacentersGet) | **GET** /datacenters | Get all Datacenters
*HetznerCloudApi.DatacentersApi* | [**datacentersIdGet**](docs/DatacentersApi.md#datacentersIdGet) | **GET** /datacenters/{id} | Get a Datacenter
*HetznerCloudApi.FirewallActionsApi* | [**firewallsIdActionsActionIdGet**](docs/FirewallActionsApi.md#firewallsIdActionsActionIdGet) | **GET** /firewalls/{id}/actions/{action_id} | Get an Action for a Firewall
*HetznerCloudApi.FirewallActionsApi* | [**firewallsIdActionsApplyToResourcesPost**](docs/FirewallActionsApi.md#firewallsIdActionsApplyToResourcesPost) | **POST** /firewalls/{id}/actions/apply_to_resources | Apply to Resources
*HetznerCloudApi.FirewallActionsApi* | [**firewallsIdActionsGet**](docs/FirewallActionsApi.md#firewallsIdActionsGet) | **GET** /firewalls/{id}/actions | Get all Actions for a Firewall
*HetznerCloudApi.FirewallActionsApi* | [**firewallsIdActionsRemoveFromResourcesPost**](docs/FirewallActionsApi.md#firewallsIdActionsRemoveFromResourcesPost) | **POST** /firewalls/{id}/actions/remove_from_resources | Remove from Resources
*HetznerCloudApi.FirewallActionsApi* | [**firewallsIdActionsSetRulesPost**](docs/FirewallActionsApi.md#firewallsIdActionsSetRulesPost) | **POST** /firewalls/{id}/actions/set_rules | Set Rules
*HetznerCloudApi.FirewallsApi* | [**firewallsGet**](docs/FirewallsApi.md#firewallsGet) | **GET** /firewalls | Get all Firewalls
*HetznerCloudApi.FirewallsApi* | [**firewallsIdDelete**](docs/FirewallsApi.md#firewallsIdDelete) | **DELETE** /firewalls/{id} | Delete a Firewall
*HetznerCloudApi.FirewallsApi* | [**firewallsIdGet**](docs/FirewallsApi.md#firewallsIdGet) | **GET** /firewalls/{id} | Get a Firewall
*HetznerCloudApi.FirewallsApi* | [**firewallsIdPut**](docs/FirewallsApi.md#firewallsIdPut) | **PUT** /firewalls/{id} | Update a Firewall
*HetznerCloudApi.FirewallsApi* | [**firewallsPost**](docs/FirewallsApi.md#firewallsPost) | **POST** /firewalls | Create a Firewall
*HetznerCloudApi.FloatingIPActionsApi* | [**floatingIpsIdActionsActionIdGet**](docs/FloatingIPActionsApi.md#floatingIpsIdActionsActionIdGet) | **GET** /floating_ips/{id}/actions/{action_id} | Get an Action for a Floating IP
*HetznerCloudApi.FloatingIPActionsApi* | [**floatingIpsIdActionsAssignPost**](docs/FloatingIPActionsApi.md#floatingIpsIdActionsAssignPost) | **POST** /floating_ips/{id}/actions/assign | Assign a Floating IP to a Server
*HetznerCloudApi.FloatingIPActionsApi* | [**floatingIpsIdActionsChangeDnsPtrPost**](docs/FloatingIPActionsApi.md#floatingIpsIdActionsChangeDnsPtrPost) | **POST** /floating_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Floating IP
*HetznerCloudApi.FloatingIPActionsApi* | [**floatingIpsIdActionsChangeProtectionPost**](docs/FloatingIPActionsApi.md#floatingIpsIdActionsChangeProtectionPost) | **POST** /floating_ips/{id}/actions/change_protection | Change Floating IP Protection
*HetznerCloudApi.FloatingIPActionsApi* | [**floatingIpsIdActionsGet**](docs/FloatingIPActionsApi.md#floatingIpsIdActionsGet) | **GET** /floating_ips/{id}/actions | Get all Actions for a Floating IP
*HetznerCloudApi.FloatingIPActionsApi* | [**floatingIpsIdActionsUnassignPost**](docs/FloatingIPActionsApi.md#floatingIpsIdActionsUnassignPost) | **POST** /floating_ips/{id}/actions/unassign | Unassign a Floating IP
*HetznerCloudApi.FloatingIPsApi* | [**floatingIpsGet**](docs/FloatingIPsApi.md#floatingIpsGet) | **GET** /floating_ips | Get all Floating IPs
*HetznerCloudApi.FloatingIPsApi* | [**floatingIpsIdDelete**](docs/FloatingIPsApi.md#floatingIpsIdDelete) | **DELETE** /floating_ips/{id} | Delete a Floating IP
*HetznerCloudApi.FloatingIPsApi* | [**floatingIpsIdGet**](docs/FloatingIPsApi.md#floatingIpsIdGet) | **GET** /floating_ips/{id} | Get a Floating IP
*HetznerCloudApi.FloatingIPsApi* | [**floatingIpsIdPut**](docs/FloatingIPsApi.md#floatingIpsIdPut) | **PUT** /floating_ips/{id} | Update a Floating IP
*HetznerCloudApi.FloatingIPsApi* | [**floatingIpsPost**](docs/FloatingIPsApi.md#floatingIpsPost) | **POST** /floating_ips | Create a Floating IP
*HetznerCloudApi.ISOsApi* | [**isosGet**](docs/ISOsApi.md#isosGet) | **GET** /isos | Get all ISOs
*HetznerCloudApi.ISOsApi* | [**isosIdGet**](docs/ISOsApi.md#isosIdGet) | **GET** /isos/{id} | Get an ISO
*HetznerCloudApi.ImageActionsApi* | [**imagesIdActionsActionIdGet**](docs/ImageActionsApi.md#imagesIdActionsActionIdGet) | **GET** /images/{id}/actions/{action_id} | Get an Action for an Image
*HetznerCloudApi.ImageActionsApi* | [**imagesIdActionsChangeProtectionPost**](docs/ImageActionsApi.md#imagesIdActionsChangeProtectionPost) | **POST** /images/{id}/actions/change_protection | Change Image Protection
*HetznerCloudApi.ImageActionsApi* | [**imagesIdActionsGet**](docs/ImageActionsApi.md#imagesIdActionsGet) | **GET** /images/{id}/actions | Get all Actions for an Image
*HetznerCloudApi.ImagesApi* | [**imagesGet**](docs/ImagesApi.md#imagesGet) | **GET** /images | Get all Images
*HetznerCloudApi.ImagesApi* | [**imagesIdDelete**](docs/ImagesApi.md#imagesIdDelete) | **DELETE** /images/{id} | Delete an Image
*HetznerCloudApi.ImagesApi* | [**imagesIdGet**](docs/ImagesApi.md#imagesIdGet) | **GET** /images/{id} | Get an Image
*HetznerCloudApi.ImagesApi* | [**imagesIdPut**](docs/ImagesApi.md#imagesIdPut) | **PUT** /images/{id} | Update an Image
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsActionIdGet**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsActionIdGet) | **GET** /load_balancers/{id}/actions/{action_id} | Get an Action for a Load Balancer
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsAddServicePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsAddServicePost) | **POST** /load_balancers/{id}/actions/add_service | Add Service
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsAddTargetPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsAddTargetPost) | **POST** /load_balancers/{id}/actions/add_target | Add Target
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsAttachToNetworkPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsAttachToNetworkPost) | **POST** /load_balancers/{id}/actions/attach_to_network | Attach a Load Balancer to a Network
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeAlgorithmPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeAlgorithmPost) | **POST** /load_balancers/{id}/actions/change_algorithm | Change Algorithm
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeDnsPtrPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeDnsPtrPost) | **POST** /load_balancers/{id}/actions/change_dns_ptr | Change reverse DNS entry for this Load Balancer
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeProtectionPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeProtectionPost) | **POST** /load_balancers/{id}/actions/change_protection | Change Load Balancer Protection
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsChangeTypePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsChangeTypePost) | **POST** /load_balancers/{id}/actions/change_type | Change the Type of a Load Balancer
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsDeleteServicePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsDeleteServicePost) | **POST** /load_balancers/{id}/actions/delete_service | Delete Service
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsDetachFromNetworkPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsDetachFromNetworkPost) | **POST** /load_balancers/{id}/actions/detach_from_network | Detach a Load Balancer from a Network
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsDisablePublicInterfacePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsDisablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/disable_public_interface | Disable the public interface of a Load Balancer
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsEnablePublicInterfacePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsEnablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/enable_public_interface | Enable the public interface of a Load Balancer
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsGet**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsGet) | **GET** /load_balancers/{id}/actions | Get all Actions for a Load Balancer
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsRemoveTargetPost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsRemoveTargetPost) | **POST** /load_balancers/{id}/actions/remove_target | Remove Target
*HetznerCloudApi.LoadBalancerActionsApi* | [**loadBalancersIdActionsUpdateServicePost**](docs/LoadBalancerActionsApi.md#loadBalancersIdActionsUpdateServicePost) | **POST** /load_balancers/{id}/actions/update_service | Update Service
*HetznerCloudApi.LoadBalancerTypesApi* | [**loadBalancerTypesGet**](docs/LoadBalancerTypesApi.md#loadBalancerTypesGet) | **GET** /load_balancer_types | Get all Load Balancer Types
*HetznerCloudApi.LoadBalancerTypesApi* | [**loadBalancerTypesIdGet**](docs/LoadBalancerTypesApi.md#loadBalancerTypesIdGet) | **GET** /load_balancer_types/{id} | Get a Load Balancer Type
*HetznerCloudApi.LoadBalancersApi* | [**loadBalancersGet**](docs/LoadBalancersApi.md#loadBalancersGet) | **GET** /load_balancers | Get all Load Balancers
*HetznerCloudApi.LoadBalancersApi* | [**loadBalancersIdDelete**](docs/LoadBalancersApi.md#loadBalancersIdDelete) | **DELETE** /load_balancers/{id} | Delete a Load Balancer
*HetznerCloudApi.LoadBalancersApi* | [**loadBalancersIdGet**](docs/LoadBalancersApi.md#loadBalancersIdGet) | **GET** /load_balancers/{id} | Get a Load Balancer
*HetznerCloudApi.LoadBalancersApi* | [**loadBalancersIdMetricsGet**](docs/LoadBalancersApi.md#loadBalancersIdMetricsGet) | **GET** /load_balancers/{id}/metrics | Get Metrics for a LoadBalancer
*HetznerCloudApi.LoadBalancersApi* | [**loadBalancersIdPut**](docs/LoadBalancersApi.md#loadBalancersIdPut) | **PUT** /load_balancers/{id} | Update a Load Balancer
*HetznerCloudApi.LoadBalancersApi* | [**loadBalancersPost**](docs/LoadBalancersApi.md#loadBalancersPost) | **POST** /load_balancers | Create a Load Balancer
*HetznerCloudApi.LocationsApi* | [**locationsGet**](docs/LocationsApi.md#locationsGet) | **GET** /locations | Get all Locations
*HetznerCloudApi.LocationsApi* | [**locationsIdGet**](docs/LocationsApi.md#locationsIdGet) | **GET** /locations/{id} | Get a Location
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsActionIdGet**](docs/NetworkActionsApi.md#networksIdActionsActionIdGet) | **GET** /networks/{id}/actions/{action_id} | Get an Action for a Network
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsAddRoutePost**](docs/NetworkActionsApi.md#networksIdActionsAddRoutePost) | **POST** /networks/{id}/actions/add_route | Add a route to a Network
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsAddSubnetPost**](docs/NetworkActionsApi.md#networksIdActionsAddSubnetPost) | **POST** /networks/{id}/actions/add_subnet | Add a subnet to a Network
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsChangeIpRangePost**](docs/NetworkActionsApi.md#networksIdActionsChangeIpRangePost) | **POST** /networks/{id}/actions/change_ip_range | Change IP range of a Network
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsChangeProtectionPost**](docs/NetworkActionsApi.md#networksIdActionsChangeProtectionPost) | **POST** /networks/{id}/actions/change_protection | Change Network Protection
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsDeleteRoutePost**](docs/NetworkActionsApi.md#networksIdActionsDeleteRoutePost) | **POST** /networks/{id}/actions/delete_route | Delete a route from a Network
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsDeleteSubnetPost**](docs/NetworkActionsApi.md#networksIdActionsDeleteSubnetPost) | **POST** /networks/{id}/actions/delete_subnet | Delete a subnet from a Network
*HetznerCloudApi.NetworkActionsApi* | [**networksIdActionsGet**](docs/NetworkActionsApi.md#networksIdActionsGet) | **GET** /networks/{id}/actions | Get all Actions for a Network
*HetznerCloudApi.NetworksApi* | [**networksGet**](docs/NetworksApi.md#networksGet) | **GET** /networks | Get all Networks
*HetznerCloudApi.NetworksApi* | [**networksIdDelete**](docs/NetworksApi.md#networksIdDelete) | **DELETE** /networks/{id} | Delete a Network
*HetznerCloudApi.NetworksApi* | [**networksIdGet**](docs/NetworksApi.md#networksIdGet) | **GET** /networks/{id} | Get a Network
*HetznerCloudApi.NetworksApi* | [**networksIdPut**](docs/NetworksApi.md#networksIdPut) | **PUT** /networks/{id} | Update a Network
*HetznerCloudApi.NetworksApi* | [**networksPost**](docs/NetworksApi.md#networksPost) | **POST** /networks | Create a Network
*HetznerCloudApi.PlacementGroupsApi* | [**placementGroupsGet**](docs/PlacementGroupsApi.md#placementGroupsGet) | **GET** /placement_groups | Get all PlacementGroups
*HetznerCloudApi.PlacementGroupsApi* | [**placementGroupsIdDelete**](docs/PlacementGroupsApi.md#placementGroupsIdDelete) | **DELETE** /placement_groups/{id} | Delete a PlacementGroup
*HetznerCloudApi.PlacementGroupsApi* | [**placementGroupsIdGet**](docs/PlacementGroupsApi.md#placementGroupsIdGet) | **GET** /placement_groups/{id} | Get a PlacementGroup
*HetznerCloudApi.PlacementGroupsApi* | [**placementGroupsIdPut**](docs/PlacementGroupsApi.md#placementGroupsIdPut) | **PUT** /placement_groups/{id} | Update a PlacementGroup
*HetznerCloudApi.PlacementGroupsApi* | [**placementGroupsPost**](docs/PlacementGroupsApi.md#placementGroupsPost) | **POST** /placement_groups | Create a PlacementGroup
*HetznerCloudApi.PricingApi* | [**pricingGet**](docs/PricingApi.md#pricingGet) | **GET** /pricing | Get all prices
*HetznerCloudApi.PrimaryIPActionsApi* | [**primaryIpsIdActionsAssignPost**](docs/PrimaryIPActionsApi.md#primaryIpsIdActionsAssignPost) | **POST** /primary_ips/{id}/actions/assign | Assign a Primary IP to a resource
*HetznerCloudApi.PrimaryIPActionsApi* | [**primaryIpsIdActionsChangeDnsPtrPost**](docs/PrimaryIPActionsApi.md#primaryIpsIdActionsChangeDnsPtrPost) | **POST** /primary_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Primary IP
*HetznerCloudApi.PrimaryIPActionsApi* | [**primaryIpsIdActionsChangeProtectionPost**](docs/PrimaryIPActionsApi.md#primaryIpsIdActionsChangeProtectionPost) | **POST** /primary_ips/{id}/actions/change_protection | Change Primary IP Protection
*HetznerCloudApi.PrimaryIPActionsApi* | [**primaryIpsIdActionsUnassignPost**](docs/PrimaryIPActionsApi.md#primaryIpsIdActionsUnassignPost) | **POST** /primary_ips/{id}/actions/unassign | Unassign a Primary IP from a resource
*HetznerCloudApi.PrimaryIPsApi* | [**primaryIpsGet**](docs/PrimaryIPsApi.md#primaryIpsGet) | **GET** /primary_ips | Get all Primary IPs
*HetznerCloudApi.PrimaryIPsApi* | [**primaryIpsIdDelete**](docs/PrimaryIPsApi.md#primaryIpsIdDelete) | **DELETE** /primary_ips/{id} | Delete a Primary IP
*HetznerCloudApi.PrimaryIPsApi* | [**primaryIpsIdGet**](docs/PrimaryIPsApi.md#primaryIpsIdGet) | **GET** /primary_ips/{id} | Get a Primary IP
*HetznerCloudApi.PrimaryIPsApi* | [**primaryIpsIdPut**](docs/PrimaryIPsApi.md#primaryIpsIdPut) | **PUT** /primary_ips/{id} | Update a Primary IP
*HetznerCloudApi.PrimaryIPsApi* | [**primaryIpsPost**](docs/PrimaryIPsApi.md#primaryIpsPost) | **POST** /primary_ips | Create a Primary IP
*HetznerCloudApi.SSHKeysApi* | [**sshKeysGet**](docs/SSHKeysApi.md#sshKeysGet) | **GET** /ssh_keys | Get all SSH keys
*HetznerCloudApi.SSHKeysApi* | [**sshKeysIdDelete**](docs/SSHKeysApi.md#sshKeysIdDelete) | **DELETE** /ssh_keys/{id} | Delete an SSH key
*HetznerCloudApi.SSHKeysApi* | [**sshKeysIdGet**](docs/SSHKeysApi.md#sshKeysIdGet) | **GET** /ssh_keys/{id} | Get a SSH key
*HetznerCloudApi.SSHKeysApi* | [**sshKeysIdPut**](docs/SSHKeysApi.md#sshKeysIdPut) | **PUT** /ssh_keys/{id} | Update an SSH key
*HetznerCloudApi.SSHKeysApi* | [**sshKeysPost**](docs/SSHKeysApi.md#sshKeysPost) | **POST** /ssh_keys | Create an SSH key
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsActionIdGet**](docs/ServerActionsApi.md#serversIdActionsActionIdGet) | **GET** /servers/{id}/actions/{action_id} | Get an Action for a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsAddToPlacementGroupPost**](docs/ServerActionsApi.md#serversIdActionsAddToPlacementGroupPost) | **POST** /servers/{id}/actions/add_to_placement_group | Add a Server to a Placement Group
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsAttachIsoPost**](docs/ServerActionsApi.md#serversIdActionsAttachIsoPost) | **POST** /servers/{id}/actions/attach_iso | Attach an ISO to a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsAttachToNetworkPost**](docs/ServerActionsApi.md#serversIdActionsAttachToNetworkPost) | **POST** /servers/{id}/actions/attach_to_network | Attach a Server to a Network
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsChangeAliasIpsPost**](docs/ServerActionsApi.md#serversIdActionsChangeAliasIpsPost) | **POST** /servers/{id}/actions/change_alias_ips | Change alias IPs of a Network
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsChangeDnsPtrPost**](docs/ServerActionsApi.md#serversIdActionsChangeDnsPtrPost) | **POST** /servers/{id}/actions/change_dns_ptr | Change reverse DNS entry for this Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsChangeProtectionPost**](docs/ServerActionsApi.md#serversIdActionsChangeProtectionPost) | **POST** /servers/{id}/actions/change_protection | Change Server Protection
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsChangeTypePost**](docs/ServerActionsApi.md#serversIdActionsChangeTypePost) | **POST** /servers/{id}/actions/change_type | Change the Type of a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsCreateImagePost**](docs/ServerActionsApi.md#serversIdActionsCreateImagePost) | **POST** /servers/{id}/actions/create_image | Create Image from a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsDetachFromNetworkPost**](docs/ServerActionsApi.md#serversIdActionsDetachFromNetworkPost) | **POST** /servers/{id}/actions/detach_from_network | Detach a Server from a Network
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsDetachIsoPost**](docs/ServerActionsApi.md#serversIdActionsDetachIsoPost) | **POST** /servers/{id}/actions/detach_iso | Detach an ISO from a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsDisableBackupPost**](docs/ServerActionsApi.md#serversIdActionsDisableBackupPost) | **POST** /servers/{id}/actions/disable_backup | Disable Backups for a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsDisableRescuePost**](docs/ServerActionsApi.md#serversIdActionsDisableRescuePost) | **POST** /servers/{id}/actions/disable_rescue | Disable Rescue Mode for a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsEnableBackupPost**](docs/ServerActionsApi.md#serversIdActionsEnableBackupPost) | **POST** /servers/{id}/actions/enable_backup | Enable and Configure Backups for a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsEnableRescuePost**](docs/ServerActionsApi.md#serversIdActionsEnableRescuePost) | **POST** /servers/{id}/actions/enable_rescue | Enable Rescue Mode for a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsGet**](docs/ServerActionsApi.md#serversIdActionsGet) | **GET** /servers/{id}/actions | Get all Actions for a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsPoweroffPost**](docs/ServerActionsApi.md#serversIdActionsPoweroffPost) | **POST** /servers/{id}/actions/poweroff | Power off a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsPoweronPost**](docs/ServerActionsApi.md#serversIdActionsPoweronPost) | **POST** /servers/{id}/actions/poweron | Power on a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsRebootPost**](docs/ServerActionsApi.md#serversIdActionsRebootPost) | **POST** /servers/{id}/actions/reboot | Soft-reboot a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsRebuildPost**](docs/ServerActionsApi.md#serversIdActionsRebuildPost) | **POST** /servers/{id}/actions/rebuild | Rebuild a Server from an Image
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsRemoveFromPlacementGroupPost**](docs/ServerActionsApi.md#serversIdActionsRemoveFromPlacementGroupPost) | **POST** /servers/{id}/actions/remove_from_placement_group | Remove from Placement Group
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsRequestConsolePost**](docs/ServerActionsApi.md#serversIdActionsRequestConsolePost) | **POST** /servers/{id}/actions/request_console | Request Console for a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsResetPasswordPost**](docs/ServerActionsApi.md#serversIdActionsResetPasswordPost) | **POST** /servers/{id}/actions/reset_password | Reset root Password of a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsResetPost**](docs/ServerActionsApi.md#serversIdActionsResetPost) | **POST** /servers/{id}/actions/reset | Reset a Server
*HetznerCloudApi.ServerActionsApi* | [**serversIdActionsShutdownPost**](docs/ServerActionsApi.md#serversIdActionsShutdownPost) | **POST** /servers/{id}/actions/shutdown | Shutdown a Server
*HetznerCloudApi.ServerTypesApi* | [**serverTypesGet**](docs/ServerTypesApi.md#serverTypesGet) | **GET** /server_types | Get all Server Types
*HetznerCloudApi.ServerTypesApi* | [**serverTypesIdGet**](docs/ServerTypesApi.md#serverTypesIdGet) | **GET** /server_types/{id} | Get a Server Type
*HetznerCloudApi.ServersApi* | [**serversGet**](docs/ServersApi.md#serversGet) | **GET** /servers | Get all Servers
*HetznerCloudApi.ServersApi* | [**serversIdDelete**](docs/ServersApi.md#serversIdDelete) | **DELETE** /servers/{id} | Delete a Server
*HetznerCloudApi.ServersApi* | [**serversIdGet**](docs/ServersApi.md#serversIdGet) | **GET** /servers/{id} | Get a Server
*HetznerCloudApi.ServersApi* | [**serversIdMetricsGet**](docs/ServersApi.md#serversIdMetricsGet) | **GET** /servers/{id}/metrics | Get Metrics for a Server
*HetznerCloudApi.ServersApi* | [**serversIdPut**](docs/ServersApi.md#serversIdPut) | **PUT** /servers/{id} | Update a Server
*HetznerCloudApi.ServersApi* | [**serversPost**](docs/ServersApi.md#serversPost) | **POST** /servers | Create a Server
*HetznerCloudApi.VolumeActionsApi* | [**volumesIdActionsActionIdGet**](docs/VolumeActionsApi.md#volumesIdActionsActionIdGet) | **GET** /volumes/{id}/actions/{action_id} | Get an Action for a Volume
*HetznerCloudApi.VolumeActionsApi* | [**volumesIdActionsAttachPost**](docs/VolumeActionsApi.md#volumesIdActionsAttachPost) | **POST** /volumes/{id}/actions/attach | Attach Volume to a Server
*HetznerCloudApi.VolumeActionsApi* | [**volumesIdActionsChangeProtectionPost**](docs/VolumeActionsApi.md#volumesIdActionsChangeProtectionPost) | **POST** /volumes/{id}/actions/change_protection | Change Volume Protection
*HetznerCloudApi.VolumeActionsApi* | [**volumesIdActionsDetachPost**](docs/VolumeActionsApi.md#volumesIdActionsDetachPost) | **POST** /volumes/{id}/actions/detach | Detach Volume
*HetznerCloudApi.VolumeActionsApi* | [**volumesIdActionsGet**](docs/VolumeActionsApi.md#volumesIdActionsGet) | **GET** /volumes/{id}/actions | Get all Actions for a Volume
*HetznerCloudApi.VolumeActionsApi* | [**volumesIdActionsResizePost**](docs/VolumeActionsApi.md#volumesIdActionsResizePost) | **POST** /volumes/{id}/actions/resize | Resize Volume
*HetznerCloudApi.VolumesApi* | [**volumesGet**](docs/VolumesApi.md#volumesGet) | **GET** /volumes | Get all Volumes
*HetznerCloudApi.VolumesApi* | [**volumesIdDelete**](docs/VolumesApi.md#volumesIdDelete) | **DELETE** /volumes/{id} | Delete a Volume
*HetznerCloudApi.VolumesApi* | [**volumesIdGet**](docs/VolumesApi.md#volumesIdGet) | **GET** /volumes/{id} | Get a Volume
*HetznerCloudApi.VolumesApi* | [**volumesIdPut**](docs/VolumesApi.md#volumesIdPut) | **PUT** /volumes/{id} | Update a Volume
*HetznerCloudApi.VolumesApi* | [**volumesPost**](docs/VolumesApi.md#volumesPost) | **POST** /volumes | Create a Volume


## Documentation for Models

 - [HetznerCloudApi.Action](docs/Action.md)
 - [HetznerCloudApi.ActionError](docs/ActionError.md)
 - [HetznerCloudApi.ActionResourcesInner](docs/ActionResourcesInner.md)
 - [HetznerCloudApi.ActionResponse](docs/ActionResponse.md)
 - [HetznerCloudApi.ActionsResponse](docs/ActionsResponse.md)
 - [HetznerCloudApi.ActionsResponseMeta](docs/ActionsResponseMeta.md)
 - [HetznerCloudApi.ActionsResponseMetaPagination](docs/ActionsResponseMetaPagination.md)
 - [HetznerCloudApi.AddDeleteRouteRequest](docs/AddDeleteRouteRequest.md)
 - [HetznerCloudApi.AddSubnetRequest](docs/AddSubnetRequest.md)
 - [HetznerCloudApi.AddTargetRequest](docs/AddTargetRequest.md)
 - [HetznerCloudApi.AddTargetRequestLabelSelector](docs/AddTargetRequestLabelSelector.md)
 - [HetznerCloudApi.AddTargetRequestServer](docs/AddTargetRequestServer.md)
 - [HetznerCloudApi.AddToPlacementGroupRequest](docs/AddToPlacementGroupRequest.md)
 - [HetznerCloudApi.ApplyToResourcesRequest](docs/ApplyToResourcesRequest.md)
 - [HetznerCloudApi.AssignFloatingIPRequest](docs/AssignFloatingIPRequest.md)
 - [HetznerCloudApi.AssignPrimaryIPRequest](docs/AssignPrimaryIPRequest.md)
 - [HetznerCloudApi.AttachToNetworkRequest](docs/AttachToNetworkRequest.md)
 - [HetznerCloudApi.AttachVolumeRequest](docs/AttachVolumeRequest.md)
 - [HetznerCloudApi.Certificate](docs/Certificate.md)
 - [HetznerCloudApi.CertificateResponse](docs/CertificateResponse.md)
 - [HetznerCloudApi.CertificateStatus](docs/CertificateStatus.md)
 - [HetznerCloudApi.CertificateStatusError](docs/CertificateStatusError.md)
 - [HetznerCloudApi.CertificateUsedByInner](docs/CertificateUsedByInner.md)
 - [HetznerCloudApi.CertificatesResponse](docs/CertificatesResponse.md)
 - [HetznerCloudApi.ChangeDNSPTRRequest](docs/ChangeDNSPTRRequest.md)
 - [HetznerCloudApi.ChangeIPRangeRequest](docs/ChangeIPRangeRequest.md)
 - [HetznerCloudApi.ChangeLoadbalancerDnsPtrRequest](docs/ChangeLoadbalancerDnsPtrRequest.md)
 - [HetznerCloudApi.ChangeProtectionRequest](docs/ChangeProtectionRequest.md)
 - [HetznerCloudApi.ChangeProtectionRequest1](docs/ChangeProtectionRequest1.md)
 - [HetznerCloudApi.ChangeProtectionRequest2](docs/ChangeProtectionRequest2.md)
 - [HetznerCloudApi.ChangeTypeRequest](docs/ChangeTypeRequest.md)
 - [HetznerCloudApi.CreateCertificateRequest](docs/CreateCertificateRequest.md)
 - [HetznerCloudApi.CreateCertificateResponse](docs/CreateCertificateResponse.md)
 - [HetznerCloudApi.CreateFirewallRequest](docs/CreateFirewallRequest.md)
 - [HetznerCloudApi.CreateFirewallRequestApplyToInner](docs/CreateFirewallRequestApplyToInner.md)
 - [HetznerCloudApi.CreateFirewallRequestApplyToInnerLabelSelector](docs/CreateFirewallRequestApplyToInnerLabelSelector.md)
 - [HetznerCloudApi.CreateFirewallRequestApplyToInnerServer](docs/CreateFirewallRequestApplyToInnerServer.md)
 - [HetznerCloudApi.CreateFirewallResponse](docs/CreateFirewallResponse.md)
 - [HetznerCloudApi.CreateFloatingIPRequest](docs/CreateFloatingIPRequest.md)
 - [HetznerCloudApi.CreateImageRequest](docs/CreateImageRequest.md)
 - [HetznerCloudApi.CreateLoadBalancerRequest](docs/CreateLoadBalancerRequest.md)
 - [HetznerCloudApi.CreateLoadBalancerRequestLabels](docs/CreateLoadBalancerRequestLabels.md)
 - [HetznerCloudApi.CreateNetworkRequest](docs/CreateNetworkRequest.md)
 - [HetznerCloudApi.CreateNetworkRequestSubnetsInner](docs/CreateNetworkRequestSubnetsInner.md)
 - [HetznerCloudApi.CreatePlacementGroupRequest](docs/CreatePlacementGroupRequest.md)
 - [HetznerCloudApi.CreatePlacementGroupResponse](docs/CreatePlacementGroupResponse.md)
 - [HetznerCloudApi.CreatePrimaryIPRequest](docs/CreatePrimaryIPRequest.md)
 - [HetznerCloudApi.CreatePrimaryIPResponse](docs/CreatePrimaryIPResponse.md)
 - [HetznerCloudApi.CreateServerRequest](docs/CreateServerRequest.md)
 - [HetznerCloudApi.CreateServerRequestFirewallsInner](docs/CreateServerRequestFirewallsInner.md)
 - [HetznerCloudApi.CreateServerRequestPublicNet](docs/CreateServerRequestPublicNet.md)
 - [HetznerCloudApi.CreateServerResponse](docs/CreateServerResponse.md)
 - [HetznerCloudApi.CreateVolumeRequest](docs/CreateVolumeRequest.md)
 - [HetznerCloudApi.DatacentersGet200Response](docs/DatacentersGet200Response.md)
 - [HetznerCloudApi.DatacentersGet200ResponseDatacentersInner](docs/DatacentersGet200ResponseDatacentersInner.md)
 - [HetznerCloudApi.DatacentersGet200ResponseDatacentersInnerLocation](docs/DatacentersGet200ResponseDatacentersInnerLocation.md)
 - [HetznerCloudApi.DatacentersGet200ResponseDatacentersInnerServerTypes](docs/DatacentersGet200ResponseDatacentersInnerServerTypes.md)
 - [HetznerCloudApi.DatacentersIdGet200Response](docs/DatacentersIdGet200Response.md)
 - [HetznerCloudApi.DeleteSubnetRequest](docs/DeleteSubnetRequest.md)
 - [HetznerCloudApi.DetachFromNetworkRequest](docs/DetachFromNetworkRequest.md)
 - [HetznerCloudApi.Firewall](docs/Firewall.md)
 - [HetznerCloudApi.FirewallAppliedToInner](docs/FirewallAppliedToInner.md)
 - [HetznerCloudApi.FirewallAppliedToInnerAppliedToResourcesInner](docs/FirewallAppliedToInnerAppliedToResourcesInner.md)
 - [HetznerCloudApi.FirewallAppliedToInnerAppliedToResourcesInnerServer](docs/FirewallAppliedToInnerAppliedToResourcesInnerServer.md)
 - [HetznerCloudApi.FirewallAppliedToInnerLabelSelector](docs/FirewallAppliedToInnerLabelSelector.md)
 - [HetznerCloudApi.FirewallApplyToResources](docs/FirewallApplyToResources.md)
 - [HetznerCloudApi.FirewallApplyToResourcesLabelSelector](docs/FirewallApplyToResourcesLabelSelector.md)
 - [HetznerCloudApi.FirewallApplyToResourcesServer](docs/FirewallApplyToResourcesServer.md)
 - [HetznerCloudApi.FirewallRemoveFromResources](docs/FirewallRemoveFromResources.md)
 - [HetznerCloudApi.FirewallResponse](docs/FirewallResponse.md)
 - [HetznerCloudApi.FirewallsResponse](docs/FirewallsResponse.md)
 - [HetznerCloudApi.FloatingIpsGet200Response](docs/FloatingIpsGet200Response.md)
 - [HetznerCloudApi.FloatingIpsGet200ResponseFloatingIpsInner](docs/FloatingIpsGet200ResponseFloatingIpsInner.md)
 - [HetznerCloudApi.FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner](docs/FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner.md)
 - [HetznerCloudApi.FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation](docs/FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation.md)
 - [HetznerCloudApi.FloatingIpsGet200ResponseFloatingIpsInnerProtection](docs/FloatingIpsGet200ResponseFloatingIpsInnerProtection.md)
 - [HetznerCloudApi.FloatingIpsIdActionsGet200Response](docs/FloatingIpsIdActionsGet200Response.md)
 - [HetznerCloudApi.FloatingIpsIdGet200Response](docs/FloatingIpsIdGet200Response.md)
 - [HetznerCloudApi.FloatingIpsPost201Response](docs/FloatingIpsPost201Response.md)
 - [HetznerCloudApi.ImagesGet200Response](docs/ImagesGet200Response.md)
 - [HetznerCloudApi.ImagesGet200ResponseImagesInner](docs/ImagesGet200ResponseImagesInner.md)
 - [HetznerCloudApi.ImagesGet200ResponseImagesInnerCreatedFrom](docs/ImagesGet200ResponseImagesInnerCreatedFrom.md)
 - [HetznerCloudApi.ImagesIdActionsChangeProtectionPostRequest](docs/ImagesIdActionsChangeProtectionPostRequest.md)
 - [HetznerCloudApi.ImagesIdGet200Response](docs/ImagesIdGet200Response.md)
 - [HetznerCloudApi.IsosGet200Response](docs/IsosGet200Response.md)
 - [HetznerCloudApi.IsosGet200ResponseIsosInner](docs/IsosGet200ResponseIsosInner.md)
 - [HetznerCloudApi.IsosIdGet200Response](docs/IsosIdGet200Response.md)
 - [HetznerCloudApi.LoadBalancerAlgorithm](docs/LoadBalancerAlgorithm.md)
 - [HetznerCloudApi.LoadBalancerService](docs/LoadBalancerService.md)
 - [HetznerCloudApi.LoadBalancerServiceHTTP](docs/LoadBalancerServiceHTTP.md)
 - [HetznerCloudApi.LoadBalancerServiceHealthCheck](docs/LoadBalancerServiceHealthCheck.md)
 - [HetznerCloudApi.LoadBalancerServiceHealthCheckHttp](docs/LoadBalancerServiceHealthCheckHttp.md)
 - [HetznerCloudApi.LoadBalancerTarget](docs/LoadBalancerTarget.md)
 - [HetznerCloudApi.LoadBalancerTargetHealthStatusInner](docs/LoadBalancerTargetHealthStatusInner.md)
 - [HetznerCloudApi.LoadBalancerTargetIP](docs/LoadBalancerTargetIP.md)
 - [HetznerCloudApi.LoadBalancerTargetLabelSelector](docs/LoadBalancerTargetLabelSelector.md)
 - [HetznerCloudApi.LoadBalancerTargetServer](docs/LoadBalancerTargetServer.md)
 - [HetznerCloudApi.LoadBalancerTargetTarget](docs/LoadBalancerTargetTarget.md)
 - [HetznerCloudApi.LoadBalancerTypesGet200Response](docs/LoadBalancerTypesGet200Response.md)
 - [HetznerCloudApi.LoadBalancerTypesGet200ResponseLoadBalancerTypesInner](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInner.md)
 - [HetznerCloudApi.LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInner.md)
 - [HetznerCloudApi.LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceHourly.md)
 - [HetznerCloudApi.LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly](docs/LoadBalancerTypesGet200ResponseLoadBalancerTypesInnerPricesInnerPriceMonthly.md)
 - [HetznerCloudApi.LoadBalancerTypesIdGet200Response](docs/LoadBalancerTypesIdGet200Response.md)
 - [HetznerCloudApi.LoadBalancersGet200Response](docs/LoadBalancersGet200Response.md)
 - [HetznerCloudApi.LoadBalancersGet200ResponseLoadBalancersInner](docs/LoadBalancersGet200ResponseLoadBalancersInner.md)
 - [HetznerCloudApi.LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm](docs/LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm.md)
 - [HetznerCloudApi.LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner](docs/LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner.md)
 - [HetznerCloudApi.LoadBalancersGet200ResponseLoadBalancersInnerPublicNet](docs/LoadBalancersGet200ResponseLoadBalancersInnerPublicNet.md)
 - [HetznerCloudApi.LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4](docs/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv4.md)
 - [HetznerCloudApi.LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6](docs/LoadBalancersGet200ResponseLoadBalancersInnerPublicNetIpv6.md)
 - [HetznerCloudApi.LoadBalancersIdActionsAttachToNetworkPostRequest](docs/LoadBalancersIdActionsAttachToNetworkPostRequest.md)
 - [HetznerCloudApi.LoadBalancersIdActionsChangeAlgorithmPostRequest](docs/LoadBalancersIdActionsChangeAlgorithmPostRequest.md)
 - [HetznerCloudApi.LoadBalancersIdActionsChangeProtectionPostRequest](docs/LoadBalancersIdActionsChangeProtectionPostRequest.md)
 - [HetznerCloudApi.LoadBalancersIdActionsDeleteServicePostRequest](docs/LoadBalancersIdActionsDeleteServicePostRequest.md)
 - [HetznerCloudApi.LoadBalancersIdActionsDetachFromNetworkPostRequest](docs/LoadBalancersIdActionsDetachFromNetworkPostRequest.md)
 - [HetznerCloudApi.LoadBalancersIdGet200Response](docs/LoadBalancersIdGet200Response.md)
 - [HetznerCloudApi.LoadBalancersIdMetricsGet200Response](docs/LoadBalancersIdMetricsGet200Response.md)
 - [HetznerCloudApi.LoadBalancersIdMetricsGet200ResponseMetrics](docs/LoadBalancersIdMetricsGet200ResponseMetrics.md)
 - [HetznerCloudApi.LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue](docs/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValue.md)
 - [HetznerCloudApi.LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner](docs/LoadBalancersIdMetricsGet200ResponseMetricsTimeSeriesValueValuesInnerInner.md)
 - [HetznerCloudApi.LoadBalancersIdPutRequest](docs/LoadBalancersIdPutRequest.md)
 - [HetznerCloudApi.LoadBalancersPost201Response](docs/LoadBalancersPost201Response.md)
 - [HetznerCloudApi.LocationsGet200Response](docs/LocationsGet200Response.md)
 - [HetznerCloudApi.LocationsIdGet200Response](docs/LocationsIdGet200Response.md)
 - [HetznerCloudApi.NetworksGet200Response](docs/NetworksGet200Response.md)
 - [HetznerCloudApi.NetworksGet200ResponseNetworksInner](docs/NetworksGet200ResponseNetworksInner.md)
 - [HetznerCloudApi.NetworksGet200ResponseNetworksInnerProtection](docs/NetworksGet200ResponseNetworksInnerProtection.md)
 - [HetznerCloudApi.NetworksGet200ResponseNetworksInnerRoutesInner](docs/NetworksGet200ResponseNetworksInnerRoutesInner.md)
 - [HetznerCloudApi.NetworksGet200ResponseNetworksInnerSubnetsInner](docs/NetworksGet200ResponseNetworksInnerSubnetsInner.md)
 - [HetznerCloudApi.NetworksPost201Response](docs/NetworksPost201Response.md)
 - [HetznerCloudApi.NullableAction](docs/NullableAction.md)
 - [HetznerCloudApi.PlacementGroup](docs/PlacementGroup.md)
 - [HetznerCloudApi.PlacementGroupNullable](docs/PlacementGroupNullable.md)
 - [HetznerCloudApi.PlacementGroupResponse](docs/PlacementGroupResponse.md)
 - [HetznerCloudApi.PlacementGroupsResponse](docs/PlacementGroupsResponse.md)
 - [HetznerCloudApi.PricingGet200Response](docs/PricingGet200Response.md)
 - [HetznerCloudApi.PricingGet200ResponsePricing](docs/PricingGet200ResponsePricing.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingFloatingIp](docs/PricingGet200ResponsePricingFloatingIp.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingFloatingIpPriceMonthly](docs/PricingGet200ResponsePricingFloatingIpPriceMonthly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingFloatingIpsInner](docs/PricingGet200ResponsePricingFloatingIpsInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingFloatingIpsInnerPricesInner](docs/PricingGet200ResponsePricingFloatingIpsInnerPricesInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingFloatingIpsInnerPricesInnerPriceMonthly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingImage](docs/PricingGet200ResponsePricingImage.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingLoadBalancerTypesInner](docs/PricingGet200ResponsePricingLoadBalancerTypesInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner](docs/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly](docs/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceHourly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingLoadBalancerTypesInnerPricesInnerPriceMonthly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingPrimaryIpsInner](docs/PricingGet200ResponsePricingPrimaryIpsInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingPrimaryIpsInnerPricesInner](docs/PricingGet200ResponsePricingPrimaryIpsInnerPricesInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly](docs/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceHourly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingPrimaryIpsInnerPricesInnerPriceMonthly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingServerBackup](docs/PricingGet200ResponsePricingServerBackup.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingServerTypesInner](docs/PricingGet200ResponsePricingServerTypesInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingServerTypesInnerPricesInner](docs/PricingGet200ResponsePricingServerTypesInnerPricesInner.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly](docs/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceHourly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly](docs/PricingGet200ResponsePricingServerTypesInnerPricesInnerPriceMonthly.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingTraffic](docs/PricingGet200ResponsePricingTraffic.md)
 - [HetznerCloudApi.PricingGet200ResponsePricingVolume](docs/PricingGet200ResponsePricingVolume.md)
 - [HetznerCloudApi.PrimaryIP](docs/PrimaryIP.md)
 - [HetznerCloudApi.PrimaryIPDatacenter](docs/PrimaryIPDatacenter.md)
 - [HetznerCloudApi.PrimaryIPDnsPtrInner](docs/PrimaryIPDnsPtrInner.md)
 - [HetznerCloudApi.PrimaryIPResponse](docs/PrimaryIPResponse.md)
 - [HetznerCloudApi.PrimaryIPsResponse](docs/PrimaryIPsResponse.md)
 - [HetznerCloudApi.RebuildServerRequest](docs/RebuildServerRequest.md)
 - [HetznerCloudApi.RemoveFromResourcesRequest](docs/RemoveFromResourcesRequest.md)
 - [HetznerCloudApi.RemoveTargetRequest](docs/RemoveTargetRequest.md)
 - [HetznerCloudApi.Rule](docs/Rule.md)
 - [HetznerCloudApi.ServerPublicNetFirewall](docs/ServerPublicNetFirewall.md)
 - [HetznerCloudApi.ServerTypesGet200Response](docs/ServerTypesGet200Response.md)
 - [HetznerCloudApi.ServerTypesGet200ResponseServerTypesInner](docs/ServerTypesGet200ResponseServerTypesInner.md)
 - [HetznerCloudApi.ServerTypesIdGet200Response](docs/ServerTypesIdGet200Response.md)
 - [HetznerCloudApi.ServersGet200Response](docs/ServersGet200Response.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInner](docs/ServersGet200ResponseServersInner.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerDatacenter](docs/ServersGet200ResponseServersInnerDatacenter.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerImage](docs/ServersGet200ResponseServersInnerImage.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerIso](docs/ServersGet200ResponseServersInnerIso.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerPrivateNetInner](docs/ServersGet200ResponseServersInnerPrivateNetInner.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerProtection](docs/ServersGet200ResponseServersInnerProtection.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerPublicNet](docs/ServersGet200ResponseServersInnerPublicNet.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerPublicNetIpv4](docs/ServersGet200ResponseServersInnerPublicNetIpv4.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerPublicNetIpv6](docs/ServersGet200ResponseServersInnerPublicNetIpv6.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner](docs/ServersGet200ResponseServersInnerPublicNetIpv6DnsPtrInner.md)
 - [HetznerCloudApi.ServersGet200ResponseServersInnerServerType](docs/ServersGet200ResponseServersInnerServerType.md)
 - [HetznerCloudApi.ServersIdActionsAttachIsoPostRequest](docs/ServersIdActionsAttachIsoPostRequest.md)
 - [HetznerCloudApi.ServersIdActionsChangeAliasIpsPostRequest](docs/ServersIdActionsChangeAliasIpsPostRequest.md)
 - [HetznerCloudApi.ServersIdActionsChangeDnsPtrPostRequest](docs/ServersIdActionsChangeDnsPtrPostRequest.md)
 - [HetznerCloudApi.ServersIdActionsChangeProtectionPostRequest](docs/ServersIdActionsChangeProtectionPostRequest.md)
 - [HetznerCloudApi.ServersIdActionsChangeTypePostRequest](docs/ServersIdActionsChangeTypePostRequest.md)
 - [HetznerCloudApi.ServersIdActionsCreateImagePost201Response](docs/ServersIdActionsCreateImagePost201Response.md)
 - [HetznerCloudApi.ServersIdActionsEnableRescuePost201Response](docs/ServersIdActionsEnableRescuePost201Response.md)
 - [HetznerCloudApi.ServersIdActionsEnableRescuePostRequest](docs/ServersIdActionsEnableRescuePostRequest.md)
 - [HetznerCloudApi.ServersIdActionsRebuildPost201Response](docs/ServersIdActionsRebuildPost201Response.md)
 - [HetznerCloudApi.ServersIdActionsRequestConsolePost201Response](docs/ServersIdActionsRequestConsolePost201Response.md)
 - [HetznerCloudApi.ServersIdDelete200Response](docs/ServersIdDelete200Response.md)
 - [HetznerCloudApi.ServersIdGet200Response](docs/ServersIdGet200Response.md)
 - [HetznerCloudApi.SetRulesRequest](docs/SetRulesRequest.md)
 - [HetznerCloudApi.SshKeysGet200Response](docs/SshKeysGet200Response.md)
 - [HetznerCloudApi.SshKeysGet200ResponseSshKeysInner](docs/SshKeysGet200ResponseSshKeysInner.md)
 - [HetznerCloudApi.SshKeysIdPutRequest](docs/SshKeysIdPutRequest.md)
 - [HetznerCloudApi.SshKeysPost201Response](docs/SshKeysPost201Response.md)
 - [HetznerCloudApi.SshKeysPostRequest](docs/SshKeysPostRequest.md)
 - [HetznerCloudApi.UpdateCertificateRequest](docs/UpdateCertificateRequest.md)
 - [HetznerCloudApi.UpdateFirewallRequest](docs/UpdateFirewallRequest.md)
 - [HetznerCloudApi.UpdateFloatingIPRequest](docs/UpdateFloatingIPRequest.md)
 - [HetznerCloudApi.UpdateImageRequest](docs/UpdateImageRequest.md)
 - [HetznerCloudApi.UpdateNetworkRequest](docs/UpdateNetworkRequest.md)
 - [HetznerCloudApi.UpdateNetworkRequestLabels](docs/UpdateNetworkRequestLabels.md)
 - [HetznerCloudApi.UpdatePlacementGroupRequest](docs/UpdatePlacementGroupRequest.md)
 - [HetznerCloudApi.UpdatePrimaryIPRequest](docs/UpdatePrimaryIPRequest.md)
 - [HetznerCloudApi.UpdateServerRequest](docs/UpdateServerRequest.md)
 - [HetznerCloudApi.UpdateVolumeRequest](docs/UpdateVolumeRequest.md)
 - [HetznerCloudApi.VolumesGet200Response](docs/VolumesGet200Response.md)
 - [HetznerCloudApi.VolumesGet200ResponseVolumesInner](docs/VolumesGet200ResponseVolumesInner.md)
 - [HetznerCloudApi.VolumesGet200ResponseVolumesInnerLocation](docs/VolumesGet200ResponseVolumesInnerLocation.md)
 - [HetznerCloudApi.VolumesIdActionsChangeProtectionPostRequest](docs/VolumesIdActionsChangeProtectionPostRequest.md)
 - [HetznerCloudApi.VolumesIdActionsResizePostRequest](docs/VolumesIdActionsResizePostRequest.md)
 - [HetznerCloudApi.VolumesIdGet200Response](docs/VolumesIdGet200Response.md)
 - [HetznerCloudApi.VolumesPost201Response](docs/VolumesPost201Response.md)


## Documentation for Authorization

Endpoints do not require authorization.

