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
import org.openapitools.client.model.BundleDataBundleOptionInterface;
import org.openapitools.client.model.CatalogDataCustomOptionInterface;
import org.openapitools.client.model.ConfigurableProductDataConfigurableItemOptionValueInterface;
import org.openapitools.client.model.DownloadableDataDownloadableOptionInterface;
import org.openapitools.client.model.GiftCardDataGiftCardOptionInterface;

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
 * ExtensionInterface class for @see \\Magento\\Quote\\Api\\Data\\ProductOptionInterface
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QuoteDataProductOptionExtensionInterface {
  public static final String SERIALIZED_NAME_BUNDLE_OPTIONS = "bundle_options";
  @SerializedName(SERIALIZED_NAME_BUNDLE_OPTIONS)
  private List<BundleDataBundleOptionInterface> bundleOptions = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONFIGURABLE_ITEM_OPTIONS = "configurable_item_options";
  @SerializedName(SERIALIZED_NAME_CONFIGURABLE_ITEM_OPTIONS)
  private List<ConfigurableProductDataConfigurableItemOptionValueInterface> configurableItemOptions = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_OPTIONS = "custom_options";
  @SerializedName(SERIALIZED_NAME_CUSTOM_OPTIONS)
  private List<CatalogDataCustomOptionInterface> customOptions = new ArrayList<>();

  public static final String SERIALIZED_NAME_DOWNLOADABLE_OPTION = "downloadable_option";
  @SerializedName(SERIALIZED_NAME_DOWNLOADABLE_OPTION)
  private DownloadableDataDownloadableOptionInterface downloadableOption;

  public static final String SERIALIZED_NAME_GIFTCARD_ITEM_OPTION = "giftcard_item_option";
  @SerializedName(SERIALIZED_NAME_GIFTCARD_ITEM_OPTION)
  private GiftCardDataGiftCardOptionInterface giftcardItemOption;

  public QuoteDataProductOptionExtensionInterface() {
  }

  public QuoteDataProductOptionExtensionInterface bundleOptions(List<BundleDataBundleOptionInterface> bundleOptions) {
    this.bundleOptions = bundleOptions;
    return this;
  }

  public QuoteDataProductOptionExtensionInterface addBundleOptionsItem(BundleDataBundleOptionInterface bundleOptionsItem) {
    if (this.bundleOptions == null) {
      this.bundleOptions = new ArrayList<>();
    }
    this.bundleOptions.add(bundleOptionsItem);
    return this;
  }

  /**
   * Get bundleOptions
   * @return bundleOptions
   */
  @javax.annotation.Nullable
  public List<BundleDataBundleOptionInterface> getBundleOptions() {
    return bundleOptions;
  }

  public void setBundleOptions(List<BundleDataBundleOptionInterface> bundleOptions) {
    this.bundleOptions = bundleOptions;
  }


  public QuoteDataProductOptionExtensionInterface configurableItemOptions(List<ConfigurableProductDataConfigurableItemOptionValueInterface> configurableItemOptions) {
    this.configurableItemOptions = configurableItemOptions;
    return this;
  }

  public QuoteDataProductOptionExtensionInterface addConfigurableItemOptionsItem(ConfigurableProductDataConfigurableItemOptionValueInterface configurableItemOptionsItem) {
    if (this.configurableItemOptions == null) {
      this.configurableItemOptions = new ArrayList<>();
    }
    this.configurableItemOptions.add(configurableItemOptionsItem);
    return this;
  }

  /**
   * Get configurableItemOptions
   * @return configurableItemOptions
   */
  @javax.annotation.Nullable
  public List<ConfigurableProductDataConfigurableItemOptionValueInterface> getConfigurableItemOptions() {
    return configurableItemOptions;
  }

  public void setConfigurableItemOptions(List<ConfigurableProductDataConfigurableItemOptionValueInterface> configurableItemOptions) {
    this.configurableItemOptions = configurableItemOptions;
  }


  public QuoteDataProductOptionExtensionInterface customOptions(List<CatalogDataCustomOptionInterface> customOptions) {
    this.customOptions = customOptions;
    return this;
  }

  public QuoteDataProductOptionExtensionInterface addCustomOptionsItem(CatalogDataCustomOptionInterface customOptionsItem) {
    if (this.customOptions == null) {
      this.customOptions = new ArrayList<>();
    }
    this.customOptions.add(customOptionsItem);
    return this;
  }

  /**
   * Get customOptions
   * @return customOptions
   */
  @javax.annotation.Nullable
  public List<CatalogDataCustomOptionInterface> getCustomOptions() {
    return customOptions;
  }

  public void setCustomOptions(List<CatalogDataCustomOptionInterface> customOptions) {
    this.customOptions = customOptions;
  }


  public QuoteDataProductOptionExtensionInterface downloadableOption(DownloadableDataDownloadableOptionInterface downloadableOption) {
    this.downloadableOption = downloadableOption;
    return this;
  }

  /**
   * Get downloadableOption
   * @return downloadableOption
   */
  @javax.annotation.Nullable
  public DownloadableDataDownloadableOptionInterface getDownloadableOption() {
    return downloadableOption;
  }

  public void setDownloadableOption(DownloadableDataDownloadableOptionInterface downloadableOption) {
    this.downloadableOption = downloadableOption;
  }


  public QuoteDataProductOptionExtensionInterface giftcardItemOption(GiftCardDataGiftCardOptionInterface giftcardItemOption) {
    this.giftcardItemOption = giftcardItemOption;
    return this;
  }

  /**
   * Get giftcardItemOption
   * @return giftcardItemOption
   */
  @javax.annotation.Nullable
  public GiftCardDataGiftCardOptionInterface getGiftcardItemOption() {
    return giftcardItemOption;
  }

  public void setGiftcardItemOption(GiftCardDataGiftCardOptionInterface giftcardItemOption) {
    this.giftcardItemOption = giftcardItemOption;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QuoteDataProductOptionExtensionInterface quoteDataProductOptionExtensionInterface = (QuoteDataProductOptionExtensionInterface) o;
    return Objects.equals(this.bundleOptions, quoteDataProductOptionExtensionInterface.bundleOptions) &&
        Objects.equals(this.configurableItemOptions, quoteDataProductOptionExtensionInterface.configurableItemOptions) &&
        Objects.equals(this.customOptions, quoteDataProductOptionExtensionInterface.customOptions) &&
        Objects.equals(this.downloadableOption, quoteDataProductOptionExtensionInterface.downloadableOption) &&
        Objects.equals(this.giftcardItemOption, quoteDataProductOptionExtensionInterface.giftcardItemOption);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bundleOptions, configurableItemOptions, customOptions, downloadableOption, giftcardItemOption);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QuoteDataProductOptionExtensionInterface {\n");
    sb.append("    bundleOptions: ").append(toIndentedString(bundleOptions)).append("\n");
    sb.append("    configurableItemOptions: ").append(toIndentedString(configurableItemOptions)).append("\n");
    sb.append("    customOptions: ").append(toIndentedString(customOptions)).append("\n");
    sb.append("    downloadableOption: ").append(toIndentedString(downloadableOption)).append("\n");
    sb.append("    giftcardItemOption: ").append(toIndentedString(giftcardItemOption)).append("\n");
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
    openapiFields.add("bundle_options");
    openapiFields.add("configurable_item_options");
    openapiFields.add("custom_options");
    openapiFields.add("downloadable_option");
    openapiFields.add("giftcard_item_option");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QuoteDataProductOptionExtensionInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QuoteDataProductOptionExtensionInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QuoteDataProductOptionExtensionInterface is not found in the empty JSON string", QuoteDataProductOptionExtensionInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QuoteDataProductOptionExtensionInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QuoteDataProductOptionExtensionInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("bundle_options") != null && !jsonObj.get("bundle_options").isJsonNull()) {
        JsonArray jsonArraybundleOptions = jsonObj.getAsJsonArray("bundle_options");
        if (jsonArraybundleOptions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("bundle_options").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `bundle_options` to be an array in the JSON string but got `%s`", jsonObj.get("bundle_options").toString()));
          }

          // validate the optional field `bundle_options` (array)
          for (int i = 0; i < jsonArraybundleOptions.size(); i++) {
            BundleDataBundleOptionInterface.validateJsonElement(jsonArraybundleOptions.get(i));
          };
        }
      }
      if (jsonObj.get("configurable_item_options") != null && !jsonObj.get("configurable_item_options").isJsonNull()) {
        JsonArray jsonArrayconfigurableItemOptions = jsonObj.getAsJsonArray("configurable_item_options");
        if (jsonArrayconfigurableItemOptions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("configurable_item_options").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `configurable_item_options` to be an array in the JSON string but got `%s`", jsonObj.get("configurable_item_options").toString()));
          }

          // validate the optional field `configurable_item_options` (array)
          for (int i = 0; i < jsonArrayconfigurableItemOptions.size(); i++) {
            ConfigurableProductDataConfigurableItemOptionValueInterface.validateJsonElement(jsonArrayconfigurableItemOptions.get(i));
          };
        }
      }
      if (jsonObj.get("custom_options") != null && !jsonObj.get("custom_options").isJsonNull()) {
        JsonArray jsonArraycustomOptions = jsonObj.getAsJsonArray("custom_options");
        if (jsonArraycustomOptions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_options").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_options` to be an array in the JSON string but got `%s`", jsonObj.get("custom_options").toString()));
          }

          // validate the optional field `custom_options` (array)
          for (int i = 0; i < jsonArraycustomOptions.size(); i++) {
            CatalogDataCustomOptionInterface.validateJsonElement(jsonArraycustomOptions.get(i));
          };
        }
      }
      // validate the optional field `downloadable_option`
      if (jsonObj.get("downloadable_option") != null && !jsonObj.get("downloadable_option").isJsonNull()) {
        DownloadableDataDownloadableOptionInterface.validateJsonElement(jsonObj.get("downloadable_option"));
      }
      // validate the optional field `giftcard_item_option`
      if (jsonObj.get("giftcard_item_option") != null && !jsonObj.get("giftcard_item_option").isJsonNull()) {
        GiftCardDataGiftCardOptionInterface.validateJsonElement(jsonObj.get("giftcard_item_option"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QuoteDataProductOptionExtensionInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QuoteDataProductOptionExtensionInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QuoteDataProductOptionExtensionInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QuoteDataProductOptionExtensionInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<QuoteDataProductOptionExtensionInterface>() {
           @Override
           public void write(JsonWriter out, QuoteDataProductOptionExtensionInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QuoteDataProductOptionExtensionInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QuoteDataProductOptionExtensionInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QuoteDataProductOptionExtensionInterface
   * @throws IOException if the JSON string is invalid with respect to QuoteDataProductOptionExtensionInterface
   */
  public static QuoteDataProductOptionExtensionInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QuoteDataProductOptionExtensionInterface.class);
  }

  /**
   * Convert an instance of QuoteDataProductOptionExtensionInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

