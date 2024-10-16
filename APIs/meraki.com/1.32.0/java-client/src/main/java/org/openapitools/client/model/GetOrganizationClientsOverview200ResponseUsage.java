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
import org.openapitools.client.model.GetOrganizationClientsOverview200ResponseUsageOverall;

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
 * Usage information of all clients across organization
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationClientsOverview200ResponseUsage {
  public static final String SERIALIZED_NAME_AVERAGE = "average";
  @SerializedName(SERIALIZED_NAME_AVERAGE)
  private Float average;

  public static final String SERIALIZED_NAME_OVERALL = "overall";
  @SerializedName(SERIALIZED_NAME_OVERALL)
  private GetOrganizationClientsOverview200ResponseUsageOverall overall;

  public GetOrganizationClientsOverview200ResponseUsage() {
  }

  public GetOrganizationClientsOverview200ResponseUsage average(Float average) {
    this.average = average;
    return this;
  }

  /**
   * Average data usage (in kb) of each client in organization
   * @return average
   */
  @javax.annotation.Nullable
  public Float getAverage() {
    return average;
  }

  public void setAverage(Float average) {
    this.average = average;
  }


  public GetOrganizationClientsOverview200ResponseUsage overall(GetOrganizationClientsOverview200ResponseUsageOverall overall) {
    this.overall = overall;
    return this;
  }

  /**
   * Get overall
   * @return overall
   */
  @javax.annotation.Nullable
  public GetOrganizationClientsOverview200ResponseUsageOverall getOverall() {
    return overall;
  }

  public void setOverall(GetOrganizationClientsOverview200ResponseUsageOverall overall) {
    this.overall = overall;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationClientsOverview200ResponseUsage getOrganizationClientsOverview200ResponseUsage = (GetOrganizationClientsOverview200ResponseUsage) o;
    return Objects.equals(this.average, getOrganizationClientsOverview200ResponseUsage.average) &&
        Objects.equals(this.overall, getOrganizationClientsOverview200ResponseUsage.overall);
  }

  @Override
  public int hashCode() {
    return Objects.hash(average, overall);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationClientsOverview200ResponseUsage {\n");
    sb.append("    average: ").append(toIndentedString(average)).append("\n");
    sb.append("    overall: ").append(toIndentedString(overall)).append("\n");
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
    openapiFields.add("average");
    openapiFields.add("overall");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationClientsOverview200ResponseUsage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationClientsOverview200ResponseUsage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationClientsOverview200ResponseUsage is not found in the empty JSON string", GetOrganizationClientsOverview200ResponseUsage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationClientsOverview200ResponseUsage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationClientsOverview200ResponseUsage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `overall`
      if (jsonObj.get("overall") != null && !jsonObj.get("overall").isJsonNull()) {
        GetOrganizationClientsOverview200ResponseUsageOverall.validateJsonElement(jsonObj.get("overall"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationClientsOverview200ResponseUsage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationClientsOverview200ResponseUsage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationClientsOverview200ResponseUsage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationClientsOverview200ResponseUsage.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationClientsOverview200ResponseUsage>() {
           @Override
           public void write(JsonWriter out, GetOrganizationClientsOverview200ResponseUsage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationClientsOverview200ResponseUsage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationClientsOverview200ResponseUsage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationClientsOverview200ResponseUsage
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationClientsOverview200ResponseUsage
   */
  public static GetOrganizationClientsOverview200ResponseUsage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationClientsOverview200ResponseUsage.class);
  }

  /**
   * Convert an instance of GetOrganizationClientsOverview200ResponseUsage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

