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
import org.openapitools.client.model.FrameworkSearchFilterGroup;
import org.openapitools.client.model.FrameworkSortOrder;

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
 * Search criteria interface.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FrameworkSearchCriteriaInterface {
  public static final String SERIALIZED_NAME_CURRENT_PAGE = "current_page";
  @SerializedName(SERIALIZED_NAME_CURRENT_PAGE)
  private Integer currentPage;

  public static final String SERIALIZED_NAME_FILTER_GROUPS = "filter_groups";
  @SerializedName(SERIALIZED_NAME_FILTER_GROUPS)
  private List<FrameworkSearchFilterGroup> filterGroups = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAGE_SIZE = "page_size";
  @SerializedName(SERIALIZED_NAME_PAGE_SIZE)
  private Integer pageSize;

  public static final String SERIALIZED_NAME_SORT_ORDERS = "sort_orders";
  @SerializedName(SERIALIZED_NAME_SORT_ORDERS)
  private List<FrameworkSortOrder> sortOrders = new ArrayList<>();

  public FrameworkSearchCriteriaInterface() {
  }

  public FrameworkSearchCriteriaInterface currentPage(Integer currentPage) {
    this.currentPage = currentPage;
    return this;
  }

  /**
   * Current page.
   * @return currentPage
   */
  @javax.annotation.Nullable
  public Integer getCurrentPage() {
    return currentPage;
  }

  public void setCurrentPage(Integer currentPage) {
    this.currentPage = currentPage;
  }


  public FrameworkSearchCriteriaInterface filterGroups(List<FrameworkSearchFilterGroup> filterGroups) {
    this.filterGroups = filterGroups;
    return this;
  }

  public FrameworkSearchCriteriaInterface addFilterGroupsItem(FrameworkSearchFilterGroup filterGroupsItem) {
    if (this.filterGroups == null) {
      this.filterGroups = new ArrayList<>();
    }
    this.filterGroups.add(filterGroupsItem);
    return this;
  }

  /**
   * A list of filter groups.
   * @return filterGroups
   */
  @javax.annotation.Nonnull
  public List<FrameworkSearchFilterGroup> getFilterGroups() {
    return filterGroups;
  }

  public void setFilterGroups(List<FrameworkSearchFilterGroup> filterGroups) {
    this.filterGroups = filterGroups;
  }


  public FrameworkSearchCriteriaInterface pageSize(Integer pageSize) {
    this.pageSize = pageSize;
    return this;
  }

  /**
   * Page size.
   * @return pageSize
   */
  @javax.annotation.Nullable
  public Integer getPageSize() {
    return pageSize;
  }

  public void setPageSize(Integer pageSize) {
    this.pageSize = pageSize;
  }


  public FrameworkSearchCriteriaInterface sortOrders(List<FrameworkSortOrder> sortOrders) {
    this.sortOrders = sortOrders;
    return this;
  }

  public FrameworkSearchCriteriaInterface addSortOrdersItem(FrameworkSortOrder sortOrdersItem) {
    if (this.sortOrders == null) {
      this.sortOrders = new ArrayList<>();
    }
    this.sortOrders.add(sortOrdersItem);
    return this;
  }

  /**
   * Sort order.
   * @return sortOrders
   */
  @javax.annotation.Nullable
  public List<FrameworkSortOrder> getSortOrders() {
    return sortOrders;
  }

  public void setSortOrders(List<FrameworkSortOrder> sortOrders) {
    this.sortOrders = sortOrders;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FrameworkSearchCriteriaInterface frameworkSearchCriteriaInterface = (FrameworkSearchCriteriaInterface) o;
    return Objects.equals(this.currentPage, frameworkSearchCriteriaInterface.currentPage) &&
        Objects.equals(this.filterGroups, frameworkSearchCriteriaInterface.filterGroups) &&
        Objects.equals(this.pageSize, frameworkSearchCriteriaInterface.pageSize) &&
        Objects.equals(this.sortOrders, frameworkSearchCriteriaInterface.sortOrders);
  }

  @Override
  public int hashCode() {
    return Objects.hash(currentPage, filterGroups, pageSize, sortOrders);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FrameworkSearchCriteriaInterface {\n");
    sb.append("    currentPage: ").append(toIndentedString(currentPage)).append("\n");
    sb.append("    filterGroups: ").append(toIndentedString(filterGroups)).append("\n");
    sb.append("    pageSize: ").append(toIndentedString(pageSize)).append("\n");
    sb.append("    sortOrders: ").append(toIndentedString(sortOrders)).append("\n");
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
    openapiFields.add("current_page");
    openapiFields.add("filter_groups");
    openapiFields.add("page_size");
    openapiFields.add("sort_orders");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("filter_groups");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FrameworkSearchCriteriaInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FrameworkSearchCriteriaInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FrameworkSearchCriteriaInterface is not found in the empty JSON string", FrameworkSearchCriteriaInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FrameworkSearchCriteriaInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FrameworkSearchCriteriaInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FrameworkSearchCriteriaInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("filter_groups").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `filter_groups` to be an array in the JSON string but got `%s`", jsonObj.get("filter_groups").toString()));
      }

      JsonArray jsonArrayfilterGroups = jsonObj.getAsJsonArray("filter_groups");
      // validate the required field `filter_groups` (array)
      for (int i = 0; i < jsonArrayfilterGroups.size(); i++) {
        FrameworkSearchFilterGroup.validateJsonElement(jsonArrayfilterGroups.get(i));
      };
      if (jsonObj.get("sort_orders") != null && !jsonObj.get("sort_orders").isJsonNull()) {
        JsonArray jsonArraysortOrders = jsonObj.getAsJsonArray("sort_orders");
        if (jsonArraysortOrders != null) {
          // ensure the json data is an array
          if (!jsonObj.get("sort_orders").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `sort_orders` to be an array in the JSON string but got `%s`", jsonObj.get("sort_orders").toString()));
          }

          // validate the optional field `sort_orders` (array)
          for (int i = 0; i < jsonArraysortOrders.size(); i++) {
            FrameworkSortOrder.validateJsonElement(jsonArraysortOrders.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FrameworkSearchCriteriaInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FrameworkSearchCriteriaInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FrameworkSearchCriteriaInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FrameworkSearchCriteriaInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<FrameworkSearchCriteriaInterface>() {
           @Override
           public void write(JsonWriter out, FrameworkSearchCriteriaInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FrameworkSearchCriteriaInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FrameworkSearchCriteriaInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FrameworkSearchCriteriaInterface
   * @throws IOException if the JSON string is invalid with respect to FrameworkSearchCriteriaInterface
   */
  public static FrameworkSearchCriteriaInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FrameworkSearchCriteriaInterface.class);
  }

  /**
   * Convert an instance of FrameworkSearchCriteriaInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

