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
import org.openapitools.client.model.EmbeddedImage;
import org.openapitools.client.model.OutputFile;
import org.openapitools.client.model.Size;
import org.openapitools.client.model.Style;

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
 * TextQRCode
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:56.961414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TextQRCode {
  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private Object data;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private EmbeddedImage image;

  public static final String SERIALIZED_NAME_OUTPUT = "output";
  @SerializedName(SERIALIZED_NAME_OUTPUT)
  private OutputFile output = {"filename":"qrcode","format":"svg"};

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private Size size = {"error_correction":"M","quiet_zone":4,"width":200};

  public static final String SERIALIZED_NAME_STYLE = "style";
  @SerializedName(SERIALIZED_NAME_STYLE)
  private Style style = {"background":{},"inner_eye":{"shape":"default"},"module":{"color":"black","shape":"default"},"outer_eye":{"shape":"default"}};

  public TextQRCode() {
  }

  public TextQRCode data(Object data) {
    this.data = data;
    return this;
  }

  /**
   * &#x60;data&#x60; property allows you to specify the text stored in the QR Code.
   * @return data
   */
  @javax.annotation.Nonnull
  public Object getData() {
    return data;
  }

  public void setData(Object data) {
    this.data = data;
  }


  public TextQRCode image(EmbeddedImage image) {
    this.image = image;
    return this;
  }

  /**
   * &#x60;image&#x60; property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code.
   * @return image
   */
  @javax.annotation.Nullable
  public EmbeddedImage getImage() {
    return image;
  }

  public void setImage(EmbeddedImage image) {
    this.image = image;
  }


  public TextQRCode output(OutputFile output) {
    this.output = output;
    return this;
  }

  /**
   * &#x60;output&#x60; property allows you to specify the name and extension (type) of the file returned by the API
   * @return output
   */
  @javax.annotation.Nullable
  public OutputFile getOutput() {
    return output;
  }

  public void setOutput(OutputFile output) {
    this.output = output;
  }


  public TextQRCode size(Size size) {
    this.size = size;
    return this;
  }

  /**
   * &#x60;size&#x60; property allows you to set the values that define the sizes of the generated QR Code.
   * @return size
   */
  @javax.annotation.Nullable
  public Size getSize() {
    return size;
  }

  public void setSize(Size size) {
    this.size = size;
  }


  public TextQRCode style(Style style) {
    this.style = style;
    return this;
  }

  /**
   * &#x60;style&#x60; property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: &#x60;Black&#x60;, &#x60;azure&#x60;, ... * hex value: &#x60;0x000&#x60;, &#x60;#FFFFFF&#x60;, &#x60;7fffd4&#x60;, ... * RGB/RGBA strings: &#x60;rgb(255, 255, 255)&#x60;, &#x60;rgba(255, 255, 255, 0.5)&#x60;, ... * HSL strings: &#x60;hsl(270, 60%, 70%)&#x60;, &#x60;hsl(270, 60%, 70%, .5)&#x60;, ...  Color values can be obtained from any online color picker like &lt;a href&#x3D;\&quot;https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;developer.mozilla.org&lt;/a&gt;.
   * @return style
   */
  @javax.annotation.Nullable
  public Style getStyle() {
    return style;
  }

  public void setStyle(Style style) {
    this.style = style;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TextQRCode textQRCode = (TextQRCode) o;
    return Objects.equals(this.data, textQRCode.data) &&
        Objects.equals(this.image, textQRCode.image) &&
        Objects.equals(this.output, textQRCode.output) &&
        Objects.equals(this.size, textQRCode.size) &&
        Objects.equals(this.style, textQRCode.style);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, image, output, size, style);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TextQRCode {\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    output: ").append(toIndentedString(output)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    style: ").append(toIndentedString(style)).append("\n");
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
    openapiFields.add("data");
    openapiFields.add("image");
    openapiFields.add("output");
    openapiFields.add("size");
    openapiFields.add("style");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("data");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TextQRCode
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TextQRCode.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TextQRCode is not found in the empty JSON string", TextQRCode.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TextQRCode.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TextQRCode` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TextQRCode.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `image`
      if (jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) {
        EmbeddedImage.validateJsonElement(jsonObj.get("image"));
      }
      // validate the optional field `output`
      if (jsonObj.get("output") != null && !jsonObj.get("output").isJsonNull()) {
        OutputFile.validateJsonElement(jsonObj.get("output"));
      }
      // validate the optional field `size`
      if (jsonObj.get("size") != null && !jsonObj.get("size").isJsonNull()) {
        Size.validateJsonElement(jsonObj.get("size"));
      }
      // validate the optional field `style`
      if (jsonObj.get("style") != null && !jsonObj.get("style").isJsonNull()) {
        Style.validateJsonElement(jsonObj.get("style"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TextQRCode.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TextQRCode' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TextQRCode> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TextQRCode.class));

       return (TypeAdapter<T>) new TypeAdapter<TextQRCode>() {
           @Override
           public void write(JsonWriter out, TextQRCode value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TextQRCode read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TextQRCode given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TextQRCode
   * @throws IOException if the JSON string is invalid with respect to TextQRCode
   */
  public static TextQRCode fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TextQRCode.class);
  }

  /**
   * Convert an instance of TextQRCode to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

