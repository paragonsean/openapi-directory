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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ListAccountsResponseLinks;
import org.openapitools.client.model.WebhookDeliveryLogResource;

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
 * Successful response to get all delivery logs for a webhook. This returns a paginated list of delivery logs, which can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links if present. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:05.017128-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ListWebhookDeliveryLogsResponse {
  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private List<WebhookDeliveryLogResource> data = new ArrayList<>();

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private ListAccountsResponseLinks links;

  public ListWebhookDeliveryLogsResponse() {
  }

  public ListWebhookDeliveryLogsResponse data(List<WebhookDeliveryLogResource> data) {
    this.data = data;
    return this;
  }

  public ListWebhookDeliveryLogsResponse addDataItem(WebhookDeliveryLogResource dataItem) {
    if (this.data == null) {
      this.data = new ArrayList<>();
    }
    this.data.add(dataItem);
    return this;
  }

  /**
   * The list of delivery logs returned in this response. 
   * @return data
   */
  @javax.annotation.Nonnull
  public List<WebhookDeliveryLogResource> getData() {
    return data;
  }

  public void setData(List<WebhookDeliveryLogResource> data) {
    this.data = data;
  }


  public ListWebhookDeliveryLogsResponse links(ListAccountsResponseLinks links) {
    this.links = links;
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nonnull
  public ListAccountsResponseLinks getLinks() {
    return links;
  }

  public void setLinks(ListAccountsResponseLinks links) {
    this.links = links;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ListWebhookDeliveryLogsResponse listWebhookDeliveryLogsResponse = (ListWebhookDeliveryLogsResponse) o;
    return Objects.equals(this.data, listWebhookDeliveryLogsResponse.data) &&
        Objects.equals(this.links, listWebhookDeliveryLogsResponse.links);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, links);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListWebhookDeliveryLogsResponse {\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
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
    openapiFields.add("data");
    openapiFields.add("links");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("data");
    openapiRequiredFields.add("links");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ListWebhookDeliveryLogsResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ListWebhookDeliveryLogsResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ListWebhookDeliveryLogsResponse is not found in the empty JSON string", ListWebhookDeliveryLogsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ListWebhookDeliveryLogsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ListWebhookDeliveryLogsResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ListWebhookDeliveryLogsResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("data").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `data` to be an array in the JSON string but got `%s`", jsonObj.get("data").toString()));
      }

      JsonArray jsonArraydata = jsonObj.getAsJsonArray("data");
      // validate the required field `data` (array)
      for (int i = 0; i < jsonArraydata.size(); i++) {
        WebhookDeliveryLogResource.validateJsonElement(jsonArraydata.get(i));
      };
      // validate the required field `links`
      ListAccountsResponseLinks.validateJsonElement(jsonObj.get("links"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ListWebhookDeliveryLogsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ListWebhookDeliveryLogsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ListWebhookDeliveryLogsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ListWebhookDeliveryLogsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<ListWebhookDeliveryLogsResponse>() {
           @Override
           public void write(JsonWriter out, ListWebhookDeliveryLogsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ListWebhookDeliveryLogsResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ListWebhookDeliveryLogsResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ListWebhookDeliveryLogsResponse
   * @throws IOException if the JSON string is invalid with respect to ListWebhookDeliveryLogsResponse
   */
  public static ListWebhookDeliveryLogsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ListWebhookDeliveryLogsResponse.class);
  }

  /**
   * Convert an instance of ListWebhookDeliveryLogsResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

