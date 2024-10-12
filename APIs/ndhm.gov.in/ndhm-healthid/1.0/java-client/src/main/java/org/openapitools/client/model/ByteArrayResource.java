/*
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
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
import java.net.URI;
import java.util.Arrays;
import org.openapitools.client.model.ModelFile;
import org.openapitools.client.model.URL;

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
 * ByteArrayResource
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:34.465238-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ByteArrayResource {
  public static final String SERIALIZED_NAME_BYTE_ARRAY = "byteArray";
  @SerializedName(SERIALIZED_NAME_BYTE_ARRAY)
  private byte[] byteArray;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FILE = "file";
  @SerializedName(SERIALIZED_NAME_FILE)
  private ModelFile _file;

  public static final String SERIALIZED_NAME_FILENAME = "filename";
  @SerializedName(SERIALIZED_NAME_FILENAME)
  private String filename;

  public static final String SERIALIZED_NAME_INPUT_STREAM = "inputStream";
  @SerializedName(SERIALIZED_NAME_INPUT_STREAM)
  private Object inputStream;

  public static final String SERIALIZED_NAME_OPEN = "open";
  @SerializedName(SERIALIZED_NAME_OPEN)
  private Boolean open;

  public static final String SERIALIZED_NAME_READABLE = "readable";
  @SerializedName(SERIALIZED_NAME_READABLE)
  private Boolean readable;

  public static final String SERIALIZED_NAME_URI = "uri";
  @SerializedName(SERIALIZED_NAME_URI)
  private URI uri;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private URL url;

  public ByteArrayResource() {
  }

  public ByteArrayResource byteArray(byte[] byteArray) {
    this.byteArray = byteArray;
    return this;
  }

  /**
   * Get byteArray
   * @return byteArray
   */
  @javax.annotation.Nullable
  public byte[] getByteArray() {
    return byteArray;
  }

  public void setByteArray(byte[] byteArray) {
    this.byteArray = byteArray;
  }


  public ByteArrayResource description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ByteArrayResource _file(ModelFile _file) {
    this._file = _file;
    return this;
  }

  /**
   * Get _file
   * @return _file
   */
  @javax.annotation.Nullable
  public ModelFile getFile() {
    return _file;
  }

  public void setFile(ModelFile _file) {
    this._file = _file;
  }


  public ByteArrayResource filename(String filename) {
    this.filename = filename;
    return this;
  }

  /**
   * Get filename
   * @return filename
   */
  @javax.annotation.Nullable
  public String getFilename() {
    return filename;
  }

  public void setFilename(String filename) {
    this.filename = filename;
  }


  public ByteArrayResource inputStream(Object inputStream) {
    this.inputStream = inputStream;
    return this;
  }

  /**
   * Get inputStream
   * @return inputStream
   */
  @javax.annotation.Nullable
  public Object getInputStream() {
    return inputStream;
  }

  public void setInputStream(Object inputStream) {
    this.inputStream = inputStream;
  }


  public ByteArrayResource open(Boolean open) {
    this.open = open;
    return this;
  }

  /**
   * Get open
   * @return open
   */
  @javax.annotation.Nullable
  public Boolean getOpen() {
    return open;
  }

  public void setOpen(Boolean open) {
    this.open = open;
  }


  public ByteArrayResource readable(Boolean readable) {
    this.readable = readable;
    return this;
  }

  /**
   * Get readable
   * @return readable
   */
  @javax.annotation.Nullable
  public Boolean getReadable() {
    return readable;
  }

  public void setReadable(Boolean readable) {
    this.readable = readable;
  }


  public ByteArrayResource uri(URI uri) {
    this.uri = uri;
    return this;
  }

  /**
   * Get uri
   * @return uri
   */
  @javax.annotation.Nullable
  public URI getUri() {
    return uri;
  }

  public void setUri(URI uri) {
    this.uri = uri;
  }


  public ByteArrayResource url(URL url) {
    this.url = url;
    return this;
  }

  /**
   * Get url
   * @return url
   */
  @javax.annotation.Nullable
  public URL getUrl() {
    return url;
  }

  public void setUrl(URL url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ByteArrayResource byteArrayResource = (ByteArrayResource) o;
    return Arrays.equals(this.byteArray, byteArrayResource.byteArray) &&
        Objects.equals(this.description, byteArrayResource.description) &&
        Objects.equals(this._file, byteArrayResource._file) &&
        Objects.equals(this.filename, byteArrayResource.filename) &&
        Objects.equals(this.inputStream, byteArrayResource.inputStream) &&
        Objects.equals(this.open, byteArrayResource.open) &&
        Objects.equals(this.readable, byteArrayResource.readable) &&
        Objects.equals(this.uri, byteArrayResource.uri) &&
        Objects.equals(this.url, byteArrayResource.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(Arrays.hashCode(byteArray), description, _file, filename, inputStream, open, readable, uri, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ByteArrayResource {\n");
    sb.append("    byteArray: ").append(toIndentedString(byteArray)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    _file: ").append(toIndentedString(_file)).append("\n");
    sb.append("    filename: ").append(toIndentedString(filename)).append("\n");
    sb.append("    inputStream: ").append(toIndentedString(inputStream)).append("\n");
    sb.append("    open: ").append(toIndentedString(open)).append("\n");
    sb.append("    readable: ").append(toIndentedString(readable)).append("\n");
    sb.append("    uri: ").append(toIndentedString(uri)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("byteArray");
    openapiFields.add("description");
    openapiFields.add("file");
    openapiFields.add("filename");
    openapiFields.add("inputStream");
    openapiFields.add("open");
    openapiFields.add("readable");
    openapiFields.add("uri");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ByteArrayResource
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ByteArrayResource.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ByteArrayResource is not found in the empty JSON string", ByteArrayResource.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ByteArrayResource.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ByteArrayResource` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `file`
      if (jsonObj.get("file") != null && !jsonObj.get("file").isJsonNull()) {
        ModelFile.validateJsonElement(jsonObj.get("file"));
      }
      if ((jsonObj.get("filename") != null && !jsonObj.get("filename").isJsonNull()) && !jsonObj.get("filename").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `filename` to be a primitive type in the JSON string but got `%s`", jsonObj.get("filename").toString()));
      }
      // validate the optional field `uri`
      if (jsonObj.get("uri") != null && !jsonObj.get("uri").isJsonNull()) {
        URI.validateJsonElement(jsonObj.get("uri"));
      }
      // validate the optional field `url`
      if (jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) {
        URL.validateJsonElement(jsonObj.get("url"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ByteArrayResource.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ByteArrayResource' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ByteArrayResource> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ByteArrayResource.class));

       return (TypeAdapter<T>) new TypeAdapter<ByteArrayResource>() {
           @Override
           public void write(JsonWriter out, ByteArrayResource value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ByteArrayResource read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ByteArrayResource given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ByteArrayResource
   * @throws IOException if the JSON string is invalid with respect to ByteArrayResource
   */
  public static ByteArrayResource fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ByteArrayResource.class);
  }

  /**
   * Convert an instance of ByteArrayResource to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

