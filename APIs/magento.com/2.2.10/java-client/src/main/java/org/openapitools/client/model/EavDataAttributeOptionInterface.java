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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.EavDataAttributeOptionLabelInterface;

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
 * Created from:
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EavDataAttributeOptionInterface {
  public static final String SERIALIZED_NAME_IS_DEFAULT = "is_default";
  @SerializedName(SERIALIZED_NAME_IS_DEFAULT)
  private Boolean isDefault;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_SORT_ORDER = "sort_order";
  @SerializedName(SERIALIZED_NAME_SORT_ORDER)
  private Integer sortOrder;

  public static final String SERIALIZED_NAME_STORE_LABELS = "store_labels";
  @SerializedName(SERIALIZED_NAME_STORE_LABELS)
  private List<EavDataAttributeOptionLabelInterface> storeLabels = new ArrayList<>();

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public EavDataAttributeOptionInterface() {
  }

  public EavDataAttributeOptionInterface isDefault(Boolean isDefault) {
    this.isDefault = isDefault;
    return this;
  }

  /**
   * Default
   * @return isDefault
   */
  @javax.annotation.Nullable
  public Boolean getIsDefault() {
    return isDefault;
  }

  public void setIsDefault(Boolean isDefault) {
    this.isDefault = isDefault;
  }


  public EavDataAttributeOptionInterface label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Option label
   * @return label
   */
  @javax.annotation.Nonnull
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public EavDataAttributeOptionInterface sortOrder(Integer sortOrder) {
    this.sortOrder = sortOrder;
    return this;
  }

  /**
   * Option order
   * @return sortOrder
   */
  @javax.annotation.Nullable
  public Integer getSortOrder() {
    return sortOrder;
  }

  public void setSortOrder(Integer sortOrder) {
    this.sortOrder = sortOrder;
  }


  public EavDataAttributeOptionInterface storeLabels(List<EavDataAttributeOptionLabelInterface> storeLabels) {
    this.storeLabels = storeLabels;
    return this;
  }

  public EavDataAttributeOptionInterface addStoreLabelsItem(EavDataAttributeOptionLabelInterface storeLabelsItem) {
    if (this.storeLabels == null) {
      this.storeLabels = new ArrayList<>();
    }
    this.storeLabels.add(storeLabelsItem);
    return this;
  }

  /**
   * Option label for store scopes
   * @return storeLabels
   */
  @javax.annotation.Nullable
  public List<EavDataAttributeOptionLabelInterface> getStoreLabels() {
    return storeLabels;
  }

  public void setStoreLabels(List<EavDataAttributeOptionLabelInterface> storeLabels) {
    this.storeLabels = storeLabels;
  }


  public EavDataAttributeOptionInterface value(String value) {
    this.value = value;
    return this;
  }

  /**
   * Option value
   * @return value
   */
  @javax.annotation.Nonnull
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EavDataAttributeOptionInterface eavDataAttributeOptionInterface = (EavDataAttributeOptionInterface) o;
    return Objects.equals(this.isDefault, eavDataAttributeOptionInterface.isDefault) &&
        Objects.equals(this.label, eavDataAttributeOptionInterface.label) &&
        Objects.equals(this.sortOrder, eavDataAttributeOptionInterface.sortOrder) &&
        Objects.equals(this.storeLabels, eavDataAttributeOptionInterface.storeLabels) &&
        Objects.equals(this.value, eavDataAttributeOptionInterface.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isDefault, label, sortOrder, storeLabels, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EavDataAttributeOptionInterface {\n");
    sb.append("    isDefault: ").append(toIndentedString(isDefault)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    sortOrder: ").append(toIndentedString(sortOrder)).append("\n");
    sb.append("    storeLabels: ").append(toIndentedString(storeLabels)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("is_default");
    openapiFields.add("label");
    openapiFields.add("sort_order");
    openapiFields.add("store_labels");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("label");
    openapiRequiredFields.add("value");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EavDataAttributeOptionInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EavDataAttributeOptionInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EavDataAttributeOptionInterface is not found in the empty JSON string", EavDataAttributeOptionInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EavDataAttributeOptionInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EavDataAttributeOptionInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EavDataAttributeOptionInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      if (jsonObj.get("store_labels") != null && !jsonObj.get("store_labels").isJsonNull()) {
        JsonArray jsonArraystoreLabels = jsonObj.getAsJsonArray("store_labels");
        if (jsonArraystoreLabels != null) {
          // ensure the json data is an array
          if (!jsonObj.get("store_labels").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `store_labels` to be an array in the JSON string but got `%s`", jsonObj.get("store_labels").toString()));
          }

          // validate the optional field `store_labels` (array)
          for (int i = 0; i < jsonArraystoreLabels.size(); i++) {
            EavDataAttributeOptionLabelInterface.validateJsonElement(jsonArraystoreLabels.get(i));
          };
        }
      }
      if (!jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EavDataAttributeOptionInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EavDataAttributeOptionInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EavDataAttributeOptionInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EavDataAttributeOptionInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<EavDataAttributeOptionInterface>() {
           @Override
           public void write(JsonWriter out, EavDataAttributeOptionInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EavDataAttributeOptionInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EavDataAttributeOptionInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EavDataAttributeOptionInterface
   * @throws IOException if the JSON string is invalid with respect to EavDataAttributeOptionInterface
   */
  public static EavDataAttributeOptionInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EavDataAttributeOptionInterface.class);
  }

  /**
   * Convert an instance of EavDataAttributeOptionInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

