/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import org.openapitools.client.model.BillingAggregatedInformationGetByApp200Response;

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
 * Aggregated Billing Information for a user an the organizations in which the user is an admin.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BillingAggregatedInformationGetAll200Response {
  public static final String SERIALIZED_NAME_AGGREGATED_BILLINGS = "aggregatedBillings";
  @SerializedName(SERIALIZED_NAME_AGGREGATED_BILLINGS)
  private BillingAggregatedInformationGetByApp200Response aggregatedBillings;

  public BillingAggregatedInformationGetAll200Response() {
  }

  public BillingAggregatedInformationGetAll200Response aggregatedBillings(BillingAggregatedInformationGetByApp200Response aggregatedBillings) {
    this.aggregatedBillings = aggregatedBillings;
    return this;
  }

  /**
   * Get aggregatedBillings
   * @return aggregatedBillings
   */
  @javax.annotation.Nullable
  public BillingAggregatedInformationGetByApp200Response getAggregatedBillings() {
    return aggregatedBillings;
  }

  public void setAggregatedBillings(BillingAggregatedInformationGetByApp200Response aggregatedBillings) {
    this.aggregatedBillings = aggregatedBillings;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BillingAggregatedInformationGetAll200Response billingAggregatedInformationGetAll200Response = (BillingAggregatedInformationGetAll200Response) o;
    return Objects.equals(this.aggregatedBillings, billingAggregatedInformationGetAll200Response.aggregatedBillings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aggregatedBillings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BillingAggregatedInformationGetAll200Response {\n");
    sb.append("    aggregatedBillings: ").append(toIndentedString(aggregatedBillings)).append("\n");
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
    openapiFields.add("aggregatedBillings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BillingAggregatedInformationGetAll200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BillingAggregatedInformationGetAll200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BillingAggregatedInformationGetAll200Response is not found in the empty JSON string", BillingAggregatedInformationGetAll200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BillingAggregatedInformationGetAll200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BillingAggregatedInformationGetAll200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `aggregatedBillings`
      if (jsonObj.get("aggregatedBillings") != null && !jsonObj.get("aggregatedBillings").isJsonNull()) {
        BillingAggregatedInformationGetByApp200Response.validateJsonElement(jsonObj.get("aggregatedBillings"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BillingAggregatedInformationGetAll200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BillingAggregatedInformationGetAll200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BillingAggregatedInformationGetAll200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BillingAggregatedInformationGetAll200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<BillingAggregatedInformationGetAll200Response>() {
           @Override
           public void write(JsonWriter out, BillingAggregatedInformationGetAll200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BillingAggregatedInformationGetAll200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BillingAggregatedInformationGetAll200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BillingAggregatedInformationGetAll200Response
   * @throws IOException if the JSON string is invalid with respect to BillingAggregatedInformationGetAll200Response
   */
  public static BillingAggregatedInformationGetAll200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BillingAggregatedInformationGetAll200Response.class);
  }

  /**
   * Convert an instance of BillingAggregatedInformationGetAll200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

