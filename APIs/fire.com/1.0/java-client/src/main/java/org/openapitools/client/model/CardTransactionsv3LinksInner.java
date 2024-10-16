/*
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
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
 * CardTransactionsv3LinksInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:07.131817-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CardTransactionsv3LinksInner {
  public static final String SERIALIZED_NAME_HREF = "href";
  @SerializedName(SERIALIZED_NAME_HREF)
  private String href;

  public static final String SERIALIZED_NAME_REL = "rel";
  @SerializedName(SERIALIZED_NAME_REL)
  private String rel;

  public CardTransactionsv3LinksInner() {
  }

  public CardTransactionsv3LinksInner href(String href) {
    this.href = href;
    return this;
  }

  /**
   * https://api.fire.com/business/v3/accounts/1/transactions?startAfter&#x3D;eyJpY2F
   * @return href
   */
  @javax.annotation.Nullable
  public String getHref() {
    return href;
  }

  public void setHref(String href) {
    this.href = href;
  }


  public CardTransactionsv3LinksInner rel(String rel) {
    this.rel = rel;
    return this;
  }

  /**
   * The relationship of this link to the current object - self, next, prev page.
   * @return rel
   */
  @javax.annotation.Nullable
  public String getRel() {
    return rel;
  }

  public void setRel(String rel) {
    this.rel = rel;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CardTransactionsv3LinksInner cardTransactionsv3LinksInner = (CardTransactionsv3LinksInner) o;
    return Objects.equals(this.href, cardTransactionsv3LinksInner.href) &&
        Objects.equals(this.rel, cardTransactionsv3LinksInner.rel);
  }

  @Override
  public int hashCode() {
    return Objects.hash(href, rel);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CardTransactionsv3LinksInner {\n");
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    rel: ").append(toIndentedString(rel)).append("\n");
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
    openapiFields.add("href");
    openapiFields.add("rel");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CardTransactionsv3LinksInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CardTransactionsv3LinksInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CardTransactionsv3LinksInner is not found in the empty JSON string", CardTransactionsv3LinksInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CardTransactionsv3LinksInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CardTransactionsv3LinksInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("href") != null && !jsonObj.get("href").isJsonNull()) && !jsonObj.get("href").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `href` to be a primitive type in the JSON string but got `%s`", jsonObj.get("href").toString()));
      }
      if ((jsonObj.get("rel") != null && !jsonObj.get("rel").isJsonNull()) && !jsonObj.get("rel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rel").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CardTransactionsv3LinksInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CardTransactionsv3LinksInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CardTransactionsv3LinksInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CardTransactionsv3LinksInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CardTransactionsv3LinksInner>() {
           @Override
           public void write(JsonWriter out, CardTransactionsv3LinksInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CardTransactionsv3LinksInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CardTransactionsv3LinksInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CardTransactionsv3LinksInner
   * @throws IOException if the JSON string is invalid with respect to CardTransactionsv3LinksInner
   */
  public static CardTransactionsv3LinksInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CardTransactionsv3LinksInner.class);
  }

  /**
   * Convert an instance of CardTransactionsv3LinksInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

