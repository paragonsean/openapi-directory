/*
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
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
import org.openapitools.client.model.CategoryResourceRelationshipsChildren;
import org.openapitools.client.model.CategoryResourceRelationshipsParent;

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
 * CategoryResourceRelationships
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:05.017128-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CategoryResourceRelationships {
  public static final String SERIALIZED_NAME_CHILDREN = "children";
  @SerializedName(SERIALIZED_NAME_CHILDREN)
  private CategoryResourceRelationshipsChildren children;

  public static final String SERIALIZED_NAME_PARENT = "parent";
  @SerializedName(SERIALIZED_NAME_PARENT)
  private CategoryResourceRelationshipsParent parent;

  public CategoryResourceRelationships() {
  }

  public CategoryResourceRelationships children(CategoryResourceRelationshipsChildren children) {
    this.children = children;
    return this;
  }

  /**
   * Get children
   * @return children
   */
  @javax.annotation.Nonnull
  public CategoryResourceRelationshipsChildren getChildren() {
    return children;
  }

  public void setChildren(CategoryResourceRelationshipsChildren children) {
    this.children = children;
  }


  public CategoryResourceRelationships parent(CategoryResourceRelationshipsParent parent) {
    this.parent = parent;
    return this;
  }

  /**
   * Get parent
   * @return parent
   */
  @javax.annotation.Nonnull
  public CategoryResourceRelationshipsParent getParent() {
    return parent;
  }

  public void setParent(CategoryResourceRelationshipsParent parent) {
    this.parent = parent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CategoryResourceRelationships categoryResourceRelationships = (CategoryResourceRelationships) o;
    return Objects.equals(this.children, categoryResourceRelationships.children) &&
        Objects.equals(this.parent, categoryResourceRelationships.parent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(children, parent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CategoryResourceRelationships {\n");
    sb.append("    children: ").append(toIndentedString(children)).append("\n");
    sb.append("    parent: ").append(toIndentedString(parent)).append("\n");
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
    openapiFields.add("children");
    openapiFields.add("parent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("children");
    openapiRequiredFields.add("parent");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CategoryResourceRelationships
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CategoryResourceRelationships.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CategoryResourceRelationships is not found in the empty JSON string", CategoryResourceRelationships.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CategoryResourceRelationships.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CategoryResourceRelationships` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CategoryResourceRelationships.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `children`
      CategoryResourceRelationshipsChildren.validateJsonElement(jsonObj.get("children"));
      // validate the required field `parent`
      CategoryResourceRelationshipsParent.validateJsonElement(jsonObj.get("parent"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CategoryResourceRelationships.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CategoryResourceRelationships' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CategoryResourceRelationships> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CategoryResourceRelationships.class));

       return (TypeAdapter<T>) new TypeAdapter<CategoryResourceRelationships>() {
           @Override
           public void write(JsonWriter out, CategoryResourceRelationships value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CategoryResourceRelationships read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CategoryResourceRelationships given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CategoryResourceRelationships
   * @throws IOException if the JSON string is invalid with respect to CategoryResourceRelationships
   */
  public static CategoryResourceRelationships fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CategoryResourceRelationships.class);
  }

  /**
   * Convert an instance of CategoryResourceRelationships to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

