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
import java.util.Arrays;
import org.openapitools.client.model.GetTokenMetadataResponseMetadataOfIssuance;
import org.openapitools.client.model.GetTokenMetadataResponseMetadataOfUtxo;

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
 * GetTokenMetadataResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:38.969239-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetTokenMetadataResponse {
  public static final String SERIALIZED_NAME_AGGREGATION_POLICY = "aggregationPolicy";
  @SerializedName(SERIALIZED_NAME_AGGREGATION_POLICY)
  private String aggregationPolicy;

  public static final String SERIALIZED_NAME_DIVISIBILITY = "divisibility";
  @SerializedName(SERIALIZED_NAME_DIVISIBILITY)
  private BigDecimal divisibility;

  public static final String SERIALIZED_NAME_FIRST_BLOCK = "firstBlock";
  @SerializedName(SERIALIZED_NAME_FIRST_BLOCK)
  private BigDecimal firstBlock;

  public static final String SERIALIZED_NAME_INITIAL_ISSUANCE_AMOUNT = "initialIssuanceAmount";
  @SerializedName(SERIALIZED_NAME_INITIAL_ISSUANCE_AMOUNT)
  private BigDecimal initialIssuanceAmount;

  public static final String SERIALIZED_NAME_ISSUANCE_TXID = "issuanceTxid";
  @SerializedName(SERIALIZED_NAME_ISSUANCE_TXID)
  private String issuanceTxid;

  public static final String SERIALIZED_NAME_ISSUE_ADDRESS = "issueAddress";
  @SerializedName(SERIALIZED_NAME_ISSUE_ADDRESS)
  private String issueAddress;

  public static final String SERIALIZED_NAME_LOCK_STATUS = "lockStatus";
  @SerializedName(SERIALIZED_NAME_LOCK_STATUS)
  private Boolean lockStatus;

  public static final String SERIALIZED_NAME_METADATA_OF_ISSUANCE = "metadataOfIssuance";
  @SerializedName(SERIALIZED_NAME_METADATA_OF_ISSUANCE)
  private GetTokenMetadataResponseMetadataOfIssuance metadataOfIssuance;

  public static final String SERIALIZED_NAME_METADATA_OF_UTXO = "metadataOfUtxo";
  @SerializedName(SERIALIZED_NAME_METADATA_OF_UTXO)
  private GetTokenMetadataResponseMetadataOfUtxo metadataOfUtxo;

  public static final String SERIALIZED_NAME_NUM_OF_BURNS = "numOfBurns";
  @SerializedName(SERIALIZED_NAME_NUM_OF_BURNS)
  private BigDecimal numOfBurns;

  public static final String SERIALIZED_NAME_NUM_OF_HOLDERS = "numOfHolders";
  @SerializedName(SERIALIZED_NAME_NUM_OF_HOLDERS)
  private BigDecimal numOfHolders;

  public static final String SERIALIZED_NAME_NUM_OF_ISSUANCE = "numOfIssuance";
  @SerializedName(SERIALIZED_NAME_NUM_OF_ISSUANCE)
  private BigDecimal numOfIssuance;

  public static final String SERIALIZED_NAME_NUM_OF_TRANSFERS = "numOfTransfers";
  @SerializedName(SERIALIZED_NAME_NUM_OF_TRANSFERS)
  private BigDecimal numOfTransfers;

  public static final String SERIALIZED_NAME_SOME_UTXO = "someUtxo";
  @SerializedName(SERIALIZED_NAME_SOME_UTXO)
  private String someUtxo;

  public static final String SERIALIZED_NAME_TOKEN_ID = "tokenId";
  @SerializedName(SERIALIZED_NAME_TOKEN_ID)
  private String tokenId;

  public static final String SERIALIZED_NAME_TOTAL_SUPPLY = "totalSupply";
  @SerializedName(SERIALIZED_NAME_TOTAL_SUPPLY)
  private BigDecimal totalSupply;

  public GetTokenMetadataResponse() {
  }

  public GetTokenMetadataResponse aggregationPolicy(String aggregationPolicy) {
    this.aggregationPolicy = aggregationPolicy;
    return this;
  }

  /**
   * Whether the tokens are aggregatable
   * @return aggregationPolicy
   */
  @javax.annotation.Nullable
  public String getAggregationPolicy() {
    return aggregationPolicy;
  }

  public void setAggregationPolicy(String aggregationPolicy) {
    this.aggregationPolicy = aggregationPolicy;
  }


  public GetTokenMetadataResponse divisibility(BigDecimal divisibility) {
    this.divisibility = divisibility;
    return this;
  }

  /**
   * Decimal places the token is divisible to
   * @return divisibility
   */
  @javax.annotation.Nullable
  public BigDecimal getDivisibility() {
    return divisibility;
  }

  public void setDivisibility(BigDecimal divisibility) {
    this.divisibility = divisibility;
  }


  public GetTokenMetadataResponse firstBlock(BigDecimal firstBlock) {
    this.firstBlock = firstBlock;
    return this;
  }

  /**
   * Block number token was issued in
   * @return firstBlock
   */
  @javax.annotation.Nullable
  public BigDecimal getFirstBlock() {
    return firstBlock;
  }

  public void setFirstBlock(BigDecimal firstBlock) {
    this.firstBlock = firstBlock;
  }


  public GetTokenMetadataResponse initialIssuanceAmount(BigDecimal initialIssuanceAmount) {
    this.initialIssuanceAmount = initialIssuanceAmount;
    return this;
  }

  /**
   * Total tokens issued in initial issuance
   * @return initialIssuanceAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getInitialIssuanceAmount() {
    return initialIssuanceAmount;
  }

  public void setInitialIssuanceAmount(BigDecimal initialIssuanceAmount) {
    this.initialIssuanceAmount = initialIssuanceAmount;
  }


  public GetTokenMetadataResponse issuanceTxid(String issuanceTxid) {
    this.issuanceTxid = issuanceTxid;
    return this;
  }

  /**
   * TXID the token was issued with
   * @return issuanceTxid
   */
  @javax.annotation.Nullable
  public String getIssuanceTxid() {
    return issuanceTxid;
  }

  public void setIssuanceTxid(String issuanceTxid) {
    this.issuanceTxid = issuanceTxid;
  }


  public GetTokenMetadataResponse issueAddress(String issueAddress) {
    this.issueAddress = issueAddress;
    return this;
  }

  /**
   * Address that issued the tokens
   * @return issueAddress
   */
  @javax.annotation.Nullable
  public String getIssueAddress() {
    return issueAddress;
  }

  public void setIssueAddress(String issueAddress) {
    this.issueAddress = issueAddress;
  }


  public GetTokenMetadataResponse lockStatus(Boolean lockStatus) {
    this.lockStatus = lockStatus;
    return this;
  }

  /**
   * Whether issuance of more tokens is locked
   * @return lockStatus
   */
  @javax.annotation.Nullable
  public Boolean getLockStatus() {
    return lockStatus;
  }

  public void setLockStatus(Boolean lockStatus) {
    this.lockStatus = lockStatus;
  }


  public GetTokenMetadataResponse metadataOfIssuance(GetTokenMetadataResponseMetadataOfIssuance metadataOfIssuance) {
    this.metadataOfIssuance = metadataOfIssuance;
    return this;
  }

  /**
   * Get metadataOfIssuance
   * @return metadataOfIssuance
   */
  @javax.annotation.Nullable
  public GetTokenMetadataResponseMetadataOfIssuance getMetadataOfIssuance() {
    return metadataOfIssuance;
  }

  public void setMetadataOfIssuance(GetTokenMetadataResponseMetadataOfIssuance metadataOfIssuance) {
    this.metadataOfIssuance = metadataOfIssuance;
  }


  public GetTokenMetadataResponse metadataOfUtxo(GetTokenMetadataResponseMetadataOfUtxo metadataOfUtxo) {
    this.metadataOfUtxo = metadataOfUtxo;
    return this;
  }

  /**
   * Get metadataOfUtxo
   * @return metadataOfUtxo
   */
  @javax.annotation.Nullable
  public GetTokenMetadataResponseMetadataOfUtxo getMetadataOfUtxo() {
    return metadataOfUtxo;
  }

  public void setMetadataOfUtxo(GetTokenMetadataResponseMetadataOfUtxo metadataOfUtxo) {
    this.metadataOfUtxo = metadataOfUtxo;
  }


  public GetTokenMetadataResponse numOfBurns(BigDecimal numOfBurns) {
    this.numOfBurns = numOfBurns;
    return this;
  }

  /**
   * Number of times tokens have been burned
   * @return numOfBurns
   */
  @javax.annotation.Nullable
  public BigDecimal getNumOfBurns() {
    return numOfBurns;
  }

  public void setNumOfBurns(BigDecimal numOfBurns) {
    this.numOfBurns = numOfBurns;
  }


  public GetTokenMetadataResponse numOfHolders(BigDecimal numOfHolders) {
    this.numOfHolders = numOfHolders;
    return this;
  }

  /**
   * Total number of addresses this token is held at
   * @return numOfHolders
   */
  @javax.annotation.Nullable
  public BigDecimal getNumOfHolders() {
    return numOfHolders;
  }

  public void setNumOfHolders(BigDecimal numOfHolders) {
    this.numOfHolders = numOfHolders;
  }


  public GetTokenMetadataResponse numOfIssuance(BigDecimal numOfIssuance) {
    this.numOfIssuance = numOfIssuance;
    return this;
  }

  /**
   * Total number of times this token has been issued
   * @return numOfIssuance
   */
  @javax.annotation.Nullable
  public BigDecimal getNumOfIssuance() {
    return numOfIssuance;
  }

  public void setNumOfIssuance(BigDecimal numOfIssuance) {
    this.numOfIssuance = numOfIssuance;
  }


  public GetTokenMetadataResponse numOfTransfers(BigDecimal numOfTransfers) {
    this.numOfTransfers = numOfTransfers;
    return this;
  }

  /**
   * Total number of transactions of this token
   * @return numOfTransfers
   */
  @javax.annotation.Nullable
  public BigDecimal getNumOfTransfers() {
    return numOfTransfers;
  }

  public void setNumOfTransfers(BigDecimal numOfTransfers) {
    this.numOfTransfers = numOfTransfers;
  }


  public GetTokenMetadataResponse someUtxo(String someUtxo) {
    this.someUtxo = someUtxo;
    return this;
  }

  /**
   * Example UTXO containing this token.
   * @return someUtxo
   */
  @javax.annotation.Nullable
  public String getSomeUtxo() {
    return someUtxo;
  }

  public void setSomeUtxo(String someUtxo) {
    this.someUtxo = someUtxo;
  }


  public GetTokenMetadataResponse tokenId(String tokenId) {
    this.tokenId = tokenId;
    return this;
  }

  /**
   * ID of the token
   * @return tokenId
   */
  @javax.annotation.Nullable
  public String getTokenId() {
    return tokenId;
  }

  public void setTokenId(String tokenId) {
    this.tokenId = tokenId;
  }


  public GetTokenMetadataResponse totalSupply(BigDecimal totalSupply) {
    this.totalSupply = totalSupply;
    return this;
  }

  /**
   * Total number of tokens in supply
   * @return totalSupply
   */
  @javax.annotation.Nullable
  public BigDecimal getTotalSupply() {
    return totalSupply;
  }

  public void setTotalSupply(BigDecimal totalSupply) {
    this.totalSupply = totalSupply;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetTokenMetadataResponse getTokenMetadataResponse = (GetTokenMetadataResponse) o;
    return Objects.equals(this.aggregationPolicy, getTokenMetadataResponse.aggregationPolicy) &&
        Objects.equals(this.divisibility, getTokenMetadataResponse.divisibility) &&
        Objects.equals(this.firstBlock, getTokenMetadataResponse.firstBlock) &&
        Objects.equals(this.initialIssuanceAmount, getTokenMetadataResponse.initialIssuanceAmount) &&
        Objects.equals(this.issuanceTxid, getTokenMetadataResponse.issuanceTxid) &&
        Objects.equals(this.issueAddress, getTokenMetadataResponse.issueAddress) &&
        Objects.equals(this.lockStatus, getTokenMetadataResponse.lockStatus) &&
        Objects.equals(this.metadataOfIssuance, getTokenMetadataResponse.metadataOfIssuance) &&
        Objects.equals(this.metadataOfUtxo, getTokenMetadataResponse.metadataOfUtxo) &&
        Objects.equals(this.numOfBurns, getTokenMetadataResponse.numOfBurns) &&
        Objects.equals(this.numOfHolders, getTokenMetadataResponse.numOfHolders) &&
        Objects.equals(this.numOfIssuance, getTokenMetadataResponse.numOfIssuance) &&
        Objects.equals(this.numOfTransfers, getTokenMetadataResponse.numOfTransfers) &&
        Objects.equals(this.someUtxo, getTokenMetadataResponse.someUtxo) &&
        Objects.equals(this.tokenId, getTokenMetadataResponse.tokenId) &&
        Objects.equals(this.totalSupply, getTokenMetadataResponse.totalSupply);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aggregationPolicy, divisibility, firstBlock, initialIssuanceAmount, issuanceTxid, issueAddress, lockStatus, metadataOfIssuance, metadataOfUtxo, numOfBurns, numOfHolders, numOfIssuance, numOfTransfers, someUtxo, tokenId, totalSupply);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetTokenMetadataResponse {\n");
    sb.append("    aggregationPolicy: ").append(toIndentedString(aggregationPolicy)).append("\n");
    sb.append("    divisibility: ").append(toIndentedString(divisibility)).append("\n");
    sb.append("    firstBlock: ").append(toIndentedString(firstBlock)).append("\n");
    sb.append("    initialIssuanceAmount: ").append(toIndentedString(initialIssuanceAmount)).append("\n");
    sb.append("    issuanceTxid: ").append(toIndentedString(issuanceTxid)).append("\n");
    sb.append("    issueAddress: ").append(toIndentedString(issueAddress)).append("\n");
    sb.append("    lockStatus: ").append(toIndentedString(lockStatus)).append("\n");
    sb.append("    metadataOfIssuance: ").append(toIndentedString(metadataOfIssuance)).append("\n");
    sb.append("    metadataOfUtxo: ").append(toIndentedString(metadataOfUtxo)).append("\n");
    sb.append("    numOfBurns: ").append(toIndentedString(numOfBurns)).append("\n");
    sb.append("    numOfHolders: ").append(toIndentedString(numOfHolders)).append("\n");
    sb.append("    numOfIssuance: ").append(toIndentedString(numOfIssuance)).append("\n");
    sb.append("    numOfTransfers: ").append(toIndentedString(numOfTransfers)).append("\n");
    sb.append("    someUtxo: ").append(toIndentedString(someUtxo)).append("\n");
    sb.append("    tokenId: ").append(toIndentedString(tokenId)).append("\n");
    sb.append("    totalSupply: ").append(toIndentedString(totalSupply)).append("\n");
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
    openapiFields.add("aggregationPolicy");
    openapiFields.add("divisibility");
    openapiFields.add("firstBlock");
    openapiFields.add("initialIssuanceAmount");
    openapiFields.add("issuanceTxid");
    openapiFields.add("issueAddress");
    openapiFields.add("lockStatus");
    openapiFields.add("metadataOfIssuance");
    openapiFields.add("metadataOfUtxo");
    openapiFields.add("numOfBurns");
    openapiFields.add("numOfHolders");
    openapiFields.add("numOfIssuance");
    openapiFields.add("numOfTransfers");
    openapiFields.add("someUtxo");
    openapiFields.add("tokenId");
    openapiFields.add("totalSupply");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetTokenMetadataResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetTokenMetadataResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetTokenMetadataResponse is not found in the empty JSON string", GetTokenMetadataResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetTokenMetadataResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetTokenMetadataResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("aggregationPolicy") != null && !jsonObj.get("aggregationPolicy").isJsonNull()) && !jsonObj.get("aggregationPolicy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `aggregationPolicy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("aggregationPolicy").toString()));
      }
      if ((jsonObj.get("issuanceTxid") != null && !jsonObj.get("issuanceTxid").isJsonNull()) && !jsonObj.get("issuanceTxid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issuanceTxid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issuanceTxid").toString()));
      }
      if ((jsonObj.get("issueAddress") != null && !jsonObj.get("issueAddress").isJsonNull()) && !jsonObj.get("issueAddress").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `issueAddress` to be a primitive type in the JSON string but got `%s`", jsonObj.get("issueAddress").toString()));
      }
      // validate the optional field `metadataOfIssuance`
      if (jsonObj.get("metadataOfIssuance") != null && !jsonObj.get("metadataOfIssuance").isJsonNull()) {
        GetTokenMetadataResponseMetadataOfIssuance.validateJsonElement(jsonObj.get("metadataOfIssuance"));
      }
      // validate the optional field `metadataOfUtxo`
      if (jsonObj.get("metadataOfUtxo") != null && !jsonObj.get("metadataOfUtxo").isJsonNull()) {
        GetTokenMetadataResponseMetadataOfUtxo.validateJsonElement(jsonObj.get("metadataOfUtxo"));
      }
      if ((jsonObj.get("someUtxo") != null && !jsonObj.get("someUtxo").isJsonNull()) && !jsonObj.get("someUtxo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `someUtxo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("someUtxo").toString()));
      }
      if ((jsonObj.get("tokenId") != null && !jsonObj.get("tokenId").isJsonNull()) && !jsonObj.get("tokenId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tokenId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tokenId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetTokenMetadataResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetTokenMetadataResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetTokenMetadataResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetTokenMetadataResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<GetTokenMetadataResponse>() {
           @Override
           public void write(JsonWriter out, GetTokenMetadataResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetTokenMetadataResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetTokenMetadataResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetTokenMetadataResponse
   * @throws IOException if the JSON string is invalid with respect to GetTokenMetadataResponse
   */
  public static GetTokenMetadataResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetTokenMetadataResponse.class);
  }

  /**
   * Convert an instance of GetTokenMetadataResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

