/*
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
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
import org.openapitools.client.model.Lab;

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
 * The response of a list operation.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:25.069739-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ResponseWithContinuationLab {
  public static final String SERIALIZED_NAME_NEXT_LINK = "nextLink";
  @SerializedName(SERIALIZED_NAME_NEXT_LINK)
  private String nextLink;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private List<Lab> value = new ArrayList<>();

  public ResponseWithContinuationLab() {
  }

  public ResponseWithContinuationLab nextLink(String nextLink) {
    this.nextLink = nextLink;
    return this;
  }

  /**
   * Link for next set of results.
   * @return nextLink
   */
  @javax.annotation.Nullable
  public String getNextLink() {
    return nextLink;
  }

  public void setNextLink(String nextLink) {
    this.nextLink = nextLink;
  }


  public ResponseWithContinuationLab value(List<Lab> value) {
    this.value = value;
    return this;
  }

  public ResponseWithContinuationLab addValueItem(Lab valueItem) {
    if (this.value == null) {
      this.value = new ArrayList<>();
    }
    this.value.add(valueItem);
    return this;
  }

  /**
   * Results of the list operation.
   * @return value
   */
  @javax.annotation.Nullable
  public List<Lab> getValue() {
    return value;
  }

  public void setValue(List<Lab> value) {
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
    ResponseWithContinuationLab responseWithContinuationLab = (ResponseWithContinuationLab) o;
    return Objects.equals(this.nextLink, responseWithContinuationLab.nextLink) &&
        Objects.equals(this.value, responseWithContinuationLab.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nextLink, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ResponseWithContinuationLab {\n");
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
   * @throws IOException if the JSON Element is invalid with respect to ResponseWithContinuationLab
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ResponseWithContinuationLab.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ResponseWithContinuationLab is not found in the empty JSON string", ResponseWithContinuationLab.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ResponseWithContinuationLab.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ResponseWithContinuationLab` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            Lab.validateJsonElement(jsonArrayvalue.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ResponseWithContinuationLab.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ResponseWithContinuationLab' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ResponseWithContinuationLab> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ResponseWithContinuationLab.class));

       return (TypeAdapter<T>) new TypeAdapter<ResponseWithContinuationLab>() {
           @Override
           public void write(JsonWriter out, ResponseWithContinuationLab value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ResponseWithContinuationLab read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ResponseWithContinuationLab given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ResponseWithContinuationLab
   * @throws IOException if the JSON string is invalid with respect to ResponseWithContinuationLab
   */
  public static ResponseWithContinuationLab fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ResponseWithContinuationLab.class);
  }

  /**
   * Convert an instance of ResponseWithContinuationLab to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

