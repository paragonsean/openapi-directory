/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVersion_availability_mixin.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVersion_availability_mixin::OAIVersion_availability_mixin(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVersion_availability_mixin::OAIVersion_availability_mixin() {
    this->initializeModel();
}

OAIVersion_availability_mixin::~OAIVersion_availability_mixin() {}

void OAIVersion_availability_mixin::initializeModel() {

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIVersion_availability_mixin::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVersion_availability_mixin::fromJsonObject(QJsonObject json) {

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIVersion_availability_mixin::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVersion_availability_mixin::asJsonObject() const {
    QJsonObject obj;
    if (m_version.size() > 0) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QList<OAIVersion_availability_mixin_version_inner> OAIVersion_availability_mixin::getVersion() const {
    return m_version;
}
void OAIVersion_availability_mixin::setVersion(const QList<OAIVersion_availability_mixin_version_inner> &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIVersion_availability_mixin::is_version_Set() const{
    return m_version_isSet;
}

bool OAIVersion_availability_mixin::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIVersion_availability_mixin::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_version.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVersion_availability_mixin::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
