/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
 * QuoteCartManagementV1AssignCustomerPutRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QuoteCartManagementV1AssignCustomerPutRequest {
  public static final String SERIALIZED_NAME_CUSTOMER_ID = "customerId";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ID)
  private Integer customerId;

  public static final String SERIALIZED_NAME_STORE_ID = "storeId";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private Integer storeId;

  public QuoteCartManagementV1AssignCustomerPutRequest() {
  }

  public QuoteCartManagementV1AssignCustomerPutRequest customerId(Integer customerId) {
    this.customerId = customerId;
    return this;
  }

  /**
   * The customer ID.
   * @return customerId
   */
  @javax.annotation.Nonnull
  public Integer getCustomerId() {
    return customerId;
  }

  public void setCustomerId(Integer customerId) {
    this.customerId = customerId;
  }


  public QuoteCartManagementV1AssignCustomerPutRequest storeId(Integer storeId) {
    this.storeId = storeId;
    return this;
  }

  /**
   * Get storeId
   * @return storeId
   */
  @javax.annotation.Nonnull
  public Integer getStoreId() {
    return storeId;
  }

  public void setStoreId(Integer storeId) {
    this.storeId = storeId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QuoteCartManagementV1AssignCustomerPutRequest quoteCartManagementV1AssignCustomerPutRequest = (QuoteCartManagementV1AssignCustomerPutRequest) o;
    return Objects.equals(this.customerId, quoteCartManagementV1AssignCustomerPutRequest.customerId) &&
        Objects.equals(this.storeId, quoteCartManagementV1AssignCustomerPutRequest.storeId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(customerId, storeId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QuoteCartManagementV1AssignCustomerPutRequest {\n");
    sb.append("    customerId: ").append(toIndentedString(customerId)).append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
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
    openapiFields.add("customerId");
    openapiFields.add("storeId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("customerId");
    openapiRequiredFields.add("storeId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QuoteCartManagementV1AssignCustomerPutRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QuoteCartManagementV1AssignCustomerPutRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QuoteCartManagementV1AssignCustomerPutRequest is not found in the empty JSON string", QuoteCartManagementV1AssignCustomerPutRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QuoteCartManagementV1AssignCustomerPutRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QuoteCartManagementV1AssignCustomerPutRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : QuoteCartManagementV1AssignCustomerPutRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QuoteCartManagementV1AssignCustomerPutRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QuoteCartManagementV1AssignCustomerPutRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QuoteCartManagementV1AssignCustomerPutRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QuoteCartManagementV1AssignCustomerPutRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<QuoteCartManagementV1AssignCustomerPutRequest>() {
           @Override
           public void write(JsonWriter out, QuoteCartManagementV1AssignCustomerPutRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QuoteCartManagementV1AssignCustomerPutRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QuoteCartManagementV1AssignCustomerPutRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QuoteCartManagementV1AssignCustomerPutRequest
   * @throws IOException if the JSON string is invalid with respect to QuoteCartManagementV1AssignCustomerPutRequest
   */
  public static QuoteCartManagementV1AssignCustomerPutRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QuoteCartManagementV1AssignCustomerPutRequest.class);
  }

  /**
   * Convert an instance of QuoteCartManagementV1AssignCustomerPutRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

