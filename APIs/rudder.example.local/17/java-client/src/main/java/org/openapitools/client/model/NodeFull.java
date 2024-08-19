/*
 * Rudder API
 * Download OpenAPI specification: [openapi.yml](openapi.yml)  # Introduction  Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.  ## Versioning  Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or `latest`.  You can change the version of the API used by setting it either within the url or in a header:  * the URL: each URL is prefixed by its version id, like `/api/version/function`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/10/rules # Latest curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules # Wrong (not an integer) => 404 not found curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/3.14/rules ```  * the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or `latest`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 10\" https://rudder.example.com/rudder/api/rules # Wrong => Error response indicating which versions are available curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 3.14\" https://rudder.example.com/rudder/api/rules ```  In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe period of time to allow migration from previous versions.   <h4>Existing versions</h4> <table>   <thead>     <tr>       <th style=\"width: 20%\">Version</th>       <th style=\"width: 20%\">Rudder versions it appeared in</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">1</td>       <td class=\"code\">Never released (for internal use only)</td>       <td>Experimental version</td>     </tr>     <tr>       <td class=\"code\">2 to 10 (deprecated)</td>       <td class=\"code\">4.3 and before</td>       <td>These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API</td>     </tr>     <tr>       <td class=\"code\">11</td>       <td class=\"code\">5.0</td>       <td>New system API (replacing old localhost v1 api): status, maintenance operations and server behavior</td>     </tr>     <tr>       <td class=\"code\">12</td>       <td class=\"code\">6.0 and 6.1</td>       <td>Node key management</td>     </tr>     <tr>       <td class=\"code\">13</td>       <td class=\"code\">6.2</td>       <td><ul>         <li>Node status endpoint</li>         <li>System health check</li>         <li>System maintenance job to purge software [that endpoint was back-ported in 6.1]</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">14</td>       <td class=\"code\">7.0</td>       <td><ul>         <li>Secret management</li>         <li>Directive tree</li>         <li>Improve techniques management</li>         <li>Demote a relay</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">15</td>       <td class=\"code\">7.1</td>       <td><ul>         <li>Package updates in nodes</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">16</td>       <td class=\"code\">7.2</td>       <td><ul>         <li>Create node API included from plugin</li>         <li>Configuration archive import/export</li>       </ul></td>     </tr>   </tbody> </table>   ## Response format  All responses from the API are in the JSON format.  ```json {   \"action\": \"The name of the called function\",   \"id\": \"The ID of the element you want, if relevant\",   \"result\": \"The result of your action: success or error\",   \"data\": \"Only present if this is a success and depends on the function, it's usually a JSON object\",   \"errorDetails\": \"Only present if this is an error, it contains the error message\" } ```   * __Success__ responses are sent with the 200 HTTP (Success) code  * __Error__ responses are sent with a HTTP error code (mostly 5xx...)   ## HTTP method  Rudder's REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:   * **GET**: search or retrieve information (get rule details, get a group, ...)  * **PUT**: add new objects (create a directive, clone a Rule, ...)  * **DELETE**: remove objects (delete a node, delete a parameter, ...)  * **POST**: update existing objects (update a directive, reload a group, ...)   ## Parameters  ### General parameters  Some parameters are available for almost all API functions. They will be described in this section. They must be part of the query and can't be submitted in a JSON form.  #### Available for all requests  <table>   <thead>     <tr>       <th style=\"width: 30%\">Field</th>       <th style=\"width: 10%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">prettify</td>       <td><b>boolean</b><br><i>optional</i></td>       <td>         Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.         <p class=\"default-value\">Default value: <code>false</code></p>       </td>     </tr>   </tbody> </table>   #### Available for modification requests (PUT/POST/DELETE)  <table>   <thead>     <tr>       <th style=\"width: 25%\">Field</th>       <th style=\"width: 12%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">reason</td>       <td><b>string</b><br><i>optional</i> or <i>required</i></td>       <td>         Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestName</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request name, is used only if workflows are enabled. The default value depends on the function called         <p class=\"default-value\">Default value: <code>A default string for each function</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestDescription</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request description, is used only if workflows are enabled.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>   </tbody> </table>   ### Passing parameters  Parameters to the API can be sent:  * As part of the URL for resource identification  * As data for POST/PUT requests    * Directly in JSON format    * As request arguments  #### As part of the URL for resource identification  Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.  ```bash # Get the Rule of ID \"id\" curl -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules/id ```    CAUTION: To avoid surprising behavior, do not put a '/' at the end of an URL: it would be interpreted as '/[empty string parameter]' and redirected to '/index', likely not what you wanted to do.   #### Sending data for POST/PUT requests  ##### Directly in JSON format  JSON format is the preferred way to interact with Rudder API for creating or updating resources. You'll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored). In a `curl` `POST` request, that header can be provided with the `-H` parameter:  ```bash curl -X POST -H \"Content-Type: application/json\" ... ```  The supplied file must contain a valid JSON: strings need quotes, booleans and integers don't, etc.  The (human readable) format is:  ```json {   \"key1\": \"value1\",   \"key2\": false,   \"key3\": 42 } ```   Here is an example with inlined data:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H  \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id}   -d '{ \"displayName\": \"new name\", \"enabled\": false, \"directives\": \"directiveId\"}' ```  You can also pass a supply the JSON in a file:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam ```  Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can't mix JSON and request parameters):  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive with reason message \"Reason used\" curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" \"https://rudder.example.com/rudder/api/rules/latest/{id}?reason=Reason used\" -d @jsonParam -d \"reason=Reason ignored\" ```  ##### Request parameters  In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use request parameters. You will need to pass one parameter for each data you want to change.  Parameters follow the following schema:  ``` key=value ```  You can pass parameters by two means:  * As query parameters: At the end of your url, put a **?** then your first parameter and then a **&** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\"  https://rudder.example.com/rudder/api/rules/latest/{id}?\"displayName=my new name\"&\"enabled=false\"&\"directives=aDirectiveId\" ```  * As request data: You can pass those parameters in the request data, they won't figure in the URL, making it lighter to read, You can pass a file that contains data.  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive (in file directive-info.json) curl -X POST -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/rules/latest/{id} -d \"displayName=my new name\" -d \"enabled=false\" -d @directive-info.json ``` 
 *
 * The version of the OpenAPI document: 17
 * Contact: dev@rudder.io
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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.NodeAddInnerPropertiesInner;
import org.openapitools.client.model.NodeFullBios;
import org.openapitools.client.model.NodeFullControllersInner;
import org.openapitools.client.model.NodeFullEnvironmentVariablesInner;
import org.openapitools.client.model.NodeFullFileSystemsInner;
import org.openapitools.client.model.NodeFullMachine;
import org.openapitools.client.model.NodeFullManagementTechnologyDetails;
import org.openapitools.client.model.NodeFullManagementTechnologyInner;
import org.openapitools.client.model.NodeFullMemoriesInner;
import org.openapitools.client.model.NodeFullNetworkInterfacesInner;
import org.openapitools.client.model.NodeFullOs;
import org.openapitools.client.model.NodeFullPortsInner;
import org.openapitools.client.model.NodeFullProcessesInner;
import org.openapitools.client.model.NodeFullProcessorsInner;
import org.openapitools.client.model.NodeFullSlotsInner;
import org.openapitools.client.model.NodeFullSoftwareInner;
import org.openapitools.client.model.NodeFullSoftwareUpdateInner;
import org.openapitools.client.model.NodeFullSoundInner;
import org.openapitools.client.model.NodeFullStorageInner;
import org.openapitools.client.model.NodeFullTimezone;
import org.openapitools.client.model.NodeFullVideosInner;
import org.openapitools.client.model.NodeFullVirtualMachinesInner;

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
 * NodeFull
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:58.781092-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NodeFull {
  public static final String SERIALIZED_NAME_ACCOUNTS = "accounts";
  @SerializedName(SERIALIZED_NAME_ACCOUNTS)
  private List<String> accounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_ARCHITECTURE_DESCRIPTION = "architectureDescription";
  @SerializedName(SERIALIZED_NAME_ARCHITECTURE_DESCRIPTION)
  private String architectureDescription;

  public static final String SERIALIZED_NAME_BIOS = "bios";
  @SerializedName(SERIALIZED_NAME_BIOS)
  private NodeFullBios bios;

  public static final String SERIALIZED_NAME_CONTROLLERS = "controllers";
  @SerializedName(SERIALIZED_NAME_CONTROLLERS)
  private List<NodeFullControllersInner> controllers = new ArrayList<>();

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ENVIRONMENT_VARIABLES = "environmentVariables";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_VARIABLES)
  private List<NodeFullEnvironmentVariablesInner> environmentVariables = new ArrayList<>();

  public static final String SERIALIZED_NAME_FILE_SYSTEMS = "fileSystems";
  @SerializedName(SERIALIZED_NAME_FILE_SYSTEMS)
  private List<NodeFullFileSystemsInner> fileSystems = new ArrayList<>();

  public static final String SERIALIZED_NAME_HOSTNAME = "hostname";
  @SerializedName(SERIALIZED_NAME_HOSTNAME)
  private String hostname;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IP_ADDRESSES = "ipAddresses";
  @SerializedName(SERIALIZED_NAME_IP_ADDRESSES)
  private List<String> ipAddresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_LAST_INVENTORY_DATE = "lastInventoryDate";
  @SerializedName(SERIALIZED_NAME_LAST_INVENTORY_DATE)
  private LocalDate lastInventoryDate;

  public static final String SERIALIZED_NAME_LAST_RUN_DATE = "lastRunDate";
  @SerializedName(SERIALIZED_NAME_LAST_RUN_DATE)
  private LocalDate lastRunDate;

  public static final String SERIALIZED_NAME_MACHINE = "machine";
  @SerializedName(SERIALIZED_NAME_MACHINE)
  private NodeFullMachine machine;

  public static final String SERIALIZED_NAME_MANAGEMENT_TECHNOLOGY = "managementTechnology";
  @SerializedName(SERIALIZED_NAME_MANAGEMENT_TECHNOLOGY)
  private List<NodeFullManagementTechnologyInner> managementTechnology = new ArrayList<>();

  public static final String SERIALIZED_NAME_MANAGEMENT_TECHNOLOGY_DETAILS = "managementTechnologyDetails";
  @SerializedName(SERIALIZED_NAME_MANAGEMENT_TECHNOLOGY_DETAILS)
  private NodeFullManagementTechnologyDetails managementTechnologyDetails;

  public static final String SERIALIZED_NAME_MEMORIES = "memories";
  @SerializedName(SERIALIZED_NAME_MEMORIES)
  private List<NodeFullMemoriesInner> memories = new ArrayList<>();

  public static final String SERIALIZED_NAME_NETWORK_INTERFACES = "networkInterfaces";
  @SerializedName(SERIALIZED_NAME_NETWORK_INTERFACES)
  private List<NodeFullNetworkInterfacesInner> networkInterfaces = new ArrayList<>();

  public static final String SERIALIZED_NAME_OS = "os";
  @SerializedName(SERIALIZED_NAME_OS)
  private NodeFullOs os;

  /**
   * Rudder policy mode for the node (&#x60;default&#x60; follows the global configuration)
   */
  @JsonAdapter(PolicyModeEnum.Adapter.class)
  public enum PolicyModeEnum {
    ENFORCE("enforce"),
    
    AUDIT("audit"),
    
    DEFAULT("default");

    private String value;

    PolicyModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PolicyModeEnum fromValue(String value) {
      for (PolicyModeEnum b : PolicyModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PolicyModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PolicyModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PolicyModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PolicyModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PolicyModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_POLICY_MODE = "policyMode";
  @SerializedName(SERIALIZED_NAME_POLICY_MODE)
  private PolicyModeEnum policyMode;

  public static final String SERIALIZED_NAME_POLICY_SERVER_ID = "policyServerId";
  @SerializedName(SERIALIZED_NAME_POLICY_SERVER_ID)
  private String policyServerId;

  public static final String SERIALIZED_NAME_PORTS = "ports";
  @SerializedName(SERIALIZED_NAME_PORTS)
  private List<NodeFullPortsInner> ports = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROCESSES = "processes";
  @SerializedName(SERIALIZED_NAME_PROCESSES)
  private List<NodeFullProcessesInner> processes = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROCESSORS = "processors";
  @SerializedName(SERIALIZED_NAME_PROCESSORS)
  private List<NodeFullProcessorsInner> processors = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private List<NodeAddInnerPropertiesInner> properties = new ArrayList<>();

  public static final String SERIALIZED_NAME_RAM = "ram";
  @SerializedName(SERIALIZED_NAME_RAM)
  private Integer ram;

  public static final String SERIALIZED_NAME_SLOTS = "slots";
  @SerializedName(SERIALIZED_NAME_SLOTS)
  private List<NodeFullSlotsInner> slots = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOFTWARE = "software";
  @SerializedName(SERIALIZED_NAME_SOFTWARE)
  private List<NodeFullSoftwareInner> software = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOFTWARE_UPDATE = "softwareUpdate";
  @SerializedName(SERIALIZED_NAME_SOFTWARE_UPDATE)
  private List<NodeFullSoftwareUpdateInner> softwareUpdate = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOUND = "sound";
  @SerializedName(SERIALIZED_NAME_SOUND)
  private List<NodeFullSoundInner> sound = new ArrayList<>();

  /**
   * Status of the node
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    PENDING("pending"),
    
    ACCEPTED("accepted"),
    
    DELETED("deleted");

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

  public static final String SERIALIZED_NAME_STORAGE = "storage";
  @SerializedName(SERIALIZED_NAME_STORAGE)
  private List<NodeFullStorageInner> storage = new ArrayList<>();

  public static final String SERIALIZED_NAME_TIMEZONE = "timezone";
  @SerializedName(SERIALIZED_NAME_TIMEZONE)
  private NodeFullTimezone timezone;

  public static final String SERIALIZED_NAME_VIDEOS = "videos";
  @SerializedName(SERIALIZED_NAME_VIDEOS)
  private List<NodeFullVideosInner> videos = new ArrayList<>();

  public static final String SERIALIZED_NAME_VIRTUAL_MACHINES = "virtualMachines";
  @SerializedName(SERIALIZED_NAME_VIRTUAL_MACHINES)
  private List<NodeFullVirtualMachinesInner> virtualMachines = new ArrayList<>();

  public NodeFull() {
  }

  public NodeFull accounts(List<String> accounts) {
    this.accounts = accounts;
    return this;
  }

  public NodeFull addAccountsItem(String accountsItem) {
    if (this.accounts == null) {
      this.accounts = new ArrayList<>();
    }
    this.accounts.add(accountsItem);
    return this;
  }

  /**
   * User accounts declared in the node
   * @return accounts
   */
  @javax.annotation.Nullable
  public List<String> getAccounts() {
    return accounts;
  }

  public void setAccounts(List<String> accounts) {
    this.accounts = accounts;
  }


  public NodeFull architectureDescription(String architectureDescription) {
    this.architectureDescription = architectureDescription;
    return this;
  }

  /**
   * Information about CPU architecture (32/64 bits)
   * @return architectureDescription
   */
  @javax.annotation.Nullable
  public String getArchitectureDescription() {
    return architectureDescription;
  }

  public void setArchitectureDescription(String architectureDescription) {
    this.architectureDescription = architectureDescription;
  }


  public NodeFull bios(NodeFullBios bios) {
    this.bios = bios;
    return this;
  }

  /**
   * Get bios
   * @return bios
   */
  @javax.annotation.Nullable
  public NodeFullBios getBios() {
    return bios;
  }

  public void setBios(NodeFullBios bios) {
    this.bios = bios;
  }


  public NodeFull controllers(List<NodeFullControllersInner> controllers) {
    this.controllers = controllers;
    return this;
  }

  public NodeFull addControllersItem(NodeFullControllersInner controllersItem) {
    if (this.controllers == null) {
      this.controllers = new ArrayList<>();
    }
    this.controllers.add(controllersItem);
    return this;
  }

  /**
   * Physical controller information
   * @return controllers
   */
  @javax.annotation.Nullable
  public List<NodeFullControllersInner> getControllers() {
    return controllers;
  }

  public void setControllers(List<NodeFullControllersInner> controllers) {
    this.controllers = controllers;
  }


  public NodeFull description(String description) {
    this.description = description;
    return this;
  }

  /**
   * A human intended description of the node (not used)
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public NodeFull environmentVariables(List<NodeFullEnvironmentVariablesInner> environmentVariables) {
    this.environmentVariables = environmentVariables;
    return this;
  }

  public NodeFull addEnvironmentVariablesItem(NodeFullEnvironmentVariablesInner environmentVariablesItem) {
    if (this.environmentVariables == null) {
      this.environmentVariables = new ArrayList<>();
    }
    this.environmentVariables.add(environmentVariablesItem);
    return this;
  }

  /**
   * Environment variables defined on the node in the context of the agent
   * @return environmentVariables
   */
  @javax.annotation.Nullable
  public List<NodeFullEnvironmentVariablesInner> getEnvironmentVariables() {
    return environmentVariables;
  }

  public void setEnvironmentVariables(List<NodeFullEnvironmentVariablesInner> environmentVariables) {
    this.environmentVariables = environmentVariables;
  }


  public NodeFull fileSystems(List<NodeFullFileSystemsInner> fileSystems) {
    this.fileSystems = fileSystems;
    return this;
  }

  public NodeFull addFileSystemsItem(NodeFullFileSystemsInner fileSystemsItem) {
    if (this.fileSystems == null) {
      this.fileSystems = new ArrayList<>();
    }
    this.fileSystems.add(fileSystemsItem);
    return this;
  }

  /**
   * File system declared on the node
   * @return fileSystems
   */
  @javax.annotation.Nullable
  public List<NodeFullFileSystemsInner> getFileSystems() {
    return fileSystems;
  }

  public void setFileSystems(List<NodeFullFileSystemsInner> fileSystems) {
    this.fileSystems = fileSystems;
  }


  public NodeFull hostname(String hostname) {
    this.hostname = hostname;
    return this;
  }

  /**
   * Fully qualified name of the node
   * @return hostname
   */
  @javax.annotation.Nonnull
  public String getHostname() {
    return hostname;
  }

  public void setHostname(String hostname) {
    this.hostname = hostname;
  }


  public NodeFull id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Unique id of the node
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public NodeFull ipAddresses(List<String> ipAddresses) {
    this.ipAddresses = ipAddresses;
    return this;
  }

  public NodeFull addIpAddressesItem(String ipAddressesItem) {
    if (this.ipAddresses == null) {
      this.ipAddresses = new ArrayList<>();
    }
    this.ipAddresses.add(ipAddressesItem);
    return this;
  }

  /**
   * IP addresses of the node (IPv4 and IPv6)
   * @return ipAddresses
   */
  @javax.annotation.Nonnull
  public List<String> getIpAddresses() {
    return ipAddresses;
  }

  public void setIpAddresses(List<String> ipAddresses) {
    this.ipAddresses = ipAddresses;
  }


  public NodeFull lastInventoryDate(LocalDate lastInventoryDate) {
    this.lastInventoryDate = lastInventoryDate;
    return this;
  }

  /**
   * Date and time of the latest generated inventory, if one is available (node time). Up to API v11, format was: \&quot;YYYY-MM-dd HH:mm\&quot;
   * @return lastInventoryDate
   */
  @javax.annotation.Nullable
  public LocalDate getLastInventoryDate() {
    return lastInventoryDate;
  }

  public void setLastInventoryDate(LocalDate lastInventoryDate) {
    this.lastInventoryDate = lastInventoryDate;
  }


  public NodeFull lastRunDate(LocalDate lastRunDate) {
    this.lastRunDate = lastRunDate;
    return this;
  }

  /**
   * Date and time of the latest run, if one is available (node time). Up to API v11, format was: \&quot;YYYY-MM-dd HH:mm\&quot;
   * @return lastRunDate
   */
  @javax.annotation.Nullable
  public LocalDate getLastRunDate() {
    return lastRunDate;
  }

  public void setLastRunDate(LocalDate lastRunDate) {
    this.lastRunDate = lastRunDate;
  }


  public NodeFull machine(NodeFullMachine machine) {
    this.machine = machine;
    return this;
  }

  /**
   * Get machine
   * @return machine
   */
  @javax.annotation.Nullable
  public NodeFullMachine getMachine() {
    return machine;
  }

  public void setMachine(NodeFullMachine machine) {
    this.machine = machine;
  }


  public NodeFull managementTechnology(List<NodeFullManagementTechnologyInner> managementTechnology) {
    this.managementTechnology = managementTechnology;
    return this;
  }

  public NodeFull addManagementTechnologyItem(NodeFullManagementTechnologyInner managementTechnologyItem) {
    if (this.managementTechnology == null) {
      this.managementTechnology = new ArrayList<>();
    }
    this.managementTechnology.add(managementTechnologyItem);
    return this;
  }

  /**
   * Management agents running on the node
   * @return managementTechnology
   */
  @javax.annotation.Nonnull
  public List<NodeFullManagementTechnologyInner> getManagementTechnology() {
    return managementTechnology;
  }

  public void setManagementTechnology(List<NodeFullManagementTechnologyInner> managementTechnology) {
    this.managementTechnology = managementTechnology;
  }


  public NodeFull managementTechnologyDetails(NodeFullManagementTechnologyDetails managementTechnologyDetails) {
    this.managementTechnologyDetails = managementTechnologyDetails;
    return this;
  }

  /**
   * Get managementTechnologyDetails
   * @return managementTechnologyDetails
   */
  @javax.annotation.Nullable
  public NodeFullManagementTechnologyDetails getManagementTechnologyDetails() {
    return managementTechnologyDetails;
  }

  public void setManagementTechnologyDetails(NodeFullManagementTechnologyDetails managementTechnologyDetails) {
    this.managementTechnologyDetails = managementTechnologyDetails;
  }


  public NodeFull memories(List<NodeFullMemoriesInner> memories) {
    this.memories = memories;
    return this;
  }

  public NodeFull addMemoriesItem(NodeFullMemoriesInner memoriesItem) {
    if (this.memories == null) {
      this.memories = new ArrayList<>();
    }
    this.memories.add(memoriesItem);
    return this;
  }

  /**
   * Memory slots
   * @return memories
   */
  @javax.annotation.Nullable
  public List<NodeFullMemoriesInner> getMemories() {
    return memories;
  }

  public void setMemories(List<NodeFullMemoriesInner> memories) {
    this.memories = memories;
  }


  public NodeFull networkInterfaces(List<NodeFullNetworkInterfacesInner> networkInterfaces) {
    this.networkInterfaces = networkInterfaces;
    return this;
  }

  public NodeFull addNetworkInterfacesItem(NodeFullNetworkInterfacesInner networkInterfacesItem) {
    if (this.networkInterfaces == null) {
      this.networkInterfaces = new ArrayList<>();
    }
    this.networkInterfaces.add(networkInterfacesItem);
    return this;
  }

  /**
   * Detailed information about registered network interfaces on the node
   * @return networkInterfaces
   */
  @javax.annotation.Nullable
  public List<NodeFullNetworkInterfacesInner> getNetworkInterfaces() {
    return networkInterfaces;
  }

  public void setNetworkInterfaces(List<NodeFullNetworkInterfacesInner> networkInterfaces) {
    this.networkInterfaces = networkInterfaces;
  }


  public NodeFull os(NodeFullOs os) {
    this.os = os;
    return this;
  }

  /**
   * Get os
   * @return os
   */
  @javax.annotation.Nullable
  public NodeFullOs getOs() {
    return os;
  }

  public void setOs(NodeFullOs os) {
    this.os = os;
  }


  public NodeFull policyMode(PolicyModeEnum policyMode) {
    this.policyMode = policyMode;
    return this;
  }

  /**
   * Rudder policy mode for the node (&#x60;default&#x60; follows the global configuration)
   * @return policyMode
   */
  @javax.annotation.Nullable
  public PolicyModeEnum getPolicyMode() {
    return policyMode;
  }

  public void setPolicyMode(PolicyModeEnum policyMode) {
    this.policyMode = policyMode;
  }


  public NodeFull policyServerId(String policyServerId) {
    this.policyServerId = policyServerId;
    return this;
  }

  /**
   * Rudder policy server managing the node
   * @return policyServerId
   */
  @javax.annotation.Nonnull
  public String getPolicyServerId() {
    return policyServerId;
  }

  public void setPolicyServerId(String policyServerId) {
    this.policyServerId = policyServerId;
  }


  public NodeFull ports(List<NodeFullPortsInner> ports) {
    this.ports = ports;
    return this;
  }

  public NodeFull addPortsItem(NodeFullPortsInner portsItem) {
    if (this.ports == null) {
      this.ports = new ArrayList<>();
    }
    this.ports.add(portsItem);
    return this;
  }

  /**
   * Physical port information objects
   * @return ports
   */
  @javax.annotation.Nullable
  public List<NodeFullPortsInner> getPorts() {
    return ports;
  }

  public void setPorts(List<NodeFullPortsInner> ports) {
    this.ports = ports;
  }


  public NodeFull processes(List<NodeFullProcessesInner> processes) {
    this.processes = processes;
    return this;
  }

  public NodeFull addProcessesItem(NodeFullProcessesInner processesItem) {
    if (this.processes == null) {
      this.processes = new ArrayList<>();
    }
    this.processes.add(processesItem);
    return this;
  }

  /**
   * Process running (at inventory time)
   * @return processes
   */
  @javax.annotation.Nullable
  public List<NodeFullProcessesInner> getProcesses() {
    return processes;
  }

  public void setProcesses(List<NodeFullProcessesInner> processes) {
    this.processes = processes;
  }


  public NodeFull processors(List<NodeFullProcessorsInner> processors) {
    this.processors = processors;
    return this;
  }

  public NodeFull addProcessorsItem(NodeFullProcessorsInner processorsItem) {
    if (this.processors == null) {
      this.processors = new ArrayList<>();
    }
    this.processors.add(processorsItem);
    return this;
  }

  /**
   * CPU information
   * @return processors
   */
  @javax.annotation.Nullable
  public List<NodeFullProcessorsInner> getProcessors() {
    return processors;
  }

  public void setProcessors(List<NodeFullProcessorsInner> processors) {
    this.processors = processors;
  }


  public NodeFull properties(List<NodeAddInnerPropertiesInner> properties) {
    this.properties = properties;
    return this;
  }

  public NodeFull addPropertiesItem(NodeAddInnerPropertiesInner propertiesItem) {
    if (this.properties == null) {
      this.properties = new ArrayList<>();
    }
    this.properties.add(propertiesItem);
    return this;
  }

  /**
   * Node properties (either set by user or filled by third party sources)
   * @return properties
   */
  @javax.annotation.Nonnull
  public List<NodeAddInnerPropertiesInner> getProperties() {
    return properties;
  }

  public void setProperties(List<NodeAddInnerPropertiesInner> properties) {
    this.properties = properties;
  }


  public NodeFull ram(Integer ram) {
    this.ram = ram;
    return this;
  }

  /**
   * Size of RAM in MB
   * @return ram
   */
  @javax.annotation.Nullable
  public Integer getRam() {
    return ram;
  }

  public void setRam(Integer ram) {
    this.ram = ram;
  }


  public NodeFull slots(List<NodeFullSlotsInner> slots) {
    this.slots = slots;
    return this;
  }

  public NodeFull addSlotsItem(NodeFullSlotsInner slotsItem) {
    if (this.slots == null) {
      this.slots = new ArrayList<>();
    }
    this.slots.add(slotsItem);
    return this;
  }

  /**
   * Physical extension slot information
   * @return slots
   */
  @javax.annotation.Nullable
  public List<NodeFullSlotsInner> getSlots() {
    return slots;
  }

  public void setSlots(List<NodeFullSlotsInner> slots) {
    this.slots = slots;
  }


  public NodeFull software(List<NodeFullSoftwareInner> software) {
    this.software = software;
    return this;
  }

  public NodeFull addSoftwareItem(NodeFullSoftwareInner softwareItem) {
    if (this.software == null) {
      this.software = new ArrayList<>();
    }
    this.software.add(softwareItem);
    return this;
  }

  /**
   * Software installed on the node (can have thousands items)
   * @return software
   */
  @javax.annotation.Nullable
  public List<NodeFullSoftwareInner> getSoftware() {
    return software;
  }

  public void setSoftware(List<NodeFullSoftwareInner> software) {
    this.software = software;
  }


  public NodeFull softwareUpdate(List<NodeFullSoftwareUpdateInner> softwareUpdate) {
    this.softwareUpdate = softwareUpdate;
    return this;
  }

  public NodeFull addSoftwareUpdateItem(NodeFullSoftwareUpdateInner softwareUpdateItem) {
    if (this.softwareUpdate == null) {
      this.softwareUpdate = new ArrayList<>();
    }
    this.softwareUpdate.add(softwareUpdateItem);
    return this;
  }

  /**
   * Software that can be updated on that machine
   * @return softwareUpdate
   */
  @javax.annotation.Nullable
  public List<NodeFullSoftwareUpdateInner> getSoftwareUpdate() {
    return softwareUpdate;
  }

  public void setSoftwareUpdate(List<NodeFullSoftwareUpdateInner> softwareUpdate) {
    this.softwareUpdate = softwareUpdate;
  }


  public NodeFull sound(List<NodeFullSoundInner> sound) {
    this.sound = sound;
    return this;
  }

  public NodeFull addSoundItem(NodeFullSoundInner soundItem) {
    if (this.sound == null) {
      this.sound = new ArrayList<>();
    }
    this.sound.add(soundItem);
    return this;
  }

  /**
   * Sound card information
   * @return sound
   */
  @javax.annotation.Nullable
  public List<NodeFullSoundInner> getSound() {
    return sound;
  }

  public void setSound(List<NodeFullSoundInner> sound) {
    this.sound = sound;
  }


  public NodeFull status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Status of the node
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public NodeFull storage(List<NodeFullStorageInner> storage) {
    this.storage = storage;
    return this;
  }

  public NodeFull addStorageItem(NodeFullStorageInner storageItem) {
    if (this.storage == null) {
      this.storage = new ArrayList<>();
    }
    this.storage.add(storageItem);
    return this;
  }

  /**
   * Storage (disks) information objects
   * @return storage
   */
  @javax.annotation.Nullable
  public List<NodeFullStorageInner> getStorage() {
    return storage;
  }

  public void setStorage(List<NodeFullStorageInner> storage) {
    this.storage = storage;
  }


  public NodeFull timezone(NodeFullTimezone timezone) {
    this.timezone = timezone;
    return this;
  }

  /**
   * Get timezone
   * @return timezone
   */
  @javax.annotation.Nullable
  public NodeFullTimezone getTimezone() {
    return timezone;
  }

  public void setTimezone(NodeFullTimezone timezone) {
    this.timezone = timezone;
  }


  public NodeFull videos(List<NodeFullVideosInner> videos) {
    this.videos = videos;
    return this;
  }

  public NodeFull addVideosItem(NodeFullVideosInner videosItem) {
    if (this.videos == null) {
      this.videos = new ArrayList<>();
    }
    this.videos.add(videosItem);
    return this;
  }

  /**
   * Video card information
   * @return videos
   */
  @javax.annotation.Nullable
  public List<NodeFullVideosInner> getVideos() {
    return videos;
  }

  public void setVideos(List<NodeFullVideosInner> videos) {
    this.videos = videos;
  }


  public NodeFull virtualMachines(List<NodeFullVirtualMachinesInner> virtualMachines) {
    this.virtualMachines = virtualMachines;
    return this;
  }

  public NodeFull addVirtualMachinesItem(NodeFullVirtualMachinesInner virtualMachinesItem) {
    if (this.virtualMachines == null) {
      this.virtualMachines = new ArrayList<>();
    }
    this.virtualMachines.add(virtualMachinesItem);
    return this;
  }

  /**
   * Hosted virtual machine information
   * @return virtualMachines
   */
  @javax.annotation.Nullable
  public List<NodeFullVirtualMachinesInner> getVirtualMachines() {
    return virtualMachines;
  }

  public void setVirtualMachines(List<NodeFullVirtualMachinesInner> virtualMachines) {
    this.virtualMachines = virtualMachines;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NodeFull nodeFull = (NodeFull) o;
    return Objects.equals(this.accounts, nodeFull.accounts) &&
        Objects.equals(this.architectureDescription, nodeFull.architectureDescription) &&
        Objects.equals(this.bios, nodeFull.bios) &&
        Objects.equals(this.controllers, nodeFull.controllers) &&
        Objects.equals(this.description, nodeFull.description) &&
        Objects.equals(this.environmentVariables, nodeFull.environmentVariables) &&
        Objects.equals(this.fileSystems, nodeFull.fileSystems) &&
        Objects.equals(this.hostname, nodeFull.hostname) &&
        Objects.equals(this.id, nodeFull.id) &&
        Objects.equals(this.ipAddresses, nodeFull.ipAddresses) &&
        Objects.equals(this.lastInventoryDate, nodeFull.lastInventoryDate) &&
        Objects.equals(this.lastRunDate, nodeFull.lastRunDate) &&
        Objects.equals(this.machine, nodeFull.machine) &&
        Objects.equals(this.managementTechnology, nodeFull.managementTechnology) &&
        Objects.equals(this.managementTechnologyDetails, nodeFull.managementTechnologyDetails) &&
        Objects.equals(this.memories, nodeFull.memories) &&
        Objects.equals(this.networkInterfaces, nodeFull.networkInterfaces) &&
        Objects.equals(this.os, nodeFull.os) &&
        Objects.equals(this.policyMode, nodeFull.policyMode) &&
        Objects.equals(this.policyServerId, nodeFull.policyServerId) &&
        Objects.equals(this.ports, nodeFull.ports) &&
        Objects.equals(this.processes, nodeFull.processes) &&
        Objects.equals(this.processors, nodeFull.processors) &&
        Objects.equals(this.properties, nodeFull.properties) &&
        Objects.equals(this.ram, nodeFull.ram) &&
        Objects.equals(this.slots, nodeFull.slots) &&
        Objects.equals(this.software, nodeFull.software) &&
        Objects.equals(this.softwareUpdate, nodeFull.softwareUpdate) &&
        Objects.equals(this.sound, nodeFull.sound) &&
        Objects.equals(this.status, nodeFull.status) &&
        Objects.equals(this.storage, nodeFull.storage) &&
        Objects.equals(this.timezone, nodeFull.timezone) &&
        Objects.equals(this.videos, nodeFull.videos) &&
        Objects.equals(this.virtualMachines, nodeFull.virtualMachines);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accounts, architectureDescription, bios, controllers, description, environmentVariables, fileSystems, hostname, id, ipAddresses, lastInventoryDate, lastRunDate, machine, managementTechnology, managementTechnologyDetails, memories, networkInterfaces, os, policyMode, policyServerId, ports, processes, processors, properties, ram, slots, software, softwareUpdate, sound, status, storage, timezone, videos, virtualMachines);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NodeFull {\n");
    sb.append("    accounts: ").append(toIndentedString(accounts)).append("\n");
    sb.append("    architectureDescription: ").append(toIndentedString(architectureDescription)).append("\n");
    sb.append("    bios: ").append(toIndentedString(bios)).append("\n");
    sb.append("    controllers: ").append(toIndentedString(controllers)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    environmentVariables: ").append(toIndentedString(environmentVariables)).append("\n");
    sb.append("    fileSystems: ").append(toIndentedString(fileSystems)).append("\n");
    sb.append("    hostname: ").append(toIndentedString(hostname)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    ipAddresses: ").append(toIndentedString(ipAddresses)).append("\n");
    sb.append("    lastInventoryDate: ").append(toIndentedString(lastInventoryDate)).append("\n");
    sb.append("    lastRunDate: ").append(toIndentedString(lastRunDate)).append("\n");
    sb.append("    machine: ").append(toIndentedString(machine)).append("\n");
    sb.append("    managementTechnology: ").append(toIndentedString(managementTechnology)).append("\n");
    sb.append("    managementTechnologyDetails: ").append(toIndentedString(managementTechnologyDetails)).append("\n");
    sb.append("    memories: ").append(toIndentedString(memories)).append("\n");
    sb.append("    networkInterfaces: ").append(toIndentedString(networkInterfaces)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    policyMode: ").append(toIndentedString(policyMode)).append("\n");
    sb.append("    policyServerId: ").append(toIndentedString(policyServerId)).append("\n");
    sb.append("    ports: ").append(toIndentedString(ports)).append("\n");
    sb.append("    processes: ").append(toIndentedString(processes)).append("\n");
    sb.append("    processors: ").append(toIndentedString(processors)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
    sb.append("    ram: ").append(toIndentedString(ram)).append("\n");
    sb.append("    slots: ").append(toIndentedString(slots)).append("\n");
    sb.append("    software: ").append(toIndentedString(software)).append("\n");
    sb.append("    softwareUpdate: ").append(toIndentedString(softwareUpdate)).append("\n");
    sb.append("    sound: ").append(toIndentedString(sound)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    storage: ").append(toIndentedString(storage)).append("\n");
    sb.append("    timezone: ").append(toIndentedString(timezone)).append("\n");
    sb.append("    videos: ").append(toIndentedString(videos)).append("\n");
    sb.append("    virtualMachines: ").append(toIndentedString(virtualMachines)).append("\n");
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
    openapiFields.add("accounts");
    openapiFields.add("architectureDescription");
    openapiFields.add("bios");
    openapiFields.add("controllers");
    openapiFields.add("description");
    openapiFields.add("environmentVariables");
    openapiFields.add("fileSystems");
    openapiFields.add("hostname");
    openapiFields.add("id");
    openapiFields.add("ipAddresses");
    openapiFields.add("lastInventoryDate");
    openapiFields.add("lastRunDate");
    openapiFields.add("machine");
    openapiFields.add("managementTechnology");
    openapiFields.add("managementTechnologyDetails");
    openapiFields.add("memories");
    openapiFields.add("networkInterfaces");
    openapiFields.add("os");
    openapiFields.add("policyMode");
    openapiFields.add("policyServerId");
    openapiFields.add("ports");
    openapiFields.add("processes");
    openapiFields.add("processors");
    openapiFields.add("properties");
    openapiFields.add("ram");
    openapiFields.add("slots");
    openapiFields.add("software");
    openapiFields.add("softwareUpdate");
    openapiFields.add("sound");
    openapiFields.add("status");
    openapiFields.add("storage");
    openapiFields.add("timezone");
    openapiFields.add("videos");
    openapiFields.add("virtualMachines");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("hostname");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("ipAddresses");
    openapiRequiredFields.add("managementTechnology");
    openapiRequiredFields.add("policyServerId");
    openapiRequiredFields.add("properties");
    openapiRequiredFields.add("status");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NodeFull
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NodeFull.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NodeFull is not found in the empty JSON string", NodeFull.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NodeFull.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NodeFull` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : NodeFull.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("accounts") != null && !jsonObj.get("accounts").isJsonNull() && !jsonObj.get("accounts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `accounts` to be an array in the JSON string but got `%s`", jsonObj.get("accounts").toString()));
      }
      if ((jsonObj.get("architectureDescription") != null && !jsonObj.get("architectureDescription").isJsonNull()) && !jsonObj.get("architectureDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `architectureDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("architectureDescription").toString()));
      }
      // validate the optional field `bios`
      if (jsonObj.get("bios") != null && !jsonObj.get("bios").isJsonNull()) {
        NodeFullBios.validateJsonElement(jsonObj.get("bios"));
      }
      if (jsonObj.get("controllers") != null && !jsonObj.get("controllers").isJsonNull()) {
        JsonArray jsonArraycontrollers = jsonObj.getAsJsonArray("controllers");
        if (jsonArraycontrollers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("controllers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `controllers` to be an array in the JSON string but got `%s`", jsonObj.get("controllers").toString()));
          }

          // validate the optional field `controllers` (array)
          for (int i = 0; i < jsonArraycontrollers.size(); i++) {
            NodeFullControllersInner.validateJsonElement(jsonArraycontrollers.get(i));
          };
        }
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("environmentVariables") != null && !jsonObj.get("environmentVariables").isJsonNull()) {
        JsonArray jsonArrayenvironmentVariables = jsonObj.getAsJsonArray("environmentVariables");
        if (jsonArrayenvironmentVariables != null) {
          // ensure the json data is an array
          if (!jsonObj.get("environmentVariables").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `environmentVariables` to be an array in the JSON string but got `%s`", jsonObj.get("environmentVariables").toString()));
          }

          // validate the optional field `environmentVariables` (array)
          for (int i = 0; i < jsonArrayenvironmentVariables.size(); i++) {
            NodeFullEnvironmentVariablesInner.validateJsonElement(jsonArrayenvironmentVariables.get(i));
          };
        }
      }
      if (jsonObj.get("fileSystems") != null && !jsonObj.get("fileSystems").isJsonNull()) {
        JsonArray jsonArrayfileSystems = jsonObj.getAsJsonArray("fileSystems");
        if (jsonArrayfileSystems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("fileSystems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `fileSystems` to be an array in the JSON string but got `%s`", jsonObj.get("fileSystems").toString()));
          }

          // validate the optional field `fileSystems` (array)
          for (int i = 0; i < jsonArrayfileSystems.size(); i++) {
            NodeFullFileSystemsInner.validateJsonElement(jsonArrayfileSystems.get(i));
          };
        }
      }
      if (!jsonObj.get("hostname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hostname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hostname").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("ipAddresses") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("ipAddresses").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ipAddresses` to be an array in the JSON string but got `%s`", jsonObj.get("ipAddresses").toString()));
      }
      // validate the optional field `machine`
      if (jsonObj.get("machine") != null && !jsonObj.get("machine").isJsonNull()) {
        NodeFullMachine.validateJsonElement(jsonObj.get("machine"));
      }
      // ensure the json data is an array
      if (!jsonObj.get("managementTechnology").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `managementTechnology` to be an array in the JSON string but got `%s`", jsonObj.get("managementTechnology").toString()));
      }

      JsonArray jsonArraymanagementTechnology = jsonObj.getAsJsonArray("managementTechnology");
      // validate the required field `managementTechnology` (array)
      for (int i = 0; i < jsonArraymanagementTechnology.size(); i++) {
        NodeFullManagementTechnologyInner.validateJsonElement(jsonArraymanagementTechnology.get(i));
      };
      // validate the optional field `managementTechnologyDetails`
      if (jsonObj.get("managementTechnologyDetails") != null && !jsonObj.get("managementTechnologyDetails").isJsonNull()) {
        NodeFullManagementTechnologyDetails.validateJsonElement(jsonObj.get("managementTechnologyDetails"));
      }
      if (jsonObj.get("memories") != null && !jsonObj.get("memories").isJsonNull()) {
        JsonArray jsonArraymemories = jsonObj.getAsJsonArray("memories");
        if (jsonArraymemories != null) {
          // ensure the json data is an array
          if (!jsonObj.get("memories").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `memories` to be an array in the JSON string but got `%s`", jsonObj.get("memories").toString()));
          }

          // validate the optional field `memories` (array)
          for (int i = 0; i < jsonArraymemories.size(); i++) {
            NodeFullMemoriesInner.validateJsonElement(jsonArraymemories.get(i));
          };
        }
      }
      if (jsonObj.get("networkInterfaces") != null && !jsonObj.get("networkInterfaces").isJsonNull()) {
        JsonArray jsonArraynetworkInterfaces = jsonObj.getAsJsonArray("networkInterfaces");
        if (jsonArraynetworkInterfaces != null) {
          // ensure the json data is an array
          if (!jsonObj.get("networkInterfaces").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `networkInterfaces` to be an array in the JSON string but got `%s`", jsonObj.get("networkInterfaces").toString()));
          }

          // validate the optional field `networkInterfaces` (array)
          for (int i = 0; i < jsonArraynetworkInterfaces.size(); i++) {
            NodeFullNetworkInterfacesInner.validateJsonElement(jsonArraynetworkInterfaces.get(i));
          };
        }
      }
      // validate the optional field `os`
      if (jsonObj.get("os") != null && !jsonObj.get("os").isJsonNull()) {
        NodeFullOs.validateJsonElement(jsonObj.get("os"));
      }
      if ((jsonObj.get("policyMode") != null && !jsonObj.get("policyMode").isJsonNull()) && !jsonObj.get("policyMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `policyMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("policyMode").toString()));
      }
      // validate the optional field `policyMode`
      if (jsonObj.get("policyMode") != null && !jsonObj.get("policyMode").isJsonNull()) {
        PolicyModeEnum.validateJsonElement(jsonObj.get("policyMode"));
      }
      if (!jsonObj.get("policyServerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `policyServerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("policyServerId").toString()));
      }
      if (jsonObj.get("ports") != null && !jsonObj.get("ports").isJsonNull()) {
        JsonArray jsonArrayports = jsonObj.getAsJsonArray("ports");
        if (jsonArrayports != null) {
          // ensure the json data is an array
          if (!jsonObj.get("ports").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `ports` to be an array in the JSON string but got `%s`", jsonObj.get("ports").toString()));
          }

          // validate the optional field `ports` (array)
          for (int i = 0; i < jsonArrayports.size(); i++) {
            NodeFullPortsInner.validateJsonElement(jsonArrayports.get(i));
          };
        }
      }
      if (jsonObj.get("processes") != null && !jsonObj.get("processes").isJsonNull()) {
        JsonArray jsonArrayprocesses = jsonObj.getAsJsonArray("processes");
        if (jsonArrayprocesses != null) {
          // ensure the json data is an array
          if (!jsonObj.get("processes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `processes` to be an array in the JSON string but got `%s`", jsonObj.get("processes").toString()));
          }

          // validate the optional field `processes` (array)
          for (int i = 0; i < jsonArrayprocesses.size(); i++) {
            NodeFullProcessesInner.validateJsonElement(jsonArrayprocesses.get(i));
          };
        }
      }
      if (jsonObj.get("processors") != null && !jsonObj.get("processors").isJsonNull()) {
        JsonArray jsonArrayprocessors = jsonObj.getAsJsonArray("processors");
        if (jsonArrayprocessors != null) {
          // ensure the json data is an array
          if (!jsonObj.get("processors").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `processors` to be an array in the JSON string but got `%s`", jsonObj.get("processors").toString()));
          }

          // validate the optional field `processors` (array)
          for (int i = 0; i < jsonArrayprocessors.size(); i++) {
            NodeFullProcessorsInner.validateJsonElement(jsonArrayprocessors.get(i));
          };
        }
      }
      // ensure the json data is an array
      if (!jsonObj.get("properties").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `properties` to be an array in the JSON string but got `%s`", jsonObj.get("properties").toString()));
      }

      JsonArray jsonArrayproperties = jsonObj.getAsJsonArray("properties");
      // validate the required field `properties` (array)
      for (int i = 0; i < jsonArrayproperties.size(); i++) {
        NodeAddInnerPropertiesInner.validateJsonElement(jsonArrayproperties.get(i));
      };
      if (jsonObj.get("slots") != null && !jsonObj.get("slots").isJsonNull()) {
        JsonArray jsonArrayslots = jsonObj.getAsJsonArray("slots");
        if (jsonArrayslots != null) {
          // ensure the json data is an array
          if (!jsonObj.get("slots").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `slots` to be an array in the JSON string but got `%s`", jsonObj.get("slots").toString()));
          }

          // validate the optional field `slots` (array)
          for (int i = 0; i < jsonArrayslots.size(); i++) {
            NodeFullSlotsInner.validateJsonElement(jsonArrayslots.get(i));
          };
        }
      }
      if (jsonObj.get("software") != null && !jsonObj.get("software").isJsonNull()) {
        JsonArray jsonArraysoftware = jsonObj.getAsJsonArray("software");
        if (jsonArraysoftware != null) {
          // ensure the json data is an array
          if (!jsonObj.get("software").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `software` to be an array in the JSON string but got `%s`", jsonObj.get("software").toString()));
          }

          // validate the optional field `software` (array)
          for (int i = 0; i < jsonArraysoftware.size(); i++) {
            NodeFullSoftwareInner.validateJsonElement(jsonArraysoftware.get(i));
          };
        }
      }
      if (jsonObj.get("softwareUpdate") != null && !jsonObj.get("softwareUpdate").isJsonNull()) {
        JsonArray jsonArraysoftwareUpdate = jsonObj.getAsJsonArray("softwareUpdate");
        if (jsonArraysoftwareUpdate != null) {
          // ensure the json data is an array
          if (!jsonObj.get("softwareUpdate").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `softwareUpdate` to be an array in the JSON string but got `%s`", jsonObj.get("softwareUpdate").toString()));
          }

          // validate the optional field `softwareUpdate` (array)
          for (int i = 0; i < jsonArraysoftwareUpdate.size(); i++) {
            NodeFullSoftwareUpdateInner.validateJsonElement(jsonArraysoftwareUpdate.get(i));
          };
        }
      }
      if (jsonObj.get("sound") != null && !jsonObj.get("sound").isJsonNull()) {
        JsonArray jsonArraysound = jsonObj.getAsJsonArray("sound");
        if (jsonArraysound != null) {
          // ensure the json data is an array
          if (!jsonObj.get("sound").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `sound` to be an array in the JSON string but got `%s`", jsonObj.get("sound").toString()));
          }

          // validate the optional field `sound` (array)
          for (int i = 0; i < jsonArraysound.size(); i++) {
            NodeFullSoundInner.validateJsonElement(jsonArraysound.get(i));
          };
        }
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      if (jsonObj.get("storage") != null && !jsonObj.get("storage").isJsonNull()) {
        JsonArray jsonArraystorage = jsonObj.getAsJsonArray("storage");
        if (jsonArraystorage != null) {
          // ensure the json data is an array
          if (!jsonObj.get("storage").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `storage` to be an array in the JSON string but got `%s`", jsonObj.get("storage").toString()));
          }

          // validate the optional field `storage` (array)
          for (int i = 0; i < jsonArraystorage.size(); i++) {
            NodeFullStorageInner.validateJsonElement(jsonArraystorage.get(i));
          };
        }
      }
      // validate the optional field `timezone`
      if (jsonObj.get("timezone") != null && !jsonObj.get("timezone").isJsonNull()) {
        NodeFullTimezone.validateJsonElement(jsonObj.get("timezone"));
      }
      if (jsonObj.get("videos") != null && !jsonObj.get("videos").isJsonNull()) {
        JsonArray jsonArrayvideos = jsonObj.getAsJsonArray("videos");
        if (jsonArrayvideos != null) {
          // ensure the json data is an array
          if (!jsonObj.get("videos").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `videos` to be an array in the JSON string but got `%s`", jsonObj.get("videos").toString()));
          }

          // validate the optional field `videos` (array)
          for (int i = 0; i < jsonArrayvideos.size(); i++) {
            NodeFullVideosInner.validateJsonElement(jsonArrayvideos.get(i));
          };
        }
      }
      if (jsonObj.get("virtualMachines") != null && !jsonObj.get("virtualMachines").isJsonNull()) {
        JsonArray jsonArrayvirtualMachines = jsonObj.getAsJsonArray("virtualMachines");
        if (jsonArrayvirtualMachines != null) {
          // ensure the json data is an array
          if (!jsonObj.get("virtualMachines").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `virtualMachines` to be an array in the JSON string but got `%s`", jsonObj.get("virtualMachines").toString()));
          }

          // validate the optional field `virtualMachines` (array)
          for (int i = 0; i < jsonArrayvirtualMachines.size(); i++) {
            NodeFullVirtualMachinesInner.validateJsonElement(jsonArrayvirtualMachines.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NodeFull.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NodeFull' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NodeFull> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NodeFull.class));

       return (TypeAdapter<T>) new TypeAdapter<NodeFull>() {
           @Override
           public void write(JsonWriter out, NodeFull value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NodeFull read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NodeFull given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NodeFull
   * @throws IOException if the JSON string is invalid with respect to NodeFull
   */
  public static NodeFull fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NodeFull.class);
  }

  /**
   * Convert an instance of NodeFull to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

