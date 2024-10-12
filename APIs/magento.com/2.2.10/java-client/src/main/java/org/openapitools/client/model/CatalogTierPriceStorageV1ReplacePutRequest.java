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
import org.openapitools.client.model.CatalogDataTierPriceInterface;

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
 * CatalogTierPriceStorageV1ReplacePutRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CatalogTierPriceStorageV1ReplacePutRequest {
  public static final String SERIALIZED_NAME_PRICES = "prices";
  @SerializedName(SERIALIZED_NAME_PRICES)
  private List<CatalogDataTierPriceInterface> prices = new ArrayList<>();

  public CatalogTierPriceStorageV1ReplacePutRequest() {
  }

  public CatalogTierPriceStorageV1ReplacePutRequest prices(List<CatalogDataTierPriceInterface> prices) {
    this.prices = prices;
    return this;
  }

  public CatalogTierPriceStorageV1ReplacePutRequest addPricesItem(CatalogDataTierPriceInterface pricesItem) {
    if (this.prices == null) {
      this.prices = new ArrayList<>();
    }
    this.prices.add(pricesItem);
    return this;
  }

  /**
   * Get prices
   * @return prices
   */
  @javax.annotation.Nonnull
  public List<CatalogDataTierPriceInterface> getPrices() {
    return prices;
  }

  public void setPrices(List<CatalogDataTierPriceInterface> prices) {
    this.prices = prices;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CatalogTierPriceStorageV1ReplacePutRequest catalogTierPriceStorageV1ReplacePutRequest = (CatalogTierPriceStorageV1ReplacePutRequest) o;
    return Objects.equals(this.prices, catalogTierPriceStorageV1ReplacePutRequest.prices);
  }

  @Override
  public int hashCode() {
    return Objects.hash(prices);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CatalogTierPriceStorageV1ReplacePutRequest {\n");
    sb.append("    prices: ").append(toIndentedString(prices)).append("\n");
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
    openapiFields.add("prices");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("prices");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CatalogTierPriceStorageV1ReplacePutRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CatalogTierPriceStorageV1ReplacePutRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CatalogTierPriceStorageV1ReplacePutRequest is not found in the empty JSON string", CatalogTierPriceStorageV1ReplacePutRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CatalogTierPriceStorageV1ReplacePutRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CatalogTierPriceStorageV1ReplacePutRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CatalogTierPriceStorageV1ReplacePutRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("prices").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `prices` to be an array in the JSON string but got `%s`", jsonObj.get("prices").toString()));
      }

      JsonArray jsonArrayprices = jsonObj.getAsJsonArray("prices");
      // validate the required field `prices` (array)
      for (int i = 0; i < jsonArrayprices.size(); i++) {
        CatalogDataTierPriceInterface.validateJsonElement(jsonArrayprices.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CatalogTierPriceStorageV1ReplacePutRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CatalogTierPriceStorageV1ReplacePutRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CatalogTierPriceStorageV1ReplacePutRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CatalogTierPriceStorageV1ReplacePutRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CatalogTierPriceStorageV1ReplacePutRequest>() {
           @Override
           public void write(JsonWriter out, CatalogTierPriceStorageV1ReplacePutRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CatalogTierPriceStorageV1ReplacePutRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CatalogTierPriceStorageV1ReplacePutRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CatalogTierPriceStorageV1ReplacePutRequest
   * @throws IOException if the JSON string is invalid with respect to CatalogTierPriceStorageV1ReplacePutRequest
   */
  public static CatalogTierPriceStorageV1ReplacePutRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CatalogTierPriceStorageV1ReplacePutRequest.class);
  }

  /**
   * Convert an instance of CatalogTierPriceStorageV1ReplacePutRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

