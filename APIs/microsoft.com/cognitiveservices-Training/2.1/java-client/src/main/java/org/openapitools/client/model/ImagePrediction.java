/*
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.openapitools.client.model.Prediction;
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
 * ImagePrediction
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:10.847797-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImagePrediction {
  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_ITERATION = "iteration";
  @SerializedName(SERIALIZED_NAME_ITERATION)
  private UUID iteration;

  public static final String SERIALIZED_NAME_PREDICTIONS = "predictions";
  @SerializedName(SERIALIZED_NAME_PREDICTIONS)
  private List<Prediction> predictions;

  public static final String SERIALIZED_NAME_PROJECT = "project";
  @SerializedName(SERIALIZED_NAME_PROJECT)
  private UUID project;

  public ImagePrediction() {
  }

  public ImagePrediction(
     OffsetDateTime created, 
     UUID id, 
     UUID iteration, 
     List<Prediction> predictions, 
     UUID project
  ) {
    this();
    this.created = created;
    this.id = id;
    this.iteration = iteration;
    this.predictions = predictions;
    this.project = project;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }



  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }



  /**
   * Get iteration
   * @return iteration
   */
  @javax.annotation.Nullable
  public UUID getIteration() {
    return iteration;
  }



  /**
   * Get predictions
   * @return predictions
   */
  @javax.annotation.Nullable
  public List<Prediction> getPredictions() {
    return predictions;
  }



  /**
   * Get project
   * @return project
   */
  @javax.annotation.Nullable
  public UUID getProject() {
    return project;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ImagePrediction imagePrediction = (ImagePrediction) o;
    return Objects.equals(this.created, imagePrediction.created) &&
        Objects.equals(this.id, imagePrediction.id) &&
        Objects.equals(this.iteration, imagePrediction.iteration) &&
        Objects.equals(this.predictions, imagePrediction.predictions) &&
        Objects.equals(this.project, imagePrediction.project);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(created, id, iteration, predictions, project);
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
    sb.append("class ImagePrediction {\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    iteration: ").append(toIndentedString(iteration)).append("\n");
    sb.append("    predictions: ").append(toIndentedString(predictions)).append("\n");
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
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
    openapiFields.add("created");
    openapiFields.add("id");
    openapiFields.add("iteration");
    openapiFields.add("predictions");
    openapiFields.add("project");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ImagePrediction
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImagePrediction.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImagePrediction is not found in the empty JSON string", ImagePrediction.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImagePrediction.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImagePrediction` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("iteration") != null && !jsonObj.get("iteration").isJsonNull()) && !jsonObj.get("iteration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iteration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iteration").toString()));
      }
      if (jsonObj.get("predictions") != null && !jsonObj.get("predictions").isJsonNull()) {
        JsonArray jsonArraypredictions = jsonObj.getAsJsonArray("predictions");
        if (jsonArraypredictions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("predictions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `predictions` to be an array in the JSON string but got `%s`", jsonObj.get("predictions").toString()));
          }

          // validate the optional field `predictions` (array)
          for (int i = 0; i < jsonArraypredictions.size(); i++) {
            Prediction.validateJsonElement(jsonArraypredictions.get(i));
          };
        }
      }
      if ((jsonObj.get("project") != null && !jsonObj.get("project").isJsonNull()) && !jsonObj.get("project").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImagePrediction.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImagePrediction' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImagePrediction> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImagePrediction.class));

       return (TypeAdapter<T>) new TypeAdapter<ImagePrediction>() {
           @Override
           public void write(JsonWriter out, ImagePrediction value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImagePrediction read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImagePrediction given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImagePrediction
   * @throws IOException if the JSON string is invalid with respect to ImagePrediction
   */
  public static ImagePrediction fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImagePrediction.class);
  }

  /**
   * Convert an instance of ImagePrediction to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

