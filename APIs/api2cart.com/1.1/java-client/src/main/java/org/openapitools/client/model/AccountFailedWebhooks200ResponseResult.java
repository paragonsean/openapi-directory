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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AccountFailedWebhooks200ResponseResultWebhookInner;

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
 * AccountFailedWebhooks200ResponseResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AccountFailedWebhooks200ResponseResult {
  public static final String SERIALIZED_NAME_ALL_FAILED_WEBHOOK = "all_failed_webhook";
  @SerializedName(SERIALIZED_NAME_ALL_FAILED_WEBHOOK)
  private String allFailedWebhook;

  public static final String SERIALIZED_NAME_WEBHOOK = "webhook";
  @SerializedName(SERIALIZED_NAME_WEBHOOK)
  private List<AccountFailedWebhooks200ResponseResultWebhookInner> webhook = new ArrayList<>();

  public AccountFailedWebhooks200ResponseResult() {
  }

  public AccountFailedWebhooks200ResponseResult allFailedWebhook(String allFailedWebhook) {
    this.allFailedWebhook = allFailedWebhook;
    return this;
  }

  /**
   * Get allFailedWebhook
   * @return allFailedWebhook
   */
  @javax.annotation.Nullable
  public String getAllFailedWebhook() {
    return allFailedWebhook;
  }

  public void setAllFailedWebhook(String allFailedWebhook) {
    this.allFailedWebhook = allFailedWebhook;
  }


  public AccountFailedWebhooks200ResponseResult webhook(List<AccountFailedWebhooks200ResponseResultWebhookInner> webhook) {
    this.webhook = webhook;
    return this;
  }

  public AccountFailedWebhooks200ResponseResult addWebhookItem(AccountFailedWebhooks200ResponseResultWebhookInner webhookItem) {
    if (this.webhook == null) {
      this.webhook = new ArrayList<>();
    }
    this.webhook.add(webhookItem);
    return this;
  }

  /**
   * Get webhook
   * @return webhook
   */
  @javax.annotation.Nullable
  public List<AccountFailedWebhooks200ResponseResultWebhookInner> getWebhook() {
    return webhook;
  }

  public void setWebhook(List<AccountFailedWebhooks200ResponseResultWebhookInner> webhook) {
    this.webhook = webhook;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccountFailedWebhooks200ResponseResult accountFailedWebhooks200ResponseResult = (AccountFailedWebhooks200ResponseResult) o;
    return Objects.equals(this.allFailedWebhook, accountFailedWebhooks200ResponseResult.allFailedWebhook) &&
        Objects.equals(this.webhook, accountFailedWebhooks200ResponseResult.webhook);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allFailedWebhook, webhook);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccountFailedWebhooks200ResponseResult {\n");
    sb.append("    allFailedWebhook: ").append(toIndentedString(allFailedWebhook)).append("\n");
    sb.append("    webhook: ").append(toIndentedString(webhook)).append("\n");
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
    openapiFields.add("all_failed_webhook");
    openapiFields.add("webhook");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AccountFailedWebhooks200ResponseResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AccountFailedWebhooks200ResponseResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AccountFailedWebhooks200ResponseResult is not found in the empty JSON string", AccountFailedWebhooks200ResponseResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AccountFailedWebhooks200ResponseResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AccountFailedWebhooks200ResponseResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("all_failed_webhook") != null && !jsonObj.get("all_failed_webhook").isJsonNull()) && !jsonObj.get("all_failed_webhook").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `all_failed_webhook` to be a primitive type in the JSON string but got `%s`", jsonObj.get("all_failed_webhook").toString()));
      }
      if (jsonObj.get("webhook") != null && !jsonObj.get("webhook").isJsonNull()) {
        JsonArray jsonArraywebhook = jsonObj.getAsJsonArray("webhook");
        if (jsonArraywebhook != null) {
          // ensure the json data is an array
          if (!jsonObj.get("webhook").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `webhook` to be an array in the JSON string but got `%s`", jsonObj.get("webhook").toString()));
          }

          // validate the optional field `webhook` (array)
          for (int i = 0; i < jsonArraywebhook.size(); i++) {
            AccountFailedWebhooks200ResponseResultWebhookInner.validateJsonElement(jsonArraywebhook.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AccountFailedWebhooks200ResponseResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AccountFailedWebhooks200ResponseResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AccountFailedWebhooks200ResponseResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AccountFailedWebhooks200ResponseResult.class));

       return (TypeAdapter<T>) new TypeAdapter<AccountFailedWebhooks200ResponseResult>() {
           @Override
           public void write(JsonWriter out, AccountFailedWebhooks200ResponseResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AccountFailedWebhooks200ResponseResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AccountFailedWebhooks200ResponseResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AccountFailedWebhooks200ResponseResult
   * @throws IOException if the JSON string is invalid with respect to AccountFailedWebhooks200ResponseResult
   */
  public static AccountFailedWebhooks200ResponseResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AccountFailedWebhooks200ResponseResult.class);
  }

  /**
   * Convert an instance of AccountFailedWebhooks200ResponseResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

