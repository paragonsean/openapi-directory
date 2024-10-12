/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITax.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITax::OAITax(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITax::OAITax() {
    this->initializeModel();
}

OAITax::~OAITax() {}

void OAITax::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;
}

void OAITax::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITax::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;
}

QString OAITax::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITax::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    return obj;
}

QString OAITax::getAmount() const {
    return m_amount;
}
void OAITax::setAmount(const QString &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAITax::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAITax::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAITax::getCode() const {
    return m_code;
}
void OAITax::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAITax::is_code_Set() const{
    return m_code_isSet;
}

bool OAITax::is_code_Valid() const{
    return m_code_isValid;
}

bool OAITax::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITax::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
