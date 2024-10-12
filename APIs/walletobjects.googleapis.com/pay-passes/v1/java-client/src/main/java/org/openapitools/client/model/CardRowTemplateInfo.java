/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import org.openapitools.client.model.CardRowOneItem;
import org.openapitools.client.model.CardRowThreeItems;
import org.openapitools.client.model.CardRowTwoItems;

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
 * CardRowTemplateInfo
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CardRowTemplateInfo {
  public static final String SERIALIZED_NAME_ONE_ITEM = "oneItem";
  @SerializedName(SERIALIZED_NAME_ONE_ITEM)
  private CardRowOneItem oneItem;

  public static final String SERIALIZED_NAME_THREE_ITEMS = "threeItems";
  @SerializedName(SERIALIZED_NAME_THREE_ITEMS)
  private CardRowThreeItems threeItems;

  public static final String SERIALIZED_NAME_TWO_ITEMS = "twoItems";
  @SerializedName(SERIALIZED_NAME_TWO_ITEMS)
  private CardRowTwoItems twoItems;

  public CardRowTemplateInfo() {
  }

  public CardRowTemplateInfo oneItem(CardRowOneItem oneItem) {
    this.oneItem = oneItem;
    return this;
  }

  /**
   * Get oneItem
   * @return oneItem
   */
  @javax.annotation.Nullable
  public CardRowOneItem getOneItem() {
    return oneItem;
  }

  public void setOneItem(CardRowOneItem oneItem) {
    this.oneItem = oneItem;
  }


  public CardRowTemplateInfo threeItems(CardRowThreeItems threeItems) {
    this.threeItems = threeItems;
    return this;
  }

  /**
   * Get threeItems
   * @return threeItems
   */
  @javax.annotation.Nullable
  public CardRowThreeItems getThreeItems() {
    return threeItems;
  }

  public void setThreeItems(CardRowThreeItems threeItems) {
    this.threeItems = threeItems;
  }


  public CardRowTemplateInfo twoItems(CardRowTwoItems twoItems) {
    this.twoItems = twoItems;
    return this;
  }

  /**
   * Get twoItems
   * @return twoItems
   */
  @javax.annotation.Nullable
  public CardRowTwoItems getTwoItems() {
    return twoItems;
  }

  public void setTwoItems(CardRowTwoItems twoItems) {
    this.twoItems = twoItems;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CardRowTemplateInfo cardRowTemplateInfo = (CardRowTemplateInfo) o;
    return Objects.equals(this.oneItem, cardRowTemplateInfo.oneItem) &&
        Objects.equals(this.threeItems, cardRowTemplateInfo.threeItems) &&
        Objects.equals(this.twoItems, cardRowTemplateInfo.twoItems);
  }

  @Override
  public int hashCode() {
    return Objects.hash(oneItem, threeItems, twoItems);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CardRowTemplateInfo {\n");
    sb.append("    oneItem: ").append(toIndentedString(oneItem)).append("\n");
    sb.append("    threeItems: ").append(toIndentedString(threeItems)).append("\n");
    sb.append("    twoItems: ").append(toIndentedString(twoItems)).append("\n");
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
    openapiFields.add("oneItem");
    openapiFields.add("threeItems");
    openapiFields.add("twoItems");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CardRowTemplateInfo
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CardRowTemplateInfo.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CardRowTemplateInfo is not found in the empty JSON string", CardRowTemplateInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CardRowTemplateInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CardRowTemplateInfo` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `oneItem`
      if (jsonObj.get("oneItem") != null && !jsonObj.get("oneItem").isJsonNull()) {
        CardRowOneItem.validateJsonElement(jsonObj.get("oneItem"));
      }
      // validate the optional field `threeItems`
      if (jsonObj.get("threeItems") != null && !jsonObj.get("threeItems").isJsonNull()) {
        CardRowThreeItems.validateJsonElement(jsonObj.get("threeItems"));
      }
      // validate the optional field `twoItems`
      if (jsonObj.get("twoItems") != null && !jsonObj.get("twoItems").isJsonNull()) {
        CardRowTwoItems.validateJsonElement(jsonObj.get("twoItems"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CardRowTemplateInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CardRowTemplateInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CardRowTemplateInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CardRowTemplateInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<CardRowTemplateInfo>() {
           @Override
           public void write(JsonWriter out, CardRowTemplateInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CardRowTemplateInfo read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CardRowTemplateInfo given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CardRowTemplateInfo
   * @throws IOException if the JSON string is invalid with respect to CardRowTemplateInfo
   */
  public static CardRowTemplateInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CardRowTemplateInfo.class);
  }

  /**
   * Convert an instance of CardRowTemplateInfo to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

