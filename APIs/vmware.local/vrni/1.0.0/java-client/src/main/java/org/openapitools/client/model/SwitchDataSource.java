/*
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
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
import java.util.Arrays;
import org.openapitools.client.model.BaseDataSource;
import org.openapitools.client.model.DataSourceType;
import org.openapitools.client.model.PasswordCredentials;

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
 * SwitchDataSource
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:28.864194-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SwitchDataSource extends BaseDataSource {
  public static final String SERIALIZED_NAME_CREDENTIALS = "credentials";
  @SerializedName(SERIALIZED_NAME_CREDENTIALS)
  private PasswordCredentials credentials;

  public SwitchDataSource() {
    this.entityType = this.getClass().getSimpleName();
  }

  public SwitchDataSource credentials(PasswordCredentials credentials) {
    this.credentials = credentials;
    return this;
  }

  /**
   * Get credentials
   * @return credentials
   */
  @javax.annotation.Nullable
  public PasswordCredentials getCredentials() {
    return credentials;
  }

  public void setCredentials(PasswordCredentials credentials) {
    this.credentials = credentials;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SwitchDataSource switchDataSource = (SwitchDataSource) o;
    return Objects.equals(this.credentials, switchDataSource.credentials) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(credentials, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SwitchDataSource {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    credentials: ").append(toIndentedString(credentials)).append("\n");
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
    openapiFields.add("enabled");
    openapiFields.add("entity_id");
    openapiFields.add("entity_type");
    openapiFields.add("fqdn");
    openapiFields.add("ip");
    openapiFields.add("nickname");
    openapiFields.add("notes");
    openapiFields.add("proxy_id");
    openapiFields.add("credentials");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SwitchDataSource
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SwitchDataSource.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SwitchDataSource is not found in the empty JSON string", SwitchDataSource.openapiRequiredFields.toString()));
        }
      }

      String discriminatorValue = jsonElement.getAsJsonObject().get("entity_type").getAsString();
      switch (discriminatorValue) {
        case "AristaSwitchDataSource":
          AristaSwitchDataSource.validateJsonElement(jsonElement);
          break;
        case "BrocadeSwitchDataSource":
          BrocadeSwitchDataSource.validateJsonElement(jsonElement);
          break;
        case "CheckpointFirewallDataSource":
          CheckpointFirewallDataSource.validateJsonElement(jsonElement);
          break;
        case "CiscoSwitchDataSource":
          CiscoSwitchDataSource.validateJsonElement(jsonElement);
          break;
        case "DellSwitchDataSource":
          DellSwitchDataSource.validateJsonElement(jsonElement);
          break;
        case "HPOneViewManagerDataSource":
          HPOneViewManagerDataSource.validateJsonElement(jsonElement);
          break;
        case "HPOneViewManagerDataSourceRequest":
          HPOneViewManagerDataSourceRequest.validateJsonElement(jsonElement);
          break;
        case "HPVCManagerDataSource":
          HPVCManagerDataSource.validateJsonElement(jsonElement);
          break;
        case "HPVCManagerDataSourceRequest":
          HPVCManagerDataSourceRequest.validateJsonElement(jsonElement);
          break;
        case "JuniperSwitchDataSource":
          JuniperSwitchDataSource.validateJsonElement(jsonElement);
          break;
        case "PanFirewallDataSource":
          PanFirewallDataSource.validateJsonElement(jsonElement);
          break;
        case "UCSManagerDataSource":
          UCSManagerDataSource.validateJsonElement(jsonElement);
          break;
        case "UCSManagerDataSourceRequest":
          UCSManagerDataSourceRequest.validateJsonElement(jsonElement);
          break;
        default:
          throw new IllegalArgumentException(String.format("The value of the `entity_type` field `%s` does not match any key defined in the discriminator's mapping.", discriminatorValue));
      }
  }


  /**
   * Create an instance of SwitchDataSource given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SwitchDataSource
   * @throws IOException if the JSON string is invalid with respect to SwitchDataSource
   */
  public static SwitchDataSource fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SwitchDataSource.class);
  }

  /**
   * Convert an instance of SwitchDataSource to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

