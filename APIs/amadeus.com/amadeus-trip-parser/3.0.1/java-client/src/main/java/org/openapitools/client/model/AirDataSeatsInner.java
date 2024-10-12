/*
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
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
import org.openapitools.client.model.AssociationRefs;

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
 * AirDataSeatsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:02.012843-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AirDataSeatsInner {
  public static final String SERIALIZED_NAME_CABIN = "cabin";
  @SerializedName(SERIALIZED_NAME_CABIN)
  private String cabin;

  public static final String SERIALIZED_NAME_NUMBER = "number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private String number;

  public static final String SERIALIZED_NAME_ASSOCIATION_REFS = "associationRefs";
  @SerializedName(SERIALIZED_NAME_ASSOCIATION_REFS)
  private List<AssociationRefs> associationRefs = new ArrayList<>();

  public AirDataSeatsInner() {
  }

  public AirDataSeatsInner cabin(String cabin) {
    this.cabin = cabin;
    return this;
  }

  /**
   * Cabin code associated to the seat
   * @return cabin
   */
  @javax.annotation.Nullable
  public String getCabin() {
    return cabin;
  }

  public void setCabin(String cabin) {
    this.cabin = cabin;
  }


  public AirDataSeatsInner number(String number) {
    this.number = number;
    return this;
  }

  /**
   * Seat number corresponding to the concatenation of the seatmap row and the column information, for example 12B&#39;
   * @return number
   */
  @javax.annotation.Nullable
  public String getNumber() {
    return number;
  }

  public void setNumber(String number) {
    this.number = number;
  }


  public AirDataSeatsInner associationRefs(List<AssociationRefs> associationRefs) {
    this.associationRefs = associationRefs;
    return this;
  }

  public AirDataSeatsInner addAssociationRefsItem(AssociationRefs associationRefsItem) {
    if (this.associationRefs == null) {
      this.associationRefs = new ArrayList<>();
    }
    this.associationRefs.add(associationRefsItem);
    return this;
  }

  /**
   * Get associationRefs
   * @return associationRefs
   */
  @javax.annotation.Nullable
  public List<AssociationRefs> getAssociationRefs() {
    return associationRefs;
  }

  public void setAssociationRefs(List<AssociationRefs> associationRefs) {
    this.associationRefs = associationRefs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AirDataSeatsInner airDataSeatsInner = (AirDataSeatsInner) o;
    return Objects.equals(this.cabin, airDataSeatsInner.cabin) &&
        Objects.equals(this.number, airDataSeatsInner.number) &&
        Objects.equals(this.associationRefs, airDataSeatsInner.associationRefs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cabin, number, associationRefs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AirDataSeatsInner {\n");
    sb.append("    cabin: ").append(toIndentedString(cabin)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    associationRefs: ").append(toIndentedString(associationRefs)).append("\n");
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
    openapiFields.add("cabin");
    openapiFields.add("number");
    openapiFields.add("associationRefs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AirDataSeatsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AirDataSeatsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AirDataSeatsInner is not found in the empty JSON string", AirDataSeatsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AirDataSeatsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AirDataSeatsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("cabin") != null && !jsonObj.get("cabin").isJsonNull()) && !jsonObj.get("cabin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cabin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cabin").toString()));
      }
      if ((jsonObj.get("number") != null && !jsonObj.get("number").isJsonNull()) && !jsonObj.get("number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number").toString()));
      }
      if (jsonObj.get("associationRefs") != null && !jsonObj.get("associationRefs").isJsonNull()) {
        JsonArray jsonArrayassociationRefs = jsonObj.getAsJsonArray("associationRefs");
        if (jsonArrayassociationRefs != null) {
          // ensure the json data is an array
          if (!jsonObj.get("associationRefs").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `associationRefs` to be an array in the JSON string but got `%s`", jsonObj.get("associationRefs").toString()));
          }

          // validate the optional field `associationRefs` (array)
          for (int i = 0; i < jsonArrayassociationRefs.size(); i++) {
            AssociationRefs.validateJsonElement(jsonArrayassociationRefs.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AirDataSeatsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AirDataSeatsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AirDataSeatsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AirDataSeatsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AirDataSeatsInner>() {
           @Override
           public void write(JsonWriter out, AirDataSeatsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AirDataSeatsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AirDataSeatsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AirDataSeatsInner
   * @throws IOException if the JSON string is invalid with respect to AirDataSeatsInner
   */
  public static AirDataSeatsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AirDataSeatsInner.class);
  }

  /**
   * Convert an instance of AirDataSeatsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

