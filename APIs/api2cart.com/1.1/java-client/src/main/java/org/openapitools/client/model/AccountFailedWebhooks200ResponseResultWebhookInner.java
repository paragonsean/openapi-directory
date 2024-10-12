/*
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
import org.openapitools.client.model.A2CDateTime;

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
 * AccountFailedWebhooks200ResponseResultWebhookInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AccountFailedWebhooks200ResponseResultWebhookInner {
  public static final String SERIALIZED_NAME_ENTITY_ID = "entity_id";
  @SerializedName(SERIALIZED_NAME_ENTITY_ID)
  private String entityId;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private A2CDateTime time;

  public static final String SERIALIZED_NAME_WEBHOOK_ID = "webhook_id";
  @SerializedName(SERIALIZED_NAME_WEBHOOK_ID)
  private Integer webhookId;

  public AccountFailedWebhooks200ResponseResultWebhookInner() {
  }

  public AccountFailedWebhooks200ResponseResultWebhookInner entityId(String entityId) {
    this.entityId = entityId;
    return this;
  }

  /**
   * Get entityId
   * @return entityId
   */
  @javax.annotation.Nullable
  public String getEntityId() {
    return entityId;
  }

  public void setEntityId(String entityId) {
    this.entityId = entityId;
  }


  public AccountFailedWebhooks200ResponseResultWebhookInner time(A2CDateTime time) {
    this.time = time;
    return this;
  }

  /**
   * Get time
   * @return time
   */
  @javax.annotation.Nullable
  public A2CDateTime getTime() {
    return time;
  }

  public void setTime(A2CDateTime time) {
    this.time = time;
  }


  public AccountFailedWebhooks200ResponseResultWebhookInner webhookId(Integer webhookId) {
    this.webhookId = webhookId;
    return this;
  }

  /**
   * Get webhookId
   * @return webhookId
   */
  @javax.annotation.Nullable
  public Integer getWebhookId() {
    return webhookId;
  }

  public void setWebhookId(Integer webhookId) {
    this.webhookId = webhookId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccountFailedWebhooks200ResponseResultWebhookInner accountFailedWebhooks200ResponseResultWebhookInner = (AccountFailedWebhooks200ResponseResultWebhookInner) o;
    return Objects.equals(this.entityId, accountFailedWebhooks200ResponseResultWebhookInner.entityId) &&
        Objects.equals(this.time, accountFailedWebhooks200ResponseResultWebhookInner.time) &&
        Objects.equals(this.webhookId, accountFailedWebhooks200ResponseResultWebhookInner.webhookId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(entityId, time, webhookId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccountFailedWebhooks200ResponseResultWebhookInner {\n");
    sb.append("    entityId: ").append(toIndentedString(entityId)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
    sb.append("    webhookId: ").append(toIndentedString(webhookId)).append("\n");
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
    openapiFields.add("entity_id");
    openapiFields.add("time");
    openapiFields.add("webhook_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AccountFailedWebhooks200ResponseResultWebhookInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AccountFailedWebhooks200ResponseResultWebhookInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AccountFailedWebhooks200ResponseResultWebhookInner is not found in the empty JSON string", AccountFailedWebhooks200ResponseResultWebhookInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AccountFailedWebhooks200ResponseResultWebhookInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AccountFailedWebhooks200ResponseResultWebhookInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("entity_id") != null && !jsonObj.get("entity_id").isJsonNull()) && !jsonObj.get("entity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entity_id").toString()));
      }
      // validate the optional field `time`
      if (jsonObj.get("time") != null && !jsonObj.get("time").isJsonNull()) {
        A2CDateTime.validateJsonElement(jsonObj.get("time"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AccountFailedWebhooks200ResponseResultWebhookInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AccountFailedWebhooks200ResponseResultWebhookInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AccountFailedWebhooks200ResponseResultWebhookInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AccountFailedWebhooks200ResponseResultWebhookInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AccountFailedWebhooks200ResponseResultWebhookInner>() {
           @Override
           public void write(JsonWriter out, AccountFailedWebhooks200ResponseResultWebhookInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AccountFailedWebhooks200ResponseResultWebhookInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AccountFailedWebhooks200ResponseResultWebhookInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AccountFailedWebhooks200ResponseResultWebhookInner
   * @throws IOException if the JSON string is invalid with respect to AccountFailedWebhooks200ResponseResultWebhookInner
   */
  public static AccountFailedWebhooks200ResponseResultWebhookInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AccountFailedWebhooks200ResponseResultWebhookInner.class);
  }

  /**
   * Convert an instance of AccountFailedWebhooks200ResponseResultWebhookInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

