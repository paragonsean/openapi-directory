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
 * UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  /**
   * The type of the DHCP option which should be one of (&#39;text&#39;, &#39;ip&#39;, &#39;integer&#39; or &#39;hex&#39;)
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    HEX("hex"),
    
    INTEGER("integer"),
    
    IP("ip"),
    
    TEXT("text");

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

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner() {
  }

  public UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner code(String code) {
    this.code = code;
    return this;
  }

  /**
   * The code for DHCP option which should be from 2 to 254
   * @return code
   */
  @javax.annotation.Nonnull
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The type of the DHCP option which should be one of (&#39;text&#39;, &#39;ip&#39;, &#39;integer&#39; or &#39;hex&#39;)
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner value(String value) {
    this.value = value;
    return this;
  }

  /**
   * The value of the DHCP option
   * @return value
   */
  @javax.annotation.Nonnull
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner updateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner = (UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner) o;
    return Objects.equals(this.code, updateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.code) &&
        Objects.equals(this.type, updateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.type) &&
        Objects.equals(this.value, updateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, type, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("code");
    openapiFields.add("type");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("code");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("value");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner is not found in the empty JSON string", UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
      if (!jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner>() {
           @Override
           public void write(JsonWriter out, UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner
   * @throws IOException if the JSON string is invalid with respect to UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner
   */
  public static UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.class);
  }

  /**
   * Convert an instance of UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

