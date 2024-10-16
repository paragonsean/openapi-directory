/*
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
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
import org.openapitools.client.model.HotelList;

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
 * Defines whether all properties or a subset of properties in the Hotel Center account can be managed with the linked Google Ads account. If a subset, the specific properties are specified.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:52.320664-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AccountLinkTarget {
  public static final String SERIALIZED_NAME_ALL_HOTELS = "allHotels";
  @SerializedName(SERIALIZED_NAME_ALL_HOTELS)
  private Boolean allHotels;

  public static final String SERIALIZED_NAME_HOTEL_LIST = "hotelList";
  @SerializedName(SERIALIZED_NAME_HOTEL_LIST)
  private HotelList hotelList;

  public AccountLinkTarget() {
  }

  public AccountLinkTarget allHotels(Boolean allHotels) {
    this.allHotels = allHotels;
    return this;
  }

  /**
   * True if all properties under the Hotel Center account are made available to the account link. The default is &#x60;false&#x60;.
   * @return allHotels
   */
  @javax.annotation.Nullable
  public Boolean getAllHotels() {
    return allHotels;
  }

  public void setAllHotels(Boolean allHotels) {
    this.allHotels = allHotels;
  }


  public AccountLinkTarget hotelList(HotelList hotelList) {
    this.hotelList = hotelList;
    return this;
  }

  /**
   * Get hotelList
   * @return hotelList
   */
  @javax.annotation.Nullable
  public HotelList getHotelList() {
    return hotelList;
  }

  public void setHotelList(HotelList hotelList) {
    this.hotelList = hotelList;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccountLinkTarget accountLinkTarget = (AccountLinkTarget) o;
    return Objects.equals(this.allHotels, accountLinkTarget.allHotels) &&
        Objects.equals(this.hotelList, accountLinkTarget.hotelList);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allHotels, hotelList);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccountLinkTarget {\n");
    sb.append("    allHotels: ").append(toIndentedString(allHotels)).append("\n");
    sb.append("    hotelList: ").append(toIndentedString(hotelList)).append("\n");
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
    openapiFields.add("allHotels");
    openapiFields.add("hotelList");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AccountLinkTarget
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AccountLinkTarget.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AccountLinkTarget is not found in the empty JSON string", AccountLinkTarget.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AccountLinkTarget.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AccountLinkTarget` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `hotelList`
      if (jsonObj.get("hotelList") != null && !jsonObj.get("hotelList").isJsonNull()) {
        HotelList.validateJsonElement(jsonObj.get("hotelList"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AccountLinkTarget.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AccountLinkTarget' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AccountLinkTarget> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AccountLinkTarget.class));

       return (TypeAdapter<T>) new TypeAdapter<AccountLinkTarget>() {
           @Override
           public void write(JsonWriter out, AccountLinkTarget value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AccountLinkTarget read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AccountLinkTarget given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AccountLinkTarget
   * @throws IOException if the JSON string is invalid with respect to AccountLinkTarget
   */
  public static AccountLinkTarget fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AccountLinkTarget.class);
  }

  /**
   * Convert an instance of AccountLinkTarget to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

