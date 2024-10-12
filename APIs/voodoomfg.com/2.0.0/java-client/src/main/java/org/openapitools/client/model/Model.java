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
 * Model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:36.543601-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Model {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_RENDERING_URL = "rendering_url";
  @SerializedName(SERIALIZED_NAME_RENDERING_URL)
  private String renderingUrl;

  public static final String SERIALIZED_NAME_SURFACE_AREA = "surface_area";
  @SerializedName(SERIALIZED_NAME_SURFACE_AREA)
  private BigDecimal surfaceArea;

  public static final String SERIALIZED_NAME_VOLUME = "volume";
  @SerializedName(SERIALIZED_NAME_VOLUME)
  private BigDecimal volume;

  public static final String SERIALIZED_NAME_X = "x";
  @SerializedName(SERIALIZED_NAME_X)
  private BigDecimal x;

  public static final String SERIALIZED_NAME_Y = "y";
  @SerializedName(SERIALIZED_NAME_Y)
  private BigDecimal y;

  public static final String SERIALIZED_NAME_Z = "z";
  @SerializedName(SERIALIZED_NAME_Z)
  private BigDecimal z;

  public Model() {
  }

  public Model id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * The unique identifier for this model. Use this value when submitting an order to specify the model you want to print.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public Model renderingUrl(String renderingUrl) {
    this.renderingUrl = renderingUrl;
    return this;
  }

  /**
   * (reserved) URL with a rendering of the model. Value is null until the rendering is completed.
   * @return renderingUrl
   */
  @javax.annotation.Nullable
  public String getRenderingUrl() {
    return renderingUrl;
  }

  public void setRenderingUrl(String renderingUrl) {
    this.renderingUrl = renderingUrl;
  }


  public Model surfaceArea(BigDecimal surfaceArea) {
    this.surfaceArea = surfaceArea;
    return this;
  }

  /**
   * The unitless surface area of the submitted model. This is calculated when the model is created.
   * @return surfaceArea
   */
  @javax.annotation.Nullable
  public BigDecimal getSurfaceArea() {
    return surfaceArea;
  }

  public void setSurfaceArea(BigDecimal surfaceArea) {
    this.surfaceArea = surfaceArea;
  }


  public Model volume(BigDecimal volume) {
    this.volume = volume;
    return this;
  }

  /**
   * The unitless volume of the submitted model. This is calculated when the model is created.
   * @return volume
   */
  @javax.annotation.Nullable
  public BigDecimal getVolume() {
    return volume;
  }

  public void setVolume(BigDecimal volume) {
    this.volume = volume;
  }


  public Model x(BigDecimal x) {
    this.x = x;
    return this;
  }

  /**
   * The unitless x-axis length of the model&#39;s bounding box. This is calculated when the model is created.
   * @return x
   */
  @javax.annotation.Nullable
  public BigDecimal getX() {
    return x;
  }

  public void setX(BigDecimal x) {
    this.x = x;
  }


  public Model y(BigDecimal y) {
    this.y = y;
    return this;
  }

  /**
   * The unitless y-axis length of the model&#39;s bounding box. This is calculated when the model is created.
   * @return y
   */
  @javax.annotation.Nullable
  public BigDecimal getY() {
    return y;
  }

  public void setY(BigDecimal y) {
    this.y = y;
  }


  public Model z(BigDecimal z) {
    this.z = z;
    return this;
  }

  /**
   * The unitless z-axis length of the model&#39;s bounding box. This is calculated when the model is created.
   * @return z
   */
  @javax.annotation.Nullable
  public BigDecimal getZ() {
    return z;
  }

  public void setZ(BigDecimal z) {
    this.z = z;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Model model = (Model) o;
    return Objects.equals(this.id, model.id) &&
        Objects.equals(this.renderingUrl, model.renderingUrl) &&
        Objects.equals(this.surfaceArea, model.surfaceArea) &&
        Objects.equals(this.volume, model.volume) &&
        Objects.equals(this.x, model.x) &&
        Objects.equals(this.y, model.y) &&
        Objects.equals(this.z, model.z);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, renderingUrl, surfaceArea, volume, x, y, z);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Model {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    renderingUrl: ").append(toIndentedString(renderingUrl)).append("\n");
    sb.append("    surfaceArea: ").append(toIndentedString(surfaceArea)).append("\n");
    sb.append("    volume: ").append(toIndentedString(volume)).append("\n");
    sb.append("    x: ").append(toIndentedString(x)).append("\n");
    sb.append("    y: ").append(toIndentedString(y)).append("\n");
    sb.append("    z: ").append(toIndentedString(z)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("rendering_url");
    openapiFields.add("surface_area");
    openapiFields.add("volume");
    openapiFields.add("x");
    openapiFields.add("y");
    openapiFields.add("z");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Model
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Model.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Model is not found in the empty JSON string", Model.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Model.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Model` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("rendering_url") != null && !jsonObj.get("rendering_url").isJsonNull()) && !jsonObj.get("rendering_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rendering_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rendering_url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Model.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Model' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Model> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Model.class));

       return (TypeAdapter<T>) new TypeAdapter<Model>() {
           @Override
           public void write(JsonWriter out, Model value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Model read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Model given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Model
   * @throws IOException if the JSON string is invalid with respect to Model
   */
  public static Model fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Model.class);
  }

  /**
   * Convert an instance of Model to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

