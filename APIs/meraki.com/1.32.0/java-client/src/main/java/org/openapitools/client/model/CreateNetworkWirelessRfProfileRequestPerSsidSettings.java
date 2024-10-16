/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings0;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings1;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings10;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings11;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings12;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings13;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings14;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings2;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings3;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings4;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings5;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings6;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings7;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings8;
import org.openapitools.client.model.CreateNetworkWirelessRfProfileRequestPerSsidSettings9;

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
 * Per-SSID radio settings by number.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateNetworkWirelessRfProfileRequestPerSsidSettings {
  public static final String SERIALIZED_NAME_0 = "0";
  @SerializedName(SERIALIZED_NAME_0)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings0 _0;

  public static final String SERIALIZED_NAME_1 = "1";
  @SerializedName(SERIALIZED_NAME_1)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings1 _1;

  public static final String SERIALIZED_NAME_2 = "2";
  @SerializedName(SERIALIZED_NAME_2)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings2 _2;

  public static final String SERIALIZED_NAME_3 = "3";
  @SerializedName(SERIALIZED_NAME_3)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings3 _3;

  public static final String SERIALIZED_NAME_4 = "4";
  @SerializedName(SERIALIZED_NAME_4)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings4 _4;

  public static final String SERIALIZED_NAME_5 = "5";
  @SerializedName(SERIALIZED_NAME_5)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings5 _5;

  public static final String SERIALIZED_NAME_6 = "6";
  @SerializedName(SERIALIZED_NAME_6)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings6 _6;

  public static final String SERIALIZED_NAME_7 = "7";
  @SerializedName(SERIALIZED_NAME_7)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings7 _7;

  public static final String SERIALIZED_NAME_8 = "8";
  @SerializedName(SERIALIZED_NAME_8)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings8 _8;

  public static final String SERIALIZED_NAME_9 = "9";
  @SerializedName(SERIALIZED_NAME_9)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings9 _9;

  public static final String SERIALIZED_NAME_10 = "10";
  @SerializedName(SERIALIZED_NAME_10)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings10 _10;

  public static final String SERIALIZED_NAME_11 = "11";
  @SerializedName(SERIALIZED_NAME_11)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings11 _11;

  public static final String SERIALIZED_NAME_12 = "12";
  @SerializedName(SERIALIZED_NAME_12)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings12 _12;

  public static final String SERIALIZED_NAME_13 = "13";
  @SerializedName(SERIALIZED_NAME_13)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings13 _13;

  public static final String SERIALIZED_NAME_14 = "14";
  @SerializedName(SERIALIZED_NAME_14)
  private CreateNetworkWirelessRfProfileRequestPerSsidSettings14 _14;

  public CreateNetworkWirelessRfProfileRequestPerSsidSettings() {
  }

  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _0(CreateNetworkWirelessRfProfileRequestPerSsidSettings0 _0) {
    this._0 = _0;
    return this;
  }

  /**
   * Get _0
   * @return _0
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings0 get0() {
    return _0;
  }

  public void set0(CreateNetworkWirelessRfProfileRequestPerSsidSettings0 _0) {
    this._0 = _0;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _1(CreateNetworkWirelessRfProfileRequestPerSsidSettings1 _1) {
    this._1 = _1;
    return this;
  }

  /**
   * Get _1
   * @return _1
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings1 get1() {
    return _1;
  }

  public void set1(CreateNetworkWirelessRfProfileRequestPerSsidSettings1 _1) {
    this._1 = _1;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _2(CreateNetworkWirelessRfProfileRequestPerSsidSettings2 _2) {
    this._2 = _2;
    return this;
  }

  /**
   * Get _2
   * @return _2
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings2 get2() {
    return _2;
  }

  public void set2(CreateNetworkWirelessRfProfileRequestPerSsidSettings2 _2) {
    this._2 = _2;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _3(CreateNetworkWirelessRfProfileRequestPerSsidSettings3 _3) {
    this._3 = _3;
    return this;
  }

  /**
   * Get _3
   * @return _3
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings3 get3() {
    return _3;
  }

  public void set3(CreateNetworkWirelessRfProfileRequestPerSsidSettings3 _3) {
    this._3 = _3;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _4(CreateNetworkWirelessRfProfileRequestPerSsidSettings4 _4) {
    this._4 = _4;
    return this;
  }

  /**
   * Get _4
   * @return _4
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings4 get4() {
    return _4;
  }

  public void set4(CreateNetworkWirelessRfProfileRequestPerSsidSettings4 _4) {
    this._4 = _4;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _5(CreateNetworkWirelessRfProfileRequestPerSsidSettings5 _5) {
    this._5 = _5;
    return this;
  }

  /**
   * Get _5
   * @return _5
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings5 get5() {
    return _5;
  }

  public void set5(CreateNetworkWirelessRfProfileRequestPerSsidSettings5 _5) {
    this._5 = _5;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _6(CreateNetworkWirelessRfProfileRequestPerSsidSettings6 _6) {
    this._6 = _6;
    return this;
  }

  /**
   * Get _6
   * @return _6
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings6 get6() {
    return _6;
  }

  public void set6(CreateNetworkWirelessRfProfileRequestPerSsidSettings6 _6) {
    this._6 = _6;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _7(CreateNetworkWirelessRfProfileRequestPerSsidSettings7 _7) {
    this._7 = _7;
    return this;
  }

  /**
   * Get _7
   * @return _7
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings7 get7() {
    return _7;
  }

  public void set7(CreateNetworkWirelessRfProfileRequestPerSsidSettings7 _7) {
    this._7 = _7;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _8(CreateNetworkWirelessRfProfileRequestPerSsidSettings8 _8) {
    this._8 = _8;
    return this;
  }

  /**
   * Get _8
   * @return _8
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings8 get8() {
    return _8;
  }

  public void set8(CreateNetworkWirelessRfProfileRequestPerSsidSettings8 _8) {
    this._8 = _8;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _9(CreateNetworkWirelessRfProfileRequestPerSsidSettings9 _9) {
    this._9 = _9;
    return this;
  }

  /**
   * Get _9
   * @return _9
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings9 get9() {
    return _9;
  }

  public void set9(CreateNetworkWirelessRfProfileRequestPerSsidSettings9 _9) {
    this._9 = _9;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _10(CreateNetworkWirelessRfProfileRequestPerSsidSettings10 _10) {
    this._10 = _10;
    return this;
  }

  /**
   * Get _10
   * @return _10
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings10 get10() {
    return _10;
  }

  public void set10(CreateNetworkWirelessRfProfileRequestPerSsidSettings10 _10) {
    this._10 = _10;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _11(CreateNetworkWirelessRfProfileRequestPerSsidSettings11 _11) {
    this._11 = _11;
    return this;
  }

  /**
   * Get _11
   * @return _11
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings11 get11() {
    return _11;
  }

  public void set11(CreateNetworkWirelessRfProfileRequestPerSsidSettings11 _11) {
    this._11 = _11;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _12(CreateNetworkWirelessRfProfileRequestPerSsidSettings12 _12) {
    this._12 = _12;
    return this;
  }

  /**
   * Get _12
   * @return _12
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings12 get12() {
    return _12;
  }

  public void set12(CreateNetworkWirelessRfProfileRequestPerSsidSettings12 _12) {
    this._12 = _12;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _13(CreateNetworkWirelessRfProfileRequestPerSsidSettings13 _13) {
    this._13 = _13;
    return this;
  }

  /**
   * Get _13
   * @return _13
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings13 get13() {
    return _13;
  }

  public void set13(CreateNetworkWirelessRfProfileRequestPerSsidSettings13 _13) {
    this._13 = _13;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings _14(CreateNetworkWirelessRfProfileRequestPerSsidSettings14 _14) {
    this._14 = _14;
    return this;
  }

  /**
   * Get _14
   * @return _14
   */
  @javax.annotation.Nullable
  public CreateNetworkWirelessRfProfileRequestPerSsidSettings14 get14() {
    return _14;
  }

  public void set14(CreateNetworkWirelessRfProfileRequestPerSsidSettings14 _14) {
    this._14 = _14;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateNetworkWirelessRfProfileRequestPerSsidSettings createNetworkWirelessRfProfileRequestPerSsidSettings = (CreateNetworkWirelessRfProfileRequestPerSsidSettings) o;
    return Objects.equals(this._0, createNetworkWirelessRfProfileRequestPerSsidSettings._0) &&
        Objects.equals(this._1, createNetworkWirelessRfProfileRequestPerSsidSettings._1) &&
        Objects.equals(this._2, createNetworkWirelessRfProfileRequestPerSsidSettings._2) &&
        Objects.equals(this._3, createNetworkWirelessRfProfileRequestPerSsidSettings._3) &&
        Objects.equals(this._4, createNetworkWirelessRfProfileRequestPerSsidSettings._4) &&
        Objects.equals(this._5, createNetworkWirelessRfProfileRequestPerSsidSettings._5) &&
        Objects.equals(this._6, createNetworkWirelessRfProfileRequestPerSsidSettings._6) &&
        Objects.equals(this._7, createNetworkWirelessRfProfileRequestPerSsidSettings._7) &&
        Objects.equals(this._8, createNetworkWirelessRfProfileRequestPerSsidSettings._8) &&
        Objects.equals(this._9, createNetworkWirelessRfProfileRequestPerSsidSettings._9) &&
        Objects.equals(this._10, createNetworkWirelessRfProfileRequestPerSsidSettings._10) &&
        Objects.equals(this._11, createNetworkWirelessRfProfileRequestPerSsidSettings._11) &&
        Objects.equals(this._12, createNetworkWirelessRfProfileRequestPerSsidSettings._12) &&
        Objects.equals(this._13, createNetworkWirelessRfProfileRequestPerSsidSettings._13) &&
        Objects.equals(this._14, createNetworkWirelessRfProfileRequestPerSsidSettings._14);
  }

  @Override
  public int hashCode() {
    return Objects.hash(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateNetworkWirelessRfProfileRequestPerSsidSettings {\n");
    sb.append("    _0: ").append(toIndentedString(_0)).append("\n");
    sb.append("    _1: ").append(toIndentedString(_1)).append("\n");
    sb.append("    _2: ").append(toIndentedString(_2)).append("\n");
    sb.append("    _3: ").append(toIndentedString(_3)).append("\n");
    sb.append("    _4: ").append(toIndentedString(_4)).append("\n");
    sb.append("    _5: ").append(toIndentedString(_5)).append("\n");
    sb.append("    _6: ").append(toIndentedString(_6)).append("\n");
    sb.append("    _7: ").append(toIndentedString(_7)).append("\n");
    sb.append("    _8: ").append(toIndentedString(_8)).append("\n");
    sb.append("    _9: ").append(toIndentedString(_9)).append("\n");
    sb.append("    _10: ").append(toIndentedString(_10)).append("\n");
    sb.append("    _11: ").append(toIndentedString(_11)).append("\n");
    sb.append("    _12: ").append(toIndentedString(_12)).append("\n");
    sb.append("    _13: ").append(toIndentedString(_13)).append("\n");
    sb.append("    _14: ").append(toIndentedString(_14)).append("\n");
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
    openapiFields.add("0");
    openapiFields.add("1");
    openapiFields.add("2");
    openapiFields.add("3");
    openapiFields.add("4");
    openapiFields.add("5");
    openapiFields.add("6");
    openapiFields.add("7");
    openapiFields.add("8");
    openapiFields.add("9");
    openapiFields.add("10");
    openapiFields.add("11");
    openapiFields.add("12");
    openapiFields.add("13");
    openapiFields.add("14");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateNetworkWirelessRfProfileRequestPerSsidSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateNetworkWirelessRfProfileRequestPerSsidSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateNetworkWirelessRfProfileRequestPerSsidSettings is not found in the empty JSON string", CreateNetworkWirelessRfProfileRequestPerSsidSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateNetworkWirelessRfProfileRequestPerSsidSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateNetworkWirelessRfProfileRequestPerSsidSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `0`
      if (jsonObj.get("0") != null && !jsonObj.get("0").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings0.validateJsonElement(jsonObj.get("0"));
      }
      // validate the optional field `1`
      if (jsonObj.get("1") != null && !jsonObj.get("1").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings1.validateJsonElement(jsonObj.get("1"));
      }
      // validate the optional field `2`
      if (jsonObj.get("2") != null && !jsonObj.get("2").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings2.validateJsonElement(jsonObj.get("2"));
      }
      // validate the optional field `3`
      if (jsonObj.get("3") != null && !jsonObj.get("3").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings3.validateJsonElement(jsonObj.get("3"));
      }
      // validate the optional field `4`
      if (jsonObj.get("4") != null && !jsonObj.get("4").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings4.validateJsonElement(jsonObj.get("4"));
      }
      // validate the optional field `5`
      if (jsonObj.get("5") != null && !jsonObj.get("5").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings5.validateJsonElement(jsonObj.get("5"));
      }
      // validate the optional field `6`
      if (jsonObj.get("6") != null && !jsonObj.get("6").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings6.validateJsonElement(jsonObj.get("6"));
      }
      // validate the optional field `7`
      if (jsonObj.get("7") != null && !jsonObj.get("7").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings7.validateJsonElement(jsonObj.get("7"));
      }
      // validate the optional field `8`
      if (jsonObj.get("8") != null && !jsonObj.get("8").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings8.validateJsonElement(jsonObj.get("8"));
      }
      // validate the optional field `9`
      if (jsonObj.get("9") != null && !jsonObj.get("9").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings9.validateJsonElement(jsonObj.get("9"));
      }
      // validate the optional field `10`
      if (jsonObj.get("10") != null && !jsonObj.get("10").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings10.validateJsonElement(jsonObj.get("10"));
      }
      // validate the optional field `11`
      if (jsonObj.get("11") != null && !jsonObj.get("11").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings11.validateJsonElement(jsonObj.get("11"));
      }
      // validate the optional field `12`
      if (jsonObj.get("12") != null && !jsonObj.get("12").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings12.validateJsonElement(jsonObj.get("12"));
      }
      // validate the optional field `13`
      if (jsonObj.get("13") != null && !jsonObj.get("13").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings13.validateJsonElement(jsonObj.get("13"));
      }
      // validate the optional field `14`
      if (jsonObj.get("14") != null && !jsonObj.get("14").isJsonNull()) {
        CreateNetworkWirelessRfProfileRequestPerSsidSettings14.validateJsonElement(jsonObj.get("14"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateNetworkWirelessRfProfileRequestPerSsidSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateNetworkWirelessRfProfileRequestPerSsidSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateNetworkWirelessRfProfileRequestPerSsidSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateNetworkWirelessRfProfileRequestPerSsidSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateNetworkWirelessRfProfileRequestPerSsidSettings>() {
           @Override
           public void write(JsonWriter out, CreateNetworkWirelessRfProfileRequestPerSsidSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateNetworkWirelessRfProfileRequestPerSsidSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateNetworkWirelessRfProfileRequestPerSsidSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateNetworkWirelessRfProfileRequestPerSsidSettings
   * @throws IOException if the JSON string is invalid with respect to CreateNetworkWirelessRfProfileRequestPerSsidSettings
   */
  public static CreateNetworkWirelessRfProfileRequestPerSsidSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateNetworkWirelessRfProfileRequestPerSsidSettings.class);
  }

  /**
   * Convert an instance of CreateNetworkWirelessRfProfileRequestPerSsidSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

