/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVersions_Diagnostics.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVersions_Diagnostics::OAIVersions_Diagnostics(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVersions_Diagnostics::OAIVersions_Diagnostics() {
    this->initializeModel();
}

OAIVersions_Diagnostics::~OAIVersions_Diagnostics() {}

void OAIVersions_Diagnostics::initializeModel() {

    m_total_isSet = false;
    m_total_isValid = false;

    m_versions_isSet = false;
    m_versions_isValid = false;
}

void OAIVersions_Diagnostics::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVersions_Diagnostics::fromJsonObject(QJsonObject json) {

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_versions_isValid = ::OpenAPI::fromJsonValue(m_versions, json[QString("versions")]);
    m_versions_isSet = !json[QString("versions")].isNull() && m_versions_isValid;
}

QString OAIVersions_Diagnostics::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVersions_Diagnostics::asJsonObject() const {
    QJsonObject obj;
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_versions.size() > 0) {
        obj.insert(QString("versions"), ::OpenAPI::toJsonValue(m_versions));
    }
    return obj;
}

qint64 OAIVersions_Diagnostics::getTotal() const {
    return m_total;
}
void OAIVersions_Diagnostics::setTotal(const qint64 &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIVersions_Diagnostics::is_total_Set() const{
    return m_total_isSet;
}

bool OAIVersions_Diagnostics::is_total_Valid() const{
    return m_total_isValid;
}

QList<OAIVersions_Diagnostics_versions_inner> OAIVersions_Diagnostics::getVersions() const {
    return m_versions;
}
void OAIVersions_Diagnostics::setVersions(const QList<OAIVersions_Diagnostics_versions_inner> &versions) {
    m_versions = versions;
    m_versions_isSet = true;
}

bool OAIVersions_Diagnostics::is_versions_Set() const{
    return m_versions_isSet;
}

bool OAIVersions_Diagnostics::is_versions_Valid() const{
    return m_versions_isValid;
}

bool OAIVersions_Diagnostics::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_versions.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVersions_Diagnostics::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
