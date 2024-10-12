/**
 * Flight Busiest Traveling Period
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIssue_Source.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssue_Source::OAIIssue_Source(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssue_Source::OAIIssue_Source() {
    this->initializeModel();
}

OAIIssue_Source::~OAIIssue_Source() {}

void OAIIssue_Source::initializeModel() {

    m_example_isSet = false;
    m_example_isValid = false;

    m_parameter_isSet = false;
    m_parameter_isValid = false;

    m_pointer_isSet = false;
    m_pointer_isValid = false;
}

void OAIIssue_Source::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssue_Source::fromJsonObject(QJsonObject json) {

    m_example_isValid = ::OpenAPI::fromJsonValue(m_example, json[QString("example")]);
    m_example_isSet = !json[QString("example")].isNull() && m_example_isValid;

    m_parameter_isValid = ::OpenAPI::fromJsonValue(m_parameter, json[QString("parameter")]);
    m_parameter_isSet = !json[QString("parameter")].isNull() && m_parameter_isValid;

    m_pointer_isValid = ::OpenAPI::fromJsonValue(m_pointer, json[QString("pointer")]);
    m_pointer_isSet = !json[QString("pointer")].isNull() && m_pointer_isValid;
}

QString OAIIssue_Source::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssue_Source::asJsonObject() const {
    QJsonObject obj;
    if (m_example_isSet) {
        obj.insert(QString("example"), ::OpenAPI::toJsonValue(m_example));
    }
    if (m_parameter_isSet) {
        obj.insert(QString("parameter"), ::OpenAPI::toJsonValue(m_parameter));
    }
    if (m_pointer_isSet) {
        obj.insert(QString("pointer"), ::OpenAPI::toJsonValue(m_pointer));
    }
    return obj;
}

QString OAIIssue_Source::getExample() const {
    return m_example;
}
void OAIIssue_Source::setExample(const QString &example) {
    m_example = example;
    m_example_isSet = true;
}

bool OAIIssue_Source::is_example_Set() const{
    return m_example_isSet;
}

bool OAIIssue_Source::is_example_Valid() const{
    return m_example_isValid;
}

QString OAIIssue_Source::getParameter() const {
    return m_parameter;
}
void OAIIssue_Source::setParameter(const QString &parameter) {
    m_parameter = parameter;
    m_parameter_isSet = true;
}

bool OAIIssue_Source::is_parameter_Set() const{
    return m_parameter_isSet;
}

bool OAIIssue_Source::is_parameter_Valid() const{
    return m_parameter_isValid;
}

QString OAIIssue_Source::getPointer() const {
    return m_pointer;
}
void OAIIssue_Source::setPointer(const QString &pointer) {
    m_pointer = pointer;
    m_pointer_isSet = true;
}

bool OAIIssue_Source::is_pointer_Set() const{
    return m_pointer_isSet;
}

bool OAIIssue_Source::is_pointer_Valid() const{
    return m_pointer_isValid;
}

bool OAIIssue_Source::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_example_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parameter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pointer_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIssue_Source::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
