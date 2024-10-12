/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProofOfAddress.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProofOfAddress::OAIProofOfAddress(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProofOfAddress::OAIProofOfAddress() {
    this->initializeModel();
}

OAIProofOfAddress::~OAIProofOfAddress() {}

void OAIProofOfAddress::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_document_subtype_isSet = false;
    m_document_subtype_isValid = false;

    m_document_type_isSet = false;
    m_document_type_isValid = false;

    m_file_id_isSet = false;
    m_file_id_isValid = false;

    m_file_ids_isSet = false;
    m_file_ids_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_processed_time_isSet = false;
    m_processed_time_isValid = false;

    m_rejection_reason_isSet = false;
    m_rejection_reason_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_match_level_isSet = false;
    m_match_level_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_review_time_isSet = false;
    m_review_time_isValid = false;

    m_reviewer_id_isSet = false;
    m_reviewer_id_isValid = false;

    m_reviewer_name_isSet = false;
    m_reviewer_name_isValid = false;

    m_document_matches_isSet = false;
    m_document_matches_isValid = false;

    m_parsed_data_isSet = false;
    m_parsed_data_isValid = false;
}

void OAIProofOfAddress::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProofOfAddress::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_document_subtype_isValid = ::OpenAPI::fromJsonValue(m_document_subtype, json[QString("documentSubtype")]);
    m_document_subtype_isSet = !json[QString("documentSubtype")].isNull() && m_document_subtype_isValid;

    m_document_type_isValid = ::OpenAPI::fromJsonValue(m_document_type, json[QString("documentType")]);
    m_document_type_isSet = !json[QString("documentType")].isNull() && m_document_type_isValid;

    m_file_id_isValid = ::OpenAPI::fromJsonValue(m_file_id, json[QString("fileId")]);
    m_file_id_isSet = !json[QString("fileId")].isNull() && m_file_id_isValid;

    m_file_ids_isValid = ::OpenAPI::fromJsonValue(m_file_ids, json[QString("fileIds")]);
    m_file_ids_isSet = !json[QString("fileIds")].isNull() && m_file_ids_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_processed_time_isValid = ::OpenAPI::fromJsonValue(m_processed_time, json[QString("processedTime")]);
    m_processed_time_isSet = !json[QString("processedTime")].isNull() && m_processed_time_isValid;

    m_rejection_reason_isValid = ::OpenAPI::fromJsonValue(m_rejection_reason, json[QString("rejectionReason")]);
    m_rejection_reason_isSet = !json[QString("rejectionReason")].isNull() && m_rejection_reason_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_match_level_isValid = ::OpenAPI::fromJsonValue(m_match_level, json[QString("matchLevel")]);
    m_match_level_isSet = !json[QString("matchLevel")].isNull() && m_match_level_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_review_time_isValid = ::OpenAPI::fromJsonValue(m_review_time, json[QString("reviewTime")]);
    m_review_time_isSet = !json[QString("reviewTime")].isNull() && m_review_time_isValid;

    m_reviewer_id_isValid = ::OpenAPI::fromJsonValue(m_reviewer_id, json[QString("reviewerId")]);
    m_reviewer_id_isSet = !json[QString("reviewerId")].isNull() && m_reviewer_id_isValid;

    m_reviewer_name_isValid = ::OpenAPI::fromJsonValue(m_reviewer_name, json[QString("reviewerName")]);
    m_reviewer_name_isSet = !json[QString("reviewerName")].isNull() && m_reviewer_name_isValid;

    m_document_matches_isValid = ::OpenAPI::fromJsonValue(m_document_matches, json[QString("documentMatches")]);
    m_document_matches_isSet = !json[QString("documentMatches")].isNull() && m_document_matches_isValid;

    m_parsed_data_isValid = ::OpenAPI::fromJsonValue(m_parsed_data, json[QString("parsedData")]);
    m_parsed_data_isSet = !json[QString("parsedData")].isNull() && m_parsed_data_isValid;
}

QString OAIProofOfAddress::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProofOfAddress::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_document_subtype.isSet()) {
        obj.insert(QString("documentSubtype"), ::OpenAPI::toJsonValue(m_document_subtype));
    }
    if (m_document_type.isSet()) {
        obj.insert(QString("documentType"), ::OpenAPI::toJsonValue(m_document_type));
    }
    if (m_file_id_isSet) {
        obj.insert(QString("fileId"), ::OpenAPI::toJsonValue(m_file_id));
    }
    if (m_file_ids.size() > 0) {
        obj.insert(QString("fileIds"), ::OpenAPI::toJsonValue(m_file_ids));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_processed_time_isSet) {
        obj.insert(QString("processedTime"), ::OpenAPI::toJsonValue(m_processed_time));
    }
    if (m_rejection_reason.isSet()) {
        obj.insert(QString("rejectionReason"), ::OpenAPI::toJsonValue(m_rejection_reason));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_match_level_isSet) {
        obj.insert(QString("matchLevel"), ::OpenAPI::toJsonValue(m_match_level));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_review_time_isSet) {
        obj.insert(QString("reviewTime"), ::OpenAPI::toJsonValue(m_review_time));
    }
    if (m_reviewer_id_isSet) {
        obj.insert(QString("reviewerId"), ::OpenAPI::toJsonValue(m_reviewer_id));
    }
    if (m_reviewer_name_isSet) {
        obj.insert(QString("reviewerName"), ::OpenAPI::toJsonValue(m_reviewer_name));
    }
    if (m_document_matches.isSet()) {
        obj.insert(QString("documentMatches"), ::OpenAPI::toJsonValue(m_document_matches));
    }
    if (m_parsed_data.isSet()) {
        obj.insert(QString("parsedData"), ::OpenAPI::toJsonValue(m_parsed_data));
    }
    return obj;
}

QList<OAIProofOfAddress_allOf__links> OAIProofOfAddress::getLinks() const {
    return m__links;
}
void OAIProofOfAddress::setLinks(const QList<OAIProofOfAddress_allOf__links> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIProofOfAddress::is__links_Set() const{
    return m__links_isSet;
}

bool OAIProofOfAddress::is__links_Valid() const{
    return m__links_isValid;
}

QDateTime OAIProofOfAddress::getCreatedTime() const {
    return m_created_time;
}
void OAIProofOfAddress::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIProofOfAddress::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIProofOfAddress::is_created_time_Valid() const{
    return m_created_time_isValid;
}

OAIKycDocumentSubtypes OAIProofOfAddress::getDocumentSubtype() const {
    return m_document_subtype;
}
void OAIProofOfAddress::setDocumentSubtype(const OAIKycDocumentSubtypes &document_subtype) {
    m_document_subtype = document_subtype;
    m_document_subtype_isSet = true;
}

bool OAIProofOfAddress::is_document_subtype_Set() const{
    return m_document_subtype_isSet;
}

bool OAIProofOfAddress::is_document_subtype_Valid() const{
    return m_document_subtype_isValid;
}

OAIKycDocumentTypes OAIProofOfAddress::getDocumentType() const {
    return m_document_type;
}
void OAIProofOfAddress::setDocumentType(const OAIKycDocumentTypes &document_type) {
    m_document_type = document_type;
    m_document_type_isSet = true;
}

bool OAIProofOfAddress::is_document_type_Set() const{
    return m_document_type_isSet;
}

bool OAIProofOfAddress::is_document_type_Valid() const{
    return m_document_type_isValid;
}

QString OAIProofOfAddress::getFileId() const {
    return m_file_id;
}
void OAIProofOfAddress::setFileId(const QString &file_id) {
    m_file_id = file_id;
    m_file_id_isSet = true;
}

bool OAIProofOfAddress::is_file_id_Set() const{
    return m_file_id_isSet;
}

bool OAIProofOfAddress::is_file_id_Valid() const{
    return m_file_id_isValid;
}

QList<QString> OAIProofOfAddress::getFileIds() const {
    return m_file_ids;
}
void OAIProofOfAddress::setFileIds(const QList<QString> &file_ids) {
    m_file_ids = file_ids;
    m_file_ids_isSet = true;
}

bool OAIProofOfAddress::is_file_ids_Set() const{
    return m_file_ids_isSet;
}

bool OAIProofOfAddress::is_file_ids_Valid() const{
    return m_file_ids_isValid;
}

QString OAIProofOfAddress::getId() const {
    return m_id;
}
void OAIProofOfAddress::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProofOfAddress::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProofOfAddress::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIProofOfAddress::getProcessedTime() const {
    return m_processed_time;
}
void OAIProofOfAddress::setProcessedTime(const QDateTime &processed_time) {
    m_processed_time = processed_time;
    m_processed_time_isSet = true;
}

bool OAIProofOfAddress::is_processed_time_Set() const{
    return m_processed_time_isSet;
}

bool OAIProofOfAddress::is_processed_time_Valid() const{
    return m_processed_time_isValid;
}

OAIKycDocumentRejection OAIProofOfAddress::getRejectionReason() const {
    return m_rejection_reason;
}
void OAIProofOfAddress::setRejectionReason(const OAIKycDocumentRejection &rejection_reason) {
    m_rejection_reason = rejection_reason;
    m_rejection_reason_isSet = true;
}

bool OAIProofOfAddress::is_rejection_reason_Set() const{
    return m_rejection_reason_isSet;
}

bool OAIProofOfAddress::is_rejection_reason_Valid() const{
    return m_rejection_reason_isValid;
}

QString OAIProofOfAddress::getRequestId() const {
    return m_request_id;
}
void OAIProofOfAddress::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIProofOfAddress::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIProofOfAddress::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QString OAIProofOfAddress::getStatus() const {
    return m_status;
}
void OAIProofOfAddress::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIProofOfAddress::is_status_Set() const{
    return m_status_isSet;
}

bool OAIProofOfAddress::is_status_Valid() const{
    return m_status_isValid;
}

QDateTime OAIProofOfAddress::getUpdatedTime() const {
    return m_updated_time;
}
void OAIProofOfAddress::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIProofOfAddress::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIProofOfAddress::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QString OAIProofOfAddress::getCustomerId() const {
    return m_customer_id;
}
void OAIProofOfAddress::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIProofOfAddress::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIProofOfAddress::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

qint32 OAIProofOfAddress::getMatchLevel() const {
    return m_match_level;
}
void OAIProofOfAddress::setMatchLevel(const qint32 &match_level) {
    m_match_level = match_level;
    m_match_level_isSet = true;
}

bool OAIProofOfAddress::is_match_level_Set() const{
    return m_match_level_isSet;
}

bool OAIProofOfAddress::is_match_level_Valid() const{
    return m_match_level_isValid;
}

QString OAIProofOfAddress::getNotes() const {
    return m_notes;
}
void OAIProofOfAddress::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIProofOfAddress::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIProofOfAddress::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAIProofOfAddress::getReason() const {
    return m_reason;
}
void OAIProofOfAddress::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIProofOfAddress::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIProofOfAddress::is_reason_Valid() const{
    return m_reason_isValid;
}

QDateTime OAIProofOfAddress::getReviewTime() const {
    return m_review_time;
}
void OAIProofOfAddress::setReviewTime(const QDateTime &review_time) {
    m_review_time = review_time;
    m_review_time_isSet = true;
}

bool OAIProofOfAddress::is_review_time_Set() const{
    return m_review_time_isSet;
}

bool OAIProofOfAddress::is_review_time_Valid() const{
    return m_review_time_isValid;
}

QString OAIProofOfAddress::getReviewerId() const {
    return m_reviewer_id;
}
void OAIProofOfAddress::setReviewerId(const QString &reviewer_id) {
    m_reviewer_id = reviewer_id;
    m_reviewer_id_isSet = true;
}

bool OAIProofOfAddress::is_reviewer_id_Set() const{
    return m_reviewer_id_isSet;
}

bool OAIProofOfAddress::is_reviewer_id_Valid() const{
    return m_reviewer_id_isValid;
}

QString OAIProofOfAddress::getReviewerName() const {
    return m_reviewer_name;
}
void OAIProofOfAddress::setReviewerName(const QString &reviewer_name) {
    m_reviewer_name = reviewer_name;
    m_reviewer_name_isSet = true;
}

bool OAIProofOfAddress::is_reviewer_name_Set() const{
    return m_reviewer_name_isSet;
}

bool OAIProofOfAddress::is_reviewer_name_Valid() const{
    return m_reviewer_name_isValid;
}

OAIProofOfAddress_allOf_documentMatches OAIProofOfAddress::getDocumentMatches() const {
    return m_document_matches;
}
void OAIProofOfAddress::setDocumentMatches(const OAIProofOfAddress_allOf_documentMatches &document_matches) {
    m_document_matches = document_matches;
    m_document_matches_isSet = true;
}

bool OAIProofOfAddress::is_document_matches_Set() const{
    return m_document_matches_isSet;
}

bool OAIProofOfAddress::is_document_matches_Valid() const{
    return m_document_matches_isValid;
}

OAIProofOfAddress_allOf_documentMatches OAIProofOfAddress::getParsedData() const {
    return m_parsed_data;
}
void OAIProofOfAddress::setParsedData(const OAIProofOfAddress_allOf_documentMatches &parsed_data) {
    m_parsed_data = parsed_data;
    m_parsed_data_isSet = true;
}

bool OAIProofOfAddress::is_parsed_data_Set() const{
    return m_parsed_data_isSet;
}

bool OAIProofOfAddress::is_parsed_data_Valid() const{
    return m_parsed_data_isValid;
}

bool OAIProofOfAddress::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_subtype.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_processed_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rejection_reason.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_match_level_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_review_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reviewer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reviewer_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_matches.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parsed_data.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProofOfAddress::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_document_type_isValid && m_status_isValid && m_customer_id_isValid && true;
}

} // namespace OpenAPI
