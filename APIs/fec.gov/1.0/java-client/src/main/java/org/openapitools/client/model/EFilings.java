/*
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
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
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * EFilings
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:12.812386-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EFilings {
  public static final String SERIALIZED_NAME_AMENDED_BY = "amended_by";
  @SerializedName(SERIALIZED_NAME_AMENDED_BY)
  private Integer amendedBy;

  public static final String SERIALIZED_NAME_AMENDMENT_CHAIN = "amendment_chain";
  @SerializedName(SERIALIZED_NAME_AMENDMENT_CHAIN)
  private List<Integer> amendmentChain = new ArrayList<>();

  public static final String SERIALIZED_NAME_AMENDMENT_NUMBER = "amendment_number";
  @SerializedName(SERIALIZED_NAME_AMENDMENT_NUMBER)
  private Integer amendmentNumber;

  public static final String SERIALIZED_NAME_AMENDS_FILE = "amends_file";
  @SerializedName(SERIALIZED_NAME_AMENDS_FILE)
  private Integer amendsFile;

  public static final String SERIALIZED_NAME_BEGINNING_IMAGE_NUMBER = "beginning_image_number";
  @SerializedName(SERIALIZED_NAME_BEGINNING_IMAGE_NUMBER)
  private String beginningImageNumber;

  public static final String SERIALIZED_NAME_COMMITTEE_ID = "committee_id";
  @SerializedName(SERIALIZED_NAME_COMMITTEE_ID)
  private String committeeId;

  public static final String SERIALIZED_NAME_COMMITTEE_NAME = "committee_name";
  @SerializedName(SERIALIZED_NAME_COMMITTEE_NAME)
  private String committeeName;

  public static final String SERIALIZED_NAME_COVERAGE_END_DATE = "coverage_end_date";
  @SerializedName(SERIALIZED_NAME_COVERAGE_END_DATE)
  private LocalDate coverageEndDate;

  public static final String SERIALIZED_NAME_COVERAGE_START_DATE = "coverage_start_date";
  @SerializedName(SERIALIZED_NAME_COVERAGE_START_DATE)
  private LocalDate coverageStartDate;

  public static final String SERIALIZED_NAME_CSV_URL = "csv_url";
  @SerializedName(SERIALIZED_NAME_CSV_URL)
  private String csvUrl;

  public static final String SERIALIZED_NAME_DOCUMENT_DESCRIPTION = "document_description";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_DESCRIPTION)
  private String documentDescription;

  public static final String SERIALIZED_NAME_ENDING_IMAGE_NUMBER = "ending_image_number";
  @SerializedName(SERIALIZED_NAME_ENDING_IMAGE_NUMBER)
  private String endingImageNumber;

  public static final String SERIALIZED_NAME_FEC_FILE_ID = "fec_file_id";
  @SerializedName(SERIALIZED_NAME_FEC_FILE_ID)
  private String fecFileId;

  public static final String SERIALIZED_NAME_FEC_URL = "fec_url";
  @SerializedName(SERIALIZED_NAME_FEC_URL)
  private String fecUrl;

  public static final String SERIALIZED_NAME_FILE_NUMBER = "file_number";
  @SerializedName(SERIALIZED_NAME_FILE_NUMBER)
  private Integer fileNumber;

  public static final String SERIALIZED_NAME_FILED_DATE = "filed_date";
  @SerializedName(SERIALIZED_NAME_FILED_DATE)
  private LocalDate filedDate;

  public static final String SERIALIZED_NAME_FORM_TYPE = "form_type";
  @SerializedName(SERIALIZED_NAME_FORM_TYPE)
  private String formType;

  public static final String SERIALIZED_NAME_HTML_URL = "html_url";
  @SerializedName(SERIALIZED_NAME_HTML_URL)
  private String htmlUrl;

  public static final String SERIALIZED_NAME_IS_AMENDED = "is_amended";
  @SerializedName(SERIALIZED_NAME_IS_AMENDED)
  private Boolean isAmended;

  public static final String SERIALIZED_NAME_LOAD_TIMESTAMP = "load_timestamp";
  @SerializedName(SERIALIZED_NAME_LOAD_TIMESTAMP)
  private OffsetDateTime loadTimestamp;

  public static final String SERIALIZED_NAME_MOST_RECENT = "most_recent";
  @SerializedName(SERIALIZED_NAME_MOST_RECENT)
  private Boolean mostRecent;

  public static final String SERIALIZED_NAME_MOST_RECENT_FILING = "most_recent_filing";
  @SerializedName(SERIALIZED_NAME_MOST_RECENT_FILING)
  private Integer mostRecentFiling;

  public static final String SERIALIZED_NAME_PDF_URL = "pdf_url";
  @SerializedName(SERIALIZED_NAME_PDF_URL)
  private String pdfUrl;

  public static final String SERIALIZED_NAME_RECEIPT_DATE = "receipt_date";
  @SerializedName(SERIALIZED_NAME_RECEIPT_DATE)
  private OffsetDateTime receiptDate;

  public EFilings() {
  }

  public EFilings amendedBy(Integer amendedBy) {
    this.amendedBy = amendedBy;
    return this;
  }

  /**
   * Get amendedBy
   * @return amendedBy
   */
  @javax.annotation.Nullable
  public Integer getAmendedBy() {
    return amendedBy;
  }

  public void setAmendedBy(Integer amendedBy) {
    this.amendedBy = amendedBy;
  }


  public EFilings amendmentChain(List<Integer> amendmentChain) {
    this.amendmentChain = amendmentChain;
    return this;
  }

  public EFilings addAmendmentChainItem(Integer amendmentChainItem) {
    if (this.amendmentChain == null) {
      this.amendmentChain = new ArrayList<>();
    }
    this.amendmentChain.add(amendmentChainItem);
    return this;
  }

  /**
   * Get amendmentChain
   * @return amendmentChain
   */
  @javax.annotation.Nullable
  public List<Integer> getAmendmentChain() {
    return amendmentChain;
  }

  public void setAmendmentChain(List<Integer> amendmentChain) {
    this.amendmentChain = amendmentChain;
  }


  public EFilings amendmentNumber(Integer amendmentNumber) {
    this.amendmentNumber = amendmentNumber;
    return this;
  }

  /**
   *  Number of times the report has been amended. 
   * @return amendmentNumber
   */
  @javax.annotation.Nullable
  public Integer getAmendmentNumber() {
    return amendmentNumber;
  }

  public void setAmendmentNumber(Integer amendmentNumber) {
    this.amendmentNumber = amendmentNumber;
  }


  public EFilings amendsFile(Integer amendsFile) {
    this.amendsFile = amendsFile;
    return this;
  }

  /**
   *  For amendments, this file_number is the file_number of the previous report that is being amended. Refer to the amended_by for the most recent version of the report. 
   * @return amendsFile
   */
  @javax.annotation.Nullable
  public Integer getAmendsFile() {
    return amendsFile;
  }

  public void setAmendsFile(Integer amendsFile) {
    this.amendsFile = amendsFile;
  }


  public EFilings beginningImageNumber(String beginningImageNumber) {
    this.beginningImageNumber = beginningImageNumber;
    return this;
  }

  /**
   * Get beginningImageNumber
   * @return beginningImageNumber
   */
  @javax.annotation.Nullable
  public String getBeginningImageNumber() {
    return beginningImageNumber;
  }

  public void setBeginningImageNumber(String beginningImageNumber) {
    this.beginningImageNumber = beginningImageNumber;
  }


  public EFilings committeeId(String committeeId) {
    this.committeeId = committeeId;
    return this;
  }

  /**
   *  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits. 
   * @return committeeId
   */
  @javax.annotation.Nullable
  public String getCommitteeId() {
    return committeeId;
  }

  public void setCommitteeId(String committeeId) {
    this.committeeId = committeeId;
  }


  public EFilings committeeName(String committeeName) {
    this.committeeName = committeeName;
    return this;
  }

  /**
   * The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records.
   * @return committeeName
   */
  @javax.annotation.Nullable
  public String getCommitteeName() {
    return committeeName;
  }

  public void setCommitteeName(String committeeName) {
    this.committeeName = committeeName;
  }


  public EFilings coverageEndDate(LocalDate coverageEndDate) {
    this.coverageEndDate = coverageEndDate;
    return this;
  }

  /**
   * Ending date of the reporting period
   * @return coverageEndDate
   */
  @javax.annotation.Nullable
  public LocalDate getCoverageEndDate() {
    return coverageEndDate;
  }

  public void setCoverageEndDate(LocalDate coverageEndDate) {
    this.coverageEndDate = coverageEndDate;
  }


  public EFilings coverageStartDate(LocalDate coverageStartDate) {
    this.coverageStartDate = coverageStartDate;
    return this;
  }

  /**
   * Beginning date of the reporting period
   * @return coverageStartDate
   */
  @javax.annotation.Nullable
  public LocalDate getCoverageStartDate() {
    return coverageStartDate;
  }

  public void setCoverageStartDate(LocalDate coverageStartDate) {
    this.coverageStartDate = coverageStartDate;
  }


  public EFilings csvUrl(String csvUrl) {
    this.csvUrl = csvUrl;
    return this;
  }

  /**
   * Get csvUrl
   * @return csvUrl
   */
  @javax.annotation.Nullable
  public String getCsvUrl() {
    return csvUrl;
  }

  public void setCsvUrl(String csvUrl) {
    this.csvUrl = csvUrl;
  }


  public EFilings documentDescription(String documentDescription) {
    this.documentDescription = documentDescription;
    return this;
  }

  /**
   * Get documentDescription
   * @return documentDescription
   */
  @javax.annotation.Nullable
  public String getDocumentDescription() {
    return documentDescription;
  }

  public void setDocumentDescription(String documentDescription) {
    this.documentDescription = documentDescription;
  }


  public EFilings endingImageNumber(String endingImageNumber) {
    this.endingImageNumber = endingImageNumber;
    return this;
  }

  /**
   * Get endingImageNumber
   * @return endingImageNumber
   */
  @javax.annotation.Nullable
  public String getEndingImageNumber() {
    return endingImageNumber;
  }

  public void setEndingImageNumber(String endingImageNumber) {
    this.endingImageNumber = endingImageNumber;
  }


  public EFilings fecFileId(String fecFileId) {
    this.fecFileId = fecFileId;
    return this;
  }

  /**
   * Get fecFileId
   * @return fecFileId
   */
  @javax.annotation.Nullable
  public String getFecFileId() {
    return fecFileId;
  }

  public void setFecFileId(String fecFileId) {
    this.fecFileId = fecFileId;
  }


  public EFilings fecUrl(String fecUrl) {
    this.fecUrl = fecUrl;
    return this;
  }

  /**
   * Get fecUrl
   * @return fecUrl
   */
  @javax.annotation.Nullable
  public String getFecUrl() {
    return fecUrl;
  }

  public void setFecUrl(String fecUrl) {
    this.fecUrl = fecUrl;
  }


  public EFilings fileNumber(Integer fileNumber) {
    this.fileNumber = fileNumber;
    return this;
  }

  /**
   * Filing ID number
   * @return fileNumber
   */
  @javax.annotation.Nullable
  public Integer getFileNumber() {
    return fileNumber;
  }

  public void setFileNumber(Integer fileNumber) {
    this.fileNumber = fileNumber;
  }


  public EFilings filedDate(LocalDate filedDate) {
    this.filedDate = filedDate;
    return this;
  }

  /**
   * Timestamp of electronic or paper record that FEC received
   * @return filedDate
   */
  @javax.annotation.Nullable
  public LocalDate getFiledDate() {
    return filedDate;
  }

  public void setFiledDate(LocalDate filedDate) {
    this.filedDate = filedDate;
  }


  public EFilings formType(String formType) {
    this.formType = formType;
    return this;
  }

  /**
   * The form where the underlying data comes from, for example, Form 1 would appear as F1:     - F1   Statement of Organization     - F1M  Notification of Multicandidate Status     - F2   Statement of Candidacy     - F3   Report of Receipts and Disbursements for an Authorized Committee     - F3P  Report of Receipts and Disbursements by an Authorized Committee of a Candidate for     The Office of President or Vice President     - F3L  Report of Contributions Bundled by Lobbyists/Registrants and Lobbyist/Registrant PACs     - F3X  Report of Receipts and Disbursements for other than an Authorized Committee     - F4   Report of Receipts and Disbursements for a Committee or Organization Supporting a Nomination Convention     - F5   Report of Independent Expenditures Made and Contributions Received     - F6   48 Hour Notice of Contributions/Loans Received     - F7   Report of Communication Costs by Corporations and Membership Organizations     - F8   Debt Settlement Plan     - F9   24 Hour Notice of Disbursements for Electioneering Communications     - F13  Report of Donations Accepted for Inaugural Committee     - F99  Miscellaneous Text     - FRQ  Request for Additional Information 
   * @return formType
   */
  @javax.annotation.Nullable
  public String getFormType() {
    return formType;
  }

  public void setFormType(String formType) {
    this.formType = formType;
  }


  public EFilings htmlUrl(String htmlUrl) {
    this.htmlUrl = htmlUrl;
    return this;
  }

  /**
   * Get htmlUrl
   * @return htmlUrl
   */
  @javax.annotation.Nullable
  public String getHtmlUrl() {
    return htmlUrl;
  }

  public void setHtmlUrl(String htmlUrl) {
    this.htmlUrl = htmlUrl;
  }


  public EFilings isAmended(Boolean isAmended) {
    this.isAmended = isAmended;
    return this;
  }

  /**
   * Get isAmended
   * @return isAmended
   */
  @javax.annotation.Nullable
  public Boolean getIsAmended() {
    return isAmended;
  }

  public void setIsAmended(Boolean isAmended) {
    this.isAmended = isAmended;
  }


  public EFilings loadTimestamp(OffsetDateTime loadTimestamp) {
    this.loadTimestamp = loadTimestamp;
    return this;
  }

  /**
   * Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently.
   * @return loadTimestamp
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLoadTimestamp() {
    return loadTimestamp;
  }

  public void setLoadTimestamp(OffsetDateTime loadTimestamp) {
    this.loadTimestamp = loadTimestamp;
  }


  public EFilings mostRecent(Boolean mostRecent) {
    this.mostRecent = mostRecent;
    return this;
  }

  /**
   * Get mostRecent
   * @return mostRecent
   */
  @javax.annotation.Nullable
  public Boolean getMostRecent() {
    return mostRecent;
  }

  public void setMostRecent(Boolean mostRecent) {
    this.mostRecent = mostRecent;
  }


  public EFilings mostRecentFiling(Integer mostRecentFiling) {
    this.mostRecentFiling = mostRecentFiling;
    return this;
  }

  /**
   * Get mostRecentFiling
   * @return mostRecentFiling
   */
  @javax.annotation.Nullable
  public Integer getMostRecentFiling() {
    return mostRecentFiling;
  }

  public void setMostRecentFiling(Integer mostRecentFiling) {
    this.mostRecentFiling = mostRecentFiling;
  }


  public EFilings pdfUrl(String pdfUrl) {
    this.pdfUrl = pdfUrl;
    return this;
  }

  /**
   * Get pdfUrl
   * @return pdfUrl
   */
  @javax.annotation.Nullable
  public String getPdfUrl() {
    return pdfUrl;
  }

  public void setPdfUrl(String pdfUrl) {
    this.pdfUrl = pdfUrl;
  }


  public EFilings receiptDate(OffsetDateTime receiptDate) {
    this.receiptDate = receiptDate;
    return this;
  }

  /**
   * Date the FEC received the electronic or paper record
   * @return receiptDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getReceiptDate() {
    return receiptDate;
  }

  public void setReceiptDate(OffsetDateTime receiptDate) {
    this.receiptDate = receiptDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EFilings efilings = (EFilings) o;
    return Objects.equals(this.amendedBy, efilings.amendedBy) &&
        Objects.equals(this.amendmentChain, efilings.amendmentChain) &&
        Objects.equals(this.amendmentNumber, efilings.amendmentNumber) &&
        Objects.equals(this.amendsFile, efilings.amendsFile) &&
        Objects.equals(this.beginningImageNumber, efilings.beginningImageNumber) &&
        Objects.equals(this.committeeId, efilings.committeeId) &&
        Objects.equals(this.committeeName, efilings.committeeName) &&
        Objects.equals(this.coverageEndDate, efilings.coverageEndDate) &&
        Objects.equals(this.coverageStartDate, efilings.coverageStartDate) &&
        Objects.equals(this.csvUrl, efilings.csvUrl) &&
        Objects.equals(this.documentDescription, efilings.documentDescription) &&
        Objects.equals(this.endingImageNumber, efilings.endingImageNumber) &&
        Objects.equals(this.fecFileId, efilings.fecFileId) &&
        Objects.equals(this.fecUrl, efilings.fecUrl) &&
        Objects.equals(this.fileNumber, efilings.fileNumber) &&
        Objects.equals(this.filedDate, efilings.filedDate) &&
        Objects.equals(this.formType, efilings.formType) &&
        Objects.equals(this.htmlUrl, efilings.htmlUrl) &&
        Objects.equals(this.isAmended, efilings.isAmended) &&
        Objects.equals(this.loadTimestamp, efilings.loadTimestamp) &&
        Objects.equals(this.mostRecent, efilings.mostRecent) &&
        Objects.equals(this.mostRecentFiling, efilings.mostRecentFiling) &&
        Objects.equals(this.pdfUrl, efilings.pdfUrl) &&
        Objects.equals(this.receiptDate, efilings.receiptDate);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(amendedBy, amendmentChain, amendmentNumber, amendsFile, beginningImageNumber, committeeId, committeeName, coverageEndDate, coverageStartDate, csvUrl, documentDescription, endingImageNumber, fecFileId, fecUrl, fileNumber, filedDate, formType, htmlUrl, isAmended, loadTimestamp, mostRecent, mostRecentFiling, pdfUrl, receiptDate);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EFilings {\n");
    sb.append("    amendedBy: ").append(toIndentedString(amendedBy)).append("\n");
    sb.append("    amendmentChain: ").append(toIndentedString(amendmentChain)).append("\n");
    sb.append("    amendmentNumber: ").append(toIndentedString(amendmentNumber)).append("\n");
    sb.append("    amendsFile: ").append(toIndentedString(amendsFile)).append("\n");
    sb.append("    beginningImageNumber: ").append(toIndentedString(beginningImageNumber)).append("\n");
    sb.append("    committeeId: ").append(toIndentedString(committeeId)).append("\n");
    sb.append("    committeeName: ").append(toIndentedString(committeeName)).append("\n");
    sb.append("    coverageEndDate: ").append(toIndentedString(coverageEndDate)).append("\n");
    sb.append("    coverageStartDate: ").append(toIndentedString(coverageStartDate)).append("\n");
    sb.append("    csvUrl: ").append(toIndentedString(csvUrl)).append("\n");
    sb.append("    documentDescription: ").append(toIndentedString(documentDescription)).append("\n");
    sb.append("    endingImageNumber: ").append(toIndentedString(endingImageNumber)).append("\n");
    sb.append("    fecFileId: ").append(toIndentedString(fecFileId)).append("\n");
    sb.append("    fecUrl: ").append(toIndentedString(fecUrl)).append("\n");
    sb.append("    fileNumber: ").append(toIndentedString(fileNumber)).append("\n");
    sb.append("    filedDate: ").append(toIndentedString(filedDate)).append("\n");
    sb.append("    formType: ").append(toIndentedString(formType)).append("\n");
    sb.append("    htmlUrl: ").append(toIndentedString(htmlUrl)).append("\n");
    sb.append("    isAmended: ").append(toIndentedString(isAmended)).append("\n");
    sb.append("    loadTimestamp: ").append(toIndentedString(loadTimestamp)).append("\n");
    sb.append("    mostRecent: ").append(toIndentedString(mostRecent)).append("\n");
    sb.append("    mostRecentFiling: ").append(toIndentedString(mostRecentFiling)).append("\n");
    sb.append("    pdfUrl: ").append(toIndentedString(pdfUrl)).append("\n");
    sb.append("    receiptDate: ").append(toIndentedString(receiptDate)).append("\n");
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
    openapiFields.add("amended_by");
    openapiFields.add("amendment_chain");
    openapiFields.add("amendment_number");
    openapiFields.add("amends_file");
    openapiFields.add("beginning_image_number");
    openapiFields.add("committee_id");
    openapiFields.add("committee_name");
    openapiFields.add("coverage_end_date");
    openapiFields.add("coverage_start_date");
    openapiFields.add("csv_url");
    openapiFields.add("document_description");
    openapiFields.add("ending_image_number");
    openapiFields.add("fec_file_id");
    openapiFields.add("fec_url");
    openapiFields.add("file_number");
    openapiFields.add("filed_date");
    openapiFields.add("form_type");
    openapiFields.add("html_url");
    openapiFields.add("is_amended");
    openapiFields.add("load_timestamp");
    openapiFields.add("most_recent");
    openapiFields.add("most_recent_filing");
    openapiFields.add("pdf_url");
    openapiFields.add("receipt_date");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EFilings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EFilings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EFilings is not found in the empty JSON string", EFilings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EFilings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EFilings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("amendment_chain") != null && !jsonObj.get("amendment_chain").isJsonNull() && !jsonObj.get("amendment_chain").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `amendment_chain` to be an array in the JSON string but got `%s`", jsonObj.get("amendment_chain").toString()));
      }
      if ((jsonObj.get("beginning_image_number") != null && !jsonObj.get("beginning_image_number").isJsonNull()) && !jsonObj.get("beginning_image_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `beginning_image_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("beginning_image_number").toString()));
      }
      if ((jsonObj.get("committee_id") != null && !jsonObj.get("committee_id").isJsonNull()) && !jsonObj.get("committee_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `committee_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("committee_id").toString()));
      }
      if ((jsonObj.get("committee_name") != null && !jsonObj.get("committee_name").isJsonNull()) && !jsonObj.get("committee_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `committee_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("committee_name").toString()));
      }
      if ((jsonObj.get("csv_url") != null && !jsonObj.get("csv_url").isJsonNull()) && !jsonObj.get("csv_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `csv_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("csv_url").toString()));
      }
      if ((jsonObj.get("document_description") != null && !jsonObj.get("document_description").isJsonNull()) && !jsonObj.get("document_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `document_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("document_description").toString()));
      }
      if ((jsonObj.get("ending_image_number") != null && !jsonObj.get("ending_image_number").isJsonNull()) && !jsonObj.get("ending_image_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ending_image_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ending_image_number").toString()));
      }
      if ((jsonObj.get("fec_file_id") != null && !jsonObj.get("fec_file_id").isJsonNull()) && !jsonObj.get("fec_file_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fec_file_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fec_file_id").toString()));
      }
      if ((jsonObj.get("fec_url") != null && !jsonObj.get("fec_url").isJsonNull()) && !jsonObj.get("fec_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fec_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fec_url").toString()));
      }
      if ((jsonObj.get("form_type") != null && !jsonObj.get("form_type").isJsonNull()) && !jsonObj.get("form_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `form_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("form_type").toString()));
      }
      if ((jsonObj.get("html_url") != null && !jsonObj.get("html_url").isJsonNull()) && !jsonObj.get("html_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `html_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("html_url").toString()));
      }
      if ((jsonObj.get("pdf_url") != null && !jsonObj.get("pdf_url").isJsonNull()) && !jsonObj.get("pdf_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pdf_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pdf_url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EFilings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EFilings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EFilings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EFilings.class));

       return (TypeAdapter<T>) new TypeAdapter<EFilings>() {
           @Override
           public void write(JsonWriter out, EFilings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EFilings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EFilings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EFilings
   * @throws IOException if the JSON string is invalid with respect to EFilings
   */
  public static EFilings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EFilings.class);
  }

  /**
   * Convert an instance of EFilings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

