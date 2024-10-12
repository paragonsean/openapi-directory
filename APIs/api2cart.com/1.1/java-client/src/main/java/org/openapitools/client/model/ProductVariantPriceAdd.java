/*
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
import org.openapitools.client.model.ProductAddGroupPricesInner;

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
 * ProductVariantPriceAdd
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProductVariantPriceAdd {
  public static final String SERIALIZED_NAME_GROUP_PRICES = "group_prices";
  @SerializedName(SERIALIZED_NAME_GROUP_PRICES)
  private List<ProductAddGroupPricesInner> groupPrices = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "product_id";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private String productId;

  public ProductVariantPriceAdd() {
  }

  public ProductVariantPriceAdd groupPrices(List<ProductAddGroupPricesInner> groupPrices) {
    this.groupPrices = groupPrices;
    return this;
  }

  public ProductVariantPriceAdd addGroupPricesItem(ProductAddGroupPricesInner groupPricesItem) {
    if (this.groupPrices == null) {
      this.groupPrices = new ArrayList<>();
    }
    this.groupPrices.add(groupPricesItem);
    return this;
  }

  /**
   * Defines variants&#39;s group prices
   * @return groupPrices
   */
  @javax.annotation.Nonnull
  public List<ProductAddGroupPricesInner> getGroupPrices() {
    return groupPrices;
  }

  public void setGroupPrices(List<ProductAddGroupPricesInner> groupPrices) {
    this.groupPrices = groupPrices;
  }


  public ProductVariantPriceAdd id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Defines the variant to which the price has to be added
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public ProductVariantPriceAdd productId(String productId) {
    this.productId = productId;
    return this;
  }

  /**
   * Product id
   * @return productId
   */
  @javax.annotation.Nullable
  public String getProductId() {
    return productId;
  }

  public void setProductId(String productId) {
    this.productId = productId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProductVariantPriceAdd productVariantPriceAdd = (ProductVariantPriceAdd) o;
    return Objects.equals(this.groupPrices, productVariantPriceAdd.groupPrices) &&
        Objects.equals(this.id, productVariantPriceAdd.id) &&
        Objects.equals(this.productId, productVariantPriceAdd.productId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(groupPrices, id, productId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProductVariantPriceAdd {\n");
    sb.append("    groupPrices: ").append(toIndentedString(groupPrices)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
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
    openapiFields.add("group_prices");
    openapiFields.add("id");
    openapiFields.add("product_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("group_prices");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProductVariantPriceAdd
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProductVariantPriceAdd.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProductVariantPriceAdd is not found in the empty JSON string", ProductVariantPriceAdd.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProductVariantPriceAdd.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProductVariantPriceAdd` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProductVariantPriceAdd.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("group_prices").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `group_prices` to be an array in the JSON string but got `%s`", jsonObj.get("group_prices").toString()));
      }

      JsonArray jsonArraygroupPrices = jsonObj.getAsJsonArray("group_prices");
      // validate the required field `group_prices` (array)
      for (int i = 0; i < jsonArraygroupPrices.size(); i++) {
        ProductAddGroupPricesInner.validateJsonElement(jsonArraygroupPrices.get(i));
      };
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("product_id") != null && !jsonObj.get("product_id").isJsonNull()) && !jsonObj.get("product_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `product_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("product_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProductVariantPriceAdd.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProductVariantPriceAdd' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProductVariantPriceAdd> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProductVariantPriceAdd.class));

       return (TypeAdapter<T>) new TypeAdapter<ProductVariantPriceAdd>() {
           @Override
           public void write(JsonWriter out, ProductVariantPriceAdd value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProductVariantPriceAdd read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProductVariantPriceAdd given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProductVariantPriceAdd
   * @throws IOException if the JSON string is invalid with respect to ProductVariantPriceAdd
   */
  public static ProductVariantPriceAdd fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProductVariantPriceAdd.class);
  }

  /**
   * Convert an instance of ProductVariantPriceAdd to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

