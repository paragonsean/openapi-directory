/*
 * Transportation Laws and Incentives
 * Query our database of federal and state laws and incentives for alternative fuels and vehicles, air quality, fuel efficiency, and other transportation-related topics. This dataset powers the <a href=\"https://afdc.energy.gov/laws\">Federal and State Laws and Incentives</a> on the Alternative Fuels Data Center.
 *
 * The version of the OpenAPI document: 0.1.0
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
import org.openapitools.client.model.Law;
import org.openapitools.client.model.Metadata;

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
 * LawsResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:50.620299-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LawsResponse {
  public static final String SERIALIZED_NAME_INPUTS = "inputs";
  @SerializedName(SERIALIZED_NAME_INPUTS)
  private Object inputs = null;

  public static final String SERIALIZED_NAME_METADATA = "metadata";
  @SerializedName(SERIALIZED_NAME_METADATA)
  private Metadata metadata;

  public static final String SERIALIZED_NAME_RESULT = "result";
  @SerializedName(SERIALIZED_NAME_RESULT)
  private List<Law> result = new ArrayList<>();

  public LawsResponse() {
  }

  public LawsResponse inputs(Object inputs) {
    this.inputs = inputs;
    return this;
  }

  /**
   * The parameters that were passed to the API
   * @return inputs
   */
  @javax.annotation.Nullable
  public Object getInputs() {
    return inputs;
  }

  public void setInputs(Object inputs) {
    this.inputs = inputs;
  }


  public LawsResponse metadata(Metadata metadata) {
    this.metadata = metadata;
    return this;
  }

  /**
   * Get metadata
   * @return metadata
   */
  @javax.annotation.Nonnull
  public Metadata getMetadata() {
    return metadata;
  }

  public void setMetadata(Metadata metadata) {
    this.metadata = metadata;
  }


  public LawsResponse result(List<Law> result) {
    this.result = result;
    return this;
  }

  public LawsResponse addResultItem(Law resultItem) {
    if (this.result == null) {
      this.result = new ArrayList<>();
    }
    this.result.add(resultItem);
    return this;
  }

  /**
   * The array of laws returned
   * @return result
   */
  @javax.annotation.Nonnull
  public List<Law> getResult() {
    return result;
  }

  public void setResult(List<Law> result) {
    this.result = result;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LawsResponse lawsResponse = (LawsResponse) o;
    return Objects.equals(this.inputs, lawsResponse.inputs) &&
        Objects.equals(this.metadata, lawsResponse.metadata) &&
        Objects.equals(this.result, lawsResponse.result);
  }

  @Override
  public int hashCode() {
    return Objects.hash(inputs, metadata, result);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LawsResponse {\n");
    sb.append("    inputs: ").append(toIndentedString(inputs)).append("\n");
    sb.append("    metadata: ").append(toIndentedString(metadata)).append("\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
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
    openapiFields.add("inputs");
    openapiFields.add("metadata");
    openapiFields.add("result");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("inputs");
    openapiRequiredFields.add("metadata");
    openapiRequiredFields.add("result");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LawsResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LawsResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LawsResponse is not found in the empty JSON string", LawsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LawsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LawsResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : LawsResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `metadata`
      Metadata.validateJsonElement(jsonObj.get("metadata"));
      // ensure the json data is an array
      if (!jsonObj.get("result").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `result` to be an array in the JSON string but got `%s`", jsonObj.get("result").toString()));
      }

      JsonArray jsonArrayresult = jsonObj.getAsJsonArray("result");
      // validate the required field `result` (array)
      for (int i = 0; i < jsonArrayresult.size(); i++) {
        Law.validateJsonElement(jsonArrayresult.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LawsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LawsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LawsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LawsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<LawsResponse>() {
           @Override
           public void write(JsonWriter out, LawsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LawsResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LawsResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LawsResponse
   * @throws IOException if the JSON string is invalid with respect to LawsResponse
   */
  public static LawsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LawsResponse.class);
  }

  /**
   * Convert an instance of LawsResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

