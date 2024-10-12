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

#include "OAIAllotmentDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAllotmentDetails::OAIAllotmentDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAllotmentDetails::OAIAllotmentDetails() {
    this->initializeModel();
}

OAIAllotmentDetails::~OAIAllotmentDetails() {}

void OAIAllotmentDetails::initializeModel() {

    m_tour_name_isSet = false;
    m_tour_name_isValid = false;

    m_tour_reference_isSet = false;
    m_tour_reference_isValid = false;
}

void OAIAllotmentDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAllotmentDetails::fromJsonObject(QJsonObject json) {

    m_tour_name_isValid = ::OpenAPI::fromJsonValue(m_tour_name, json[QString("tourName")]);
    m_tour_name_isSet = !json[QString("tourName")].isNull() && m_tour_name_isValid;

    m_tour_reference_isValid = ::OpenAPI::fromJsonValue(m_tour_reference, json[QString("tourReference")]);
    m_tour_reference_isSet = !json[QString("tourReference")].isNull() && m_tour_reference_isValid;
}

QString OAIAllotmentDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAllotmentDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_tour_name_isSet) {
        obj.insert(QString("tourName"), ::OpenAPI::toJsonValue(m_tour_name));
    }
    if (m_tour_reference_isSet) {
        obj.insert(QString("tourReference"), ::OpenAPI::toJsonValue(m_tour_reference));
    }
    return obj;
}

QString OAIAllotmentDetails::getTourName() const {
    return m_tour_name;
}
void OAIAllotmentDetails::setTourName(const QString &tour_name) {
    m_tour_name = tour_name;
    m_tour_name_isSet = true;
}

bool OAIAllotmentDetails::is_tour_name_Set() const{
    return m_tour_name_isSet;
}

bool OAIAllotmentDetails::is_tour_name_Valid() const{
    return m_tour_name_isValid;
}

QString OAIAllotmentDetails::getTourReference() const {
    return m_tour_reference;
}
void OAIAllotmentDetails::setTourReference(const QString &tour_reference) {
    m_tour_reference = tour_reference;
    m_tour_reference_isSet = true;
}

bool OAIAllotmentDetails::is_tour_reference_Set() const{
    return m_tour_reference_isSet;
}

bool OAIAllotmentDetails::is_tour_reference_Valid() const{
    return m_tour_reference_isValid;
}

bool OAIAllotmentDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_tour_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tour_reference_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAllotmentDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
