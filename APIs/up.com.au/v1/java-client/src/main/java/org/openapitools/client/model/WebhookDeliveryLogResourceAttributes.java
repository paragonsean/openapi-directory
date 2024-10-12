/*
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
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
import org.openapitools.client.model.WebhookDeliveryLogResourceAttributesRequest;
import org.openapitools.client.model.WebhookDeliveryLogResourceAttributesResponse;
import org.openapitools.client.model.WebhookDeliveryStatusEnum;

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
 * WebhookDeliveryLogResourceAttributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:05.017128-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WebhookDeliveryLogResourceAttributes {
  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DELIVERY_STATUS = "deliveryStatus";
  @SerializedName(SERIALIZED_NAME_DELIVERY_STATUS)
  private WebhookDeliveryStatusEnum deliveryStatus;

  public static final String SERIALIZED_NAME_REQUEST = "request";
  @SerializedName(SERIALIZED_NAME_REQUEST)
  private WebhookDeliveryLogResourceAttributesRequest request;

  public static final String SERIALIZED_NAME_RESPONSE = "response";
  @SerializedName(SERIALIZED_NAME_RESPONSE)
  private WebhookDeliveryLogResourceAttributesResponse response;

  public WebhookDeliveryLogResourceAttributes() {
  }

  public WebhookDeliveryLogResourceAttributes createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * The date-time at which this log entry was created. 
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public WebhookDeliveryLogResourceAttributes deliveryStatus(WebhookDeliveryStatusEnum deliveryStatus) {
    this.deliveryStatus = deliveryStatus;
    return this;
  }

  /**
   * The success or failure status of this delivery attempt. 
   * @return deliveryStatus
   */
  @javax.annotation.Nonnull
  public WebhookDeliveryStatusEnum getDeliveryStatus() {
    return deliveryStatus;
  }

  public void setDeliveryStatus(WebhookDeliveryStatusEnum deliveryStatus) {
    this.deliveryStatus = deliveryStatus;
  }


  public WebhookDeliveryLogResourceAttributes request(WebhookDeliveryLogResourceAttributesRequest request) {
    this.request = request;
    return this;
  }

  /**
   * Get request
   * @return request
   */
  @javax.annotation.Nonnull
  public WebhookDeliveryLogResourceAttributesRequest getRequest() {
    return request;
  }

  public void setRequest(WebhookDeliveryLogResourceAttributesRequest request) {
    this.request = request;
  }


  public WebhookDeliveryLogResourceAttributes response(WebhookDeliveryLogResourceAttributesResponse response) {
    this.response = response;
    return this;
  }

  /**
   * Get response
   * @return response
   */
  @javax.annotation.Nullable
  public WebhookDeliveryLogResourceAttributesResponse getResponse() {
    return response;
  }

  public void setResponse(WebhookDeliveryLogResourceAttributesResponse response) {
    this.response = response;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebhookDeliveryLogResourceAttributes webhookDeliveryLogResourceAttributes = (WebhookDeliveryLogResourceAttributes) o;
    return Objects.equals(this.createdAt, webhookDeliveryLogResourceAttributes.createdAt) &&
        Objects.equals(this.deliveryStatus, webhookDeliveryLogResourceAttributes.deliveryStatus) &&
        Objects.equals(this.request, webhookDeliveryLogResourceAttributes.request) &&
        Objects.equals(this.response, webhookDeliveryLogResourceAttributes.response);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, deliveryStatus, request, response);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebhookDeliveryLogResourceAttributes {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    deliveryStatus: ").append(toIndentedString(deliveryStatus)).append("\n");
    sb.append("    request: ").append(toIndentedString(request)).append("\n");
    sb.append("    response: ").append(toIndentedString(response)).append("\n");
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
    openapiFields.add("createdAt");
    openapiFields.add("deliveryStatus");
    openapiFields.add("request");
    openapiFields.add("response");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("deliveryStatus");
    openapiRequiredFields.add("request");
    openapiRequiredFields.add("response");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WebhookDeliveryLogResourceAttributes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WebhookDeliveryLogResourceAttributes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WebhookDeliveryLogResourceAttributes is not found in the empty JSON string", WebhookDeliveryLogResourceAttributes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WebhookDeliveryLogResourceAttributes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WebhookDeliveryLogResourceAttributes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : WebhookDeliveryLogResourceAttributes.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `deliveryStatus`
      WebhookDeliveryStatusEnum.validateJsonElement(jsonObj.get("deliveryStatus"));
      // validate the required field `request`
      WebhookDeliveryLogResourceAttributesRequest.validateJsonElement(jsonObj.get("request"));
      // validate the required field `response`
      WebhookDeliveryLogResourceAttributesResponse.validateJsonElement(jsonObj.get("response"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WebhookDeliveryLogResourceAttributes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WebhookDeliveryLogResourceAttributes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WebhookDeliveryLogResourceAttributes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WebhookDeliveryLogResourceAttributes.class));

       return (TypeAdapter<T>) new TypeAdapter<WebhookDeliveryLogResourceAttributes>() {
           @Override
           public void write(JsonWriter out, WebhookDeliveryLogResourceAttributes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WebhookDeliveryLogResourceAttributes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WebhookDeliveryLogResourceAttributes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WebhookDeliveryLogResourceAttributes
   * @throws IOException if the JSON string is invalid with respect to WebhookDeliveryLogResourceAttributes
   */
  public static WebhookDeliveryLogResourceAttributes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WebhookDeliveryLogResourceAttributes.class);
  }

  /**
   * Convert an instance of WebhookDeliveryLogResourceAttributes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

