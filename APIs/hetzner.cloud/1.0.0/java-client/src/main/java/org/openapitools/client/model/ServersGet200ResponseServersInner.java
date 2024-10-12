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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.PlacementGroupNullable;
import org.openapitools.client.model.ServersGet200ResponseServersInnerDatacenter;
import org.openapitools.client.model.ServersGet200ResponseServersInnerImage;
import org.openapitools.client.model.ServersGet200ResponseServersInnerIso;
import org.openapitools.client.model.ServersGet200ResponseServersInnerPrivateNetInner;
import org.openapitools.client.model.ServersGet200ResponseServersInnerProtection;
import org.openapitools.client.model.ServersGet200ResponseServersInnerPublicNet;
import org.openapitools.client.model.ServersGet200ResponseServersInnerServerType;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * ServersGet200ResponseServersInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:42:41.028370-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServersGet200ResponseServersInner {
  public static final String SERIALIZED_NAME_BACKUP_WINDOW = "backup_window";
  @SerializedName(SERIALIZED_NAME_BACKUP_WINDOW)
  private String backupWindow;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_DATACENTER = "datacenter";
  @SerializedName(SERIALIZED_NAME_DATACENTER)
  private ServersGet200ResponseServersInnerDatacenter datacenter;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private ServersGet200ResponseServersInnerImage image;

  public static final String SERIALIZED_NAME_INCLUDED_TRAFFIC = "included_traffic";
  @SerializedName(SERIALIZED_NAME_INCLUDED_TRAFFIC)
  private BigDecimal includedTraffic;

  public static final String SERIALIZED_NAME_INGOING_TRAFFIC = "ingoing_traffic";
  @SerializedName(SERIALIZED_NAME_INGOING_TRAFFIC)
  private BigDecimal ingoingTraffic;

  public static final String SERIALIZED_NAME_ISO = "iso";
  @SerializedName(SERIALIZED_NAME_ISO)
  private ServersGet200ResponseServersInnerIso iso;

  public static final String SERIALIZED_NAME_LABELS = "labels";
  @SerializedName(SERIALIZED_NAME_LABELS)
  private Map<String, String> labels = new HashMap<>();

  public static final String SERIALIZED_NAME_LOAD_BALANCERS = "load_balancers";
  @SerializedName(SERIALIZED_NAME_LOAD_BALANCERS)
  private List<Integer> loadBalancers = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOCKED = "locked";
  @SerializedName(SERIALIZED_NAME_LOCKED)
  private Boolean locked;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OUTGOING_TRAFFIC = "outgoing_traffic";
  @SerializedName(SERIALIZED_NAME_OUTGOING_TRAFFIC)
  private BigDecimal outgoingTraffic;

  public static final String SERIALIZED_NAME_PLACEMENT_GROUP = "placement_group";
  @SerializedName(SERIALIZED_NAME_PLACEMENT_GROUP)
  private PlacementGroupNullable placementGroup;

  public static final String SERIALIZED_NAME_PRIMARY_DISK_SIZE = "primary_disk_size";
  @SerializedName(SERIALIZED_NAME_PRIMARY_DISK_SIZE)
  private BigDecimal primaryDiskSize;

  public static final String SERIALIZED_NAME_PRIVATE_NET = "private_net";
  @SerializedName(SERIALIZED_NAME_PRIVATE_NET)
  private List<ServersGet200ResponseServersInnerPrivateNetInner> privateNet = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROTECTION = "protection";
  @SerializedName(SERIALIZED_NAME_PROTECTION)
  private ServersGet200ResponseServersInnerProtection protection;

  public static final String SERIALIZED_NAME_PUBLIC_NET = "public_net";
  @SerializedName(SERIALIZED_NAME_PUBLIC_NET)
  private ServersGet200ResponseServersInnerPublicNet publicNet;

  public static final String SERIALIZED_NAME_RESCUE_ENABLED = "rescue_enabled";
  @SerializedName(SERIALIZED_NAME_RESCUE_ENABLED)
  private Boolean rescueEnabled;

  public static final String SERIALIZED_NAME_SERVER_TYPE = "server_type";
  @SerializedName(SERIALIZED_NAME_SERVER_TYPE)
  private ServersGet200ResponseServersInnerServerType serverType;

  /**
   * Status of the Server
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    RUNNING("running"),
    
    INITIALIZING("initializing"),
    
    STARTING("starting"),
    
    STOPPING("stopping"),
    
    FALSE("false"),
    
    DELETING("deleting"),
    
    MIGRATING("migrating"),
    
    REBUILDING("rebuilding"),
    
    UNKNOWN("unknown");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_VOLUMES = "volumes";
  @SerializedName(SERIALIZED_NAME_VOLUMES)
  private List<Integer> volumes = new ArrayList<>();

  public ServersGet200ResponseServersInner() {
  }

  public ServersGet200ResponseServersInner backupWindow(String backupWindow) {
    this.backupWindow = backupWindow;
    return this;
  }

  /**
   * Time window (UTC) in which the backup will run, or null if the backups are not enabled
   * @return backupWindow
   */
  @javax.annotation.Nullable
  public String getBackupWindow() {
    return backupWindow;
  }

  public void setBackupWindow(String backupWindow) {
    this.backupWindow = backupWindow;
  }


  public ServersGet200ResponseServersInner created(String created) {
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


  public ServersGet200ResponseServersInner datacenter(ServersGet200ResponseServersInnerDatacenter datacenter) {
    this.datacenter = datacenter;
    return this;
  }

  /**
   * Get datacenter
   * @return datacenter
   */
  @javax.annotation.Nonnull
  public ServersGet200ResponseServersInnerDatacenter getDatacenter() {
    return datacenter;
  }

  public void setDatacenter(ServersGet200ResponseServersInnerDatacenter datacenter) {
    this.datacenter = datacenter;
  }


  public ServersGet200ResponseServersInner id(Integer id) {
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


  public ServersGet200ResponseServersInner image(ServersGet200ResponseServersInnerImage image) {
    this.image = image;
    return this;
  }

  /**
   * Get image
   * @return image
   */
  @javax.annotation.Nullable
  public ServersGet200ResponseServersInnerImage getImage() {
    return image;
  }

  public void setImage(ServersGet200ResponseServersInnerImage image) {
    this.image = image;
  }


  public ServersGet200ResponseServersInner includedTraffic(BigDecimal includedTraffic) {
    this.includedTraffic = includedTraffic;
    return this;
  }

  /**
   * Free Traffic for the current billing period in bytes
   * @return includedTraffic
   */
  @javax.annotation.Nullable
  public BigDecimal getIncludedTraffic() {
    return includedTraffic;
  }

  public void setIncludedTraffic(BigDecimal includedTraffic) {
    this.includedTraffic = includedTraffic;
  }


  public ServersGet200ResponseServersInner ingoingTraffic(BigDecimal ingoingTraffic) {
    this.ingoingTraffic = ingoingTraffic;
    return this;
  }

  /**
   * Inbound Traffic for the current billing period in bytes
   * @return ingoingTraffic
   */
  @javax.annotation.Nullable
  public BigDecimal getIngoingTraffic() {
    return ingoingTraffic;
  }

  public void setIngoingTraffic(BigDecimal ingoingTraffic) {
    this.ingoingTraffic = ingoingTraffic;
  }


  public ServersGet200ResponseServersInner iso(ServersGet200ResponseServersInnerIso iso) {
    this.iso = iso;
    return this;
  }

  /**
   * Get iso
   * @return iso
   */
  @javax.annotation.Nullable
  public ServersGet200ResponseServersInnerIso getIso() {
    return iso;
  }

  public void setIso(ServersGet200ResponseServersInnerIso iso) {
    this.iso = iso;
  }


  public ServersGet200ResponseServersInner labels(Map<String, String> labels) {
    this.labels = labels;
    return this;
  }

  public ServersGet200ResponseServersInner putLabelsItem(String key, String labelsItem) {
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


  public ServersGet200ResponseServersInner loadBalancers(List<Integer> loadBalancers) {
    this.loadBalancers = loadBalancers;
    return this;
  }

  public ServersGet200ResponseServersInner addLoadBalancersItem(Integer loadBalancersItem) {
    if (this.loadBalancers == null) {
      this.loadBalancers = new ArrayList<>();
    }
    this.loadBalancers.add(loadBalancersItem);
    return this;
  }

  /**
   * Get loadBalancers
   * @return loadBalancers
   */
  @javax.annotation.Nullable
  public List<Integer> getLoadBalancers() {
    return loadBalancers;
  }

  public void setLoadBalancers(List<Integer> loadBalancers) {
    this.loadBalancers = loadBalancers;
  }


  public ServersGet200ResponseServersInner locked(Boolean locked) {
    this.locked = locked;
    return this;
  }

  /**
   * True if Server has been locked and is not available to user
   * @return locked
   */
  @javax.annotation.Nonnull
  public Boolean getLocked() {
    return locked;
  }

  public void setLocked(Boolean locked) {
    this.locked = locked;
  }


  public ServersGet200ResponseServersInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the Server (must be unique per Project and a valid hostname as per RFC 1123)
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ServersGet200ResponseServersInner outgoingTraffic(BigDecimal outgoingTraffic) {
    this.outgoingTraffic = outgoingTraffic;
    return this;
  }

  /**
   * Outbound Traffic for the current billing period in bytes
   * @return outgoingTraffic
   */
  @javax.annotation.Nullable
  public BigDecimal getOutgoingTraffic() {
    return outgoingTraffic;
  }

  public void setOutgoingTraffic(BigDecimal outgoingTraffic) {
    this.outgoingTraffic = outgoingTraffic;
  }


  public ServersGet200ResponseServersInner placementGroup(PlacementGroupNullable placementGroup) {
    this.placementGroup = placementGroup;
    return this;
  }

  /**
   * Get placementGroup
   * @return placementGroup
   */
  @javax.annotation.Nullable
  public PlacementGroupNullable getPlacementGroup() {
    return placementGroup;
  }

  public void setPlacementGroup(PlacementGroupNullable placementGroup) {
    this.placementGroup = placementGroup;
  }


  public ServersGet200ResponseServersInner primaryDiskSize(BigDecimal primaryDiskSize) {
    this.primaryDiskSize = primaryDiskSize;
    return this;
  }

  /**
   * Size of the primary Disk
   * @return primaryDiskSize
   */
  @javax.annotation.Nonnull
  public BigDecimal getPrimaryDiskSize() {
    return primaryDiskSize;
  }

  public void setPrimaryDiskSize(BigDecimal primaryDiskSize) {
    this.primaryDiskSize = primaryDiskSize;
  }


  public ServersGet200ResponseServersInner privateNet(List<ServersGet200ResponseServersInnerPrivateNetInner> privateNet) {
    this.privateNet = privateNet;
    return this;
  }

  public ServersGet200ResponseServersInner addPrivateNetItem(ServersGet200ResponseServersInnerPrivateNetInner privateNetItem) {
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
  public List<ServersGet200ResponseServersInnerPrivateNetInner> getPrivateNet() {
    return privateNet;
  }

  public void setPrivateNet(List<ServersGet200ResponseServersInnerPrivateNetInner> privateNet) {
    this.privateNet = privateNet;
  }


  public ServersGet200ResponseServersInner protection(ServersGet200ResponseServersInnerProtection protection) {
    this.protection = protection;
    return this;
  }

  /**
   * Get protection
   * @return protection
   */
  @javax.annotation.Nonnull
  public ServersGet200ResponseServersInnerProtection getProtection() {
    return protection;
  }

  public void setProtection(ServersGet200ResponseServersInnerProtection protection) {
    this.protection = protection;
  }


  public ServersGet200ResponseServersInner publicNet(ServersGet200ResponseServersInnerPublicNet publicNet) {
    this.publicNet = publicNet;
    return this;
  }

  /**
   * Get publicNet
   * @return publicNet
   */
  @javax.annotation.Nonnull
  public ServersGet200ResponseServersInnerPublicNet getPublicNet() {
    return publicNet;
  }

  public void setPublicNet(ServersGet200ResponseServersInnerPublicNet publicNet) {
    this.publicNet = publicNet;
  }


  public ServersGet200ResponseServersInner rescueEnabled(Boolean rescueEnabled) {
    this.rescueEnabled = rescueEnabled;
    return this;
  }

  /**
   * True if rescue mode is enabled. Server will then boot into rescue system on next reboot
   * @return rescueEnabled
   */
  @javax.annotation.Nonnull
  public Boolean getRescueEnabled() {
    return rescueEnabled;
  }

  public void setRescueEnabled(Boolean rescueEnabled) {
    this.rescueEnabled = rescueEnabled;
  }


  public ServersGet200ResponseServersInner serverType(ServersGet200ResponseServersInnerServerType serverType) {
    this.serverType = serverType;
    return this;
  }

  /**
   * Get serverType
   * @return serverType
   */
  @javax.annotation.Nonnull
  public ServersGet200ResponseServersInnerServerType getServerType() {
    return serverType;
  }

  public void setServerType(ServersGet200ResponseServersInnerServerType serverType) {
    this.serverType = serverType;
  }


  public ServersGet200ResponseServersInner status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Status of the Server
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public ServersGet200ResponseServersInner volumes(List<Integer> volumes) {
    this.volumes = volumes;
    return this;
  }

  public ServersGet200ResponseServersInner addVolumesItem(Integer volumesItem) {
    if (this.volumes == null) {
      this.volumes = new ArrayList<>();
    }
    this.volumes.add(volumesItem);
    return this;
  }

  /**
   * IDs of Volumes assigned to this Server
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
    ServersGet200ResponseServersInner serversGet200ResponseServersInner = (ServersGet200ResponseServersInner) o;
    return Objects.equals(this.backupWindow, serversGet200ResponseServersInner.backupWindow) &&
        Objects.equals(this.created, serversGet200ResponseServersInner.created) &&
        Objects.equals(this.datacenter, serversGet200ResponseServersInner.datacenter) &&
        Objects.equals(this.id, serversGet200ResponseServersInner.id) &&
        Objects.equals(this.image, serversGet200ResponseServersInner.image) &&
        Objects.equals(this.includedTraffic, serversGet200ResponseServersInner.includedTraffic) &&
        Objects.equals(this.ingoingTraffic, serversGet200ResponseServersInner.ingoingTraffic) &&
        Objects.equals(this.iso, serversGet200ResponseServersInner.iso) &&
        Objects.equals(this.labels, serversGet200ResponseServersInner.labels) &&
        Objects.equals(this.loadBalancers, serversGet200ResponseServersInner.loadBalancers) &&
        Objects.equals(this.locked, serversGet200ResponseServersInner.locked) &&
        Objects.equals(this.name, serversGet200ResponseServersInner.name) &&
        Objects.equals(this.outgoingTraffic, serversGet200ResponseServersInner.outgoingTraffic) &&
        Objects.equals(this.placementGroup, serversGet200ResponseServersInner.placementGroup) &&
        Objects.equals(this.primaryDiskSize, serversGet200ResponseServersInner.primaryDiskSize) &&
        Objects.equals(this.privateNet, serversGet200ResponseServersInner.privateNet) &&
        Objects.equals(this.protection, serversGet200ResponseServersInner.protection) &&
        Objects.equals(this.publicNet, serversGet200ResponseServersInner.publicNet) &&
        Objects.equals(this.rescueEnabled, serversGet200ResponseServersInner.rescueEnabled) &&
        Objects.equals(this.serverType, serversGet200ResponseServersInner.serverType) &&
        Objects.equals(this.status, serversGet200ResponseServersInner.status) &&
        Objects.equals(this.volumes, serversGet200ResponseServersInner.volumes);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(backupWindow, created, datacenter, id, image, includedTraffic, ingoingTraffic, iso, labels, loadBalancers, locked, name, outgoingTraffic, placementGroup, primaryDiskSize, privateNet, protection, publicNet, rescueEnabled, serverType, status, volumes);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServersGet200ResponseServersInner {\n");
    sb.append("    backupWindow: ").append(toIndentedString(backupWindow)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    datacenter: ").append(toIndentedString(datacenter)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    includedTraffic: ").append(toIndentedString(includedTraffic)).append("\n");
    sb.append("    ingoingTraffic: ").append(toIndentedString(ingoingTraffic)).append("\n");
    sb.append("    iso: ").append(toIndentedString(iso)).append("\n");
    sb.append("    labels: ").append(toIndentedString(labels)).append("\n");
    sb.append("    loadBalancers: ").append(toIndentedString(loadBalancers)).append("\n");
    sb.append("    locked: ").append(toIndentedString(locked)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    outgoingTraffic: ").append(toIndentedString(outgoingTraffic)).append("\n");
    sb.append("    placementGroup: ").append(toIndentedString(placementGroup)).append("\n");
    sb.append("    primaryDiskSize: ").append(toIndentedString(primaryDiskSize)).append("\n");
    sb.append("    privateNet: ").append(toIndentedString(privateNet)).append("\n");
    sb.append("    protection: ").append(toIndentedString(protection)).append("\n");
    sb.append("    publicNet: ").append(toIndentedString(publicNet)).append("\n");
    sb.append("    rescueEnabled: ").append(toIndentedString(rescueEnabled)).append("\n");
    sb.append("    serverType: ").append(toIndentedString(serverType)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("backup_window");
    openapiFields.add("created");
    openapiFields.add("datacenter");
    openapiFields.add("id");
    openapiFields.add("image");
    openapiFields.add("included_traffic");
    openapiFields.add("ingoing_traffic");
    openapiFields.add("iso");
    openapiFields.add("labels");
    openapiFields.add("load_balancers");
    openapiFields.add("locked");
    openapiFields.add("name");
    openapiFields.add("outgoing_traffic");
    openapiFields.add("placement_group");
    openapiFields.add("primary_disk_size");
    openapiFields.add("private_net");
    openapiFields.add("protection");
    openapiFields.add("public_net");
    openapiFields.add("rescue_enabled");
    openapiFields.add("server_type");
    openapiFields.add("status");
    openapiFields.add("volumes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("backup_window");
    openapiRequiredFields.add("created");
    openapiRequiredFields.add("datacenter");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("image");
    openapiRequiredFields.add("included_traffic");
    openapiRequiredFields.add("ingoing_traffic");
    openapiRequiredFields.add("iso");
    openapiRequiredFields.add("labels");
    openapiRequiredFields.add("locked");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("outgoing_traffic");
    openapiRequiredFields.add("primary_disk_size");
    openapiRequiredFields.add("private_net");
    openapiRequiredFields.add("protection");
    openapiRequiredFields.add("public_net");
    openapiRequiredFields.add("rescue_enabled");
    openapiRequiredFields.add("server_type");
    openapiRequiredFields.add("status");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServersGet200ResponseServersInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServersGet200ResponseServersInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServersGet200ResponseServersInner is not found in the empty JSON string", ServersGet200ResponseServersInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServersGet200ResponseServersInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServersGet200ResponseServersInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ServersGet200ResponseServersInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("backup_window") != null && !jsonObj.get("backup_window").isJsonNull()) && !jsonObj.get("backup_window").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `backup_window` to be a primitive type in the JSON string but got `%s`", jsonObj.get("backup_window").toString()));
      }
      if (!jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      // validate the required field `datacenter`
      ServersGet200ResponseServersInnerDatacenter.validateJsonElement(jsonObj.get("datacenter"));
      // validate the required field `image`
      ServersGet200ResponseServersInnerImage.validateJsonElement(jsonObj.get("image"));
      // validate the required field `iso`
      ServersGet200ResponseServersInnerIso.validateJsonElement(jsonObj.get("iso"));
      // ensure the optional json data is an array if present
      if (jsonObj.get("load_balancers") != null && !jsonObj.get("load_balancers").isJsonNull() && !jsonObj.get("load_balancers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `load_balancers` to be an array in the JSON string but got `%s`", jsonObj.get("load_balancers").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `placement_group`
      if (jsonObj.get("placement_group") != null && !jsonObj.get("placement_group").isJsonNull()) {
        PlacementGroupNullable.validateJsonElement(jsonObj.get("placement_group"));
      }
      // ensure the json data is an array
      if (!jsonObj.get("private_net").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `private_net` to be an array in the JSON string but got `%s`", jsonObj.get("private_net").toString()));
      }

      JsonArray jsonArrayprivateNet = jsonObj.getAsJsonArray("private_net");
      // validate the required field `private_net` (array)
      for (int i = 0; i < jsonArrayprivateNet.size(); i++) {
        ServersGet200ResponseServersInnerPrivateNetInner.validateJsonElement(jsonArrayprivateNet.get(i));
      };
      // validate the required field `protection`
      ServersGet200ResponseServersInnerProtection.validateJsonElement(jsonObj.get("protection"));
      // validate the required field `public_net`
      ServersGet200ResponseServersInnerPublicNet.validateJsonElement(jsonObj.get("public_net"));
      // validate the required field `server_type`
      ServersGet200ResponseServersInnerServerType.validateJsonElement(jsonObj.get("server_type"));
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      // ensure the optional json data is an array if present
      if (jsonObj.get("volumes") != null && !jsonObj.get("volumes").isJsonNull() && !jsonObj.get("volumes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `volumes` to be an array in the JSON string but got `%s`", jsonObj.get("volumes").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServersGet200ResponseServersInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServersGet200ResponseServersInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServersGet200ResponseServersInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServersGet200ResponseServersInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ServersGet200ResponseServersInner>() {
           @Override
           public void write(JsonWriter out, ServersGet200ResponseServersInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServersGet200ResponseServersInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServersGet200ResponseServersInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServersGet200ResponseServersInner
   * @throws IOException if the JSON string is invalid with respect to ServersGet200ResponseServersInner
   */
  public static ServersGet200ResponseServersInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServersGet200ResponseServersInner.class);
  }

  /**
   * Convert an instance of ServersGet200ResponseServersInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

