/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAvailabilityClass.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailabilityClass::OAIAvailabilityClass(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailabilityClass::OAIAvailabilityClass() {
    this->initializeModel();
}

OAIAvailabilityClass::~OAIAvailabilityClass() {}

void OAIAvailabilityClass::initializeModel() {

    m_r_class_isSet = false;
    m_r_class_isValid = false;

    m_closed_status_isSet = false;
    m_closed_status_isValid = false;

    m_number_of_bookable_seats_isSet = false;
    m_number_of_bookable_seats_isValid = false;

    m_tour_allotment_isSet = false;
    m_tour_allotment_isValid = false;
}

void OAIAvailabilityClass::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailabilityClass::fromJsonObject(QJsonObject json) {

    m_r_class_isValid = ::OpenAPI::fromJsonValue(m_r_class, json[QString("class")]);
    m_r_class_isSet = !json[QString("class")].isNull() && m_r_class_isValid;

    m_closed_status_isValid = ::OpenAPI::fromJsonValue(m_closed_status, json[QString("closedStatus")]);
    m_closed_status_isSet = !json[QString("closedStatus")].isNull() && m_closed_status_isValid;

    m_number_of_bookable_seats_isValid = ::OpenAPI::fromJsonValue(m_number_of_bookable_seats, json[QString("numberOfBookableSeats")]);
    m_number_of_bookable_seats_isSet = !json[QString("numberOfBookableSeats")].isNull() && m_number_of_bookable_seats_isValid;

    m_tour_allotment_isValid = ::OpenAPI::fromJsonValue(m_tour_allotment, json[QString("tourAllotment")]);
    m_tour_allotment_isSet = !json[QString("tourAllotment")].isNull() && m_tour_allotment_isValid;
}

QString OAIAvailabilityClass::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailabilityClass::asJsonObject() const {
    QJsonObject obj;
    if (m_r_class_isSet) {
        obj.insert(QString("class"), ::OpenAPI::toJsonValue(m_r_class));
    }
    if (m_closed_status_isSet) {
        obj.insert(QString("closedStatus"), ::OpenAPI::toJsonValue(m_closed_status));
    }
    if (m_number_of_bookable_seats_isSet) {
        obj.insert(QString("numberOfBookableSeats"), ::OpenAPI::toJsonValue(m_number_of_bookable_seats));
    }
    if (m_tour_allotment.isSet()) {
        obj.insert(QString("tourAllotment"), ::OpenAPI::toJsonValue(m_tour_allotment));
    }
    return obj;
}

QString OAIAvailabilityClass::getRClass() const {
    return m_r_class;
}
void OAIAvailabilityClass::setRClass(const QString &r_class) {
    m_r_class = r_class;
    m_r_class_isSet = true;
}

bool OAIAvailabilityClass::is_r_class_Set() const{
    return m_r_class_isSet;
}

bool OAIAvailabilityClass::is_r_class_Valid() const{
    return m_r_class_isValid;
}

QString OAIAvailabilityClass::getClosedStatus() const {
    return m_closed_status;
}
void OAIAvailabilityClass::setClosedStatus(const QString &closed_status) {
    m_closed_status = closed_status;
    m_closed_status_isSet = true;
}

bool OAIAvailabilityClass::is_closed_status_Set() const{
    return m_closed_status_isSet;
}

bool OAIAvailabilityClass::is_closed_status_Valid() const{
    return m_closed_status_isValid;
}

double OAIAvailabilityClass::getNumberOfBookableSeats() const {
    return m_number_of_bookable_seats;
}
void OAIAvailabilityClass::setNumberOfBookableSeats(const double &number_of_bookable_seats) {
    m_number_of_bookable_seats = number_of_bookable_seats;
    m_number_of_bookable_seats_isSet = true;
}

bool OAIAvailabilityClass::is_number_of_bookable_seats_Set() const{
    return m_number_of_bookable_seats_isSet;
}

bool OAIAvailabilityClass::is_number_of_bookable_seats_Valid() const{
    return m_number_of_bookable_seats_isValid;
}

OAITourAllotment OAIAvailabilityClass::getTourAllotment() const {
    return m_tour_allotment;
}
void OAIAvailabilityClass::setTourAllotment(const OAITourAllotment &tour_allotment) {
    m_tour_allotment = tour_allotment;
    m_tour_allotment_isSet = true;
}

bool OAIAvailabilityClass::is_tour_allotment_Set() const{
    return m_tour_allotment_isSet;
}

bool OAIAvailabilityClass::is_tour_allotment_Valid() const{
    return m_tour_allotment_isValid;
}

bool OAIAvailabilityClass::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_class_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_closed_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_bookable_seats_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tour_allotment.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailabilityClass::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
