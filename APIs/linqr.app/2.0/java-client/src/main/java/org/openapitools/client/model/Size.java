/*
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
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
import org.openapitools.client.model.ECLevel;

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
 * Size
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:56.961414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Size {
  public static final String SERIALIZED_NAME_ERROR_CORRECTION = "error_correction";
  @SerializedName(SERIALIZED_NAME_ERROR_CORRECTION)
  private ECLevel errorCorrection = ECLevel.M;

  public static final String SERIALIZED_NAME_QUIET_ZONE = "quiet_zone";
  @SerializedName(SERIALIZED_NAME_QUIET_ZONE)
  private Integer quietZone = 4;

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private Integer width = 200;

  public Size() {
  }

  public Size errorCorrection(ECLevel errorCorrection) {
    this.errorCorrection = errorCorrection;
    return this;
  }

  /**
   * Error correction level for generated QR Code. Correction mechanism allows to restore some encoded data if it is partially unreadable (e.g. physically damaged). Literals correspond to amount of data (QR Code area) which can be restored: * &#x60;L&#x60;: approx. 7% * &#x60;M&#x60;: approx. 15% * &#x60;Q&#x60;: approx. 25% * &#x60;H&#x60;: approx. 30%  Higher correction level causes in bigger (more data modules) resulting QR Code. **Note:** If image is embedded in the QR Code, &#x60;H&#x60; correction level is chosen automatically and overrides user input.  For more information please refer to: &lt;a href&#x3D;\&quot;https://www.qrcode.com/en/about/error_correction.html\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;QRCode.com&lt;/a&gt;
   * @return errorCorrection
   */
  @javax.annotation.Nullable
  public ECLevel getErrorCorrection() {
    return errorCorrection;
  }

  public void setErrorCorrection(ECLevel errorCorrection) {
    this.errorCorrection = errorCorrection;
  }


  public Size quietZone(Integer quietZone) {
    this.quietZone = quietZone;
    return this;
  }

  /**
   * Default size of margin with background color around the generated QR Code. This length is expressed as number of modules of the Code. Recommended value is 4, but most readers allow you to read the code with smaller or zero margin.  For more information please refer to: &lt;a href&#x3D;\&quot;https://www.qrcode.com/en/howto/code.html\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;QRCode.com&lt;/a&gt;.
   * minimum: 0
   * @return quietZone
   */
  @javax.annotation.Nullable
  public Integer getQuietZone() {
    return quietZone;
  }

  public void setQuietZone(Integer quietZone) {
    this.quietZone = quietZone;
  }


  public Size width(Integer width) {
    this.width = width;
    return this;
  }

  /**
   * Width (and height, as the QR Codes are squares) in pixels of the generated image. If the requested value is &#x60;float&#x60; it will be casted to nearest &#x60;int&#x60;.
   * minimum: 100
   * maximum: 2500
   * @return width
   */
  @javax.annotation.Nullable
  public Integer getWidth() {
    return width;
  }

  public void setWidth(Integer width) {
    this.width = width;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Size size = (Size) o;
    return Objects.equals(this.errorCorrection, size.errorCorrection) &&
        Objects.equals(this.quietZone, size.quietZone) &&
        Objects.equals(this.width, size.width);
  }

  @Override
  public int hashCode() {
    return Objects.hash(errorCorrection, quietZone, width);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Size {\n");
    sb.append("    errorCorrection: ").append(toIndentedString(errorCorrection)).append("\n");
    sb.append("    quietZone: ").append(toIndentedString(quietZone)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
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
    openapiFields.add("error_correction");
    openapiFields.add("quiet_zone");
    openapiFields.add("width");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Size
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Size.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Size is not found in the empty JSON string", Size.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Size.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Size` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `error_correction`
      if (jsonObj.get("error_correction") != null && !jsonObj.get("error_correction").isJsonNull()) {
        ECLevel.validateJsonElement(jsonObj.get("error_correction"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Size.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Size' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Size> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Size.class));

       return (TypeAdapter<T>) new TypeAdapter<Size>() {
           @Override
           public void write(JsonWriter out, Size value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Size read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Size given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Size
   * @throws IOException if the JSON string is invalid with respect to Size
   */
  public static Size fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Size.class);
  }

  /**
   * Convert an instance of Size to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

