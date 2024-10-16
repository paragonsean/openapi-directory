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

#include "OAIAppoinmentBookingFormsViewModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppoinmentBookingFormsViewModel::OAIAppoinmentBookingFormsViewModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppoinmentBookingFormsViewModel::OAIAppoinmentBookingFormsViewModel() {
    this->initializeModel();
}

OAIAppoinmentBookingFormsViewModel::~OAIAppoinmentBookingFormsViewModel() {}

void OAIAppoinmentBookingFormsViewModel::initializeModel() {

    m_booking_confirmation_page_isSet = false;
    m_booking_confirmation_page_isValid = false;

    m_booking_form_isSet = false;
    m_booking_form_isValid = false;
}

void OAIAppoinmentBookingFormsViewModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppoinmentBookingFormsViewModel::fromJsonObject(QJsonObject json) {

    m_booking_confirmation_page_isValid = ::OpenAPI::fromJsonValue(m_booking_confirmation_page, json[QString("bookingConfirmationPage")]);
    m_booking_confirmation_page_isSet = !json[QString("bookingConfirmationPage")].isNull() && m_booking_confirmation_page_isValid;

    m_booking_form_isValid = ::OpenAPI::fromJsonValue(m_booking_form, json[QString("bookingForm")]);
    m_booking_form_isSet = !json[QString("bookingForm")].isNull() && m_booking_form_isValid;
}

QString OAIAppoinmentBookingFormsViewModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppoinmentBookingFormsViewModel::asJsonObject() const {
    QJsonObject obj;
    if (m_booking_confirmation_page_isSet) {
        obj.insert(QString("bookingConfirmationPage"), ::OpenAPI::toJsonValue(m_booking_confirmation_page));
    }
    if (m_booking_form_isSet) {
        obj.insert(QString("bookingForm"), ::OpenAPI::toJsonValue(m_booking_form));
    }
    return obj;
}

QString OAIAppoinmentBookingFormsViewModel::getBookingConfirmationPage() const {
    return m_booking_confirmation_page;
}
void OAIAppoinmentBookingFormsViewModel::setBookingConfirmationPage(const QString &booking_confirmation_page) {
    m_booking_confirmation_page = booking_confirmation_page;
    m_booking_confirmation_page_isSet = true;
}

bool OAIAppoinmentBookingFormsViewModel::is_booking_confirmation_page_Set() const{
    return m_booking_confirmation_page_isSet;
}

bool OAIAppoinmentBookingFormsViewModel::is_booking_confirmation_page_Valid() const{
    return m_booking_confirmation_page_isValid;
}

QString OAIAppoinmentBookingFormsViewModel::getBookingForm() const {
    return m_booking_form;
}
void OAIAppoinmentBookingFormsViewModel::setBookingForm(const QString &booking_form) {
    m_booking_form = booking_form;
    m_booking_form_isSet = true;
}

bool OAIAppoinmentBookingFormsViewModel::is_booking_form_Set() const{
    return m_booking_form_isSet;
}

bool OAIAppoinmentBookingFormsViewModel::is_booking_form_Valid() const{
    return m_booking_form_isValid;
}

bool OAIAppoinmentBookingFormsViewModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_booking_confirmation_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_booking_form_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppoinmentBookingFormsViewModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
