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
import org.openapitools.client.model.CatalogDataCategoryInterface;

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
 * SharedCatalogCategoryManagementV1AssignCategoriesPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SharedCatalogCategoryManagementV1AssignCategoriesPostRequest {
  public static final String SERIALIZED_NAME_CATEGORIES = "categories";
  @SerializedName(SERIALIZED_NAME_CATEGORIES)
  private List<CatalogDataCategoryInterface> categories = new ArrayList<>();

  public SharedCatalogCategoryManagementV1AssignCategoriesPostRequest() {
  }

  public SharedCatalogCategoryManagementV1AssignCategoriesPostRequest categories(List<CatalogDataCategoryInterface> categories) {
    this.categories = categories;
    return this;
  }

  public SharedCatalogCategoryManagementV1AssignCategoriesPostRequest addCategoriesItem(CatalogDataCategoryInterface categoriesItem) {
    if (this.categories == null) {
      this.categories = new ArrayList<>();
    }
    this.categories.add(categoriesItem);
    return this;
  }

  /**
   * Get categories
   * @return categories
   */
  @javax.annotation.Nonnull
  public List<CatalogDataCategoryInterface> getCategories() {
    return categories;
  }

  public void setCategories(List<CatalogDataCategoryInterface> categories) {
    this.categories = categories;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SharedCatalogCategoryManagementV1AssignCategoriesPostRequest sharedCatalogCategoryManagementV1AssignCategoriesPostRequest = (SharedCatalogCategoryManagementV1AssignCategoriesPostRequest) o;
    return Objects.equals(this.categories, sharedCatalogCategoryManagementV1AssignCategoriesPostRequest.categories);
  }

  @Override
  public int hashCode() {
    return Objects.hash(categories);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SharedCatalogCategoryManagementV1AssignCategoriesPostRequest {\n");
    sb.append("    categories: ").append(toIndentedString(categories)).append("\n");
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
    openapiFields.add("categories");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("categories");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SharedCatalogCategoryManagementV1AssignCategoriesPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SharedCatalogCategoryManagementV1AssignCategoriesPostRequest is not found in the empty JSON string", SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SharedCatalogCategoryManagementV1AssignCategoriesPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("categories").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `categories` to be an array in the JSON string but got `%s`", jsonObj.get("categories").toString()));
      }

      JsonArray jsonArraycategories = jsonObj.getAsJsonArray("categories");
      // validate the required field `categories` (array)
      for (int i = 0; i < jsonArraycategories.size(); i++) {
        CatalogDataCategoryInterface.validateJsonElement(jsonArraycategories.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SharedCatalogCategoryManagementV1AssignCategoriesPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SharedCatalogCategoryManagementV1AssignCategoriesPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<SharedCatalogCategoryManagementV1AssignCategoriesPostRequest>() {
           @Override
           public void write(JsonWriter out, SharedCatalogCategoryManagementV1AssignCategoriesPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SharedCatalogCategoryManagementV1AssignCategoriesPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SharedCatalogCategoryManagementV1AssignCategoriesPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SharedCatalogCategoryManagementV1AssignCategoriesPostRequest
   * @throws IOException if the JSON string is invalid with respect to SharedCatalogCategoryManagementV1AssignCategoriesPostRequest
   */
  public static SharedCatalogCategoryManagementV1AssignCategoriesPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.class);
  }

  /**
   * Convert an instance of SharedCatalogCategoryManagementV1AssignCategoriesPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

