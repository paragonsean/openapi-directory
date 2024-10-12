/*
 * Voodoo Manufacturing 3D Print API
 * Welcome to the Voodoo Manufacturing API docs!  Your Voodoo Manufacturing API key must be included with each request to the API. The API will look for the key in the \"api_key\" header of the request. <a href=\"https://voodoomfg.com/3d-print-api#get-access\" target=\"_blank\">You can request a key here.</a>  This API provides a programmatic interface for submitting printing orders to Voodoo Manufacturing. The general process for creating an order is as follows:   - Get a list of the available materials with the /materials endpoint   - Upload models to the API with the /models endpoint   - Get quotes for shipping methods with the /order/shipping endpoint   - Get a quote for an order with the /order/create endpoint   - Confirm the order with the /order/confirm endpoint  Uploaded models and orders can be retrieved either in bulk or by id at the /model and /order endpoints, respectively.  In some cases, you may wish to get a quote for a specific model without the context of an order. In this case, you may use the /model/quote (if you've already uploaded the model to the API) or the /model/quote_attrs (lets you quote based on calculated model attributes) endpoints. 
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@voodoomfg.com
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
import org.openapitools.client.model.ProductionOptions;

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
 * Print
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:36.543601-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Print {
  public static final String SERIALIZED_NAME_MATERIAL_ID = "material_id";
  @SerializedName(SERIALIZED_NAME_MATERIAL_ID)
  private Integer materialId;

  public static final String SERIALIZED_NAME_MODEL_ID = "model_id";
  @SerializedName(SERIALIZED_NAME_MODEL_ID)
  private Integer modelId;

  public static final String SERIALIZED_NAME_OPTIONS = "options";
  @SerializedName(SERIALIZED_NAME_OPTIONS)
  private ProductionOptions options;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Integer quantity;

  public static final String SERIALIZED_NAME_UNITS = "units";
  @SerializedName(SERIALIZED_NAME_UNITS)
  private String units;

  public Print() {
  }

  public Print materialId(Integer materialId) {
    this.materialId = materialId;
    return this;
  }

  /**
   * The unique identifier of the material you&#39;d like to print in. This value comes from the id field of the material object.
   * @return materialId
   */
  @javax.annotation.Nullable
  public Integer getMaterialId() {
    return materialId;
  }

  public void setMaterialId(Integer materialId) {
    this.materialId = materialId;
  }


  public Print modelId(Integer modelId) {
    this.modelId = modelId;
    return this;
  }

  /**
   * The unique identifier of the model you&#39;d like to print. This value comes from the id field of the model object.
   * @return modelId
   */
  @javax.annotation.Nullable
  public Integer getModelId() {
    return modelId;
  }

  public void setModelId(Integer modelId) {
    this.modelId = modelId;
  }


  public Print options(ProductionOptions options) {
    this.options = options;
    return this;
  }

  /**
   * Get options
   * @return options
   */
  @javax.annotation.Nullable
  public ProductionOptions getOptions() {
    return options;
  }

  public void setOptions(ProductionOptions options) {
    this.options = options;
  }


  public Print quantity(Integer quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * The number of prints to order for this material/model pair.
   * @return quantity
   */
  @javax.annotation.Nullable
  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }


  public Print units(String units) {
    this.units = units;
    return this;
  }

  /**
   * The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;.
   * @return units
   */
  @javax.annotation.Nullable
  public String getUnits() {
    return units;
  }

  public void setUnits(String units) {
    this.units = units;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Print print = (Print) o;
    return Objects.equals(this.materialId, print.materialId) &&
        Objects.equals(this.modelId, print.modelId) &&
        Objects.equals(this.options, print.options) &&
        Objects.equals(this.quantity, print.quantity) &&
        Objects.equals(this.units, print.units);
  }

  @Override
  public int hashCode() {
    return Objects.hash(materialId, modelId, options, quantity, units);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Print {\n");
    sb.append("    materialId: ").append(toIndentedString(materialId)).append("\n");
    sb.append("    modelId: ").append(toIndentedString(modelId)).append("\n");
    sb.append("    options: ").append(toIndentedString(options)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    units: ").append(toIndentedString(units)).append("\n");
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
    openapiFields.add("material_id");
    openapiFields.add("model_id");
    openapiFields.add("options");
    openapiFields.add("quantity");
    openapiFields.add("units");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Print
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Print.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Print is not found in the empty JSON string", Print.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Print.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Print` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `options`
      if (jsonObj.get("options") != null && !jsonObj.get("options").isJsonNull()) {
        ProductionOptions.validateJsonElement(jsonObj.get("options"));
      }
      if ((jsonObj.get("units") != null && !jsonObj.get("units").isJsonNull()) && !jsonObj.get("units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("units").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Print.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Print' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Print> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Print.class));

       return (TypeAdapter<T>) new TypeAdapter<Print>() {
           @Override
           public void write(JsonWriter out, Print value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Print read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Print given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Print
   * @throws IOException if the JSON string is invalid with respect to Print
   */
  public static Print fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Print.class);
  }

  /**
   * Convert an instance of Print to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

