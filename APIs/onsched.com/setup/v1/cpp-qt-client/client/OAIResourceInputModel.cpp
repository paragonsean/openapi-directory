/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResourceInputModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResourceInputModel::OAIResourceInputModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResourceInputModel::OAIResourceInputModel() {
    this->initializeModel();
}

OAIResourceInputModel::~OAIResourceInputModel() {}

void OAIResourceInputModel::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_availability_isSet = false;
    m_availability_isValid = false;

    m_contact_isSet = false;
    m_contact_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_group_id_isSet = false;
    m_group_id_isValid = false;

    m_location_id_isSet = false;
    m_location_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;

    m_recurring_availability_isSet = false;
    m_recurring_availability_isValid = false;

    m_service_ids_isSet = false;
    m_service_ids_isValid = false;

    m_timezone_id_isSet = false;
    m_timezone_id_isValid = false;
}

void OAIResourceInputModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResourceInputModel::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_availability_isValid = ::OpenAPI::fromJsonValue(m_availability, json[QString("availability")]);
    m_availability_isSet = !json[QString("availability")].isNull() && m_availability_isValid;

    m_contact_isValid = ::OpenAPI::fromJsonValue(m_contact, json[QString("contact")]);
    m_contact_isSet = !json[QString("contact")].isNull() && m_contact_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_group_id_isValid = ::OpenAPI::fromJsonValue(m_group_id, json[QString("groupId")]);
    m_group_id_isSet = !json[QString("groupId")].isNull() && m_group_id_isValid;

    m_location_id_isValid = ::OpenAPI::fromJsonValue(m_location_id, json[QString("locationId")]);
    m_location_id_isSet = !json[QString("locationId")].isNull() && m_location_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;

    m_recurring_availability_isValid = ::OpenAPI::fromJsonValue(m_recurring_availability, json[QString("recurringAvailability")]);
    m_recurring_availability_isSet = !json[QString("recurringAvailability")].isNull() && m_recurring_availability_isValid;

    m_service_ids_isValid = ::OpenAPI::fromJsonValue(m_service_ids, json[QString("serviceIds")]);
    m_service_ids_isSet = !json[QString("serviceIds")].isNull() && m_service_ids_isValid;

    m_timezone_id_isValid = ::OpenAPI::fromJsonValue(m_timezone_id, json[QString("timezoneId")]);
    m_timezone_id_isSet = !json[QString("timezoneId")].isNull() && m_timezone_id_isValid;
}

QString OAIResourceInputModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResourceInputModel::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_availability.isSet()) {
        obj.insert(QString("availability"), ::OpenAPI::toJsonValue(m_availability));
    }
    if (m_contact.isSet()) {
        obj.insert(QString("contact"), ::OpenAPI::toJsonValue(m_contact));
    }
    if (m_custom_fields.isSet()) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_group_id_isSet) {
        obj.insert(QString("groupId"), ::OpenAPI::toJsonValue(m_group_id));
    }
    if (m_location_id_isSet) {
        obj.insert(QString("locationId"), ::OpenAPI::toJsonValue(m_location_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_options.isSet()) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    if (m_recurring_availability_isSet) {
        obj.insert(QString("recurringAvailability"), ::OpenAPI::toJsonValue(m_recurring_availability));
    }
    if (m_service_ids.size() > 0) {
        obj.insert(QString("serviceIds"), ::OpenAPI::toJsonValue(m_service_ids));
    }
    if (m_timezone_id_isSet) {
        obj.insert(QString("timezoneId"), ::OpenAPI::toJsonValue(m_timezone_id));
    }
    return obj;
}

OAIAddressInputModel OAIResourceInputModel::getAddress() const {
    return m_address;
}
void OAIResourceInputModel::setAddress(const OAIAddressInputModel &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIResourceInputModel::is_address_Set() const{
    return m_address_isSet;
}

bool OAIResourceInputModel::is_address_Valid() const{
    return m_address_isValid;
}

OAIAvailabilityInputModel OAIResourceInputModel::getAvailability() const {
    return m_availability;
}
void OAIResourceInputModel::setAvailability(const OAIAvailabilityInputModel &availability) {
    m_availability = availability;
    m_availability_isSet = true;
}

bool OAIResourceInputModel::is_availability_Set() const{
    return m_availability_isSet;
}

bool OAIResourceInputModel::is_availability_Valid() const{
    return m_availability_isValid;
}

OAIContactInputModel OAIResourceInputModel::getContact() const {
    return m_contact;
}
void OAIResourceInputModel::setContact(const OAIContactInputModel &contact) {
    m_contact = contact;
    m_contact_isSet = true;
}

bool OAIResourceInputModel::is_contact_Set() const{
    return m_contact_isSet;
}

bool OAIResourceInputModel::is_contact_Valid() const{
    return m_contact_isValid;
}

OAICustomFieldInputModel OAIResourceInputModel::getCustomFields() const {
    return m_custom_fields;
}
void OAIResourceInputModel::setCustomFields(const OAICustomFieldInputModel &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIResourceInputModel::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIResourceInputModel::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIResourceInputModel::getDescription() const {
    return m_description;
}
void OAIResourceInputModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIResourceInputModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIResourceInputModel::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIResourceInputModel::getEmail() const {
    return m_email;
}
void OAIResourceInputModel::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIResourceInputModel::is_email_Set() const{
    return m_email_isSet;
}

bool OAIResourceInputModel::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIResourceInputModel::getGroupId() const {
    return m_group_id;
}
void OAIResourceInputModel::setGroupId(const QString &group_id) {
    m_group_id = group_id;
    m_group_id_isSet = true;
}

bool OAIResourceInputModel::is_group_id_Set() const{
    return m_group_id_isSet;
}

bool OAIResourceInputModel::is_group_id_Valid() const{
    return m_group_id_isValid;
}

QString OAIResourceInputModel::getLocationId() const {
    return m_location_id;
}
void OAIResourceInputModel::setLocationId(const QString &location_id) {
    m_location_id = location_id;
    m_location_id_isSet = true;
}

bool OAIResourceInputModel::is_location_id_Set() const{
    return m_location_id_isSet;
}

bool OAIResourceInputModel::is_location_id_Valid() const{
    return m_location_id_isValid;
}

QString OAIResourceInputModel::getName() const {
    return m_name;
}
void OAIResourceInputModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIResourceInputModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIResourceInputModel::is_name_Valid() const{
    return m_name_isValid;
}

OAIResourceOptionsInputModel OAIResourceInputModel::getOptions() const {
    return m_options;
}
void OAIResourceInputModel::setOptions(const OAIResourceOptionsInputModel &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIResourceInputModel::is_options_Set() const{
    return m_options_isSet;
}

bool OAIResourceInputModel::is_options_Valid() const{
    return m_options_isValid;
}

bool OAIResourceInputModel::isRecurringAvailability() const {
    return m_recurring_availability;
}
void OAIResourceInputModel::setRecurringAvailability(const bool &recurring_availability) {
    m_recurring_availability = recurring_availability;
    m_recurring_availability_isSet = true;
}

bool OAIResourceInputModel::is_recurring_availability_Set() const{
    return m_recurring_availability_isSet;
}

bool OAIResourceInputModel::is_recurring_availability_Valid() const{
    return m_recurring_availability_isValid;
}

QList<QString> OAIResourceInputModel::getServiceIds() const {
    return m_service_ids;
}
void OAIResourceInputModel::setServiceIds(const QList<QString> &service_ids) {
    m_service_ids = service_ids;
    m_service_ids_isSet = true;
}

bool OAIResourceInputModel::is_service_ids_Set() const{
    return m_service_ids_isSet;
}

bool OAIResourceInputModel::is_service_ids_Valid() const{
    return m_service_ids_isValid;
}

QString OAIResourceInputModel::getTimezoneId() const {
    return m_timezone_id;
}
void OAIResourceInputModel::setTimezoneId(const QString &timezone_id) {
    m_timezone_id = timezone_id;
    m_timezone_id_isSet = true;
}

bool OAIResourceInputModel::is_timezone_id_Set() const{
    return m_timezone_id_isSet;
}

bool OAIResourceInputModel::is_timezone_id_Valid() const{
    return m_timezone_id_isValid;
}

bool OAIResourceInputModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_availability.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurring_availability_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResourceInputModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
