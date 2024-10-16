/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * CreateOrganizationSamlRoleRequestNetworksInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateOrganizationSamlRoleRequestNetworksInner {
  /**
   * The privilege of the SAML administrator on the network. Can be one of &#39;full&#39;, &#39;read-only&#39;, &#39;guest-ambassador&#39;, &#39;monitor-only&#39; or &#39;ssid-admin&#39;
   */
  @JsonAdapter(AccessEnum.Adapter.class)
  public enum AccessEnum {
    FULL("full"),
    
    GUEST_AMBASSADOR("guest-ambassador"),
    
    MONITOR_ONLY("monitor-only"),
    
    READ_ONLY("read-only"),
    
    SSID_ADMIN("ssid-admin");

    private String value;

    AccessEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AccessEnum fromValue(String value) {
      for (AccessEnum b : AccessEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AccessEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AccessEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AccessEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AccessEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AccessEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACCESS = "access";
  @SerializedName(SERIALIZED_NAME_ACCESS)
  private AccessEnum access;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public CreateOrganizationSamlRoleRequestNetworksInner() {
  }

  public CreateOrganizationSamlRoleRequestNetworksInner access(AccessEnum access) {
    this.access = access;
    return this;
  }

  /**
   * The privilege of the SAML administrator on the network. Can be one of &#39;full&#39;, &#39;read-only&#39;, &#39;guest-ambassador&#39;, &#39;monitor-only&#39; or &#39;ssid-admin&#39;
   * @return access
   */
  @javax.annotation.Nonnull
  public AccessEnum getAccess() {
    return access;
  }

  public void setAccess(AccessEnum access) {
    this.access = access;
  }


  public CreateOrganizationSamlRoleRequestNetworksInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The network ID
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateOrganizationSamlRoleRequestNetworksInner createOrganizationSamlRoleRequestNetworksInner = (CreateOrganizationSamlRoleRequestNetworksInner) o;
    return Objects.equals(this.access, createOrganizationSamlRoleRequestNetworksInner.access) &&
        Objects.equals(this.id, createOrganizationSamlRoleRequestNetworksInner.id);
  }

  @Override
  public int hashCode() {
    return Objects.hash(access, id);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateOrganizationSamlRoleRequestNetworksInner {\n");
    sb.append("    access: ").append(toIndentedString(access)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
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
    openapiFields.add("access");
    openapiFields.add("id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("access");
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateOrganizationSamlRoleRequestNetworksInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateOrganizationSamlRoleRequestNetworksInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateOrganizationSamlRoleRequestNetworksInner is not found in the empty JSON string", CreateOrganizationSamlRoleRequestNetworksInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateOrganizationSamlRoleRequestNetworksInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateOrganizationSamlRoleRequestNetworksInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateOrganizationSamlRoleRequestNetworksInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("access").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `access` to be a primitive type in the JSON string but got `%s`", jsonObj.get("access").toString()));
      }
      // validate the required field `access`
      AccessEnum.validateJsonElement(jsonObj.get("access"));
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateOrganizationSamlRoleRequestNetworksInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateOrganizationSamlRoleRequestNetworksInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateOrganizationSamlRoleRequestNetworksInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateOrganizationSamlRoleRequestNetworksInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateOrganizationSamlRoleRequestNetworksInner>() {
           @Override
           public void write(JsonWriter out, CreateOrganizationSamlRoleRequestNetworksInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateOrganizationSamlRoleRequestNetworksInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateOrganizationSamlRoleRequestNetworksInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateOrganizationSamlRoleRequestNetworksInner
   * @throws IOException if the JSON string is invalid with respect to CreateOrganizationSamlRoleRequestNetworksInner
   */
  public static CreateOrganizationSamlRoleRequestNetworksInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateOrganizationSamlRoleRequestNetworksInner.class);
  }

  /**
   * Convert an instance of CreateOrganizationSamlRoleRequestNetworksInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

