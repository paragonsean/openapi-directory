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
import org.openapitools.client.model.PricingGet200ResponsePricingFloatingIp;
import org.openapitools.client.model.PricingGet200ResponsePricingFloatingIpsInner;
import org.openapitools.client.model.PricingGet200ResponsePricingImage;
import org.openapitools.client.model.PricingGet200ResponsePricingLoadBalancerTypesInner;
import org.openapitools.client.model.PricingGet200ResponsePricingPrimaryIpsInner;
import org.openapitools.client.model.PricingGet200ResponsePricingServerBackup;
import org.openapitools.client.model.PricingGet200ResponsePricingServerTypesInner;
import org.openapitools.client.model.PricingGet200ResponsePricingTraffic;
import org.openapitools.client.model.PricingGet200ResponsePricingVolume;

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
 * PricingGet200ResponsePricing
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:42:41.028370-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PricingGet200ResponsePricing {
  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_FLOATING_IP = "floating_ip";
  @SerializedName(SERIALIZED_NAME_FLOATING_IP)
  private PricingGet200ResponsePricingFloatingIp floatingIp;

  public static final String SERIALIZED_NAME_FLOATING_IPS = "floating_ips";
  @SerializedName(SERIALIZED_NAME_FLOATING_IPS)
  private List<PricingGet200ResponsePricingFloatingIpsInner> floatingIps = new ArrayList<>();

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private PricingGet200ResponsePricingImage image;

  public static final String SERIALIZED_NAME_LOAD_BALANCER_TYPES = "load_balancer_types";
  @SerializedName(SERIALIZED_NAME_LOAD_BALANCER_TYPES)
  private List<PricingGet200ResponsePricingLoadBalancerTypesInner> loadBalancerTypes = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRIMARY_IPS = "primary_ips";
  @SerializedName(SERIALIZED_NAME_PRIMARY_IPS)
  private List<PricingGet200ResponsePricingPrimaryIpsInner> primaryIps = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVER_BACKUP = "server_backup";
  @SerializedName(SERIALIZED_NAME_SERVER_BACKUP)
  private PricingGet200ResponsePricingServerBackup serverBackup;

  public static final String SERIALIZED_NAME_SERVER_TYPES = "server_types";
  @SerializedName(SERIALIZED_NAME_SERVER_TYPES)
  private List<PricingGet200ResponsePricingServerTypesInner> serverTypes = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRAFFIC = "traffic";
  @SerializedName(SERIALIZED_NAME_TRAFFIC)
  private PricingGet200ResponsePricingTraffic traffic;

  public static final String SERIALIZED_NAME_VAT_RATE = "vat_rate";
  @SerializedName(SERIALIZED_NAME_VAT_RATE)
  private String vatRate;

  public static final String SERIALIZED_NAME_VOLUME = "volume";
  @SerializedName(SERIALIZED_NAME_VOLUME)
  private PricingGet200ResponsePricingVolume volume;

  public PricingGet200ResponsePricing() {
  }

  public PricingGet200ResponsePricing currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Currency the returned prices are expressed in, coded according to ISO 4217
   * @return currency
   */
  @javax.annotation.Nonnull
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public PricingGet200ResponsePricing floatingIp(PricingGet200ResponsePricingFloatingIp floatingIp) {
    this.floatingIp = floatingIp;
    return this;
  }

  /**
   * Get floatingIp
   * @return floatingIp
   */
  @javax.annotation.Nonnull
  public PricingGet200ResponsePricingFloatingIp getFloatingIp() {
    return floatingIp;
  }

  public void setFloatingIp(PricingGet200ResponsePricingFloatingIp floatingIp) {
    this.floatingIp = floatingIp;
  }


  public PricingGet200ResponsePricing floatingIps(List<PricingGet200ResponsePricingFloatingIpsInner> floatingIps) {
    this.floatingIps = floatingIps;
    return this;
  }

  public PricingGet200ResponsePricing addFloatingIpsItem(PricingGet200ResponsePricingFloatingIpsInner floatingIpsItem) {
    if (this.floatingIps == null) {
      this.floatingIps = new ArrayList<>();
    }
    this.floatingIps.add(floatingIpsItem);
    return this;
  }

  /**
   * Costs of Floating IPs types per Location and type
   * @return floatingIps
   */
  @javax.annotation.Nonnull
  public List<PricingGet200ResponsePricingFloatingIpsInner> getFloatingIps() {
    return floatingIps;
  }

  public void setFloatingIps(List<PricingGet200ResponsePricingFloatingIpsInner> floatingIps) {
    this.floatingIps = floatingIps;
  }


  public PricingGet200ResponsePricing image(PricingGet200ResponsePricingImage image) {
    this.image = image;
    return this;
  }

  /**
   * Get image
   * @return image
   */
  @javax.annotation.Nonnull
  public PricingGet200ResponsePricingImage getImage() {
    return image;
  }

  public void setImage(PricingGet200ResponsePricingImage image) {
    this.image = image;
  }


  public PricingGet200ResponsePricing loadBalancerTypes(List<PricingGet200ResponsePricingLoadBalancerTypesInner> loadBalancerTypes) {
    this.loadBalancerTypes = loadBalancerTypes;
    return this;
  }

  public PricingGet200ResponsePricing addLoadBalancerTypesItem(PricingGet200ResponsePricingLoadBalancerTypesInner loadBalancerTypesItem) {
    if (this.loadBalancerTypes == null) {
      this.loadBalancerTypes = new ArrayList<>();
    }
    this.loadBalancerTypes.add(loadBalancerTypesItem);
    return this;
  }

  /**
   * Costs of Load Balancer types per Location and type
   * @return loadBalancerTypes
   */
  @javax.annotation.Nonnull
  public List<PricingGet200ResponsePricingLoadBalancerTypesInner> getLoadBalancerTypes() {
    return loadBalancerTypes;
  }

  public void setLoadBalancerTypes(List<PricingGet200ResponsePricingLoadBalancerTypesInner> loadBalancerTypes) {
    this.loadBalancerTypes = loadBalancerTypes;
  }


  public PricingGet200ResponsePricing primaryIps(List<PricingGet200ResponsePricingPrimaryIpsInner> primaryIps) {
    this.primaryIps = primaryIps;
    return this;
  }

  public PricingGet200ResponsePricing addPrimaryIpsItem(PricingGet200ResponsePricingPrimaryIpsInner primaryIpsItem) {
    if (this.primaryIps == null) {
      this.primaryIps = new ArrayList<>();
    }
    this.primaryIps.add(primaryIpsItem);
    return this;
  }

  /**
   * Costs of Primary IPs types per Location
   * @return primaryIps
   */
  @javax.annotation.Nonnull
  public List<PricingGet200ResponsePricingPrimaryIpsInner> getPrimaryIps() {
    return primaryIps;
  }

  public void setPrimaryIps(List<PricingGet200ResponsePricingPrimaryIpsInner> primaryIps) {
    this.primaryIps = primaryIps;
  }


  public PricingGet200ResponsePricing serverBackup(PricingGet200ResponsePricingServerBackup serverBackup) {
    this.serverBackup = serverBackup;
    return this;
  }

  /**
   * Get serverBackup
   * @return serverBackup
   */
  @javax.annotation.Nonnull
  public PricingGet200ResponsePricingServerBackup getServerBackup() {
    return serverBackup;
  }

  public void setServerBackup(PricingGet200ResponsePricingServerBackup serverBackup) {
    this.serverBackup = serverBackup;
  }


  public PricingGet200ResponsePricing serverTypes(List<PricingGet200ResponsePricingServerTypesInner> serverTypes) {
    this.serverTypes = serverTypes;
    return this;
  }

  public PricingGet200ResponsePricing addServerTypesItem(PricingGet200ResponsePricingServerTypesInner serverTypesItem) {
    if (this.serverTypes == null) {
      this.serverTypes = new ArrayList<>();
    }
    this.serverTypes.add(serverTypesItem);
    return this;
  }

  /**
   * Costs of Server types per Location and type
   * @return serverTypes
   */
  @javax.annotation.Nonnull
  public List<PricingGet200ResponsePricingServerTypesInner> getServerTypes() {
    return serverTypes;
  }

  public void setServerTypes(List<PricingGet200ResponsePricingServerTypesInner> serverTypes) {
    this.serverTypes = serverTypes;
  }


  public PricingGet200ResponsePricing traffic(PricingGet200ResponsePricingTraffic traffic) {
    this.traffic = traffic;
    return this;
  }

  /**
   * Get traffic
   * @return traffic
   */
  @javax.annotation.Nonnull
  public PricingGet200ResponsePricingTraffic getTraffic() {
    return traffic;
  }

  public void setTraffic(PricingGet200ResponsePricingTraffic traffic) {
    this.traffic = traffic;
  }


  public PricingGet200ResponsePricing vatRate(String vatRate) {
    this.vatRate = vatRate;
    return this;
  }

  /**
   * The VAT rate used for calculating prices with VAT
   * @return vatRate
   */
  @javax.annotation.Nonnull
  public String getVatRate() {
    return vatRate;
  }

  public void setVatRate(String vatRate) {
    this.vatRate = vatRate;
  }


  public PricingGet200ResponsePricing volume(PricingGet200ResponsePricingVolume volume) {
    this.volume = volume;
    return this;
  }

  /**
   * Get volume
   * @return volume
   */
  @javax.annotation.Nonnull
  public PricingGet200ResponsePricingVolume getVolume() {
    return volume;
  }

  public void setVolume(PricingGet200ResponsePricingVolume volume) {
    this.volume = volume;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PricingGet200ResponsePricing pricingGet200ResponsePricing = (PricingGet200ResponsePricing) o;
    return Objects.equals(this.currency, pricingGet200ResponsePricing.currency) &&
        Objects.equals(this.floatingIp, pricingGet200ResponsePricing.floatingIp) &&
        Objects.equals(this.floatingIps, pricingGet200ResponsePricing.floatingIps) &&
        Objects.equals(this.image, pricingGet200ResponsePricing.image) &&
        Objects.equals(this.loadBalancerTypes, pricingGet200ResponsePricing.loadBalancerTypes) &&
        Objects.equals(this.primaryIps, pricingGet200ResponsePricing.primaryIps) &&
        Objects.equals(this.serverBackup, pricingGet200ResponsePricing.serverBackup) &&
        Objects.equals(this.serverTypes, pricingGet200ResponsePricing.serverTypes) &&
        Objects.equals(this.traffic, pricingGet200ResponsePricing.traffic) &&
        Objects.equals(this.vatRate, pricingGet200ResponsePricing.vatRate) &&
        Objects.equals(this.volume, pricingGet200ResponsePricing.volume);
  }

  @Override
  public int hashCode() {
    return Objects.hash(currency, floatingIp, floatingIps, image, loadBalancerTypes, primaryIps, serverBackup, serverTypes, traffic, vatRate, volume);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PricingGet200ResponsePricing {\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    floatingIp: ").append(toIndentedString(floatingIp)).append("\n");
    sb.append("    floatingIps: ").append(toIndentedString(floatingIps)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    loadBalancerTypes: ").append(toIndentedString(loadBalancerTypes)).append("\n");
    sb.append("    primaryIps: ").append(toIndentedString(primaryIps)).append("\n");
    sb.append("    serverBackup: ").append(toIndentedString(serverBackup)).append("\n");
    sb.append("    serverTypes: ").append(toIndentedString(serverTypes)).append("\n");
    sb.append("    traffic: ").append(toIndentedString(traffic)).append("\n");
    sb.append("    vatRate: ").append(toIndentedString(vatRate)).append("\n");
    sb.append("    volume: ").append(toIndentedString(volume)).append("\n");
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
    openapiFields.add("currency");
    openapiFields.add("floating_ip");
    openapiFields.add("floating_ips");
    openapiFields.add("image");
    openapiFields.add("load_balancer_types");
    openapiFields.add("primary_ips");
    openapiFields.add("server_backup");
    openapiFields.add("server_types");
    openapiFields.add("traffic");
    openapiFields.add("vat_rate");
    openapiFields.add("volume");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("currency");
    openapiRequiredFields.add("floating_ip");
    openapiRequiredFields.add("floating_ips");
    openapiRequiredFields.add("image");
    openapiRequiredFields.add("load_balancer_types");
    openapiRequiredFields.add("primary_ips");
    openapiRequiredFields.add("server_backup");
    openapiRequiredFields.add("server_types");
    openapiRequiredFields.add("traffic");
    openapiRequiredFields.add("vat_rate");
    openapiRequiredFields.add("volume");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PricingGet200ResponsePricing
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PricingGet200ResponsePricing.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PricingGet200ResponsePricing is not found in the empty JSON string", PricingGet200ResponsePricing.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PricingGet200ResponsePricing.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PricingGet200ResponsePricing` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PricingGet200ResponsePricing.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      // validate the required field `floating_ip`
      PricingGet200ResponsePricingFloatingIp.validateJsonElement(jsonObj.get("floating_ip"));
      // ensure the json data is an array
      if (!jsonObj.get("floating_ips").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `floating_ips` to be an array in the JSON string but got `%s`", jsonObj.get("floating_ips").toString()));
      }

      JsonArray jsonArrayfloatingIps = jsonObj.getAsJsonArray("floating_ips");
      // validate the required field `floating_ips` (array)
      for (int i = 0; i < jsonArrayfloatingIps.size(); i++) {
        PricingGet200ResponsePricingFloatingIpsInner.validateJsonElement(jsonArrayfloatingIps.get(i));
      };
      // validate the required field `image`
      PricingGet200ResponsePricingImage.validateJsonElement(jsonObj.get("image"));
      // ensure the json data is an array
      if (!jsonObj.get("load_balancer_types").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `load_balancer_types` to be an array in the JSON string but got `%s`", jsonObj.get("load_balancer_types").toString()));
      }

      JsonArray jsonArrayloadBalancerTypes = jsonObj.getAsJsonArray("load_balancer_types");
      // validate the required field `load_balancer_types` (array)
      for (int i = 0; i < jsonArrayloadBalancerTypes.size(); i++) {
        PricingGet200ResponsePricingLoadBalancerTypesInner.validateJsonElement(jsonArrayloadBalancerTypes.get(i));
      };
      // ensure the json data is an array
      if (!jsonObj.get("primary_ips").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `primary_ips` to be an array in the JSON string but got `%s`", jsonObj.get("primary_ips").toString()));
      }

      JsonArray jsonArrayprimaryIps = jsonObj.getAsJsonArray("primary_ips");
      // validate the required field `primary_ips` (array)
      for (int i = 0; i < jsonArrayprimaryIps.size(); i++) {
        PricingGet200ResponsePricingPrimaryIpsInner.validateJsonElement(jsonArrayprimaryIps.get(i));
      };
      // validate the required field `server_backup`
      PricingGet200ResponsePricingServerBackup.validateJsonElement(jsonObj.get("server_backup"));
      // ensure the json data is an array
      if (!jsonObj.get("server_types").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `server_types` to be an array in the JSON string but got `%s`", jsonObj.get("server_types").toString()));
      }

      JsonArray jsonArrayserverTypes = jsonObj.getAsJsonArray("server_types");
      // validate the required field `server_types` (array)
      for (int i = 0; i < jsonArrayserverTypes.size(); i++) {
        PricingGet200ResponsePricingServerTypesInner.validateJsonElement(jsonArrayserverTypes.get(i));
      };
      // validate the required field `traffic`
      PricingGet200ResponsePricingTraffic.validateJsonElement(jsonObj.get("traffic"));
      if (!jsonObj.get("vat_rate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vat_rate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vat_rate").toString()));
      }
      // validate the required field `volume`
      PricingGet200ResponsePricingVolume.validateJsonElement(jsonObj.get("volume"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PricingGet200ResponsePricing.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PricingGet200ResponsePricing' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PricingGet200ResponsePricing> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PricingGet200ResponsePricing.class));

       return (TypeAdapter<T>) new TypeAdapter<PricingGet200ResponsePricing>() {
           @Override
           public void write(JsonWriter out, PricingGet200ResponsePricing value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PricingGet200ResponsePricing read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PricingGet200ResponsePricing given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PricingGet200ResponsePricing
   * @throws IOException if the JSON string is invalid with respect to PricingGet200ResponsePricing
   */
  public static PricingGet200ResponsePricing fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PricingGet200ResponsePricing.class);
  }

  /**
   * Convert an instance of PricingGet200ResponsePricing to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

