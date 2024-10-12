/*
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
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
 * MyOrdersSellingIdMarkPickedUpPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:29.182990-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MyOrdersSellingIdMarkPickedUpPostRequest {
  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public MyOrdersSellingIdMarkPickedUpPostRequest() {
  }

  public MyOrdersSellingIdMarkPickedUpPostRequest date(String date) {
    this.date = date;
    return this;
  }

  /**
   * Date the item was picked up.
   * @return date
   */
  @javax.annotation.Nullable
  public String getDate() {
    return date;
  }

  public void setDate(String date) {
    this.date = date;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MyOrdersSellingIdMarkPickedUpPostRequest myOrdersSellingIdMarkPickedUpPostRequest = (MyOrdersSellingIdMarkPickedUpPostRequest) o;
    return Objects.equals(this.date, myOrdersSellingIdMarkPickedUpPostRequest.date);
  }

  @Override
  public int hashCode() {
    return Objects.hash(date);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MyOrdersSellingIdMarkPickedUpPostRequest {\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
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
    openapiFields.add("date");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MyOrdersSellingIdMarkPickedUpPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MyOrdersSellingIdMarkPickedUpPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MyOrdersSellingIdMarkPickedUpPostRequest is not found in the empty JSON string", MyOrdersSellingIdMarkPickedUpPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MyOrdersSellingIdMarkPickedUpPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MyOrdersSellingIdMarkPickedUpPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("date") != null && !jsonObj.get("date").isJsonNull()) && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MyOrdersSellingIdMarkPickedUpPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MyOrdersSellingIdMarkPickedUpPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MyOrdersSellingIdMarkPickedUpPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MyOrdersSellingIdMarkPickedUpPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<MyOrdersSellingIdMarkPickedUpPostRequest>() {
           @Override
           public void write(JsonWriter out, MyOrdersSellingIdMarkPickedUpPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MyOrdersSellingIdMarkPickedUpPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MyOrdersSellingIdMarkPickedUpPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MyOrdersSellingIdMarkPickedUpPostRequest
   * @throws IOException if the JSON string is invalid with respect to MyOrdersSellingIdMarkPickedUpPostRequest
   */
  public static MyOrdersSellingIdMarkPickedUpPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MyOrdersSellingIdMarkPickedUpPostRequest.class);
  }

  /**
   * Convert an instance of MyOrdersSellingIdMarkPickedUpPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

