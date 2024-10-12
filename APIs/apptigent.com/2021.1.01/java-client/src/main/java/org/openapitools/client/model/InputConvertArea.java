/*
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
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
import java.math.BigDecimal;
import java.util.Arrays;

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
 * InputConvertArea
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:11.265696-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InputConvertArea {
  public static final String SERIALIZED_NAME_INPUT = "input";
  @SerializedName(SERIALIZED_NAME_INPUT)
  private BigDecimal input;

  /**
   * Gets or Sets source
   */
  @JsonAdapter(SourceEnum.Adapter.class)
  public enum SourceEnum {
    ACRE("Acre"),
    
    HECTARE("Hectare"),
    
    SQUARE_CENTIMETER("SquareCentimeter"),
    
    SQUARE_DECIMETER("SquareDecimeter"),
    
    SQUARE_FOOT("SquareFoot"),
    
    SQUARE_INCH("SquareInch"),
    
    SQUARE_KILOMETER("SquareKilometer"),
    
    SQUARE_METER("SquareMeter"),
    
    SQUARE_MICROMETER("SquareMicrometer"),
    
    SQUARE_MILE("SquareMile"),
    
    SQUARE_MILLIMETER("SquareMillimeter"),
    
    SQUARE_YARD("SquareYard");

    private String value;

    SourceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SourceEnum fromValue(String value) {
      for (SourceEnum b : SourceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SourceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SourceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SourceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SourceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SourceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private SourceEnum source;

  /**
   * Gets or Sets target
   */
  @JsonAdapter(TargetEnum.Adapter.class)
  public enum TargetEnum {
    ACRE("Acre"),
    
    HECTARE("Hectare"),
    
    SQUARE_CENTIMETER("SquareCentimeter"),
    
    SQUARE_DECIMETER("SquareDecimeter"),
    
    SQUARE_FOOT("SquareFoot"),
    
    SQUARE_INCH("SquareInch"),
    
    SQUARE_KILOMETER("SquareKilometer"),
    
    SQUARE_METER("SquareMeter"),
    
    SQUARE_MICROMETER("SquareMicrometer"),
    
    SQUARE_MILE("SquareMile"),
    
    SQUARE_MILLIMETER("SquareMillimeter"),
    
    SQUARE_YARD("SquareYard");

    private String value;

    TargetEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TargetEnum fromValue(String value) {
      for (TargetEnum b : TargetEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TargetEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TargetEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TargetEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TargetEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TargetEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private TargetEnum target;

  public InputConvertArea() {
  }

  public InputConvertArea input(BigDecimal input) {
    this.input = input;
    return this;
  }

  /**
   * Get input
   * @return input
   */
  @javax.annotation.Nonnull
  public BigDecimal getInput() {
    return input;
  }

  public void setInput(BigDecimal input) {
    this.input = input;
  }


  public InputConvertArea source(SourceEnum source) {
    this.source = source;
    return this;
  }

  /**
   * Get source
   * @return source
   */
  @javax.annotation.Nonnull
  public SourceEnum getSource() {
    return source;
  }

  public void setSource(SourceEnum source) {
    this.source = source;
  }


  public InputConvertArea target(TargetEnum target) {
    this.target = target;
    return this;
  }

  /**
   * Get target
   * @return target
   */
  @javax.annotation.Nonnull
  public TargetEnum getTarget() {
    return target;
  }

  public void setTarget(TargetEnum target) {
    this.target = target;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InputConvertArea inputConvertArea = (InputConvertArea) o;
    return Objects.equals(this.input, inputConvertArea.input) &&
        Objects.equals(this.source, inputConvertArea.source) &&
        Objects.equals(this.target, inputConvertArea.target);
  }

  @Override
  public int hashCode() {
    return Objects.hash(input, source, target);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InputConvertArea {\n");
    sb.append("    input: ").append(toIndentedString(input)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
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
    openapiFields.add("input");
    openapiFields.add("source");
    openapiFields.add("target");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("input");
    openapiRequiredFields.add("source");
    openapiRequiredFields.add("target");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InputConvertArea
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InputConvertArea.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InputConvertArea is not found in the empty JSON string", InputConvertArea.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InputConvertArea.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InputConvertArea` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : InputConvertArea.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      // validate the required field `source`
      SourceEnum.validateJsonElement(jsonObj.get("source"));
      if (!jsonObj.get("target").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `target` to be a primitive type in the JSON string but got `%s`", jsonObj.get("target").toString()));
      }
      // validate the required field `target`
      TargetEnum.validateJsonElement(jsonObj.get("target"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InputConvertArea.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InputConvertArea' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InputConvertArea> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InputConvertArea.class));

       return (TypeAdapter<T>) new TypeAdapter<InputConvertArea>() {
           @Override
           public void write(JsonWriter out, InputConvertArea value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InputConvertArea read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InputConvertArea given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InputConvertArea
   * @throws IOException if the JSON string is invalid with respect to InputConvertArea
   */
  public static InputConvertArea fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InputConvertArea.class);
  }

  /**
   * Convert an instance of InputConvertArea to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

