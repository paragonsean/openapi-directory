/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRotatingBarcodeTotpDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRotatingBarcodeTotpDetails::OAIRotatingBarcodeTotpDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRotatingBarcodeTotpDetails::OAIRotatingBarcodeTotpDetails() {
    this->initializeModel();
}

OAIRotatingBarcodeTotpDetails::~OAIRotatingBarcodeTotpDetails() {}

void OAIRotatingBarcodeTotpDetails::initializeModel() {

    m_algorithm_isSet = false;
    m_algorithm_isValid = false;

    m_parameters_isSet = false;
    m_parameters_isValid = false;

    m_period_millis_isSet = false;
    m_period_millis_isValid = false;
}

void OAIRotatingBarcodeTotpDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRotatingBarcodeTotpDetails::fromJsonObject(QJsonObject json) {

    m_algorithm_isValid = ::OpenAPI::fromJsonValue(m_algorithm, json[QString("algorithm")]);
    m_algorithm_isSet = !json[QString("algorithm")].isNull() && m_algorithm_isValid;

    m_parameters_isValid = ::OpenAPI::fromJsonValue(m_parameters, json[QString("parameters")]);
    m_parameters_isSet = !json[QString("parameters")].isNull() && m_parameters_isValid;

    m_period_millis_isValid = ::OpenAPI::fromJsonValue(m_period_millis, json[QString("periodMillis")]);
    m_period_millis_isSet = !json[QString("periodMillis")].isNull() && m_period_millis_isValid;
}

QString OAIRotatingBarcodeTotpDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRotatingBarcodeTotpDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_algorithm_isSet) {
        obj.insert(QString("algorithm"), ::OpenAPI::toJsonValue(m_algorithm));
    }
    if (m_parameters.size() > 0) {
        obj.insert(QString("parameters"), ::OpenAPI::toJsonValue(m_parameters));
    }
    if (m_period_millis_isSet) {
        obj.insert(QString("periodMillis"), ::OpenAPI::toJsonValue(m_period_millis));
    }
    return obj;
}

QString OAIRotatingBarcodeTotpDetails::getAlgorithm() const {
    return m_algorithm;
}
void OAIRotatingBarcodeTotpDetails::setAlgorithm(const QString &algorithm) {
    m_algorithm = algorithm;
    m_algorithm_isSet = true;
}

bool OAIRotatingBarcodeTotpDetails::is_algorithm_Set() const{
    return m_algorithm_isSet;
}

bool OAIRotatingBarcodeTotpDetails::is_algorithm_Valid() const{
    return m_algorithm_isValid;
}

QList<OAIRotatingBarcodeTotpDetailsTotpParameters> OAIRotatingBarcodeTotpDetails::getParameters() const {
    return m_parameters;
}
void OAIRotatingBarcodeTotpDetails::setParameters(const QList<OAIRotatingBarcodeTotpDetailsTotpParameters> &parameters) {
    m_parameters = parameters;
    m_parameters_isSet = true;
}

bool OAIRotatingBarcodeTotpDetails::is_parameters_Set() const{
    return m_parameters_isSet;
}

bool OAIRotatingBarcodeTotpDetails::is_parameters_Valid() const{
    return m_parameters_isValid;
}

QString OAIRotatingBarcodeTotpDetails::getPeriodMillis() const {
    return m_period_millis;
}
void OAIRotatingBarcodeTotpDetails::setPeriodMillis(const QString &period_millis) {
    m_period_millis = period_millis;
    m_period_millis_isSet = true;
}

bool OAIRotatingBarcodeTotpDetails::is_period_millis_Set() const{
    return m_period_millis_isSet;
}

bool OAIRotatingBarcodeTotpDetails::is_period_millis_Valid() const{
    return m_period_millis_isValid;
}

bool OAIRotatingBarcodeTotpDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_algorithm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parameters.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_period_millis_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRotatingBarcodeTotpDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
