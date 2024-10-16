/*
 * Runscope API
 * Manage Runscope programmatically.
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
import org.openapitools.client.model.Agent;
import org.openapitools.client.model.Integration;

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
 * Environment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:55.705127-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Environment {
  public static final String SERIALIZED_NAME_AUTH = "auth";
  @SerializedName(SERIALIZED_NAME_AUTH)
  private String auth;

  public static final String SERIALIZED_NAME_CLIENT_CERTIFICATE = "client_certificate";
  @SerializedName(SERIALIZED_NAME_CLIENT_CERTIFICATE)
  private String clientCertificate;

  public static final String SERIALIZED_NAME_EMAILS = "emails";
  @SerializedName(SERIALIZED_NAME_EMAILS)
  private Object emails;

  public static final String SERIALIZED_NAME_EXPORTED_AT = "exported_at";
  @SerializedName(SERIALIZED_NAME_EXPORTED_AT)
  private Integer exportedAt;

  public static final String SERIALIZED_NAME_HEADERS = "headers";
  @SerializedName(SERIALIZED_NAME_HEADERS)
  private Object headers;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INITIAL_SCRIPT_HASH = "initial_script_hash";
  @SerializedName(SERIALIZED_NAME_INITIAL_SCRIPT_HASH)
  private String initialScriptHash;

  public static final String SERIALIZED_NAME_INITIAL_VARIABLES = "initial_variables";
  @SerializedName(SERIALIZED_NAME_INITIAL_VARIABLES)
  private Object initialVariables;

  public static final String SERIALIZED_NAME_INTEGRATIONS = "integrations";
  @SerializedName(SERIALIZED_NAME_INTEGRATIONS)
  private List<Integration> integrations = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PARENT_ENVIRONMENT_ID = "parent_environment_id";
  @SerializedName(SERIALIZED_NAME_PARENT_ENVIRONMENT_ID)
  private String parentEnvironmentId;

  public static final String SERIALIZED_NAME_PRESERVE_COOKIES = "preserve_cookies";
  @SerializedName(SERIALIZED_NAME_PRESERVE_COOKIES)
  private Boolean preserveCookies;

  public static final String SERIALIZED_NAME_REGIONS = "regions";
  @SerializedName(SERIALIZED_NAME_REGIONS)
  private List<String> regions = new ArrayList<>();

  public static final String SERIALIZED_NAME_REMOTE_AGENTS = "remote_agents";
  @SerializedName(SERIALIZED_NAME_REMOTE_AGENTS)
  private List<Agent> remoteAgents = new ArrayList<>();

  public static final String SERIALIZED_NAME_RETRY_ON_FAILURE = "retry_on_failure";
  @SerializedName(SERIALIZED_NAME_RETRY_ON_FAILURE)
  private Boolean retryOnFailure;

  public static final String SERIALIZED_NAME_SCRIPT = "script";
  @SerializedName(SERIALIZED_NAME_SCRIPT)
  private String script;

  public static final String SERIALIZED_NAME_SCRIPT_LIBRARY = "script_library";
  @SerializedName(SERIALIZED_NAME_SCRIPT_LIBRARY)
  private List<String> scriptLibrary = new ArrayList<>();

  public static final String SERIALIZED_NAME_STOP_ON_FAILURE = "stop_on_failure";
  @SerializedName(SERIALIZED_NAME_STOP_ON_FAILURE)
  private Boolean stopOnFailure;

  public static final String SERIALIZED_NAME_TEST_ID = "test_id";
  @SerializedName(SERIALIZED_NAME_TEST_ID)
  private String testId;

  public static final String SERIALIZED_NAME_VERIFY_SSL = "verify_ssl";
  @SerializedName(SERIALIZED_NAME_VERIFY_SSL)
  private Boolean verifySsl;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public static final String SERIALIZED_NAME_WEBHOOKS = "webhooks";
  @SerializedName(SERIALIZED_NAME_WEBHOOKS)
  private String webhooks;

  public Environment() {
  }

  public Environment auth(String auth) {
    this.auth = auth;
    return this;
  }

  /**
   * Get auth
   * @return auth
   */
  @javax.annotation.Nullable
  public String getAuth() {
    return auth;
  }

  public void setAuth(String auth) {
    this.auth = auth;
  }


  public Environment clientCertificate(String clientCertificate) {
    this.clientCertificate = clientCertificate;
    return this;
  }

  /**
   * Get clientCertificate
   * @return clientCertificate
   */
  @javax.annotation.Nullable
  public String getClientCertificate() {
    return clientCertificate;
  }

  public void setClientCertificate(String clientCertificate) {
    this.clientCertificate = clientCertificate;
  }


  public Environment emails(Object emails) {
    this.emails = emails;
    return this;
  }

  /**
   * Get emails
   * @return emails
   */
  @javax.annotation.Nullable
  public Object getEmails() {
    return emails;
  }

  public void setEmails(Object emails) {
    this.emails = emails;
  }


  public Environment exportedAt(Integer exportedAt) {
    this.exportedAt = exportedAt;
    return this;
  }

  /**
   * Get exportedAt
   * @return exportedAt
   */
  @javax.annotation.Nullable
  public Integer getExportedAt() {
    return exportedAt;
  }

  public void setExportedAt(Integer exportedAt) {
    this.exportedAt = exportedAt;
  }


  public Environment headers(Object headers) {
    this.headers = headers;
    return this;
  }

  /**
   * Get headers
   * @return headers
   */
  @javax.annotation.Nullable
  public Object getHeaders() {
    return headers;
  }

  public void setHeaders(Object headers) {
    this.headers = headers;
  }


  public Environment id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The unique identifier for this environment.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Environment initialScriptHash(String initialScriptHash) {
    this.initialScriptHash = initialScriptHash;
    return this;
  }

  /**
   * Get initialScriptHash
   * @return initialScriptHash
   */
  @javax.annotation.Nullable
  public String getInitialScriptHash() {
    return initialScriptHash;
  }

  public void setInitialScriptHash(String initialScriptHash) {
    this.initialScriptHash = initialScriptHash;
  }


  public Environment initialVariables(Object initialVariables) {
    this.initialVariables = initialVariables;
    return this;
  }

  /**
   * Get initialVariables
   * @return initialVariables
   */
  @javax.annotation.Nullable
  public Object getInitialVariables() {
    return initialVariables;
  }

  public void setInitialVariables(Object initialVariables) {
    this.initialVariables = initialVariables;
  }


  public Environment integrations(List<Integration> integrations) {
    this.integrations = integrations;
    return this;
  }

  public Environment addIntegrationsItem(Integration integrationsItem) {
    if (this.integrations == null) {
      this.integrations = new ArrayList<>();
    }
    this.integrations.add(integrationsItem);
    return this;
  }

  /**
   * The list of integrations for this environment.
   * @return integrations
   */
  @javax.annotation.Nullable
  public List<Integration> getIntegrations() {
    return integrations;
  }

  public void setIntegrations(List<Integration> integrations) {
    this.integrations = integrations;
  }


  public Environment name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of this environment.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Environment parentEnvironmentId(String parentEnvironmentId) {
    this.parentEnvironmentId = parentEnvironmentId;
    return this;
  }

  /**
   * Get parentEnvironmentId
   * @return parentEnvironmentId
   */
  @javax.annotation.Nullable
  public String getParentEnvironmentId() {
    return parentEnvironmentId;
  }

  public void setParentEnvironmentId(String parentEnvironmentId) {
    this.parentEnvironmentId = parentEnvironmentId;
  }


  public Environment preserveCookies(Boolean preserveCookies) {
    this.preserveCookies = preserveCookies;
    return this;
  }

  /**
   * Get preserveCookies
   * @return preserveCookies
   */
  @javax.annotation.Nullable
  public Boolean getPreserveCookies() {
    return preserveCookies;
  }

  public void setPreserveCookies(Boolean preserveCookies) {
    this.preserveCookies = preserveCookies;
  }


  public Environment regions(List<String> regions) {
    this.regions = regions;
    return this;
  }

  public Environment addRegionsItem(String regionsItem) {
    if (this.regions == null) {
      this.regions = new ArrayList<>();
    }
    this.regions.add(regionsItem);
    return this;
  }

  /**
   * An array of the region codes that this environment is using.
   * @return regions
   */
  @javax.annotation.Nullable
  public List<String> getRegions() {
    return regions;
  }

  public void setRegions(List<String> regions) {
    this.regions = regions;
  }


  public Environment remoteAgents(List<Agent> remoteAgents) {
    this.remoteAgents = remoteAgents;
    return this;
  }

  public Environment addRemoteAgentsItem(Agent remoteAgentsItem) {
    if (this.remoteAgents == null) {
      this.remoteAgents = new ArrayList<>();
    }
    this.remoteAgents.add(remoteAgentsItem);
    return this;
  }

  /**
   * Get remoteAgents
   * @return remoteAgents
   */
  @javax.annotation.Nullable
  public List<Agent> getRemoteAgents() {
    return remoteAgents;
  }

  public void setRemoteAgents(List<Agent> remoteAgents) {
    this.remoteAgents = remoteAgents;
  }


  public Environment retryOnFailure(Boolean retryOnFailure) {
    this.retryOnFailure = retryOnFailure;
    return this;
  }

  /**
   * Get retryOnFailure
   * @return retryOnFailure
   */
  @javax.annotation.Nullable
  public Boolean getRetryOnFailure() {
    return retryOnFailure;
  }

  public void setRetryOnFailure(Boolean retryOnFailure) {
    this.retryOnFailure = retryOnFailure;
  }


  public Environment script(String script) {
    this.script = script;
    return this;
  }

  /**
   * 
   * @return script
   */
  @javax.annotation.Nullable
  public String getScript() {
    return script;
  }

  public void setScript(String script) {
    this.script = script;
  }


  public Environment scriptLibrary(List<String> scriptLibrary) {
    this.scriptLibrary = scriptLibrary;
    return this;
  }

  public Environment addScriptLibraryItem(String scriptLibraryItem) {
    if (this.scriptLibrary == null) {
      this.scriptLibrary = new ArrayList<>();
    }
    this.scriptLibrary.add(scriptLibraryItem);
    return this;
  }

  /**
   * The list of ids for scripts, part of the script libraries, being used for this environment.
   * @return scriptLibrary
   */
  @javax.annotation.Nullable
  public List<String> getScriptLibrary() {
    return scriptLibrary;
  }

  public void setScriptLibrary(List<String> scriptLibrary) {
    this.scriptLibrary = scriptLibrary;
  }


  public Environment stopOnFailure(Boolean stopOnFailure) {
    this.stopOnFailure = stopOnFailure;
    return this;
  }

  /**
   * Stop executing the test after the first failed step.
   * @return stopOnFailure
   */
  @javax.annotation.Nullable
  public Boolean getStopOnFailure() {
    return stopOnFailure;
  }

  public void setStopOnFailure(Boolean stopOnFailure) {
    this.stopOnFailure = stopOnFailure;
  }


  public Environment testId(String testId) {
    this.testId = testId;
    return this;
  }

  /**
   * The unique identifier for this test.
   * @return testId
   */
  @javax.annotation.Nullable
  public String getTestId() {
    return testId;
  }

  public void setTestId(String testId) {
    this.testId = testId;
  }


  public Environment verifySsl(Boolean verifySsl) {
    this.verifySsl = verifySsl;
    return this;
  }

  /**
   * Validate all SSL certificates on any HTTPS connections.
   * @return verifySsl
   */
  @javax.annotation.Nullable
  public Boolean getVerifySsl() {
    return verifySsl;
  }

  public void setVerifySsl(Boolean verifySsl) {
    this.verifySsl = verifySsl;
  }


  public Environment version(String version) {
    this.version = version;
    return this;
  }

  /**
   * Get version
   * @return version
   */
  @javax.annotation.Nullable
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }


  public Environment webhooks(String webhooks) {
    this.webhooks = webhooks;
    return this;
  }

  /**
   * Get webhooks
   * @return webhooks
   */
  @javax.annotation.Nullable
  public String getWebhooks() {
    return webhooks;
  }

  public void setWebhooks(String webhooks) {
    this.webhooks = webhooks;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Environment environment = (Environment) o;
    return Objects.equals(this.auth, environment.auth) &&
        Objects.equals(this.clientCertificate, environment.clientCertificate) &&
        Objects.equals(this.emails, environment.emails) &&
        Objects.equals(this.exportedAt, environment.exportedAt) &&
        Objects.equals(this.headers, environment.headers) &&
        Objects.equals(this.id, environment.id) &&
        Objects.equals(this.initialScriptHash, environment.initialScriptHash) &&
        Objects.equals(this.initialVariables, environment.initialVariables) &&
        Objects.equals(this.integrations, environment.integrations) &&
        Objects.equals(this.name, environment.name) &&
        Objects.equals(this.parentEnvironmentId, environment.parentEnvironmentId) &&
        Objects.equals(this.preserveCookies, environment.preserveCookies) &&
        Objects.equals(this.regions, environment.regions) &&
        Objects.equals(this.remoteAgents, environment.remoteAgents) &&
        Objects.equals(this.retryOnFailure, environment.retryOnFailure) &&
        Objects.equals(this.script, environment.script) &&
        Objects.equals(this.scriptLibrary, environment.scriptLibrary) &&
        Objects.equals(this.stopOnFailure, environment.stopOnFailure) &&
        Objects.equals(this.testId, environment.testId) &&
        Objects.equals(this.verifySsl, environment.verifySsl) &&
        Objects.equals(this.version, environment.version) &&
        Objects.equals(this.webhooks, environment.webhooks);
  }

  @Override
  public int hashCode() {
    return Objects.hash(auth, clientCertificate, emails, exportedAt, headers, id, initialScriptHash, initialVariables, integrations, name, parentEnvironmentId, preserveCookies, regions, remoteAgents, retryOnFailure, script, scriptLibrary, stopOnFailure, testId, verifySsl, version, webhooks);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Environment {\n");
    sb.append("    auth: ").append(toIndentedString(auth)).append("\n");
    sb.append("    clientCertificate: ").append(toIndentedString(clientCertificate)).append("\n");
    sb.append("    emails: ").append(toIndentedString(emails)).append("\n");
    sb.append("    exportedAt: ").append(toIndentedString(exportedAt)).append("\n");
    sb.append("    headers: ").append(toIndentedString(headers)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    initialScriptHash: ").append(toIndentedString(initialScriptHash)).append("\n");
    sb.append("    initialVariables: ").append(toIndentedString(initialVariables)).append("\n");
    sb.append("    integrations: ").append(toIndentedString(integrations)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    parentEnvironmentId: ").append(toIndentedString(parentEnvironmentId)).append("\n");
    sb.append("    preserveCookies: ").append(toIndentedString(preserveCookies)).append("\n");
    sb.append("    regions: ").append(toIndentedString(regions)).append("\n");
    sb.append("    remoteAgents: ").append(toIndentedString(remoteAgents)).append("\n");
    sb.append("    retryOnFailure: ").append(toIndentedString(retryOnFailure)).append("\n");
    sb.append("    script: ").append(toIndentedString(script)).append("\n");
    sb.append("    scriptLibrary: ").append(toIndentedString(scriptLibrary)).append("\n");
    sb.append("    stopOnFailure: ").append(toIndentedString(stopOnFailure)).append("\n");
    sb.append("    testId: ").append(toIndentedString(testId)).append("\n");
    sb.append("    verifySsl: ").append(toIndentedString(verifySsl)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    webhooks: ").append(toIndentedString(webhooks)).append("\n");
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
    openapiFields.add("auth");
    openapiFields.add("client_certificate");
    openapiFields.add("emails");
    openapiFields.add("exported_at");
    openapiFields.add("headers");
    openapiFields.add("id");
    openapiFields.add("initial_script_hash");
    openapiFields.add("initial_variables");
    openapiFields.add("integrations");
    openapiFields.add("name");
    openapiFields.add("parent_environment_id");
    openapiFields.add("preserve_cookies");
    openapiFields.add("regions");
    openapiFields.add("remote_agents");
    openapiFields.add("retry_on_failure");
    openapiFields.add("script");
    openapiFields.add("script_library");
    openapiFields.add("stop_on_failure");
    openapiFields.add("test_id");
    openapiFields.add("verify_ssl");
    openapiFields.add("version");
    openapiFields.add("webhooks");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Environment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Environment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Environment is not found in the empty JSON string", Environment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Environment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Environment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Environment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("auth") != null && !jsonObj.get("auth").isJsonNull()) && !jsonObj.get("auth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auth").toString()));
      }
      if ((jsonObj.get("client_certificate") != null && !jsonObj.get("client_certificate").isJsonNull()) && !jsonObj.get("client_certificate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `client_certificate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("client_certificate").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("initial_script_hash") != null && !jsonObj.get("initial_script_hash").isJsonNull()) && !jsonObj.get("initial_script_hash").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `initial_script_hash` to be a primitive type in the JSON string but got `%s`", jsonObj.get("initial_script_hash").toString()));
      }
      if (jsonObj.get("integrations") != null && !jsonObj.get("integrations").isJsonNull()) {
        JsonArray jsonArrayintegrations = jsonObj.getAsJsonArray("integrations");
        if (jsonArrayintegrations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("integrations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `integrations` to be an array in the JSON string but got `%s`", jsonObj.get("integrations").toString()));
          }

          // validate the optional field `integrations` (array)
          for (int i = 0; i < jsonArrayintegrations.size(); i++) {
            Integration.validateJsonElement(jsonArrayintegrations.get(i));
          };
        }
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("parent_environment_id") != null && !jsonObj.get("parent_environment_id").isJsonNull()) && !jsonObj.get("parent_environment_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parent_environment_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parent_environment_id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("regions") != null && !jsonObj.get("regions").isJsonNull() && !jsonObj.get("regions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `regions` to be an array in the JSON string but got `%s`", jsonObj.get("regions").toString()));
      }
      if (jsonObj.get("remote_agents") != null && !jsonObj.get("remote_agents").isJsonNull()) {
        JsonArray jsonArrayremoteAgents = jsonObj.getAsJsonArray("remote_agents");
        if (jsonArrayremoteAgents != null) {
          // ensure the json data is an array
          if (!jsonObj.get("remote_agents").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `remote_agents` to be an array in the JSON string but got `%s`", jsonObj.get("remote_agents").toString()));
          }

          // validate the optional field `remote_agents` (array)
          for (int i = 0; i < jsonArrayremoteAgents.size(); i++) {
            Agent.validateJsonElement(jsonArrayremoteAgents.get(i));
          };
        }
      }
      if ((jsonObj.get("script") != null && !jsonObj.get("script").isJsonNull()) && !jsonObj.get("script").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `script` to be a primitive type in the JSON string but got `%s`", jsonObj.get("script").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("script_library") != null && !jsonObj.get("script_library").isJsonNull() && !jsonObj.get("script_library").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `script_library` to be an array in the JSON string but got `%s`", jsonObj.get("script_library").toString()));
      }
      if ((jsonObj.get("test_id") != null && !jsonObj.get("test_id").isJsonNull()) && !jsonObj.get("test_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `test_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("test_id").toString()));
      }
      if ((jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
      if ((jsonObj.get("webhooks") != null && !jsonObj.get("webhooks").isJsonNull()) && !jsonObj.get("webhooks").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `webhooks` to be a primitive type in the JSON string but got `%s`", jsonObj.get("webhooks").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Environment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Environment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Environment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Environment.class));

       return (TypeAdapter<T>) new TypeAdapter<Environment>() {
           @Override
           public void write(JsonWriter out, Environment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Environment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Environment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Environment
   * @throws IOException if the JSON string is invalid with respect to Environment
   */
  public static Environment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Environment.class);
  }

  /**
   * Convert an instance of Environment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

