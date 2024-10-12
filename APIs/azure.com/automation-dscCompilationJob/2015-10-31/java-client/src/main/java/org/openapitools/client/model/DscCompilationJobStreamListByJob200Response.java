/*
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-10-31
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
import org.openapitools.client.model.DscCompilationJobStreamListByJob200ResponseValueInner;

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
 * The response model for the list job stream operation.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:44:36.885548-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DscCompilationJobStreamListByJob200Response {
  public static final String SERIALIZED_NAME_NEXT_LINK = "nextLink";
  @SerializedName(SERIALIZED_NAME_NEXT_LINK)
  private String nextLink;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private List<DscCompilationJobStreamListByJob200ResponseValueInner> value = new ArrayList<>();

  public DscCompilationJobStreamListByJob200Response() {
  }

  public DscCompilationJobStreamListByJob200Response nextLink(String nextLink) {
    this.nextLink = nextLink;
    return this;
  }

  /**
   * Gets or sets the next link.
   * @return nextLink
   */
  @javax.annotation.Nullable
  public String getNextLink() {
    return nextLink;
  }

  public void setNextLink(String nextLink) {
    this.nextLink = nextLink;
  }


  public DscCompilationJobStreamListByJob200Response value(List<DscCompilationJobStreamListByJob200ResponseValueInner> value) {
    this.value = value;
    return this;
  }

  public DscCompilationJobStreamListByJob200Response addValueItem(DscCompilationJobStreamListByJob200ResponseValueInner valueItem) {
    if (this.value == null) {
      this.value = new ArrayList<>();
    }
    this.value.add(valueItem);
    return this;
  }

  /**
   * A list of job streams.
   * @return value
   */
  @javax.annotation.Nullable
  public List<DscCompilationJobStreamListByJob200ResponseValueInner> getValue() {
    return value;
  }

  public void setValue(List<DscCompilationJobStreamListByJob200ResponseValueInner> value) {
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
    DscCompilationJobStreamListByJob200Response dscCompilationJobStreamListByJob200Response = (DscCompilationJobStreamListByJob200Response) o;
    return Objects.equals(this.nextLink, dscCompilationJobStreamListByJob200Response.nextLink) &&
        Objects.equals(this.value, dscCompilationJobStreamListByJob200Response.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nextLink, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DscCompilationJobStreamListByJob200Response {\n");
    sb.append("    nextLink: ").append(toIndentedString(nextLink)).append("\n");
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
    openapiFields.add("nextLink");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DscCompilationJobStreamListByJob200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DscCompilationJobStreamListByJob200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DscCompilationJobStreamListByJob200Response is not found in the empty JSON string", DscCompilationJobStreamListByJob200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DscCompilationJobStreamListByJob200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DscCompilationJobStreamListByJob200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("nextLink") != null && !jsonObj.get("nextLink").isJsonNull()) && !jsonObj.get("nextLink").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nextLink` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nextLink").toString()));
      }
      if (jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) {
        JsonArray jsonArrayvalue = jsonObj.getAsJsonArray("value");
        if (jsonArrayvalue != null) {
          // ensure the json data is an array
          if (!jsonObj.get("value").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `value` to be an array in the JSON string but got `%s`", jsonObj.get("value").toString()));
          }

          // validate the optional field `value` (array)
          for (int i = 0; i < jsonArrayvalue.size(); i++) {
            DscCompilationJobStreamListByJob200ResponseValueInner.validateJsonElement(jsonArrayvalue.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DscCompilationJobStreamListByJob200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DscCompilationJobStreamListByJob200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DscCompilationJobStreamListByJob200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DscCompilationJobStreamListByJob200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<DscCompilationJobStreamListByJob200Response>() {
           @Override
           public void write(JsonWriter out, DscCompilationJobStreamListByJob200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DscCompilationJobStreamListByJob200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DscCompilationJobStreamListByJob200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DscCompilationJobStreamListByJob200Response
   * @throws IOException if the JSON string is invalid with respect to DscCompilationJobStreamListByJob200Response
   */
  public static DscCompilationJobStreamListByJob200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DscCompilationJobStreamListByJob200Response.class);
  }

  /**
   * Convert an instance of DscCompilationJobStreamListByJob200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

