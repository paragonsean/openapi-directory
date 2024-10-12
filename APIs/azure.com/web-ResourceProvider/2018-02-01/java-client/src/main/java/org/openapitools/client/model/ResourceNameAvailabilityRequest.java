/*
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
 * Resource name availability request content.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:50.427441-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ResourceNameAvailabilityRequest {
  public static final String SERIALIZED_NAME_IS_FQDN = "isFqdn";
  @SerializedName(SERIALIZED_NAME_IS_FQDN)
  private Boolean isFqdn;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * Resource type used for verification.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    SITE("Site"),
    
    SLOT("Slot"),
    
    HOSTING_ENVIRONMENT("HostingEnvironment"),
    
    PUBLISHING_USER("PublishingUser"),
    
    MICROSOFT_WEB_SITES("Microsoft.Web/sites"),
    
    MICROSOFT_WEB_SITES_SLOTS("Microsoft.Web/sites/slots"),
    
    MICROSOFT_WEB_HOSTING_ENVIRONMENTS("Microsoft.Web/hostingEnvironments"),
    
    MICROSOFT_WEB_PUBLISHING_USERS("Microsoft.Web/publishingUsers");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public ResourceNameAvailabilityRequest() {
  }

  public ResourceNameAvailabilityRequest isFqdn(Boolean isFqdn) {
    this.isFqdn = isFqdn;
    return this;
  }

  /**
   * Is fully qualified domain name.
   * @return isFqdn
   */
  @javax.annotation.Nullable
  public Boolean getIsFqdn() {
    return isFqdn;
  }

  public void setIsFqdn(Boolean isFqdn) {
    this.isFqdn = isFqdn;
  }


  public ResourceNameAvailabilityRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Resource name to verify.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ResourceNameAvailabilityRequest type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Resource type used for verification.
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ResourceNameAvailabilityRequest resourceNameAvailabilityRequest = (ResourceNameAvailabilityRequest) o;
    return Objects.equals(this.isFqdn, resourceNameAvailabilityRequest.isFqdn) &&
        Objects.equals(this.name, resourceNameAvailabilityRequest.name) &&
        Objects.equals(this.type, resourceNameAvailabilityRequest.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isFqdn, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ResourceNameAvailabilityRequest {\n");
    sb.append("    isFqdn: ").append(toIndentedString(isFqdn)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("isFqdn");
    openapiFields.add("name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ResourceNameAvailabilityRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ResourceNameAvailabilityRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ResourceNameAvailabilityRequest is not found in the empty JSON string", ResourceNameAvailabilityRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ResourceNameAvailabilityRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ResourceNameAvailabilityRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ResourceNameAvailabilityRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ResourceNameAvailabilityRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ResourceNameAvailabilityRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ResourceNameAvailabilityRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ResourceNameAvailabilityRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ResourceNameAvailabilityRequest>() {
           @Override
           public void write(JsonWriter out, ResourceNameAvailabilityRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ResourceNameAvailabilityRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ResourceNameAvailabilityRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ResourceNameAvailabilityRequest
   * @throws IOException if the JSON string is invalid with respect to ResourceNameAvailabilityRequest
   */
  public static ResourceNameAvailabilityRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ResourceNameAvailabilityRequest.class);
  }

  /**
   * Convert an instance of ResourceNameAvailabilityRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

