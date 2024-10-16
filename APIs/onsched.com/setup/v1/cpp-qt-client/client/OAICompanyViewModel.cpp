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

#include "OAICompanyViewModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICompanyViewModel::OAICompanyViewModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICompanyViewModel::OAICompanyViewModel() {
    this->initializeModel();
}

OAICompanyViewModel::~OAICompanyViewModel() {}

void OAICompanyViewModel::initializeModel() {

    m_address_line1_isSet = false;
    m_address_line1_isValid = false;

    m_address_line2_isSet = false;
    m_address_line2_isValid = false;

    m_booking_webhook_url_isSet = false;
    m_booking_webhook_url_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_client_id_isSet = false;
    m_client_id_isValid = false;

    m_client_secret_isSet = false;
    m_client_secret_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_customer_webhook_url_isSet = false;
    m_customer_webhook_url_isValid = false;

    m_deleted_status_isSet = false;
    m_deleted_status_isValid = false;

    m_deleted_time_isSet = false;
    m_deleted_time_isValid = false;

    m_disable_email_and_sms_notifications_isSet = false;
    m_disable_email_and_sms_notifications_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_fax_isSet = false;
    m_fax_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_notification_from_email_address_isSet = false;
    m_notification_from_email_address_isValid = false;

    m_notification_from_name_isSet = false;
    m_notification_from_name_isValid = false;

    m_object_isSet = false;
    m_object_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_registration_date_isSet = false;
    m_registration_date_isValid = false;

    m_registration_email_isSet = false;
    m_registration_email_isValid = false;

    m_reminder_webhook_url_isSet = false;
    m_reminder_webhook_url_isValid = false;

    m_resource_webhook_url_isSet = false;
    m_resource_webhook_url_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_timezone_id_isSet = false;
    m_timezone_id_isValid = false;

    m_timezone_name_isSet = false;
    m_timezone_name_isValid = false;

    m_webhook_signature_hash_isSet = false;
    m_webhook_signature_hash_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;
}

void OAICompanyViewModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICompanyViewModel::fromJsonObject(QJsonObject json) {

    m_address_line1_isValid = ::OpenAPI::fromJsonValue(m_address_line1, json[QString("addressLine1")]);
    m_address_line1_isSet = !json[QString("addressLine1")].isNull() && m_address_line1_isValid;

    m_address_line2_isValid = ::OpenAPI::fromJsonValue(m_address_line2, json[QString("addressLine2")]);
    m_address_line2_isSet = !json[QString("addressLine2")].isNull() && m_address_line2_isValid;

    m_booking_webhook_url_isValid = ::OpenAPI::fromJsonValue(m_booking_webhook_url, json[QString("bookingWebhookUrl")]);
    m_booking_webhook_url_isSet = !json[QString("bookingWebhookUrl")].isNull() && m_booking_webhook_url_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_client_id_isValid = ::OpenAPI::fromJsonValue(m_client_id, json[QString("clientId")]);
    m_client_id_isSet = !json[QString("clientId")].isNull() && m_client_id_isValid;

    m_client_secret_isValid = ::OpenAPI::fromJsonValue(m_client_secret, json[QString("clientSecret")]);
    m_client_secret_isSet = !json[QString("clientSecret")].isNull() && m_client_secret_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_customer_webhook_url_isValid = ::OpenAPI::fromJsonValue(m_customer_webhook_url, json[QString("customerWebhookUrl")]);
    m_customer_webhook_url_isSet = !json[QString("customerWebhookUrl")].isNull() && m_customer_webhook_url_isValid;

    m_deleted_status_isValid = ::OpenAPI::fromJsonValue(m_deleted_status, json[QString("deletedStatus")]);
    m_deleted_status_isSet = !json[QString("deletedStatus")].isNull() && m_deleted_status_isValid;

    m_deleted_time_isValid = ::OpenAPI::fromJsonValue(m_deleted_time, json[QString("deletedTime")]);
    m_deleted_time_isSet = !json[QString("deletedTime")].isNull() && m_deleted_time_isValid;

    m_disable_email_and_sms_notifications_isValid = ::OpenAPI::fromJsonValue(m_disable_email_and_sms_notifications, json[QString("disableEmailAndSmsNotifications")]);
    m_disable_email_and_sms_notifications_isSet = !json[QString("disableEmailAndSmsNotifications")].isNull() && m_disable_email_and_sms_notifications_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_fax_isValid = ::OpenAPI::fromJsonValue(m_fax, json[QString("fax")]);
    m_fax_isSet = !json[QString("fax")].isNull() && m_fax_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_notification_from_email_address_isValid = ::OpenAPI::fromJsonValue(m_notification_from_email_address, json[QString("notificationFromEmailAddress")]);
    m_notification_from_email_address_isSet = !json[QString("notificationFromEmailAddress")].isNull() && m_notification_from_email_address_isValid;

    m_notification_from_name_isValid = ::OpenAPI::fromJsonValue(m_notification_from_name, json[QString("notificationFromName")]);
    m_notification_from_name_isSet = !json[QString("notificationFromName")].isNull() && m_notification_from_name_isValid;

    m_object_isValid = ::OpenAPI::fromJsonValue(m_object, json[QString("object")]);
    m_object_isSet = !json[QString("object")].isNull() && m_object_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postalCode")]);
    m_postal_code_isSet = !json[QString("postalCode")].isNull() && m_postal_code_isValid;

    m_registration_date_isValid = ::OpenAPI::fromJsonValue(m_registration_date, json[QString("registrationDate")]);
    m_registration_date_isSet = !json[QString("registrationDate")].isNull() && m_registration_date_isValid;

    m_registration_email_isValid = ::OpenAPI::fromJsonValue(m_registration_email, json[QString("registrationEmail")]);
    m_registration_email_isSet = !json[QString("registrationEmail")].isNull() && m_registration_email_isValid;

    m_reminder_webhook_url_isValid = ::OpenAPI::fromJsonValue(m_reminder_webhook_url, json[QString("reminderWebhookUrl")]);
    m_reminder_webhook_url_isSet = !json[QString("reminderWebhookUrl")].isNull() && m_reminder_webhook_url_isValid;

    m_resource_webhook_url_isValid = ::OpenAPI::fromJsonValue(m_resource_webhook_url, json[QString("resourceWebhookUrl")]);
    m_resource_webhook_url_isSet = !json[QString("resourceWebhookUrl")].isNull() && m_resource_webhook_url_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_timezone_id_isValid = ::OpenAPI::fromJsonValue(m_timezone_id, json[QString("timezoneId")]);
    m_timezone_id_isSet = !json[QString("timezoneId")].isNull() && m_timezone_id_isValid;

    m_timezone_name_isValid = ::OpenAPI::fromJsonValue(m_timezone_name, json[QString("timezoneName")]);
    m_timezone_name_isSet = !json[QString("timezoneName")].isNull() && m_timezone_name_isValid;

    m_webhook_signature_hash_isValid = ::OpenAPI::fromJsonValue(m_webhook_signature_hash, json[QString("webhookSignatureHash")]);
    m_webhook_signature_hash_isSet = !json[QString("webhookSignatureHash")].isNull() && m_webhook_signature_hash_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;
}

QString OAICompanyViewModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICompanyViewModel::asJsonObject() const {
    QJsonObject obj;
    if (m_address_line1_isSet) {
        obj.insert(QString("addressLine1"), ::OpenAPI::toJsonValue(m_address_line1));
    }
    if (m_address_line2_isSet) {
        obj.insert(QString("addressLine2"), ::OpenAPI::toJsonValue(m_address_line2));
    }
    if (m_booking_webhook_url_isSet) {
        obj.insert(QString("bookingWebhookUrl"), ::OpenAPI::toJsonValue(m_booking_webhook_url));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_client_id_isSet) {
        obj.insert(QString("clientId"), ::OpenAPI::toJsonValue(m_client_id));
    }
    if (m_client_secret_isSet) {
        obj.insert(QString("clientSecret"), ::OpenAPI::toJsonValue(m_client_secret));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_customer_webhook_url_isSet) {
        obj.insert(QString("customerWebhookUrl"), ::OpenAPI::toJsonValue(m_customer_webhook_url));
    }
    if (m_deleted_status_isSet) {
        obj.insert(QString("deletedStatus"), ::OpenAPI::toJsonValue(m_deleted_status));
    }
    if (m_deleted_time_isSet) {
        obj.insert(QString("deletedTime"), ::OpenAPI::toJsonValue(m_deleted_time));
    }
    if (m_disable_email_and_sms_notifications_isSet) {
        obj.insert(QString("disableEmailAndSmsNotifications"), ::OpenAPI::toJsonValue(m_disable_email_and_sms_notifications));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_fax_isSet) {
        obj.insert(QString("fax"), ::OpenAPI::toJsonValue(m_fax));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_notification_from_email_address_isSet) {
        obj.insert(QString("notificationFromEmailAddress"), ::OpenAPI::toJsonValue(m_notification_from_email_address));
    }
    if (m_notification_from_name_isSet) {
        obj.insert(QString("notificationFromName"), ::OpenAPI::toJsonValue(m_notification_from_name));
    }
    if (m_object_isSet) {
        obj.insert(QString("object"), ::OpenAPI::toJsonValue(m_object));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postalCode"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_registration_date_isSet) {
        obj.insert(QString("registrationDate"), ::OpenAPI::toJsonValue(m_registration_date));
    }
    if (m_registration_email_isSet) {
        obj.insert(QString("registrationEmail"), ::OpenAPI::toJsonValue(m_registration_email));
    }
    if (m_reminder_webhook_url_isSet) {
        obj.insert(QString("reminderWebhookUrl"), ::OpenAPI::toJsonValue(m_reminder_webhook_url));
    }
    if (m_resource_webhook_url_isSet) {
        obj.insert(QString("resourceWebhookUrl"), ::OpenAPI::toJsonValue(m_resource_webhook_url));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_timezone_id_isSet) {
        obj.insert(QString("timezoneId"), ::OpenAPI::toJsonValue(m_timezone_id));
    }
    if (m_timezone_name_isSet) {
        obj.insert(QString("timezoneName"), ::OpenAPI::toJsonValue(m_timezone_name));
    }
    if (m_webhook_signature_hash_isSet) {
        obj.insert(QString("webhookSignatureHash"), ::OpenAPI::toJsonValue(m_webhook_signature_hash));
    }
    if (m_website_isSet) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    return obj;
}

QString OAICompanyViewModel::getAddressLine1() const {
    return m_address_line1;
}
void OAICompanyViewModel::setAddressLine1(const QString &address_line1) {
    m_address_line1 = address_line1;
    m_address_line1_isSet = true;
}

bool OAICompanyViewModel::is_address_line1_Set() const{
    return m_address_line1_isSet;
}

bool OAICompanyViewModel::is_address_line1_Valid() const{
    return m_address_line1_isValid;
}

QString OAICompanyViewModel::getAddressLine2() const {
    return m_address_line2;
}
void OAICompanyViewModel::setAddressLine2(const QString &address_line2) {
    m_address_line2 = address_line2;
    m_address_line2_isSet = true;
}

bool OAICompanyViewModel::is_address_line2_Set() const{
    return m_address_line2_isSet;
}

bool OAICompanyViewModel::is_address_line2_Valid() const{
    return m_address_line2_isValid;
}

QString OAICompanyViewModel::getBookingWebhookUrl() const {
    return m_booking_webhook_url;
}
void OAICompanyViewModel::setBookingWebhookUrl(const QString &booking_webhook_url) {
    m_booking_webhook_url = booking_webhook_url;
    m_booking_webhook_url_isSet = true;
}

bool OAICompanyViewModel::is_booking_webhook_url_Set() const{
    return m_booking_webhook_url_isSet;
}

bool OAICompanyViewModel::is_booking_webhook_url_Valid() const{
    return m_booking_webhook_url_isValid;
}

QString OAICompanyViewModel::getCity() const {
    return m_city;
}
void OAICompanyViewModel::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAICompanyViewModel::is_city_Set() const{
    return m_city_isSet;
}

bool OAICompanyViewModel::is_city_Valid() const{
    return m_city_isValid;
}

QString OAICompanyViewModel::getClientId() const {
    return m_client_id;
}
void OAICompanyViewModel::setClientId(const QString &client_id) {
    m_client_id = client_id;
    m_client_id_isSet = true;
}

bool OAICompanyViewModel::is_client_id_Set() const{
    return m_client_id_isSet;
}

bool OAICompanyViewModel::is_client_id_Valid() const{
    return m_client_id_isValid;
}

QString OAICompanyViewModel::getClientSecret() const {
    return m_client_secret;
}
void OAICompanyViewModel::setClientSecret(const QString &client_secret) {
    m_client_secret = client_secret;
    m_client_secret_isSet = true;
}

bool OAICompanyViewModel::is_client_secret_Set() const{
    return m_client_secret_isSet;
}

bool OAICompanyViewModel::is_client_secret_Valid() const{
    return m_client_secret_isValid;
}

QString OAICompanyViewModel::getCountry() const {
    return m_country;
}
void OAICompanyViewModel::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAICompanyViewModel::is_country_Set() const{
    return m_country_isSet;
}

bool OAICompanyViewModel::is_country_Valid() const{
    return m_country_isValid;
}

QString OAICompanyViewModel::getCustomerWebhookUrl() const {
    return m_customer_webhook_url;
}
void OAICompanyViewModel::setCustomerWebhookUrl(const QString &customer_webhook_url) {
    m_customer_webhook_url = customer_webhook_url;
    m_customer_webhook_url_isSet = true;
}

bool OAICompanyViewModel::is_customer_webhook_url_Set() const{
    return m_customer_webhook_url_isSet;
}

bool OAICompanyViewModel::is_customer_webhook_url_Valid() const{
    return m_customer_webhook_url_isValid;
}

bool OAICompanyViewModel::isDeletedStatus() const {
    return m_deleted_status;
}
void OAICompanyViewModel::setDeletedStatus(const bool &deleted_status) {
    m_deleted_status = deleted_status;
    m_deleted_status_isSet = true;
}

bool OAICompanyViewModel::is_deleted_status_Set() const{
    return m_deleted_status_isSet;
}

bool OAICompanyViewModel::is_deleted_status_Valid() const{
    return m_deleted_status_isValid;
}

QString OAICompanyViewModel::getDeletedTime() const {
    return m_deleted_time;
}
void OAICompanyViewModel::setDeletedTime(const QString &deleted_time) {
    m_deleted_time = deleted_time;
    m_deleted_time_isSet = true;
}

bool OAICompanyViewModel::is_deleted_time_Set() const{
    return m_deleted_time_isSet;
}

bool OAICompanyViewModel::is_deleted_time_Valid() const{
    return m_deleted_time_isValid;
}

bool OAICompanyViewModel::isDisableEmailAndSmsNotifications() const {
    return m_disable_email_and_sms_notifications;
}
void OAICompanyViewModel::setDisableEmailAndSmsNotifications(const bool &disable_email_and_sms_notifications) {
    m_disable_email_and_sms_notifications = disable_email_and_sms_notifications;
    m_disable_email_and_sms_notifications_isSet = true;
}

bool OAICompanyViewModel::is_disable_email_and_sms_notifications_Set() const{
    return m_disable_email_and_sms_notifications_isSet;
}

bool OAICompanyViewModel::is_disable_email_and_sms_notifications_Valid() const{
    return m_disable_email_and_sms_notifications_isValid;
}

QString OAICompanyViewModel::getEmail() const {
    return m_email;
}
void OAICompanyViewModel::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAICompanyViewModel::is_email_Set() const{
    return m_email_isSet;
}

bool OAICompanyViewModel::is_email_Valid() const{
    return m_email_isValid;
}

QString OAICompanyViewModel::getFax() const {
    return m_fax;
}
void OAICompanyViewModel::setFax(const QString &fax) {
    m_fax = fax;
    m_fax_isSet = true;
}

bool OAICompanyViewModel::is_fax_Set() const{
    return m_fax_isSet;
}

bool OAICompanyViewModel::is_fax_Valid() const{
    return m_fax_isValid;
}

QString OAICompanyViewModel::getId() const {
    return m_id;
}
void OAICompanyViewModel::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICompanyViewModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAICompanyViewModel::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICompanyViewModel::getName() const {
    return m_name;
}
void OAICompanyViewModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICompanyViewModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAICompanyViewModel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICompanyViewModel::getNotificationFromEmailAddress() const {
    return m_notification_from_email_address;
}
void OAICompanyViewModel::setNotificationFromEmailAddress(const QString &notification_from_email_address) {
    m_notification_from_email_address = notification_from_email_address;
    m_notification_from_email_address_isSet = true;
}

bool OAICompanyViewModel::is_notification_from_email_address_Set() const{
    return m_notification_from_email_address_isSet;
}

bool OAICompanyViewModel::is_notification_from_email_address_Valid() const{
    return m_notification_from_email_address_isValid;
}

QString OAICompanyViewModel::getNotificationFromName() const {
    return m_notification_from_name;
}
void OAICompanyViewModel::setNotificationFromName(const QString &notification_from_name) {
    m_notification_from_name = notification_from_name;
    m_notification_from_name_isSet = true;
}

bool OAICompanyViewModel::is_notification_from_name_Set() const{
    return m_notification_from_name_isSet;
}

bool OAICompanyViewModel::is_notification_from_name_Valid() const{
    return m_notification_from_name_isValid;
}

QString OAICompanyViewModel::getObject() const {
    return m_object;
}
void OAICompanyViewModel::setObject(const QString &object) {
    m_object = object;
    m_object_isSet = true;
}

bool OAICompanyViewModel::is_object_Set() const{
    return m_object_isSet;
}

bool OAICompanyViewModel::is_object_Valid() const{
    return m_object_isValid;
}

QString OAICompanyViewModel::getPhone() const {
    return m_phone;
}
void OAICompanyViewModel::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAICompanyViewModel::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAICompanyViewModel::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAICompanyViewModel::getPostalCode() const {
    return m_postal_code;
}
void OAICompanyViewModel::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAICompanyViewModel::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAICompanyViewModel::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

QString OAICompanyViewModel::getRegistrationDate() const {
    return m_registration_date;
}
void OAICompanyViewModel::setRegistrationDate(const QString &registration_date) {
    m_registration_date = registration_date;
    m_registration_date_isSet = true;
}

bool OAICompanyViewModel::is_registration_date_Set() const{
    return m_registration_date_isSet;
}

bool OAICompanyViewModel::is_registration_date_Valid() const{
    return m_registration_date_isValid;
}

QString OAICompanyViewModel::getRegistrationEmail() const {
    return m_registration_email;
}
void OAICompanyViewModel::setRegistrationEmail(const QString &registration_email) {
    m_registration_email = registration_email;
    m_registration_email_isSet = true;
}

bool OAICompanyViewModel::is_registration_email_Set() const{
    return m_registration_email_isSet;
}

bool OAICompanyViewModel::is_registration_email_Valid() const{
    return m_registration_email_isValid;
}

QString OAICompanyViewModel::getReminderWebhookUrl() const {
    return m_reminder_webhook_url;
}
void OAICompanyViewModel::setReminderWebhookUrl(const QString &reminder_webhook_url) {
    m_reminder_webhook_url = reminder_webhook_url;
    m_reminder_webhook_url_isSet = true;
}

bool OAICompanyViewModel::is_reminder_webhook_url_Set() const{
    return m_reminder_webhook_url_isSet;
}

bool OAICompanyViewModel::is_reminder_webhook_url_Valid() const{
    return m_reminder_webhook_url_isValid;
}

QString OAICompanyViewModel::getResourceWebhookUrl() const {
    return m_resource_webhook_url;
}
void OAICompanyViewModel::setResourceWebhookUrl(const QString &resource_webhook_url) {
    m_resource_webhook_url = resource_webhook_url;
    m_resource_webhook_url_isSet = true;
}

bool OAICompanyViewModel::is_resource_webhook_url_Set() const{
    return m_resource_webhook_url_isSet;
}

bool OAICompanyViewModel::is_resource_webhook_url_Valid() const{
    return m_resource_webhook_url_isValid;
}

QString OAICompanyViewModel::getState() const {
    return m_state;
}
void OAICompanyViewModel::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAICompanyViewModel::is_state_Set() const{
    return m_state_isSet;
}

bool OAICompanyViewModel::is_state_Valid() const{
    return m_state_isValid;
}

QString OAICompanyViewModel::getTimezoneId() const {
    return m_timezone_id;
}
void OAICompanyViewModel::setTimezoneId(const QString &timezone_id) {
    m_timezone_id = timezone_id;
    m_timezone_id_isSet = true;
}

bool OAICompanyViewModel::is_timezone_id_Set() const{
    return m_timezone_id_isSet;
}

bool OAICompanyViewModel::is_timezone_id_Valid() const{
    return m_timezone_id_isValid;
}

QString OAICompanyViewModel::getTimezoneName() const {
    return m_timezone_name;
}
void OAICompanyViewModel::setTimezoneName(const QString &timezone_name) {
    m_timezone_name = timezone_name;
    m_timezone_name_isSet = true;
}

bool OAICompanyViewModel::is_timezone_name_Set() const{
    return m_timezone_name_isSet;
}

bool OAICompanyViewModel::is_timezone_name_Valid() const{
    return m_timezone_name_isValid;
}

QString OAICompanyViewModel::getWebhookSignatureHash() const {
    return m_webhook_signature_hash;
}
void OAICompanyViewModel::setWebhookSignatureHash(const QString &webhook_signature_hash) {
    m_webhook_signature_hash = webhook_signature_hash;
    m_webhook_signature_hash_isSet = true;
}

bool OAICompanyViewModel::is_webhook_signature_hash_Set() const{
    return m_webhook_signature_hash_isSet;
}

bool OAICompanyViewModel::is_webhook_signature_hash_Valid() const{
    return m_webhook_signature_hash_isValid;
}

QString OAICompanyViewModel::getWebsite() const {
    return m_website;
}
void OAICompanyViewModel::setWebsite(const QString &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAICompanyViewModel::is_website_Set() const{
    return m_website_isSet;
}

bool OAICompanyViewModel::is_website_Valid() const{
    return m_website_isValid;
}

bool OAICompanyViewModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_line1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_address_line2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_booking_webhook_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_secret_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_webhook_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_disable_email_and_sms_notifications_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notification_from_email_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notification_from_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_object_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_registration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_registration_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reminder_webhook_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_webhook_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_webhook_signature_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICompanyViewModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
