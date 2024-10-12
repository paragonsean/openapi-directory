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
 * NSXVManagerDataSource
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:28.864194-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NSXVManagerDataSource extends BaseDataSource {
  public static final String SERIALIZED_NAME_CENTRAL_CLI_ENABLED = "central_cli_enabled";
  @SerializedName(SERIALIZED_NAME_CENTRAL_CLI_ENABLED)
  private Boolean centralCliEnabled = false;

  public static final String SERIALIZED_NAME_CREDENTIALS = "credentials";
  @SerializedName(SERIALIZED_NAME_CREDENTIALS)
  private PasswordCredentials credentials;

  public static final String SERIALIZED_NAME_IPFIX_ENABLED = "ipfix_enabled";
  @SerializedName(SERIALIZED_NAME_IPFIX_ENABLED)
  private Boolean ipfixEnabled = false;

  public static final String SERIALIZED_NAME_VCENTER_ID = "vcenter_id";
  @SerializedName(SERIALIZED_NAME_VCENTER_ID)
  private String vcenterId;

  public NSXVManagerDataSource() {
    this.entityType = this.getClass().getSimpleName();
  }

  public NSXVManagerDataSource centralCliEnabled(Boolean centralCliEnabled) {
    this.centralCliEnabled = centralCliEnabled;
    return this;
  }

  /**
   * Get centralCliEnabled
   * @return centralCliEnabled
   */
  @javax.annotation.Nullable
  public Boolean getCentralCliEnabled() {
    return centralCliEnabled;
  }

  public void setCentralCliEnabled(Boolean centralCliEnabled) {
    this.centralCliEnabled = centralCliEnabled;
  }


  public NSXVManagerDataSource credentials(PasswordCredentials credentials) {
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


  public NSXVManagerDataSource ipfixEnabled(Boolean ipfixEnabled) {
    this.ipfixEnabled = ipfixEnabled;
    return this;
  }

  /**
   * Get ipfixEnabled
   * @return ipfixEnabled
   */
  @javax.annotation.Nullable
  public Boolean getIpfixEnabled() {
    return ipfixEnabled;
  }

  public void setIpfixEnabled(Boolean ipfixEnabled) {
    this.ipfixEnabled = ipfixEnabled;
  }


  public NSXVManagerDataSource vcenterId(String vcenterId) {
    this.vcenterId = vcenterId;
    return this;
  }

  /**
   * Associated vcenter data source entity Id
   * @return vcenterId
   */
  @javax.annotation.Nullable
  public String getVcenterId() {
    return vcenterId;
  }

  public void setVcenterId(String vcenterId) {
    this.vcenterId = vcenterId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NSXVManagerDataSource nsXVManagerDataSource = (NSXVManagerDataSource) o;
    return Objects.equals(this.centralCliEnabled, nsXVManagerDataSource.centralCliEnabled) &&
        Objects.equals(this.credentials, nsXVManagerDataSource.credentials) &&
        Objects.equals(this.ipfixEnabled, nsXVManagerDataSource.ipfixEnabled) &&
        Objects.equals(this.vcenterId, nsXVManagerDataSource.vcenterId) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(centralCliEnabled, credentials, ipfixEnabled, vcenterId, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NSXVManagerDataSource {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    centralCliEnabled: ").append(toIndentedString(centralCliEnabled)).append("\n");
    sb.append("    credentials: ").append(toIndentedString(credentials)).append("\n");
    sb.append("    ipfixEnabled: ").append(toIndentedString(ipfixEnabled)).append("\n");
    sb.append("    vcenterId: ").append(toIndentedString(vcenterId)).append("\n");
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
    openapiFields.add("central_cli_enabled");
    openapiFields.add("credentials");
    openapiFields.add("ipfix_enabled");
    openapiFields.add("vcenter_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NSXVManagerDataSource
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NSXVManagerDataSource.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NSXVManagerDataSource is not found in the empty JSON string", NSXVManagerDataSource.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NSXVManagerDataSource.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NSXVManagerDataSource` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NSXVManagerDataSource.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NSXVManagerDataSource' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NSXVManagerDataSource> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NSXVManagerDataSource.class));

       return (TypeAdapter<T>) new TypeAdapter<NSXVManagerDataSource>() {
           @Override
           public void write(JsonWriter out, NSXVManagerDataSource value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NSXVManagerDataSource read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NSXVManagerDataSource given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NSXVManagerDataSource
   * @throws IOException if the JSON string is invalid with respect to NSXVManagerDataSource
   */
  public static NSXVManagerDataSource fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NSXVManagerDataSource.class);
  }

  /**
   * Convert an instance of NSXVManagerDataSource to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

