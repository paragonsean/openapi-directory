/*
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
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
import org.openapitools.client.model.BandwidthSchedule;

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
 * The collection of bandwidth schedules.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:10.716364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BandwidthSchedulesList {
  public static final String SERIALIZED_NAME_NEXT_LINK = "nextLink";
  @SerializedName(SERIALIZED_NAME_NEXT_LINK)
  private String nextLink;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private List<BandwidthSchedule> value = new ArrayList<>();

  public BandwidthSchedulesList() {
  }

  public BandwidthSchedulesList(
     String nextLink, 
     List<BandwidthSchedule> value
  ) {
    this();
    this.nextLink = nextLink;
    this.value = value;
  }

  /**
   * Link to the next set of results.
   * @return nextLink
   */
  @javax.annotation.Nullable
  public String getNextLink() {
    return nextLink;
  }



  /**
   * The list of bandwidth schedules.
   * @return value
   */
  @javax.annotation.Nullable
  public List<BandwidthSchedule> getValue() {
    return value;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BandwidthSchedulesList bandwidthSchedulesList = (BandwidthSchedulesList) o;
    return Objects.equals(this.nextLink, bandwidthSchedulesList.nextLink) &&
        Objects.equals(this.value, bandwidthSchedulesList.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nextLink, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BandwidthSchedulesList {\n");
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
   * @throws IOException if the JSON Element is invalid with respect to BandwidthSchedulesList
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BandwidthSchedulesList.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BandwidthSchedulesList is not found in the empty JSON string", BandwidthSchedulesList.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BandwidthSchedulesList.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BandwidthSchedulesList` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            BandwidthSchedule.validateJsonElement(jsonArrayvalue.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BandwidthSchedulesList.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BandwidthSchedulesList' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BandwidthSchedulesList> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BandwidthSchedulesList.class));

       return (TypeAdapter<T>) new TypeAdapter<BandwidthSchedulesList>() {
           @Override
           public void write(JsonWriter out, BandwidthSchedulesList value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BandwidthSchedulesList read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BandwidthSchedulesList given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BandwidthSchedulesList
   * @throws IOException if the JSON string is invalid with respect to BandwidthSchedulesList
   */
  public static BandwidthSchedulesList fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BandwidthSchedulesList.class);
  }

  /**
   * Convert an instance of BandwidthSchedulesList to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

