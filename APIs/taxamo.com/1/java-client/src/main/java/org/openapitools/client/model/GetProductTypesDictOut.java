/*
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
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
import org.openapitools.client.model.ProductTypeSchema;

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
 * GetProductTypesDictOut
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetProductTypesDictOut {
  public static final String SERIALIZED_NAME_DICTIONARY = "dictionary";
  @SerializedName(SERIALIZED_NAME_DICTIONARY)
  private List<ProductTypeSchema> dictionary = new ArrayList<>();

  public GetProductTypesDictOut() {
  }

  public GetProductTypesDictOut dictionary(List<ProductTypeSchema> dictionary) {
    this.dictionary = dictionary;
    return this;
  }

  public GetProductTypesDictOut addDictionaryItem(ProductTypeSchema dictionaryItem) {
    if (this.dictionary == null) {
      this.dictionary = new ArrayList<>();
    }
    this.dictionary.add(dictionaryItem);
    return this;
  }

  /**
   * Product type dictionary.
   * @return dictionary
   */
  @javax.annotation.Nullable
  public List<ProductTypeSchema> getDictionary() {
    return dictionary;
  }

  public void setDictionary(List<ProductTypeSchema> dictionary) {
    this.dictionary = dictionary;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetProductTypesDictOut getProductTypesDictOut = (GetProductTypesDictOut) o;
    return Objects.equals(this.dictionary, getProductTypesDictOut.dictionary);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dictionary);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetProductTypesDictOut {\n");
    sb.append("    dictionary: ").append(toIndentedString(dictionary)).append("\n");
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
    openapiFields.add("dictionary");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetProductTypesDictOut
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetProductTypesDictOut.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetProductTypesDictOut is not found in the empty JSON string", GetProductTypesDictOut.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetProductTypesDictOut.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetProductTypesDictOut` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("dictionary") != null && !jsonObj.get("dictionary").isJsonNull()) {
        JsonArray jsonArraydictionary = jsonObj.getAsJsonArray("dictionary");
        if (jsonArraydictionary != null) {
          // ensure the json data is an array
          if (!jsonObj.get("dictionary").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `dictionary` to be an array in the JSON string but got `%s`", jsonObj.get("dictionary").toString()));
          }

          // validate the optional field `dictionary` (array)
          for (int i = 0; i < jsonArraydictionary.size(); i++) {
            ProductTypeSchema.validateJsonElement(jsonArraydictionary.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetProductTypesDictOut.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetProductTypesDictOut' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetProductTypesDictOut> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetProductTypesDictOut.class));

       return (TypeAdapter<T>) new TypeAdapter<GetProductTypesDictOut>() {
           @Override
           public void write(JsonWriter out, GetProductTypesDictOut value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetProductTypesDictOut read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetProductTypesDictOut given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetProductTypesDictOut
   * @throws IOException if the JSON string is invalid with respect to GetProductTypesDictOut
   */
  public static GetProductTypesDictOut fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetProductTypesDictOut.class);
  }

  /**
   * Convert an instance of GetProductTypesDictOut to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

