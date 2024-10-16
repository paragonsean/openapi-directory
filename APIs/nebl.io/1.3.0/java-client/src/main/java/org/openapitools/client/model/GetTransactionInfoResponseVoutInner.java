/*
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GetTransactionInfoResponseVinInnerPreviousOutput;
import org.openapitools.client.model.GetTransactionInfoResponseVinInnerTokensInner;

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
 * GetTransactionInfoResponseVoutInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:38.969239-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetTransactionInfoResponseVoutInner {
  public static final String SERIALIZED_NAME_BLOCKHEIGHT = "blockheight";
  @SerializedName(SERIALIZED_NAME_BLOCKHEIGHT)
  private BigDecimal blockheight;

  public static final String SERIALIZED_NAME_N = "n";
  @SerializedName(SERIALIZED_NAME_N)
  private BigDecimal n;

  public static final String SERIALIZED_NAME_SCRIPT_PUB_KEY = "scriptPubKey";
  @SerializedName(SERIALIZED_NAME_SCRIPT_PUB_KEY)
  private GetTransactionInfoResponseVinInnerPreviousOutput scriptPubKey;

  public static final String SERIALIZED_NAME_TOKENS = "tokens";
  @SerializedName(SERIALIZED_NAME_TOKENS)
  private List<GetTransactionInfoResponseVinInnerTokensInner> tokens = new ArrayList<>();

  public static final String SERIALIZED_NAME_USED = "used";
  @SerializedName(SERIALIZED_NAME_USED)
  private Boolean used;

  public static final String SERIALIZED_NAME_USED_BLOCKHEIGHT = "usedBlockheight";
  @SerializedName(SERIALIZED_NAME_USED_BLOCKHEIGHT)
  private BigDecimal usedBlockheight;

  public static final String SERIALIZED_NAME_USED_TXID = "usedTxid";
  @SerializedName(SERIALIZED_NAME_USED_TXID)
  private String usedTxid;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private BigDecimal value;

  public GetTransactionInfoResponseVoutInner() {
  }

  public GetTransactionInfoResponseVoutInner blockheight(BigDecimal blockheight) {
    this.blockheight = blockheight;
    return this;
  }

  /**
   * Blockheight of this transaction
   * @return blockheight
   */
  @javax.annotation.Nullable
  public BigDecimal getBlockheight() {
    return blockheight;
  }

  public void setBlockheight(BigDecimal blockheight) {
    this.blockheight = blockheight;
  }


  public GetTransactionInfoResponseVoutInner n(BigDecimal n) {
    this.n = n;
    return this;
  }

  /**
   * Output index
   * @return n
   */
  @javax.annotation.Nullable
  public BigDecimal getN() {
    return n;
  }

  public void setN(BigDecimal n) {
    this.n = n;
  }


  public GetTransactionInfoResponseVoutInner scriptPubKey(GetTransactionInfoResponseVinInnerPreviousOutput scriptPubKey) {
    this.scriptPubKey = scriptPubKey;
    return this;
  }

  /**
   * Get scriptPubKey
   * @return scriptPubKey
   */
  @javax.annotation.Nullable
  public GetTransactionInfoResponseVinInnerPreviousOutput getScriptPubKey() {
    return scriptPubKey;
  }

  public void setScriptPubKey(GetTransactionInfoResponseVinInnerPreviousOutput scriptPubKey) {
    this.scriptPubKey = scriptPubKey;
  }


  public GetTransactionInfoResponseVoutInner tokens(List<GetTransactionInfoResponseVinInnerTokensInner> tokens) {
    this.tokens = tokens;
    return this;
  }

  public GetTransactionInfoResponseVoutInner addTokensItem(GetTransactionInfoResponseVinInnerTokensInner tokensItem) {
    if (this.tokens == null) {
      this.tokens = new ArrayList<>();
    }
    this.tokens.add(tokensItem);
    return this;
  }

  /**
   * Get tokens
   * @return tokens
   */
  @javax.annotation.Nullable
  public List<GetTransactionInfoResponseVinInnerTokensInner> getTokens() {
    return tokens;
  }

  public void setTokens(List<GetTransactionInfoResponseVinInnerTokensInner> tokens) {
    this.tokens = tokens;
  }


  public GetTransactionInfoResponseVoutInner used(Boolean used) {
    this.used = used;
    return this;
  }

  /**
   * Whether this output has now been used
   * @return used
   */
  @javax.annotation.Nullable
  public Boolean getUsed() {
    return used;
  }

  public void setUsed(Boolean used) {
    this.used = used;
  }


  public GetTransactionInfoResponseVoutInner usedBlockheight(BigDecimal usedBlockheight) {
    this.usedBlockheight = usedBlockheight;
    return this;
  }

  /**
   * Blockheight this output was used in
   * @return usedBlockheight
   */
  @javax.annotation.Nullable
  public BigDecimal getUsedBlockheight() {
    return usedBlockheight;
  }

  public void setUsedBlockheight(BigDecimal usedBlockheight) {
    this.usedBlockheight = usedBlockheight;
  }


  public GetTransactionInfoResponseVoutInner usedTxid(String usedTxid) {
    this.usedTxid = usedTxid;
    return this;
  }

  /**
   * TXID this output was used in
   * @return usedTxid
   */
  @javax.annotation.Nullable
  public String getUsedTxid() {
    return usedTxid;
  }

  public void setUsedTxid(String usedTxid) {
    this.usedTxid = usedTxid;
  }


  public GetTransactionInfoResponseVoutInner value(BigDecimal value) {
    this.value = value;
    return this;
  }

  /**
   * Value of the output in NEBL satoshi
   * @return value
   */
  @javax.annotation.Nullable
  public BigDecimal getValue() {
    return value;
  }

  public void setValue(BigDecimal value) {
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
    GetTransactionInfoResponseVoutInner getTransactionInfoResponseVoutInner = (GetTransactionInfoResponseVoutInner) o;
    return Objects.equals(this.blockheight, getTransactionInfoResponseVoutInner.blockheight) &&
        Objects.equals(this.n, getTransactionInfoResponseVoutInner.n) &&
        Objects.equals(this.scriptPubKey, getTransactionInfoResponseVoutInner.scriptPubKey) &&
        Objects.equals(this.tokens, getTransactionInfoResponseVoutInner.tokens) &&
        Objects.equals(this.used, getTransactionInfoResponseVoutInner.used) &&
        Objects.equals(this.usedBlockheight, getTransactionInfoResponseVoutInner.usedBlockheight) &&
        Objects.equals(this.usedTxid, getTransactionInfoResponseVoutInner.usedTxid) &&
        Objects.equals(this.value, getTransactionInfoResponseVoutInner.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(blockheight, n, scriptPubKey, tokens, used, usedBlockheight, usedTxid, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetTransactionInfoResponseVoutInner {\n");
    sb.append("    blockheight: ").append(toIndentedString(blockheight)).append("\n");
    sb.append("    n: ").append(toIndentedString(n)).append("\n");
    sb.append("    scriptPubKey: ").append(toIndentedString(scriptPubKey)).append("\n");
    sb.append("    tokens: ").append(toIndentedString(tokens)).append("\n");
    sb.append("    used: ").append(toIndentedString(used)).append("\n");
    sb.append("    usedBlockheight: ").append(toIndentedString(usedBlockheight)).append("\n");
    sb.append("    usedTxid: ").append(toIndentedString(usedTxid)).append("\n");
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
    openapiFields.add("blockheight");
    openapiFields.add("n");
    openapiFields.add("scriptPubKey");
    openapiFields.add("tokens");
    openapiFields.add("used");
    openapiFields.add("usedBlockheight");
    openapiFields.add("usedTxid");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetTransactionInfoResponseVoutInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetTransactionInfoResponseVoutInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetTransactionInfoResponseVoutInner is not found in the empty JSON string", GetTransactionInfoResponseVoutInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetTransactionInfoResponseVoutInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetTransactionInfoResponseVoutInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `scriptPubKey`
      if (jsonObj.get("scriptPubKey") != null && !jsonObj.get("scriptPubKey").isJsonNull()) {
        GetTransactionInfoResponseVinInnerPreviousOutput.validateJsonElement(jsonObj.get("scriptPubKey"));
      }
      if (jsonObj.get("tokens") != null && !jsonObj.get("tokens").isJsonNull()) {
        JsonArray jsonArraytokens = jsonObj.getAsJsonArray("tokens");
        if (jsonArraytokens != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tokens").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tokens` to be an array in the JSON string but got `%s`", jsonObj.get("tokens").toString()));
          }

          // validate the optional field `tokens` (array)
          for (int i = 0; i < jsonArraytokens.size(); i++) {
            GetTransactionInfoResponseVinInnerTokensInner.validateJsonElement(jsonArraytokens.get(i));
          };
        }
      }
      if ((jsonObj.get("usedTxid") != null && !jsonObj.get("usedTxid").isJsonNull()) && !jsonObj.get("usedTxid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `usedTxid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("usedTxid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetTransactionInfoResponseVoutInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetTransactionInfoResponseVoutInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetTransactionInfoResponseVoutInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetTransactionInfoResponseVoutInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetTransactionInfoResponseVoutInner>() {
           @Override
           public void write(JsonWriter out, GetTransactionInfoResponseVoutInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetTransactionInfoResponseVoutInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetTransactionInfoResponseVoutInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetTransactionInfoResponseVoutInner
   * @throws IOException if the JSON string is invalid with respect to GetTransactionInfoResponseVoutInner
   */
  public static GetTransactionInfoResponseVoutInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetTransactionInfoResponseVoutInner.class);
  }

  /**
   * Convert an instance of GetTransactionInfoResponseVoutInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

