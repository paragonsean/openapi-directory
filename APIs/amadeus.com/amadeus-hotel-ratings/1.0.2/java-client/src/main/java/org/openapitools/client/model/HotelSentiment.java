/*
 * Hotel Ratings
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, this API in test only offers 24 hotels; 10 in London and 14 in New-York. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.2
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
import org.openapitools.client.model.HotelSentimentSentiments;

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
 * HotelSentiment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:38.818955-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HotelSentiment {
  public static final String SERIALIZED_NAME_HOTEL_ID = "hotelId";
  @SerializedName(SERIALIZED_NAME_HOTEL_ID)
  private String hotelId;

  public static final String SERIALIZED_NAME_NUMBER_OF_RATINGS = "numberOfRatings";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_RATINGS)
  private Integer numberOfRatings;

  public static final String SERIALIZED_NAME_NUMBER_OF_REVIEWS = "numberOfReviews";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_REVIEWS)
  private Integer numberOfReviews;

  public static final String SERIALIZED_NAME_OVERALL_RATING = "overallRating";
  @SerializedName(SERIALIZED_NAME_OVERALL_RATING)
  private Integer overallRating;

  public static final String SERIALIZED_NAME_SENTIMENTS = "sentiments";
  @SerializedName(SERIALIZED_NAME_SENTIMENTS)
  private HotelSentimentSentiments sentiments;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public HotelSentiment() {
  }

  public HotelSentiment hotelId(String hotelId) {
    this.hotelId = hotelId;
    return this;
  }

  /**
   * Amadeus Hotel Ids are found in the Hotel Search response (parameter name is &#39;hotelId&#39;)
   * @return hotelId
   */
  @javax.annotation.Nonnull
  public String getHotelId() {
    return hotelId;
  }

  public void setHotelId(String hotelId) {
    this.hotelId = hotelId;
  }


  public HotelSentiment numberOfRatings(Integer numberOfRatings) {
    this.numberOfRatings = numberOfRatings;
    return this;
  }

  /**
   * Get numberOfRatings
   * @return numberOfRatings
   */
  @javax.annotation.Nonnull
  public Integer getNumberOfRatings() {
    return numberOfRatings;
  }

  public void setNumberOfRatings(Integer numberOfRatings) {
    this.numberOfRatings = numberOfRatings;
  }


  public HotelSentiment numberOfReviews(Integer numberOfReviews) {
    this.numberOfReviews = numberOfReviews;
    return this;
  }

  /**
   * Get numberOfReviews
   * @return numberOfReviews
   */
  @javax.annotation.Nonnull
  public Integer getNumberOfReviews() {
    return numberOfReviews;
  }

  public void setNumberOfReviews(Integer numberOfReviews) {
    this.numberOfReviews = numberOfReviews;
  }


  public HotelSentiment overallRating(Integer overallRating) {
    this.overallRating = overallRating;
    return this;
  }

  /**
   * Integer between 0 and 100. It represents the score for a specific category or the overall rating for a given Hotel.
   * @return overallRating
   */
  @javax.annotation.Nonnull
  public Integer getOverallRating() {
    return overallRating;
  }

  public void setOverallRating(Integer overallRating) {
    this.overallRating = overallRating;
  }


  public HotelSentiment sentiments(HotelSentimentSentiments sentiments) {
    this.sentiments = sentiments;
    return this;
  }

  /**
   * Get sentiments
   * @return sentiments
   */
  @javax.annotation.Nullable
  public HotelSentimentSentiments getSentiments() {
    return sentiments;
  }

  public void setSentiments(HotelSentimentSentiments sentiments) {
    this.sentiments = sentiments;
  }


  public HotelSentiment type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HotelSentiment hotelSentiment = (HotelSentiment) o;
    return Objects.equals(this.hotelId, hotelSentiment.hotelId) &&
        Objects.equals(this.numberOfRatings, hotelSentiment.numberOfRatings) &&
        Objects.equals(this.numberOfReviews, hotelSentiment.numberOfReviews) &&
        Objects.equals(this.overallRating, hotelSentiment.overallRating) &&
        Objects.equals(this.sentiments, hotelSentiment.sentiments) &&
        Objects.equals(this.type, hotelSentiment.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hotelId, numberOfRatings, numberOfReviews, overallRating, sentiments, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HotelSentiment {\n");
    sb.append("    hotelId: ").append(toIndentedString(hotelId)).append("\n");
    sb.append("    numberOfRatings: ").append(toIndentedString(numberOfRatings)).append("\n");
    sb.append("    numberOfReviews: ").append(toIndentedString(numberOfReviews)).append("\n");
    sb.append("    overallRating: ").append(toIndentedString(overallRating)).append("\n");
    sb.append("    sentiments: ").append(toIndentedString(sentiments)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("hotelId");
    openapiFields.add("numberOfRatings");
    openapiFields.add("numberOfReviews");
    openapiFields.add("overallRating");
    openapiFields.add("sentiments");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("hotelId");
    openapiRequiredFields.add("numberOfRatings");
    openapiRequiredFields.add("numberOfReviews");
    openapiRequiredFields.add("overallRating");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HotelSentiment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HotelSentiment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HotelSentiment is not found in the empty JSON string", HotelSentiment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HotelSentiment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HotelSentiment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HotelSentiment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("hotelId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hotelId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hotelId").toString()));
      }
      // validate the optional field `sentiments`
      if (jsonObj.get("sentiments") != null && !jsonObj.get("sentiments").isJsonNull()) {
        HotelSentimentSentiments.validateJsonElement(jsonObj.get("sentiments"));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HotelSentiment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HotelSentiment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HotelSentiment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HotelSentiment.class));

       return (TypeAdapter<T>) new TypeAdapter<HotelSentiment>() {
           @Override
           public void write(JsonWriter out, HotelSentiment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HotelSentiment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HotelSentiment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HotelSentiment
   * @throws IOException if the JSON string is invalid with respect to HotelSentiment
   */
  public static HotelSentiment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HotelSentiment.class);
  }

  /**
   * Convert an instance of HotelSentiment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

