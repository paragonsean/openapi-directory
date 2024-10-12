/*
 * Cnab Online
 * Processe arquivos de retorno CNAB
 *
 * The version of the OpenAPI document: 1.0.0
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
 * OccurrenceAttributes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.615441-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OccurrenceAttributes {
  public static final String SERIALIZED_NAME_AGENCY = "agency";
  @SerializedName(SERIALIZED_NAME_AGENCY)
  private String agency;

  public static final String SERIALIZED_NAME_BANK_TAX = "bank_tax";
  @SerializedName(SERIALIZED_NAME_BANK_TAX)
  private BigDecimal bankTax;

  public static final String SERIALIZED_NAME_CHARGED_AGENCY = "charged_agency";
  @SerializedName(SERIALIZED_NAME_CHARGED_AGENCY)
  private String chargedAgency;

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_CODE_NAME = "code_name";
  @SerializedName(SERIALIZED_NAME_CODE_NAME)
  private String codeName;

  public static final String SERIALIZED_NAME_CREDIT_DATE = "credit_date";
  @SerializedName(SERIALIZED_NAME_CREDIT_DATE)
  private String creditDate;

  public static final String SERIALIZED_NAME_DISCOUNT_VALUE = "discount_value";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_VALUE)
  private BigDecimal discountValue;

  public static final String SERIALIZED_NAME_DOCUMENT_NUMBER = "document_number";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_NUMBER)
  private String documentNumber;

  public static final String SERIALIZED_NAME_DUE_DATE = "due_date";
  @SerializedName(SERIALIZED_NAME_DUE_DATE)
  private String dueDate;

  public static final String SERIALIZED_NAME_IOF_TAX = "iof_tax";
  @SerializedName(SERIALIZED_NAME_IOF_TAX)
  private BigDecimal iofTax;

  public static final String SERIALIZED_NAME_IS_DDA = "is_dda";
  @SerializedName(SERIALIZED_NAME_IS_DDA)
  private String isDda;

  public static final String SERIALIZED_NAME_IS_PAYMENT = "is_payment";
  @SerializedName(SERIALIZED_NAME_IS_PAYMENT)
  private Boolean isPayment;

  public static final String SERIALIZED_NAME_IS_REJECTED_PAYMENT = "is_rejected_payment";
  @SerializedName(SERIALIZED_NAME_IS_REJECTED_PAYMENT)
  private Boolean isRejectedPayment;

  public static final String SERIALIZED_NAME_LIQUIDATION_CODE = "liquidation_code";
  @SerializedName(SERIALIZED_NAME_LIQUIDATION_CODE)
  private String liquidationCode;

  public static final String SERIALIZED_NAME_LIQUIDATION_DESCRIPTION = "liquidation_description";
  @SerializedName(SERIALIZED_NAME_LIQUIDATION_DESCRIPTION)
  private String liquidationDescription;

  public static final String SERIALIZED_NAME_MULCT_VALUE = "mulct_value";
  @SerializedName(SERIALIZED_NAME_MULCT_VALUE)
  private String mulctValue;

  public static final String SERIALIZED_NAME_OCCURRENCE_DATE = "occurrence_date";
  @SerializedName(SERIALIZED_NAME_OCCURRENCE_DATE)
  private String occurrenceDate;

  public static final String SERIALIZED_NAME_OTHERS_CREDITS_VALUE = "others_credits_value";
  @SerializedName(SERIALIZED_NAME_OTHERS_CREDITS_VALUE)
  private BigDecimal othersCreditsValue;

  public static final String SERIALIZED_NAME_OUR_NUMBER = "our_number";
  @SerializedName(SERIALIZED_NAME_OUR_NUMBER)
  private String ourNumber;

  public static final String SERIALIZED_NAME_PAYER_ALLEGATION = "payer_allegation";
  @SerializedName(SERIALIZED_NAME_PAYER_ALLEGATION)
  private String payerAllegation;

  public static final String SERIALIZED_NAME_REBATE_VALUE = "rebate_value";
  @SerializedName(SERIALIZED_NAME_REBATE_VALUE)
  private BigDecimal rebateValue;

  public static final String SERIALIZED_NAME_RECEIVED_VALUE = "received_value";
  @SerializedName(SERIALIZED_NAME_RECEIVED_VALUE)
  private BigDecimal receivedValue;

  public static final String SERIALIZED_NAME_SEQUENCIAL_NUMBER = "sequencial_number";
  @SerializedName(SERIALIZED_NAME_SEQUENCIAL_NUMBER)
  private BigDecimal sequencialNumber;

  public static final String SERIALIZED_NAME_TITLE_VALUE = "title_value";
  @SerializedName(SERIALIZED_NAME_TITLE_VALUE)
  private BigDecimal titleValue;

  public static final String SERIALIZED_NAME_WALLET = "wallet";
  @SerializedName(SERIALIZED_NAME_WALLET)
  private String wallet;

  public OccurrenceAttributes() {
  }

  public OccurrenceAttributes agency(String agency) {
    this.agency = agency;
    return this;
  }

  /**
   * Retorna o número da agencia
   * @return agency
   */
  @javax.annotation.Nullable
  public String getAgency() {
    return agency;
  }

  public void setAgency(String agency) {
    this.agency = agency;
  }


  public OccurrenceAttributes bankTax(BigDecimal bankTax) {
    this.bankTax = bankTax;
    return this;
  }

  /**
   * Tarifa bancária
   * @return bankTax
   */
  @javax.annotation.Nullable
  public BigDecimal getBankTax() {
    return bankTax;
  }

  public void setBankTax(BigDecimal bankTax) {
    this.bankTax = bankTax;
  }


  public OccurrenceAttributes chargedAgency(String chargedAgency) {
    this.chargedAgency = chargedAgency;
    return this;
  }

  /**
   * Retorna a agencia cobradora (com o digito)
   * @return chargedAgency
   */
  @javax.annotation.Nullable
  public String getChargedAgency() {
    return chargedAgency;
  }

  public void setChargedAgency(String chargedAgency) {
    this.chargedAgency = chargedAgency;
  }


  public OccurrenceAttributes code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Código de Ocorrência conforme o padrão CNAB
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public OccurrenceAttributes codeName(String codeName) {
    this.codeName = codeName;
    return this;
  }

  /**
   * Nome do código
   * @return codeName
   */
  @javax.annotation.Nullable
  public String getCodeName() {
    return codeName;
  }

  public void setCodeName(String codeName) {
    this.codeName = codeName;
  }


  public OccurrenceAttributes creditDate(String creditDate) {
    this.creditDate = creditDate;
    return this;
  }

  /**
   * Retorna a data em que o dinheiro caiu na conta
   * @return creditDate
   */
  @javax.annotation.Nullable
  public String getCreditDate() {
    return creditDate;
  }

  public void setCreditDate(String creditDate) {
    this.creditDate = creditDate;
  }


  public OccurrenceAttributes discountValue(BigDecimal discountValue) {
    this.discountValue = discountValue;
    return this;
  }

  /**
   * Valor de desconto
   * @return discountValue
   */
  @javax.annotation.Nullable
  public BigDecimal getDiscountValue() {
    return discountValue;
  }

  public void setDiscountValue(BigDecimal discountValue) {
    this.discountValue = discountValue;
  }


  public OccurrenceAttributes documentNumber(String documentNumber) {
    this.documentNumber = documentNumber;
    return this;
  }

  /**
   * Retorna o número do documento do boleto
   * @return documentNumber
   */
  @javax.annotation.Nullable
  public String getDocumentNumber() {
    return documentNumber;
  }

  public void setDocumentNumber(String documentNumber) {
    this.documentNumber = documentNumber;
  }


  public OccurrenceAttributes dueDate(String dueDate) {
    this.dueDate = dueDate;
    return this;
  }

  /**
   * Retorna a data de vencimento de boleto
   * @return dueDate
   */
  @javax.annotation.Nullable
  public String getDueDate() {
    return dueDate;
  }

  public void setDueDate(String dueDate) {
    this.dueDate = dueDate;
  }


  public OccurrenceAttributes iofTax(BigDecimal iofTax) {
    this.iofTax = iofTax;
    return this;
  }

  /**
   * Retorna o valor do Imposto sobre operações financeiras (IOF)
   * @return iofTax
   */
  @javax.annotation.Nullable
  public BigDecimal getIofTax() {
    return iofTax;
  }

  public void setIofTax(BigDecimal iofTax) {
    this.iofTax = iofTax;
  }


  public OccurrenceAttributes isDda(String isDda) {
    this.isDda = isDda;
    return this;
  }

  /**
   * Retorna de o boleto foi pago através do Débito Direto Autorizado
   * @return isDda
   */
  @javax.annotation.Nullable
  public String getIsDda() {
    return isDda;
  }

  public void setIsDda(String isDda) {
    this.isDda = isDda;
  }


  public OccurrenceAttributes isPayment(Boolean isPayment) {
    this.isPayment = isPayment;
    return this;
  }

  /**
   * Retorna se é para dar baixa no boleto
   * @return isPayment
   */
  @javax.annotation.Nullable
  public Boolean getIsPayment() {
    return isPayment;
  }

  public void setIsPayment(Boolean isPayment) {
    this.isPayment = isPayment;
  }


  public OccurrenceAttributes isRejectedPayment(Boolean isRejectedPayment) {
    this.isRejectedPayment = isRejectedPayment;
    return this;
  }

  /**
   * Retorno se é uma baixa rejeitada (Ex: pedido de baixa foi rejeitado)
   * @return isRejectedPayment
   */
  @javax.annotation.Nullable
  public Boolean getIsRejectedPayment() {
    return isRejectedPayment;
  }

  public void setIsRejectedPayment(Boolean isRejectedPayment) {
    this.isRejectedPayment = isRejectedPayment;
  }


  public OccurrenceAttributes liquidationCode(String liquidationCode) {
    this.liquidationCode = liquidationCode;
    return this;
  }

  /**
   * Retorna o código de liquidação, normalmente usado para saber onde o cliente efetuou o pagamento
   * @return liquidationCode
   */
  @javax.annotation.Nullable
  public String getLiquidationCode() {
    return liquidationCode;
  }

  public void setLiquidationCode(String liquidationCode) {
    this.liquidationCode = liquidationCode;
  }


  public OccurrenceAttributes liquidationDescription(String liquidationDescription) {
    this.liquidationDescription = liquidationDescription;
    return this;
  }

  /**
   * Retorna a descrição do código de liquidação
   * @return liquidationDescription
   */
  @javax.annotation.Nullable
  public String getLiquidationDescription() {
    return liquidationDescription;
  }

  public void setLiquidationDescription(String liquidationDescription) {
    this.liquidationDescription = liquidationDescription;
  }


  public OccurrenceAttributes mulctValue(String mulctValue) {
    this.mulctValue = mulctValue;
    return this;
  }

  /**
   * Retorna o valor de juros e mora
   * @return mulctValue
   */
  @javax.annotation.Nullable
  public String getMulctValue() {
    return mulctValue;
  }

  public void setMulctValue(String mulctValue) {
    this.mulctValue = mulctValue;
  }


  public OccurrenceAttributes occurrenceDate(String occurrenceDate) {
    this.occurrenceDate = occurrenceDate;
    return this;
  }

  /**
   * Retorna a data da ocorrencia, o dia do pagamento
   * @return occurrenceDate
   */
  @javax.annotation.Nullable
  public String getOccurrenceDate() {
    return occurrenceDate;
  }

  public void setOccurrenceDate(String occurrenceDate) {
    this.occurrenceDate = occurrenceDate;
  }


  public OccurrenceAttributes othersCreditsValue(BigDecimal othersCreditsValue) {
    this.othersCreditsValue = othersCreditsValue;
    return this;
  }

  /**
   * Retorna o valor de outros creditos
   * @return othersCreditsValue
   */
  @javax.annotation.Nullable
  public BigDecimal getOthersCreditsValue() {
    return othersCreditsValue;
  }

  public void setOthersCreditsValue(BigDecimal othersCreditsValue) {
    this.othersCreditsValue = othersCreditsValue;
  }


  public OccurrenceAttributes ourNumber(String ourNumber) {
    this.ourNumber = ourNumber;
    return this;
  }

  /**
   * Retorna o nosso número do boleto (sem o digito)
   * @return ourNumber
   */
  @javax.annotation.Nullable
  public String getOurNumber() {
    return ourNumber;
  }

  public void setOurNumber(String ourNumber) {
    this.ourNumber = ourNumber;
  }


  public OccurrenceAttributes payerAllegation(String payerAllegation) {
    this.payerAllegation = payerAllegation;
    return this;
  }

  /**
   * Retorna a alegação do pagador (para erros)
   * @return payerAllegation
   */
  @javax.annotation.Nullable
  public String getPayerAllegation() {
    return payerAllegation;
  }

  public void setPayerAllegation(String payerAllegation) {
    this.payerAllegation = payerAllegation;
  }


  public OccurrenceAttributes rebateValue(BigDecimal rebateValue) {
    this.rebateValue = rebateValue;
    return this;
  }

  /**
   * Retornna o valor dos abatimentos concedidos (depois da emissão)
   * @return rebateValue
   */
  @javax.annotation.Nullable
  public BigDecimal getRebateValue() {
    return rebateValue;
  }

  public void setRebateValue(BigDecimal rebateValue) {
    this.rebateValue = rebateValue;
  }


  public OccurrenceAttributes receivedValue(BigDecimal receivedValue) {
    this.receivedValue = receivedValue;
    return this;
  }

  /**
   * Valor recebido
   * @return receivedValue
   */
  @javax.annotation.Nullable
  public BigDecimal getReceivedValue() {
    return receivedValue;
  }

  public void setReceivedValue(BigDecimal receivedValue) {
    this.receivedValue = receivedValue;
  }


  public OccurrenceAttributes sequencialNumber(BigDecimal sequencialNumber) {
    this.sequencialNumber = sequencialNumber;
    return this;
  }

  /**
   * Retorna o numero sequencial da ocorrência no arquivo
   * @return sequencialNumber
   */
  @javax.annotation.Nullable
  public BigDecimal getSequencialNumber() {
    return sequencialNumber;
  }

  public void setSequencialNumber(BigDecimal sequencialNumber) {
    this.sequencialNumber = sequencialNumber;
  }


  public OccurrenceAttributes titleValue(BigDecimal titleValue) {
    this.titleValue = titleValue;
    return this;
  }

  /**
   * Valor do título (valor do boleto)
   * @return titleValue
   */
  @javax.annotation.Nullable
  public BigDecimal getTitleValue() {
    return titleValue;
  }

  public void setTitleValue(BigDecimal titleValue) {
    this.titleValue = titleValue;
  }


  public OccurrenceAttributes wallet(String wallet) {
    this.wallet = wallet;
    return this;
  }

  /**
   * Retorna o número da carteira do boleto
   * @return wallet
   */
  @javax.annotation.Nullable
  public String getWallet() {
    return wallet;
  }

  public void setWallet(String wallet) {
    this.wallet = wallet;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OccurrenceAttributes occurrenceAttributes = (OccurrenceAttributes) o;
    return Objects.equals(this.agency, occurrenceAttributes.agency) &&
        Objects.equals(this.bankTax, occurrenceAttributes.bankTax) &&
        Objects.equals(this.chargedAgency, occurrenceAttributes.chargedAgency) &&
        Objects.equals(this.code, occurrenceAttributes.code) &&
        Objects.equals(this.codeName, occurrenceAttributes.codeName) &&
        Objects.equals(this.creditDate, occurrenceAttributes.creditDate) &&
        Objects.equals(this.discountValue, occurrenceAttributes.discountValue) &&
        Objects.equals(this.documentNumber, occurrenceAttributes.documentNumber) &&
        Objects.equals(this.dueDate, occurrenceAttributes.dueDate) &&
        Objects.equals(this.iofTax, occurrenceAttributes.iofTax) &&
        Objects.equals(this.isDda, occurrenceAttributes.isDda) &&
        Objects.equals(this.isPayment, occurrenceAttributes.isPayment) &&
        Objects.equals(this.isRejectedPayment, occurrenceAttributes.isRejectedPayment) &&
        Objects.equals(this.liquidationCode, occurrenceAttributes.liquidationCode) &&
        Objects.equals(this.liquidationDescription, occurrenceAttributes.liquidationDescription) &&
        Objects.equals(this.mulctValue, occurrenceAttributes.mulctValue) &&
        Objects.equals(this.occurrenceDate, occurrenceAttributes.occurrenceDate) &&
        Objects.equals(this.othersCreditsValue, occurrenceAttributes.othersCreditsValue) &&
        Objects.equals(this.ourNumber, occurrenceAttributes.ourNumber) &&
        Objects.equals(this.payerAllegation, occurrenceAttributes.payerAllegation) &&
        Objects.equals(this.rebateValue, occurrenceAttributes.rebateValue) &&
        Objects.equals(this.receivedValue, occurrenceAttributes.receivedValue) &&
        Objects.equals(this.sequencialNumber, occurrenceAttributes.sequencialNumber) &&
        Objects.equals(this.titleValue, occurrenceAttributes.titleValue) &&
        Objects.equals(this.wallet, occurrenceAttributes.wallet);
  }

  @Override
  public int hashCode() {
    return Objects.hash(agency, bankTax, chargedAgency, code, codeName, creditDate, discountValue, documentNumber, dueDate, iofTax, isDda, isPayment, isRejectedPayment, liquidationCode, liquidationDescription, mulctValue, occurrenceDate, othersCreditsValue, ourNumber, payerAllegation, rebateValue, receivedValue, sequencialNumber, titleValue, wallet);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OccurrenceAttributes {\n");
    sb.append("    agency: ").append(toIndentedString(agency)).append("\n");
    sb.append("    bankTax: ").append(toIndentedString(bankTax)).append("\n");
    sb.append("    chargedAgency: ").append(toIndentedString(chargedAgency)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    codeName: ").append(toIndentedString(codeName)).append("\n");
    sb.append("    creditDate: ").append(toIndentedString(creditDate)).append("\n");
    sb.append("    discountValue: ").append(toIndentedString(discountValue)).append("\n");
    sb.append("    documentNumber: ").append(toIndentedString(documentNumber)).append("\n");
    sb.append("    dueDate: ").append(toIndentedString(dueDate)).append("\n");
    sb.append("    iofTax: ").append(toIndentedString(iofTax)).append("\n");
    sb.append("    isDda: ").append(toIndentedString(isDda)).append("\n");
    sb.append("    isPayment: ").append(toIndentedString(isPayment)).append("\n");
    sb.append("    isRejectedPayment: ").append(toIndentedString(isRejectedPayment)).append("\n");
    sb.append("    liquidationCode: ").append(toIndentedString(liquidationCode)).append("\n");
    sb.append("    liquidationDescription: ").append(toIndentedString(liquidationDescription)).append("\n");
    sb.append("    mulctValue: ").append(toIndentedString(mulctValue)).append("\n");
    sb.append("    occurrenceDate: ").append(toIndentedString(occurrenceDate)).append("\n");
    sb.append("    othersCreditsValue: ").append(toIndentedString(othersCreditsValue)).append("\n");
    sb.append("    ourNumber: ").append(toIndentedString(ourNumber)).append("\n");
    sb.append("    payerAllegation: ").append(toIndentedString(payerAllegation)).append("\n");
    sb.append("    rebateValue: ").append(toIndentedString(rebateValue)).append("\n");
    sb.append("    receivedValue: ").append(toIndentedString(receivedValue)).append("\n");
    sb.append("    sequencialNumber: ").append(toIndentedString(sequencialNumber)).append("\n");
    sb.append("    titleValue: ").append(toIndentedString(titleValue)).append("\n");
    sb.append("    wallet: ").append(toIndentedString(wallet)).append("\n");
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
    openapiFields.add("agency");
    openapiFields.add("bank_tax");
    openapiFields.add("charged_agency");
    openapiFields.add("code");
    openapiFields.add("code_name");
    openapiFields.add("credit_date");
    openapiFields.add("discount_value");
    openapiFields.add("document_number");
    openapiFields.add("due_date");
    openapiFields.add("iof_tax");
    openapiFields.add("is_dda");
    openapiFields.add("is_payment");
    openapiFields.add("is_rejected_payment");
    openapiFields.add("liquidation_code");
    openapiFields.add("liquidation_description");
    openapiFields.add("mulct_value");
    openapiFields.add("occurrence_date");
    openapiFields.add("others_credits_value");
    openapiFields.add("our_number");
    openapiFields.add("payer_allegation");
    openapiFields.add("rebate_value");
    openapiFields.add("received_value");
    openapiFields.add("sequencial_number");
    openapiFields.add("title_value");
    openapiFields.add("wallet");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OccurrenceAttributes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OccurrenceAttributes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OccurrenceAttributes is not found in the empty JSON string", OccurrenceAttributes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OccurrenceAttributes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OccurrenceAttributes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("agency") != null && !jsonObj.get("agency").isJsonNull()) && !jsonObj.get("agency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `agency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("agency").toString()));
      }
      if ((jsonObj.get("charged_agency") != null && !jsonObj.get("charged_agency").isJsonNull()) && !jsonObj.get("charged_agency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `charged_agency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("charged_agency").toString()));
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("code_name") != null && !jsonObj.get("code_name").isJsonNull()) && !jsonObj.get("code_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code_name").toString()));
      }
      if ((jsonObj.get("credit_date") != null && !jsonObj.get("credit_date").isJsonNull()) && !jsonObj.get("credit_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `credit_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("credit_date").toString()));
      }
      if ((jsonObj.get("document_number") != null && !jsonObj.get("document_number").isJsonNull()) && !jsonObj.get("document_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `document_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("document_number").toString()));
      }
      if ((jsonObj.get("due_date") != null && !jsonObj.get("due_date").isJsonNull()) && !jsonObj.get("due_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `due_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("due_date").toString()));
      }
      if ((jsonObj.get("is_dda") != null && !jsonObj.get("is_dda").isJsonNull()) && !jsonObj.get("is_dda").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_dda` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_dda").toString()));
      }
      if ((jsonObj.get("liquidation_code") != null && !jsonObj.get("liquidation_code").isJsonNull()) && !jsonObj.get("liquidation_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `liquidation_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("liquidation_code").toString()));
      }
      if ((jsonObj.get("liquidation_description") != null && !jsonObj.get("liquidation_description").isJsonNull()) && !jsonObj.get("liquidation_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `liquidation_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("liquidation_description").toString()));
      }
      if ((jsonObj.get("mulct_value") != null && !jsonObj.get("mulct_value").isJsonNull()) && !jsonObj.get("mulct_value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mulct_value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mulct_value").toString()));
      }
      if ((jsonObj.get("occurrence_date") != null && !jsonObj.get("occurrence_date").isJsonNull()) && !jsonObj.get("occurrence_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `occurrence_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("occurrence_date").toString()));
      }
      if ((jsonObj.get("our_number") != null && !jsonObj.get("our_number").isJsonNull()) && !jsonObj.get("our_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `our_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("our_number").toString()));
      }
      if ((jsonObj.get("payer_allegation") != null && !jsonObj.get("payer_allegation").isJsonNull()) && !jsonObj.get("payer_allegation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payer_allegation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payer_allegation").toString()));
      }
      if ((jsonObj.get("wallet") != null && !jsonObj.get("wallet").isJsonNull()) && !jsonObj.get("wallet").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `wallet` to be a primitive type in the JSON string but got `%s`", jsonObj.get("wallet").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OccurrenceAttributes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OccurrenceAttributes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OccurrenceAttributes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OccurrenceAttributes.class));

       return (TypeAdapter<T>) new TypeAdapter<OccurrenceAttributes>() {
           @Override
           public void write(JsonWriter out, OccurrenceAttributes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OccurrenceAttributes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OccurrenceAttributes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OccurrenceAttributes
   * @throws IOException if the JSON string is invalid with respect to OccurrenceAttributes
   */
  public static OccurrenceAttributes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OccurrenceAttributes.class);
  }

  /**
   * Convert an instance of OccurrenceAttributes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

