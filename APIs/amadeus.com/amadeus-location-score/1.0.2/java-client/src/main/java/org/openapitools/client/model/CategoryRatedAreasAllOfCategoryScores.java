/*
 * Location Score
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
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
import org.openapitools.client.model.CategoryRatedAreasAllOfCategoryScoresNightLife;
import org.openapitools.client.model.CategoryRatedAreasAllOfCategoryScoresRestaurant;
import org.openapitools.client.model.CategoryRatedAreasAllOfCategoryScoresShopping;
import org.openapitools.client.model.CategoryRatedAreasAllOfCategoryScoresSight;

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
 * category scoring of the location
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:16.395202-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CategoryRatedAreasAllOfCategoryScores {
  public static final String SERIALIZED_NAME_NIGHT_LIFE = "nightLife";
  @SerializedName(SERIALIZED_NAME_NIGHT_LIFE)
  private CategoryRatedAreasAllOfCategoryScoresNightLife nightLife;

  public static final String SERIALIZED_NAME_RESTAURANT = "restaurant";
  @SerializedName(SERIALIZED_NAME_RESTAURANT)
  private CategoryRatedAreasAllOfCategoryScoresRestaurant restaurant;

  public static final String SERIALIZED_NAME_SHOPPING = "shopping";
  @SerializedName(SERIALIZED_NAME_SHOPPING)
  private CategoryRatedAreasAllOfCategoryScoresShopping shopping;

  public static final String SERIALIZED_NAME_SIGHT = "sight";
  @SerializedName(SERIALIZED_NAME_SIGHT)
  private CategoryRatedAreasAllOfCategoryScoresSight sight;

  public CategoryRatedAreasAllOfCategoryScores() {
  }

  public CategoryRatedAreasAllOfCategoryScores nightLife(CategoryRatedAreasAllOfCategoryScoresNightLife nightLife) {
    this.nightLife = nightLife;
    return this;
  }

  /**
   * Get nightLife
   * @return nightLife
   */
  @javax.annotation.Nullable
  public CategoryRatedAreasAllOfCategoryScoresNightLife getNightLife() {
    return nightLife;
  }

  public void setNightLife(CategoryRatedAreasAllOfCategoryScoresNightLife nightLife) {
    this.nightLife = nightLife;
  }


  public CategoryRatedAreasAllOfCategoryScores restaurant(CategoryRatedAreasAllOfCategoryScoresRestaurant restaurant) {
    this.restaurant = restaurant;
    return this;
  }

  /**
   * Get restaurant
   * @return restaurant
   */
  @javax.annotation.Nullable
  public CategoryRatedAreasAllOfCategoryScoresRestaurant getRestaurant() {
    return restaurant;
  }

  public void setRestaurant(CategoryRatedAreasAllOfCategoryScoresRestaurant restaurant) {
    this.restaurant = restaurant;
  }


  public CategoryRatedAreasAllOfCategoryScores shopping(CategoryRatedAreasAllOfCategoryScoresShopping shopping) {
    this.shopping = shopping;
    return this;
  }

  /**
   * Get shopping
   * @return shopping
   */
  @javax.annotation.Nullable
  public CategoryRatedAreasAllOfCategoryScoresShopping getShopping() {
    return shopping;
  }

  public void setShopping(CategoryRatedAreasAllOfCategoryScoresShopping shopping) {
    this.shopping = shopping;
  }


  public CategoryRatedAreasAllOfCategoryScores sight(CategoryRatedAreasAllOfCategoryScoresSight sight) {
    this.sight = sight;
    return this;
  }

  /**
   * Get sight
   * @return sight
   */
  @javax.annotation.Nullable
  public CategoryRatedAreasAllOfCategoryScoresSight getSight() {
    return sight;
  }

  public void setSight(CategoryRatedAreasAllOfCategoryScoresSight sight) {
    this.sight = sight;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CategoryRatedAreasAllOfCategoryScores categoryRatedAreasAllOfCategoryScores = (CategoryRatedAreasAllOfCategoryScores) o;
    return Objects.equals(this.nightLife, categoryRatedAreasAllOfCategoryScores.nightLife) &&
        Objects.equals(this.restaurant, categoryRatedAreasAllOfCategoryScores.restaurant) &&
        Objects.equals(this.shopping, categoryRatedAreasAllOfCategoryScores.shopping) &&
        Objects.equals(this.sight, categoryRatedAreasAllOfCategoryScores.sight);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nightLife, restaurant, shopping, sight);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CategoryRatedAreasAllOfCategoryScores {\n");
    sb.append("    nightLife: ").append(toIndentedString(nightLife)).append("\n");
    sb.append("    restaurant: ").append(toIndentedString(restaurant)).append("\n");
    sb.append("    shopping: ").append(toIndentedString(shopping)).append("\n");
    sb.append("    sight: ").append(toIndentedString(sight)).append("\n");
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
    openapiFields.add("nightLife");
    openapiFields.add("restaurant");
    openapiFields.add("shopping");
    openapiFields.add("sight");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CategoryRatedAreasAllOfCategoryScores
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CategoryRatedAreasAllOfCategoryScores.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CategoryRatedAreasAllOfCategoryScores is not found in the empty JSON string", CategoryRatedAreasAllOfCategoryScores.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CategoryRatedAreasAllOfCategoryScores.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CategoryRatedAreasAllOfCategoryScores` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `nightLife`
      if (jsonObj.get("nightLife") != null && !jsonObj.get("nightLife").isJsonNull()) {
        CategoryRatedAreasAllOfCategoryScoresNightLife.validateJsonElement(jsonObj.get("nightLife"));
      }
      // validate the optional field `restaurant`
      if (jsonObj.get("restaurant") != null && !jsonObj.get("restaurant").isJsonNull()) {
        CategoryRatedAreasAllOfCategoryScoresRestaurant.validateJsonElement(jsonObj.get("restaurant"));
      }
      // validate the optional field `shopping`
      if (jsonObj.get("shopping") != null && !jsonObj.get("shopping").isJsonNull()) {
        CategoryRatedAreasAllOfCategoryScoresShopping.validateJsonElement(jsonObj.get("shopping"));
      }
      // validate the optional field `sight`
      if (jsonObj.get("sight") != null && !jsonObj.get("sight").isJsonNull()) {
        CategoryRatedAreasAllOfCategoryScoresSight.validateJsonElement(jsonObj.get("sight"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CategoryRatedAreasAllOfCategoryScores.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CategoryRatedAreasAllOfCategoryScores' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CategoryRatedAreasAllOfCategoryScores> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CategoryRatedAreasAllOfCategoryScores.class));

       return (TypeAdapter<T>) new TypeAdapter<CategoryRatedAreasAllOfCategoryScores>() {
           @Override
           public void write(JsonWriter out, CategoryRatedAreasAllOfCategoryScores value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CategoryRatedAreasAllOfCategoryScores read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CategoryRatedAreasAllOfCategoryScores given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CategoryRatedAreasAllOfCategoryScores
   * @throws IOException if the JSON string is invalid with respect to CategoryRatedAreasAllOfCategoryScores
   */
  public static CategoryRatedAreasAllOfCategoryScores fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CategoryRatedAreasAllOfCategoryScores.class);
  }

  /**
   * Convert an instance of CategoryRatedAreasAllOfCategoryScores to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

