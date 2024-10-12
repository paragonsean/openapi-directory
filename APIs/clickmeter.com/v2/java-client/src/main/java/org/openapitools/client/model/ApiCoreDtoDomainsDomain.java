/*
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
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
 * ApiCoreDtoDomainsDomain
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:30.746224-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiCoreDtoDomainsDomain {
  public static final String SERIALIZED_NAME_CUSTOM404 = "custom404";
  @SerializedName(SERIALIZED_NAME_CUSTOM404)
  private String custom404;

  public static final String SERIALIZED_NAME_CUSTOM_HOMEPAGE = "customHomepage";
  @SerializedName(SERIALIZED_NAME_CUSTOM_HOMEPAGE)
  private String customHomepage;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * Gets or Sets type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    SYSTEM("System"),
    
    GO("Go"),
    
    DEDICATED("Dedicated"),
    
    PERSONAL("Personal");

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

  public ApiCoreDtoDomainsDomain() {
  }

  public ApiCoreDtoDomainsDomain custom404(String custom404) {
    this.custom404 = custom404;
    return this;
  }

  /**
   * Get custom404
   * @return custom404
   */
  @javax.annotation.Nullable
  public String getCustom404() {
    return custom404;
  }

  public void setCustom404(String custom404) {
    this.custom404 = custom404;
  }


  public ApiCoreDtoDomainsDomain customHomepage(String customHomepage) {
    this.customHomepage = customHomepage;
    return this;
  }

  /**
   * Get customHomepage
   * @return customHomepage
   */
  @javax.annotation.Nullable
  public String getCustomHomepage() {
    return customHomepage;
  }

  public void setCustomHomepage(String customHomepage) {
    this.customHomepage = customHomepage;
  }


  public ApiCoreDtoDomainsDomain id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public ApiCoreDtoDomainsDomain name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ApiCoreDtoDomainsDomain type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
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
    ApiCoreDtoDomainsDomain apiCoreDtoDomainsDomain = (ApiCoreDtoDomainsDomain) o;
    return Objects.equals(this.custom404, apiCoreDtoDomainsDomain.custom404) &&
        Objects.equals(this.customHomepage, apiCoreDtoDomainsDomain.customHomepage) &&
        Objects.equals(this.id, apiCoreDtoDomainsDomain.id) &&
        Objects.equals(this.name, apiCoreDtoDomainsDomain.name) &&
        Objects.equals(this.type, apiCoreDtoDomainsDomain.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(custom404, customHomepage, id, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiCoreDtoDomainsDomain {\n");
    sb.append("    custom404: ").append(toIndentedString(custom404)).append("\n");
    sb.append("    customHomepage: ").append(toIndentedString(customHomepage)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
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
    openapiFields.add("custom404");
    openapiFields.add("customHomepage");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiCoreDtoDomainsDomain
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiCoreDtoDomainsDomain.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiCoreDtoDomainsDomain is not found in the empty JSON string", ApiCoreDtoDomainsDomain.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiCoreDtoDomainsDomain.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiCoreDtoDomainsDomain` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("custom404") != null && !jsonObj.get("custom404").isJsonNull()) && !jsonObj.get("custom404").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `custom404` to be a primitive type in the JSON string but got `%s`", jsonObj.get("custom404").toString()));
      }
      if ((jsonObj.get("customHomepage") != null && !jsonObj.get("customHomepage").isJsonNull()) && !jsonObj.get("customHomepage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customHomepage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customHomepage").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiCoreDtoDomainsDomain.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiCoreDtoDomainsDomain' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiCoreDtoDomainsDomain> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiCoreDtoDomainsDomain.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiCoreDtoDomainsDomain>() {
           @Override
           public void write(JsonWriter out, ApiCoreDtoDomainsDomain value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiCoreDtoDomainsDomain read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiCoreDtoDomainsDomain given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiCoreDtoDomainsDomain
   * @throws IOException if the JSON string is invalid with respect to ApiCoreDtoDomainsDomain
   */
  public static ApiCoreDtoDomainsDomain fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiCoreDtoDomainsDomain.class);
  }

  /**
   * Convert an instance of ApiCoreDtoDomainsDomain to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

