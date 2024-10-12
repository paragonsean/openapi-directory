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

#include "OAIAvailability_mixin.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailability_mixin::OAIAvailability_mixin(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailability_mixin::OAIAvailability_mixin() {
    this->initializeModel();
}

OAIAvailability_mixin::~OAIAvailability_mixin() {}

void OAIAvailability_mixin::initializeModel() {

    m_availability_isSet = false;
    m_availability_isValid = false;
}

void OAIAvailability_mixin::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailability_mixin::fromJsonObject(QJsonObject json) {

    m_availability_isValid = ::OpenAPI::fromJsonValue(m_availability, json[QString("availability")]);
    m_availability_isSet = !json[QString("availability")].isNull() && m_availability_isValid;
}

QString OAIAvailability_mixin::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailability_mixin::asJsonObject() const {
    QJsonObject obj;
    if (m_availability.size() > 0) {
        obj.insert(QString("availability"), ::OpenAPI::toJsonValue(m_availability));
    }
    return obj;
}

QList<OAIAvailability_mixin_availability_inner> OAIAvailability_mixin::getAvailability() const {
    return m_availability;
}
void OAIAvailability_mixin::setAvailability(const QList<OAIAvailability_mixin_availability_inner> &availability) {
    m_availability = availability;
    m_availability_isSet = true;
}

bool OAIAvailability_mixin::is_availability_Set() const{
    return m_availability_isSet;
}

bool OAIAvailability_mixin::is_availability_Valid() const{
    return m_availability_isValid;
}

bool OAIAvailability_mixin::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_availability.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailability_mixin::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
