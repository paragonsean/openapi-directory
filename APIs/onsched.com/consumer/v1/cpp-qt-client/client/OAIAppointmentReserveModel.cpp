/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppointmentReserveModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppointmentReserveModel::OAIAppointmentReserveModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppointmentReserveModel::OAIAppointmentReserveModel() {
    this->initializeModel();
}

OAIAppointmentReserveModel::~OAIAppointmentReserveModel() {}

void OAIAppointmentReserveModel::initializeModel() {

    m_appointment_booking_fields_isSet = false;
    m_appointment_booking_fields_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_customer_booking_fields_isSet = false;
    m_customer_booking_fields_isValid = false;

    m_customer_message_isSet = false;
    m_customer_message_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_phone_ext_isSet = false;
    m_phone_ext_isValid = false;

    m_phone_type_isSet = false;
    m_phone_type_isValid = false;
}

void OAIAppointmentReserveModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppointmentReserveModel::fromJsonObject(QJsonObject json) {

    m_appointment_booking_fields_isValid = ::OpenAPI::fromJsonValue(m_appointment_booking_fields, json[QString("appointmentBookingFields")]);
    m_appointment_booking_fields_isSet = !json[QString("appointmentBookingFields")].isNull() && m_appointment_booking_fields_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_customer_booking_fields_isValid = ::OpenAPI::fromJsonValue(m_customer_booking_fields, json[QString("customerBookingFields")]);
    m_customer_booking_fields_isSet = !json[QString("customerBookingFields")].isNull() && m_customer_booking_fields_isValid;

    m_customer_message_isValid = ::OpenAPI::fromJsonValue(m_customer_message, json[QString("customerMessage")]);
    m_customer_message_isSet = !json[QString("customerMessage")].isNull() && m_customer_message_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_phone_ext_isValid = ::OpenAPI::fromJsonValue(m_phone_ext, json[QString("phoneExt")]);
    m_phone_ext_isSet = !json[QString("phoneExt")].isNull() && m_phone_ext_isValid;

    m_phone_type_isValid = ::OpenAPI::fromJsonValue(m_phone_type, json[QString("phoneType")]);
    m_phone_type_isSet = !json[QString("phoneType")].isNull() && m_phone_type_isValid;
}

QString OAIAppointmentReserveModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppointmentReserveModel::asJsonObject() const {
    QJsonObject obj;
    if (m_appointment_booking_fields.size() > 0) {
        obj.insert(QString("appointmentBookingFields"), ::OpenAPI::toJsonValue(m_appointment_booking_fields));
    }
    if (m_custom_fields.isSet()) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_customer_booking_fields.size() > 0) {
        obj.insert(QString("customerBookingFields"), ::OpenAPI::toJsonValue(m_customer_booking_fields));
    }
    if (m_customer_message_isSet) {
        obj.insert(QString("customerMessage"), ::OpenAPI::toJsonValue(m_customer_message));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_phone_ext_isSet) {
        obj.insert(QString("phoneExt"), ::OpenAPI::toJsonValue(m_phone_ext));
    }
    if (m_phone_type_isSet) {
        obj.insert(QString("phoneType"), ::OpenAPI::toJsonValue(m_phone_type));
    }
    return obj;
}

QList<OAIBookingFieldItem> OAIAppointmentReserveModel::getAppointmentBookingFields() const {
    return m_appointment_booking_fields;
}
void OAIAppointmentReserveModel::setAppointmentBookingFields(const QList<OAIBookingFieldItem> &appointment_booking_fields) {
    m_appointment_booking_fields = appointment_booking_fields;
    m_appointment_booking_fields_isSet = true;
}

bool OAIAppointmentReserveModel::is_appointment_booking_fields_Set() const{
    return m_appointment_booking_fields_isSet;
}

bool OAIAppointmentReserveModel::is_appointment_booking_fields_Valid() const{
    return m_appointment_booking_fields_isValid;
}

OAICustomFieldInputModel OAIAppointmentReserveModel::getCustomFields() const {
    return m_custom_fields;
}
void OAIAppointmentReserveModel::setCustomFields(const OAICustomFieldInputModel &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIAppointmentReserveModel::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIAppointmentReserveModel::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QList<OAIBookingFieldItem> OAIAppointmentReserveModel::getCustomerBookingFields() const {
    return m_customer_booking_fields;
}
void OAIAppointmentReserveModel::setCustomerBookingFields(const QList<OAIBookingFieldItem> &customer_booking_fields) {
    m_customer_booking_fields = customer_booking_fields;
    m_customer_booking_fields_isSet = true;
}

bool OAIAppointmentReserveModel::is_customer_booking_fields_Set() const{
    return m_customer_booking_fields_isSet;
}

bool OAIAppointmentReserveModel::is_customer_booking_fields_Valid() const{
    return m_customer_booking_fields_isValid;
}

QString OAIAppointmentReserveModel::getCustomerMessage() const {
    return m_customer_message;
}
void OAIAppointmentReserveModel::setCustomerMessage(const QString &customer_message) {
    m_customer_message = customer_message;
    m_customer_message_isSet = true;
}

bool OAIAppointmentReserveModel::is_customer_message_Set() const{
    return m_customer_message_isSet;
}

bool OAIAppointmentReserveModel::is_customer_message_Valid() const{
    return m_customer_message_isValid;
}

QString OAIAppointmentReserveModel::getEmail() const {
    return m_email;
}
void OAIAppointmentReserveModel::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIAppointmentReserveModel::is_email_Set() const{
    return m_email_isSet;
}

bool OAIAppointmentReserveModel::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIAppointmentReserveModel::getName() const {
    return m_name;
}
void OAIAppointmentReserveModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAppointmentReserveModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAppointmentReserveModel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAppointmentReserveModel::getNotes() const {
    return m_notes;
}
void OAIAppointmentReserveModel::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIAppointmentReserveModel::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIAppointmentReserveModel::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAIAppointmentReserveModel::getPhone() const {
    return m_phone;
}
void OAIAppointmentReserveModel::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAIAppointmentReserveModel::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAIAppointmentReserveModel::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAIAppointmentReserveModel::getPhoneExt() const {
    return m_phone_ext;
}
void OAIAppointmentReserveModel::setPhoneExt(const QString &phone_ext) {
    m_phone_ext = phone_ext;
    m_phone_ext_isSet = true;
}

bool OAIAppointmentReserveModel::is_phone_ext_Set() const{
    return m_phone_ext_isSet;
}

bool OAIAppointmentReserveModel::is_phone_ext_Valid() const{
    return m_phone_ext_isValid;
}

QString OAIAppointmentReserveModel::getPhoneType() const {
    return m_phone_type;
}
void OAIAppointmentReserveModel::setPhoneType(const QString &phone_type) {
    m_phone_type = phone_type;
    m_phone_type_isSet = true;
}

bool OAIAppointmentReserveModel::is_phone_type_Set() const{
    return m_phone_type_isSet;
}

bool OAIAppointmentReserveModel::is_phone_type_Valid() const{
    return m_phone_type_isValid;
}

bool OAIAppointmentReserveModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appointment_booking_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_booking_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_ext_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppointmentReserveModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
