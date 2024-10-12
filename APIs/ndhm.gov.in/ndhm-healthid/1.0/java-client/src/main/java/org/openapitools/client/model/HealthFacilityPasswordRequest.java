/*
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
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
 * HealthFacilityPasswordRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:34.465238-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HealthFacilityPasswordRequest {
  public static final String SERIALIZED_NAME_HFR_UID = "hfrUid";
  @SerializedName(SERIALIZED_NAME_HFR_UID)
  private String hfrUid;

  public HealthFacilityPasswordRequest() {
  }

  public HealthFacilityPasswordRequest hfrUid(String hfrUid) {
    this.hfrUid = hfrUid;
    return this;
  }

  /**
   * Get hfrUid
   * @return hfrUid
   */
  @javax.annotation.Nullable
  public String getHfrUid() {
    return hfrUid;
  }

  public void setHfrUid(String hfrUid) {
    this.hfrUid = hfrUid;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HealthFacilityPasswordRequest healthFacilityPasswordRequest = (HealthFacilityPasswordRequest) o;
    return Objects.equals(this.hfrUid, healthFacilityPasswordRequest.hfrUid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hfrUid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HealthFacilityPasswordRequest {\n");
    sb.append("    hfrUid: ").append(toIndentedString(hfrUid)).append("\n");
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
    openapiFields.add("hfrUid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HealthFacilityPasswordRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HealthFacilityPasswordRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HealthFacilityPasswordRequest is not found in the empty JSON string", HealthFacilityPasswordRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HealthFacilityPasswordRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HealthFacilityPasswordRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("hfrUid") != null && !jsonObj.get("hfrUid").isJsonNull()) && !jsonObj.get("hfrUid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hfrUid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hfrUid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HealthFacilityPasswordRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HealthFacilityPasswordRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HealthFacilityPasswordRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HealthFacilityPasswordRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<HealthFacilityPasswordRequest>() {
           @Override
           public void write(JsonWriter out, HealthFacilityPasswordRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HealthFacilityPasswordRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HealthFacilityPasswordRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HealthFacilityPasswordRequest
   * @throws IOException if the JSON string is invalid with respect to HealthFacilityPasswordRequest
   */
  public static HealthFacilityPasswordRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HealthFacilityPasswordRequest.class);
  }

  /**
   * Convert an instance of HealthFacilityPasswordRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

