/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHotelProduct_CancellationPolicy.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHotelProduct_CancellationPolicy::OAIHotelProduct_CancellationPolicy(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHotelProduct_CancellationPolicy::OAIHotelProduct_CancellationPolicy() {
    this->initializeModel();
}

OAIHotelProduct_CancellationPolicy::~OAIHotelProduct_CancellationPolicy() {}

void OAIHotelProduct_CancellationPolicy::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_deadline_isSet = false;
    m_deadline_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_number_of_nights_isSet = false;
    m_number_of_nights_isValid = false;

    m_percentage_isSet = false;
    m_percentage_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIHotelProduct_CancellationPolicy::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHotelProduct_CancellationPolicy::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_deadline_isValid = ::OpenAPI::fromJsonValue(m_deadline, json[QString("deadline")]);
    m_deadline_isSet = !json[QString("deadline")].isNull() && m_deadline_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_number_of_nights_isValid = ::OpenAPI::fromJsonValue(m_number_of_nights, json[QString("numberOfNights")]);
    m_number_of_nights_isSet = !json[QString("numberOfNights")].isNull() && m_number_of_nights_isValid;

    m_percentage_isValid = ::OpenAPI::fromJsonValue(m_percentage, json[QString("percentage")]);
    m_percentage_isSet = !json[QString("percentage")].isNull() && m_percentage_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIHotelProduct_CancellationPolicy::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHotelProduct_CancellationPolicy::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_deadline_isSet) {
        obj.insert(QString("deadline"), ::OpenAPI::toJsonValue(m_deadline));
    }
    if (m_description.isSet()) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_number_of_nights_isSet) {
        obj.insert(QString("numberOfNights"), ::OpenAPI::toJsonValue(m_number_of_nights));
    }
    if (m_percentage_isSet) {
        obj.insert(QString("percentage"), ::OpenAPI::toJsonValue(m_percentage));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIHotelProduct_CancellationPolicy::getAmount() const {
    return m_amount;
}
void OAIHotelProduct_CancellationPolicy::setAmount(const QString &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIHotelProduct_CancellationPolicy::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIHotelProduct_CancellationPolicy::is_amount_Valid() const{
    return m_amount_isValid;
}

QDateTime OAIHotelProduct_CancellationPolicy::getDeadline() const {
    return m_deadline;
}
void OAIHotelProduct_CancellationPolicy::setDeadline(const QDateTime &deadline) {
    m_deadline = deadline;
    m_deadline_isSet = true;
}

bool OAIHotelProduct_CancellationPolicy::is_deadline_Set() const{
    return m_deadline_isSet;
}

bool OAIHotelProduct_CancellationPolicy::is_deadline_Valid() const{
    return m_deadline_isValid;
}

OAIQualifiedFreeText OAIHotelProduct_CancellationPolicy::getDescription() const {
    return m_description;
}
void OAIHotelProduct_CancellationPolicy::setDescription(const OAIQualifiedFreeText &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIHotelProduct_CancellationPolicy::is_description_Set() const{
    return m_description_isSet;
}

bool OAIHotelProduct_CancellationPolicy::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIHotelProduct_CancellationPolicy::getNumberOfNights() const {
    return m_number_of_nights;
}
void OAIHotelProduct_CancellationPolicy::setNumberOfNights(const qint32 &number_of_nights) {
    m_number_of_nights = number_of_nights;
    m_number_of_nights_isSet = true;
}

bool OAIHotelProduct_CancellationPolicy::is_number_of_nights_Set() const{
    return m_number_of_nights_isSet;
}

bool OAIHotelProduct_CancellationPolicy::is_number_of_nights_Valid() const{
    return m_number_of_nights_isValid;
}

QString OAIHotelProduct_CancellationPolicy::getPercentage() const {
    return m_percentage;
}
void OAIHotelProduct_CancellationPolicy::setPercentage(const QString &percentage) {
    m_percentage = percentage;
    m_percentage_isSet = true;
}

bool OAIHotelProduct_CancellationPolicy::is_percentage_Set() const{
    return m_percentage_isSet;
}

bool OAIHotelProduct_CancellationPolicy::is_percentage_Valid() const{
    return m_percentage_isValid;
}

OAICancellationType OAIHotelProduct_CancellationPolicy::getType() const {
    return m_type;
}
void OAIHotelProduct_CancellationPolicy::setType(const OAICancellationType &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIHotelProduct_CancellationPolicy::is_type_Set() const{
    return m_type_isSet;
}

bool OAIHotelProduct_CancellationPolicy::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIHotelProduct_CancellationPolicy::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deadline_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_nights_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHotelProduct_CancellationPolicy::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
