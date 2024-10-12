/*
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
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
import org.openapitools.client.model.DemoAuthResponseDetails;

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
 * DemoAuthResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:03.399628-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DemoAuthResponse {
  public static final String SERIALIZED_NAME_DETAILS = "details";
  @SerializedName(SERIALIZED_NAME_DETAILS)
  private DemoAuthResponseDetails details;

  public DemoAuthResponse() {
  }

  public DemoAuthResponse details(DemoAuthResponseDetails details) {
    this.details = details;
    return this;
  }

  /**
   * Get details
   * @return details
   */
  @javax.annotation.Nullable
  public DemoAuthResponseDetails getDetails() {
    return details;
  }

  public void setDetails(DemoAuthResponseDetails details) {
    this.details = details;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DemoAuthResponse demoAuthResponse = (DemoAuthResponse) o;
    return Objects.equals(this.details, demoAuthResponse.details);
  }

  @Override
  public int hashCode() {
    return Objects.hash(details);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DemoAuthResponse {\n");
    sb.append("    details: ").append(toIndentedString(details)).append("\n");
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
    openapiFields.add("details");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DemoAuthResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DemoAuthResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DemoAuthResponse is not found in the empty JSON string", DemoAuthResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DemoAuthResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DemoAuthResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `details`
      if (jsonObj.get("details") != null && !jsonObj.get("details").isJsonNull()) {
        DemoAuthResponseDetails.validateJsonElement(jsonObj.get("details"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DemoAuthResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DemoAuthResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DemoAuthResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DemoAuthResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<DemoAuthResponse>() {
           @Override
           public void write(JsonWriter out, DemoAuthResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DemoAuthResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DemoAuthResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DemoAuthResponse
   * @throws IOException if the JSON string is invalid with respect to DemoAuthResponse
   */
  public static DemoAuthResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DemoAuthResponse.class);
  }

  /**
   * Convert an instance of DemoAuthResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

