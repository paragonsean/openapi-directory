/*
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
import java.util.Arrays;
import org.openapitools.client.model.IPeriodRateOfReturnDetails;

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
 * IRateOfReturnDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IRateOfReturnDetails {
  public static final String SERIALIZED_NAME_PRE_RETIREMENT = "preRetirement";
  @SerializedName(SERIALIZED_NAME_PRE_RETIREMENT)
  private IPeriodRateOfReturnDetails preRetirement;

  public static final String SERIALIZED_NAME_RETIREMENT = "retirement";
  @SerializedName(SERIALIZED_NAME_RETIREMENT)
  private IPeriodRateOfReturnDetails retirement;

  public IRateOfReturnDetails() {
  }

  public IRateOfReturnDetails preRetirement(IPeriodRateOfReturnDetails preRetirement) {
    this.preRetirement = preRetirement;
    return this;
  }

  /**
   * Get preRetirement
   * @return preRetirement
   */
  @javax.annotation.Nullable
  public IPeriodRateOfReturnDetails getPreRetirement() {
    return preRetirement;
  }

  public void setPreRetirement(IPeriodRateOfReturnDetails preRetirement) {
    this.preRetirement = preRetirement;
  }


  public IRateOfReturnDetails retirement(IPeriodRateOfReturnDetails retirement) {
    this.retirement = retirement;
    return this;
  }

  /**
   * Get retirement
   * @return retirement
   */
  @javax.annotation.Nullable
  public IPeriodRateOfReturnDetails getRetirement() {
    return retirement;
  }

  public void setRetirement(IPeriodRateOfReturnDetails retirement) {
    this.retirement = retirement;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IRateOfReturnDetails irateOfReturnDetails = (IRateOfReturnDetails) o;
    return Objects.equals(this.preRetirement, irateOfReturnDetails.preRetirement) &&
        Objects.equals(this.retirement, irateOfReturnDetails.retirement);
  }

  @Override
  public int hashCode() {
    return Objects.hash(preRetirement, retirement);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IRateOfReturnDetails {\n");
    sb.append("    preRetirement: ").append(toIndentedString(preRetirement)).append("\n");
    sb.append("    retirement: ").append(toIndentedString(retirement)).append("\n");
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
    openapiFields.add("preRetirement");
    openapiFields.add("retirement");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IRateOfReturnDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IRateOfReturnDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IRateOfReturnDetails is not found in the empty JSON string", IRateOfReturnDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IRateOfReturnDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IRateOfReturnDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `preRetirement`
      if (jsonObj.get("preRetirement") != null && !jsonObj.get("preRetirement").isJsonNull()) {
        IPeriodRateOfReturnDetails.validateJsonElement(jsonObj.get("preRetirement"));
      }
      // validate the optional field `retirement`
      if (jsonObj.get("retirement") != null && !jsonObj.get("retirement").isJsonNull()) {
        IPeriodRateOfReturnDetails.validateJsonElement(jsonObj.get("retirement"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IRateOfReturnDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IRateOfReturnDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IRateOfReturnDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IRateOfReturnDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<IRateOfReturnDetails>() {
           @Override
           public void write(JsonWriter out, IRateOfReturnDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IRateOfReturnDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IRateOfReturnDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IRateOfReturnDetails
   * @throws IOException if the JSON string is invalid with respect to IRateOfReturnDetails
   */
  public static IRateOfReturnDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IRateOfReturnDetails.class);
  }

  /**
   * Convert an instance of IRateOfReturnDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

