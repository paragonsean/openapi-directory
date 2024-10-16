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
 * Reading for the &#39;button&#39; metric. This will only be present if the &#39;metric&#39; property equals &#39;button&#39;.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationSensorReadingsHistory200ResponseInnerButton {
  /**
   * Type of button press that occurred.
   */
  @JsonAdapter(PressTypeEnum.Adapter.class)
  public enum PressTypeEnum {
    LONG("long"),
    
    SHORT("short");

    private String value;

    PressTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PressTypeEnum fromValue(String value) {
      for (PressTypeEnum b : PressTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PressTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PressTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PressTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PressTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PressTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PRESS_TYPE = "pressType";
  @SerializedName(SERIALIZED_NAME_PRESS_TYPE)
  private PressTypeEnum pressType;

  public GetOrganizationSensorReadingsHistory200ResponseInnerButton() {
  }

  public GetOrganizationSensorReadingsHistory200ResponseInnerButton pressType(PressTypeEnum pressType) {
    this.pressType = pressType;
    return this;
  }

  /**
   * Type of button press that occurred.
   * @return pressType
   */
  @javax.annotation.Nullable
  public PressTypeEnum getPressType() {
    return pressType;
  }

  public void setPressType(PressTypeEnum pressType) {
    this.pressType = pressType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationSensorReadingsHistory200ResponseInnerButton getOrganizationSensorReadingsHistory200ResponseInnerButton = (GetOrganizationSensorReadingsHistory200ResponseInnerButton) o;
    return Objects.equals(this.pressType, getOrganizationSensorReadingsHistory200ResponseInnerButton.pressType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pressType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationSensorReadingsHistory200ResponseInnerButton {\n");
    sb.append("    pressType: ").append(toIndentedString(pressType)).append("\n");
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
    openapiFields.add("pressType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationSensorReadingsHistory200ResponseInnerButton
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationSensorReadingsHistory200ResponseInnerButton.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationSensorReadingsHistory200ResponseInnerButton is not found in the empty JSON string", GetOrganizationSensorReadingsHistory200ResponseInnerButton.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationSensorReadingsHistory200ResponseInnerButton.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationSensorReadingsHistory200ResponseInnerButton` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("pressType") != null && !jsonObj.get("pressType").isJsonNull()) && !jsonObj.get("pressType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pressType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pressType").toString()));
      }
      // validate the optional field `pressType`
      if (jsonObj.get("pressType") != null && !jsonObj.get("pressType").isJsonNull()) {
        PressTypeEnum.validateJsonElement(jsonObj.get("pressType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationSensorReadingsHistory200ResponseInnerButton.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationSensorReadingsHistory200ResponseInnerButton' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationSensorReadingsHistory200ResponseInnerButton> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationSensorReadingsHistory200ResponseInnerButton.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationSensorReadingsHistory200ResponseInnerButton>() {
           @Override
           public void write(JsonWriter out, GetOrganizationSensorReadingsHistory200ResponseInnerButton value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationSensorReadingsHistory200ResponseInnerButton read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationSensorReadingsHistory200ResponseInnerButton given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationSensorReadingsHistory200ResponseInnerButton
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationSensorReadingsHistory200ResponseInnerButton
   */
  public static GetOrganizationSensorReadingsHistory200ResponseInnerButton fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationSensorReadingsHistory200ResponseInnerButton.class);
  }

  /**
   * Convert an instance of GetOrganizationSensorReadingsHistory200ResponseInnerButton to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

