/**
 * EVEMarketer Marketstat API
 * EVEMarketer Marketstat API is almost compatible with EVE-Central's Marketstat API.
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExecAPI.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExecAPI::OAIExecAPI(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExecAPI::OAIExecAPI() {
    this->initializeModel();
}

OAIExecAPI::~OAIExecAPI() {}

void OAIExecAPI::initializeModel() {

    m_marketstat_isSet = false;
    m_marketstat_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIExecAPI::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExecAPI::fromJsonObject(QJsonObject json) {

    m_marketstat_isValid = ::OpenAPI::fromJsonValue(m_marketstat, json[QString("marketstat")]);
    m_marketstat_isSet = !json[QString("marketstat")].isNull() && m_marketstat_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIExecAPI::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExecAPI::asJsonObject() const {
    QJsonObject obj;
    if (m_marketstat.size() > 0) {
        obj.insert(QString("marketstat"), ::OpenAPI::toJsonValue(m_marketstat));
    }
    if (m_method_isSet) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QList<OAIMarketStatXML_inner> OAIExecAPI::getMarketstat() const {
    return m_marketstat;
}
void OAIExecAPI::setMarketstat(const QList<OAIMarketStatXML_inner> &marketstat) {
    m_marketstat = marketstat;
    m_marketstat_isSet = true;
}

bool OAIExecAPI::is_marketstat_Set() const{
    return m_marketstat_isSet;
}

bool OAIExecAPI::is_marketstat_Valid() const{
    return m_marketstat_isValid;
}

QString OAIExecAPI::getMethod() const {
    return m_method;
}
void OAIExecAPI::setMethod(const QString &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIExecAPI::is_method_Set() const{
    return m_method_isSet;
}

bool OAIExecAPI::is_method_Valid() const{
    return m_method_isValid;
}

QString OAIExecAPI::getVersion() const {
    return m_version;
}
void OAIExecAPI::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIExecAPI::is_version_Set() const{
    return m_version_isSet;
}

bool OAIExecAPI::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIExecAPI::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_marketstat.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExecAPI::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
