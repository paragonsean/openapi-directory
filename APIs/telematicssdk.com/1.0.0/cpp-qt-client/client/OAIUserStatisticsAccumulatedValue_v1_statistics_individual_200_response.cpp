/**
 * Quick start - Telematics SDK
 * # Introduction We have prepared a set of APIs for quick start to integrate telematics SDK that powers mobile telematics inside 3rd party mobile applications.  * [CONTACT US](https://telematicssdk.com) * [SANDBOX](https://userdatahub.com) * [DEV.PORTAL](https://docs.telematicssdk.com) * [DEMO APP](https://raxeltelematics.com/telematics-app)   # Overview Datamotion provides telematics infrastructure for mobile applications.   Telematics SDK turns any smartphone into telematics data gathering device to collect Location, driving and behavior data. API services unlocks power of your mobile application  There are 3 groups of methods: * 1 - user management * 2 - statistics for mobile app * 3 - statistics for back-end(s)  in certain cases you will need SNS or any other notification services. read more [here](https://docs.telematicssdk.com/platform-features/sns) # Possible architecture  There are three common schemes that are used by our clients. These schemes can be combined * Collect, Process, Store (required: 1&2) * Collect, Process (required: 1& sns) * Collect (required 1&sns)   ## Collect, Process, Store ![Collect, Process, Store](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection%2C+processing%2C+storage)  ## Collect, Process ![Collect, Process](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+and+processing)  ## Collect ![Collect](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+only)  *** ![Telematic sdk](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Github/transportation_small.png)  # Common use-cases: * Safe and efficient driving * Usage-based insurance * Safe driving assessment * Driver assessment * Trip log * Geo-analysis * Accident monitoring * Driving engagements * Location based services * Realtime Tracking and beyond  # How to start * Register a [SANDBOX ACCOUNT](https://userdatahub.com) * Get [CREDENTIALS](https://docs.userdatahub.com/sandbox/credentials)  * Follow the guide from [DEVELOPER POERTAL](https://docs.telematicssdk.com)  # Authentication To create a user on datamotion platform, you require to use InstanceID and InstanceKEY. You can get it in Datahub -> management -> user-service credentials  Once you create a user, you will get Device token, JWT token and refresh token. then, you will use it for APIs
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response() {
    this->initializeModel();
}

OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::~OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response() {}

void OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::initializeModel() {

    m_errors_isSet = false;
    m_errors_isValid = false;

    m_result_isSet = false;
    m_result_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::fromJsonObject(QJsonObject json) {

    m_errors_isValid = ::OpenAPI::fromJsonValue(m_errors, json[QString("Errors")]);
    m_errors_isSet = !json[QString("Errors")].isNull() && m_errors_isValid;

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("Result")]);
    m_result_isSet = !json[QString("Result")].isNull() && m_result_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("Title")]);
    m_title_isSet = !json[QString("Title")].isNull() && m_title_isValid;
}

QString OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_errors.size() > 0) {
        obj.insert(QString("Errors"), ::OpenAPI::toJsonValue(m_errors));
    }
    if (m_result.isSet()) {
        obj.insert(QString("Result"), ::OpenAPI::toJsonValue(m_result));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_title_isSet) {
        obj.insert(QString("Title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QList<QJsonValue> OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::getErrors() const {
    return m_errors;
}
void OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::setErrors(const QList<QJsonValue> &errors) {
    m_errors = errors;
    m_errors_isSet = true;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_errors_Set() const{
    return m_errors_isSet;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_errors_Valid() const{
    return m_errors_isValid;
}

OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response_Result OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::getResult() const {
    return m_result;
}
void OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::setResult(const OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response_Result &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_result_Set() const{
    return m_result_isSet;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_result_Valid() const{
    return m_result_isValid;
}

double OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::getStatus() const {
    return m_status;
}
void OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::setStatus(const double &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::getTitle() const {
    return m_title;
}
void OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_title_Set() const{
    return m_title_isSet;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_result.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserStatisticsAccumulatedValue_v1_statistics_individual_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
