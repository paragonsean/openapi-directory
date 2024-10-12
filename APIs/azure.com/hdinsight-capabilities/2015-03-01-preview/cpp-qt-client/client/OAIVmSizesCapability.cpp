/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVmSizesCapability.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVmSizesCapability::OAIVmSizesCapability(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVmSizesCapability::OAIVmSizesCapability() {
    this->initializeModel();
}

OAIVmSizesCapability::~OAIVmSizesCapability() {}

void OAIVmSizesCapability::initializeModel() {

    m_available_isSet = false;
    m_available_isValid = false;
}

void OAIVmSizesCapability::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVmSizesCapability::fromJsonObject(QJsonObject json) {

    m_available_isValid = ::OpenAPI::fromJsonValue(m_available, json[QString("available")]);
    m_available_isSet = !json[QString("available")].isNull() && m_available_isValid;
}

QString OAIVmSizesCapability::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVmSizesCapability::asJsonObject() const {
    QJsonObject obj;
    if (m_available.size() > 0) {
        obj.insert(QString("available"), ::OpenAPI::toJsonValue(m_available));
    }
    return obj;
}

QList<QString> OAIVmSizesCapability::getAvailable() const {
    return m_available;
}
void OAIVmSizesCapability::setAvailable(const QList<QString> &available) {
    m_available = available;
    m_available_isSet = true;
}

bool OAIVmSizesCapability::is_available_Set() const{
    return m_available_isSet;
}

bool OAIVmSizesCapability::is_available_Valid() const{
    return m_available_isValid;
}

bool OAIVmSizesCapability::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVmSizesCapability::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
