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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.HotelPricePerItinerary;

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
 * A price view. Covers the Prices functionality in pre-v3.0 API versions.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:52.320664-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PriceView {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PER_ITINERARY_PRICES = "perItineraryPrices";
  @SerializedName(SERIALIZED_NAME_PER_ITINERARY_PRICES)
  private List<HotelPricePerItinerary> perItineraryPrices = new ArrayList<>();

  public PriceView() {
  }

  public PriceView name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Resource name in the format &#x60;accounts/{account_id}/priceViews/{partner_hotel_id}&#x60;.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PriceView perItineraryPrices(List<HotelPricePerItinerary> perItineraryPrices) {
    this.perItineraryPrices = perItineraryPrices;
    return this;
  }

  public PriceView addPerItineraryPricesItem(HotelPricePerItinerary perItineraryPricesItem) {
    if (this.perItineraryPrices == null) {
      this.perItineraryPrices = new ArrayList<>();
    }
    this.perItineraryPrices.add(perItineraryPricesItem);
    return this;
  }

  /**
   * Price for each itinerary.
   * @return perItineraryPrices
   */
  @javax.annotation.Nullable
  public List<HotelPricePerItinerary> getPerItineraryPrices() {
    return perItineraryPrices;
  }

  public void setPerItineraryPrices(List<HotelPricePerItinerary> perItineraryPrices) {
    this.perItineraryPrices = perItineraryPrices;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PriceView priceView = (PriceView) o;
    return Objects.equals(this.name, priceView.name) &&
        Objects.equals(this.perItineraryPrices, priceView.perItineraryPrices);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, perItineraryPrices);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PriceView {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    perItineraryPrices: ").append(toIndentedString(perItineraryPrices)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("perItineraryPrices");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PriceView
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PriceView.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PriceView is not found in the empty JSON string", PriceView.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PriceView.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PriceView` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("perItineraryPrices") != null && !jsonObj.get("perItineraryPrices").isJsonNull()) {
        JsonArray jsonArrayperItineraryPrices = jsonObj.getAsJsonArray("perItineraryPrices");
        if (jsonArrayperItineraryPrices != null) {
          // ensure the json data is an array
          if (!jsonObj.get("perItineraryPrices").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `perItineraryPrices` to be an array in the JSON string but got `%s`", jsonObj.get("perItineraryPrices").toString()));
          }

          // validate the optional field `perItineraryPrices` (array)
          for (int i = 0; i < jsonArrayperItineraryPrices.size(); i++) {
            HotelPricePerItinerary.validateJsonElement(jsonArrayperItineraryPrices.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PriceView.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PriceView' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PriceView> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PriceView.class));

       return (TypeAdapter<T>) new TypeAdapter<PriceView>() {
           @Override
           public void write(JsonWriter out, PriceView value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PriceView read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PriceView given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PriceView
   * @throws IOException if the JSON string is invalid with respect to PriceView
   */
  public static PriceView fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PriceView.class);
  }

  /**
   * Convert an instance of PriceView to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

