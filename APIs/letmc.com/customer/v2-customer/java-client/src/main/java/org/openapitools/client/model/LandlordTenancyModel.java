/*
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.LandlordLettingsInspectionModel;
import org.openapitools.client.model.LandlordMaintenanceCertificateModel;
import org.openapitools.client.model.LandlordMaintenancePreferenceModel;
import org.openapitools.client.model.LettingsLandlordDocument;

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
 * Landlord Tenancy Model.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:04.921745-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LandlordTenancyModel {
  public static final String SERIALIZED_NAME_ACTUAL_END_DATE = "ActualEndDate";
  @SerializedName(SERIALIZED_NAME_ACTUAL_END_DATE)
  private OffsetDateTime actualEndDate;

  public static final String SERIALIZED_NAME_BEDS = "Beds";
  @SerializedName(SERIALIZED_NAME_BEDS)
  private Integer beds;

  public static final String SERIALIZED_NAME_BOND = "Bond";
  @SerializedName(SERIALIZED_NAME_BOND)
  private Double bond;

  public static final String SERIALIZED_NAME_BRANCH_I_D = "BranchID";
  @SerializedName(SERIALIZED_NAME_BRANCH_I_D)
  private String branchID;

  public static final String SERIALIZED_NAME_CERTIFICATES = "Certificates";
  @SerializedName(SERIALIZED_NAME_CERTIFICATES)
  private List<LandlordMaintenanceCertificateModel> certificates = new ArrayList<>();

  public static final String SERIALIZED_NAME_DOCUMENTS = "Documents";
  @SerializedName(SERIALIZED_NAME_DOCUMENTS)
  private List<LettingsLandlordDocument> documents = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIXED_DATE = "FixedDate";
  @SerializedName(SERIALIZED_NAME_FIXED_DATE)
  private OffsetDateTime fixedDate;

  public static final String SERIALIZED_NAME_GLOBAL_REFERENCE = "GlobalReference";
  @SerializedName(SERIALIZED_NAME_GLOBAL_REFERENCE)
  private String globalReference;

  public static final String SERIALIZED_NAME_I_D = "ID";
  @SerializedName(SERIALIZED_NAME_I_D)
  private String ID;

  public static final String SERIALIZED_NAME_INSPECTIONS = "Inspections";
  @SerializedName(SERIALIZED_NAME_INSPECTIONS)
  private List<LandlordLettingsInspectionModel> inspections = new ArrayList<>();

  public static final String SERIALIZED_NAME_MANAGED_RENT = "ManagedRent";
  @SerializedName(SERIALIZED_NAME_MANAGED_RENT)
  private Boolean managedRent;

  public static final String SERIALIZED_NAME_PREFERENCES = "Preferences";
  @SerializedName(SERIALIZED_NAME_PREFERENCES)
  private List<LandlordMaintenancePreferenceModel> preferences = new ArrayList<>();

  public static final String SERIALIZED_NAME_PREVIOUS_RENT_AMOUNT = "PreviousRentAmount";
  @SerializedName(SERIALIZED_NAME_PREVIOUS_RENT_AMOUNT)
  private Double previousRentAmount;

  public static final String SERIALIZED_NAME_PROPERTY_ADDRESS = "PropertyAddress";
  @SerializedName(SERIALIZED_NAME_PROPERTY_ADDRESS)
  private String propertyAddress;

  public static final String SERIALIZED_NAME_RENT = "Rent";
  @SerializedName(SERIALIZED_NAME_RENT)
  private String rent;

  public static final String SERIALIZED_NAME_RENT_AMOUNT = "RentAmount";
  @SerializedName(SERIALIZED_NAME_RENT_AMOUNT)
  private Double rentAmount;

  public static final String SERIALIZED_NAME_START_DATE = "StartDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private OffsetDateTime startDate;

  public static final String SERIALIZED_NAME_TENANCY_PROPERTY = "TenancyProperty";
  @SerializedName(SERIALIZED_NAME_TENANCY_PROPERTY)
  private String tenancyProperty;

  public static final String SERIALIZED_NAME_TENANCY_STATE = "TenancyState";
  @SerializedName(SERIALIZED_NAME_TENANCY_STATE)
  private String tenancyState;

  public static final String SERIALIZED_NAME_TENANTS = "Tenants";
  @SerializedName(SERIALIZED_NAME_TENANTS)
  private List<String> tenants = new ArrayList<>();

  public LandlordTenancyModel() {
  }

  public LandlordTenancyModel actualEndDate(OffsetDateTime actualEndDate) {
    this.actualEndDate = actualEndDate;
    return this;
  }

  /**
   * Actual End Date
   * @return actualEndDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getActualEndDate() {
    return actualEndDate;
  }

  public void setActualEndDate(OffsetDateTime actualEndDate) {
    this.actualEndDate = actualEndDate;
  }


  public LandlordTenancyModel beds(Integer beds) {
    this.beds = beds;
    return this;
  }

  /**
   * Beds
   * @return beds
   */
  @javax.annotation.Nullable
  public Integer getBeds() {
    return beds;
  }

  public void setBeds(Integer beds) {
    this.beds = beds;
  }


  public LandlordTenancyModel bond(Double bond) {
    this.bond = bond;
    return this;
  }

  /**
   * Bond
   * @return bond
   */
  @javax.annotation.Nullable
  public Double getBond() {
    return bond;
  }

  public void setBond(Double bond) {
    this.bond = bond;
  }


  public LandlordTenancyModel branchID(String branchID) {
    this.branchID = branchID;
    return this;
  }

  /**
   * The tenancy branch ID:-
   * @return branchID
   */
  @javax.annotation.Nullable
  public String getBranchID() {
    return branchID;
  }

  public void setBranchID(String branchID) {
    this.branchID = branchID;
  }


  public LandlordTenancyModel certificates(List<LandlordMaintenanceCertificateModel> certificates) {
    this.certificates = certificates;
    return this;
  }

  public LandlordTenancyModel addCertificatesItem(LandlordMaintenanceCertificateModel certificatesItem) {
    if (this.certificates == null) {
      this.certificates = new ArrayList<>();
    }
    this.certificates.add(certificatesItem);
    return this;
  }

  /**
   * Maintenance Certificates.
   * @return certificates
   */
  @javax.annotation.Nullable
  public List<LandlordMaintenanceCertificateModel> getCertificates() {
    return certificates;
  }

  public void setCertificates(List<LandlordMaintenanceCertificateModel> certificates) {
    this.certificates = certificates;
  }


  public LandlordTenancyModel documents(List<LettingsLandlordDocument> documents) {
    this.documents = documents;
    return this;
  }

  public LandlordTenancyModel addDocumentsItem(LettingsLandlordDocument documentsItem) {
    if (this.documents == null) {
      this.documents = new ArrayList<>();
    }
    this.documents.add(documentsItem);
    return this;
  }

  /**
   * Tenancy documents:-
   * @return documents
   */
  @javax.annotation.Nullable
  public List<LettingsLandlordDocument> getDocuments() {
    return documents;
  }

  public void setDocuments(List<LettingsLandlordDocument> documents) {
    this.documents = documents;
  }


  public LandlordTenancyModel fixedDate(OffsetDateTime fixedDate) {
    this.fixedDate = fixedDate;
    return this;
  }

  /**
   * Fixed Date
   * @return fixedDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getFixedDate() {
    return fixedDate;
  }

  public void setFixedDate(OffsetDateTime fixedDate) {
    this.fixedDate = fixedDate;
  }


  public LandlordTenancyModel globalReference(String globalReference) {
    this.globalReference = globalReference;
    return this;
  }

  /**
   * User Friendly ID
   * @return globalReference
   */
  @javax.annotation.Nullable
  public String getGlobalReference() {
    return globalReference;
  }

  public void setGlobalReference(String globalReference) {
    this.globalReference = globalReference;
  }


  public LandlordTenancyModel ID(String ID) {
    this.ID = ID;
    return this;
  }

  /**
   * ID
   * @return ID
   */
  @javax.annotation.Nullable
  public String getID() {
    return ID;
  }

  public void setID(String ID) {
    this.ID = ID;
  }


  public LandlordTenancyModel inspections(List<LandlordLettingsInspectionModel> inspections) {
    this.inspections = inspections;
    return this;
  }

  public LandlordTenancyModel addInspectionsItem(LandlordLettingsInspectionModel inspectionsItem) {
    if (this.inspections == null) {
      this.inspections = new ArrayList<>();
    }
    this.inspections.add(inspectionsItem);
    return this;
  }

  /**
   * Inspections
   * @return inspections
   */
  @javax.annotation.Nullable
  public List<LandlordLettingsInspectionModel> getInspections() {
    return inspections;
  }

  public void setInspections(List<LandlordLettingsInspectionModel> inspections) {
    this.inspections = inspections;
  }


  public LandlordTenancyModel managedRent(Boolean managedRent) {
    this.managedRent = managedRent;
    return this;
  }

  /**
   * State of the tenancy
   * @return managedRent
   */
  @javax.annotation.Nullable
  public Boolean getManagedRent() {
    return managedRent;
  }

  public void setManagedRent(Boolean managedRent) {
    this.managedRent = managedRent;
  }


  public LandlordTenancyModel preferences(List<LandlordMaintenancePreferenceModel> preferences) {
    this.preferences = preferences;
    return this;
  }

  public LandlordTenancyModel addPreferencesItem(LandlordMaintenancePreferenceModel preferencesItem) {
    if (this.preferences == null) {
      this.preferences = new ArrayList<>();
    }
    this.preferences.add(preferencesItem);
    return this;
  }

  /**
   * Maintenance Preferences.
   * @return preferences
   */
  @javax.annotation.Nullable
  public List<LandlordMaintenancePreferenceModel> getPreferences() {
    return preferences;
  }

  public void setPreferences(List<LandlordMaintenancePreferenceModel> preferences) {
    this.preferences = preferences;
  }


  public LandlordTenancyModel previousRentAmount(Double previousRentAmount) {
    this.previousRentAmount = previousRentAmount;
    return this;
  }

  /**
   * Previous Rent Amount
   * @return previousRentAmount
   */
  @javax.annotation.Nullable
  public Double getPreviousRentAmount() {
    return previousRentAmount;
  }

  public void setPreviousRentAmount(Double previousRentAmount) {
    this.previousRentAmount = previousRentAmount;
  }


  public LandlordTenancyModel propertyAddress(String propertyAddress) {
    this.propertyAddress = propertyAddress;
    return this;
  }

  /**
   * Display Property Address
   * @return propertyAddress
   */
  @javax.annotation.Nullable
  public String getPropertyAddress() {
    return propertyAddress;
  }

  public void setPropertyAddress(String propertyAddress) {
    this.propertyAddress = propertyAddress;
  }


  public LandlordTenancyModel rent(String rent) {
    this.rent = rent;
    return this;
  }

  /**
   * Rent
   * @return rent
   */
  @javax.annotation.Nullable
  public String getRent() {
    return rent;
  }

  public void setRent(String rent) {
    this.rent = rent;
  }


  public LandlordTenancyModel rentAmount(Double rentAmount) {
    this.rentAmount = rentAmount;
    return this;
  }

  /**
   * Rent Amount
   * @return rentAmount
   */
  @javax.annotation.Nullable
  public Double getRentAmount() {
    return rentAmount;
  }

  public void setRentAmount(Double rentAmount) {
    this.rentAmount = rentAmount;
  }


  public LandlordTenancyModel startDate(OffsetDateTime startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Start Date
   * @return startDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartDate() {
    return startDate;
  }

  public void setStartDate(OffsetDateTime startDate) {
    this.startDate = startDate;
  }


  public LandlordTenancyModel tenancyProperty(String tenancyProperty) {
    this.tenancyProperty = tenancyProperty;
    return this;
  }

  /**
   * Tenancy Property
   * @return tenancyProperty
   */
  @javax.annotation.Nullable
  public String getTenancyProperty() {
    return tenancyProperty;
  }

  public void setTenancyProperty(String tenancyProperty) {
    this.tenancyProperty = tenancyProperty;
  }


  public LandlordTenancyModel tenancyState(String tenancyState) {
    this.tenancyState = tenancyState;
    return this;
  }

  /**
   * State of the tenancy
   * @return tenancyState
   */
  @javax.annotation.Nullable
  public String getTenancyState() {
    return tenancyState;
  }

  public void setTenancyState(String tenancyState) {
    this.tenancyState = tenancyState;
  }


  public LandlordTenancyModel tenants(List<String> tenants) {
    this.tenants = tenants;
    return this;
  }

  public LandlordTenancyModel addTenantsItem(String tenantsItem) {
    if (this.tenants == null) {
      this.tenants = new ArrayList<>();
    }
    this.tenants.add(tenantsItem);
    return this;
  }

  /**
   * Tenants
   * @return tenants
   */
  @javax.annotation.Nullable
  public List<String> getTenants() {
    return tenants;
  }

  public void setTenants(List<String> tenants) {
    this.tenants = tenants;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LandlordTenancyModel landlordTenancyModel = (LandlordTenancyModel) o;
    return Objects.equals(this.actualEndDate, landlordTenancyModel.actualEndDate) &&
        Objects.equals(this.beds, landlordTenancyModel.beds) &&
        Objects.equals(this.bond, landlordTenancyModel.bond) &&
        Objects.equals(this.branchID, landlordTenancyModel.branchID) &&
        Objects.equals(this.certificates, landlordTenancyModel.certificates) &&
        Objects.equals(this.documents, landlordTenancyModel.documents) &&
        Objects.equals(this.fixedDate, landlordTenancyModel.fixedDate) &&
        Objects.equals(this.globalReference, landlordTenancyModel.globalReference) &&
        Objects.equals(this.ID, landlordTenancyModel.ID) &&
        Objects.equals(this.inspections, landlordTenancyModel.inspections) &&
        Objects.equals(this.managedRent, landlordTenancyModel.managedRent) &&
        Objects.equals(this.preferences, landlordTenancyModel.preferences) &&
        Objects.equals(this.previousRentAmount, landlordTenancyModel.previousRentAmount) &&
        Objects.equals(this.propertyAddress, landlordTenancyModel.propertyAddress) &&
        Objects.equals(this.rent, landlordTenancyModel.rent) &&
        Objects.equals(this.rentAmount, landlordTenancyModel.rentAmount) &&
        Objects.equals(this.startDate, landlordTenancyModel.startDate) &&
        Objects.equals(this.tenancyProperty, landlordTenancyModel.tenancyProperty) &&
        Objects.equals(this.tenancyState, landlordTenancyModel.tenancyState) &&
        Objects.equals(this.tenants, landlordTenancyModel.tenants);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actualEndDate, beds, bond, branchID, certificates, documents, fixedDate, globalReference, ID, inspections, managedRent, preferences, previousRentAmount, propertyAddress, rent, rentAmount, startDate, tenancyProperty, tenancyState, tenants);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LandlordTenancyModel {\n");
    sb.append("    actualEndDate: ").append(toIndentedString(actualEndDate)).append("\n");
    sb.append("    beds: ").append(toIndentedString(beds)).append("\n");
    sb.append("    bond: ").append(toIndentedString(bond)).append("\n");
    sb.append("    branchID: ").append(toIndentedString(branchID)).append("\n");
    sb.append("    certificates: ").append(toIndentedString(certificates)).append("\n");
    sb.append("    documents: ").append(toIndentedString(documents)).append("\n");
    sb.append("    fixedDate: ").append(toIndentedString(fixedDate)).append("\n");
    sb.append("    globalReference: ").append(toIndentedString(globalReference)).append("\n");
    sb.append("    ID: ").append(toIndentedString(ID)).append("\n");
    sb.append("    inspections: ").append(toIndentedString(inspections)).append("\n");
    sb.append("    managedRent: ").append(toIndentedString(managedRent)).append("\n");
    sb.append("    preferences: ").append(toIndentedString(preferences)).append("\n");
    sb.append("    previousRentAmount: ").append(toIndentedString(previousRentAmount)).append("\n");
    sb.append("    propertyAddress: ").append(toIndentedString(propertyAddress)).append("\n");
    sb.append("    rent: ").append(toIndentedString(rent)).append("\n");
    sb.append("    rentAmount: ").append(toIndentedString(rentAmount)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    tenancyProperty: ").append(toIndentedString(tenancyProperty)).append("\n");
    sb.append("    tenancyState: ").append(toIndentedString(tenancyState)).append("\n");
    sb.append("    tenants: ").append(toIndentedString(tenants)).append("\n");
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
    openapiFields.add("ActualEndDate");
    openapiFields.add("Beds");
    openapiFields.add("Bond");
    openapiFields.add("BranchID");
    openapiFields.add("Certificates");
    openapiFields.add("Documents");
    openapiFields.add("FixedDate");
    openapiFields.add("GlobalReference");
    openapiFields.add("ID");
    openapiFields.add("Inspections");
    openapiFields.add("ManagedRent");
    openapiFields.add("Preferences");
    openapiFields.add("PreviousRentAmount");
    openapiFields.add("PropertyAddress");
    openapiFields.add("Rent");
    openapiFields.add("RentAmount");
    openapiFields.add("StartDate");
    openapiFields.add("TenancyProperty");
    openapiFields.add("TenancyState");
    openapiFields.add("Tenants");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LandlordTenancyModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LandlordTenancyModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LandlordTenancyModel is not found in the empty JSON string", LandlordTenancyModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LandlordTenancyModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LandlordTenancyModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("BranchID") != null && !jsonObj.get("BranchID").isJsonNull()) && !jsonObj.get("BranchID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BranchID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BranchID").toString()));
      }
      if (jsonObj.get("Certificates") != null && !jsonObj.get("Certificates").isJsonNull()) {
        JsonArray jsonArraycertificates = jsonObj.getAsJsonArray("Certificates");
        if (jsonArraycertificates != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Certificates").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Certificates` to be an array in the JSON string but got `%s`", jsonObj.get("Certificates").toString()));
          }

          // validate the optional field `Certificates` (array)
          for (int i = 0; i < jsonArraycertificates.size(); i++) {
            LandlordMaintenanceCertificateModel.validateJsonElement(jsonArraycertificates.get(i));
          };
        }
      }
      if (jsonObj.get("Documents") != null && !jsonObj.get("Documents").isJsonNull()) {
        JsonArray jsonArraydocuments = jsonObj.getAsJsonArray("Documents");
        if (jsonArraydocuments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Documents").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Documents` to be an array in the JSON string but got `%s`", jsonObj.get("Documents").toString()));
          }

          // validate the optional field `Documents` (array)
          for (int i = 0; i < jsonArraydocuments.size(); i++) {
            LettingsLandlordDocument.validateJsonElement(jsonArraydocuments.get(i));
          };
        }
      }
      if ((jsonObj.get("GlobalReference") != null && !jsonObj.get("GlobalReference").isJsonNull()) && !jsonObj.get("GlobalReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `GlobalReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("GlobalReference").toString()));
      }
      if ((jsonObj.get("ID") != null && !jsonObj.get("ID").isJsonNull()) && !jsonObj.get("ID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ID").toString()));
      }
      if (jsonObj.get("Inspections") != null && !jsonObj.get("Inspections").isJsonNull()) {
        JsonArray jsonArrayinspections = jsonObj.getAsJsonArray("Inspections");
        if (jsonArrayinspections != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Inspections").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Inspections` to be an array in the JSON string but got `%s`", jsonObj.get("Inspections").toString()));
          }

          // validate the optional field `Inspections` (array)
          for (int i = 0; i < jsonArrayinspections.size(); i++) {
            LandlordLettingsInspectionModel.validateJsonElement(jsonArrayinspections.get(i));
          };
        }
      }
      if (jsonObj.get("Preferences") != null && !jsonObj.get("Preferences").isJsonNull()) {
        JsonArray jsonArraypreferences = jsonObj.getAsJsonArray("Preferences");
        if (jsonArraypreferences != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Preferences").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Preferences` to be an array in the JSON string but got `%s`", jsonObj.get("Preferences").toString()));
          }

          // validate the optional field `Preferences` (array)
          for (int i = 0; i < jsonArraypreferences.size(); i++) {
            LandlordMaintenancePreferenceModel.validateJsonElement(jsonArraypreferences.get(i));
          };
        }
      }
      if ((jsonObj.get("PropertyAddress") != null && !jsonObj.get("PropertyAddress").isJsonNull()) && !jsonObj.get("PropertyAddress").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PropertyAddress` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PropertyAddress").toString()));
      }
      if ((jsonObj.get("Rent") != null && !jsonObj.get("Rent").isJsonNull()) && !jsonObj.get("Rent").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Rent` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Rent").toString()));
      }
      if ((jsonObj.get("TenancyProperty") != null && !jsonObj.get("TenancyProperty").isJsonNull()) && !jsonObj.get("TenancyProperty").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TenancyProperty` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TenancyProperty").toString()));
      }
      if ((jsonObj.get("TenancyState") != null && !jsonObj.get("TenancyState").isJsonNull()) && !jsonObj.get("TenancyState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TenancyState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TenancyState").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("Tenants") != null && !jsonObj.get("Tenants").isJsonNull() && !jsonObj.get("Tenants").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Tenants` to be an array in the JSON string but got `%s`", jsonObj.get("Tenants").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LandlordTenancyModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LandlordTenancyModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LandlordTenancyModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LandlordTenancyModel.class));

       return (TypeAdapter<T>) new TypeAdapter<LandlordTenancyModel>() {
           @Override
           public void write(JsonWriter out, LandlordTenancyModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LandlordTenancyModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LandlordTenancyModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LandlordTenancyModel
   * @throws IOException if the JSON string is invalid with respect to LandlordTenancyModel
   */
  public static LandlordTenancyModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LandlordTenancyModel.class);
  }

  /**
   * Convert an instance of LandlordTenancyModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

