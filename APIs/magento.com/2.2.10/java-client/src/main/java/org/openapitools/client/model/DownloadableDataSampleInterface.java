/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
import java.util.Arrays;
import org.openapitools.client.model.DownloadableDataFileContentInterface;

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
 * 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DownloadableDataSampleInterface {
  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private Object extensionAttributes;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_SAMPLE_FILE = "sample_file";
  @SerializedName(SERIALIZED_NAME_SAMPLE_FILE)
  private String sampleFile;

  public static final String SERIALIZED_NAME_SAMPLE_FILE_CONTENT = "sample_file_content";
  @SerializedName(SERIALIZED_NAME_SAMPLE_FILE_CONTENT)
  private DownloadableDataFileContentInterface sampleFileContent;

  public static final String SERIALIZED_NAME_SAMPLE_TYPE = "sample_type";
  @SerializedName(SERIALIZED_NAME_SAMPLE_TYPE)
  private String sampleType;

  public static final String SERIALIZED_NAME_SAMPLE_URL = "sample_url";
  @SerializedName(SERIALIZED_NAME_SAMPLE_URL)
  private String sampleUrl;

  public static final String SERIALIZED_NAME_SORT_ORDER = "sort_order";
  @SerializedName(SERIALIZED_NAME_SORT_ORDER)
  private Integer sortOrder;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public DownloadableDataSampleInterface() {
  }

  public DownloadableDataSampleInterface extensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * ExtensionInterface class for @see \\Magento\\Downloadable\\Api\\Data\\SampleInterface
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public Object getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public DownloadableDataSampleInterface id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Sample(or link) id
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public DownloadableDataSampleInterface sampleFile(String sampleFile) {
    this.sampleFile = sampleFile;
    return this;
  }

  /**
   * relative file path
   * @return sampleFile
   */
  @javax.annotation.Nullable
  public String getSampleFile() {
    return sampleFile;
  }

  public void setSampleFile(String sampleFile) {
    this.sampleFile = sampleFile;
  }


  public DownloadableDataSampleInterface sampleFileContent(DownloadableDataFileContentInterface sampleFileContent) {
    this.sampleFileContent = sampleFileContent;
    return this;
  }

  /**
   * Get sampleFileContent
   * @return sampleFileContent
   */
  @javax.annotation.Nullable
  public DownloadableDataFileContentInterface getSampleFileContent() {
    return sampleFileContent;
  }

  public void setSampleFileContent(DownloadableDataFileContentInterface sampleFileContent) {
    this.sampleFileContent = sampleFileContent;
  }


  public DownloadableDataSampleInterface sampleType(String sampleType) {
    this.sampleType = sampleType;
    return this;
  }

  /**
   * Get sampleType
   * @return sampleType
   */
  @javax.annotation.Nonnull
  public String getSampleType() {
    return sampleType;
  }

  public void setSampleType(String sampleType) {
    this.sampleType = sampleType;
  }


  public DownloadableDataSampleInterface sampleUrl(String sampleUrl) {
    this.sampleUrl = sampleUrl;
    return this;
  }

  /**
   * file URL
   * @return sampleUrl
   */
  @javax.annotation.Nullable
  public String getSampleUrl() {
    return sampleUrl;
  }

  public void setSampleUrl(String sampleUrl) {
    this.sampleUrl = sampleUrl;
  }


  public DownloadableDataSampleInterface sortOrder(Integer sortOrder) {
    this.sortOrder = sortOrder;
    return this;
  }

  /**
   * Order index for sample
   * @return sortOrder
   */
  @javax.annotation.Nonnull
  public Integer getSortOrder() {
    return sortOrder;
  }

  public void setSortOrder(Integer sortOrder) {
    this.sortOrder = sortOrder;
  }


  public DownloadableDataSampleInterface title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Title
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DownloadableDataSampleInterface downloadableDataSampleInterface = (DownloadableDataSampleInterface) o;
    return Objects.equals(this.extensionAttributes, downloadableDataSampleInterface.extensionAttributes) &&
        Objects.equals(this.id, downloadableDataSampleInterface.id) &&
        Objects.equals(this.sampleFile, downloadableDataSampleInterface.sampleFile) &&
        Objects.equals(this.sampleFileContent, downloadableDataSampleInterface.sampleFileContent) &&
        Objects.equals(this.sampleType, downloadableDataSampleInterface.sampleType) &&
        Objects.equals(this.sampleUrl, downloadableDataSampleInterface.sampleUrl) &&
        Objects.equals(this.sortOrder, downloadableDataSampleInterface.sortOrder) &&
        Objects.equals(this.title, downloadableDataSampleInterface.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(extensionAttributes, id, sampleFile, sampleFileContent, sampleType, sampleUrl, sortOrder, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DownloadableDataSampleInterface {\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    sampleFile: ").append(toIndentedString(sampleFile)).append("\n");
    sb.append("    sampleFileContent: ").append(toIndentedString(sampleFileContent)).append("\n");
    sb.append("    sampleType: ").append(toIndentedString(sampleType)).append("\n");
    sb.append("    sampleUrl: ").append(toIndentedString(sampleUrl)).append("\n");
    sb.append("    sortOrder: ").append(toIndentedString(sortOrder)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("extension_attributes");
    openapiFields.add("id");
    openapiFields.add("sample_file");
    openapiFields.add("sample_file_content");
    openapiFields.add("sample_type");
    openapiFields.add("sample_url");
    openapiFields.add("sort_order");
    openapiFields.add("title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("sample_type");
    openapiRequiredFields.add("sort_order");
    openapiRequiredFields.add("title");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DownloadableDataSampleInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DownloadableDataSampleInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DownloadableDataSampleInterface is not found in the empty JSON string", DownloadableDataSampleInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DownloadableDataSampleInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DownloadableDataSampleInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DownloadableDataSampleInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("sample_file") != null && !jsonObj.get("sample_file").isJsonNull()) && !jsonObj.get("sample_file").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sample_file` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sample_file").toString()));
      }
      // validate the optional field `sample_file_content`
      if (jsonObj.get("sample_file_content") != null && !jsonObj.get("sample_file_content").isJsonNull()) {
        DownloadableDataFileContentInterface.validateJsonElement(jsonObj.get("sample_file_content"));
      }
      if (!jsonObj.get("sample_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sample_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sample_type").toString()));
      }
      if ((jsonObj.get("sample_url") != null && !jsonObj.get("sample_url").isJsonNull()) && !jsonObj.get("sample_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sample_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sample_url").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DownloadableDataSampleInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DownloadableDataSampleInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DownloadableDataSampleInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DownloadableDataSampleInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<DownloadableDataSampleInterface>() {
           @Override
           public void write(JsonWriter out, DownloadableDataSampleInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DownloadableDataSampleInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DownloadableDataSampleInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DownloadableDataSampleInterface
   * @throws IOException if the JSON string is invalid with respect to DownloadableDataSampleInterface
   */
  public static DownloadableDataSampleInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DownloadableDataSampleInterface.class);
  }

  /**
   * Convert an instance of DownloadableDataSampleInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

