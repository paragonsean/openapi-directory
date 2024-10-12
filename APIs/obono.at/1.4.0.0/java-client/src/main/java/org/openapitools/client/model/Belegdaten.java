/*
 * obono RKSV API
 * Provides a RESTful API for interacting with virtual cash registers and creating receipts that are conform with the Registrierkassensicherheitsverordnung (RKSV).  You may find our [automatically generated clients](./clients) for various programming languages and environments helpful... 
 *
 * The version of the OpenAPI document: 1.4.0.0
 * Contact: info@obono.at
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
import java.util.UUID;
import org.openapitools.client.model.Posten;
import org.openapitools.client.model.Rabatt;
import org.openapitools.client.model.Zahlung;

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
 * The &#x60;Beleg&#x60; to be signed by the \&quot;Signaturerstellungseinheit\&quot; and stored in the \&quot;Datenerfassungsprotokoll\&quot;.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:42.053838-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Belegdaten {
  public static final String SERIALIZED_NAME_EXTERNER_BELEG_BELEGKREIS = "Externer-Beleg-Belegkreis";
  @SerializedName(SERIALIZED_NAME_EXTERNER_BELEG_BELEGKREIS)
  private String externerBelegBelegkreis;

  public static final String SERIALIZED_NAME_EXTERNER_BELEG_BEZEICHNUNG = "Externer-Beleg-Bezeichnung";
  @SerializedName(SERIALIZED_NAME_EXTERNER_BELEG_BEZEICHNUNG)
  private String externerBelegBezeichnung;

  public static final String SERIALIZED_NAME_EXTERNER_BELEG_REFERENZ = "Externer-Beleg-Referenz";
  @SerializedName(SERIALIZED_NAME_EXTERNER_BELEG_REFERENZ)
  private String externerBelegReferenz;

  public static final String SERIALIZED_NAME_KUNDE = "Kunde";
  @SerializedName(SERIALIZED_NAME_KUNDE)
  private String kunde;

  public static final String SERIALIZED_NAME_NOTIZEN = "Notizen";
  @SerializedName(SERIALIZED_NAME_NOTIZEN)
  private List<String> notizen = new ArrayList<>();

  public static final String SERIALIZED_NAME_POSTEN = "Posten";
  @SerializedName(SERIALIZED_NAME_POSTEN)
  private List<Posten> posten = new ArrayList<>();

  public static final String SERIALIZED_NAME_RABATTE = "Rabatte";
  @SerializedName(SERIALIZED_NAME_RABATTE)
  private List<Rabatt> rabatte = new ArrayList<>();

  public static final String SERIALIZED_NAME_STORNO = "Storno";
  @SerializedName(SERIALIZED_NAME_STORNO)
  private Boolean storno;

  public static final String SERIALIZED_NAME_STORNO_BELEG_U_U_I_D = "Storno-Beleg-UUID";
  @SerializedName(SERIALIZED_NAME_STORNO_BELEG_U_U_I_D)
  private UUID stornoBelegUUID;

  public static final String SERIALIZED_NAME_STORNO_TEXT = "Storno-Text";
  @SerializedName(SERIALIZED_NAME_STORNO_TEXT)
  private String stornoText;

  public static final String SERIALIZED_NAME_TRAINING = "Training";
  @SerializedName(SERIALIZED_NAME_TRAINING)
  private Boolean training;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_ADRESSE1 = "Unternehmen-Adresse1";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_ADRESSE1)
  private String unternehmenAdresse1;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_ADRESSE2 = "Unternehmen-Adresse2";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_ADRESSE2)
  private String unternehmenAdresse2;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_FUSSZEILE = "Unternehmen-Fusszeile";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_FUSSZEILE)
  private String unternehmenFusszeile;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_I_D = "Unternehmen-ID";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_I_D)
  private String unternehmenID;

  /**
   * Gets or Sets unternehmenIDTyp
   */
  @JsonAdapter(UnternehmenIDTypEnum.Adapter.class)
  public enum UnternehmenIDTypEnum {
    STEUERNUMMER("steuernummer"),
    
    UID("uid"),
    
    GLN("gln");

    private String value;

    UnternehmenIDTypEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static UnternehmenIDTypEnum fromValue(String value) {
      for (UnternehmenIDTypEnum b : UnternehmenIDTypEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<UnternehmenIDTypEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final UnternehmenIDTypEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public UnternehmenIDTypEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return UnternehmenIDTypEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      UnternehmenIDTypEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_UNTERNEHMEN_I_D_TYP = "Unternehmen-ID-Typ";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_I_D_TYP)
  private UnternehmenIDTypEnum unternehmenIDTyp;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_KOPFZEILE = "Unternehmen-Kopfzeile";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_KOPFZEILE)
  private String unternehmenKopfzeile;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_NAME = "Unternehmen-Name";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_NAME)
  private String unternehmenName;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_ORT = "Unternehmen-Ort";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_ORT)
  private String unternehmenOrt;

  public static final String SERIALIZED_NAME_UNTERNEHMEN_P_L_Z = "Unternehmen-PLZ";
  @SerializedName(SERIALIZED_NAME_UNTERNEHMEN_P_L_Z)
  private String unternehmenPLZ;

  public static final String SERIALIZED_NAME_ZAHLUNGEN = "Zahlungen";
  @SerializedName(SERIALIZED_NAME_ZAHLUNGEN)
  private List<Zahlung> zahlungen = new ArrayList<>();

  public Belegdaten() {
  }

  public Belegdaten externerBelegBelegkreis(String externerBelegBelegkreis) {
    this.externerBelegBelegkreis = externerBelegBelegkreis;
    return this;
  }

  /**
   * Get externerBelegBelegkreis
   * @return externerBelegBelegkreis
   */
  @javax.annotation.Nullable
  public String getExternerBelegBelegkreis() {
    return externerBelegBelegkreis;
  }

  public void setExternerBelegBelegkreis(String externerBelegBelegkreis) {
    this.externerBelegBelegkreis = externerBelegBelegkreis;
  }


  public Belegdaten externerBelegBezeichnung(String externerBelegBezeichnung) {
    this.externerBelegBezeichnung = externerBelegBezeichnung;
    return this;
  }

  /**
   * Get externerBelegBezeichnung
   * @return externerBelegBezeichnung
   */
  @javax.annotation.Nullable
  public String getExternerBelegBezeichnung() {
    return externerBelegBezeichnung;
  }

  public void setExternerBelegBezeichnung(String externerBelegBezeichnung) {
    this.externerBelegBezeichnung = externerBelegBezeichnung;
  }


  public Belegdaten externerBelegReferenz(String externerBelegReferenz) {
    this.externerBelegReferenz = externerBelegReferenz;
    return this;
  }

  /**
   * Get externerBelegReferenz
   * @return externerBelegReferenz
   */
  @javax.annotation.Nullable
  public String getExternerBelegReferenz() {
    return externerBelegReferenz;
  }

  public void setExternerBelegReferenz(String externerBelegReferenz) {
    this.externerBelegReferenz = externerBelegReferenz;
  }


  public Belegdaten kunde(String kunde) {
    this.kunde = kunde;
    return this;
  }

  /**
   * Get kunde
   * @return kunde
   */
  @javax.annotation.Nullable
  public String getKunde() {
    return kunde;
  }

  public void setKunde(String kunde) {
    this.kunde = kunde;
  }


  public Belegdaten notizen(List<String> notizen) {
    this.notizen = notizen;
    return this;
  }

  public Belegdaten addNotizenItem(String notizenItem) {
    if (this.notizen == null) {
      this.notizen = new ArrayList<>();
    }
    this.notizen.add(notizenItem);
    return this;
  }

  /**
   * Get notizen
   * @return notizen
   */
  @javax.annotation.Nullable
  public List<String> getNotizen() {
    return notizen;
  }

  public void setNotizen(List<String> notizen) {
    this.notizen = notizen;
  }


  public Belegdaten posten(List<Posten> posten) {
    this.posten = posten;
    return this;
  }

  public Belegdaten addPostenItem(Posten postenItem) {
    if (this.posten == null) {
      this.posten = new ArrayList<>();
    }
    this.posten.add(postenItem);
    return this;
  }

  /**
   * Get posten
   * @return posten
   */
  @javax.annotation.Nullable
  public List<Posten> getPosten() {
    return posten;
  }

  public void setPosten(List<Posten> posten) {
    this.posten = posten;
  }


  public Belegdaten rabatte(List<Rabatt> rabatte) {
    this.rabatte = rabatte;
    return this;
  }

  public Belegdaten addRabatteItem(Rabatt rabatteItem) {
    if (this.rabatte == null) {
      this.rabatte = new ArrayList<>();
    }
    this.rabatte.add(rabatteItem);
    return this;
  }

  /**
   * Get rabatte
   * @return rabatte
   */
  @javax.annotation.Nullable
  public List<Rabatt> getRabatte() {
    return rabatte;
  }

  public void setRabatte(List<Rabatt> rabatte) {
    this.rabatte = rabatte;
  }


  public Belegdaten storno(Boolean storno) {
    this.storno = storno;
    return this;
  }

  /**
   * Storno?
   * @return storno
   */
  @javax.annotation.Nullable
  public Boolean getStorno() {
    return storno;
  }

  public void setStorno(Boolean storno) {
    this.storno = storno;
  }


  public Belegdaten stornoBelegUUID(UUID stornoBelegUUID) {
    this.stornoBelegUUID = stornoBelegUUID;
    return this;
  }

  /**
   * The &#x60;Beleg-UUID&#x60; property of the &#x60;Beleg&#x60; to be cancelled
   * @return stornoBelegUUID
   */
  @javax.annotation.Nullable
  public UUID getStornoBelegUUID() {
    return stornoBelegUUID;
  }

  public void setStornoBelegUUID(UUID stornoBelegUUID) {
    this.stornoBelegUUID = stornoBelegUUID;
  }


  public Belegdaten stornoText(String stornoText) {
    this.stornoText = stornoText;
    return this;
  }

  /**
   * Get stornoText
   * @return stornoText
   */
  @javax.annotation.Nullable
  public String getStornoText() {
    return stornoText;
  }

  public void setStornoText(String stornoText) {
    this.stornoText = stornoText;
  }


  public Belegdaten training(Boolean training) {
    this.training = training;
    return this;
  }

  /**
   * Training?
   * @return training
   */
  @javax.annotation.Nullable
  public Boolean getTraining() {
    return training;
  }

  public void setTraining(Boolean training) {
    this.training = training;
  }


  public Belegdaten unternehmenAdresse1(String unternehmenAdresse1) {
    this.unternehmenAdresse1 = unternehmenAdresse1;
    return this;
  }

  /**
   * Get unternehmenAdresse1
   * @return unternehmenAdresse1
   */
  @javax.annotation.Nullable
  public String getUnternehmenAdresse1() {
    return unternehmenAdresse1;
  }

  public void setUnternehmenAdresse1(String unternehmenAdresse1) {
    this.unternehmenAdresse1 = unternehmenAdresse1;
  }


  public Belegdaten unternehmenAdresse2(String unternehmenAdresse2) {
    this.unternehmenAdresse2 = unternehmenAdresse2;
    return this;
  }

  /**
   * Get unternehmenAdresse2
   * @return unternehmenAdresse2
   */
  @javax.annotation.Nullable
  public String getUnternehmenAdresse2() {
    return unternehmenAdresse2;
  }

  public void setUnternehmenAdresse2(String unternehmenAdresse2) {
    this.unternehmenAdresse2 = unternehmenAdresse2;
  }


  public Belegdaten unternehmenFusszeile(String unternehmenFusszeile) {
    this.unternehmenFusszeile = unternehmenFusszeile;
    return this;
  }

  /**
   * Get unternehmenFusszeile
   * @return unternehmenFusszeile
   */
  @javax.annotation.Nullable
  public String getUnternehmenFusszeile() {
    return unternehmenFusszeile;
  }

  public void setUnternehmenFusszeile(String unternehmenFusszeile) {
    this.unternehmenFusszeile = unternehmenFusszeile;
  }


  public Belegdaten unternehmenID(String unternehmenID) {
    this.unternehmenID = unternehmenID;
    return this;
  }

  /**
   * Get unternehmenID
   * @return unternehmenID
   */
  @javax.annotation.Nullable
  public String getUnternehmenID() {
    return unternehmenID;
  }

  public void setUnternehmenID(String unternehmenID) {
    this.unternehmenID = unternehmenID;
  }


  public Belegdaten unternehmenIDTyp(UnternehmenIDTypEnum unternehmenIDTyp) {
    this.unternehmenIDTyp = unternehmenIDTyp;
    return this;
  }

  /**
   * Get unternehmenIDTyp
   * @return unternehmenIDTyp
   */
  @javax.annotation.Nullable
  public UnternehmenIDTypEnum getUnternehmenIDTyp() {
    return unternehmenIDTyp;
  }

  public void setUnternehmenIDTyp(UnternehmenIDTypEnum unternehmenIDTyp) {
    this.unternehmenIDTyp = unternehmenIDTyp;
  }


  public Belegdaten unternehmenKopfzeile(String unternehmenKopfzeile) {
    this.unternehmenKopfzeile = unternehmenKopfzeile;
    return this;
  }

  /**
   * Get unternehmenKopfzeile
   * @return unternehmenKopfzeile
   */
  @javax.annotation.Nullable
  public String getUnternehmenKopfzeile() {
    return unternehmenKopfzeile;
  }

  public void setUnternehmenKopfzeile(String unternehmenKopfzeile) {
    this.unternehmenKopfzeile = unternehmenKopfzeile;
  }


  public Belegdaten unternehmenName(String unternehmenName) {
    this.unternehmenName = unternehmenName;
    return this;
  }

  /**
   * Get unternehmenName
   * @return unternehmenName
   */
  @javax.annotation.Nullable
  public String getUnternehmenName() {
    return unternehmenName;
  }

  public void setUnternehmenName(String unternehmenName) {
    this.unternehmenName = unternehmenName;
  }


  public Belegdaten unternehmenOrt(String unternehmenOrt) {
    this.unternehmenOrt = unternehmenOrt;
    return this;
  }

  /**
   * Get unternehmenOrt
   * @return unternehmenOrt
   */
  @javax.annotation.Nullable
  public String getUnternehmenOrt() {
    return unternehmenOrt;
  }

  public void setUnternehmenOrt(String unternehmenOrt) {
    this.unternehmenOrt = unternehmenOrt;
  }


  public Belegdaten unternehmenPLZ(String unternehmenPLZ) {
    this.unternehmenPLZ = unternehmenPLZ;
    return this;
  }

  /**
   * Get unternehmenPLZ
   * @return unternehmenPLZ
   */
  @javax.annotation.Nullable
  public String getUnternehmenPLZ() {
    return unternehmenPLZ;
  }

  public void setUnternehmenPLZ(String unternehmenPLZ) {
    this.unternehmenPLZ = unternehmenPLZ;
  }


  public Belegdaten zahlungen(List<Zahlung> zahlungen) {
    this.zahlungen = zahlungen;
    return this;
  }

  public Belegdaten addZahlungenItem(Zahlung zahlungenItem) {
    if (this.zahlungen == null) {
      this.zahlungen = new ArrayList<>();
    }
    this.zahlungen.add(zahlungenItem);
    return this;
  }

  /**
   * Get zahlungen
   * @return zahlungen
   */
  @javax.annotation.Nullable
  public List<Zahlung> getZahlungen() {
    return zahlungen;
  }

  public void setZahlungen(List<Zahlung> zahlungen) {
    this.zahlungen = zahlungen;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Belegdaten belegdaten = (Belegdaten) o;
    return Objects.equals(this.externerBelegBelegkreis, belegdaten.externerBelegBelegkreis) &&
        Objects.equals(this.externerBelegBezeichnung, belegdaten.externerBelegBezeichnung) &&
        Objects.equals(this.externerBelegReferenz, belegdaten.externerBelegReferenz) &&
        Objects.equals(this.kunde, belegdaten.kunde) &&
        Objects.equals(this.notizen, belegdaten.notizen) &&
        Objects.equals(this.posten, belegdaten.posten) &&
        Objects.equals(this.rabatte, belegdaten.rabatte) &&
        Objects.equals(this.storno, belegdaten.storno) &&
        Objects.equals(this.stornoBelegUUID, belegdaten.stornoBelegUUID) &&
        Objects.equals(this.stornoText, belegdaten.stornoText) &&
        Objects.equals(this.training, belegdaten.training) &&
        Objects.equals(this.unternehmenAdresse1, belegdaten.unternehmenAdresse1) &&
        Objects.equals(this.unternehmenAdresse2, belegdaten.unternehmenAdresse2) &&
        Objects.equals(this.unternehmenFusszeile, belegdaten.unternehmenFusszeile) &&
        Objects.equals(this.unternehmenID, belegdaten.unternehmenID) &&
        Objects.equals(this.unternehmenIDTyp, belegdaten.unternehmenIDTyp) &&
        Objects.equals(this.unternehmenKopfzeile, belegdaten.unternehmenKopfzeile) &&
        Objects.equals(this.unternehmenName, belegdaten.unternehmenName) &&
        Objects.equals(this.unternehmenOrt, belegdaten.unternehmenOrt) &&
        Objects.equals(this.unternehmenPLZ, belegdaten.unternehmenPLZ) &&
        Objects.equals(this.zahlungen, belegdaten.zahlungen);
  }

  @Override
  public int hashCode() {
    return Objects.hash(externerBelegBelegkreis, externerBelegBezeichnung, externerBelegReferenz, kunde, notizen, posten, rabatte, storno, stornoBelegUUID, stornoText, training, unternehmenAdresse1, unternehmenAdresse2, unternehmenFusszeile, unternehmenID, unternehmenIDTyp, unternehmenKopfzeile, unternehmenName, unternehmenOrt, unternehmenPLZ, zahlungen);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Belegdaten {\n");
    sb.append("    externerBelegBelegkreis: ").append(toIndentedString(externerBelegBelegkreis)).append("\n");
    sb.append("    externerBelegBezeichnung: ").append(toIndentedString(externerBelegBezeichnung)).append("\n");
    sb.append("    externerBelegReferenz: ").append(toIndentedString(externerBelegReferenz)).append("\n");
    sb.append("    kunde: ").append(toIndentedString(kunde)).append("\n");
    sb.append("    notizen: ").append(toIndentedString(notizen)).append("\n");
    sb.append("    posten: ").append(toIndentedString(posten)).append("\n");
    sb.append("    rabatte: ").append(toIndentedString(rabatte)).append("\n");
    sb.append("    storno: ").append(toIndentedString(storno)).append("\n");
    sb.append("    stornoBelegUUID: ").append(toIndentedString(stornoBelegUUID)).append("\n");
    sb.append("    stornoText: ").append(toIndentedString(stornoText)).append("\n");
    sb.append("    training: ").append(toIndentedString(training)).append("\n");
    sb.append("    unternehmenAdresse1: ").append(toIndentedString(unternehmenAdresse1)).append("\n");
    sb.append("    unternehmenAdresse2: ").append(toIndentedString(unternehmenAdresse2)).append("\n");
    sb.append("    unternehmenFusszeile: ").append(toIndentedString(unternehmenFusszeile)).append("\n");
    sb.append("    unternehmenID: ").append(toIndentedString(unternehmenID)).append("\n");
    sb.append("    unternehmenIDTyp: ").append(toIndentedString(unternehmenIDTyp)).append("\n");
    sb.append("    unternehmenKopfzeile: ").append(toIndentedString(unternehmenKopfzeile)).append("\n");
    sb.append("    unternehmenName: ").append(toIndentedString(unternehmenName)).append("\n");
    sb.append("    unternehmenOrt: ").append(toIndentedString(unternehmenOrt)).append("\n");
    sb.append("    unternehmenPLZ: ").append(toIndentedString(unternehmenPLZ)).append("\n");
    sb.append("    zahlungen: ").append(toIndentedString(zahlungen)).append("\n");
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
    openapiFields.add("Externer-Beleg-Belegkreis");
    openapiFields.add("Externer-Beleg-Bezeichnung");
    openapiFields.add("Externer-Beleg-Referenz");
    openapiFields.add("Kunde");
    openapiFields.add("Notizen");
    openapiFields.add("Posten");
    openapiFields.add("Rabatte");
    openapiFields.add("Storno");
    openapiFields.add("Storno-Beleg-UUID");
    openapiFields.add("Storno-Text");
    openapiFields.add("Training");
    openapiFields.add("Unternehmen-Adresse1");
    openapiFields.add("Unternehmen-Adresse2");
    openapiFields.add("Unternehmen-Fusszeile");
    openapiFields.add("Unternehmen-ID");
    openapiFields.add("Unternehmen-ID-Typ");
    openapiFields.add("Unternehmen-Kopfzeile");
    openapiFields.add("Unternehmen-Name");
    openapiFields.add("Unternehmen-Ort");
    openapiFields.add("Unternehmen-PLZ");
    openapiFields.add("Zahlungen");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Belegdaten
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Belegdaten.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Belegdaten is not found in the empty JSON string", Belegdaten.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Belegdaten.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Belegdaten` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Externer-Beleg-Belegkreis") != null && !jsonObj.get("Externer-Beleg-Belegkreis").isJsonNull()) && !jsonObj.get("Externer-Beleg-Belegkreis").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Externer-Beleg-Belegkreis` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Externer-Beleg-Belegkreis").toString()));
      }
      if ((jsonObj.get("Externer-Beleg-Bezeichnung") != null && !jsonObj.get("Externer-Beleg-Bezeichnung").isJsonNull()) && !jsonObj.get("Externer-Beleg-Bezeichnung").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Externer-Beleg-Bezeichnung` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Externer-Beleg-Bezeichnung").toString()));
      }
      if ((jsonObj.get("Externer-Beleg-Referenz") != null && !jsonObj.get("Externer-Beleg-Referenz").isJsonNull()) && !jsonObj.get("Externer-Beleg-Referenz").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Externer-Beleg-Referenz` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Externer-Beleg-Referenz").toString()));
      }
      if ((jsonObj.get("Kunde") != null && !jsonObj.get("Kunde").isJsonNull()) && !jsonObj.get("Kunde").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Kunde` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Kunde").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("Notizen") != null && !jsonObj.get("Notizen").isJsonNull() && !jsonObj.get("Notizen").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Notizen` to be an array in the JSON string but got `%s`", jsonObj.get("Notizen").toString()));
      }
      if (jsonObj.get("Posten") != null && !jsonObj.get("Posten").isJsonNull()) {
        JsonArray jsonArrayposten = jsonObj.getAsJsonArray("Posten");
        if (jsonArrayposten != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Posten").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Posten` to be an array in the JSON string but got `%s`", jsonObj.get("Posten").toString()));
          }

          // validate the optional field `Posten` (array)
          for (int i = 0; i < jsonArrayposten.size(); i++) {
            Posten.validateJsonElement(jsonArrayposten.get(i));
          };
        }
      }
      if (jsonObj.get("Rabatte") != null && !jsonObj.get("Rabatte").isJsonNull()) {
        JsonArray jsonArrayrabatte = jsonObj.getAsJsonArray("Rabatte");
        if (jsonArrayrabatte != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Rabatte").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Rabatte` to be an array in the JSON string but got `%s`", jsonObj.get("Rabatte").toString()));
          }

          // validate the optional field `Rabatte` (array)
          for (int i = 0; i < jsonArrayrabatte.size(); i++) {
            Rabatt.validateJsonElement(jsonArrayrabatte.get(i));
          };
        }
      }
      if ((jsonObj.get("Storno-Beleg-UUID") != null && !jsonObj.get("Storno-Beleg-UUID").isJsonNull()) && !jsonObj.get("Storno-Beleg-UUID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Storno-Beleg-UUID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Storno-Beleg-UUID").toString()));
      }
      if ((jsonObj.get("Storno-Text") != null && !jsonObj.get("Storno-Text").isJsonNull()) && !jsonObj.get("Storno-Text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Storno-Text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Storno-Text").toString()));
      }
      if ((jsonObj.get("Unternehmen-Adresse1") != null && !jsonObj.get("Unternehmen-Adresse1").isJsonNull()) && !jsonObj.get("Unternehmen-Adresse1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-Adresse1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-Adresse1").toString()));
      }
      if ((jsonObj.get("Unternehmen-Adresse2") != null && !jsonObj.get("Unternehmen-Adresse2").isJsonNull()) && !jsonObj.get("Unternehmen-Adresse2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-Adresse2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-Adresse2").toString()));
      }
      if ((jsonObj.get("Unternehmen-Fusszeile") != null && !jsonObj.get("Unternehmen-Fusszeile").isJsonNull()) && !jsonObj.get("Unternehmen-Fusszeile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-Fusszeile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-Fusszeile").toString()));
      }
      if ((jsonObj.get("Unternehmen-ID") != null && !jsonObj.get("Unternehmen-ID").isJsonNull()) && !jsonObj.get("Unternehmen-ID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-ID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-ID").toString()));
      }
      if ((jsonObj.get("Unternehmen-ID-Typ") != null && !jsonObj.get("Unternehmen-ID-Typ").isJsonNull()) && !jsonObj.get("Unternehmen-ID-Typ").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-ID-Typ` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-ID-Typ").toString()));
      }
      // validate the optional field `Unternehmen-ID-Typ`
      if (jsonObj.get("Unternehmen-ID-Typ") != null && !jsonObj.get("Unternehmen-ID-Typ").isJsonNull()) {
        UnternehmenIDTypEnum.validateJsonElement(jsonObj.get("Unternehmen-ID-Typ"));
      }
      if ((jsonObj.get("Unternehmen-Kopfzeile") != null && !jsonObj.get("Unternehmen-Kopfzeile").isJsonNull()) && !jsonObj.get("Unternehmen-Kopfzeile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-Kopfzeile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-Kopfzeile").toString()));
      }
      if ((jsonObj.get("Unternehmen-Name") != null && !jsonObj.get("Unternehmen-Name").isJsonNull()) && !jsonObj.get("Unternehmen-Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-Name").toString()));
      }
      if ((jsonObj.get("Unternehmen-Ort") != null && !jsonObj.get("Unternehmen-Ort").isJsonNull()) && !jsonObj.get("Unternehmen-Ort").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-Ort` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-Ort").toString()));
      }
      if ((jsonObj.get("Unternehmen-PLZ") != null && !jsonObj.get("Unternehmen-PLZ").isJsonNull()) && !jsonObj.get("Unternehmen-PLZ").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Unternehmen-PLZ` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Unternehmen-PLZ").toString()));
      }
      if (jsonObj.get("Zahlungen") != null && !jsonObj.get("Zahlungen").isJsonNull()) {
        JsonArray jsonArrayzahlungen = jsonObj.getAsJsonArray("Zahlungen");
        if (jsonArrayzahlungen != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Zahlungen").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Zahlungen` to be an array in the JSON string but got `%s`", jsonObj.get("Zahlungen").toString()));
          }

          // validate the optional field `Zahlungen` (array)
          for (int i = 0; i < jsonArrayzahlungen.size(); i++) {
            Zahlung.validateJsonElement(jsonArrayzahlungen.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Belegdaten.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Belegdaten' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Belegdaten> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Belegdaten.class));

       return (TypeAdapter<T>) new TypeAdapter<Belegdaten>() {
           @Override
           public void write(JsonWriter out, Belegdaten value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Belegdaten read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Belegdaten given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Belegdaten
   * @throws IOException if the JSON string is invalid with respect to Belegdaten
   */
  public static Belegdaten fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Belegdaten.class);
  }

  /**
   * Convert an instance of Belegdaten to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

