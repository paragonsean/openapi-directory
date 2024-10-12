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
 * sight category
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:16.395202-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CategoryRatedAreasAllOfCategoryScoresSight {
  public static final String SERIALIZED_NAME_BEACH_AND_PARK = "beachAndPark";
  @SerializedName(SERIALIZED_NAME_BEACH_AND_PARK)
  private Integer beachAndPark;

  public static final String SERIALIZED_NAME_HISTORICAL = "historical";
  @SerializedName(SERIALIZED_NAME_HISTORICAL)
  private Integer historical;

  public static final String SERIALIZED_NAME_OVERALL = "overall";
  @SerializedName(SERIALIZED_NAME_OVERALL)
  private Integer overall;

  public CategoryRatedAreasAllOfCategoryScoresSight() {
  }

  public CategoryRatedAreasAllOfCategoryScoresSight beachAndPark(Integer beachAndPark) {
    this.beachAndPark = beachAndPark;
    return this;
  }

  /**
   * score of outdoor activity possibility from 0 (no outdoor spaces) to 100 (many parks or beaches to enjoy)
   * @return beachAndPark
   */
  @javax.annotation.Nullable
  public Integer getBeachAndPark() {
    return beachAndPark;
  }

  public void setBeachAndPark(Integer beachAndPark) {
    this.beachAndPark = beachAndPark;
  }


  public CategoryRatedAreasAllOfCategoryScoresSight historical(Integer historical) {
    this.historical = historical;
    return this;
  }

  /**
   * score of historical discovery possibility from 0 (no historical site) to 100 (many historical site to enjoy)
   * @return historical
   */
  @javax.annotation.Nullable
  public Integer getHistorical() {
    return historical;
  }

  public void setHistorical(Integer historical) {
    this.historical = historical;
  }


  public CategoryRatedAreasAllOfCategoryScoresSight overall(Integer overall) {
    this.overall = overall;
    return this;
  }

  /**
   * score of sight seeing possibility from 0 (nothing to see) to 100 (many sceneries to enjoy)
   * @return overall
   */
  @javax.annotation.Nullable
  public Integer getOverall() {
    return overall;
  }

  public void setOverall(Integer overall) {
    this.overall = overall;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CategoryRatedAreasAllOfCategoryScoresSight categoryRatedAreasAllOfCategoryScoresSight = (CategoryRatedAreasAllOfCategoryScoresSight) o;
    return Objects.equals(this.beachAndPark, categoryRatedAreasAllOfCategoryScoresSight.beachAndPark) &&
        Objects.equals(this.historical, categoryRatedAreasAllOfCategoryScoresSight.historical) &&
        Objects.equals(this.overall, categoryRatedAreasAllOfCategoryScoresSight.overall);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beachAndPark, historical, overall);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CategoryRatedAreasAllOfCategoryScoresSight {\n");
    sb.append("    beachAndPark: ").append(toIndentedString(beachAndPark)).append("\n");
    sb.append("    historical: ").append(toIndentedString(historical)).append("\n");
    sb.append("    overall: ").append(toIndentedString(overall)).append("\n");
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
    openapiFields.add("beachAndPark");
    openapiFields.add("historical");
    openapiFields.add("overall");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CategoryRatedAreasAllOfCategoryScoresSight
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CategoryRatedAreasAllOfCategoryScoresSight.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CategoryRatedAreasAllOfCategoryScoresSight is not found in the empty JSON string", CategoryRatedAreasAllOfCategoryScoresSight.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CategoryRatedAreasAllOfCategoryScoresSight.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CategoryRatedAreasAllOfCategoryScoresSight` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CategoryRatedAreasAllOfCategoryScoresSight.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CategoryRatedAreasAllOfCategoryScoresSight' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CategoryRatedAreasAllOfCategoryScoresSight> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CategoryRatedAreasAllOfCategoryScoresSight.class));

       return (TypeAdapter<T>) new TypeAdapter<CategoryRatedAreasAllOfCategoryScoresSight>() {
           @Override
           public void write(JsonWriter out, CategoryRatedAreasAllOfCategoryScoresSight value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CategoryRatedAreasAllOfCategoryScoresSight read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CategoryRatedAreasAllOfCategoryScoresSight given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CategoryRatedAreasAllOfCategoryScoresSight
   * @throws IOException if the JSON string is invalid with respect to CategoryRatedAreasAllOfCategoryScoresSight
   */
  public static CategoryRatedAreasAllOfCategoryScoresSight fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CategoryRatedAreasAllOfCategoryScoresSight.class);
  }

  /**
   * Convert an instance of CategoryRatedAreasAllOfCategoryScoresSight to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

