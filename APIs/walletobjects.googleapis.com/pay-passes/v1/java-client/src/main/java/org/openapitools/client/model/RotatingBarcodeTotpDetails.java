/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.RotatingBarcodeTotpDetailsTotpParameters;

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
 * Configuration for the time-based OTP substitutions. See https://tools.ietf.org/html/rfc6238
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RotatingBarcodeTotpDetails {
  /**
   * The TOTP algorithm used to generate the OTP.
   */
  @JsonAdapter(AlgorithmEnum.Adapter.class)
  public enum AlgorithmEnum {
    ALGORITHM_UNSPECIFIED("TOTP_ALGORITHM_UNSPECIFIED"),
    
    SHA1("TOTP_SHA1");

    private String value;

    AlgorithmEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AlgorithmEnum fromValue(String value) {
      for (AlgorithmEnum b : AlgorithmEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AlgorithmEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AlgorithmEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AlgorithmEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AlgorithmEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AlgorithmEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ALGORITHM = "algorithm";
  @SerializedName(SERIALIZED_NAME_ALGORITHM)
  private AlgorithmEnum algorithm;

  public static final String SERIALIZED_NAME_PARAMETERS = "parameters";
  @SerializedName(SERIALIZED_NAME_PARAMETERS)
  private List<RotatingBarcodeTotpDetailsTotpParameters> parameters = new ArrayList<>();

  public static final String SERIALIZED_NAME_PERIOD_MILLIS = "periodMillis";
  @SerializedName(SERIALIZED_NAME_PERIOD_MILLIS)
  private String periodMillis;

  public RotatingBarcodeTotpDetails() {
  }

  public RotatingBarcodeTotpDetails algorithm(AlgorithmEnum algorithm) {
    this.algorithm = algorithm;
    return this;
  }

  /**
   * The TOTP algorithm used to generate the OTP.
   * @return algorithm
   */
  @javax.annotation.Nullable
  public AlgorithmEnum getAlgorithm() {
    return algorithm;
  }

  public void setAlgorithm(AlgorithmEnum algorithm) {
    this.algorithm = algorithm;
  }


  public RotatingBarcodeTotpDetails parameters(List<RotatingBarcodeTotpDetailsTotpParameters> parameters) {
    this.parameters = parameters;
    return this;
  }

  public RotatingBarcodeTotpDetails addParametersItem(RotatingBarcodeTotpDetailsTotpParameters parametersItem) {
    if (this.parameters == null) {
      this.parameters = new ArrayList<>();
    }
    this.parameters.add(parametersItem);
    return this;
  }

  /**
   * The TOTP parameters for each of the {totp_value_*} substitutions. The TotpParameters at index n is used for the {totp_value_n} substitution.
   * @return parameters
   */
  @javax.annotation.Nullable
  public List<RotatingBarcodeTotpDetailsTotpParameters> getParameters() {
    return parameters;
  }

  public void setParameters(List<RotatingBarcodeTotpDetailsTotpParameters> parameters) {
    this.parameters = parameters;
  }


  public RotatingBarcodeTotpDetails periodMillis(String periodMillis) {
    this.periodMillis = periodMillis;
    return this;
  }

  /**
   * The time interval used for the TOTP value generation, in milliseconds.
   * @return periodMillis
   */
  @javax.annotation.Nullable
  public String getPeriodMillis() {
    return periodMillis;
  }

  public void setPeriodMillis(String periodMillis) {
    this.periodMillis = periodMillis;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RotatingBarcodeTotpDetails rotatingBarcodeTotpDetails = (RotatingBarcodeTotpDetails) o;
    return Objects.equals(this.algorithm, rotatingBarcodeTotpDetails.algorithm) &&
        Objects.equals(this.parameters, rotatingBarcodeTotpDetails.parameters) &&
        Objects.equals(this.periodMillis, rotatingBarcodeTotpDetails.periodMillis);
  }

  @Override
  public int hashCode() {
    return Objects.hash(algorithm, parameters, periodMillis);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RotatingBarcodeTotpDetails {\n");
    sb.append("    algorithm: ").append(toIndentedString(algorithm)).append("\n");
    sb.append("    parameters: ").append(toIndentedString(parameters)).append("\n");
    sb.append("    periodMillis: ").append(toIndentedString(periodMillis)).append("\n");
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
    openapiFields.add("algorithm");
    openapiFields.add("parameters");
    openapiFields.add("periodMillis");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RotatingBarcodeTotpDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RotatingBarcodeTotpDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RotatingBarcodeTotpDetails is not found in the empty JSON string", RotatingBarcodeTotpDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RotatingBarcodeTotpDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RotatingBarcodeTotpDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("algorithm") != null && !jsonObj.get("algorithm").isJsonNull()) && !jsonObj.get("algorithm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `algorithm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("algorithm").toString()));
      }
      // validate the optional field `algorithm`
      if (jsonObj.get("algorithm") != null && !jsonObj.get("algorithm").isJsonNull()) {
        AlgorithmEnum.validateJsonElement(jsonObj.get("algorithm"));
      }
      if (jsonObj.get("parameters") != null && !jsonObj.get("parameters").isJsonNull()) {
        JsonArray jsonArrayparameters = jsonObj.getAsJsonArray("parameters");
        if (jsonArrayparameters != null) {
          // ensure the json data is an array
          if (!jsonObj.get("parameters").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `parameters` to be an array in the JSON string but got `%s`", jsonObj.get("parameters").toString()));
          }

          // validate the optional field `parameters` (array)
          for (int i = 0; i < jsonArrayparameters.size(); i++) {
            RotatingBarcodeTotpDetailsTotpParameters.validateJsonElement(jsonArrayparameters.get(i));
          };
        }
      }
      if ((jsonObj.get("periodMillis") != null && !jsonObj.get("periodMillis").isJsonNull()) && !jsonObj.get("periodMillis").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `periodMillis` to be a primitive type in the JSON string but got `%s`", jsonObj.get("periodMillis").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RotatingBarcodeTotpDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RotatingBarcodeTotpDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RotatingBarcodeTotpDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RotatingBarcodeTotpDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<RotatingBarcodeTotpDetails>() {
           @Override
           public void write(JsonWriter out, RotatingBarcodeTotpDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RotatingBarcodeTotpDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RotatingBarcodeTotpDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RotatingBarcodeTotpDetails
   * @throws IOException if the JSON string is invalid with respect to RotatingBarcodeTotpDetails
   */
  public static RotatingBarcodeTotpDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RotatingBarcodeTotpDetails.class);
  }

  /**
   * Convert an instance of RotatingBarcodeTotpDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

