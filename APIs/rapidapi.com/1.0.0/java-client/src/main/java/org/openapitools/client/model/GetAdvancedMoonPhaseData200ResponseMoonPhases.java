/*
 * Moon API
 * # Moon-API.com Postman Collection  Welcome to the Moon Phase API Postman Collection! This collection contains a set of pre-configured API requests to interact with the Moon Phase API endpoints provided by [moon-api.com](https://moon-api.com). Explore the enchanting world of the moon and its ever-changing phases with ease using this collection.  ## Getting Started  To start using this Postman collection, follow these steps:  1. [Download and install Postman](https://www.postman.com/downloads/) if you haven't already. 2. Import the Moon API Postman Collection into your Postman app. 3. Set your RapidAPI key in the collection's environment variables. 4. Begin making requests to explore the moon phase data and retrieve lunar information.       ## Collection Structure  The Moon-API.com Postman Collection consists of the following requests:  - **Basic Moon Phase**: Retrieve the main moon phase data. - **Advanced Moon Phase**: Get detailed moon phase data based on a specific timezone and coordinates. - **Plain Text Moon Phase**: Get a plain text description of the current moon phase. - **Emoji Moon Phase**: Get the relevant emoji of the current moon phase. - **Lunar Calender**: Get the current year's moon phases in a markdown calender.       ## Environment Variables  The collection uses environment variables to store your RapidAPI key. To use this collection effectively, ensure you set the `X-Rapidapi-Key` variable in the collection's environment with your actual RapidAPI key.  ## How to Use  1. Select the desired request from the Moon API collection. 2. Click on the request to open it. 3. Send the request and view the response to retrieve the moon phase data.       ## Documentation  For more information on the Moon Phase API endpoints and their response formats, refer to the [official Moon API documentation](https://rapidapi.com/MoonAPIcom/api/moon-phase/details). Visit [moon-api.com](https://moon-api.com) to learn more about the Moon Phase API and the services provided.  Happy moon exploration with the Moon Phase API Postman Collection provided by [moon-api.com](https://moon-api.com)!
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.GetAdvancedMoonPhaseData200ResponseMoonPhasesFirstQuarter;
import org.openapitools.client.model.GetAdvancedMoonPhaseData200ResponseMoonPhasesFullMoon;
import org.openapitools.client.model.GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter;
import org.openapitools.client.model.GetAdvancedMoonPhaseData200ResponseMoonPhasesNewMoon;

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
 * GetAdvancedMoonPhaseData200ResponseMoonPhases
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:03.709234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetAdvancedMoonPhaseData200ResponseMoonPhases {
  public static final String SERIALIZED_NAME_FIRST_QUARTER = "first_quarter";
  @SerializedName(SERIALIZED_NAME_FIRST_QUARTER)
  private GetAdvancedMoonPhaseData200ResponseMoonPhasesFirstQuarter firstQuarter;

  public static final String SERIALIZED_NAME_FULL_MOON = "full_moon";
  @SerializedName(SERIALIZED_NAME_FULL_MOON)
  private GetAdvancedMoonPhaseData200ResponseMoonPhasesFullMoon fullMoon;

  public static final String SERIALIZED_NAME_LAST_QUARTER = "last_quarter";
  @SerializedName(SERIALIZED_NAME_LAST_QUARTER)
  private GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter lastQuarter;

  public static final String SERIALIZED_NAME_NEW_MOON = "new_moon";
  @SerializedName(SERIALIZED_NAME_NEW_MOON)
  private GetAdvancedMoonPhaseData200ResponseMoonPhasesNewMoon newMoon;

  public GetAdvancedMoonPhaseData200ResponseMoonPhases() {
  }

  public GetAdvancedMoonPhaseData200ResponseMoonPhases firstQuarter(GetAdvancedMoonPhaseData200ResponseMoonPhasesFirstQuarter firstQuarter) {
    this.firstQuarter = firstQuarter;
    return this;
  }

  /**
   * Get firstQuarter
   * @return firstQuarter
   */
  @javax.annotation.Nullable
  public GetAdvancedMoonPhaseData200ResponseMoonPhasesFirstQuarter getFirstQuarter() {
    return firstQuarter;
  }

  public void setFirstQuarter(GetAdvancedMoonPhaseData200ResponseMoonPhasesFirstQuarter firstQuarter) {
    this.firstQuarter = firstQuarter;
  }


  public GetAdvancedMoonPhaseData200ResponseMoonPhases fullMoon(GetAdvancedMoonPhaseData200ResponseMoonPhasesFullMoon fullMoon) {
    this.fullMoon = fullMoon;
    return this;
  }

  /**
   * Get fullMoon
   * @return fullMoon
   */
  @javax.annotation.Nullable
  public GetAdvancedMoonPhaseData200ResponseMoonPhasesFullMoon getFullMoon() {
    return fullMoon;
  }

  public void setFullMoon(GetAdvancedMoonPhaseData200ResponseMoonPhasesFullMoon fullMoon) {
    this.fullMoon = fullMoon;
  }


  public GetAdvancedMoonPhaseData200ResponseMoonPhases lastQuarter(GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter lastQuarter) {
    this.lastQuarter = lastQuarter;
    return this;
  }

  /**
   * Get lastQuarter
   * @return lastQuarter
   */
  @javax.annotation.Nullable
  public GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter getLastQuarter() {
    return lastQuarter;
  }

  public void setLastQuarter(GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter lastQuarter) {
    this.lastQuarter = lastQuarter;
  }


  public GetAdvancedMoonPhaseData200ResponseMoonPhases newMoon(GetAdvancedMoonPhaseData200ResponseMoonPhasesNewMoon newMoon) {
    this.newMoon = newMoon;
    return this;
  }

  /**
   * Get newMoon
   * @return newMoon
   */
  @javax.annotation.Nullable
  public GetAdvancedMoonPhaseData200ResponseMoonPhasesNewMoon getNewMoon() {
    return newMoon;
  }

  public void setNewMoon(GetAdvancedMoonPhaseData200ResponseMoonPhasesNewMoon newMoon) {
    this.newMoon = newMoon;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetAdvancedMoonPhaseData200ResponseMoonPhases getAdvancedMoonPhaseData200ResponseMoonPhases = (GetAdvancedMoonPhaseData200ResponseMoonPhases) o;
    return Objects.equals(this.firstQuarter, getAdvancedMoonPhaseData200ResponseMoonPhases.firstQuarter) &&
        Objects.equals(this.fullMoon, getAdvancedMoonPhaseData200ResponseMoonPhases.fullMoon) &&
        Objects.equals(this.lastQuarter, getAdvancedMoonPhaseData200ResponseMoonPhases.lastQuarter) &&
        Objects.equals(this.newMoon, getAdvancedMoonPhaseData200ResponseMoonPhases.newMoon);
  }

  @Override
  public int hashCode() {
    return Objects.hash(firstQuarter, fullMoon, lastQuarter, newMoon);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetAdvancedMoonPhaseData200ResponseMoonPhases {\n");
    sb.append("    firstQuarter: ").append(toIndentedString(firstQuarter)).append("\n");
    sb.append("    fullMoon: ").append(toIndentedString(fullMoon)).append("\n");
    sb.append("    lastQuarter: ").append(toIndentedString(lastQuarter)).append("\n");
    sb.append("    newMoon: ").append(toIndentedString(newMoon)).append("\n");
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
    openapiFields.add("first_quarter");
    openapiFields.add("full_moon");
    openapiFields.add("last_quarter");
    openapiFields.add("new_moon");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetAdvancedMoonPhaseData200ResponseMoonPhases
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetAdvancedMoonPhaseData200ResponseMoonPhases.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetAdvancedMoonPhaseData200ResponseMoonPhases is not found in the empty JSON string", GetAdvancedMoonPhaseData200ResponseMoonPhases.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetAdvancedMoonPhaseData200ResponseMoonPhases.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetAdvancedMoonPhaseData200ResponseMoonPhases` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `first_quarter`
      if (jsonObj.get("first_quarter") != null && !jsonObj.get("first_quarter").isJsonNull()) {
        GetAdvancedMoonPhaseData200ResponseMoonPhasesFirstQuarter.validateJsonElement(jsonObj.get("first_quarter"));
      }
      // validate the optional field `full_moon`
      if (jsonObj.get("full_moon") != null && !jsonObj.get("full_moon").isJsonNull()) {
        GetAdvancedMoonPhaseData200ResponseMoonPhasesFullMoon.validateJsonElement(jsonObj.get("full_moon"));
      }
      // validate the optional field `last_quarter`
      if (jsonObj.get("last_quarter") != null && !jsonObj.get("last_quarter").isJsonNull()) {
        GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.validateJsonElement(jsonObj.get("last_quarter"));
      }
      // validate the optional field `new_moon`
      if (jsonObj.get("new_moon") != null && !jsonObj.get("new_moon").isJsonNull()) {
        GetAdvancedMoonPhaseData200ResponseMoonPhasesNewMoon.validateJsonElement(jsonObj.get("new_moon"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetAdvancedMoonPhaseData200ResponseMoonPhases.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetAdvancedMoonPhaseData200ResponseMoonPhases' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetAdvancedMoonPhaseData200ResponseMoonPhases> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetAdvancedMoonPhaseData200ResponseMoonPhases.class));

       return (TypeAdapter<T>) new TypeAdapter<GetAdvancedMoonPhaseData200ResponseMoonPhases>() {
           @Override
           public void write(JsonWriter out, GetAdvancedMoonPhaseData200ResponseMoonPhases value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetAdvancedMoonPhaseData200ResponseMoonPhases read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetAdvancedMoonPhaseData200ResponseMoonPhases given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetAdvancedMoonPhaseData200ResponseMoonPhases
   * @throws IOException if the JSON string is invalid with respect to GetAdvancedMoonPhaseData200ResponseMoonPhases
   */
  public static GetAdvancedMoonPhaseData200ResponseMoonPhases fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetAdvancedMoonPhaseData200ResponseMoonPhases.class);
  }

  /**
   * Convert an instance of GetAdvancedMoonPhaseData200ResponseMoonPhases to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

