/*
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
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
import org.openapitools.client.model.Answer;

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
 * Defines a search result answer.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:10:59.700770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SearchResultsAnswer extends Answer {
  public static final String SERIALIZED_NAME_TOTAL_ESTIMATED_MATCHES = "totalEstimatedMatches";
  @SerializedName(SERIALIZED_NAME_TOTAL_ESTIMATED_MATCHES)
  private Long totalEstimatedMatches;

  public SearchResultsAnswer() {
    this.type = this.getClass().getSimpleName();
  }

  public SearchResultsAnswer(
     Long totalEstimatedMatches, 
     String readLink, 
     String webSearchUrl, 
     String id
  ) {
    this();
    this.totalEstimatedMatches = totalEstimatedMatches;
    this.readLink = readLink;
    this.webSearchUrl = webSearchUrl;
    this.id = id;
  }

  /**
   * The estimated number of webpages that are relevant to the query. Use this number along with the count and offset query parameters to page the results.
   * @return totalEstimatedMatches
   */
  @javax.annotation.Nullable
  public Long getTotalEstimatedMatches() {
    return totalEstimatedMatches;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SearchResultsAnswer searchResultsAnswer = (SearchResultsAnswer) o;
    return Objects.equals(this.totalEstimatedMatches, searchResultsAnswer.totalEstimatedMatches) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(totalEstimatedMatches, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SearchResultsAnswer {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    totalEstimatedMatches: ").append(toIndentedString(totalEstimatedMatches)).append("\n");
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
    openapiFields.add("readLink");
    openapiFields.add("webSearchUrl");
    openapiFields.add("id");
    openapiFields.add("_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SearchResultsAnswer
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SearchResultsAnswer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SearchResultsAnswer is not found in the empty JSON string", SearchResultsAnswer.openapiRequiredFields.toString()));
        }
      }

      String discriminatorValue = jsonElement.getAsJsonObject().get("_type").getAsString();
      switch (discriminatorValue) {
        case "Images":
          Images.validateJsonElement(jsonElement);
          break;
        default:
          throw new IllegalArgumentException(String.format("The value of the `_type` field `%s` does not match any key defined in the discriminator's mapping.", discriminatorValue));
      }
  }


  /**
   * Create an instance of SearchResultsAnswer given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SearchResultsAnswer
   * @throws IOException if the JSON string is invalid with respect to SearchResultsAnswer
   */
  public static SearchResultsAnswer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SearchResultsAnswer.class);
  }

  /**
   * Convert an instance of SearchResultsAnswer to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

