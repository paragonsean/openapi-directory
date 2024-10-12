/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
 * Azure Files or Blob Storage access information value for dictionary storage.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:50.309367-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue {
  public static final String SERIALIZED_NAME_ACCESS_KEY = "accessKey";
  @SerializedName(SERIALIZED_NAME_ACCESS_KEY)
  private String accessKey;

  public static final String SERIALIZED_NAME_ACCOUNT_NAME = "accountName";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NAME)
  private String accountName;

  public static final String SERIALIZED_NAME_MOUNT_PATH = "mountPath";
  @SerializedName(SERIALIZED_NAME_MOUNT_PATH)
  private String mountPath;

  public static final String SERIALIZED_NAME_SHARE_NAME = "shareName";
  @SerializedName(SERIALIZED_NAME_SHARE_NAME)
  private String shareName;

  /**
   * State of the storage account.
   */
  @JsonAdapter(StateEnum.Adapter.class)
  public enum StateEnum {
    OK("Ok"),
    
    INVALID_CREDENTIALS("InvalidCredentials"),
    
    INVALID_SHARE("InvalidShare");

    private String value;

    StateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StateEnum fromValue(String value) {
      for (StateEnum b : StateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private StateEnum state;

  /**
   * Type of storage.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    AZURE_FILES("AzureFiles"),
    
    AZURE_BLOB("AzureBlob");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue() {
  }

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue(
     StateEnum state
  ) {
    this();
    this.state = state;
  }

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue accessKey(String accessKey) {
    this.accessKey = accessKey;
    return this;
  }

  /**
   * Access key for the storage account.
   * @return accessKey
   */
  @javax.annotation.Nullable
  public String getAccessKey() {
    return accessKey;
  }

  public void setAccessKey(String accessKey) {
    this.accessKey = accessKey;
  }


  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue accountName(String accountName) {
    this.accountName = accountName;
    return this;
  }

  /**
   * Name of the storage account.
   * @return accountName
   */
  @javax.annotation.Nullable
  public String getAccountName() {
    return accountName;
  }

  public void setAccountName(String accountName) {
    this.accountName = accountName;
  }


  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue mountPath(String mountPath) {
    this.mountPath = mountPath;
    return this;
  }

  /**
   * Path to mount the storage within the site&#39;s runtime environment.
   * @return mountPath
   */
  @javax.annotation.Nullable
  public String getMountPath() {
    return mountPath;
  }

  public void setMountPath(String mountPath) {
    this.mountPath = mountPath;
  }


  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue shareName(String shareName) {
    this.shareName = shareName;
    return this;
  }

  /**
   * Name of the file share (container name, for Blob storage).
   * @return shareName
   */
  @javax.annotation.Nullable
  public String getShareName() {
    return shareName;
  }

  public void setShareName(String shareName) {
    this.shareName = shareName;
  }


  /**
   * State of the storage account.
   * @return state
   */
  @javax.annotation.Nullable
  public StateEnum getState() {
    return state;
  }



  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Type of storage.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue = (AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue) o;
    return Objects.equals(this.accessKey, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.accessKey) &&
        Objects.equals(this.accountName, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.accountName) &&
        Objects.equals(this.mountPath, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.mountPath) &&
        Objects.equals(this.shareName, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.shareName) &&
        Objects.equals(this.state, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.state) &&
        Objects.equals(this.type, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accessKey, accountName, mountPath, shareName, state, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue {\n");
    sb.append("    accessKey: ").append(toIndentedString(accessKey)).append("\n");
    sb.append("    accountName: ").append(toIndentedString(accountName)).append("\n");
    sb.append("    mountPath: ").append(toIndentedString(mountPath)).append("\n");
    sb.append("    shareName: ").append(toIndentedString(shareName)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("accessKey");
    openapiFields.add("accountName");
    openapiFields.add("mountPath");
    openapiFields.add("shareName");
    openapiFields.add("state");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue is not found in the empty JSON string", AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("accessKey") != null && !jsonObj.get("accessKey").isJsonNull()) && !jsonObj.get("accessKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accessKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accessKey").toString()));
      }
      if ((jsonObj.get("accountName") != null && !jsonObj.get("accountName").isJsonNull()) && !jsonObj.get("accountName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountName").toString()));
      }
      if ((jsonObj.get("mountPath") != null && !jsonObj.get("mountPath").isJsonNull()) && !jsonObj.get("mountPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mountPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mountPath").toString()));
      }
      if ((jsonObj.get("shareName") != null && !jsonObj.get("shareName").isJsonNull()) && !jsonObj.get("shareName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shareName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shareName").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        StateEnum.validateJsonElement(jsonObj.get("state"));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue>() {
           @Override
           public void write(JsonWriter out, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue
   */
  public static AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue.class);
  }

  /**
   * Convert an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

