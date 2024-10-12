/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
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
import java.util.UUID;
import org.openapitools.client.model.BoundingBox;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * Prediction result.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:14.859299-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Prediction {
  public static final String SERIALIZED_NAME_BOUNDING_BOX = "boundingBox";
  @SerializedName(SERIALIZED_NAME_BOUNDING_BOX)
  private BoundingBox boundingBox;

  public static final String SERIALIZED_NAME_PROBABILITY = "probability";
  @SerializedName(SERIALIZED_NAME_PROBABILITY)
  private Float probability;

  public static final String SERIALIZED_NAME_TAG_ID = "tagId";
  @SerializedName(SERIALIZED_NAME_TAG_ID)
  private UUID tagId;

  public static final String SERIALIZED_NAME_TAG_NAME = "tagName";
  @SerializedName(SERIALIZED_NAME_TAG_NAME)
  private String tagName;

  public Prediction() {
  }

  public Prediction(
     Float probability, 
     UUID tagId, 
     String tagName
  ) {
    this();
    this.probability = probability;
    this.tagId = tagId;
    this.tagName = tagName;
  }

  public Prediction boundingBox(BoundingBox boundingBox) {
    this.boundingBox = boundingBox;
    return this;
  }

  /**
   * Get boundingBox
   * @return boundingBox
   */
  @javax.annotation.Nullable
  public BoundingBox getBoundingBox() {
    return boundingBox;
  }

  public void setBoundingBox(BoundingBox boundingBox) {
    this.boundingBox = boundingBox;
  }


  /**
   * Probability of the tag.
   * @return probability
   */
  @javax.annotation.Nullable
  public Float getProbability() {
    return probability;
  }



  /**
   * Id of the predicted tag.
   * @return tagId
   */
  @javax.annotation.Nullable
  public UUID getTagId() {
    return tagId;
  }



  /**
   * Name of the predicted tag.
   * @return tagName
   */
  @javax.annotation.Nullable
  public String getTagName() {
    return tagName;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Prediction prediction = (Prediction) o;
    return Objects.equals(this.boundingBox, prediction.boundingBox) &&
        Objects.equals(this.probability, prediction.probability) &&
        Objects.equals(this.tagId, prediction.tagId) &&
        Objects.equals(this.tagName, prediction.tagName);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(boundingBox, probability, tagId, tagName);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Prediction {\n");
    sb.append("    boundingBox: ").append(toIndentedString(boundingBox)).append("\n");
    sb.append("    probability: ").append(toIndentedString(probability)).append("\n");
    sb.append("    tagId: ").append(toIndentedString(tagId)).append("\n");
    sb.append("    tagName: ").append(toIndentedString(tagName)).append("\n");
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
    openapiFields.add("boundingBox");
    openapiFields.add("probability");
    openapiFields.add("tagId");
    openapiFields.add("tagName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Prediction
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Prediction.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Prediction is not found in the empty JSON string", Prediction.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Prediction.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Prediction` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `boundingBox`
      if (jsonObj.get("boundingBox") != null && !jsonObj.get("boundingBox").isJsonNull()) {
        BoundingBox.validateJsonElement(jsonObj.get("boundingBox"));
      }
      if ((jsonObj.get("tagId") != null && !jsonObj.get("tagId").isJsonNull()) && !jsonObj.get("tagId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tagId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tagId").toString()));
      }
      if ((jsonObj.get("tagName") != null && !jsonObj.get("tagName").isJsonNull()) && !jsonObj.get("tagName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tagName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tagName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Prediction.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Prediction' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Prediction> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Prediction.class));

       return (TypeAdapter<T>) new TypeAdapter<Prediction>() {
           @Override
           public void write(JsonWriter out, Prediction value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Prediction read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Prediction given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Prediction
   * @throws IOException if the JSON string is invalid with respect to Prediction
   */
  public static Prediction fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Prediction.class);
  }

  /**
   * Convert an instance of Prediction to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

