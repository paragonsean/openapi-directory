/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImportExportStats.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImportExportStats::OAIImportExportStats(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImportExportStats::OAIImportExportStats() {
    this->initializeModel();
}

OAIImportExportStats::~OAIImportExportStats() {}

void OAIImportExportStats::initializeModel() {

    m_calls_isSet = false;
    m_calls_isValid = false;

    m_data_in_isSet = false;
    m_data_in_isValid = false;

    m_data_out_isSet = false;
    m_data_out_isValid = false;
}

void OAIImportExportStats::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImportExportStats::fromJsonObject(QJsonObject json) {

    m_calls_isValid = ::OpenAPI::fromJsonValue(m_calls, json[QString("calls")]);
    m_calls_isSet = !json[QString("calls")].isNull() && m_calls_isValid;

    m_data_in_isValid = ::OpenAPI::fromJsonValue(m_data_in, json[QString("dataIn")]);
    m_data_in_isSet = !json[QString("dataIn")].isNull() && m_data_in_isValid;

    m_data_out_isValid = ::OpenAPI::fromJsonValue(m_data_out, json[QString("dataOut")]);
    m_data_out_isSet = !json[QString("dataOut")].isNull() && m_data_out_isValid;
}

QString OAIImportExportStats::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImportExportStats::asJsonObject() const {
    QJsonObject obj;
    if (m_calls_isSet) {
        obj.insert(QString("calls"), ::OpenAPI::toJsonValue(m_calls));
    }
    if (m_data_in_isSet) {
        obj.insert(QString("dataIn"), ::OpenAPI::toJsonValue(m_data_in));
    }
    if (m_data_out_isSet) {
        obj.insert(QString("dataOut"), ::OpenAPI::toJsonValue(m_data_out));
    }
    return obj;
}

qint64 OAIImportExportStats::getCalls() const {
    return m_calls;
}
void OAIImportExportStats::setCalls(const qint64 &calls) {
    m_calls = calls;
    m_calls_isSet = true;
}

bool OAIImportExportStats::is_calls_Set() const{
    return m_calls_isSet;
}

bool OAIImportExportStats::is_calls_Valid() const{
    return m_calls_isValid;
}

qint64 OAIImportExportStats::getDataIn() const {
    return m_data_in;
}
void OAIImportExportStats::setDataIn(const qint64 &data_in) {
    m_data_in = data_in;
    m_data_in_isSet = true;
}

bool OAIImportExportStats::is_data_in_Set() const{
    return m_data_in_isSet;
}

bool OAIImportExportStats::is_data_in_Valid() const{
    return m_data_in_isValid;
}

qint64 OAIImportExportStats::getDataOut() const {
    return m_data_out;
}
void OAIImportExportStats::setDataOut(const qint64 &data_out) {
    m_data_out = data_out;
    m_data_out_isSet = true;
}

bool OAIImportExportStats::is_data_out_Set() const{
    return m_data_out_isSet;
}

bool OAIImportExportStats::is_data_out_Valid() const{
    return m_data_out_isValid;
}

bool OAIImportExportStats::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_calls_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_out_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImportExportStats::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_calls_isValid && m_data_in_isValid && m_data_out_isValid && true;
}

} // namespace OpenAPI
