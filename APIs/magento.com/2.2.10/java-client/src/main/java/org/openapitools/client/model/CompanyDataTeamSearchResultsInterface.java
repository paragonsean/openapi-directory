/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
import org.openapitools.client.model.CompanyDataTeamInterface;
import org.openapitools.client.model.FrameworkSearchCriteriaInterface;

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
 * Interface for company team search results
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompanyDataTeamSearchResultsInterface {
  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<CompanyDataTeamInterface> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_SEARCH_CRITERIA = "search_criteria";
  @SerializedName(SERIALIZED_NAME_SEARCH_CRITERIA)
  private FrameworkSearchCriteriaInterface searchCriteria;

  public static final String SERIALIZED_NAME_TOTAL_COUNT = "total_count";
  @SerializedName(SERIALIZED_NAME_TOTAL_COUNT)
  private Integer totalCount;

  public CompanyDataTeamSearchResultsInterface() {
  }

  public CompanyDataTeamSearchResultsInterface items(List<CompanyDataTeamInterface> items) {
    this.items = items;
    return this;
  }

  public CompanyDataTeamSearchResultsInterface addItemsItem(CompanyDataTeamInterface itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Teams list
   * @return items
   */
  @javax.annotation.Nonnull
  public List<CompanyDataTeamInterface> getItems() {
    return items;
  }

  public void setItems(List<CompanyDataTeamInterface> items) {
    this.items = items;
  }


  public CompanyDataTeamSearchResultsInterface searchCriteria(FrameworkSearchCriteriaInterface searchCriteria) {
    this.searchCriteria = searchCriteria;
    return this;
  }

  /**
   * Get searchCriteria
   * @return searchCriteria
   */
  @javax.annotation.Nonnull
  public FrameworkSearchCriteriaInterface getSearchCriteria() {
    return searchCriteria;
  }

  public void setSearchCriteria(FrameworkSearchCriteriaInterface searchCriteria) {
    this.searchCriteria = searchCriteria;
  }


  public CompanyDataTeamSearchResultsInterface totalCount(Integer totalCount) {
    this.totalCount = totalCount;
    return this;
  }

  /**
   * Total count.
   * @return totalCount
   */
  @javax.annotation.Nonnull
  public Integer getTotalCount() {
    return totalCount;
  }

  public void setTotalCount(Integer totalCount) {
    this.totalCount = totalCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompanyDataTeamSearchResultsInterface companyDataTeamSearchResultsInterface = (CompanyDataTeamSearchResultsInterface) o;
    return Objects.equals(this.items, companyDataTeamSearchResultsInterface.items) &&
        Objects.equals(this.searchCriteria, companyDataTeamSearchResultsInterface.searchCriteria) &&
        Objects.equals(this.totalCount, companyDataTeamSearchResultsInterface.totalCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(items, searchCriteria, totalCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompanyDataTeamSearchResultsInterface {\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    searchCriteria: ").append(toIndentedString(searchCriteria)).append("\n");
    sb.append("    totalCount: ").append(toIndentedString(totalCount)).append("\n");
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
    openapiFields.add("items");
    openapiFields.add("search_criteria");
    openapiFields.add("total_count");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("items");
    openapiRequiredFields.add("search_criteria");
    openapiRequiredFields.add("total_count");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompanyDataTeamSearchResultsInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompanyDataTeamSearchResultsInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompanyDataTeamSearchResultsInterface is not found in the empty JSON string", CompanyDataTeamSearchResultsInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompanyDataTeamSearchResultsInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompanyDataTeamSearchResultsInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CompanyDataTeamSearchResultsInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("items").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
      }

      JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
      // validate the required field `items` (array)
      for (int i = 0; i < jsonArrayitems.size(); i++) {
        CompanyDataTeamInterface.validateJsonElement(jsonArrayitems.get(i));
      };
      // validate the required field `search_criteria`
      FrameworkSearchCriteriaInterface.validateJsonElement(jsonObj.get("search_criteria"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompanyDataTeamSearchResultsInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompanyDataTeamSearchResultsInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompanyDataTeamSearchResultsInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompanyDataTeamSearchResultsInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<CompanyDataTeamSearchResultsInterface>() {
           @Override
           public void write(JsonWriter out, CompanyDataTeamSearchResultsInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompanyDataTeamSearchResultsInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompanyDataTeamSearchResultsInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompanyDataTeamSearchResultsInterface
   * @throws IOException if the JSON string is invalid with respect to CompanyDataTeamSearchResultsInterface
   */
  public static CompanyDataTeamSearchResultsInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompanyDataTeamSearchResultsInterface.class);
  }

  /**
   * Convert an instance of CompanyDataTeamSearchResultsInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

