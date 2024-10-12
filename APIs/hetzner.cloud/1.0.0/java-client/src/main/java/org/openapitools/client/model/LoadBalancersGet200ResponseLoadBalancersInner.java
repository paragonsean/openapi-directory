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


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.DatacentersGet200ResponseDatacentersInnerLocation;
import org.openapitools.client.model.FloatingIpsGet200ResponseFloatingIpsInnerProtection;
import org.openapitools.client.model.LoadBalancerService;
import org.openapitools.client.model.LoadBalancerTarget;
import org.openapitools.client.model.LoadBalancerTypesGet200ResponseLoadBalancerTypesInner;
import org.openapitools.client.model.LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm;
import org.openapitools.client.model.LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner;
import org.openapitools.client.model.LoadBalancersGet200ResponseLoadBalancersInnerPublicNet;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * LoadBalancersGet200ResponseLoadBalancersInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:42:41.028370-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LoadBalancersGet200ResponseLoadBalancersInner {
  public static final String SERIALIZED_NAME_ALGORITHM = "algorithm";
  @SerializedName(SERIALIZED_NAME_ALGORITHM)
  private LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm algorithm;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INCLUDED_TRAFFIC = "included_traffic";
  @SerializedName(SERIALIZED_NAME_INCLUDED_TRAFFIC)
  private Integer includedTraffic;

  public static final String SERIALIZED_NAME_INGOING_TRAFFIC = "ingoing_traffic";
  @SerializedName(SERIALIZED_NAME_INGOING_TRAFFIC)
  private Integer ingoingTraffic;

  public static final String SERIALIZED_NAME_LABELS = "labels";
  @SerializedName(SERIALIZED_NAME_LABELS)
  private Map<String, String> labels = new HashMap<>();

  public static final String SERIALIZED_NAME_LOAD_BALANCER_TYPE = "load_balancer_type";
  @SerializedName(SERIALIZED_NAME_LOAD_BALANCER_TYPE)
  private LoadBalancerTypesGet200ResponseLoadBalancerTypesInner loadBalancerType;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private DatacentersGet200ResponseDatacentersInnerLocation location;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OUTGOING_TRAFFIC = "outgoing_traffic";
  @SerializedName(SERIALIZED_NAME_OUTGOING_TRAFFIC)
  private Integer outgoingTraffic;

  public static final String SERIALIZED_NAME_PRIVATE_NET = "private_net";
  @SerializedName(SERIALIZED_NAME_PRIVATE_NET)
  private List<LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner> privateNet = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROTECTION = "protection";
  @SerializedName(SERIALIZED_NAME_PROTECTION)
  private FloatingIpsGet200ResponseFloatingIpsInnerProtection protection;

  public static final String SERIALIZED_NAME_PUBLIC_NET = "public_net";
  @SerializedName(SERIALIZED_NAME_PUBLIC_NET)
  private LoadBalancersGet200ResponseLoadBalancersInnerPublicNet publicNet;

  public static final String SERIALIZED_NAME_SERVICES = "services";
  @SerializedName(SERIALIZED_NAME_SERVICES)
  private List<LoadBalancerService> services = new ArrayList<>();

  public static final String SERIALIZED_NAME_TARGETS = "targets";
  @SerializedName(SERIALIZED_NAME_TARGETS)
  private List<LoadBalancerTarget> targets = new ArrayList<>();

  public LoadBalancersGet200ResponseLoadBalancersInner() {
  }

  public LoadBalancersGet200ResponseLoadBalancersInner algorithm(LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm algorithm) {
    this.algorithm = algorithm;
    return this;
  }

  /**
   * Get algorithm
   * @return algorithm
   */
  @javax.annotation.Nonnull
  public LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm getAlgorithm() {
    return algorithm;
  }

  public void setAlgorithm(LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm algorithm) {
    this.algorithm = algorithm;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner created(String created) {
    this.created = created;
    return this;
  }

  /**
   * Point in time when the Resource was created (in ISO-8601 format)
   * @return created
   */
  @javax.annotation.Nonnull
  public String getCreated() {
    return created;
  }

  public void setCreated(String created) {
    this.created = created;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * ID of the Resource
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner includedTraffic(Integer includedTraffic) {
    this.includedTraffic = includedTraffic;
    return this;
  }

  /**
   * Free Traffic for the current billing period in bytes
   * @return includedTraffic
   */
  @javax.annotation.Nonnull
  public Integer getIncludedTraffic() {
    return includedTraffic;
  }

  public void setIncludedTraffic(Integer includedTraffic) {
    this.includedTraffic = includedTraffic;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner ingoingTraffic(Integer ingoingTraffic) {
    this.ingoingTraffic = ingoingTraffic;
    return this;
  }

  /**
   * Inbound Traffic for the current billing period in bytes
   * @return ingoingTraffic
   */
  @javax.annotation.Nullable
  public Integer getIngoingTraffic() {
    return ingoingTraffic;
  }

  public void setIngoingTraffic(Integer ingoingTraffic) {
    this.ingoingTraffic = ingoingTraffic;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner labels(Map<String, String> labels) {
    this.labels = labels;
    return this;
  }

  public LoadBalancersGet200ResponseLoadBalancersInner putLabelsItem(String key, String labelsItem) {
    if (this.labels == null) {
      this.labels = new HashMap<>();
    }
    this.labels.put(key, labelsItem);
    return this;
  }

  /**
   * User-defined labels (key-value pairs)
   * @return labels
   */
  @javax.annotation.Nonnull
  public Map<String, String> getLabels() {
    return labels;
  }

  public void setLabels(Map<String, String> labels) {
    this.labels = labels;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner loadBalancerType(LoadBalancerTypesGet200ResponseLoadBalancerTypesInner loadBalancerType) {
    this.loadBalancerType = loadBalancerType;
    return this;
  }

  /**
   * Get loadBalancerType
   * @return loadBalancerType
   */
  @javax.annotation.Nonnull
  public LoadBalancerTypesGet200ResponseLoadBalancerTypesInner getLoadBalancerType() {
    return loadBalancerType;
  }

  public void setLoadBalancerType(LoadBalancerTypesGet200ResponseLoadBalancerTypesInner loadBalancerType) {
    this.loadBalancerType = loadBalancerType;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner location(DatacentersGet200ResponseDatacentersInnerLocation location) {
    this.location = location;
    return this;
  }

  /**
   * Get location
   * @return location
   */
  @javax.annotation.Nonnull
  public DatacentersGet200ResponseDatacentersInnerLocation getLocation() {
    return location;
  }

  public void setLocation(DatacentersGet200ResponseDatacentersInnerLocation location) {
    this.location = location;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the Resource. Must be unique per Project.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner outgoingTraffic(Integer outgoingTraffic) {
    this.outgoingTraffic = outgoingTraffic;
    return this;
  }

  /**
   * Outbound Traffic for the current billing period in bytes
   * @return outgoingTraffic
   */
  @javax.annotation.Nullable
  public Integer getOutgoingTraffic() {
    return outgoingTraffic;
  }

  public void setOutgoingTraffic(Integer outgoingTraffic) {
    this.outgoingTraffic = outgoingTraffic;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner privateNet(List<LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner> privateNet) {
    this.privateNet = privateNet;
    return this;
  }

  public LoadBalancersGet200ResponseLoadBalancersInner addPrivateNetItem(LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner privateNetItem) {
    if (this.privateNet == null) {
      this.privateNet = new ArrayList<>();
    }
    this.privateNet.add(privateNetItem);
    return this;
  }

  /**
   * Private networks information
   * @return privateNet
   */
  @javax.annotation.Nonnull
  public List<LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner> getPrivateNet() {
    return privateNet;
  }

  public void setPrivateNet(List<LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner> privateNet) {
    this.privateNet = privateNet;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner protection(FloatingIpsGet200ResponseFloatingIpsInnerProtection protection) {
    this.protection = protection;
    return this;
  }

  /**
   * Get protection
   * @return protection
   */
  @javax.annotation.Nonnull
  public FloatingIpsGet200ResponseFloatingIpsInnerProtection getProtection() {
    return protection;
  }

  public void setProtection(FloatingIpsGet200ResponseFloatingIpsInnerProtection protection) {
    this.protection = protection;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner publicNet(LoadBalancersGet200ResponseLoadBalancersInnerPublicNet publicNet) {
    this.publicNet = publicNet;
    return this;
  }

  /**
   * Get publicNet
   * @return publicNet
   */
  @javax.annotation.Nonnull
  public LoadBalancersGet200ResponseLoadBalancersInnerPublicNet getPublicNet() {
    return publicNet;
  }

  public void setPublicNet(LoadBalancersGet200ResponseLoadBalancersInnerPublicNet publicNet) {
    this.publicNet = publicNet;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner services(List<LoadBalancerService> services) {
    this.services = services;
    return this;
  }

  public LoadBalancersGet200ResponseLoadBalancersInner addServicesItem(LoadBalancerService servicesItem) {
    if (this.services == null) {
      this.services = new ArrayList<>();
    }
    this.services.add(servicesItem);
    return this;
  }

  /**
   * List of services that belong to this Load Balancer
   * @return services
   */
  @javax.annotation.Nonnull
  public List<LoadBalancerService> getServices() {
    return services;
  }

  public void setServices(List<LoadBalancerService> services) {
    this.services = services;
  }


  public LoadBalancersGet200ResponseLoadBalancersInner targets(List<LoadBalancerTarget> targets) {
    this.targets = targets;
    return this;
  }

  public LoadBalancersGet200ResponseLoadBalancersInner addTargetsItem(LoadBalancerTarget targetsItem) {
    if (this.targets == null) {
      this.targets = new ArrayList<>();
    }
    this.targets.add(targetsItem);
    return this;
  }

  /**
   * List of targets that belong to this Load Balancer
   * @return targets
   */
  @javax.annotation.Nonnull
  public List<LoadBalancerTarget> getTargets() {
    return targets;
  }

  public void setTargets(List<LoadBalancerTarget> targets) {
    this.targets = targets;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LoadBalancersGet200ResponseLoadBalancersInner loadBalancersGet200ResponseLoadBalancersInner = (LoadBalancersGet200ResponseLoadBalancersInner) o;
    return Objects.equals(this.algorithm, loadBalancersGet200ResponseLoadBalancersInner.algorithm) &&
        Objects.equals(this.created, loadBalancersGet200ResponseLoadBalancersInner.created) &&
        Objects.equals(this.id, loadBalancersGet200ResponseLoadBalancersInner.id) &&
        Objects.equals(this.includedTraffic, loadBalancersGet200ResponseLoadBalancersInner.includedTraffic) &&
        Objects.equals(this.ingoingTraffic, loadBalancersGet200ResponseLoadBalancersInner.ingoingTraffic) &&
        Objects.equals(this.labels, loadBalancersGet200ResponseLoadBalancersInner.labels) &&
        Objects.equals(this.loadBalancerType, loadBalancersGet200ResponseLoadBalancersInner.loadBalancerType) &&
        Objects.equals(this.location, loadBalancersGet200ResponseLoadBalancersInner.location) &&
        Objects.equals(this.name, loadBalancersGet200ResponseLoadBalancersInner.name) &&
        Objects.equals(this.outgoingTraffic, loadBalancersGet200ResponseLoadBalancersInner.outgoingTraffic) &&
        Objects.equals(this.privateNet, loadBalancersGet200ResponseLoadBalancersInner.privateNet) &&
        Objects.equals(this.protection, loadBalancersGet200ResponseLoadBalancersInner.protection) &&
        Objects.equals(this.publicNet, loadBalancersGet200ResponseLoadBalancersInner.publicNet) &&
        Objects.equals(this.services, loadBalancersGet200ResponseLoadBalancersInner.services) &&
        Objects.equals(this.targets, loadBalancersGet200ResponseLoadBalancersInner.targets);
  }

  @Override
  public int hashCode() {
    return Objects.hash(algorithm, created, id, includedTraffic, ingoingTraffic, labels, loadBalancerType, location, name, outgoingTraffic, privateNet, protection, publicNet, services, targets);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LoadBalancersGet200ResponseLoadBalancersInner {\n");
    sb.append("    algorithm: ").append(toIndentedString(algorithm)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    includedTraffic: ").append(toIndentedString(includedTraffic)).append("\n");
    sb.append("    ingoingTraffic: ").append(toIndentedString(ingoingTraffic)).append("\n");
    sb.append("    labels: ").append(toIndentedString(labels)).append("\n");
    sb.append("    loadBalancerType: ").append(toIndentedString(loadBalancerType)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    outgoingTraffic: ").append(toIndentedString(outgoingTraffic)).append("\n");
    sb.append("    privateNet: ").append(toIndentedString(privateNet)).append("\n");
    sb.append("    protection: ").append(toIndentedString(protection)).append("\n");
    sb.append("    publicNet: ").append(toIndentedString(publicNet)).append("\n");
    sb.append("    services: ").append(toIndentedString(services)).append("\n");
    sb.append("    targets: ").append(toIndentedString(targets)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("algorithm");
    openapiFields.add("created");
    openapiFields.add("id");
    openapiFields.add("included_traffic");
    openapiFields.add("ingoing_traffic");
    openapiFields.add("labels");
    openapiFields.add("load_balancer_type");
    openapiFields.add("location");
    openapiFields.add("name");
    openapiFields.add("outgoing_traffic");
    openapiFields.add("private_net");
    openapiFields.add("protection");
    openapiFields.add("public_net");
    openapiFields.add("services");
    openapiFields.add("targets");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("algorithm");
    openapiRequiredFields.add("created");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("included_traffic");
    openapiRequiredFields.add("ingoing_traffic");
    openapiRequiredFields.add("labels");
    openapiRequiredFields.add("load_balancer_type");
    openapiRequiredFields.add("location");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("outgoing_traffic");
    openapiRequiredFields.add("private_net");
    openapiRequiredFields.add("protection");
    openapiRequiredFields.add("public_net");
    openapiRequiredFields.add("services");
    openapiRequiredFields.add("targets");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LoadBalancersGet200ResponseLoadBalancersInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LoadBalancersGet200ResponseLoadBalancersInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LoadBalancersGet200ResponseLoadBalancersInner is not found in the empty JSON string", LoadBalancersGet200ResponseLoadBalancersInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LoadBalancersGet200ResponseLoadBalancersInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LoadBalancersGet200ResponseLoadBalancersInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : LoadBalancersGet200ResponseLoadBalancersInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `algorithm`
      LoadBalancersGet200ResponseLoadBalancersInnerAlgorithm.validateJsonElement(jsonObj.get("algorithm"));
      if (!jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      // validate the required field `load_balancer_type`
      LoadBalancerTypesGet200ResponseLoadBalancerTypesInner.validateJsonElement(jsonObj.get("load_balancer_type"));
      // validate the required field `location`
      DatacentersGet200ResponseDatacentersInnerLocation.validateJsonElement(jsonObj.get("location"));
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("private_net").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `private_net` to be an array in the JSON string but got `%s`", jsonObj.get("private_net").toString()));
      }

      JsonArray jsonArrayprivateNet = jsonObj.getAsJsonArray("private_net");
      // validate the required field `private_net` (array)
      for (int i = 0; i < jsonArrayprivateNet.size(); i++) {
        LoadBalancersGet200ResponseLoadBalancersInnerPrivateNetInner.validateJsonElement(jsonArrayprivateNet.get(i));
      };
      // validate the required field `protection`
      FloatingIpsGet200ResponseFloatingIpsInnerProtection.validateJsonElement(jsonObj.get("protection"));
      // validate the required field `public_net`
      LoadBalancersGet200ResponseLoadBalancersInnerPublicNet.validateJsonElement(jsonObj.get("public_net"));
      // ensure the json data is an array
      if (!jsonObj.get("services").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `services` to be an array in the JSON string but got `%s`", jsonObj.get("services").toString()));
      }

      JsonArray jsonArrayservices = jsonObj.getAsJsonArray("services");
      // validate the required field `services` (array)
      for (int i = 0; i < jsonArrayservices.size(); i++) {
        LoadBalancerService.validateJsonElement(jsonArrayservices.get(i));
      };
      // ensure the json data is an array
      if (!jsonObj.get("targets").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `targets` to be an array in the JSON string but got `%s`", jsonObj.get("targets").toString()));
      }

      JsonArray jsonArraytargets = jsonObj.getAsJsonArray("targets");
      // validate the required field `targets` (array)
      for (int i = 0; i < jsonArraytargets.size(); i++) {
        LoadBalancerTarget.validateJsonElement(jsonArraytargets.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LoadBalancersGet200ResponseLoadBalancersInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LoadBalancersGet200ResponseLoadBalancersInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LoadBalancersGet200ResponseLoadBalancersInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LoadBalancersGet200ResponseLoadBalancersInner.class));

       return (TypeAdapter<T>) new TypeAdapter<LoadBalancersGet200ResponseLoadBalancersInner>() {
           @Override
           public void write(JsonWriter out, LoadBalancersGet200ResponseLoadBalancersInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LoadBalancersGet200ResponseLoadBalancersInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LoadBalancersGet200ResponseLoadBalancersInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LoadBalancersGet200ResponseLoadBalancersInner
   * @throws IOException if the JSON string is invalid with respect to LoadBalancersGet200ResponseLoadBalancersInner
   */
  public static LoadBalancersGet200ResponseLoadBalancersInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LoadBalancersGet200ResponseLoadBalancersInner.class);
  }

  /**
   * Convert an instance of LoadBalancersGet200ResponseLoadBalancersInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

