/*
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
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
import org.openapitools.client.model.MetricSpecificationV1;

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
 * Service specification.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:10.716364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServiceSpecification {
  public static final String SERIALIZED_NAME_METRIC_SPECIFICATIONS = "metricSpecifications";
  @SerializedName(SERIALIZED_NAME_METRIC_SPECIFICATIONS)
  private List<MetricSpecificationV1> metricSpecifications = new ArrayList<>();

  public ServiceSpecification() {
  }

  public ServiceSpecification metricSpecifications(List<MetricSpecificationV1> metricSpecifications) {
    this.metricSpecifications = metricSpecifications;
    return this;
  }

  public ServiceSpecification addMetricSpecificationsItem(MetricSpecificationV1 metricSpecificationsItem) {
    if (this.metricSpecifications == null) {
      this.metricSpecifications = new ArrayList<>();
    }
    this.metricSpecifications.add(metricSpecificationsItem);
    return this;
  }

  /**
   * Metric specification as defined by shoebox.
   * @return metricSpecifications
   */
  @javax.annotation.Nullable
  public List<MetricSpecificationV1> getMetricSpecifications() {
    return metricSpecifications;
  }

  public void setMetricSpecifications(List<MetricSpecificationV1> metricSpecifications) {
    this.metricSpecifications = metricSpecifications;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServiceSpecification serviceSpecification = (ServiceSpecification) o;
    return Objects.equals(this.metricSpecifications, serviceSpecification.metricSpecifications);
  }

  @Override
  public int hashCode() {
    return Objects.hash(metricSpecifications);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServiceSpecification {\n");
    sb.append("    metricSpecifications: ").append(toIndentedString(metricSpecifications)).append("\n");
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
    openapiFields.add("metricSpecifications");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServiceSpecification
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServiceSpecification.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServiceSpecification is not found in the empty JSON string", ServiceSpecification.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServiceSpecification.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServiceSpecification` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("metricSpecifications") != null && !jsonObj.get("metricSpecifications").isJsonNull()) {
        JsonArray jsonArraymetricSpecifications = jsonObj.getAsJsonArray("metricSpecifications");
        if (jsonArraymetricSpecifications != null) {
          // ensure the json data is an array
          if (!jsonObj.get("metricSpecifications").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `metricSpecifications` to be an array in the JSON string but got `%s`", jsonObj.get("metricSpecifications").toString()));
          }

          // validate the optional field `metricSpecifications` (array)
          for (int i = 0; i < jsonArraymetricSpecifications.size(); i++) {
            MetricSpecificationV1.validateJsonElement(jsonArraymetricSpecifications.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServiceSpecification.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServiceSpecification' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServiceSpecification> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServiceSpecification.class));

       return (TypeAdapter<T>) new TypeAdapter<ServiceSpecification>() {
           @Override
           public void write(JsonWriter out, ServiceSpecification value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServiceSpecification read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServiceSpecification given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServiceSpecification
   * @throws IOException if the JSON string is invalid with respect to ServiceSpecification
   */
  public static ServiceSpecification fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServiceSpecification.class);
  }

  /**
   * Convert an instance of ServiceSpecification to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

