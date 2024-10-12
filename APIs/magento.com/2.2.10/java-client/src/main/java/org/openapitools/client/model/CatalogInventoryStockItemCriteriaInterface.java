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
import org.openapitools.client.model.FrameworkCriteriaInterface;

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
 * Interface StockItemCriteriaInterface
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CatalogInventoryStockItemCriteriaInterface {
  public static final String SERIALIZED_NAME_CRITERIA_LIST = "criteria_list";
  @SerializedName(SERIALIZED_NAME_CRITERIA_LIST)
  private List<FrameworkCriteriaInterface> criteriaList = new ArrayList<>();

  public static final String SERIALIZED_NAME_FILTERS = "filters";
  @SerializedName(SERIALIZED_NAME_FILTERS)
  private List<String> filters = new ArrayList<>();

  public static final String SERIALIZED_NAME_LIMIT = "limit";
  @SerializedName(SERIALIZED_NAME_LIMIT)
  private List<String> limit = new ArrayList<>();

  public static final String SERIALIZED_NAME_MAPPER_INTERFACE_NAME = "mapper_interface_name";
  @SerializedName(SERIALIZED_NAME_MAPPER_INTERFACE_NAME)
  private String mapperInterfaceName;

  public static final String SERIALIZED_NAME_ORDERS = "orders";
  @SerializedName(SERIALIZED_NAME_ORDERS)
  private List<String> orders = new ArrayList<>();

  public CatalogInventoryStockItemCriteriaInterface() {
  }

  public CatalogInventoryStockItemCriteriaInterface criteriaList(List<FrameworkCriteriaInterface> criteriaList) {
    this.criteriaList = criteriaList;
    return this;
  }

  public CatalogInventoryStockItemCriteriaInterface addCriteriaListItem(FrameworkCriteriaInterface criteriaListItem) {
    if (this.criteriaList == null) {
      this.criteriaList = new ArrayList<>();
    }
    this.criteriaList.add(criteriaListItem);
    return this;
  }

  /**
   * Criteria objects added to current Composite Criteria
   * @return criteriaList
   */
  @javax.annotation.Nonnull
  public List<FrameworkCriteriaInterface> getCriteriaList() {
    return criteriaList;
  }

  public void setCriteriaList(List<FrameworkCriteriaInterface> criteriaList) {
    this.criteriaList = criteriaList;
  }


  public CatalogInventoryStockItemCriteriaInterface filters(List<String> filters) {
    this.filters = filters;
    return this;
  }

  public CatalogInventoryStockItemCriteriaInterface addFiltersItem(String filtersItem) {
    if (this.filters == null) {
      this.filters = new ArrayList<>();
    }
    this.filters.add(filtersItem);
    return this;
  }

  /**
   * List of filters
   * @return filters
   */
  @javax.annotation.Nonnull
  public List<String> getFilters() {
    return filters;
  }

  public void setFilters(List<String> filters) {
    this.filters = filters;
  }


  public CatalogInventoryStockItemCriteriaInterface limit(List<String> limit) {
    this.limit = limit;
    return this;
  }

  public CatalogInventoryStockItemCriteriaInterface addLimitItem(String limitItem) {
    if (this.limit == null) {
      this.limit = new ArrayList<>();
    }
    this.limit.add(limitItem);
    return this;
  }

  /**
   * Limit
   * @return limit
   */
  @javax.annotation.Nonnull
  public List<String> getLimit() {
    return limit;
  }

  public void setLimit(List<String> limit) {
    this.limit = limit;
  }


  public CatalogInventoryStockItemCriteriaInterface mapperInterfaceName(String mapperInterfaceName) {
    this.mapperInterfaceName = mapperInterfaceName;
    return this;
  }

  /**
   * Associated Mapper Interface name
   * @return mapperInterfaceName
   */
  @javax.annotation.Nonnull
  public String getMapperInterfaceName() {
    return mapperInterfaceName;
  }

  public void setMapperInterfaceName(String mapperInterfaceName) {
    this.mapperInterfaceName = mapperInterfaceName;
  }


  public CatalogInventoryStockItemCriteriaInterface orders(List<String> orders) {
    this.orders = orders;
    return this;
  }

  public CatalogInventoryStockItemCriteriaInterface addOrdersItem(String ordersItem) {
    if (this.orders == null) {
      this.orders = new ArrayList<>();
    }
    this.orders.add(ordersItem);
    return this;
  }

  /**
   * Ordering criteria
   * @return orders
   */
  @javax.annotation.Nonnull
  public List<String> getOrders() {
    return orders;
  }

  public void setOrders(List<String> orders) {
    this.orders = orders;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CatalogInventoryStockItemCriteriaInterface catalogInventoryStockItemCriteriaInterface = (CatalogInventoryStockItemCriteriaInterface) o;
    return Objects.equals(this.criteriaList, catalogInventoryStockItemCriteriaInterface.criteriaList) &&
        Objects.equals(this.filters, catalogInventoryStockItemCriteriaInterface.filters) &&
        Objects.equals(this.limit, catalogInventoryStockItemCriteriaInterface.limit) &&
        Objects.equals(this.mapperInterfaceName, catalogInventoryStockItemCriteriaInterface.mapperInterfaceName) &&
        Objects.equals(this.orders, catalogInventoryStockItemCriteriaInterface.orders);
  }

  @Override
  public int hashCode() {
    return Objects.hash(criteriaList, filters, limit, mapperInterfaceName, orders);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CatalogInventoryStockItemCriteriaInterface {\n");
    sb.append("    criteriaList: ").append(toIndentedString(criteriaList)).append("\n");
    sb.append("    filters: ").append(toIndentedString(filters)).append("\n");
    sb.append("    limit: ").append(toIndentedString(limit)).append("\n");
    sb.append("    mapperInterfaceName: ").append(toIndentedString(mapperInterfaceName)).append("\n");
    sb.append("    orders: ").append(toIndentedString(orders)).append("\n");
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
    openapiFields.add("criteria_list");
    openapiFields.add("filters");
    openapiFields.add("limit");
    openapiFields.add("mapper_interface_name");
    openapiFields.add("orders");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("criteria_list");
    openapiRequiredFields.add("filters");
    openapiRequiredFields.add("limit");
    openapiRequiredFields.add("mapper_interface_name");
    openapiRequiredFields.add("orders");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CatalogInventoryStockItemCriteriaInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CatalogInventoryStockItemCriteriaInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CatalogInventoryStockItemCriteriaInterface is not found in the empty JSON string", CatalogInventoryStockItemCriteriaInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CatalogInventoryStockItemCriteriaInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CatalogInventoryStockItemCriteriaInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CatalogInventoryStockItemCriteriaInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("criteria_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `criteria_list` to be an array in the JSON string but got `%s`", jsonObj.get("criteria_list").toString()));
      }

      JsonArray jsonArraycriteriaList = jsonObj.getAsJsonArray("criteria_list");
      // validate the required field `criteria_list` (array)
      for (int i = 0; i < jsonArraycriteriaList.size(); i++) {
        FrameworkCriteriaInterface.validateJsonElement(jsonArraycriteriaList.get(i));
      };
      // ensure the required json array is present
      if (jsonObj.get("filters") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("filters").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `filters` to be an array in the JSON string but got `%s`", jsonObj.get("filters").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("limit") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("limit").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `limit` to be an array in the JSON string but got `%s`", jsonObj.get("limit").toString()));
      }
      if (!jsonObj.get("mapper_interface_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mapper_interface_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mapper_interface_name").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("orders") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("orders").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `orders` to be an array in the JSON string but got `%s`", jsonObj.get("orders").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CatalogInventoryStockItemCriteriaInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CatalogInventoryStockItemCriteriaInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CatalogInventoryStockItemCriteriaInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CatalogInventoryStockItemCriteriaInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<CatalogInventoryStockItemCriteriaInterface>() {
           @Override
           public void write(JsonWriter out, CatalogInventoryStockItemCriteriaInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CatalogInventoryStockItemCriteriaInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CatalogInventoryStockItemCriteriaInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CatalogInventoryStockItemCriteriaInterface
   * @throws IOException if the JSON string is invalid with respect to CatalogInventoryStockItemCriteriaInterface
   */
  public static CatalogInventoryStockItemCriteriaInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CatalogInventoryStockItemCriteriaInterface.class);
  }

  /**
   * Convert an instance of CatalogInventoryStockItemCriteriaInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

