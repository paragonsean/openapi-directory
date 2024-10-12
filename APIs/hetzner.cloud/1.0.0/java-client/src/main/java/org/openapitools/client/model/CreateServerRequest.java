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
import java.util.List;
import org.openapitools.client.model.CreateServerRequestFirewallsInner;
import org.openapitools.client.model.CreateServerRequestPublicNet;

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
 * CreateServerRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:42:41.028370-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateServerRequest {
  public static final String SERIALIZED_NAME_AUTOMOUNT = "automount";
  @SerializedName(SERIALIZED_NAME_AUTOMOUNT)
  private Boolean automount;

  public static final String SERIALIZED_NAME_DATACENTER = "datacenter";
  @SerializedName(SERIALIZED_NAME_DATACENTER)
  private String datacenter;

  public static final String SERIALIZED_NAME_FIREWALLS = "firewalls";
  @SerializedName(SERIALIZED_NAME_FIREWALLS)
  private List<CreateServerRequestFirewallsInner> firewalls = new ArrayList<>();

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_LABELS = "labels";
  @SerializedName(SERIALIZED_NAME_LABELS)
  private Object labels;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private String location;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NETWORKS = "networks";
  @SerializedName(SERIALIZED_NAME_NETWORKS)
  private List<Integer> networks = new ArrayList<>();

  public static final String SERIALIZED_NAME_PLACEMENT_GROUP = "placement_group";
  @SerializedName(SERIALIZED_NAME_PLACEMENT_GROUP)
  private Integer placementGroup;

  public static final String SERIALIZED_NAME_PUBLIC_NET = "public_net";
  @SerializedName(SERIALIZED_NAME_PUBLIC_NET)
  private CreateServerRequestPublicNet publicNet;

  public static final String SERIALIZED_NAME_SERVER_TYPE = "server_type";
  @SerializedName(SERIALIZED_NAME_SERVER_TYPE)
  private String serverType;

  public static final String SERIALIZED_NAME_SSH_KEYS = "ssh_keys";
  @SerializedName(SERIALIZED_NAME_SSH_KEYS)
  private List<String> sshKeys = new ArrayList<>();

  public static final String SERIALIZED_NAME_START_AFTER_CREATE = "start_after_create";
  @SerializedName(SERIALIZED_NAME_START_AFTER_CREATE)
  private Boolean startAfterCreate;

  public static final String SERIALIZED_NAME_USER_DATA = "user_data";
  @SerializedName(SERIALIZED_NAME_USER_DATA)
  private String userData;

  public static final String SERIALIZED_NAME_VOLUMES = "volumes";
  @SerializedName(SERIALIZED_NAME_VOLUMES)
  private List<Integer> volumes = new ArrayList<>();

  public CreateServerRequest() {
  }

  public CreateServerRequest automount(Boolean automount) {
    this.automount = automount;
    return this;
  }

  /**
   * Auto-mount Volumes after attach
   * @return automount
   */
  @javax.annotation.Nullable
  public Boolean getAutomount() {
    return automount;
  }

  public void setAutomount(Boolean automount) {
    this.automount = automount;
  }


  public CreateServerRequest datacenter(String datacenter) {
    this.datacenter = datacenter;
    return this;
  }

  /**
   * ID or name of Datacenter to create Server in (must not be used together with location)
   * @return datacenter
   */
  @javax.annotation.Nullable
  public String getDatacenter() {
    return datacenter;
  }

  public void setDatacenter(String datacenter) {
    this.datacenter = datacenter;
  }


  public CreateServerRequest firewalls(List<CreateServerRequestFirewallsInner> firewalls) {
    this.firewalls = firewalls;
    return this;
  }

  public CreateServerRequest addFirewallsItem(CreateServerRequestFirewallsInner firewallsItem) {
    if (this.firewalls == null) {
      this.firewalls = new ArrayList<>();
    }
    this.firewalls.add(firewallsItem);
    return this;
  }

  /**
   * Firewalls which should be applied on the Server&#39;s public network interface at creation time
   * @return firewalls
   */
  @javax.annotation.Nullable
  public List<CreateServerRequestFirewallsInner> getFirewalls() {
    return firewalls;
  }

  public void setFirewalls(List<CreateServerRequestFirewallsInner> firewalls) {
    this.firewalls = firewalls;
  }


  public CreateServerRequest image(String image) {
    this.image = image;
    return this;
  }

  /**
   * ID or name of the Image the Server is created from
   * @return image
   */
  @javax.annotation.Nonnull
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public CreateServerRequest labels(Object labels) {
    this.labels = labels;
    return this;
  }

  /**
   * User-defined labels (key-value pairs)
   * @return labels
   */
  @javax.annotation.Nullable
  public Object getLabels() {
    return labels;
  }

  public void setLabels(Object labels) {
    this.labels = labels;
  }


  public CreateServerRequest location(String location) {
    this.location = location;
    return this;
  }

  /**
   * ID or name of Location to create Server in (must not be used together with datacenter)
   * @return location
   */
  @javax.annotation.Nullable
  public String getLocation() {
    return location;
  }

  public void setLocation(String location) {
    this.location = location;
  }


  public CreateServerRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the Server to create (must be unique per Project and a valid hostname as per RFC 1123)
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateServerRequest networks(List<Integer> networks) {
    this.networks = networks;
    return this;
  }

  public CreateServerRequest addNetworksItem(Integer networksItem) {
    if (this.networks == null) {
      this.networks = new ArrayList<>();
    }
    this.networks.add(networksItem);
    return this;
  }

  /**
   * Network IDs which should be attached to the Server private network interface at the creation time
   * @return networks
   */
  @javax.annotation.Nullable
  public List<Integer> getNetworks() {
    return networks;
  }

  public void setNetworks(List<Integer> networks) {
    this.networks = networks;
  }


  public CreateServerRequest placementGroup(Integer placementGroup) {
    this.placementGroup = placementGroup;
    return this;
  }

  /**
   * ID of the Placement Group the server should be in
   * @return placementGroup
   */
  @javax.annotation.Nullable
  public Integer getPlacementGroup() {
    return placementGroup;
  }

  public void setPlacementGroup(Integer placementGroup) {
    this.placementGroup = placementGroup;
  }


  public CreateServerRequest publicNet(CreateServerRequestPublicNet publicNet) {
    this.publicNet = publicNet;
    return this;
  }

  /**
   * Get publicNet
   * @return publicNet
   */
  @javax.annotation.Nullable
  public CreateServerRequestPublicNet getPublicNet() {
    return publicNet;
  }

  public void setPublicNet(CreateServerRequestPublicNet publicNet) {
    this.publicNet = publicNet;
  }


  public CreateServerRequest serverType(String serverType) {
    this.serverType = serverType;
    return this;
  }

  /**
   * ID or name of the Server type this Server should be created with
   * @return serverType
   */
  @javax.annotation.Nonnull
  public String getServerType() {
    return serverType;
  }

  public void setServerType(String serverType) {
    this.serverType = serverType;
  }


  public CreateServerRequest sshKeys(List<String> sshKeys) {
    this.sshKeys = sshKeys;
    return this;
  }

  public CreateServerRequest addSshKeysItem(String sshKeysItem) {
    if (this.sshKeys == null) {
      this.sshKeys = new ArrayList<>();
    }
    this.sshKeys.add(sshKeysItem);
    return this;
  }

  /**
   * SSH key IDs (&#x60;integer&#x60;) or names (&#x60;string&#x60;) which should be injected into the Server at creation time
   * @return sshKeys
   */
  @javax.annotation.Nullable
  public List<String> getSshKeys() {
    return sshKeys;
  }

  public void setSshKeys(List<String> sshKeys) {
    this.sshKeys = sshKeys;
  }


  public CreateServerRequest startAfterCreate(Boolean startAfterCreate) {
    this.startAfterCreate = startAfterCreate;
    return this;
  }

  /**
   * Start Server right after creation. Defaults to true.
   * @return startAfterCreate
   */
  @javax.annotation.Nullable
  public Boolean getStartAfterCreate() {
    return startAfterCreate;
  }

  public void setStartAfterCreate(Boolean startAfterCreate) {
    this.startAfterCreate = startAfterCreate;
  }


  public CreateServerRequest userData(String userData) {
    this.userData = userData;
    return this;
  }

  /**
   * Cloud-Init user data to use during Server creation. This field is limited to 32KiB.
   * @return userData
   */
  @javax.annotation.Nullable
  public String getUserData() {
    return userData;
  }

  public void setUserData(String userData) {
    this.userData = userData;
  }


  public CreateServerRequest volumes(List<Integer> volumes) {
    this.volumes = volumes;
    return this;
  }

  public CreateServerRequest addVolumesItem(Integer volumesItem) {
    if (this.volumes == null) {
      this.volumes = new ArrayList<>();
    }
    this.volumes.add(volumesItem);
    return this;
  }

  /**
   * Volume IDs which should be attached to the Server at the creation time. Volumes must be in the same Location.
   * @return volumes
   */
  @javax.annotation.Nullable
  public List<Integer> getVolumes() {
    return volumes;
  }

  public void setVolumes(List<Integer> volumes) {
    this.volumes = volumes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateServerRequest createServerRequest = (CreateServerRequest) o;
    return Objects.equals(this.automount, createServerRequest.automount) &&
        Objects.equals(this.datacenter, createServerRequest.datacenter) &&
        Objects.equals(this.firewalls, createServerRequest.firewalls) &&
        Objects.equals(this.image, createServerRequest.image) &&
        Objects.equals(this.labels, createServerRequest.labels) &&
        Objects.equals(this.location, createServerRequest.location) &&
        Objects.equals(this.name, createServerRequest.name) &&
        Objects.equals(this.networks, createServerRequest.networks) &&
        Objects.equals(this.placementGroup, createServerRequest.placementGroup) &&
        Objects.equals(this.publicNet, createServerRequest.publicNet) &&
        Objects.equals(this.serverType, createServerRequest.serverType) &&
        Objects.equals(this.sshKeys, createServerRequest.sshKeys) &&
        Objects.equals(this.startAfterCreate, createServerRequest.startAfterCreate) &&
        Objects.equals(this.userData, createServerRequest.userData) &&
        Objects.equals(this.volumes, createServerRequest.volumes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(automount, datacenter, firewalls, image, labels, location, name, networks, placementGroup, publicNet, serverType, sshKeys, startAfterCreate, userData, volumes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateServerRequest {\n");
    sb.append("    automount: ").append(toIndentedString(automount)).append("\n");
    sb.append("    datacenter: ").append(toIndentedString(datacenter)).append("\n");
    sb.append("    firewalls: ").append(toIndentedString(firewalls)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    labels: ").append(toIndentedString(labels)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    networks: ").append(toIndentedString(networks)).append("\n");
    sb.append("    placementGroup: ").append(toIndentedString(placementGroup)).append("\n");
    sb.append("    publicNet: ").append(toIndentedString(publicNet)).append("\n");
    sb.append("    serverType: ").append(toIndentedString(serverType)).append("\n");
    sb.append("    sshKeys: ").append(toIndentedString(sshKeys)).append("\n");
    sb.append("    startAfterCreate: ").append(toIndentedString(startAfterCreate)).append("\n");
    sb.append("    userData: ").append(toIndentedString(userData)).append("\n");
    sb.append("    volumes: ").append(toIndentedString(volumes)).append("\n");
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
    openapiFields.add("automount");
    openapiFields.add("datacenter");
    openapiFields.add("firewalls");
    openapiFields.add("image");
    openapiFields.add("labels");
    openapiFields.add("location");
    openapiFields.add("name");
    openapiFields.add("networks");
    openapiFields.add("placement_group");
    openapiFields.add("public_net");
    openapiFields.add("server_type");
    openapiFields.add("ssh_keys");
    openapiFields.add("start_after_create");
    openapiFields.add("user_data");
    openapiFields.add("volumes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("image");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("server_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateServerRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateServerRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateServerRequest is not found in the empty JSON string", CreateServerRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateServerRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateServerRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateServerRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("datacenter") != null && !jsonObj.get("datacenter").isJsonNull()) && !jsonObj.get("datacenter").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `datacenter` to be a primitive type in the JSON string but got `%s`", jsonObj.get("datacenter").toString()));
      }
      if (jsonObj.get("firewalls") != null && !jsonObj.get("firewalls").isJsonNull()) {
        JsonArray jsonArrayfirewalls = jsonObj.getAsJsonArray("firewalls");
        if (jsonArrayfirewalls != null) {
          // ensure the json data is an array
          if (!jsonObj.get("firewalls").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `firewalls` to be an array in the JSON string but got `%s`", jsonObj.get("firewalls").toString()));
          }

          // validate the optional field `firewalls` (array)
          for (int i = 0; i < jsonArrayfirewalls.size(); i++) {
            CreateServerRequestFirewallsInner.validateJsonElement(jsonArrayfirewalls.get(i));
          };
        }
      }
      if (!jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if ((jsonObj.get("location") != null && !jsonObj.get("location").isJsonNull()) && !jsonObj.get("location").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("networks") != null && !jsonObj.get("networks").isJsonNull() && !jsonObj.get("networks").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `networks` to be an array in the JSON string but got `%s`", jsonObj.get("networks").toString()));
      }
      // validate the optional field `public_net`
      if (jsonObj.get("public_net") != null && !jsonObj.get("public_net").isJsonNull()) {
        CreateServerRequestPublicNet.validateJsonElement(jsonObj.get("public_net"));
      }
      if (!jsonObj.get("server_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `server_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("server_type").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("ssh_keys") != null && !jsonObj.get("ssh_keys").isJsonNull() && !jsonObj.get("ssh_keys").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssh_keys` to be an array in the JSON string but got `%s`", jsonObj.get("ssh_keys").toString()));
      }
      if ((jsonObj.get("user_data") != null && !jsonObj.get("user_data").isJsonNull()) && !jsonObj.get("user_data").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_data` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_data").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("volumes") != null && !jsonObj.get("volumes").isJsonNull() && !jsonObj.get("volumes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `volumes` to be an array in the JSON string but got `%s`", jsonObj.get("volumes").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateServerRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateServerRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateServerRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateServerRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateServerRequest>() {
           @Override
           public void write(JsonWriter out, CreateServerRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateServerRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateServerRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateServerRequest
   * @throws IOException if the JSON string is invalid with respect to CreateServerRequest
   */
  public static CreateServerRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateServerRequest.class);
  }

  /**
   * Convert an instance of CreateServerRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

