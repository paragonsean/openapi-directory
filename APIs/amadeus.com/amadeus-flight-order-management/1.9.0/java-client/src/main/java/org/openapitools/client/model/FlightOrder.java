/*
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AirTravelDocument;
import org.openapitools.client.model.AssociatedRecord;
import org.openapitools.client.model.AutomatedProcess;
import org.openapitools.client.model.Contact;
import org.openapitools.client.model.FlightOffer;
import org.openapitools.client.model.FormOfIdentification;
import org.openapitools.client.model.FormOfPayment;
import org.openapitools.client.model.Remarks;
import org.openapitools.client.model.TicketingAgreement;
import org.openapitools.client.model.Traveler;

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
 * input parameter to create a flight order
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:54.608298-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FlightOrder {
  public static final String SERIALIZED_NAME_ASSOCIATED_RECORDS = "associatedRecords";
  @SerializedName(SERIALIZED_NAME_ASSOCIATED_RECORDS)
  private List<AssociatedRecord> associatedRecords = new ArrayList<>();

  public static final String SERIALIZED_NAME_AUTOMATED_PROCESS = "automatedProcess";
  @SerializedName(SERIALIZED_NAME_AUTOMATED_PROCESS)
  private List<AutomatedProcess> automatedProcess = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONTACTS = "contacts";
  @SerializedName(SERIALIZED_NAME_CONTACTS)
  private List<Contact> contacts = new ArrayList<>();

  public static final String SERIALIZED_NAME_FLIGHT_OFFERS = "flightOffers";
  @SerializedName(SERIALIZED_NAME_FLIGHT_OFFERS)
  private List<FlightOffer> flightOffers = new ArrayList<>();

  public static final String SERIALIZED_NAME_FORM_OF_IDENTIFICATIONS = "formOfIdentifications";
  @SerializedName(SERIALIZED_NAME_FORM_OF_IDENTIFICATIONS)
  private List<FormOfIdentification> formOfIdentifications = new ArrayList<>();

  public static final String SERIALIZED_NAME_FORM_OF_PAYMENTS = "formOfPayments";
  @SerializedName(SERIALIZED_NAME_FORM_OF_PAYMENTS)
  private List<FormOfPayment> formOfPayments = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_OWNER_OFFICE_ID = "ownerOfficeId";
  @SerializedName(SERIALIZED_NAME_OWNER_OFFICE_ID)
  private String ownerOfficeId;

  public static final String SERIALIZED_NAME_QUEUING_OFFICE_ID = "queuingOfficeId";
  @SerializedName(SERIALIZED_NAME_QUEUING_OFFICE_ID)
  private String queuingOfficeId;

  public static final String SERIALIZED_NAME_REMARKS = "remarks";
  @SerializedName(SERIALIZED_NAME_REMARKS)
  private Remarks remarks;

  public static final String SERIALIZED_NAME_TICKETING_AGREEMENT = "ticketingAgreement";
  @SerializedName(SERIALIZED_NAME_TICKETING_AGREEMENT)
  private TicketingAgreement ticketingAgreement;

  public static final String SERIALIZED_NAME_TICKETS = "tickets";
  @SerializedName(SERIALIZED_NAME_TICKETS)
  private List<AirTravelDocument> tickets = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRAVELERS = "travelers";
  @SerializedName(SERIALIZED_NAME_TRAVELERS)
  private List<Traveler> travelers = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public FlightOrder() {
  }

  public FlightOrder(
     List<AssociatedRecord> associatedRecords, 
     String id, 
     List<AirTravelDocument> tickets
  ) {
    this();
    this.associatedRecords = associatedRecords;
    this.id = id;
    this.tickets = tickets;
  }

  /**
   * list of associated record
   * @return associatedRecords
   */
  @javax.annotation.Nullable
  public List<AssociatedRecord> getAssociatedRecords() {
    return associatedRecords;
  }



  public FlightOrder automatedProcess(List<AutomatedProcess> automatedProcess) {
    this.automatedProcess = automatedProcess;
    return this;
  }

  public FlightOrder addAutomatedProcessItem(AutomatedProcess automatedProcessItem) {
    if (this.automatedProcess == null) {
      this.automatedProcess = new ArrayList<>();
    }
    this.automatedProcess.add(automatedProcessItem);
    return this;
  }

  /**
   * list of automatic queuing
   * @return automatedProcess
   */
  @javax.annotation.Nullable
  public List<AutomatedProcess> getAutomatedProcess() {
    return automatedProcess;
  }

  public void setAutomatedProcess(List<AutomatedProcess> automatedProcess) {
    this.automatedProcess = automatedProcess;
  }


  public FlightOrder contacts(List<Contact> contacts) {
    this.contacts = contacts;
    return this;
  }

  public FlightOrder addContactsItem(Contact contactsItem) {
    if (this.contacts == null) {
      this.contacts = new ArrayList<>();
    }
    this.contacts.add(contactsItem);
    return this;
  }

  /**
   * list of general contact information
   * @return contacts
   */
  @javax.annotation.Nullable
  public List<Contact> getContacts() {
    return contacts;
  }

  public void setContacts(List<Contact> contacts) {
    this.contacts = contacts;
  }


  public FlightOrder flightOffers(List<FlightOffer> flightOffers) {
    this.flightOffers = flightOffers;
    return this;
  }

  public FlightOrder addFlightOffersItem(FlightOffer flightOffersItem) {
    if (this.flightOffers == null) {
      this.flightOffers = new ArrayList<>();
    }
    this.flightOffers.add(flightOffersItem);
    return this;
  }

  /**
   * list of flight offer
   * @return flightOffers
   */
  @javax.annotation.Nonnull
  public List<FlightOffer> getFlightOffers() {
    return flightOffers;
  }

  public void setFlightOffers(List<FlightOffer> flightOffers) {
    this.flightOffers = flightOffers;
  }


  public FlightOrder formOfIdentifications(List<FormOfIdentification> formOfIdentifications) {
    this.formOfIdentifications = formOfIdentifications;
    return this;
  }

  public FlightOrder addFormOfIdentificationsItem(FormOfIdentification formOfIdentificationsItem) {
    if (this.formOfIdentifications == null) {
      this.formOfIdentifications = new ArrayList<>();
    }
    this.formOfIdentifications.add(formOfIdentificationsItem);
    return this;
  }

  /**
   * list of forms of identifications applicable to travelers by airline
   * @return formOfIdentifications
   */
  @javax.annotation.Nullable
  public List<FormOfIdentification> getFormOfIdentifications() {
    return formOfIdentifications;
  }

  public void setFormOfIdentifications(List<FormOfIdentification> formOfIdentifications) {
    this.formOfIdentifications = formOfIdentifications;
  }


  public FlightOrder formOfPayments(List<FormOfPayment> formOfPayments) {
    this.formOfPayments = formOfPayments;
    return this;
  }

  public FlightOrder addFormOfPaymentsItem(FormOfPayment formOfPaymentsItem) {
    if (this.formOfPayments == null) {
      this.formOfPayments = new ArrayList<>();
    }
    this.formOfPayments.add(formOfPaymentsItem);
    return this;
  }

  /**
   * list of form of payments
   * @return formOfPayments
   */
  @javax.annotation.Nullable
  public List<FormOfPayment> getFormOfPayments() {
    return formOfPayments;
  }

  public void setFormOfPayments(List<FormOfPayment> formOfPayments) {
    this.formOfPayments = formOfPayments;
  }


  /**
   * unique identifier of the flight order
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public FlightOrder ownerOfficeId(String ownerOfficeId) {
    this.ownerOfficeId = ownerOfficeId;
    return this;
  }

  /**
   * office Id where will be transfered the ownership of the order
   * @return ownerOfficeId
   */
  @javax.annotation.Nullable
  public String getOwnerOfficeId() {
    return ownerOfficeId;
  }

  public void setOwnerOfficeId(String ownerOfficeId) {
    this.ownerOfficeId = ownerOfficeId;
  }


  public FlightOrder queuingOfficeId(String queuingOfficeId) {
    this.queuingOfficeId = queuingOfficeId;
    return this;
  }

  /**
   * office Id where to queue the order
   * @return queuingOfficeId
   */
  @javax.annotation.Nullable
  public String getQueuingOfficeId() {
    return queuingOfficeId;
  }

  public void setQueuingOfficeId(String queuingOfficeId) {
    this.queuingOfficeId = queuingOfficeId;
  }


  public FlightOrder remarks(Remarks remarks) {
    this.remarks = remarks;
    return this;
  }

  /**
   * Get remarks
   * @return remarks
   */
  @javax.annotation.Nullable
  public Remarks getRemarks() {
    return remarks;
  }

  public void setRemarks(Remarks remarks) {
    this.remarks = remarks;
  }


  public FlightOrder ticketingAgreement(TicketingAgreement ticketingAgreement) {
    this.ticketingAgreement = ticketingAgreement;
    return this;
  }

  /**
   * Get ticketingAgreement
   * @return ticketingAgreement
   */
  @javax.annotation.Nullable
  public TicketingAgreement getTicketingAgreement() {
    return ticketingAgreement;
  }

  public void setTicketingAgreement(TicketingAgreement ticketingAgreement) {
    this.ticketingAgreement = ticketingAgreement;
  }


  /**
   * list of tickets
   * @return tickets
   */
  @javax.annotation.Nullable
  public List<AirTravelDocument> getTickets() {
    return tickets;
  }



  public FlightOrder travelers(List<Traveler> travelers) {
    this.travelers = travelers;
    return this;
  }

  public FlightOrder addTravelersItem(Traveler travelersItem) {
    if (this.travelers == null) {
      this.travelers = new ArrayList<>();
    }
    this.travelers.add(travelersItem);
    return this;
  }

  /**
   * list of travelers
   * @return travelers
   */
  @javax.annotation.Nullable
  public List<Traveler> getTravelers() {
    return travelers;
  }

  public void setTravelers(List<Traveler> travelers) {
    this.travelers = travelers;
  }


  public FlightOrder type(String type) {
    this.type = type;
    return this;
  }

  /**
   * the resource name
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
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
    FlightOrder flightOrder = (FlightOrder) o;
    return Objects.equals(this.associatedRecords, flightOrder.associatedRecords) &&
        Objects.equals(this.automatedProcess, flightOrder.automatedProcess) &&
        Objects.equals(this.contacts, flightOrder.contacts) &&
        Objects.equals(this.flightOffers, flightOrder.flightOffers) &&
        Objects.equals(this.formOfIdentifications, flightOrder.formOfIdentifications) &&
        Objects.equals(this.formOfPayments, flightOrder.formOfPayments) &&
        Objects.equals(this.id, flightOrder.id) &&
        Objects.equals(this.ownerOfficeId, flightOrder.ownerOfficeId) &&
        Objects.equals(this.queuingOfficeId, flightOrder.queuingOfficeId) &&
        Objects.equals(this.remarks, flightOrder.remarks) &&
        Objects.equals(this.ticketingAgreement, flightOrder.ticketingAgreement) &&
        Objects.equals(this.tickets, flightOrder.tickets) &&
        Objects.equals(this.travelers, flightOrder.travelers) &&
        Objects.equals(this.type, flightOrder.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(associatedRecords, automatedProcess, contacts, flightOffers, formOfIdentifications, formOfPayments, id, ownerOfficeId, queuingOfficeId, remarks, ticketingAgreement, tickets, travelers, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlightOrder {\n");
    sb.append("    associatedRecords: ").append(toIndentedString(associatedRecords)).append("\n");
    sb.append("    automatedProcess: ").append(toIndentedString(automatedProcess)).append("\n");
    sb.append("    contacts: ").append(toIndentedString(contacts)).append("\n");
    sb.append("    flightOffers: ").append(toIndentedString(flightOffers)).append("\n");
    sb.append("    formOfIdentifications: ").append(toIndentedString(formOfIdentifications)).append("\n");
    sb.append("    formOfPayments: ").append(toIndentedString(formOfPayments)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    ownerOfficeId: ").append(toIndentedString(ownerOfficeId)).append("\n");
    sb.append("    queuingOfficeId: ").append(toIndentedString(queuingOfficeId)).append("\n");
    sb.append("    remarks: ").append(toIndentedString(remarks)).append("\n");
    sb.append("    ticketingAgreement: ").append(toIndentedString(ticketingAgreement)).append("\n");
    sb.append("    tickets: ").append(toIndentedString(tickets)).append("\n");
    sb.append("    travelers: ").append(toIndentedString(travelers)).append("\n");
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
    openapiFields.add("associatedRecords");
    openapiFields.add("automatedProcess");
    openapiFields.add("contacts");
    openapiFields.add("flightOffers");
    openapiFields.add("formOfIdentifications");
    openapiFields.add("formOfPayments");
    openapiFields.add("id");
    openapiFields.add("ownerOfficeId");
    openapiFields.add("queuingOfficeId");
    openapiFields.add("remarks");
    openapiFields.add("ticketingAgreement");
    openapiFields.add("tickets");
    openapiFields.add("travelers");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("flightOffers");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FlightOrder
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FlightOrder.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FlightOrder is not found in the empty JSON string", FlightOrder.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FlightOrder.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FlightOrder` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FlightOrder.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("associatedRecords") != null && !jsonObj.get("associatedRecords").isJsonNull()) {
        JsonArray jsonArrayassociatedRecords = jsonObj.getAsJsonArray("associatedRecords");
        if (jsonArrayassociatedRecords != null) {
          // ensure the json data is an array
          if (!jsonObj.get("associatedRecords").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `associatedRecords` to be an array in the JSON string but got `%s`", jsonObj.get("associatedRecords").toString()));
          }

          // validate the optional field `associatedRecords` (array)
          for (int i = 0; i < jsonArrayassociatedRecords.size(); i++) {
            AssociatedRecord.validateJsonElement(jsonArrayassociatedRecords.get(i));
          };
        }
      }
      if (jsonObj.get("automatedProcess") != null && !jsonObj.get("automatedProcess").isJsonNull()) {
        JsonArray jsonArrayautomatedProcess = jsonObj.getAsJsonArray("automatedProcess");
        if (jsonArrayautomatedProcess != null) {
          // ensure the json data is an array
          if (!jsonObj.get("automatedProcess").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `automatedProcess` to be an array in the JSON string but got `%s`", jsonObj.get("automatedProcess").toString()));
          }

          // validate the optional field `automatedProcess` (array)
          for (int i = 0; i < jsonArrayautomatedProcess.size(); i++) {
            AutomatedProcess.validateJsonElement(jsonArrayautomatedProcess.get(i));
          };
        }
      }
      if (jsonObj.get("contacts") != null && !jsonObj.get("contacts").isJsonNull()) {
        JsonArray jsonArraycontacts = jsonObj.getAsJsonArray("contacts");
        if (jsonArraycontacts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("contacts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `contacts` to be an array in the JSON string but got `%s`", jsonObj.get("contacts").toString()));
          }

          // validate the optional field `contacts` (array)
          for (int i = 0; i < jsonArraycontacts.size(); i++) {
            Contact.validateJsonElement(jsonArraycontacts.get(i));
          };
        }
      }
      // ensure the json data is an array
      if (!jsonObj.get("flightOffers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `flightOffers` to be an array in the JSON string but got `%s`", jsonObj.get("flightOffers").toString()));
      }

      JsonArray jsonArrayflightOffers = jsonObj.getAsJsonArray("flightOffers");
      // validate the required field `flightOffers` (array)
      for (int i = 0; i < jsonArrayflightOffers.size(); i++) {
        FlightOffer.validateJsonElement(jsonArrayflightOffers.get(i));
      };
      if (jsonObj.get("formOfIdentifications") != null && !jsonObj.get("formOfIdentifications").isJsonNull()) {
        JsonArray jsonArrayformOfIdentifications = jsonObj.getAsJsonArray("formOfIdentifications");
        if (jsonArrayformOfIdentifications != null) {
          // ensure the json data is an array
          if (!jsonObj.get("formOfIdentifications").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `formOfIdentifications` to be an array in the JSON string but got `%s`", jsonObj.get("formOfIdentifications").toString()));
          }

          // validate the optional field `formOfIdentifications` (array)
          for (int i = 0; i < jsonArrayformOfIdentifications.size(); i++) {
            FormOfIdentification.validateJsonElement(jsonArrayformOfIdentifications.get(i));
          };
        }
      }
      if (jsonObj.get("formOfPayments") != null && !jsonObj.get("formOfPayments").isJsonNull()) {
        JsonArray jsonArrayformOfPayments = jsonObj.getAsJsonArray("formOfPayments");
        if (jsonArrayformOfPayments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("formOfPayments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `formOfPayments` to be an array in the JSON string but got `%s`", jsonObj.get("formOfPayments").toString()));
          }

          // validate the optional field `formOfPayments` (array)
          for (int i = 0; i < jsonArrayformOfPayments.size(); i++) {
            FormOfPayment.validateJsonElement(jsonArrayformOfPayments.get(i));
          };
        }
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("ownerOfficeId") != null && !jsonObj.get("ownerOfficeId").isJsonNull()) && !jsonObj.get("ownerOfficeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ownerOfficeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ownerOfficeId").toString()));
      }
      if ((jsonObj.get("queuingOfficeId") != null && !jsonObj.get("queuingOfficeId").isJsonNull()) && !jsonObj.get("queuingOfficeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `queuingOfficeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("queuingOfficeId").toString()));
      }
      // validate the optional field `remarks`
      if (jsonObj.get("remarks") != null && !jsonObj.get("remarks").isJsonNull()) {
        Remarks.validateJsonElement(jsonObj.get("remarks"));
      }
      // validate the optional field `ticketingAgreement`
      if (jsonObj.get("ticketingAgreement") != null && !jsonObj.get("ticketingAgreement").isJsonNull()) {
        TicketingAgreement.validateJsonElement(jsonObj.get("ticketingAgreement"));
      }
      if (jsonObj.get("tickets") != null && !jsonObj.get("tickets").isJsonNull()) {
        JsonArray jsonArraytickets = jsonObj.getAsJsonArray("tickets");
        if (jsonArraytickets != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tickets").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tickets` to be an array in the JSON string but got `%s`", jsonObj.get("tickets").toString()));
          }

          // validate the optional field `tickets` (array)
          for (int i = 0; i < jsonArraytickets.size(); i++) {
            AirTravelDocument.validateJsonElement(jsonArraytickets.get(i));
          };
        }
      }
      if (jsonObj.get("travelers") != null && !jsonObj.get("travelers").isJsonNull()) {
        JsonArray jsonArraytravelers = jsonObj.getAsJsonArray("travelers");
        if (jsonArraytravelers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("travelers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `travelers` to be an array in the JSON string but got `%s`", jsonObj.get("travelers").toString()));
          }

          // validate the optional field `travelers` (array)
          for (int i = 0; i < jsonArraytravelers.size(); i++) {
            Traveler.validateJsonElement(jsonArraytravelers.get(i));
          };
        }
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FlightOrder.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FlightOrder' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FlightOrder> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FlightOrder.class));

       return (TypeAdapter<T>) new TypeAdapter<FlightOrder>() {
           @Override
           public void write(JsonWriter out, FlightOrder value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FlightOrder read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FlightOrder given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FlightOrder
   * @throws IOException if the JSON string is invalid with respect to FlightOrder
   */
  public static FlightOrder fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FlightOrder.class);
  }

  /**
   * Convert an instance of FlightOrder to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

