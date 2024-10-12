/*
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CompanySummary;
import org.openapitools.client.model.Score;
import org.openapitools.client.model.Status;
import org.openapitools.client.model.Summary;
import org.openapitools.client.model.VehicleSummary;
import org.openapitools.client.model.WrongInput;

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
 * Represents a background check
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Check {
  public static final String SERIALIZED_NAME_BIRTH_CERTIFICATE = "birth_certificate";
  @SerializedName(SERIALIZED_NAME_BIRTH_CERTIFICATE)
  private String birthCertificate;

  public static final String SERIALIZED_NAME_CHECK_ID = "check_id";
  @SerializedName(SERIALIZED_NAME_CHECK_ID)
  private String checkId;

  public static final String SERIALIZED_NAME_COMPANY_SUMMARY = "company_summary";
  @SerializedName(SERIALIZED_NAME_COMPANY_SUMMARY)
  private CompanySummary companySummary;

  /**
   * ID Document country
   */
  @JsonAdapter(CountryEnum.Adapter.class)
  public enum CountryEnum {
    ALL("ALL"),
    
    BR("BR"),
    
    CL("CL"),
    
    CO("CO"),
    
    CR("CR"),
    
    EC("EC"),
    
    MX("MX"),
    
    PE("PE"),
    
    AR("AR");

    private String value;

    CountryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CountryEnum fromValue(String value) {
      for (CountryEnum b : CountryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CountryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CountryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CountryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CountryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CountryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private CountryEnum country;

  public static final String SERIALIZED_NAME_CREATION_DATE = "creation_date";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private OffsetDateTime creationDate;

  public static final String SERIALIZED_NAME_DATE_OF_BIRTH = "date_of_birth";
  @SerializedName(SERIALIZED_NAME_DATE_OF_BIRTH)
  private OffsetDateTime dateOfBirth;

  public static final String SERIALIZED_NAME_DIPLOMATIC_ID = "diplomatic_id";
  @SerializedName(SERIALIZED_NAME_DIPLOMATIC_ID)
  private String diplomaticId;

  public static final String SERIALIZED_NAME_DRIVER_LICENSE = "driver_license";
  @SerializedName(SERIALIZED_NAME_DRIVER_LICENSE)
  private String driverLicense;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_FOREIGN_ID = "foreign_id";
  @SerializedName(SERIALIZED_NAME_FOREIGN_ID)
  private String foreignId;

  public static final String SERIALIZED_NAME_HOMONYM_PROBABILITY = "homonym_probability";
  @SerializedName(SERIALIZED_NAME_HOMONYM_PROBABILITY)
  private Float homonymProbability;

  public static final String SERIALIZED_NAME_HOMONYM_SCORE = "homonym_score";
  @SerializedName(SERIALIZED_NAME_HOMONYM_SCORE)
  private Float homonymScore;

  public static final String SERIALIZED_NAME_HOMONYM_SCORES = "homonym_scores";
  @SerializedName(SERIALIZED_NAME_HOMONYM_SCORES)
  private List<Score> homonymScores = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID_SCORE = "id_score";
  @SerializedName(SERIALIZED_NAME_ID_SCORE)
  private Float idScore;

  public static final String SERIALIZED_NAME_ISSUE_DATE = "issue_date";
  @SerializedName(SERIALIZED_NAME_ISSUE_DATE)
  private OffsetDateTime issueDate;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_LICENSE_PLATE = "license_plate";
  @SerializedName(SERIALIZED_NAME_LICENSE_PLATE)
  private String licensePlate;

  public static final String SERIALIZED_NAME_NATIONAL_ID = "national_id";
  @SerializedName(SERIALIZED_NAME_NATIONAL_ID)
  private String nationalId;

  /**
   * Person origin country
   */
  @JsonAdapter(NativeCountryEnum.Adapter.class)
  public enum NativeCountryEnum {
    AD("ad"),
    
    AE("ae"),
    
    AF("af"),
    
    AG("ag"),
    
    AI("ai"),
    
    AL("al"),
    
    AM("am"),
    
    AN("an"),
    
    AO("ao"),
    
    AQ("aq"),
    
    AR("ar"),
    
    AS("as"),
    
    AT("at"),
    
    AU("au"),
    
    AW("aw"),
    
    AX("ax"),
    
    AZ("az"),
    
    BA("ba"),
    
    BB("bb"),
    
    BD("bd"),
    
    BE("be"),
    
    BF("bf"),
    
    BG("bg"),
    
    BH("bh"),
    
    BI("bi"),
    
    BJ("bj"),
    
    BM("bm"),
    
    BN("bn"),
    
    BO("bo"),
    
    BR("br"),
    
    BS("bs"),
    
    BT("bt"),
    
    BV("bv"),
    
    BW("bw"),
    
    BY("by"),
    
    BZ("bz"),
    
    CA("ca"),
    
    CC("cc"),
    
    CD("cd"),
    
    CF("cf"),
    
    CG("cg"),
    
    CH("ch"),
    
    CI("ci"),
    
    CK("ck"),
    
    CL("cl"),
    
    CM("cm"),
    
    CN("cn"),
    
    CO("co"),
    
    CR("cr"),
    
    CU("cu"),
    
    CV("cv"),
    
    CX("cx"),
    
    CY("cy"),
    
    CZ("cz"),
    
    DE("de"),
    
    DJ("dj"),
    
    DK("dk"),
    
    DM("dm"),
    
    DO("do"),
    
    DZ("dz"),
    
    EA("ea"),
    
    EC("ec"),
    
    EE("ee"),
    
    EG("eg"),
    
    EH("eh"),
    
    ER("er"),
    
    ES("es"),
    
    ET("et"),
    
    FI("fi"),
    
    FJ("fj"),
    
    FK("fk"),
    
    FM("fm"),
    
    FO("fo"),
    
    FR("fr"),
    
    GA("ga"),
    
    GB("gb"),
    
    GD("gd"),
    
    GE("ge"),
    
    GF("gf"),
    
    GG("gg"),
    
    GH("gh"),
    
    GI("gi"),
    
    GL("gl"),
    
    GM("gm"),
    
    GN("gn"),
    
    GP("gp"),
    
    GQ("gq"),
    
    GR("gr"),
    
    GS("gs"),
    
    GT("gt"),
    
    GU("gu"),
    
    GW("gw"),
    
    GY("gy"),
    
    HK("hk"),
    
    HM("hm"),
    
    HN("hn"),
    
    HR("hr"),
    
    HT("ht"),
    
    HU("hu"),
    
    ID("id"),
    
    IE("ie"),
    
    IL("il"),
    
    IM("im"),
    
    IN("in"),
    
    IO("io"),
    
    IQ("iq"),
    
    IR("ir"),
    
    IS("is"),
    
    IT("it"),
    
    JE("je"),
    
    JM("jm"),
    
    JO("jo"),
    
    JP("jp"),
    
    KE("ke"),
    
    KG("kg"),
    
    KH("kh"),
    
    KI("ki"),
    
    KM("km"),
    
    KN("kn"),
    
    KP("kp"),
    
    KR("kr"),
    
    KW("kw"),
    
    KY("ky"),
    
    KZ("kz"),
    
    LA("la"),
    
    LB("lb"),
    
    LC("lc"),
    
    LI("li"),
    
    LK("lk"),
    
    LR("lr"),
    
    LS("ls"),
    
    LT("lt"),
    
    LU("lu"),
    
    LV("lv"),
    
    LY("ly"),
    
    MA("ma"),
    
    MC("mc"),
    
    MD("md"),
    
    ME("me"),
    
    MG("mg"),
    
    MH("mh"),
    
    MK("mk"),
    
    ML("ml"),
    
    MM("mm"),
    
    MN("mn"),
    
    MO("mo"),
    
    MP("mp"),
    
    MQ("mq"),
    
    MR("mr"),
    
    MS("ms"),
    
    MT("mt"),
    
    MU("mu"),
    
    MV("mv"),
    
    MW("mw"),
    
    MX("mx"),
    
    MY("my"),
    
    MZ("mz"),
    
    NA("na"),
    
    NC("nc"),
    
    NE("ne"),
    
    NF("nf"),
    
    NG("ng"),
    
    NI("ni"),
    
    NL("nl"),
    
    FALSE("false"),
    
    NP("np"),
    
    NR("nr"),
    
    NU("nu"),
    
    NZ("nz"),
    
    OM("om"),
    
    PA("pa"),
    
    PE("pe"),
    
    PF("pf"),
    
    PG("pg"),
    
    PH("ph"),
    
    PK("pk"),
    
    PL("pl"),
    
    PM("pm"),
    
    PN("pn"),
    
    PR("pr"),
    
    PS("ps"),
    
    PT("pt"),
    
    PW("pw"),
    
    PY("py"),
    
    QA("qa"),
    
    RE("re"),
    
    RO("ro"),
    
    RS("rs"),
    
    RU("ru"),
    
    RW("rw"),
    
    SA("sa"),
    
    SB("sb"),
    
    SC("sc"),
    
    SD("sd"),
    
    SE("se"),
    
    SG("sg"),
    
    SH("sh"),
    
    SI("si"),
    
    SJ("sj"),
    
    SK("sk"),
    
    SL("sl"),
    
    SM("sm"),
    
    SN("sn"),
    
    SO("so"),
    
    SR("sr"),
    
    ST("st"),
    
    SV("sv"),
    
    SY("sy"),
    
    SZ("sz"),
    
    TC("tc"),
    
    TD("td"),
    
    TF("tf"),
    
    TG("tg"),
    
    TH("th"),
    
    TJ("tj"),
    
    TK("tk"),
    
    TL("tl"),
    
    TM("tm"),
    
    TN("tn"),
    
    TO("to"),
    
    TR("tr"),
    
    TT("tt"),
    
    TV("tv"),
    
    TW("tw"),
    
    TZ("tz"),
    
    UA("ua"),
    
    UG("ug"),
    
    UM("um"),
    
    US("us"),
    
    UY("uy"),
    
    UZ("uz"),
    
    VA("va"),
    
    VC("vc"),
    
    VE("ve"),
    
    VG("vg"),
    
    VI("vi"),
    
    VN("vn"),
    
    VU("vu"),
    
    WF("wf"),
    
    WS("ws"),
    
    YE("ye"),
    
    YT("yt"),
    
    ZA("za"),
    
    ZM("zm"),
    
    ZW("zw");

    private String value;

    NativeCountryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NativeCountryEnum fromValue(String value) {
      for (NativeCountryEnum b : NativeCountryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NativeCountryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NativeCountryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NativeCountryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NativeCountryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NativeCountryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NATIVE_COUNTRY = "native_country";
  @SerializedName(SERIALIZED_NAME_NATIVE_COUNTRY)
  private NativeCountryEnum nativeCountry;

  public static final String SERIALIZED_NAME_OWNER_DOCUMENT_ID = "owner_document_id";
  @SerializedName(SERIALIZED_NAME_OWNER_DOCUMENT_ID)
  private String ownerDocumentId;

  public static final String SERIALIZED_NAME_OWNER_DOCUMENT_TYPE = "owner_document_type";
  @SerializedName(SERIALIZED_NAME_OWNER_DOCUMENT_TYPE)
  private String ownerDocumentType;

  public static final String SERIALIZED_NAME_PASSPORT = "passport";
  @SerializedName(SERIALIZED_NAME_PASSPORT)
  private String passport;

  public static final String SERIALIZED_NAME_PAYMENT_DATE = "payment_date";
  @SerializedName(SERIALIZED_NAME_PAYMENT_DATE)
  private String paymentDate;

  public static final String SERIALIZED_NAME_PEP = "pep";
  @SerializedName(SERIALIZED_NAME_PEP)
  private String pep;

  public static final String SERIALIZED_NAME_PHONE_NUMBER = "phone_number";
  @SerializedName(SERIALIZED_NAME_PHONE_NUMBER)
  private String phoneNumber;

  public static final String SERIALIZED_NAME_PROFESSIONAL_CARD = "professional_card";
  @SerializedName(SERIALIZED_NAME_PROFESSIONAL_CARD)
  private String professionalCard;

  public static final String SERIALIZED_NAME_PTP = "ptp";
  @SerializedName(SERIALIZED_NAME_PTP)
  private String ptp;

  /**
   * Region where the background is to be checked. By default, background checks in Brazil are performed in region where the person is from. Applies for some Brazil collectors only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.  
   */
  @JsonAdapter(RegionEnum.Adapter.class)
  public enum RegionEnum {
    DF("DF"),
    
    AC("AC"),
    
    AL("AL"),
    
    AP("AP"),
    
    AM("AM"),
    
    BA("BA"),
    
    CE("CE"),
    
    ES("ES"),
    
    GO("GO"),
    
    MA("MA"),
    
    MT("MT"),
    
    MS("MS"),
    
    MG("MG"),
    
    PA("PA"),
    
    PB("PB"),
    
    PR("PR"),
    
    PE("PE"),
    
    PI("PI"),
    
    RJ("RJ"),
    
    RN("RN"),
    
    RS("RS"),
    
    RO("RO"),
    
    RR("RR"),
    
    SC("SC"),
    
    SP("SP"),
    
    SE("SE"),
    
    TO("TO");

    private String value;

    RegionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RegionEnum fromValue(String value) {
      for (RegionEnum b : RegionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RegionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RegionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RegionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RegionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RegionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private RegionEnum region;

  public static final String SERIALIZED_NAME_REPORT_ID = "report_id";
  @SerializedName(SERIALIZED_NAME_REPORT_ID)
  private String reportId;

  public static final String SERIALIZED_NAME_SCORE = "score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Float score;

  public static final String SERIALIZED_NAME_SCORES = "scores";
  @SerializedName(SERIALIZED_NAME_SCORES)
  private List<Score> scores = new ArrayList<>();

  /**
   * Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the check finished successfully, **error** means the check failed, **in_progress** means the check is currently being processed, **delayed** means the check is waiting for an additional requirement to be met, this can last up to 3 days. **Completed** and **error** are the two only final statuses
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    NOT_STARTED("not_started"),
    
    IN_PROGRESS("in_progress"),
    
    COMPLETED("completed"),
    
    ERROR("error"),
    
    DELAYED("delayed");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_STATUSES = "statuses";
  @SerializedName(SERIALIZED_NAME_STATUSES)
  private List<Status> statuses = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUMMARY = "summary";
  @SerializedName(SERIALIZED_NAME_SUMMARY)
  private Summary summary;

  public static final String SERIALIZED_NAME_TAX_ID = "tax_id";
  @SerializedName(SERIALIZED_NAME_TAX_ID)
  private String taxId;

  /**
   * Background check type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    COMPANY("company"),
    
    PERSON("person"),
    
    VEHICLE("vehicle");

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

  public static final String SERIALIZED_NAME_UPDATE_DATE = "update_date";
  @SerializedName(SERIALIZED_NAME_UPDATE_DATE)
  private OffsetDateTime updateDate;

  public static final String SERIALIZED_NAME_VEHICLE_ID = "vehicle_id";
  @SerializedName(SERIALIZED_NAME_VEHICLE_ID)
  private String vehicleId;

  public static final String SERIALIZED_NAME_VEHICLE_SUMMARY = "vehicle_summary";
  @SerializedName(SERIALIZED_NAME_VEHICLE_SUMMARY)
  private VehicleSummary vehicleSummary;

  public static final String SERIALIZED_NAME_WRONG_INPUTS = "wrong_inputs";
  @SerializedName(SERIALIZED_NAME_WRONG_INPUTS)
  private List<WrongInput> wrongInputs = new ArrayList<>();

  public Check() {
  }

  public Check birthCertificate(String birthCertificate) {
    this.birthCertificate = birthCertificate;
    return this;
  }

  /**
   * Person birth certificate
   * @return birthCertificate
   */
  @javax.annotation.Nullable
  public String getBirthCertificate() {
    return birthCertificate;
  }

  public void setBirthCertificate(String birthCertificate) {
    this.birthCertificate = birthCertificate;
  }


  public Check checkId(String checkId) {
    this.checkId = checkId;
    return this;
  }

  /**
   * Background check ID
   * @return checkId
   */
  @javax.annotation.Nonnull
  public String getCheckId() {
    return checkId;
  }

  public void setCheckId(String checkId) {
    this.checkId = checkId;
  }


  public Check companySummary(CompanySummary companySummary) {
    this.companySummary = companySummary;
    return this;
  }

  /**
   * Get companySummary
   * @return companySummary
   */
  @javax.annotation.Nullable
  public CompanySummary getCompanySummary() {
    return companySummary;
  }

  public void setCompanySummary(CompanySummary companySummary) {
    this.companySummary = companySummary;
  }


  public Check country(CountryEnum country) {
    this.country = country;
    return this;
  }

  /**
   * ID Document country
   * @return country
   */
  @javax.annotation.Nonnull
  public CountryEnum getCountry() {
    return country;
  }

  public void setCountry(CountryEnum country) {
    this.country = country;
  }


  public Check creationDate(OffsetDateTime creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * Background check creation date
   * @return creationDate
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(OffsetDateTime creationDate) {
    this.creationDate = creationDate;
  }


  public Check dateOfBirth(OffsetDateTime dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
    return this;
  }

  /**
   * Person birthdate. Shown only if provided during check creation. YYYY-MM-DD format
   * @return dateOfBirth
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateOfBirth() {
    return dateOfBirth;
  }

  public void setDateOfBirth(OffsetDateTime dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }


  public Check diplomaticId(String diplomaticId) {
    this.diplomaticId = diplomaticId;
    return this;
  }

  /**
   * Person diplomatic id
   * @return diplomaticId
   */
  @javax.annotation.Nullable
  public String getDiplomaticId() {
    return diplomaticId;
  }

  public void setDiplomaticId(String diplomaticId) {
    this.diplomaticId = diplomaticId;
  }


  public Check driverLicense(String driverLicense) {
    this.driverLicense = driverLicense;
    return this;
  }

  /**
   * Person driver&#39;s license
   * @return driverLicense
   */
  @javax.annotation.Nullable
  public String getDriverLicense() {
    return driverLicense;
  }

  public void setDriverLicense(String driverLicense) {
    this.driverLicense = driverLicense;
  }


  public Check firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * Person or entity first name. Shown only if provided during check creation
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public Check foreignId(String foreignId) {
    this.foreignId = foreignId;
    return this;
  }

  /**
   * Person foreign identification
   * @return foreignId
   */
  @javax.annotation.Nullable
  public String getForeignId() {
    return foreignId;
  }

  public void setForeignId(String foreignId) {
    this.foreignId = foreignId;
  }


  public Check homonymProbability(Float homonymProbability) {
    this.homonymProbability = homonymProbability;
    return this;
  }

  /**
   * [Experimental] Analyzes the probability that the results by name are attributed to a homonym. Number between 0 and 1 where 1 is the the greatest probability
   * @return homonymProbability
   */
  @javax.annotation.Nullable
  public Float getHomonymProbability() {
    return homonymProbability;
  }

  public void setHomonymProbability(Float homonymProbability) {
    this.homonymProbability = homonymProbability;
  }


  public Check homonymScore(Float homonymScore) {
    this.homonymScore = homonymScore;
    return this;
  }

  /**
   * Background check score including results by name only. This might contain homonym information
   * minimum: 0
   * maximum: 1
   * @return homonymScore
   */
  @javax.annotation.Nullable
  public Float getHomonymScore() {
    return homonymScore;
  }

  public void setHomonymScore(Float homonymScore) {
    this.homonymScore = homonymScore;
  }


  public Check homonymScores(List<Score> homonymScores) {
    this.homonymScores = homonymScores;
    return this;
  }

  public Check addHomonymScoresItem(Score homonymScoresItem) {
    if (this.homonymScores == null) {
      this.homonymScores = new ArrayList<>();
    }
    this.homonymScores.add(homonymScoresItem);
    return this;
  }

  /**
   * Background check scores by name for each profile group. [Deprecated for API key V1]
   * @return homonymScores
   */
  @javax.annotation.Nullable
  public List<Score> getHomonymScores() {
    return homonymScores;
  }

  public void setHomonymScores(List<Score> homonymScores) {
    this.homonymScores = homonymScores;
  }


  public Check idScore(Float idScore) {
    this.idScore = idScore;
    return this;
  }

  /**
   * Background check score regarding results by ID number only. It is a number between 0 and 1 where 1 is the best score. This result is a weighted average of the id_scores listed under scores.
   * @return idScore
   */
  @javax.annotation.Nonnull
  public Float getIdScore() {
    return idScore;
  }

  public void setIdScore(Float idScore) {
    this.idScore = idScore;
  }


  public Check issueDate(OffsetDateTime issueDate) {
    this.issueDate = issueDate;
    return this;
  }

  /**
   * Issue date of the person ID
   * @return issueDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getIssueDate() {
    return issueDate;
  }

  public void setIssueDate(OffsetDateTime issueDate) {
    this.issueDate = issueDate;
  }


  public Check lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * Person or entity last name. Shown only if provided during check creation
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public Check licensePlate(String licensePlate) {
    this.licensePlate = licensePlate;
    return this;
  }

  /**
   * Vehicle license plate
   * @return licensePlate
   */
  @javax.annotation.Nullable
  public String getLicensePlate() {
    return licensePlate;
  }

  public void setLicensePlate(String licensePlate) {
    this.licensePlate = licensePlate;
  }


  public Check nationalId(String nationalId) {
    this.nationalId = nationalId;
    return this;
  }

  /**
   * Person national identification
   * @return nationalId
   */
  @javax.annotation.Nullable
  public String getNationalId() {
    return nationalId;
  }

  public void setNationalId(String nationalId) {
    this.nationalId = nationalId;
  }


  public Check nativeCountry(NativeCountryEnum nativeCountry) {
    this.nativeCountry = nativeCountry;
    return this;
  }

  /**
   * Person origin country
   * @return nativeCountry
   */
  @javax.annotation.Nullable
  public NativeCountryEnum getNativeCountry() {
    return nativeCountry;
  }

  public void setNativeCountry(NativeCountryEnum nativeCountry) {
    this.nativeCountry = nativeCountry;
  }


  public Check ownerDocumentId(String ownerDocumentId) {
    this.ownerDocumentId = ownerDocumentId;
    return this;
  }

  /**
   * Vehicle owner identification
   * @return ownerDocumentId
   */
  @javax.annotation.Nullable
  public String getOwnerDocumentId() {
    return ownerDocumentId;
  }

  public void setOwnerDocumentId(String ownerDocumentId) {
    this.ownerDocumentId = ownerDocumentId;
  }


  public Check ownerDocumentType(String ownerDocumentType) {
    this.ownerDocumentType = ownerDocumentType;
    return this;
  }

  /**
   * Vehicle owner document type
   * @return ownerDocumentType
   */
  @javax.annotation.Nullable
  public String getOwnerDocumentType() {
    return ownerDocumentType;
  }

  public void setOwnerDocumentType(String ownerDocumentType) {
    this.ownerDocumentType = ownerDocumentType;
  }


  public Check passport(String passport) {
    this.passport = passport;
    return this;
  }

  /**
   * Person passport
   * @return passport
   */
  @javax.annotation.Nullable
  public String getPassport() {
    return passport;
  }

  public void setPassport(String passport) {
    this.passport = passport;
  }


  public Check paymentDate(String paymentDate) {
    this.paymentDate = paymentDate;
    return this;
  }

  /**
   * Vehicle license payment date
   * @return paymentDate
   */
  @javax.annotation.Nullable
  public String getPaymentDate() {
    return paymentDate;
  }

  public void setPaymentDate(String paymentDate) {
    this.paymentDate = paymentDate;
  }


  public Check pep(String pep) {
    this.pep = pep;
    return this;
  }

  /**
   * Colombian PEP idenfitication for Venezuelans
   * @return pep
   */
  @javax.annotation.Nullable
  public String getPep() {
    return pep;
  }

  public void setPep(String pep) {
    this.pep = pep;
  }


  public Check phoneNumber(String phoneNumber) {
    this.phoneNumber = phoneNumber;
    return this;
  }

  /**
   * Person phone number. Required by law in order to notify the person their background is being checked
   * @return phoneNumber
   */
  @javax.annotation.Nullable
  public String getPhoneNumber() {
    return phoneNumber;
  }

  public void setPhoneNumber(String phoneNumber) {
    this.phoneNumber = phoneNumber;
  }


  public Check professionalCard(String professionalCard) {
    this.professionalCard = professionalCard;
    return this;
  }

  /**
   * Person professional card number
   * @return professionalCard
   */
  @javax.annotation.Nullable
  public String getProfessionalCard() {
    return professionalCard;
  }

  public void setProfessionalCard(String professionalCard) {
    this.professionalCard = professionalCard;
  }


  public Check ptp(String ptp) {
    this.ptp = ptp;
    return this;
  }

  /**
   * Temporary residence permit of the person
   * @return ptp
   */
  @javax.annotation.Nullable
  public String getPtp() {
    return ptp;
  }

  public void setPtp(String ptp) {
    this.ptp = ptp;
  }


  public Check region(RegionEnum region) {
    this.region = region;
    return this;
  }

  /**
   * Region where the background is to be checked. By default, background checks in Brazil are performed in region where the person is from. Applies for some Brazil collectors only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.  
   * @return region
   */
  @javax.annotation.Nullable
  public RegionEnum getRegion() {
    return region;
  }

  public void setRegion(RegionEnum region) {
    this.region = region;
  }


  public Check reportId(String reportId) {
    this.reportId = reportId;
    return this;
  }

  /**
   * Report ID the background check is associated with
   * @return reportId
   */
  @javax.annotation.Nullable
  public String getReportId() {
    return reportId;
  }

  public void setReportId(String reportId) {
    this.reportId = reportId;
  }


  public Check score(Float score) {
    this.score = score;
    return this;
  }

  /**
   * Background check score. Number between 0 and 1 where 1 is the best score
   * minimum: 0
   * maximum: 1
   * @return score
   */
  @javax.annotation.Nonnull
  public Float getScore() {
    return score;
  }

  public void setScore(Float score) {
    this.score = score;
  }


  public Check scores(List<Score> scores) {
    this.scores = scores;
    return this;
  }

  public Check addScoresItem(Score scoresItem) {
    if (this.scores == null) {
      this.scores = new ArrayList<>();
    }
    this.scores.add(scoresItem);
    return this;
  }

  /**
   * Background check score of each profile group and dataset
   * @return scores
   */
  @javax.annotation.Nullable
  public List<Score> getScores() {
    return scores;
  }

  public void setScores(List<Score> scores) {
    this.scores = scores;
  }


  public Check status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the check finished successfully, **error** means the check failed, **in_progress** means the check is currently being processed, **delayed** means the check is waiting for an additional requirement to be met, this can last up to 3 days. **Completed** and **error** are the two only final statuses
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public Check statuses(List<Status> statuses) {
    this.statuses = statuses;
    return this;
  }

  public Check addStatusesItem(Status statusesItem) {
    if (this.statuses == null) {
      this.statuses = new ArrayList<>();
    }
    this.statuses.add(statusesItem);
    return this;
  }

  /**
   * Database status list
   * @return statuses
   */
  @javax.annotation.Nonnull
  public List<Status> getStatuses() {
    return statuses;
  }

  public void setStatuses(List<Status> statuses) {
    this.statuses = statuses;
  }


  public Check summary(Summary summary) {
    this.summary = summary;
    return this;
  }

  /**
   * Get summary
   * @return summary
   */
  @javax.annotation.Nonnull
  public Summary getSummary() {
    return summary;
  }

  public void setSummary(Summary summary) {
    this.summary = summary;
  }


  public Check taxId(String taxId) {
    this.taxId = taxId;
    return this;
  }

  /**
   * Person or company tax id
   * @return taxId
   */
  @javax.annotation.Nullable
  public String getTaxId() {
    return taxId;
  }

  public void setTaxId(String taxId) {
    this.taxId = taxId;
  }


  public Check type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Background check type
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public Check updateDate(OffsetDateTime updateDate) {
    this.updateDate = updateDate;
    return this;
  }

  /**
   * Background check update date
   * @return updateDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdateDate() {
    return updateDate;
  }

  public void setUpdateDate(OffsetDateTime updateDate) {
    this.updateDate = updateDate;
  }


  public Check vehicleId(String vehicleId) {
    this.vehicleId = vehicleId;
    return this;
  }

  /**
   * Vehicle identification
   * @return vehicleId
   */
  @javax.annotation.Nullable
  public String getVehicleId() {
    return vehicleId;
  }

  public void setVehicleId(String vehicleId) {
    this.vehicleId = vehicleId;
  }


  public Check vehicleSummary(VehicleSummary vehicleSummary) {
    this.vehicleSummary = vehicleSummary;
    return this;
  }

  /**
   * Get vehicleSummary
   * @return vehicleSummary
   */
  @javax.annotation.Nullable
  public VehicleSummary getVehicleSummary() {
    return vehicleSummary;
  }

  public void setVehicleSummary(VehicleSummary vehicleSummary) {
    this.vehicleSummary = vehicleSummary;
  }


  public Check wrongInputs(List<WrongInput> wrongInputs) {
    this.wrongInputs = wrongInputs;
    return this;
  }

  public Check addWrongInputsItem(WrongInput wrongInputsItem) {
    if (this.wrongInputs == null) {
      this.wrongInputs = new ArrayList<>();
    }
    this.wrongInputs.add(wrongInputsItem);
    return this;
  }

  /**
   * List of parameters entered during background check creation that do not match the information obtained
   * @return wrongInputs
   */
  @javax.annotation.Nullable
  public List<WrongInput> getWrongInputs() {
    return wrongInputs;
  }

  public void setWrongInputs(List<WrongInput> wrongInputs) {
    this.wrongInputs = wrongInputs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Check check = (Check) o;
    return Objects.equals(this.birthCertificate, check.birthCertificate) &&
        Objects.equals(this.checkId, check.checkId) &&
        Objects.equals(this.companySummary, check.companySummary) &&
        Objects.equals(this.country, check.country) &&
        Objects.equals(this.creationDate, check.creationDate) &&
        Objects.equals(this.dateOfBirth, check.dateOfBirth) &&
        Objects.equals(this.diplomaticId, check.diplomaticId) &&
        Objects.equals(this.driverLicense, check.driverLicense) &&
        Objects.equals(this.firstName, check.firstName) &&
        Objects.equals(this.foreignId, check.foreignId) &&
        Objects.equals(this.homonymProbability, check.homonymProbability) &&
        Objects.equals(this.homonymScore, check.homonymScore) &&
        Objects.equals(this.homonymScores, check.homonymScores) &&
        Objects.equals(this.idScore, check.idScore) &&
        Objects.equals(this.issueDate, check.issueDate) &&
        Objects.equals(this.lastName, check.lastName) &&
        Objects.equals(this.licensePlate, check.licensePlate) &&
        Objects.equals(this.nationalId, check.nationalId) &&
        Objects.equals(this.nativeCountry, check.nativeCountry) &&
        Objects.equals(this.ownerDocumentId, check.ownerDocumentId) &&
        Objects.equals(this.ownerDocumentType, check.ownerDocumentType) &&
        Objects.equals(this.passport, check.passport) &&
        Objects.equals(this.paymentDate, check.paymentDate) &&
        Objects.equals(this.pep, check.pep) &&
        Objects.equals(this.phoneNumber, check.phoneNumber) &&
        Objects.equals(this.professionalCard, check.professionalCard) &&
        Objects.equals(this.ptp, check.ptp) &&
        Objects.equals(this.region, check.region) &&
        Objects.equals(this.reportId, check.reportId) &&
        Objects.equals(this.score, check.score) &&
        Objects.equals(this.scores, check.scores) &&
        Objects.equals(this.status, check.status) &&
        Objects.equals(this.statuses, check.statuses) &&
        Objects.equals(this.summary, check.summary) &&
        Objects.equals(this.taxId, check.taxId) &&
        Objects.equals(this.type, check.type) &&
        Objects.equals(this.updateDate, check.updateDate) &&
        Objects.equals(this.vehicleId, check.vehicleId) &&
        Objects.equals(this.vehicleSummary, check.vehicleSummary) &&
        Objects.equals(this.wrongInputs, check.wrongInputs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(birthCertificate, checkId, companySummary, country, creationDate, dateOfBirth, diplomaticId, driverLicense, firstName, foreignId, homonymProbability, homonymScore, homonymScores, idScore, issueDate, lastName, licensePlate, nationalId, nativeCountry, ownerDocumentId, ownerDocumentType, passport, paymentDate, pep, phoneNumber, professionalCard, ptp, region, reportId, score, scores, status, statuses, summary, taxId, type, updateDate, vehicleId, vehicleSummary, wrongInputs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Check {\n");
    sb.append("    birthCertificate: ").append(toIndentedString(birthCertificate)).append("\n");
    sb.append("    checkId: ").append(toIndentedString(checkId)).append("\n");
    sb.append("    companySummary: ").append(toIndentedString(companySummary)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    dateOfBirth: ").append(toIndentedString(dateOfBirth)).append("\n");
    sb.append("    diplomaticId: ").append(toIndentedString(diplomaticId)).append("\n");
    sb.append("    driverLicense: ").append(toIndentedString(driverLicense)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    foreignId: ").append(toIndentedString(foreignId)).append("\n");
    sb.append("    homonymProbability: ").append(toIndentedString(homonymProbability)).append("\n");
    sb.append("    homonymScore: ").append(toIndentedString(homonymScore)).append("\n");
    sb.append("    homonymScores: ").append(toIndentedString(homonymScores)).append("\n");
    sb.append("    idScore: ").append(toIndentedString(idScore)).append("\n");
    sb.append("    issueDate: ").append(toIndentedString(issueDate)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    licensePlate: ").append(toIndentedString(licensePlate)).append("\n");
    sb.append("    nationalId: ").append(toIndentedString(nationalId)).append("\n");
    sb.append("    nativeCountry: ").append(toIndentedString(nativeCountry)).append("\n");
    sb.append("    ownerDocumentId: ").append(toIndentedString(ownerDocumentId)).append("\n");
    sb.append("    ownerDocumentType: ").append(toIndentedString(ownerDocumentType)).append("\n");
    sb.append("    passport: ").append(toIndentedString(passport)).append("\n");
    sb.append("    paymentDate: ").append(toIndentedString(paymentDate)).append("\n");
    sb.append("    pep: ").append(toIndentedString(pep)).append("\n");
    sb.append("    phoneNumber: ").append(toIndentedString(phoneNumber)).append("\n");
    sb.append("    professionalCard: ").append(toIndentedString(professionalCard)).append("\n");
    sb.append("    ptp: ").append(toIndentedString(ptp)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    reportId: ").append(toIndentedString(reportId)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    scores: ").append(toIndentedString(scores)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statuses: ").append(toIndentedString(statuses)).append("\n");
    sb.append("    summary: ").append(toIndentedString(summary)).append("\n");
    sb.append("    taxId: ").append(toIndentedString(taxId)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updateDate: ").append(toIndentedString(updateDate)).append("\n");
    sb.append("    vehicleId: ").append(toIndentedString(vehicleId)).append("\n");
    sb.append("    vehicleSummary: ").append(toIndentedString(vehicleSummary)).append("\n");
    sb.append("    wrongInputs: ").append(toIndentedString(wrongInputs)).append("\n");
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
    openapiFields.add("birth_certificate");
    openapiFields.add("check_id");
    openapiFields.add("company_summary");
    openapiFields.add("country");
    openapiFields.add("creation_date");
    openapiFields.add("date_of_birth");
    openapiFields.add("diplomatic_id");
    openapiFields.add("driver_license");
    openapiFields.add("first_name");
    openapiFields.add("foreign_id");
    openapiFields.add("homonym_probability");
    openapiFields.add("homonym_score");
    openapiFields.add("homonym_scores");
    openapiFields.add("id_score");
    openapiFields.add("issue_date");
    openapiFields.add("last_name");
    openapiFields.add("license_plate");
    openapiFields.add("national_id");
    openapiFields.add("native_country");
    openapiFields.add("owner_document_id");
    openapiFields.add("owner_document_type");
    openapiFields.add("passport");
    openapiFields.add("payment_date");
    openapiFields.add("pep");
    openapiFields.add("phone_number");
    openapiFields.add("professional_card");
    openapiFields.add("ptp");
    openapiFields.add("region");
    openapiFields.add("report_id");
    openapiFields.add("score");
    openapiFields.add("scores");
    openapiFields.add("status");
    openapiFields.add("statuses");
    openapiFields.add("summary");
    openapiFields.add("tax_id");
    openapiFields.add("type");
    openapiFields.add("update_date");
    openapiFields.add("vehicle_id");
    openapiFields.add("vehicle_summary");
    openapiFields.add("wrong_inputs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("check_id");
    openapiRequiredFields.add("country");
    openapiRequiredFields.add("creation_date");
    openapiRequiredFields.add("id_score");
    openapiRequiredFields.add("score");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("statuses");
    openapiRequiredFields.add("summary");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Check
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Check.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Check is not found in the empty JSON string", Check.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Check.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Check` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Check.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("birth_certificate") != null && !jsonObj.get("birth_certificate").isJsonNull()) && !jsonObj.get("birth_certificate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `birth_certificate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("birth_certificate").toString()));
      }
      if (!jsonObj.get("check_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `check_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("check_id").toString()));
      }
      // validate the optional field `company_summary`
      if (jsonObj.get("company_summary") != null && !jsonObj.get("company_summary").isJsonNull()) {
        CompanySummary.validateJsonElement(jsonObj.get("company_summary"));
      }
      if (!jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      // validate the required field `country`
      CountryEnum.validateJsonElement(jsonObj.get("country"));
      if ((jsonObj.get("diplomatic_id") != null && !jsonObj.get("diplomatic_id").isJsonNull()) && !jsonObj.get("diplomatic_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `diplomatic_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("diplomatic_id").toString()));
      }
      if ((jsonObj.get("driver_license") != null && !jsonObj.get("driver_license").isJsonNull()) && !jsonObj.get("driver_license").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `driver_license` to be a primitive type in the JSON string but got `%s`", jsonObj.get("driver_license").toString()));
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      if ((jsonObj.get("foreign_id") != null && !jsonObj.get("foreign_id").isJsonNull()) && !jsonObj.get("foreign_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `foreign_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("foreign_id").toString()));
      }
      if (jsonObj.get("homonym_scores") != null && !jsonObj.get("homonym_scores").isJsonNull()) {
        JsonArray jsonArrayhomonymScores = jsonObj.getAsJsonArray("homonym_scores");
        if (jsonArrayhomonymScores != null) {
          // ensure the json data is an array
          if (!jsonObj.get("homonym_scores").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `homonym_scores` to be an array in the JSON string but got `%s`", jsonObj.get("homonym_scores").toString()));
          }

          // validate the optional field `homonym_scores` (array)
          for (int i = 0; i < jsonArrayhomonymScores.size(); i++) {
            Score.validateJsonElement(jsonArrayhomonymScores.get(i));
          };
        }
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("license_plate") != null && !jsonObj.get("license_plate").isJsonNull()) && !jsonObj.get("license_plate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `license_plate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("license_plate").toString()));
      }
      if ((jsonObj.get("national_id") != null && !jsonObj.get("national_id").isJsonNull()) && !jsonObj.get("national_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `national_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("national_id").toString()));
      }
      if ((jsonObj.get("native_country") != null && !jsonObj.get("native_country").isJsonNull()) && !jsonObj.get("native_country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `native_country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("native_country").toString()));
      }
      // validate the optional field `native_country`
      if (jsonObj.get("native_country") != null && !jsonObj.get("native_country").isJsonNull()) {
        NativeCountryEnum.validateJsonElement(jsonObj.get("native_country"));
      }
      if ((jsonObj.get("owner_document_id") != null && !jsonObj.get("owner_document_id").isJsonNull()) && !jsonObj.get("owner_document_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner_document_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner_document_id").toString()));
      }
      if ((jsonObj.get("owner_document_type") != null && !jsonObj.get("owner_document_type").isJsonNull()) && !jsonObj.get("owner_document_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner_document_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner_document_type").toString()));
      }
      if ((jsonObj.get("passport") != null && !jsonObj.get("passport").isJsonNull()) && !jsonObj.get("passport").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `passport` to be a primitive type in the JSON string but got `%s`", jsonObj.get("passport").toString()));
      }
      if ((jsonObj.get("payment_date") != null && !jsonObj.get("payment_date").isJsonNull()) && !jsonObj.get("payment_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_date").toString()));
      }
      if ((jsonObj.get("pep") != null && !jsonObj.get("pep").isJsonNull()) && !jsonObj.get("pep").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pep` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pep").toString()));
      }
      if ((jsonObj.get("phone_number") != null && !jsonObj.get("phone_number").isJsonNull()) && !jsonObj.get("phone_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone_number").toString()));
      }
      if ((jsonObj.get("professional_card") != null && !jsonObj.get("professional_card").isJsonNull()) && !jsonObj.get("professional_card").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `professional_card` to be a primitive type in the JSON string but got `%s`", jsonObj.get("professional_card").toString()));
      }
      if ((jsonObj.get("ptp") != null && !jsonObj.get("ptp").isJsonNull()) && !jsonObj.get("ptp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ptp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ptp").toString()));
      }
      if ((jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) && !jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      // validate the optional field `region`
      if (jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) {
        RegionEnum.validateJsonElement(jsonObj.get("region"));
      }
      if ((jsonObj.get("report_id") != null && !jsonObj.get("report_id").isJsonNull()) && !jsonObj.get("report_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `report_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("report_id").toString()));
      }
      if (jsonObj.get("scores") != null && !jsonObj.get("scores").isJsonNull()) {
        JsonArray jsonArrayscores = jsonObj.getAsJsonArray("scores");
        if (jsonArrayscores != null) {
          // ensure the json data is an array
          if (!jsonObj.get("scores").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `scores` to be an array in the JSON string but got `%s`", jsonObj.get("scores").toString()));
          }

          // validate the optional field `scores` (array)
          for (int i = 0; i < jsonArrayscores.size(); i++) {
            Score.validateJsonElement(jsonArrayscores.get(i));
          };
        }
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      // ensure the json data is an array
      if (!jsonObj.get("statuses").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `statuses` to be an array in the JSON string but got `%s`", jsonObj.get("statuses").toString()));
      }

      JsonArray jsonArraystatuses = jsonObj.getAsJsonArray("statuses");
      // validate the required field `statuses` (array)
      for (int i = 0; i < jsonArraystatuses.size(); i++) {
        Status.validateJsonElement(jsonArraystatuses.get(i));
      };
      // validate the required field `summary`
      Summary.validateJsonElement(jsonObj.get("summary"));
      if ((jsonObj.get("tax_id") != null && !jsonObj.get("tax_id").isJsonNull()) && !jsonObj.get("tax_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_id").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
      if ((jsonObj.get("vehicle_id") != null && !jsonObj.get("vehicle_id").isJsonNull()) && !jsonObj.get("vehicle_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vehicle_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vehicle_id").toString()));
      }
      // validate the optional field `vehicle_summary`
      if (jsonObj.get("vehicle_summary") != null && !jsonObj.get("vehicle_summary").isJsonNull()) {
        VehicleSummary.validateJsonElement(jsonObj.get("vehicle_summary"));
      }
      if (jsonObj.get("wrong_inputs") != null && !jsonObj.get("wrong_inputs").isJsonNull()) {
        JsonArray jsonArraywrongInputs = jsonObj.getAsJsonArray("wrong_inputs");
        if (jsonArraywrongInputs != null) {
          // ensure the json data is an array
          if (!jsonObj.get("wrong_inputs").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `wrong_inputs` to be an array in the JSON string but got `%s`", jsonObj.get("wrong_inputs").toString()));
          }

          // validate the optional field `wrong_inputs` (array)
          for (int i = 0; i < jsonArraywrongInputs.size(); i++) {
            WrongInput.validateJsonElement(jsonArraywrongInputs.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Check.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Check' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Check> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Check.class));

       return (TypeAdapter<T>) new TypeAdapter<Check>() {
           @Override
           public void write(JsonWriter out, Check value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Check read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Check given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Check
   * @throws IOException if the JSON string is invalid with respect to Check
   */
  public static Check fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Check.class);
  }

  /**
   * Convert an instance of Check to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

