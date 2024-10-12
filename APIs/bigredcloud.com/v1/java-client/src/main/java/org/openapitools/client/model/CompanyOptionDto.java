/*
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
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
 * CompanyOptionDto
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:05.666566-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompanyOptionDto {
  public static final String SERIALIZED_NAME_ALLOW_ENTRY_OF_GROSS_PRICE_IN_INVOICING = "allowEntryOfGrossPriceInInvoicing";
  @SerializedName(SERIALIZED_NAME_ALLOW_ENTRY_OF_GROSS_PRICE_IN_INVOICING)
  private Boolean allowEntryOfGrossPriceInInvoicing;

  public static final String SERIALIZED_NAME_CREDIT_INPUT_FOR_REVERSE_CHARGE_V_A_T = "creditInputForReverseChargeVAT";
  @SerializedName(SERIALIZED_NAME_CREDIT_INPUT_FOR_REVERSE_CHARGE_V_A_T)
  private Boolean creditInputForReverseChargeVAT;

  public static final String SERIALIZED_NAME_CREDIT_NOTE_JOURNAL_AGEING_NAME = "creditNoteJournalAgeingName";
  @SerializedName(SERIALIZED_NAME_CREDIT_NOTE_JOURNAL_AGEING_NAME)
  private String creditNoteJournalAgeingName;

  public static final String SERIALIZED_NAME_CREDIT_NOTE_JOURNAL_AGEING_VALUE = "creditNoteJournalAgeingValue";
  @SerializedName(SERIALIZED_NAME_CREDIT_NOTE_JOURNAL_AGEING_VALUE)
  private Integer creditNoteJournalAgeingValue;

  public static final String SERIALIZED_NAME_DISCREPANCY_ALLOWED = "discrepancyAllowed";
  @SerializedName(SERIALIZED_NAME_DISCREPANCY_ALLOWED)
  private Double discrepancyAllowed;

  public static final String SERIALIZED_NAME_ENABLE_V_O_C_R_REPORTING = "enableVOCRReporting";
  @SerializedName(SERIALIZED_NAME_ENABLE_V_O_C_R_REPORTING)
  private Boolean enableVOCRReporting;

  public static final String SERIALIZED_NAME_MARGIN_VAT_SCHEME = "marginVatScheme";
  @SerializedName(SERIALIZED_NAME_MARGIN_VAT_SCHEME)
  private Boolean marginVatScheme;

  public static final String SERIALIZED_NAME_PRINT_O_S_ITEMS_ONLY = "printOSItemsOnly";
  @SerializedName(SERIALIZED_NAME_PRINT_O_S_ITEMS_ONLY)
  private Boolean printOSItemsOnly;

  public static final String SERIALIZED_NAME_PURCHASES_VAT_ANALYSIS_TYPE = "purchasesVatAnalysisType";
  @SerializedName(SERIALIZED_NAME_PURCHASES_VAT_ANALYSIS_TYPE)
  private Long purchasesVatAnalysisType;

  public static final String SERIALIZED_NAME_SALES_VAT_ANALYSIS_TYPE = "salesVatAnalysisType";
  @SerializedName(SERIALIZED_NAME_SALES_VAT_ANALYSIS_TYPE)
  private Long salesVatAnalysisType;

  public static final String SERIALIZED_NAME_USE_ALLOCATIONS = "useAllocations";
  @SerializedName(SERIALIZED_NAME_USE_ALLOCATIONS)
  private Boolean useAllocations;

  public static final String SERIALIZED_NAME_USE_NOMINAL = "useNominal";
  @SerializedName(SERIALIZED_NAME_USE_NOMINAL)
  private Boolean useNominal;

  public static final String SERIALIZED_NAME_USE_NOMINAL_CODE = "useNominalCode";
  @SerializedName(SERIALIZED_NAME_USE_NOMINAL_CODE)
  private Boolean useNominalCode;

  public static final String SERIALIZED_NAME_VOCR_SETTING_VALUE = "vocrSettingValue";
  @SerializedName(SERIALIZED_NAME_VOCR_SETTING_VALUE)
  private Boolean vocrSettingValue;

  public CompanyOptionDto() {
  }

  public CompanyOptionDto allowEntryOfGrossPriceInInvoicing(Boolean allowEntryOfGrossPriceInInvoicing) {
    this.allowEntryOfGrossPriceInInvoicing = allowEntryOfGrossPriceInInvoicing;
    return this;
  }

  /**
   * Get allowEntryOfGrossPriceInInvoicing
   * @return allowEntryOfGrossPriceInInvoicing
   */
  @javax.annotation.Nullable
  public Boolean getAllowEntryOfGrossPriceInInvoicing() {
    return allowEntryOfGrossPriceInInvoicing;
  }

  public void setAllowEntryOfGrossPriceInInvoicing(Boolean allowEntryOfGrossPriceInInvoicing) {
    this.allowEntryOfGrossPriceInInvoicing = allowEntryOfGrossPriceInInvoicing;
  }


  public CompanyOptionDto creditInputForReverseChargeVAT(Boolean creditInputForReverseChargeVAT) {
    this.creditInputForReverseChargeVAT = creditInputForReverseChargeVAT;
    return this;
  }

  /**
   * Get creditInputForReverseChargeVAT
   * @return creditInputForReverseChargeVAT
   */
  @javax.annotation.Nullable
  public Boolean getCreditInputForReverseChargeVAT() {
    return creditInputForReverseChargeVAT;
  }

  public void setCreditInputForReverseChargeVAT(Boolean creditInputForReverseChargeVAT) {
    this.creditInputForReverseChargeVAT = creditInputForReverseChargeVAT;
  }


  public CompanyOptionDto creditNoteJournalAgeingName(String creditNoteJournalAgeingName) {
    this.creditNoteJournalAgeingName = creditNoteJournalAgeingName;
    return this;
  }

  /**
   * Get creditNoteJournalAgeingName
   * @return creditNoteJournalAgeingName
   */
  @javax.annotation.Nullable
  public String getCreditNoteJournalAgeingName() {
    return creditNoteJournalAgeingName;
  }

  public void setCreditNoteJournalAgeingName(String creditNoteJournalAgeingName) {
    this.creditNoteJournalAgeingName = creditNoteJournalAgeingName;
  }


  public CompanyOptionDto creditNoteJournalAgeingValue(Integer creditNoteJournalAgeingValue) {
    this.creditNoteJournalAgeingValue = creditNoteJournalAgeingValue;
    return this;
  }

  /**
   * Get creditNoteJournalAgeingValue
   * @return creditNoteJournalAgeingValue
   */
  @javax.annotation.Nullable
  public Integer getCreditNoteJournalAgeingValue() {
    return creditNoteJournalAgeingValue;
  }

  public void setCreditNoteJournalAgeingValue(Integer creditNoteJournalAgeingValue) {
    this.creditNoteJournalAgeingValue = creditNoteJournalAgeingValue;
  }


  public CompanyOptionDto discrepancyAllowed(Double discrepancyAllowed) {
    this.discrepancyAllowed = discrepancyAllowed;
    return this;
  }

  /**
   * Get discrepancyAllowed
   * @return discrepancyAllowed
   */
  @javax.annotation.Nullable
  public Double getDiscrepancyAllowed() {
    return discrepancyAllowed;
  }

  public void setDiscrepancyAllowed(Double discrepancyAllowed) {
    this.discrepancyAllowed = discrepancyAllowed;
  }


  public CompanyOptionDto enableVOCRReporting(Boolean enableVOCRReporting) {
    this.enableVOCRReporting = enableVOCRReporting;
    return this;
  }

  /**
   * Get enableVOCRReporting
   * @return enableVOCRReporting
   */
  @javax.annotation.Nullable
  public Boolean getEnableVOCRReporting() {
    return enableVOCRReporting;
  }

  public void setEnableVOCRReporting(Boolean enableVOCRReporting) {
    this.enableVOCRReporting = enableVOCRReporting;
  }


  public CompanyOptionDto marginVatScheme(Boolean marginVatScheme) {
    this.marginVatScheme = marginVatScheme;
    return this;
  }

  /**
   * Get marginVatScheme
   * @return marginVatScheme
   */
  @javax.annotation.Nullable
  public Boolean getMarginVatScheme() {
    return marginVatScheme;
  }

  public void setMarginVatScheme(Boolean marginVatScheme) {
    this.marginVatScheme = marginVatScheme;
  }


  public CompanyOptionDto printOSItemsOnly(Boolean printOSItemsOnly) {
    this.printOSItemsOnly = printOSItemsOnly;
    return this;
  }

  /**
   * Get printOSItemsOnly
   * @return printOSItemsOnly
   */
  @javax.annotation.Nullable
  public Boolean getPrintOSItemsOnly() {
    return printOSItemsOnly;
  }

  public void setPrintOSItemsOnly(Boolean printOSItemsOnly) {
    this.printOSItemsOnly = printOSItemsOnly;
  }


  public CompanyOptionDto purchasesVatAnalysisType(Long purchasesVatAnalysisType) {
    this.purchasesVatAnalysisType = purchasesVatAnalysisType;
    return this;
  }

  /**
   * Get purchasesVatAnalysisType
   * @return purchasesVatAnalysisType
   */
  @javax.annotation.Nullable
  public Long getPurchasesVatAnalysisType() {
    return purchasesVatAnalysisType;
  }

  public void setPurchasesVatAnalysisType(Long purchasesVatAnalysisType) {
    this.purchasesVatAnalysisType = purchasesVatAnalysisType;
  }


  public CompanyOptionDto salesVatAnalysisType(Long salesVatAnalysisType) {
    this.salesVatAnalysisType = salesVatAnalysisType;
    return this;
  }

  /**
   * Get salesVatAnalysisType
   * @return salesVatAnalysisType
   */
  @javax.annotation.Nullable
  public Long getSalesVatAnalysisType() {
    return salesVatAnalysisType;
  }

  public void setSalesVatAnalysisType(Long salesVatAnalysisType) {
    this.salesVatAnalysisType = salesVatAnalysisType;
  }


  public CompanyOptionDto useAllocations(Boolean useAllocations) {
    this.useAllocations = useAllocations;
    return this;
  }

  /**
   * Get useAllocations
   * @return useAllocations
   */
  @javax.annotation.Nullable
  public Boolean getUseAllocations() {
    return useAllocations;
  }

  public void setUseAllocations(Boolean useAllocations) {
    this.useAllocations = useAllocations;
  }


  public CompanyOptionDto useNominal(Boolean useNominal) {
    this.useNominal = useNominal;
    return this;
  }

  /**
   * Get useNominal
   * @return useNominal
   */
  @javax.annotation.Nullable
  public Boolean getUseNominal() {
    return useNominal;
  }

  public void setUseNominal(Boolean useNominal) {
    this.useNominal = useNominal;
  }


  public CompanyOptionDto useNominalCode(Boolean useNominalCode) {
    this.useNominalCode = useNominalCode;
    return this;
  }

  /**
   * Get useNominalCode
   * @return useNominalCode
   */
  @javax.annotation.Nullable
  public Boolean getUseNominalCode() {
    return useNominalCode;
  }

  public void setUseNominalCode(Boolean useNominalCode) {
    this.useNominalCode = useNominalCode;
  }


  public CompanyOptionDto vocrSettingValue(Boolean vocrSettingValue) {
    this.vocrSettingValue = vocrSettingValue;
    return this;
  }

  /**
   * Get vocrSettingValue
   * @return vocrSettingValue
   */
  @javax.annotation.Nullable
  public Boolean getVocrSettingValue() {
    return vocrSettingValue;
  }

  public void setVocrSettingValue(Boolean vocrSettingValue) {
    this.vocrSettingValue = vocrSettingValue;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompanyOptionDto companyOptionDto = (CompanyOptionDto) o;
    return Objects.equals(this.allowEntryOfGrossPriceInInvoicing, companyOptionDto.allowEntryOfGrossPriceInInvoicing) &&
        Objects.equals(this.creditInputForReverseChargeVAT, companyOptionDto.creditInputForReverseChargeVAT) &&
        Objects.equals(this.creditNoteJournalAgeingName, companyOptionDto.creditNoteJournalAgeingName) &&
        Objects.equals(this.creditNoteJournalAgeingValue, companyOptionDto.creditNoteJournalAgeingValue) &&
        Objects.equals(this.discrepancyAllowed, companyOptionDto.discrepancyAllowed) &&
        Objects.equals(this.enableVOCRReporting, companyOptionDto.enableVOCRReporting) &&
        Objects.equals(this.marginVatScheme, companyOptionDto.marginVatScheme) &&
        Objects.equals(this.printOSItemsOnly, companyOptionDto.printOSItemsOnly) &&
        Objects.equals(this.purchasesVatAnalysisType, companyOptionDto.purchasesVatAnalysisType) &&
        Objects.equals(this.salesVatAnalysisType, companyOptionDto.salesVatAnalysisType) &&
        Objects.equals(this.useAllocations, companyOptionDto.useAllocations) &&
        Objects.equals(this.useNominal, companyOptionDto.useNominal) &&
        Objects.equals(this.useNominalCode, companyOptionDto.useNominalCode) &&
        Objects.equals(this.vocrSettingValue, companyOptionDto.vocrSettingValue);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowEntryOfGrossPriceInInvoicing, creditInputForReverseChargeVAT, creditNoteJournalAgeingName, creditNoteJournalAgeingValue, discrepancyAllowed, enableVOCRReporting, marginVatScheme, printOSItemsOnly, purchasesVatAnalysisType, salesVatAnalysisType, useAllocations, useNominal, useNominalCode, vocrSettingValue);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompanyOptionDto {\n");
    sb.append("    allowEntryOfGrossPriceInInvoicing: ").append(toIndentedString(allowEntryOfGrossPriceInInvoicing)).append("\n");
    sb.append("    creditInputForReverseChargeVAT: ").append(toIndentedString(creditInputForReverseChargeVAT)).append("\n");
    sb.append("    creditNoteJournalAgeingName: ").append(toIndentedString(creditNoteJournalAgeingName)).append("\n");
    sb.append("    creditNoteJournalAgeingValue: ").append(toIndentedString(creditNoteJournalAgeingValue)).append("\n");
    sb.append("    discrepancyAllowed: ").append(toIndentedString(discrepancyAllowed)).append("\n");
    sb.append("    enableVOCRReporting: ").append(toIndentedString(enableVOCRReporting)).append("\n");
    sb.append("    marginVatScheme: ").append(toIndentedString(marginVatScheme)).append("\n");
    sb.append("    printOSItemsOnly: ").append(toIndentedString(printOSItemsOnly)).append("\n");
    sb.append("    purchasesVatAnalysisType: ").append(toIndentedString(purchasesVatAnalysisType)).append("\n");
    sb.append("    salesVatAnalysisType: ").append(toIndentedString(salesVatAnalysisType)).append("\n");
    sb.append("    useAllocations: ").append(toIndentedString(useAllocations)).append("\n");
    sb.append("    useNominal: ").append(toIndentedString(useNominal)).append("\n");
    sb.append("    useNominalCode: ").append(toIndentedString(useNominalCode)).append("\n");
    sb.append("    vocrSettingValue: ").append(toIndentedString(vocrSettingValue)).append("\n");
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
    openapiFields.add("allowEntryOfGrossPriceInInvoicing");
    openapiFields.add("creditInputForReverseChargeVAT");
    openapiFields.add("creditNoteJournalAgeingName");
    openapiFields.add("creditNoteJournalAgeingValue");
    openapiFields.add("discrepancyAllowed");
    openapiFields.add("enableVOCRReporting");
    openapiFields.add("marginVatScheme");
    openapiFields.add("printOSItemsOnly");
    openapiFields.add("purchasesVatAnalysisType");
    openapiFields.add("salesVatAnalysisType");
    openapiFields.add("useAllocations");
    openapiFields.add("useNominal");
    openapiFields.add("useNominalCode");
    openapiFields.add("vocrSettingValue");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompanyOptionDto
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompanyOptionDto.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompanyOptionDto is not found in the empty JSON string", CompanyOptionDto.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompanyOptionDto.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompanyOptionDto` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("creditNoteJournalAgeingName") != null && !jsonObj.get("creditNoteJournalAgeingName").isJsonNull()) && !jsonObj.get("creditNoteJournalAgeingName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creditNoteJournalAgeingName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creditNoteJournalAgeingName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompanyOptionDto.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompanyOptionDto' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompanyOptionDto> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompanyOptionDto.class));

       return (TypeAdapter<T>) new TypeAdapter<CompanyOptionDto>() {
           @Override
           public void write(JsonWriter out, CompanyOptionDto value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompanyOptionDto read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompanyOptionDto given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompanyOptionDto
   * @throws IOException if the JSON string is invalid with respect to CompanyOptionDto
   */
  public static CompanyOptionDto fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompanyOptionDto.class);
  }

  /**
   * Convert an instance of CompanyOptionDto to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

