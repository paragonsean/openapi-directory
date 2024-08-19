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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GetAllSettings200ResponseDataSettingsAllowedNetworksInner;

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
 * GetAllSettings200ResponseDataSettings
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:58.781092-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetAllSettings200ResponseDataSettings {
  public static final String SERIALIZED_NAME_ALLOWED_NETWORKS = "allowed_networks";
  @SerializedName(SERIALIZED_NAME_ALLOWED_NETWORKS)
  private List<GetAllSettings200ResponseDataSettingsAllowedNetworksInner> allowedNetworks = new ArrayList<>();

  public static final String SERIALIZED_NAME_CHANGE_MESSAGE_PROMPT = "change_message_prompt";
  @SerializedName(SERIALIZED_NAME_CHANGE_MESSAGE_PROMPT)
  private String changeMessagePrompt;

  public static final String SERIALIZED_NAME_DISPLAY_RECENT_CHANGES_GRAPHS = "display_recent_changes_graphs";
  @SerializedName(SERIALIZED_NAME_DISPLAY_RECENT_CHANGES_GRAPHS)
  private Boolean displayRecentChangesGraphs;

  public static final String SERIALIZED_NAME_ENABLE_CHANGE_MESSAGE = "enable_change_message";
  @SerializedName(SERIALIZED_NAME_ENABLE_CHANGE_MESSAGE)
  private Boolean enableChangeMessage;

  public static final String SERIALIZED_NAME_ENABLE_CHANGE_REQUEST = "enable_change_request";
  @SerializedName(SERIALIZED_NAME_ENABLE_CHANGE_REQUEST)
  private Boolean enableChangeRequest;

  public static final String SERIALIZED_NAME_ENABLE_JAVASCRIPT_DIRECTIVES = "enable_javascript_directives";
  @SerializedName(SERIALIZED_NAME_ENABLE_JAVASCRIPT_DIRECTIVES)
  private String enableJavascriptDirectives;

  public static final String SERIALIZED_NAME_ENABLE_SELF_DEPLOYMENT = "enable_self_deployment";
  @SerializedName(SERIALIZED_NAME_ENABLE_SELF_DEPLOYMENT)
  private Boolean enableSelfDeployment;

  public static final String SERIALIZED_NAME_ENABLE_SELF_VALIDATION = "enable_self_validation";
  @SerializedName(SERIALIZED_NAME_ENABLE_SELF_VALIDATION)
  private Boolean enableSelfValidation;

  public static final String SERIALIZED_NAME_FIRST_RUN_HOUR = "first_run_hour";
  @SerializedName(SERIALIZED_NAME_FIRST_RUN_HOUR)
  private Integer firstRunHour;

  public static final String SERIALIZED_NAME_FIRST_RUN_MINUTE = "first_run_minute";
  @SerializedName(SERIALIZED_NAME_FIRST_RUN_MINUTE)
  private Integer firstRunMinute;

  /**
   * Define the default setting for global policy mode
   */
  @JsonAdapter(GlobalPolicyModeEnum.Adapter.class)
  public enum GlobalPolicyModeEnum {
    ENFORCE("enforce"),
    
    AUDIT("audit");

    private String value;

    GlobalPolicyModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GlobalPolicyModeEnum fromValue(String value) {
      for (GlobalPolicyModeEnum b : GlobalPolicyModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<GlobalPolicyModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GlobalPolicyModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GlobalPolicyModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GlobalPolicyModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GlobalPolicyModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GLOBAL_POLICY_MODE = "global_policy_mode";
  @SerializedName(SERIALIZED_NAME_GLOBAL_POLICY_MODE)
  private GlobalPolicyModeEnum globalPolicyMode;

  public static final String SERIALIZED_NAME_GLOBAL_POLICY_MODE_OVERRIDABLE = "global_policy_mode_overridable";
  @SerializedName(SERIALIZED_NAME_GLOBAL_POLICY_MODE_OVERRIDABLE)
  private Boolean globalPolicyModeOverridable;

  public static final String SERIALIZED_NAME_HEARTBEAT_FREQUENCY = "heartbeat_frequency";
  @SerializedName(SERIALIZED_NAME_HEARTBEAT_FREQUENCY)
  private Integer heartbeatFrequency;

  public static final String SERIALIZED_NAME_MANDATORY_CHANGE_MESSAGE = "mandatory_change_message";
  @SerializedName(SERIALIZED_NAME_MANDATORY_CHANGE_MESSAGE)
  private Boolean mandatoryChangeMessage;

  public static final String SERIALIZED_NAME_MODIFIED_FILE_TTL = "modified_file_ttl";
  @SerializedName(SERIALIZED_NAME_MODIFIED_FILE_TTL)
  private Integer modifiedFileTtl;

  public static final String SERIALIZED_NAME_NODE_ACCEPT_DUPLICATED_HOSTNAME = "node_accept_duplicated_hostname";
  @SerializedName(SERIALIZED_NAME_NODE_ACCEPT_DUPLICATED_HOSTNAME)
  private Boolean nodeAcceptDuplicatedHostname = false;

  /**
   * Default policy mode for accepted node
   */
  @JsonAdapter(NodeOnacceptDefaultPolicyModeEnum.Adapter.class)
  public enum NodeOnacceptDefaultPolicyModeEnum {
    DEFAULT("default"),
    
    ENFORCE("enforce"),
    
    AUDIT("audit");

    private String value;

    NodeOnacceptDefaultPolicyModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NodeOnacceptDefaultPolicyModeEnum fromValue(String value) {
      for (NodeOnacceptDefaultPolicyModeEnum b : NodeOnacceptDefaultPolicyModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NodeOnacceptDefaultPolicyModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NodeOnacceptDefaultPolicyModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NodeOnacceptDefaultPolicyModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NodeOnacceptDefaultPolicyModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NodeOnacceptDefaultPolicyModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NODE_ONACCEPT_DEFAULT_POLICY_MODE = "node_onaccept_default_policyMode";
  @SerializedName(SERIALIZED_NAME_NODE_ONACCEPT_DEFAULT_POLICY_MODE)
  private NodeOnacceptDefaultPolicyModeEnum nodeOnacceptDefaultPolicyMode;

  /**
   * Set default state for node when they are accepted within Rudder
   */
  @JsonAdapter(NodeOnacceptDefaultStateEnum.Adapter.class)
  public enum NodeOnacceptDefaultStateEnum {
    ENABLED("enabled"),
    
    IGNORED("ignored"),
    
    EMPTY_POLICIES("empty-policies"),
    
    INITIALIZING("initializing"),
    
    PREPARING_EOL("preparing-eol");

    private String value;

    NodeOnacceptDefaultStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NodeOnacceptDefaultStateEnum fromValue(String value) {
      for (NodeOnacceptDefaultStateEnum b : NodeOnacceptDefaultStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NodeOnacceptDefaultStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NodeOnacceptDefaultStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NodeOnacceptDefaultStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NodeOnacceptDefaultStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NodeOnacceptDefaultStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NODE_ONACCEPT_DEFAULT_STATE = "node_onaccept_default_state";
  @SerializedName(SERIALIZED_NAME_NODE_ONACCEPT_DEFAULT_STATE)
  private NodeOnacceptDefaultStateEnum nodeOnacceptDefaultState;

  public static final String SERIALIZED_NAME_OUTPUT_FILE_TTL = "output_file_ttl";
  @SerializedName(SERIALIZED_NAME_OUTPUT_FILE_TTL)
  private Integer outputFileTtl;

  /**
   * Method used to synchronize data between server and relays, either \&quot;classic\&quot; (agent protocol, default), \&quot;rsync\&quot; (use rsync to synchronize, that you&#39;ll need to be manually set up), or \&quot;disabled\&quot; (use third party system to transmit data)
   */
  @JsonAdapter(RelayServerSynchronizationMethodEnum.Adapter.class)
  public enum RelayServerSynchronizationMethodEnum {
    CLASSIC("classic"),
    
    RSYNC("rsync"),
    
    DISABLED("disabled");

    private String value;

    RelayServerSynchronizationMethodEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RelayServerSynchronizationMethodEnum fromValue(String value) {
      for (RelayServerSynchronizationMethodEnum b : RelayServerSynchronizationMethodEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RelayServerSynchronizationMethodEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RelayServerSynchronizationMethodEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RelayServerSynchronizationMethodEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RelayServerSynchronizationMethodEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RelayServerSynchronizationMethodEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RELAY_SERVER_SYNCHRONIZATION_METHOD = "relay_server_synchronization_method";
  @SerializedName(SERIALIZED_NAME_RELAY_SERVER_SYNCHRONIZATION_METHOD)
  private RelayServerSynchronizationMethodEnum relayServerSynchronizationMethod;

  public static final String SERIALIZED_NAME_RELAY_SERVER_SYNCHRONIZE_POLICIES = "relay_server_synchronize_policies";
  @SerializedName(SERIALIZED_NAME_RELAY_SERVER_SYNCHRONIZE_POLICIES)
  private Boolean relayServerSynchronizePolicies;

  public static final String SERIALIZED_NAME_RELAY_SERVER_SYNCHRONIZE_SHARED_FILES = "relay_server_synchronize_shared_files";
  @SerializedName(SERIALIZED_NAME_RELAY_SERVER_SYNCHRONIZE_SHARED_FILES)
  private Boolean relayServerSynchronizeSharedFiles;

  /**
   * Compliance reporting mode
   */
  @JsonAdapter(ReportingModeEnum.Adapter.class)
  public enum ReportingModeEnum {
    FULL_COMPLIANCE("full-compliance"),
    
    CHANGES_ONLY("changes-only"),
    
    REPORTS_DISABLED("reports-disabled");

    private String value;

    ReportingModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ReportingModeEnum fromValue(String value) {
      for (ReportingModeEnum b : ReportingModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ReportingModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ReportingModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ReportingModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ReportingModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ReportingModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REPORTING_MODE = "reporting_mode";
  @SerializedName(SERIALIZED_NAME_REPORTING_MODE)
  private ReportingModeEnum reportingMode;

  public static final String SERIALIZED_NAME_REQUIRE_TIME_SYNCHRONIZATION = "require_time_synchronization";
  @SerializedName(SERIALIZED_NAME_REQUIRE_TIME_SYNCHRONIZATION)
  private Boolean requireTimeSynchronization;

  public static final String SERIALIZED_NAME_RUDDER_COMPUTE_CHANGES = "rudder_compute_changes";
  @SerializedName(SERIALIZED_NAME_RUDDER_COMPUTE_CHANGES)
  private Boolean rudderComputeChanges = true;

  public static final String SERIALIZED_NAME_RUDDER_COMPUTE_DYNGROUPS_MAX_PARALLELISM = "rudder_compute_dyngroups_max_parallelism";
  @SerializedName(SERIALIZED_NAME_RUDDER_COMPUTE_DYNGROUPS_MAX_PARALLELISM)
  private String rudderComputeDyngroupsMaxParallelism = "1";

  public static final String SERIALIZED_NAME_RUDDER_GENERATION_COMPUTE_DYNGROUPS = "rudder_generation_compute_dyngroups";
  @SerializedName(SERIALIZED_NAME_RUDDER_GENERATION_COMPUTE_DYNGROUPS)
  private Boolean rudderGenerationComputeDyngroups = true;

  public static final String SERIALIZED_NAME_RUDDER_GENERATION_CONTINUE_ON_ERROR = "rudder_generation_continue_on_error";
  @SerializedName(SERIALIZED_NAME_RUDDER_GENERATION_CONTINUE_ON_ERROR)
  private Boolean rudderGenerationContinueOnError = false;

  public static final String SERIALIZED_NAME_RUDDER_GENERATION_DELAY = "rudder_generation_delay";
  @SerializedName(SERIALIZED_NAME_RUDDER_GENERATION_DELAY)
  private String rudderGenerationDelay = "0 seconds";

  public static final String SERIALIZED_NAME_RUDDER_GENERATION_JS_TIMEOUT = "rudder_generation_js_timeout";
  @SerializedName(SERIALIZED_NAME_RUDDER_GENERATION_JS_TIMEOUT)
  private Integer rudderGenerationJsTimeout = 30;

  public static final String SERIALIZED_NAME_RUDDER_GENERATION_MAX_PARALLELISM = "rudder_generation_max_parallelism";
  @SerializedName(SERIALIZED_NAME_RUDDER_GENERATION_MAX_PARALLELISM)
  private String rudderGenerationMaxParallelism = "x0.5";

  public static final String SERIALIZED_NAME_RUDDER_GENERATION_POLICY = "rudder_generation_policy";
  @SerializedName(SERIALIZED_NAME_RUDDER_GENERATION_POLICY)
  private String rudderGenerationPolicy = "all";

  /**
   * Default reporting protocol used
   */
  @JsonAdapter(RudderReportProtocolDefaultEnum.Adapter.class)
  public enum RudderReportProtocolDefaultEnum {
    HTTPS("HTTPS"),
    
    SYSLOG("SYSLOG");

    private String value;

    RudderReportProtocolDefaultEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RudderReportProtocolDefaultEnum fromValue(String value) {
      for (RudderReportProtocolDefaultEnum b : RudderReportProtocolDefaultEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RudderReportProtocolDefaultEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RudderReportProtocolDefaultEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RudderReportProtocolDefaultEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RudderReportProtocolDefaultEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RudderReportProtocolDefaultEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RUDDER_REPORT_PROTOCOL_DEFAULT = "rudder_report_protocol_default";
  @SerializedName(SERIALIZED_NAME_RUDDER_REPORT_PROTOCOL_DEFAULT)
  private RudderReportProtocolDefaultEnum rudderReportProtocolDefault;

  public static final String SERIALIZED_NAME_RUDDER_SAVE_DB_COMPLIANCE_DETAILS = "rudder_save_db_compliance_details";
  @SerializedName(SERIALIZED_NAME_RUDDER_SAVE_DB_COMPLIANCE_DETAILS)
  private Boolean rudderSaveDbComplianceDetails = false;

  public static final String SERIALIZED_NAME_RUDDER_SAVE_DB_COMPLIANCE_LEVELS = "rudder_save_db_compliance_levels";
  @SerializedName(SERIALIZED_NAME_RUDDER_SAVE_DB_COMPLIANCE_LEVELS)
  private Boolean rudderSaveDbComplianceLevels = true;

  public static final String SERIALIZED_NAME_RUDDER_VERIFY_CERTIFICATES = "rudder_verify_certificates";
  @SerializedName(SERIALIZED_NAME_RUDDER_VERIFY_CERTIFICATES)
  private Boolean rudderVerifyCertificates = false;

  public static final String SERIALIZED_NAME_RUN_FREQUENCY = "run_frequency";
  @SerializedName(SERIALIZED_NAME_RUN_FREQUENCY)
  private Integer runFrequency;

  public static final String SERIALIZED_NAME_SEND_METRICS = "send_metrics";
  @SerializedName(SERIALIZED_NAME_SEND_METRICS)
  private String sendMetrics;

  public static final String SERIALIZED_NAME_SPLAY_TIME = "splay_time";
  @SerializedName(SERIALIZED_NAME_SPLAY_TIME)
  private Integer splayTime;

  public static final String SERIALIZED_NAME_UNEXPECTED_UNBOUND_VAR_VALUES = "unexpected_unbound_var_values";
  @SerializedName(SERIALIZED_NAME_UNEXPECTED_UNBOUND_VAR_VALUES)
  private Boolean unexpectedUnboundVarValues = true;

  public GetAllSettings200ResponseDataSettings() {
  }

  public GetAllSettings200ResponseDataSettings allowedNetworks(List<GetAllSettings200ResponseDataSettingsAllowedNetworksInner> allowedNetworks) {
    this.allowedNetworks = allowedNetworks;
    return this;
  }

  public GetAllSettings200ResponseDataSettings addAllowedNetworksItem(GetAllSettings200ResponseDataSettingsAllowedNetworksInner allowedNetworksItem) {
    if (this.allowedNetworks == null) {
      this.allowedNetworks = new ArrayList<>();
    }
    this.allowedNetworks.add(allowedNetworksItem);
    return this;
  }

  /**
   * List of allowed networks for each policy server (root and relays)
   * @return allowedNetworks
   */
  @javax.annotation.Nullable
  public List<GetAllSettings200ResponseDataSettingsAllowedNetworksInner> getAllowedNetworks() {
    return allowedNetworks;
  }

  public void setAllowedNetworks(List<GetAllSettings200ResponseDataSettingsAllowedNetworksInner> allowedNetworks) {
    this.allowedNetworks = allowedNetworks;
  }


  public GetAllSettings200ResponseDataSettings changeMessagePrompt(String changeMessagePrompt) {
    this.changeMessagePrompt = changeMessagePrompt;
    return this;
  }

  /**
   * Explanation to display
   * @return changeMessagePrompt
   */
  @javax.annotation.Nullable
  public String getChangeMessagePrompt() {
    return changeMessagePrompt;
  }

  public void setChangeMessagePrompt(String changeMessagePrompt) {
    this.changeMessagePrompt = changeMessagePrompt;
  }


  public GetAllSettings200ResponseDataSettings displayRecentChangesGraphs(Boolean displayRecentChangesGraphs) {
    this.displayRecentChangesGraphs = displayRecentChangesGraphs;
    return this;
  }

  /**
   * Display changes graphs
   * @return displayRecentChangesGraphs
   */
  @javax.annotation.Nullable
  public Boolean getDisplayRecentChangesGraphs() {
    return displayRecentChangesGraphs;
  }

  public void setDisplayRecentChangesGraphs(Boolean displayRecentChangesGraphs) {
    this.displayRecentChangesGraphs = displayRecentChangesGraphs;
  }


  public GetAllSettings200ResponseDataSettings enableChangeMessage(Boolean enableChangeMessage) {
    this.enableChangeMessage = enableChangeMessage;
    return this;
  }

  /**
   * Enable change audit logs
   * @return enableChangeMessage
   */
  @javax.annotation.Nullable
  public Boolean getEnableChangeMessage() {
    return enableChangeMessage;
  }

  public void setEnableChangeMessage(Boolean enableChangeMessage) {
    this.enableChangeMessage = enableChangeMessage;
  }


  public GetAllSettings200ResponseDataSettings enableChangeRequest(Boolean enableChangeRequest) {
    this.enableChangeRequest = enableChangeRequest;
    return this;
  }

  /**
   * Enable Change Requests
   * @return enableChangeRequest
   */
  @javax.annotation.Nullable
  public Boolean getEnableChangeRequest() {
    return enableChangeRequest;
  }

  public void setEnableChangeRequest(Boolean enableChangeRequest) {
    this.enableChangeRequest = enableChangeRequest;
  }


  public GetAllSettings200ResponseDataSettings enableJavascriptDirectives(String enableJavascriptDirectives) {
    this.enableJavascriptDirectives = enableJavascriptDirectives;
    return this;
  }

  /**
   * Enable script evaluation in Directives
   * @return enableJavascriptDirectives
   */
  @javax.annotation.Nullable
  public String getEnableJavascriptDirectives() {
    return enableJavascriptDirectives;
  }

  public void setEnableJavascriptDirectives(String enableJavascriptDirectives) {
    this.enableJavascriptDirectives = enableJavascriptDirectives;
  }


  public GetAllSettings200ResponseDataSettings enableSelfDeployment(Boolean enableSelfDeployment) {
    this.enableSelfDeployment = enableSelfDeployment;
    return this;
  }

  /**
   * Allow self deployment
   * @return enableSelfDeployment
   */
  @javax.annotation.Nullable
  public Boolean getEnableSelfDeployment() {
    return enableSelfDeployment;
  }

  public void setEnableSelfDeployment(Boolean enableSelfDeployment) {
    this.enableSelfDeployment = enableSelfDeployment;
  }


  public GetAllSettings200ResponseDataSettings enableSelfValidation(Boolean enableSelfValidation) {
    this.enableSelfValidation = enableSelfValidation;
    return this;
  }

  /**
   * Allow self validation
   * @return enableSelfValidation
   */
  @javax.annotation.Nullable
  public Boolean getEnableSelfValidation() {
    return enableSelfValidation;
  }

  public void setEnableSelfValidation(Boolean enableSelfValidation) {
    this.enableSelfValidation = enableSelfValidation;
  }


  public GetAllSettings200ResponseDataSettings firstRunHour(Integer firstRunHour) {
    this.firstRunHour = firstRunHour;
    return this;
  }

  /**
   * First agent run time - hour
   * @return firstRunHour
   */
  @javax.annotation.Nullable
  public Integer getFirstRunHour() {
    return firstRunHour;
  }

  public void setFirstRunHour(Integer firstRunHour) {
    this.firstRunHour = firstRunHour;
  }


  public GetAllSettings200ResponseDataSettings firstRunMinute(Integer firstRunMinute) {
    this.firstRunMinute = firstRunMinute;
    return this;
  }

  /**
   * First agent run time - minute
   * @return firstRunMinute
   */
  @javax.annotation.Nullable
  public Integer getFirstRunMinute() {
    return firstRunMinute;
  }

  public void setFirstRunMinute(Integer firstRunMinute) {
    this.firstRunMinute = firstRunMinute;
  }


  public GetAllSettings200ResponseDataSettings globalPolicyMode(GlobalPolicyModeEnum globalPolicyMode) {
    this.globalPolicyMode = globalPolicyMode;
    return this;
  }

  /**
   * Define the default setting for global policy mode
   * @return globalPolicyMode
   */
  @javax.annotation.Nullable
  public GlobalPolicyModeEnum getGlobalPolicyMode() {
    return globalPolicyMode;
  }

  public void setGlobalPolicyMode(GlobalPolicyModeEnum globalPolicyMode) {
    this.globalPolicyMode = globalPolicyMode;
  }


  public GetAllSettings200ResponseDataSettings globalPolicyModeOverridable(Boolean globalPolicyModeOverridable) {
    this.globalPolicyModeOverridable = globalPolicyModeOverridable;
    return this;
  }

  /**
   * Allow overrides on this default setting
   * @return globalPolicyModeOverridable
   */
  @javax.annotation.Nullable
  public Boolean getGlobalPolicyModeOverridable() {
    return globalPolicyModeOverridable;
  }

  public void setGlobalPolicyModeOverridable(Boolean globalPolicyModeOverridable) {
    this.globalPolicyModeOverridable = globalPolicyModeOverridable;
  }


  public GetAllSettings200ResponseDataSettings heartbeatFrequency(Integer heartbeatFrequency) {
    this.heartbeatFrequency = heartbeatFrequency;
    return this;
  }

  /**
   * Send heartbeat every heartbeat_frequency runs (only on **changes-only** compliance mode)
   * @return heartbeatFrequency
   */
  @javax.annotation.Nullable
  public Integer getHeartbeatFrequency() {
    return heartbeatFrequency;
  }

  public void setHeartbeatFrequency(Integer heartbeatFrequency) {
    this.heartbeatFrequency = heartbeatFrequency;
  }


  public GetAllSettings200ResponseDataSettings mandatoryChangeMessage(Boolean mandatoryChangeMessage) {
    this.mandatoryChangeMessage = mandatoryChangeMessage;
    return this;
  }

  /**
   * Make message mandatory
   * @return mandatoryChangeMessage
   */
  @javax.annotation.Nullable
  public Boolean getMandatoryChangeMessage() {
    return mandatoryChangeMessage;
  }

  public void setMandatoryChangeMessage(Boolean mandatoryChangeMessage) {
    this.mandatoryChangeMessage = mandatoryChangeMessage;
  }


  public GetAllSettings200ResponseDataSettings modifiedFileTtl(Integer modifiedFileTtl) {
    this.modifiedFileTtl = modifiedFileTtl;
    return this;
  }

  /**
   * Number of days to retain modified files
   * @return modifiedFileTtl
   */
  @javax.annotation.Nullable
  public Integer getModifiedFileTtl() {
    return modifiedFileTtl;
  }

  public void setModifiedFileTtl(Integer modifiedFileTtl) {
    this.modifiedFileTtl = modifiedFileTtl;
  }


  public GetAllSettings200ResponseDataSettings nodeAcceptDuplicatedHostname(Boolean nodeAcceptDuplicatedHostname) {
    this.nodeAcceptDuplicatedHostname = nodeAcceptDuplicatedHostname;
    return this;
  }

  /**
   * Allow acceptation of a pending node when another one with the same hostname is already accepted
   * @return nodeAcceptDuplicatedHostname
   */
  @javax.annotation.Nullable
  public Boolean getNodeAcceptDuplicatedHostname() {
    return nodeAcceptDuplicatedHostname;
  }

  public void setNodeAcceptDuplicatedHostname(Boolean nodeAcceptDuplicatedHostname) {
    this.nodeAcceptDuplicatedHostname = nodeAcceptDuplicatedHostname;
  }


  public GetAllSettings200ResponseDataSettings nodeOnacceptDefaultPolicyMode(NodeOnacceptDefaultPolicyModeEnum nodeOnacceptDefaultPolicyMode) {
    this.nodeOnacceptDefaultPolicyMode = nodeOnacceptDefaultPolicyMode;
    return this;
  }

  /**
   * Default policy mode for accepted node
   * @return nodeOnacceptDefaultPolicyMode
   */
  @javax.annotation.Nullable
  public NodeOnacceptDefaultPolicyModeEnum getNodeOnacceptDefaultPolicyMode() {
    return nodeOnacceptDefaultPolicyMode;
  }

  public void setNodeOnacceptDefaultPolicyMode(NodeOnacceptDefaultPolicyModeEnum nodeOnacceptDefaultPolicyMode) {
    this.nodeOnacceptDefaultPolicyMode = nodeOnacceptDefaultPolicyMode;
  }


  public GetAllSettings200ResponseDataSettings nodeOnacceptDefaultState(NodeOnacceptDefaultStateEnum nodeOnacceptDefaultState) {
    this.nodeOnacceptDefaultState = nodeOnacceptDefaultState;
    return this;
  }

  /**
   * Set default state for node when they are accepted within Rudder
   * @return nodeOnacceptDefaultState
   */
  @javax.annotation.Nullable
  public NodeOnacceptDefaultStateEnum getNodeOnacceptDefaultState() {
    return nodeOnacceptDefaultState;
  }

  public void setNodeOnacceptDefaultState(NodeOnacceptDefaultStateEnum nodeOnacceptDefaultState) {
    this.nodeOnacceptDefaultState = nodeOnacceptDefaultState;
  }


  public GetAllSettings200ResponseDataSettings outputFileTtl(Integer outputFileTtl) {
    this.outputFileTtl = outputFileTtl;
    return this;
  }

  /**
   * Number of days to retain agent output files
   * @return outputFileTtl
   */
  @javax.annotation.Nullable
  public Integer getOutputFileTtl() {
    return outputFileTtl;
  }

  public void setOutputFileTtl(Integer outputFileTtl) {
    this.outputFileTtl = outputFileTtl;
  }


  public GetAllSettings200ResponseDataSettings relayServerSynchronizationMethod(RelayServerSynchronizationMethodEnum relayServerSynchronizationMethod) {
    this.relayServerSynchronizationMethod = relayServerSynchronizationMethod;
    return this;
  }

  /**
   * Method used to synchronize data between server and relays, either \&quot;classic\&quot; (agent protocol, default), \&quot;rsync\&quot; (use rsync to synchronize, that you&#39;ll need to be manually set up), or \&quot;disabled\&quot; (use third party system to transmit data)
   * @return relayServerSynchronizationMethod
   */
  @javax.annotation.Nullable
  public RelayServerSynchronizationMethodEnum getRelayServerSynchronizationMethod() {
    return relayServerSynchronizationMethod;
  }

  public void setRelayServerSynchronizationMethod(RelayServerSynchronizationMethodEnum relayServerSynchronizationMethod) {
    this.relayServerSynchronizationMethod = relayServerSynchronizationMethod;
  }


  public GetAllSettings200ResponseDataSettings relayServerSynchronizePolicies(Boolean relayServerSynchronizePolicies) {
    this.relayServerSynchronizePolicies = relayServerSynchronizePolicies;
    return this;
  }

  /**
   * If **rsync** is set as a synchronization method, use rsync to synchronize policies between Rudder server and relays. If false, you&#39;ll have to synchronize policies yourself.
   * @return relayServerSynchronizePolicies
   */
  @javax.annotation.Nullable
  public Boolean getRelayServerSynchronizePolicies() {
    return relayServerSynchronizePolicies;
  }

  public void setRelayServerSynchronizePolicies(Boolean relayServerSynchronizePolicies) {
    this.relayServerSynchronizePolicies = relayServerSynchronizePolicies;
  }


  public GetAllSettings200ResponseDataSettings relayServerSynchronizeSharedFiles(Boolean relayServerSynchronizeSharedFiles) {
    this.relayServerSynchronizeSharedFiles = relayServerSynchronizeSharedFiles;
    return this;
  }

  /**
   * If **rsync** is set as a synchronization method, use rsync to synchronize shared files between Rudder server and relays. If false, you&#39;ll have to synchronize shared files yourself.
   * @return relayServerSynchronizeSharedFiles
   */
  @javax.annotation.Nullable
  public Boolean getRelayServerSynchronizeSharedFiles() {
    return relayServerSynchronizeSharedFiles;
  }

  public void setRelayServerSynchronizeSharedFiles(Boolean relayServerSynchronizeSharedFiles) {
    this.relayServerSynchronizeSharedFiles = relayServerSynchronizeSharedFiles;
  }


  public GetAllSettings200ResponseDataSettings reportingMode(ReportingModeEnum reportingMode) {
    this.reportingMode = reportingMode;
    return this;
  }

  /**
   * Compliance reporting mode
   * @return reportingMode
   */
  @javax.annotation.Nullable
  public ReportingModeEnum getReportingMode() {
    return reportingMode;
  }

  public void setReportingMode(ReportingModeEnum reportingMode) {
    this.reportingMode = reportingMode;
  }


  public GetAllSettings200ResponseDataSettings requireTimeSynchronization(Boolean requireTimeSynchronization) {
    this.requireTimeSynchronization = requireTimeSynchronization;
    return this;
  }

  /**
   * Require time synchronization between nodes and policy server
   * @return requireTimeSynchronization
   */
  @javax.annotation.Nullable
  public Boolean getRequireTimeSynchronization() {
    return requireTimeSynchronization;
  }

  public void setRequireTimeSynchronization(Boolean requireTimeSynchronization) {
    this.requireTimeSynchronization = requireTimeSynchronization;
  }


  public GetAllSettings200ResponseDataSettings rudderComputeChanges(Boolean rudderComputeChanges) {
    this.rudderComputeChanges = rudderComputeChanges;
    return this;
  }

  /**
   * Compute list of changes (repaired reports) per rule
   * @return rudderComputeChanges
   */
  @javax.annotation.Nullable
  public Boolean getRudderComputeChanges() {
    return rudderComputeChanges;
  }

  public void setRudderComputeChanges(Boolean rudderComputeChanges) {
    this.rudderComputeChanges = rudderComputeChanges;
  }


  public GetAllSettings200ResponseDataSettings rudderComputeDyngroupsMaxParallelism(String rudderComputeDyngroupsMaxParallelism) {
    this.rudderComputeDyngroupsMaxParallelism = rudderComputeDyngroupsMaxParallelism;
    return this;
  }

  /**
   * Set the parallelism to compute dynamic group, as a number of thread (i.e. 4), or a multiplicative of the number of core (x0.5)
   * @return rudderComputeDyngroupsMaxParallelism
   */
  @javax.annotation.Nullable
  public String getRudderComputeDyngroupsMaxParallelism() {
    return rudderComputeDyngroupsMaxParallelism;
  }

  public void setRudderComputeDyngroupsMaxParallelism(String rudderComputeDyngroupsMaxParallelism) {
    this.rudderComputeDyngroupsMaxParallelism = rudderComputeDyngroupsMaxParallelism;
  }


  public GetAllSettings200ResponseDataSettings rudderGenerationComputeDyngroups(Boolean rudderGenerationComputeDyngroups) {
    this.rudderGenerationComputeDyngroups = rudderGenerationComputeDyngroups;
    return this;
  }

  /**
   * Recompute all dynamic groups at the start of policy generation
   * @return rudderGenerationComputeDyngroups
   */
  @javax.annotation.Nullable
  public Boolean getRudderGenerationComputeDyngroups() {
    return rudderGenerationComputeDyngroups;
  }

  public void setRudderGenerationComputeDyngroups(Boolean rudderGenerationComputeDyngroups) {
    this.rudderGenerationComputeDyngroups = rudderGenerationComputeDyngroups;
  }


  public GetAllSettings200ResponseDataSettings rudderGenerationContinueOnError(Boolean rudderGenerationContinueOnError) {
    this.rudderGenerationContinueOnError = rudderGenerationContinueOnError;
    return this;
  }

  /**
   * Policy generation continues on error during NodeConfiguration evaluation
   * @return rudderGenerationContinueOnError
   */
  @javax.annotation.Nullable
  public Boolean getRudderGenerationContinueOnError() {
    return rudderGenerationContinueOnError;
  }

  public void setRudderGenerationContinueOnError(Boolean rudderGenerationContinueOnError) {
    this.rudderGenerationContinueOnError = rudderGenerationContinueOnError;
  }


  public GetAllSettings200ResponseDataSettings rudderGenerationDelay(String rudderGenerationDelay) {
    this.rudderGenerationDelay = rudderGenerationDelay;
    return this;
  }

  /**
   * Set a delay before starting policy generation, this will allow you to accumulate changes before they are deployed to Nodes, and can also lessen webapp resources needs. The value is a number followed by the time unit needed (seconds/s, minutes/m, hours/h ...), ie \&quot;5m\&quot; for 5 minutes
   * @return rudderGenerationDelay
   */
  @javax.annotation.Nullable
  public String getRudderGenerationDelay() {
    return rudderGenerationDelay;
  }

  public void setRudderGenerationDelay(String rudderGenerationDelay) {
    this.rudderGenerationDelay = rudderGenerationDelay;
  }


  public GetAllSettings200ResponseDataSettings rudderGenerationJsTimeout(Integer rudderGenerationJsTimeout) {
    this.rudderGenerationJsTimeout = rudderGenerationJsTimeout;
    return this;
  }

  /**
   * Policy generation JS evaluation of directive parameter timeout in seconds
   * @return rudderGenerationJsTimeout
   */
  @javax.annotation.Nullable
  public Integer getRudderGenerationJsTimeout() {
    return rudderGenerationJsTimeout;
  }

  public void setRudderGenerationJsTimeout(Integer rudderGenerationJsTimeout) {
    this.rudderGenerationJsTimeout = rudderGenerationJsTimeout;
  }


  public GetAllSettings200ResponseDataSettings rudderGenerationMaxParallelism(String rudderGenerationMaxParallelism) {
    this.rudderGenerationMaxParallelism = rudderGenerationMaxParallelism;
    return this;
  }

  /**
   * Set the policy generation parallelism, either as an number of thread (i.e. 4), or a multiplicative of the number of core (x0.5)
   * @return rudderGenerationMaxParallelism
   */
  @javax.annotation.Nullable
  public String getRudderGenerationMaxParallelism() {
    return rudderGenerationMaxParallelism;
  }

  public void setRudderGenerationMaxParallelism(String rudderGenerationMaxParallelism) {
    this.rudderGenerationMaxParallelism = rudderGenerationMaxParallelism;
  }


  public GetAllSettings200ResponseDataSettings rudderGenerationPolicy(String rudderGenerationPolicy) {
    this.rudderGenerationPolicy = rudderGenerationPolicy;
    return this;
  }

  /**
   * Should policy generation be triggered automatically after a change (value &#39;all&#39;), or should we wait until a manual launch (through api or UI, value &#39;onlyManual&#39;) or even no policy generation at all (value \&quot;none\&quot;)
   * @return rudderGenerationPolicy
   */
  @javax.annotation.Nullable
  public String getRudderGenerationPolicy() {
    return rudderGenerationPolicy;
  }

  public void setRudderGenerationPolicy(String rudderGenerationPolicy) {
    this.rudderGenerationPolicy = rudderGenerationPolicy;
  }


  public GetAllSettings200ResponseDataSettings rudderReportProtocolDefault(RudderReportProtocolDefaultEnum rudderReportProtocolDefault) {
    this.rudderReportProtocolDefault = rudderReportProtocolDefault;
    return this;
  }

  /**
   * Default reporting protocol used
   * @return rudderReportProtocolDefault
   */
  @javax.annotation.Nullable
  public RudderReportProtocolDefaultEnum getRudderReportProtocolDefault() {
    return rudderReportProtocolDefault;
  }

  public void setRudderReportProtocolDefault(RudderReportProtocolDefaultEnum rudderReportProtocolDefault) {
    this.rudderReportProtocolDefault = rudderReportProtocolDefault;
  }


  public GetAllSettings200ResponseDataSettings rudderSaveDbComplianceDetails(Boolean rudderSaveDbComplianceDetails) {
    this.rudderSaveDbComplianceDetails = rudderSaveDbComplianceDetails;
    return this;
  }

  /**
   * Store all compliance details in database
   * @return rudderSaveDbComplianceDetails
   */
  @javax.annotation.Nullable
  public Boolean getRudderSaveDbComplianceDetails() {
    return rudderSaveDbComplianceDetails;
  }

  public void setRudderSaveDbComplianceDetails(Boolean rudderSaveDbComplianceDetails) {
    this.rudderSaveDbComplianceDetails = rudderSaveDbComplianceDetails;
  }


  public GetAllSettings200ResponseDataSettings rudderSaveDbComplianceLevels(Boolean rudderSaveDbComplianceLevels) {
    this.rudderSaveDbComplianceLevels = rudderSaveDbComplianceLevels;
    return this;
  }

  /**
   * Store all compliance levels in database
   * @return rudderSaveDbComplianceLevels
   */
  @javax.annotation.Nullable
  public Boolean getRudderSaveDbComplianceLevels() {
    return rudderSaveDbComplianceLevels;
  }

  public void setRudderSaveDbComplianceLevels(Boolean rudderSaveDbComplianceLevels) {
    this.rudderSaveDbComplianceLevels = rudderSaveDbComplianceLevels;
  }


  public GetAllSettings200ResponseDataSettings rudderVerifyCertificates(Boolean rudderVerifyCertificates) {
    this.rudderVerifyCertificates = rudderVerifyCertificates;
    return this;
  }

  /**
   * Enforce certificate validation in all HTTPS calls
   * @return rudderVerifyCertificates
   */
  @javax.annotation.Nullable
  public Boolean getRudderVerifyCertificates() {
    return rudderVerifyCertificates;
  }

  public void setRudderVerifyCertificates(Boolean rudderVerifyCertificates) {
    this.rudderVerifyCertificates = rudderVerifyCertificates;
  }


  public GetAllSettings200ResponseDataSettings runFrequency(Integer runFrequency) {
    this.runFrequency = runFrequency;
    return this;
  }

  /**
   * Agent run schedule - time between agent runs (in minutes)
   * @return runFrequency
   */
  @javax.annotation.Nullable
  public Integer getRunFrequency() {
    return runFrequency;
  }

  public void setRunFrequency(Integer runFrequency) {
    this.runFrequency = runFrequency;
  }


  public GetAllSettings200ResponseDataSettings sendMetrics(String sendMetrics) {
    this.sendMetrics = sendMetrics;
    return this;
  }

  /**
   * Send anonymous usage statistics
   * @return sendMetrics
   */
  @javax.annotation.Nullable
  public String getSendMetrics() {
    return sendMetrics;
  }

  public void setSendMetrics(String sendMetrics) {
    this.sendMetrics = sendMetrics;
  }


  public GetAllSettings200ResponseDataSettings splayTime(Integer splayTime) {
    this.splayTime = splayTime;
    return this;
  }

  /**
   * Maximum delay after scheduled run time (random interval)
   * @return splayTime
   */
  @javax.annotation.Nullable
  public Integer getSplayTime() {
    return splayTime;
  }

  public void setSplayTime(Integer splayTime) {
    this.splayTime = splayTime;
  }


  public GetAllSettings200ResponseDataSettings unexpectedUnboundVarValues(Boolean unexpectedUnboundVarValues) {
    this.unexpectedUnboundVarValues = unexpectedUnboundVarValues;
    return this;
  }

  /**
   * Allows multiple reports for configuration based on a multivalued variable
   * @return unexpectedUnboundVarValues
   */
  @javax.annotation.Nullable
  public Boolean getUnexpectedUnboundVarValues() {
    return unexpectedUnboundVarValues;
  }

  public void setUnexpectedUnboundVarValues(Boolean unexpectedUnboundVarValues) {
    this.unexpectedUnboundVarValues = unexpectedUnboundVarValues;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetAllSettings200ResponseDataSettings getAllSettings200ResponseDataSettings = (GetAllSettings200ResponseDataSettings) o;
    return Objects.equals(this.allowedNetworks, getAllSettings200ResponseDataSettings.allowedNetworks) &&
        Objects.equals(this.changeMessagePrompt, getAllSettings200ResponseDataSettings.changeMessagePrompt) &&
        Objects.equals(this.displayRecentChangesGraphs, getAllSettings200ResponseDataSettings.displayRecentChangesGraphs) &&
        Objects.equals(this.enableChangeMessage, getAllSettings200ResponseDataSettings.enableChangeMessage) &&
        Objects.equals(this.enableChangeRequest, getAllSettings200ResponseDataSettings.enableChangeRequest) &&
        Objects.equals(this.enableJavascriptDirectives, getAllSettings200ResponseDataSettings.enableJavascriptDirectives) &&
        Objects.equals(this.enableSelfDeployment, getAllSettings200ResponseDataSettings.enableSelfDeployment) &&
        Objects.equals(this.enableSelfValidation, getAllSettings200ResponseDataSettings.enableSelfValidation) &&
        Objects.equals(this.firstRunHour, getAllSettings200ResponseDataSettings.firstRunHour) &&
        Objects.equals(this.firstRunMinute, getAllSettings200ResponseDataSettings.firstRunMinute) &&
        Objects.equals(this.globalPolicyMode, getAllSettings200ResponseDataSettings.globalPolicyMode) &&
        Objects.equals(this.globalPolicyModeOverridable, getAllSettings200ResponseDataSettings.globalPolicyModeOverridable) &&
        Objects.equals(this.heartbeatFrequency, getAllSettings200ResponseDataSettings.heartbeatFrequency) &&
        Objects.equals(this.mandatoryChangeMessage, getAllSettings200ResponseDataSettings.mandatoryChangeMessage) &&
        Objects.equals(this.modifiedFileTtl, getAllSettings200ResponseDataSettings.modifiedFileTtl) &&
        Objects.equals(this.nodeAcceptDuplicatedHostname, getAllSettings200ResponseDataSettings.nodeAcceptDuplicatedHostname) &&
        Objects.equals(this.nodeOnacceptDefaultPolicyMode, getAllSettings200ResponseDataSettings.nodeOnacceptDefaultPolicyMode) &&
        Objects.equals(this.nodeOnacceptDefaultState, getAllSettings200ResponseDataSettings.nodeOnacceptDefaultState) &&
        Objects.equals(this.outputFileTtl, getAllSettings200ResponseDataSettings.outputFileTtl) &&
        Objects.equals(this.relayServerSynchronizationMethod, getAllSettings200ResponseDataSettings.relayServerSynchronizationMethod) &&
        Objects.equals(this.relayServerSynchronizePolicies, getAllSettings200ResponseDataSettings.relayServerSynchronizePolicies) &&
        Objects.equals(this.relayServerSynchronizeSharedFiles, getAllSettings200ResponseDataSettings.relayServerSynchronizeSharedFiles) &&
        Objects.equals(this.reportingMode, getAllSettings200ResponseDataSettings.reportingMode) &&
        Objects.equals(this.requireTimeSynchronization, getAllSettings200ResponseDataSettings.requireTimeSynchronization) &&
        Objects.equals(this.rudderComputeChanges, getAllSettings200ResponseDataSettings.rudderComputeChanges) &&
        Objects.equals(this.rudderComputeDyngroupsMaxParallelism, getAllSettings200ResponseDataSettings.rudderComputeDyngroupsMaxParallelism) &&
        Objects.equals(this.rudderGenerationComputeDyngroups, getAllSettings200ResponseDataSettings.rudderGenerationComputeDyngroups) &&
        Objects.equals(this.rudderGenerationContinueOnError, getAllSettings200ResponseDataSettings.rudderGenerationContinueOnError) &&
        Objects.equals(this.rudderGenerationDelay, getAllSettings200ResponseDataSettings.rudderGenerationDelay) &&
        Objects.equals(this.rudderGenerationJsTimeout, getAllSettings200ResponseDataSettings.rudderGenerationJsTimeout) &&
        Objects.equals(this.rudderGenerationMaxParallelism, getAllSettings200ResponseDataSettings.rudderGenerationMaxParallelism) &&
        Objects.equals(this.rudderGenerationPolicy, getAllSettings200ResponseDataSettings.rudderGenerationPolicy) &&
        Objects.equals(this.rudderReportProtocolDefault, getAllSettings200ResponseDataSettings.rudderReportProtocolDefault) &&
        Objects.equals(this.rudderSaveDbComplianceDetails, getAllSettings200ResponseDataSettings.rudderSaveDbComplianceDetails) &&
        Objects.equals(this.rudderSaveDbComplianceLevels, getAllSettings200ResponseDataSettings.rudderSaveDbComplianceLevels) &&
        Objects.equals(this.rudderVerifyCertificates, getAllSettings200ResponseDataSettings.rudderVerifyCertificates) &&
        Objects.equals(this.runFrequency, getAllSettings200ResponseDataSettings.runFrequency) &&
        Objects.equals(this.sendMetrics, getAllSettings200ResponseDataSettings.sendMetrics) &&
        Objects.equals(this.splayTime, getAllSettings200ResponseDataSettings.splayTime) &&
        Objects.equals(this.unexpectedUnboundVarValues, getAllSettings200ResponseDataSettings.unexpectedUnboundVarValues);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowedNetworks, changeMessagePrompt, displayRecentChangesGraphs, enableChangeMessage, enableChangeRequest, enableJavascriptDirectives, enableSelfDeployment, enableSelfValidation, firstRunHour, firstRunMinute, globalPolicyMode, globalPolicyModeOverridable, heartbeatFrequency, mandatoryChangeMessage, modifiedFileTtl, nodeAcceptDuplicatedHostname, nodeOnacceptDefaultPolicyMode, nodeOnacceptDefaultState, outputFileTtl, relayServerSynchronizationMethod, relayServerSynchronizePolicies, relayServerSynchronizeSharedFiles, reportingMode, requireTimeSynchronization, rudderComputeChanges, rudderComputeDyngroupsMaxParallelism, rudderGenerationComputeDyngroups, rudderGenerationContinueOnError, rudderGenerationDelay, rudderGenerationJsTimeout, rudderGenerationMaxParallelism, rudderGenerationPolicy, rudderReportProtocolDefault, rudderSaveDbComplianceDetails, rudderSaveDbComplianceLevels, rudderVerifyCertificates, runFrequency, sendMetrics, splayTime, unexpectedUnboundVarValues);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetAllSettings200ResponseDataSettings {\n");
    sb.append("    allowedNetworks: ").append(toIndentedString(allowedNetworks)).append("\n");
    sb.append("    changeMessagePrompt: ").append(toIndentedString(changeMessagePrompt)).append("\n");
    sb.append("    displayRecentChangesGraphs: ").append(toIndentedString(displayRecentChangesGraphs)).append("\n");
    sb.append("    enableChangeMessage: ").append(toIndentedString(enableChangeMessage)).append("\n");
    sb.append("    enableChangeRequest: ").append(toIndentedString(enableChangeRequest)).append("\n");
    sb.append("    enableJavascriptDirectives: ").append(toIndentedString(enableJavascriptDirectives)).append("\n");
    sb.append("    enableSelfDeployment: ").append(toIndentedString(enableSelfDeployment)).append("\n");
    sb.append("    enableSelfValidation: ").append(toIndentedString(enableSelfValidation)).append("\n");
    sb.append("    firstRunHour: ").append(toIndentedString(firstRunHour)).append("\n");
    sb.append("    firstRunMinute: ").append(toIndentedString(firstRunMinute)).append("\n");
    sb.append("    globalPolicyMode: ").append(toIndentedString(globalPolicyMode)).append("\n");
    sb.append("    globalPolicyModeOverridable: ").append(toIndentedString(globalPolicyModeOverridable)).append("\n");
    sb.append("    heartbeatFrequency: ").append(toIndentedString(heartbeatFrequency)).append("\n");
    sb.append("    mandatoryChangeMessage: ").append(toIndentedString(mandatoryChangeMessage)).append("\n");
    sb.append("    modifiedFileTtl: ").append(toIndentedString(modifiedFileTtl)).append("\n");
    sb.append("    nodeAcceptDuplicatedHostname: ").append(toIndentedString(nodeAcceptDuplicatedHostname)).append("\n");
    sb.append("    nodeOnacceptDefaultPolicyMode: ").append(toIndentedString(nodeOnacceptDefaultPolicyMode)).append("\n");
    sb.append("    nodeOnacceptDefaultState: ").append(toIndentedString(nodeOnacceptDefaultState)).append("\n");
    sb.append("    outputFileTtl: ").append(toIndentedString(outputFileTtl)).append("\n");
    sb.append("    relayServerSynchronizationMethod: ").append(toIndentedString(relayServerSynchronizationMethod)).append("\n");
    sb.append("    relayServerSynchronizePolicies: ").append(toIndentedString(relayServerSynchronizePolicies)).append("\n");
    sb.append("    relayServerSynchronizeSharedFiles: ").append(toIndentedString(relayServerSynchronizeSharedFiles)).append("\n");
    sb.append("    reportingMode: ").append(toIndentedString(reportingMode)).append("\n");
    sb.append("    requireTimeSynchronization: ").append(toIndentedString(requireTimeSynchronization)).append("\n");
    sb.append("    rudderComputeChanges: ").append(toIndentedString(rudderComputeChanges)).append("\n");
    sb.append("    rudderComputeDyngroupsMaxParallelism: ").append(toIndentedString(rudderComputeDyngroupsMaxParallelism)).append("\n");
    sb.append("    rudderGenerationComputeDyngroups: ").append(toIndentedString(rudderGenerationComputeDyngroups)).append("\n");
    sb.append("    rudderGenerationContinueOnError: ").append(toIndentedString(rudderGenerationContinueOnError)).append("\n");
    sb.append("    rudderGenerationDelay: ").append(toIndentedString(rudderGenerationDelay)).append("\n");
    sb.append("    rudderGenerationJsTimeout: ").append(toIndentedString(rudderGenerationJsTimeout)).append("\n");
    sb.append("    rudderGenerationMaxParallelism: ").append(toIndentedString(rudderGenerationMaxParallelism)).append("\n");
    sb.append("    rudderGenerationPolicy: ").append(toIndentedString(rudderGenerationPolicy)).append("\n");
    sb.append("    rudderReportProtocolDefault: ").append(toIndentedString(rudderReportProtocolDefault)).append("\n");
    sb.append("    rudderSaveDbComplianceDetails: ").append(toIndentedString(rudderSaveDbComplianceDetails)).append("\n");
    sb.append("    rudderSaveDbComplianceLevels: ").append(toIndentedString(rudderSaveDbComplianceLevels)).append("\n");
    sb.append("    rudderVerifyCertificates: ").append(toIndentedString(rudderVerifyCertificates)).append("\n");
    sb.append("    runFrequency: ").append(toIndentedString(runFrequency)).append("\n");
    sb.append("    sendMetrics: ").append(toIndentedString(sendMetrics)).append("\n");
    sb.append("    splayTime: ").append(toIndentedString(splayTime)).append("\n");
    sb.append("    unexpectedUnboundVarValues: ").append(toIndentedString(unexpectedUnboundVarValues)).append("\n");
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
    openapiFields.add("allowed_networks");
    openapiFields.add("change_message_prompt");
    openapiFields.add("display_recent_changes_graphs");
    openapiFields.add("enable_change_message");
    openapiFields.add("enable_change_request");
    openapiFields.add("enable_javascript_directives");
    openapiFields.add("enable_self_deployment");
    openapiFields.add("enable_self_validation");
    openapiFields.add("first_run_hour");
    openapiFields.add("first_run_minute");
    openapiFields.add("global_policy_mode");
    openapiFields.add("global_policy_mode_overridable");
    openapiFields.add("heartbeat_frequency");
    openapiFields.add("mandatory_change_message");
    openapiFields.add("modified_file_ttl");
    openapiFields.add("node_accept_duplicated_hostname");
    openapiFields.add("node_onaccept_default_policyMode");
    openapiFields.add("node_onaccept_default_state");
    openapiFields.add("output_file_ttl");
    openapiFields.add("relay_server_synchronization_method");
    openapiFields.add("relay_server_synchronize_policies");
    openapiFields.add("relay_server_synchronize_shared_files");
    openapiFields.add("reporting_mode");
    openapiFields.add("require_time_synchronization");
    openapiFields.add("rudder_compute_changes");
    openapiFields.add("rudder_compute_dyngroups_max_parallelism");
    openapiFields.add("rudder_generation_compute_dyngroups");
    openapiFields.add("rudder_generation_continue_on_error");
    openapiFields.add("rudder_generation_delay");
    openapiFields.add("rudder_generation_js_timeout");
    openapiFields.add("rudder_generation_max_parallelism");
    openapiFields.add("rudder_generation_policy");
    openapiFields.add("rudder_report_protocol_default");
    openapiFields.add("rudder_save_db_compliance_details");
    openapiFields.add("rudder_save_db_compliance_levels");
    openapiFields.add("rudder_verify_certificates");
    openapiFields.add("run_frequency");
    openapiFields.add("send_metrics");
    openapiFields.add("splay_time");
    openapiFields.add("unexpected_unbound_var_values");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetAllSettings200ResponseDataSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetAllSettings200ResponseDataSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetAllSettings200ResponseDataSettings is not found in the empty JSON string", GetAllSettings200ResponseDataSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetAllSettings200ResponseDataSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetAllSettings200ResponseDataSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("allowed_networks") != null && !jsonObj.get("allowed_networks").isJsonNull()) {
        JsonArray jsonArrayallowedNetworks = jsonObj.getAsJsonArray("allowed_networks");
        if (jsonArrayallowedNetworks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("allowed_networks").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `allowed_networks` to be an array in the JSON string but got `%s`", jsonObj.get("allowed_networks").toString()));
          }

          // validate the optional field `allowed_networks` (array)
          for (int i = 0; i < jsonArrayallowedNetworks.size(); i++) {
            GetAllSettings200ResponseDataSettingsAllowedNetworksInner.validateJsonElement(jsonArrayallowedNetworks.get(i));
          };
        }
      }
      if ((jsonObj.get("change_message_prompt") != null && !jsonObj.get("change_message_prompt").isJsonNull()) && !jsonObj.get("change_message_prompt").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `change_message_prompt` to be a primitive type in the JSON string but got `%s`", jsonObj.get("change_message_prompt").toString()));
      }
      if ((jsonObj.get("enable_javascript_directives") != null && !jsonObj.get("enable_javascript_directives").isJsonNull()) && !jsonObj.get("enable_javascript_directives").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `enable_javascript_directives` to be a primitive type in the JSON string but got `%s`", jsonObj.get("enable_javascript_directives").toString()));
      }
      if ((jsonObj.get("global_policy_mode") != null && !jsonObj.get("global_policy_mode").isJsonNull()) && !jsonObj.get("global_policy_mode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `global_policy_mode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("global_policy_mode").toString()));
      }
      // validate the optional field `global_policy_mode`
      if (jsonObj.get("global_policy_mode") != null && !jsonObj.get("global_policy_mode").isJsonNull()) {
        GlobalPolicyModeEnum.validateJsonElement(jsonObj.get("global_policy_mode"));
      }
      if ((jsonObj.get("node_onaccept_default_policyMode") != null && !jsonObj.get("node_onaccept_default_policyMode").isJsonNull()) && !jsonObj.get("node_onaccept_default_policyMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `node_onaccept_default_policyMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("node_onaccept_default_policyMode").toString()));
      }
      // validate the optional field `node_onaccept_default_policyMode`
      if (jsonObj.get("node_onaccept_default_policyMode") != null && !jsonObj.get("node_onaccept_default_policyMode").isJsonNull()) {
        NodeOnacceptDefaultPolicyModeEnum.validateJsonElement(jsonObj.get("node_onaccept_default_policyMode"));
      }
      if ((jsonObj.get("node_onaccept_default_state") != null && !jsonObj.get("node_onaccept_default_state").isJsonNull()) && !jsonObj.get("node_onaccept_default_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `node_onaccept_default_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("node_onaccept_default_state").toString()));
      }
      // validate the optional field `node_onaccept_default_state`
      if (jsonObj.get("node_onaccept_default_state") != null && !jsonObj.get("node_onaccept_default_state").isJsonNull()) {
        NodeOnacceptDefaultStateEnum.validateJsonElement(jsonObj.get("node_onaccept_default_state"));
      }
      if ((jsonObj.get("relay_server_synchronization_method") != null && !jsonObj.get("relay_server_synchronization_method").isJsonNull()) && !jsonObj.get("relay_server_synchronization_method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `relay_server_synchronization_method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("relay_server_synchronization_method").toString()));
      }
      // validate the optional field `relay_server_synchronization_method`
      if (jsonObj.get("relay_server_synchronization_method") != null && !jsonObj.get("relay_server_synchronization_method").isJsonNull()) {
        RelayServerSynchronizationMethodEnum.validateJsonElement(jsonObj.get("relay_server_synchronization_method"));
      }
      if ((jsonObj.get("reporting_mode") != null && !jsonObj.get("reporting_mode").isJsonNull()) && !jsonObj.get("reporting_mode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reporting_mode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reporting_mode").toString()));
      }
      // validate the optional field `reporting_mode`
      if (jsonObj.get("reporting_mode") != null && !jsonObj.get("reporting_mode").isJsonNull()) {
        ReportingModeEnum.validateJsonElement(jsonObj.get("reporting_mode"));
      }
      if ((jsonObj.get("rudder_compute_dyngroups_max_parallelism") != null && !jsonObj.get("rudder_compute_dyngroups_max_parallelism").isJsonNull()) && !jsonObj.get("rudder_compute_dyngroups_max_parallelism").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rudder_compute_dyngroups_max_parallelism` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rudder_compute_dyngroups_max_parallelism").toString()));
      }
      if ((jsonObj.get("rudder_generation_delay") != null && !jsonObj.get("rudder_generation_delay").isJsonNull()) && !jsonObj.get("rudder_generation_delay").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rudder_generation_delay` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rudder_generation_delay").toString()));
      }
      if ((jsonObj.get("rudder_generation_max_parallelism") != null && !jsonObj.get("rudder_generation_max_parallelism").isJsonNull()) && !jsonObj.get("rudder_generation_max_parallelism").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rudder_generation_max_parallelism` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rudder_generation_max_parallelism").toString()));
      }
      if ((jsonObj.get("rudder_generation_policy") != null && !jsonObj.get("rudder_generation_policy").isJsonNull()) && !jsonObj.get("rudder_generation_policy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rudder_generation_policy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rudder_generation_policy").toString()));
      }
      if ((jsonObj.get("rudder_report_protocol_default") != null && !jsonObj.get("rudder_report_protocol_default").isJsonNull()) && !jsonObj.get("rudder_report_protocol_default").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rudder_report_protocol_default` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rudder_report_protocol_default").toString()));
      }
      // validate the optional field `rudder_report_protocol_default`
      if (jsonObj.get("rudder_report_protocol_default") != null && !jsonObj.get("rudder_report_protocol_default").isJsonNull()) {
        RudderReportProtocolDefaultEnum.validateJsonElement(jsonObj.get("rudder_report_protocol_default"));
      }
      if ((jsonObj.get("send_metrics") != null && !jsonObj.get("send_metrics").isJsonNull()) && !jsonObj.get("send_metrics").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `send_metrics` to be a primitive type in the JSON string but got `%s`", jsonObj.get("send_metrics").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetAllSettings200ResponseDataSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetAllSettings200ResponseDataSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetAllSettings200ResponseDataSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetAllSettings200ResponseDataSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<GetAllSettings200ResponseDataSettings>() {
           @Override
           public void write(JsonWriter out, GetAllSettings200ResponseDataSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetAllSettings200ResponseDataSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetAllSettings200ResponseDataSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetAllSettings200ResponseDataSettings
   * @throws IOException if the JSON string is invalid with respect to GetAllSettings200ResponseDataSettings
   */
  public static GetAllSettings200ResponseDataSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetAllSettings200ResponseDataSettings.class);
  }

  /**
   * Convert an instance of GetAllSettings200ResponseDataSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

