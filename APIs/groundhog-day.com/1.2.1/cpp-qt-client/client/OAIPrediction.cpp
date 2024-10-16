/**
 * Groundhog Day API
 * This API returns all of North America’s prognosticating animals and their yearly weather predictions.
 *
 * The version of the OpenAPI document: 1.2.1
 * Contact: hello@groundhog-day.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPrediction.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPrediction::OAIPrediction(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPrediction::OAIPrediction() {
    this->initializeModel();
}

OAIPrediction::~OAIPrediction() {}

void OAIPrediction::initializeModel() {

    m_details_isSet = false;
    m_details_isValid = false;

    m_groundhog_isSet = false;
    m_groundhog_isValid = false;

    m_shadow_isSet = false;
    m_shadow_isValid = false;

    m_year_isSet = false;
    m_year_isValid = false;
}

void OAIPrediction::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPrediction::fromJsonObject(QJsonObject json) {

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_groundhog_isValid = ::OpenAPI::fromJsonValue(m_groundhog, json[QString("groundhog")]);
    m_groundhog_isSet = !json[QString("groundhog")].isNull() && m_groundhog_isValid;

    m_shadow_isValid = ::OpenAPI::fromJsonValue(m_shadow, json[QString("shadow")]);
    m_shadow_isSet = !json[QString("shadow")].isNull() && m_shadow_isValid;

    m_year_isValid = ::OpenAPI::fromJsonValue(m_year, json[QString("year")]);
    m_year_isSet = !json[QString("year")].isNull() && m_year_isValid;
}

QString OAIPrediction::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPrediction::asJsonObject() const {
    QJsonObject obj;
    if (m_details_isSet) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_groundhog.isSet()) {
        obj.insert(QString("groundhog"), ::OpenAPI::toJsonValue(m_groundhog));
    }
    if (m_shadow_isSet) {
        obj.insert(QString("shadow"), ::OpenAPI::toJsonValue(m_shadow));
    }
    if (m_year_isSet) {
        obj.insert(QString("year"), ::OpenAPI::toJsonValue(m_year));
    }
    return obj;
}

QString OAIPrediction::getDetails() const {
    return m_details;
}
void OAIPrediction::setDetails(const QString &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIPrediction::is_details_Set() const{
    return m_details_isSet;
}

bool OAIPrediction::is_details_Valid() const{
    return m_details_isValid;
}

OAIGroundhog OAIPrediction::getGroundhog() const {
    return m_groundhog;
}
void OAIPrediction::setGroundhog(const OAIGroundhog &groundhog) {
    m_groundhog = groundhog;
    m_groundhog_isSet = true;
}

bool OAIPrediction::is_groundhog_Set() const{
    return m_groundhog_isSet;
}

bool OAIPrediction::is_groundhog_Valid() const{
    return m_groundhog_isValid;
}

qint32 OAIPrediction::getShadow() const {
    return m_shadow;
}
void OAIPrediction::setShadow(const qint32 &shadow) {
    m_shadow = shadow;
    m_shadow_isSet = true;
}

bool OAIPrediction::is_shadow_Set() const{
    return m_shadow_isSet;
}

bool OAIPrediction::is_shadow_Valid() const{
    return m_shadow_isValid;
}

qint32 OAIPrediction::getYear() const {
    return m_year;
}
void OAIPrediction::setYear(const qint32 &year) {
    m_year = year;
    m_year_isSet = true;
}

bool OAIPrediction::is_year_Set() const{
    return m_year_isSet;
}

bool OAIPrediction::is_year_Valid() const{
    return m_year_isValid;
}

bool OAIPrediction::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_details_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_groundhog.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_shadow_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPrediction::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_details_isValid && m_shadow_isValid && m_year_isValid && true;
}

} // namespace OpenAPI
