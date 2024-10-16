/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
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
 * APIModelsLog
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:35.511967-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class APIModelsLog {
  public static final String SERIALIZED_NAME_I_D = "ID";
  @SerializedName(SERIALIZED_NAME_I_D)
  private String ID;

  public static final String SERIALIZED_NAME_MESSAGE = "Message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_TIME_STAMP = "TimeStamp";
  @SerializedName(SERIALIZED_NAME_TIME_STAMP)
  private OffsetDateTime timeStamp;

  public APIModelsLog() {
  }

  public APIModelsLog ID(String ID) {
    this.ID = ID;
    return this;
  }

  /**
   * Get ID
   * @return ID
   */
  @javax.annotation.Nullable
  public String getID() {
    return ID;
  }

  public void setID(String ID) {
    this.ID = ID;
  }


  public APIModelsLog message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public APIModelsLog timeStamp(OffsetDateTime timeStamp) {
    this.timeStamp = timeStamp;
    return this;
  }

  /**
   * Get timeStamp
   * @return timeStamp
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTimeStamp() {
    return timeStamp;
  }

  public void setTimeStamp(OffsetDateTime timeStamp) {
    this.timeStamp = timeStamp;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    APIModelsLog apIModelsLog = (APIModelsLog) o;
    return Objects.equals(this.ID, apIModelsLog.ID) &&
        Objects.equals(this.message, apIModelsLog.message) &&
        Objects.equals(this.timeStamp, apIModelsLog.timeStamp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ID, message, timeStamp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class APIModelsLog {\n");
    sb.append("    ID: ").append(toIndentedString(ID)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    timeStamp: ").append(toIndentedString(timeStamp)).append("\n");
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
    openapiFields.add("ID");
    openapiFields.add("Message");
    openapiFields.add("TimeStamp");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to APIModelsLog
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!APIModelsLog.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in APIModelsLog is not found in the empty JSON string", APIModelsLog.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!APIModelsLog.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `APIModelsLog` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ID") != null && !jsonObj.get("ID").isJsonNull()) && !jsonObj.get("ID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ID").toString()));
      }
      if ((jsonObj.get("Message") != null && !jsonObj.get("Message").isJsonNull()) && !jsonObj.get("Message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Message").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!APIModelsLog.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'APIModelsLog' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<APIModelsLog> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(APIModelsLog.class));

       return (TypeAdapter<T>) new TypeAdapter<APIModelsLog>() {
           @Override
           public void write(JsonWriter out, APIModelsLog value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public APIModelsLog read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of APIModelsLog given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of APIModelsLog
   * @throws IOException if the JSON string is invalid with respect to APIModelsLog
   */
  public static APIModelsLog fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, APIModelsLog.class);
  }

  /**
   * Convert an instance of APIModelsLog to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

